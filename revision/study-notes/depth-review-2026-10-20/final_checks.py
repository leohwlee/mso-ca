"""Recheck changed outputs and the historical chain; preserve the first results."""
import json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
first=HERE/'automatic-checks.json';saved=HERE/'automatic-checks-initial.json'
if first.exists() and not saved.exists():first.rename(saved)
env=dict(os.environ,PYTHONIOENCODING='utf-8',TMP=str(ROOT/'dist/depth-review-tmp'),TEMP=str(ROOT/'dist/depth-review-tmp'))
PY=sys.executable
commands=[
 [PY,'revision/study-notes/build.py'],[PY,'revision/study-notes/gap_check.py'],
 [PY,'revision/study-notes/build.py','--check'],[PY,'revision/study-notes/gap_check.py','--check'],
 *[[PY,'bank/audit/'+name+'.py','--check'] for name in ('report','terms_report','p1_report','remaining_report')],
 [PY,'-m','unittest','discover','-s','tests','-p','*_test.py'],
 [PY,'scripts/build_study_bundle.py'],[PY,'scripts/build_study_bundle.py','--check'],
 ['git','-c','core.whitespace=cr-at-eol','diff','--check']]
results=[]
for cmd in commands:
 start=time.monotonic();r=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf8',errors='replace')
 results.append(dict(command=cmd,exit_code=r.returncode,seconds=round(time.monotonic()-start,2),stdout=r.stdout,stderr=r.stderr))
 (HERE/'automatic-checks-final.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 print(('PASS' if not r.returncode else 'FAIL')+' '+' '.join(cmd[1:]),flush=True)
 if r.returncode:print((r.stdout+r.stderr)[-4000:],flush=True)
sys.exit(any(x['exit_code'] for x in results))
