"""Verify the active bank and recover the unchanged historical baseline.

The four earlier audit reports concern their original 23-source checklist.
This follow-up validates the current bank separately; old evidence is never
rewritten to pretend it reviewed later questions or a different source scope.

Later reviewed changes to the active bank are recorded in active-followups/,
one record per change with an archive of the bank it started from. They are
unwound newest first, each checked against its own blind reviews, until the
bank the active26 record describes is rebuilt; that record is then checked
exactly as before.
"""
import collections
import hashlib
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
RECORD = ROOT / 'bank/audit/active26-implementation.json'
FOLLOWUPS = ROOT / 'bank/audit/active-followups'
APPROVED = {f'{n:02d}' for n in range(1, 27)}  # source texts 01–26 remain on disk


def question_scope():
    """Documents allowed in live and newly authored questions (catalog question_bank_scope)."""
    catalog = json.loads((ROOT / 'docs/catalog.json').read_text(encoding='utf8'))
    return set(catalog['question_bank_scope']['documents'])


def digest(data):
    return hashlib.sha256(data).hexdigest()


def review_text(q):
    return {'id': q['id'], 'module': q['module'], 'source': q['source'],
            **{lang: {k:q[lang][k] for k in ('q', 'statements')} for lang in ('en','tc')}}


def text_hash(q):
    return digest(json.dumps(review_text(q), ensure_ascii=False, sort_keys=True).encode())


def check_review(r, q):
    """A blind answer bound to the item's final text, agreeing with its key in both languages.

    A reviewer's doubt may stand only beside the author's recorded resolution of
    it; the answer itself is kept as the reviewer gave it."""
    a = r['answer']
    assert text_hash(q) == r['reviewed_text_sha256'], f'Stale blind review: {q["id"]}'
    expected = ['T' if v else 'F' for v in q['truth']]
    assert a['verdicts'] == a['tc_verdicts'] == expected, q['id']
    resolved = r.get('resolutions', [])
    for i, doubt in enumerate(a.get('doubts',[])):
        assert not doubt or (i < len(resolved) and resolved[i]), f'Unresolved reviewer doubt: {q["id"]}'
    assert not any(a.get('tc_mismatch',[])), q['id']
    assert len(a['quotes']) == len(expected) and all(a['quotes']), q['id']


def check_source_texts(d):
    expected_texts = {f'docs/text/{lang}/{n:02d}.txt'
                      for lang in ('EN', 'TC') for n in range(1, 27)}
    assert set(d['source_text_sha256']) == expected_texts, 'Incomplete source-version bindings'
    for p, sha in d['source_text_sha256'].items():
        assert digest((ROOT/p).read_bytes().replace(b'\r\n',b'\n')) == sha, p


def check_reviews(d, current, quotes, reviewed, mapped):
    """Every reviewed item has a blind review bound to its final text, every added item a
    topic mapping naming only documents it cites, and the source texts are the reviewed ones."""
    reviews = d['blind_review']['items']
    assert len(reviews) == len(reviewed)
    assert {r['answer']['id'] for r in reviews} == reviewed
    for r in reviews:
        check_review(r, current[r['answer']['id']])
    assert {r['question_id'] for r in d['coverage']} == mapped
    for r in d['coverage']:
        assert r['topic'] and r['locator'] and set(r['documents']) <= APPROVED, r
        cited = {x['doc'] for side in quotes[r['question_id']].values() for x in side}
        assert set(r['documents']) <= cited, r
    check_source_texts(d)


