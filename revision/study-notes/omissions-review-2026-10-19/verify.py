"""Structural checks and byte-preservation checks, not semantic proof."""
from pathlib import Path
import sys,subprocess,hashlib,json,tempfile,unittest
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
if len(sys.argv)>1 and sys.argv[1]=='bank':
    bank=json.loads((ROOT/'web/questions.json').read_text(encoding='utf-8'))
    quotes=json.loads((ROOT/'docs/quotes.json').read_text(encoding='utf-8'))
    rows=[]
    for q in bank:
        docs=sorted({r['doc'] for lang in ('tc','en') for r in quotes[q['id']][lang]})
        if {'04','25'}&set(docs):rows.append(dict(id=q['id'],part=q['module'],docs=docs,stem=q['tc']['q']))
    start=int(sys.argv[2]) if len(sys.argv)>2 else 0
    print('Post-authoring selected stems:',len(rows))
    for row in rows[start:start+60]:print(json.dumps(row,ensure_ascii=False))
    sys.exit(0)

results=[]
scripts=['docs/build_catalog.py','revision/study-notes/build.py','revision/study-notes/gap_check.py','bank/audit/active_scope.py','bank/audit/render_active_scope.py','bank/audit/report.py','bank/audit/terms_report.py','bank/audit/p1_report.py','bank/audit/remaining_report.py']
for script in scripts:
    r=subprocess.run([sys.executable,'-X','utf8',script,'--check'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    results.append(dict(command='python '+script+' --check',exit_code=r.returncode,output=r.stdout+r.stderr))
    print(script,r.returncode)
    if r.returncode:print(r.stdout,r.stderr)
temp=ROOT/'dist/audit-test-temp';temp.mkdir(exist_ok=True);tempfile.tempdir=str(temp)
with (HERE/'python-tests.txt').open('w',encoding='utf-8') as stream:
    outcome=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='*_test.py'))
results.append(dict(command='python unittest discovery (workspace-local temporary directory)',tests=outcome.testsRun,failures=len(outcome.failures),errors=len(outcome.errors),passed=outcome.wasSuccessful()))
baseline=json.loads((HERE/'baseline.json').read_text(encoding='utf-8'))
allowed={'README.md','part1.py','part2.py','part5.py','part6.py','part7.py','gap_check.py','build.py','coverage.json','index.html',*[f'part-{n}.html' for n in range(1,8)]}
protected={**baseline['protected'],**{n:h for n,h in baseline['active'].items() if Path(n).name not in allowed}}
changed=[n for n,h in protected.items() if not (ROOT/n).exists() or hashlib.sha256((ROOT/n).read_bytes()).hexdigest()!=h]
results.append(dict(check='protected sources, bank, app and earlier audit evidence unchanged',files=len(protected),changed=changed,passed=not changed))
current={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in baseline['active'] if Path(n).name in allowed}
(HERE/'final-active-sha256.json').write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(HERE/'verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results[-2:],ensure_ascii=False))
sys.exit(any(r.get('exit_code',0) or r.get('passed',True) is False for r in results))
