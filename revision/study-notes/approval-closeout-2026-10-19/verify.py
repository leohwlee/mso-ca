"""Fresh verification outputs; preserve every preceding audit file."""
from pathlib import Path
import hashlib, json, subprocess, sys, tempfile, unittest
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
results = []
for script in ['docs/build_catalog.py', 'revision/study-notes/build.py', 'revision/study-notes/gap_check.py', 'bank/audit/active_scope.py', 'bank/audit/render_active_scope.py', 'bank/audit/report.py', 'bank/audit/terms_report.py', 'bank/audit/p1_report.py', 'bank/audit/remaining_report.py']:
    r = subprocess.run([sys.executable, '-X', 'utf8', script, '--check'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
    results.append(dict(command=script+' --check', exit_code=r.returncode, output=r.stdout+r.stderr))
    print(script, r.returncode)
    if r.returncode: print(r.stdout, r.stderr)
temp = ROOT/'dist/audit-test-temp'; temp.mkdir(exist_ok=True); tempfile.tempdir=str(temp)
with (HERE/'python-tests.txt').open('w', encoding='utf-8') as stream:
    out = unittest.TextTestRunner(stream=stream, verbosity=2).run(unittest.defaultTestLoader.discover(str(ROOT/'tests'), pattern='*_test.py'))
results.append(dict(check='Python tests', tests=out.testsRun, passed=out.wasSuccessful()))
baseline=json.loads((HERE/'baseline.json').read_text(encoding='utf-8'))
allowed={'revision/study-notes/'+n for n in ['part6.py','README.md','build.py','gap_check.py','coverage.json','index.html',*[f'part-{n}.html' for n in range(1,8)]]}
changed=[n for n,h in baseline.items() if not (ROOT/n).exists() or hashlib.sha256((ROOT/n).read_bytes()).hexdigest()!=h]
unexpected=[n for n in changed if n not in allowed]
results.append(dict(check='preserve sources, bank, app, conflict decisions and all earlier evidence', protected=len(baseline)-len(allowed), changed=changed, unexpected=unexpected, passed=not unexpected))
(HERE/'final-active-sha256.json').write_text(json.dumps({n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(allowed)},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(HERE/'verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results[-2:],ensure_ascii=False))
sys.exit(any(r.get('exit_code',0) or r.get('passed',True) is False for r in results))
