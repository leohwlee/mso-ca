"""Verify the active 01–26 bank and recover the unchanged historical baseline.

The four earlier audit reports concern their original 23-source checklist.
This follow-up validates the current bank separately; old evidence is never
rewritten to pretend it reviewed later questions or a different source scope.
"""
import collections
import hashlib
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
RECORD = ROOT / 'bank/audit/active26-implementation.json'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def review_text(q):
    return {'id': q['id'], 'module': q['module'], 'source': q['source'],
            **{lang: {k:q[lang][k] for k in ('q', 'statements')} for lang in ('en','tc')}}


def text_hash(q):
    return digest(json.dumps(review_text(q), ensure_ascii=False, sort_keys=True).encode())


def recover(bank, quotes):
    if not RECORD.exists():
        return bank, quotes, set()
    d = json.loads(RECORD.read_text(encoding='utf8'))
    assert d['status'] == 'verified', 'Active bank review is incomplete'
    archive_path = ROOT / d['archive']
    assert digest(archive_path.read_bytes()) == d['archive_sha256'], 'Baseline archive changed'
    proven = set()
    with zipfile.ZipFile(archive_path) as archive:
        old_bank = json.loads(archive.read('web/questions.json'))
        old_quotes = json.loads(archive.read('docs/quotes.json'))
        for p in ('web/questions.json','docs/quotes.json'):
            raw = archive.read(p)
            for data in (raw, raw.replace(b'\r\n',b'\n'), raw.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')):
                proven.add((p,digest(data)))
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
    approved = {f'{n:02d}' for n in range(1,27)}
    assert set(d['approved_documents']) == approved
    for qid,sides in quotes.items():
        assert all(q['doc'] in approved for side in sides.values() for q in side), qid
    assert dict(collections.Counter(str(q['module']) for q in bank)) == d['module_counts']
    reviews = d['blind_review']['items']
    assert len(reviews) == len(added)
    assert {r['answer']['id'] for r in reviews} == added
    for r in reviews:
        a = r['answer']; q = current[a['id']]
        assert text_hash(q) == r['reviewed_text_sha256'], f'Stale blind review: {q["id"]}'
        expected = ['T' if v else 'F' for v in q['truth']]
        assert a['verdicts'] == a['tc_verdicts'] == expected, q['id']
        assert not any(a.get('doubts',[])) and not any(a.get('tc_mismatch',[])), q['id']
        assert len(a['quotes']) == len(expected) and all(a['quotes']), q['id']
    mappings = d['coverage']
    assert {r['question_id'] for r in mappings} == added
    for r in mappings:
        assert r['topic'] and r['locator'] and set(r['documents']) <= approved, r
        cited = {x['doc'] for side in quotes[r['question_id']].values() for x in side}
        assert set(r['documents']) <= cited, r
    expected_texts = {f'docs/text/{lang}/{n:02d}.txt'
                      for lang in ('EN', 'TC') for n in range(1, 27)}
    assert set(d['source_text_sha256']) == expected_texts, 'Incomplete source-version bindings'
    for p, sha in d['source_text_sha256'].items():
        assert digest((ROOT/p).read_bytes().replace(b'\r\n',b'\n')) == sha, p
    return old_bank, old_quotes, proven


def main():
    bank = json.loads((ROOT/'web/questions.json').read_text(encoding='utf8'))
    quotes = json.loads((ROOT/'docs/quotes.json').read_text(encoding='utf8'))
    assert RECORD.exists(), 'Active scope review record is missing'
    old, _, _ = recover(bank,quotes)
    print(json.dumps({'questions':len(bank),'baseline_questions':len(old),
                      'approved_documents':'01–26',
                      'module_counts':dict(collections.Counter(q['module'] for q in bank))},ensure_ascii=False))


if __name__ == '__main__':
    main()
