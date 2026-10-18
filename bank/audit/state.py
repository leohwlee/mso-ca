"""Keep audit baselines verifiable after reviewed additions and replacements."""
import hashlib
import json
import pathlib
import zipfile
from active_scope import recover

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

def prove_archived_text(proven, path, data):
    """The archive bytes are already verified; permit Git's newline conversion."""
    proven.add((path, hashlib.sha256(data).hexdigest()))
    if pathlib.Path(path).suffix.lower() in {'.json', '.md', '.py', '.txt', '.go'}:
        lf = data.replace(b'\r\n', b'\n')
        for version in (lf, lf.replace(b'\n', b'\r\n')):
            proven.add((path, hashlib.sha256(version).hexdigest()))

def validate_reviews(record, current):
    reviewed = set()
    for review in record['blind_review']['items']:
        a = review['answer']; q = current[a['id']]; reviewed.add(q['id'])
        text = {'id':q['id'], 'module':q['module'], 'source':q['source'],
                **{l:{k:q[l][k] for k in ['q','statements']} for l in ['en','tc']}}
        actual = hashlib.sha256(json.dumps(text, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        assert actual == review['reviewed_text_sha256'], q['id']
        expected = ['T' if t else 'F' for t in q['truth']]
        assert a['verdicts'] == a['tc_verdicts'] == expected, q['id']
    assert reviewed == set(record['added_question_ids']), 'Every addition needs a final bilingual blind review'

def maintenance_followups(extra_proven=None):
    """Verify later documentation changes without replacing earlier audit evidence."""
    proven = set(extra_proven or ())
    for path in sorted((HERE / 'maintenance').glob('*.json'), reverse=True):
        record = json.loads(path.read_text(encoding='utf8'))
        assert record['status'] == 'verified', path
        if record.get('archive'):
            check_hash(record['archive'], record['archive_sha256'])
        if record.get('archive_preserved'):
            with zipfile.ZipFile(ROOT / record['archive']) as archive:
                for p, entry in record['archive_preserved'].items():
                    raw = archive.read(entry.get('member', p)).replace(b'\r\n', b'\n')
                    assert hashlib.sha256(raw).hexdigest() == entry['sha256'], p
                    prove_archived_text(proven, p, raw)
        if record.get('archived_text_versions'):
            with zipfile.ZipFile(ROOT / record['archive']) as archive:
                for entry in record['archived_text_versions']:
                    value = json.loads(archive.read(entry['member']))
                    for key in entry['json_pointer']:
                        value = value[key]
                    assert hashlib.sha256(value.encode('utf8')).hexdigest() == entry['sha256']
                    proven.add((entry['after'], entry['sha256']))
        if record.get('archive_updates'):
            with zipfile.ZipFile(ROOT / record['archive']) as archive:
                for p, update in record['archive_updates'].items():
                    before = archive.read(update.get('member', p)).replace(b'\r\n', b'\n')
                    assert hashlib.sha256(before).hexdigest() == update['before_sha256'], p
                    if (p, update['after_sha256']) not in proven:
                        check_hash(p, update['after_sha256'])
                    prove_archived_text(proven, p, before)
        for move in record.get('relocations', []):
            if (move['after'], move['sha256']) not in proven:
                check_hash(move['after'], move['sha256'])
            proven.add((move['before'], move['sha256']))
        for p, update in record['documentation_updates'].items():
            before = update['before_text'].encode('utf8')
            assert hashlib.sha256(before).hexdigest() == update['before_sha256'], p
            if (p, update['after_sha256']) not in proven:
                check_hash(p, update['after_sha256'])
            proven.add((p, update['before_sha256']))
    return proven

def completion_followup(bank, quotes, extra_proven=None):
    """Validate final additions/replacements and recover the untouched 338-item state."""
    proven = maintenance_followups(extra_proven)
    path = HERE / 'remaining-implementation.json'
    if not path.exists():
        return None, bank, quotes, proven
    d = json.loads(path.read_text(encoding='utf8'))
    assert d['status'] == 'verified'
    current = {q['id']: q for q in bank}
    assert len(current) == len(bank) == d['current']['questions']
    assert sum(len(q['truth']) for q in bank) == d['current']['statements']
    assert set(quotes) == set(current), 'Quotes must match the active bank'
    for p, expected in d['current']['sha256'].items():
        if (p, expected) not in proven:
            check_hash(p, expected)
    for review in [d['pack_review']['ci'], d['pack_review']['trust']]:
        check_hash(review['file'], review['sha256'])
        for p, expected in review['source_sha256'].items():
            check_hash(p.replace('\\','/'), expected)
    check_hash(d['transcript_review']['transcript_file'], d['transcript_review']['transcript_sha256'])
    assert d['skill_review']['status'] == 'pass'
    historical_guide = ('.claude/skills/exam-prep/SKILL.md', d['skill_review']['final_skill_sha256'])
    if historical_guide not in proven:
        check_hash(*historical_guide)
    refresh = d['source_verification']
    assert len(refresh['pdfs']) == 42 and all(p['binary_equal'] for p in refresh['pdfs'])
    for p in refresh['pdfs']:
        source = p['archive'].replace('\\','/')
        if (source, p['sha256']) not in proven:
            check_hash(source, p['sha256'])
    added = set(d['added_question_ids'])
    assert len(added) == len(d['added_question_ids'])
    retired = {r['old_id']: r for r in d['replacements']}
    assert len(retired) == len(d['replacements'])
    baseline = d['baseline']
    assert added.isdisjoint(baseline['question_order'])
    assert set(current) == (set(baseline['question_order']) - set(retired)) | added
    reserved = json.loads((ROOT / 'bank/retired-ids.json').read_text(encoding='utf8'))['ids']
    assert set(retired) <= set(reserved) and set(retired).isdisjoint(current)
    assert all(set(r['new_ids']) <= added for r in retired.values())
    assert set(d['new_question_ids']) == added - {qid for r in retired.values() for qid in r['new_ids']}
    restored = dict(current)
    restored.update({qid:r['question'] for qid,r in retired.items()})
    restored_quotes = dict(quotes)
    restored_quotes.update({qid:r['quotes'] for qid,r in retired.items()})
    old_bank = [restored[qid] for qid in baseline['question_order']]
    old_quotes = {qid:restored_quotes[qid] for qid in baseline['quote_order']}
    for p, value in {'web/questions.json':old_bank, 'docs/quotes.json':old_quotes}.items():
        digest = hashlib.sha256(encoded(value, baseline['newline'][p])).hexdigest()
        assert digest == baseline['sha256'][p], f'Unrecorded change in final wave: {p}'
        proven.add((p,digest))
    assert len(old_bank) == baseline['questions']
    assert sum(len(q['truth']) for q in old_bank) == baseline['statements']
    for p, update in d.get('documentation_updates', {}).items():
        assert hashlib.sha256(update['before_text'].encode('utf8')).hexdigest() == update['before_sha256']
        if (p, update['after_sha256']) not in proven:
            check_hash(p, update['after_sha256'])
        proven.add((p, update['before_sha256']))
    audit = json.loads((HERE / 'coverage.json').read_text(encoding='utf8'))
    backlog = {b['id']:b for b in audit['backlog']}
    tasks = {t['backlog_id'] for t in d['task_results'] if t['status']=='completed'}
    assert tasks == set(baseline['remaining_task_ids'])
    assert all(b['status']=='completed' for b in backlog.values()), 'Remaining backlog tasks'
    assert {row['task_id'] for row in d['coverage']} == tasks
    for row in d['coverage']:
        assert row['topic_id'] in backlog[row['task_id']]['topic_ids']
    def check_rows(rows):
        for row in rows:
            q = current[row['question_id']]
            assert row['statements'] and len(row['snapshot'])==len(row['statements'])
            for i,snapshot in zip(row['statements'],row['snapshot']):
                assert snapshot == dict(statement=i,truth=q['truth'][i-1],en=q['en']['statements'][i-1],tc=q['tc']['statements'][i-1])
    check_rows(d['coverage']); check_rows(d['specialist_coverage'])
    terms=json.loads((HERE/'terms-and-roles.json').read_text(encoding='utf8'))
    required={(r['id'],i) for r in terms['rows'] for i,g in enumerate(r['untested']) if g['priority']=='P3'}
    assert required == {(r['row_id'],r['gap_index']) for r in d['specialist_coverage']}
    assert len(bank)-len(old_bank)==d['statistics']['net_questions']
    assert sum(len(q['truth']) for q in bank)-baseline['statements']==d['statistics']['net_statements']
    assert len(added)==d['statistics']['written_questions']
    assert len(d['new_question_ids'])==d['statistics']['new_questions']
    validate_reviews(d,current)
    return d,old_bank,old_quotes,proven

def latest_followup(bank, quotes, proven=None):
    """Validate the additive P1 wave and reconstruct the preceding 320-item state."""
    path = HERE / 'p1-implementation.json'
    if not path.exists():
        return None, bank, quotes, set()
    d = json.loads(path.read_text(encoding='utf8'))
    assert d['status'] == 'verified'
    current = {q['id']:q for q in bank}
    assert len(current) == len(bank) == d['current']['questions']
    assert sum(len(q['truth']) for q in bank) == d['current']['statements']
    proven = set(proven or ())
    for p, expected in d['current']['sha256'].items():
        if (p,expected) not in proven:
            check_hash(p, expected)
    baseline = d['baseline']; added = set(d['added_question_ids'])
    assert len(added) == len(d['added_question_ids'])
    assert added.isdisjoint(baseline['question_order'])
    assert set(current) == set(baseline['question_order']) | added
    assert added == set(d['new_question_ids'])
    old_bank = [current[qid] for qid in baseline['question_order']]
    old_quotes = {qid:quotes[qid] for qid in baseline['quote_order']}
    for p, value in {'web/questions.json':old_bank, 'docs/quotes.json':old_quotes}.items():
        digest = hashlib.sha256(encoded(value, baseline['newline'][p])).hexdigest()
        assert digest == baseline['sha256'][p], f'Pre-existing item changed in P1 wave: {p}'
        proven.add((p, digest))
    assert len(old_bank) == baseline['questions']
    assert sum(len(q['truth']) for q in old_bank) == baseline['statements']
    for p, update in d.get('documentation_updates', {}).items():
        assert hashlib.sha256(update['before_text'].encode('utf8')).hexdigest() == update['before_sha256']
        if (p,update['after_sha256']) not in proven:
            check_hash(p, update['after_sha256'])
        proven.add((p, update['before_sha256']))
    tasks = {t['backlog_id'] for t in d['task_results'] if t['status'] == 'completed'}
    assert tasks == set(baseline['p1_task_ids'])
    audit = json.loads((HERE / 'coverage.json').read_text(encoding='utf8'))
    backlog = {b['id']:b for b in audit['backlog']}
    assert all(backlog[tid]['priority'] == 'P1' for tid in tasks)
    assert all(b['status'] == 'completed' for b in backlog.values() if b['priority'] == 'P1')
    assert {row['task_id'] for row in d['coverage']} == tasks
    for row in d['coverage']:
        assert row['topic_id'] in backlog[row['task_id']]['topic_ids']
        q = current[row['question_id']]
        assert row['statements'] and len(row['snapshot']) == len(row['statements'])
        for i, snapshot in zip(row['statements'], row['snapshot']):
            assert snapshot == dict(statement=i, truth=q['truth'][i-1], en=q['en']['statements'][i-1], tc=q['tc']['statements'][i-1])
    assert len(added) == d['statistics']['new_questions']
    assert sum(len(current[qid]['truth']) for qid in added) == d['statistics']['new_statements']
    validate_reviews(d, current)
    return d, old_bank, old_quotes, proven

def load_state():
    """Validate current follow-up, then load the original checklist's historical bank."""
    bank = json.loads((ROOT / 'web/questions.json').read_text(encoding='utf8'))
    quotes = json.loads((ROOT / 'docs/quotes.json').read_text(encoding='utf8'))
    bank, quotes, scope_proven = recover(bank, quotes)
    active_bank = bank
    active_current = {q['id']:q for q in bank}
    completion, bank, quotes, proven = completion_followup(bank, quotes, scope_proven)
    intermediate = {q['id']:q for q in bank}
    latest, bank, quotes, proven = latest_followup(bank, quotes, proven)
    current = {q['id']: q for q in bank}
    path = HERE / 'implementation.json'
    if not path.exists():
        return dict(bank=bank, current=current, evidence=current, implementation=None, historical_hashes={})
    d = json.loads(path.read_text(encoding='utf8'))
    assert d['status'] == 'verified'
    assert len(current) == len(bank) == d['current']['questions']
    assert sum(len(q['truth']) for q in bank) == d['current']['statements']
    for p, expected in d['current']['sha256'].items():
        if (p, expected) not in proven:
            check_hash(p, expected)
    for p, expected in d.get('pack_review', {}).get('source_sha256', {}).items():
        if (p, expected) not in proven:
            check_hash(p, expected)
    historical_hashes = dict(d['baseline']['sha256'])
    for p, update in d.get('documentation_updates', {}).items():
        assert hashlib.sha256(update['before_text'].encode('utf8')).hexdigest() == update['before_sha256']
        if (p, update['after_sha256']) not in proven:
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
    validate_reviews(d, current)
    evidence.update(intermediate)
    evidence.update(active_current)
    return dict(bank=active_bank, current=active_current, evidence=evidence, implementation=d,
                p1_implementation=latest, remaining_implementation=completion,
                historical_hashes=historical_hashes, historical_versions=proven)

def verify_hash(path, expected, state):
    historical = state['historical_hashes']
    if path in historical and expected == historical[path]:
        return  # Reconstructed byte for byte by load_state, including retired items.
    if (path, expected) in state.get('historical_versions', set()):
        return  # Reconstructed preceding wave or preserved documentation text.
    check_hash(path, expected)
