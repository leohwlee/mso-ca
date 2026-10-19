"""Final reproducible manuscript checks, with a workspace-local Windows temp dir."""
import hashlib,json,subprocess,sys,tempfile,unittest
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
results=[]
for args in [
    ['revision/study-notes/build.py','--check'],
    ['revision/study-notes/gap_check.py','--check'],
]:
    p=subprocess.run([sys.executable,'-X','utf8',*args],cwd=ROOT,text=True,encoding='utf-8',capture_output=True)
    results.append(dict(command='python '+' '.join(args),exit_code=p.returncode,output=p.stdout+p.stderr))
    print(results[-1]['command'],p.returncode)
    if p.returncode:print(p.stdout,p.stderr)
temp=ROOT/'dist/audit-test-temp';temp.mkdir(exist_ok=True)
tempfile.tempdir=str(temp)
with (HERE/'python-tests-final.txt').open('w',encoding='utf-8') as stream:
    outcome=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='*_test.py'))
results.append(dict(command='python -m unittest discover -s tests -p *_test.py (workspace tempdir)',tests=outcome.testsRun,failures=len(outcome.failures),errors=len(outcome.errors),passed=outcome.wasSuccessful()))
base=json.loads((HERE/'baseline.json').read_text(encoding='utf-8'))['sha256']
protected={name:digest for name,digest in base.items() if not name.startswith('revision/study-notes/') and name!='tests/study_notes_test.py'}
changed=[name for name,digest in protected.items() if not (ROOT/name).exists() or hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest]
results.append(dict(check='pre-existing files outside the authorized notes/test change',files=len(protected),changed=changed,passed=not changed))
history={name:digest for name,digest in base.items() if name.startswith('revision/study-notes/') and (name.endswith('.zip') or name.endswith('.json') or name.endswith('.md')) and name not in ('revision/study-notes/coverage.json','revision/study-notes/README.md')}
changed_history=[name for name,digest in history.items() if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest]
results.append(dict(check='older notes review/history files',files=len(history),changed=changed_history,passed=not changed_history))
(HERE/'final-checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results[-3:],ensure_ascii=False))
sys.exit(any(r.get('exit_code',0) or r.get('passed',True) is False for r in results))
