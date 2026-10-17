"""Keep audit baselines verifiable after reviewed additions and replacements."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent

def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def check_hash(path, expected):
    data = (ROOT / path).read_bytes()
    variants = [data]
    if pathlib.Path(path).suffix.lower() in {'.json', '.md', '.py', '.txt', '.go'}:
        # Git uses LF in the index and may check text out as CRLF on Windows.
        # Permit only this byte-level conversion, never a content change.
        lf = data.replace(b'\r\n', b'\n')
        variants.extend([lf, lf.replace(b'\n', b'\r\n')])
    assert any(hashlib.sha256(value).hexdigest() == expected for value in variants), f'Snapshot changed: {path}'

def encoded(value, newline):
    return (json.dumps(value, ensure_ascii=False, indent=1) + '\n').replace('\n', newline).encode('utf8')

def load_state():
    bank = json.loads((ROOT / 'web/questions.json').read_text(encoding='utf8'))
    quotes = json.loads((ROOT / 'docs/quotes.json').read_text(encoding='utf8'))
    current = {q['id']: q for q in bank}
    path = HERE / 'implementation.json'
    if not path.exists():
        return dict(bank=bank, current=current, evidence=current, implementation=None, historical_hashes={})
    d = json.loads(path.read_text(encoding='utf8'))
    assert d['status'] == 'verified'
    assert len(current) == len(bank) == d['current']['questions']
    assert sum(len(q['truth']) for q in bank) == d['current']['statements']
    for p, expected in d['current']['sha256'].items():
        check_hash(p, expected)
    for p, expected in d.get('pack_review', {}).get('source_sha256', {}).items():
        check_hash(p, expected)
    historical_hashes = dict(d['baseline']['sha256'])
    for p, update in d.get('documentation_updates', {}).items():
        assert hashlib.sha256(update['before_text'].encode('utf8')).hexdigest() == update['before_sha256']
        check_hash(p, update['after_sha256'])
        historical_hashes[p] = update['before_sha256']
    retired = {r['old_id']: r for r in d['replacements']}
    ids = json.loads((ROOT / 'bank/retired-ids.json').read_text(encoding='utf8'))['ids']
    assert retired.keys().isdisjoint(current)
    assert retired.keys() <= set(ids)
    assert all(r['new_id'] in current for r in retired.values())
    all_added = set(d['added_question_ids'])
    assert len(all_added) == len(d['added_question_ids'])
    assert all_added <= current.keys()
    assert set(d['new_question_ids']) == all_added - {r['new_id'] for r in retired.values()}
    assert len(d['new_question_ids']) == d['statistics']['new_questions']
    assert sum(len(current[qid]['truth']) for qid in d['new_question_ids']) == d['statistics']['new_statements']
    evidence = dict(current)
    evidence.update({qid: r['question'] for qid, r in retired.items()})
    old_quotes = dict(quotes)
    old_quotes.update({qid: r['quotes'] for qid, r in retired.items()})
    baseline = d['baseline']
    assert set(current) == (set(baseline['question_order']) - set(retired)) | all_added
    old_bank = [evidence[qid] for qid in baseline['question_order']]
    old_quotes = {qid: old_quotes[qid] for qid in baseline['quote_order']}
    restored = {'web/questions.json': old_bank, 'docs/quotes.json': old_quotes}
    for p, value in restored.items():
        actual = hashlib.sha256(encoded(value, baseline['newline'][p])).hexdigest()
        assert actual == baseline['sha256'][p], f'Unrecorded pre-existing content change: {p}'
    audit = json.loads((HERE / 'terms-and-roles.json').read_text(encoding='utf8'))
    rows = {r['id']: r for r in audit['rows']}
    required = {(r['id'], i) for r in rows.values() for i, p in enumerate(r['untested']) if p['priority'] in ['P1','P2']}
    fulfilled = set()
    for row in d['coverage']:
        gap = rows[row['row_id']]['untested'][row['gap_index']]
        assert row['point'] == gap['point'] and row['priority'] == gap['priority']
        fulfilled.add((row['row_id'], row['gap_index']))
        assert row['question_id'] in current
        q = current[row['question_id']]
        assert row['statements'] and len(row['snapshot']) == len(row['statements'])
        for i, s in zip(row['statements'], row['snapshot']):
            assert s == dict(statement=i, truth=q['truth'][i-1], en=q['en']['statements'][i-1], tc=q['tc']['statements'][i-1])
    assert required <= fulfilled, 'Unfilled P1/P2 gap'
    assert len(required) == d['statistics']['priority_gap_mappings']
    reviewed = set()
    for review in d['blind_review']['items']:
        a=review['answer'];q=current[a['id']];reviewed.add(q['id'])
        text={'id':q['id'],'module':q['module'],'source':q['source'],**{l:{k:q[l][k] for k in ['q','statements']} for l in ['en','tc']}}
        assert hashlib.sha256(json.dumps(text,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==review['reviewed_text_sha256'],q['id']
        expected=['T' if t else 'F' for t in q['truth']]
        assert a['verdicts']==a['tc_verdicts']==expected,q['id']
    assert reviewed == all_added, 'Final bilingual review must cover every new or replacement item'
    return dict(bank=bank, current=current, evidence=evidence, implementation=d,
                historical_hashes=historical_hashes)

def verify_hash(path, expected, state):
    historical = state['historical_hashes']
    if path in historical and expected == historical[path]:
        return  # Reconstructed byte for byte by load_state, including retired items.
    check_hash(path, expected)
