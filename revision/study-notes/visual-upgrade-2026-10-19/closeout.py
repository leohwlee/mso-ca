from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((HERE/'baseline.json').read_text(encoding='utf-8'))
allowed={'.impeccable/design.json','DESIGN.md',*[f'revision/study-notes/{v}' for v in ('build.py','gap_check.py','style.css','part1.py','README.md','index.html','coverage.json',*[f'part-{n}.html' for n in range(1,8)])]}
changed=[];missing=[]
for f,h in baseline.items():
    path=ROOT/f
    if not path.is_file():missing.append(f)
    elif sha(path)!=h:changed.append(f)
unexpected=sorted(set(changed)-allowed)
assert not missing and not unexpected,(missing,unexpected)
state=dict(baseline_files=len(baseline),changed_existing=changed,unchanged_existing=len(baseline)-len(changed),unexpected_changes=unexpected,missing=missing,protected_bank_sources_web_and_history_unchanged=True)
(HERE/'preservation.json').write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
checks=json.loads((HERE/'verification.json').read_text(encoding='utf-8'))
browser=json.loads((HERE/'browser-checks.json').read_text(encoding='utf-8'))
visual=json.loads((HERE/'visual-display-checks.json').read_text(encoding='utf-8'))
integration=json.loads((HERE/'integration-checks.json').read_text(encoding='utf-8'))
assert all(v['exit_code']==0 for v in checks)
assert len(browser)==42 and not any(v['overflow'] or v['spills'] or v['wrongLanguageVisible'] or v['errors'] or v['remoteRequests'] for v in browser)
assert len(visual['results'])==198 and not visual['failed']
assert len(integration['integration'])==21 and len(integration['indexChecks'])==6
files=[p for p in HERE.parent.iterdir() if p.is_file() and p.suffix in ('.py','.html','.css','.json','.md')]
files+=[ROOT/'DESIGN.md',ROOT/'.impeccable/design.json']
final=dict(files={str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in files},checks=dict(commands=len(checks),pages=42,figures=198,practice=21,index=6),limitations='Structural/source-route checks and targeted source-meaning review; no learner outcome study or blanket syllabus certification.')
review=json.loads((HERE/'independent-source-review.json').read_text(encoding='utf-8'))
final['independent_review_binding']=[dict(path=r['path'],matches_final=sha(ROOT/r['path'])==r['sha256']) for r in review['files']]
addendum=json.loads((HERE/'independent-source-fee-addendum.json').read_text(encoding='utf-8'))
final['independent_review_addendum_binding']=[dict(path=r['path'],matches_final=sha(ROOT/r['path'])==r['sha256']) for r in addendum['files']]
assert all(r['matches_final'] or any(a['path']==r['path'] and a['matches_final'] for a in final['independent_review_addendum_binding']) for r in final['independent_review_binding'])
(HERE/'final-state.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(preservation=state,checks=final['checks'],review_binding=final['independent_review_binding']),ensure_ascii=False))
