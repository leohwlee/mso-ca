from pathlib import Path
import subprocess,sys,json,concurrent.futures
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
P=sys.executable
N='C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
commands=[
 [P,'revision/study-notes/build.py','--check'],
 [P,'docs/build_catalog.py','--check'],
 *[[P,'bank/audit/'+name+'.py','--check'] for name in ('active_scope','render_active_scope','report','terms_report','p1_report','remaining_report')],
 [P,'-c',"import tempfile,unittest,pathlib,sys;tmp=pathlib.Path('dist/visual-qa-temp');tmp.mkdir(exist_ok=True);tempfile.tempdir=str(tmp.resolve());r=unittest.TextTestRunner().run(unittest.defaultTestLoader.discover('tests',pattern='*_test.py'));sys.exit(not r.wasSuccessful())"],
 [N,'--test',*[str(p.relative_to(ROOT)) for p in (ROOT/'tests').glob('*.test.cjs')]],
 ['go','test','./...'],
 [P,'revision/study-notes/gap_check.py','--check','--output','revision/study-notes/visual-upgrade-2026-10-19/bank-source-routes.json']]
def run(args):
 r=subprocess.run(args,cwd=ROOT,capture_output=True,encoding='utf-8',errors='replace')
 return dict(command=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(run,commands))
(HERE/'verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(checks=len(results),failed=[r for r in results if r['exit_code']]),ensure_ascii=False))
sys.exit(any(r['exit_code'] for r in results))
