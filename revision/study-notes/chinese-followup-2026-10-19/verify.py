"""Check final outputs and preservation; these checks do not prove legal meaning."""
from pathlib import Path
import sys,subprocess,hashlib,json,tempfile,unittest
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
results=[]
for args in [['docs/build_catalog.py','--check'],['revision/study-notes/build.py','--check'],['revision/study-notes/gap_check.py','--check']]:
    r=subprocess.run([sys.executable,'-X','utf8',*args],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    results.append(dict(command='python '+' '.join(args),exit_code=r.returncode,output=r.stdout+r.stderr))
    print(results[-1]['command'],r.returncode)
    if r.returncode:print(r.stdout,r.stderr)
temp=ROOT/'dist/audit-test-temp';temp.mkdir(exist_ok=True);tempfile.tempdir=str(temp)
with (HERE/'python-tests.txt').open('w',encoding='utf-8') as stream:
    outcome=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='*_test.py'))
results.append(dict(command='python unittest discovery (workspace-local temporary directory)',tests=outcome.testsRun,failures=len(outcome.failures),errors=len(outcome.errors),passed=outcome.wasSuccessful()))
prior=json.loads((HERE.parent/'independent-audit-2026-10-19/baseline.json').read_text(encoding='utf-8'))['sha256']
protected={n:h for n,h in prior.items() if not n.startswith('revision/study-notes/') and n!='tests/study_notes_test.py'}
changed=[n for n,h in protected.items() if not (ROOT/n).exists() or hashlib.sha256((ROOT/n).read_bytes()).hexdigest()!=h]
results.append(dict(check='original outside-notes baseline, including questions/answers/IDs/sources',files=len(protected),changed=changed,passed=not changed))
baseline=json.loads((HERE/'baseline.json').read_text(encoding='utf-8'))
allowed={'README.md','part1.py','part2.py','part3.py','part6.py','memory_panels.py','gap_check.py','coverage.json','index.html',*[f'part-{i}.html' for i in range(1,8)]}
history={n:h for n,h in baseline.items() if (ROOT/n).parent!=HERE.parent or Path(n).name not in allowed}
changed=[n for n,h in history.items() if hashlib.sha256((ROOT/n).read_bytes()).hexdigest()!=h]
results.append(dict(check='follow-up baseline protected files and prior review evidence',files=len(history),changed=changed,passed=not changed))
(HERE/'verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results[-3:],ensure_ascii=False))
sys.exit(any(r.get('exit_code',0) or r.get('passed',True) is False for r in results))