def archived_bank(d, proven):
    archive_path = ROOT / d['archive']
    assert digest(archive_path.read_bytes()) == d['archive_sha256'], f'Archive changed: {d["archive"]}'
    with zipfile.ZipFile(archive_path) as archive:
        old_bank = json.loads(archive.read('web/questions.json'))
        old_quotes = json.loads(archive.read('docs/quotes.json'))
        for p in ('web/questions.json','docs/quotes.json'):
            raw = archive.read(p)
            for data in (raw, raw.replace(b'\r\n',b'\n'), raw.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')):
                proven.add((p,digest(data)))
    return old_bank, old_quotes


def unwind(d, bank, quotes, proven, later_retired=None):
    """Check one follow-up against the live bank; return the bank it started from.

    Added items leave; revised items return to their archived text and quotes.
    Retired items are restored from the follow-up archive. Every other item
    passes through unchanged, so an unreviewed edit still meets the checks of
    whichever record last reviewed it. Empty added and revised lists are allowed.
    IDs retired by a newer follow-up may now be in retired-ids.json even if this
    older record originally added them."""
    assert d['status'] == 'verified', 'Follow-up review is incomplete'
    old_bank, old_quotes = archived_bank(d, proven)
    before = {q['id']:q for q in old_bank}
    current = {q['id']:q for q in bank}
    assert len(current) == len(bank) == d['questions']
    assert set(quotes) == set(current)
    added = set(d['added_question_ids']); revised = set(d['revised_question_ids'])
    retired = set(d.get('retired_ids', []))
    assert len(added) == len(d['added_question_ids']) and len(revised) == len(d['revised_question_ids'])
    assert len(retired) == len(d.get('retired_ids', []))
    assert added.isdisjoint(before) and revised <= before.keys()
    assert retired <= before.keys()
    assert added.isdisjoint(revised) and added.isdisjoint(retired) and revised.isdisjoint(retired)
    assert current.keys() == (before.keys() - retired) | added
    reserved = set(json.loads((ROOT/'bank/retired-ids.json').read_text(encoding='utf8'))['ids'])
    later_retired = set(later_retired or [])
    assert added.isdisjoint(reserved - later_retired)
    assert retired <= reserved and retired.isdisjoint(current)
    assert dict(collections.Counter(str(q['module']) for q in bank)) == d['module_counts']
    for qid in revised:
        assert (current[qid], quotes[qid]) != (before[qid], old_quotes[qid]), f'Revision changes nothing: {qid}'
    for qid in added | revised:
        assert all(x['doc'] in APPROVED for side in quotes[qid].values() for x in side), qid
    for qid in current.keys() - added - revised:
        assert current[qid] == before[qid], f'Unreviewed old question edit: {qid}'
        assert quotes[qid] == old_quotes[qid], f'Unreviewed old quote edit: {qid}'
    check_reviews(d, current, quotes, added | revised, added)
    # Restore retired items from the archive; drop added; revert revised.
    return old_bank, old_quotes


def followups():
    if not FOLLOWUPS.exists():
        return []
    return [json.loads(p.read_text(encoding='utf8')) for p in sorted(FOLLOWUPS.glob('*.json'), reverse=True)]


def check_live_quotes(quotes):
    """The live bank may only cite the current question_bank_scope allowlist."""
    allow = question_scope()
    for qid, sides in quotes.items():
        assert all(x['doc'] in allow for side in sides.values() for x in side), f'outside the approved 01–24 and 26 scope: {qid}'


def recover(bank, quotes):
    if not RECORD.exists():
        return bank, quotes, set()
    check_live_quotes(quotes)
    later = set()
    later_retired = set()
    for record in followups():
        bank, quotes = unwind(record, bank, quotes, later, later_retired)
        later_retired |= set(record.get('retired_ids', []))
    old_bank, old_quotes, proven = recover_active26(bank, quotes)
    return old_bank, old_quotes, proven | later


def recover_active26(bank, quotes):
    d = json.loads(RECORD.read_text(encoding='utf8'))
    assert d['status'] == 'verified', 'Active bank review is incomplete'
    proven = set()
    old_bank, old_quotes = archived_bank(d, proven)
    before = {q['id']:q for q in old_bank}
    current = {q['id']:q for q in bank}
    assert len(current) == len(bank) == d['questions']
    assert set(quotes) == set(current)
    retired = set(d['retired_ids']); added = set(d['added_question_ids'])
    assert added.isdisjoint(before)
    assert retired <= before.keys()
    assert current.keys() == (before.keys() - retired) | added
    reserved = json.loads((ROOT/'bank/retired-ids.json').read_text(encoding='utf8'))['ids']
    assert retired <= set(reserved) and retired.isdisjoint(current)
    for qid in before.keys() - retired:
        assert current[qid] == before[qid], f'Unreviewed old question edit: {qid}'
        assert quotes[qid] == old_quotes[qid], f'Unreviewed old quote edit: {qid}'
    assert set(d['approved_documents']) == APPROVED
    for qid,sides in quotes.items():
        assert all(q['doc'] in APPROVED for side in sides.values() for q in side), qid
    assert dict(collections.Counter(str(q['module']) for q in bank)) == d['module_counts']
    check_reviews(d, current, quotes, added, added)
    return old_bank, old_quotes, proven


def main():
    bank = json.loads((ROOT/'web/questions.json').read_text(encoding='utf8'))
    quotes = json.loads((ROOT/'docs/quotes.json').read_text(encoding='utf8'))
    assert RECORD.exists(), 'Active scope review record is missing'
    old, _, _ = recover(bank,quotes)
    print(json.dumps({'questions':len(bank),'baseline_questions':len(old),
                      'reviewed_followups':len(followups()),
                      'source_texts':'01–26',
                      'question_scope':sorted(question_scope()),                      'module_counts':dict(collections.Counter(q['module'] for q in bank))},ensure_ascii=False))


if __name__ == '__main__':
    main()
