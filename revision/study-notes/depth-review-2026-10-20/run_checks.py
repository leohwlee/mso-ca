"""Run existing project checks and retain their actual outputs for this review."""
import glob,json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
os.chdir(ROOT)
tmp=ROOT/'dist/depth-review-tmp';tmp.mkdir(parents=True,exist_ok=True)
env=dict(os.environ,PYTHONIOENCODING='utf-8',TMP=str(tmp),TEMP=str(tmp))
PY=sys.executable
commands=[
 ['go','run','.','-export-html','dist/mso-ca.html'],
 [PY,'revision/study-notes/build.py'],
 [PY,'revision/study-notes/gap_check.py'],
 [PY,'revision/study-notes/build.py','--check'],
 [PY,'revision/study-notes/gap_check.py','--check'],
 ['go','vet','./...'],['go','test','./...'],
 ['node','--test',*glob.glob('tests/*.test.cjs')],
 [PY,'-m','unittest','discover','-s','tests','-p','*_test.py'],
 [PY,'docs/build_catalog.py','--check'],
 *[[PY,'bank/audit/'+name+'.py','--check'] for name in ('active_scope','render_active_scope','report','terms_report','p1_report','remaining_report')],
 [PY,'scripts/build_study_bundle.py'],[PY,'scripts/build_study_bundle.py','--check'],
 ['git','-c','core.whitespace=cr-at-eol','diff','--check'],
]
results=[]
for cmd in commands:
    start=time.monotonic()
    r=subprocess.run(cmd,cwd=ROOT,env=env,text=True,encoding='utf-8',errors='replace',capture_output=True)
    result=dict(command=cmd,exit_code=r.returncode,seconds=round(time.monotonic()-start,2),stdout=r.stdout,stderr=r.stderr)
    results.append(result)
    (HERE/'automatic-checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(('PASS' if r.returncode==0 else 'FAIL')+' '+ ' '.join(cmd[1:] if cmd[0]==PY else cmd),flush=True)
    if r.returncode:print((r.stdout+r.stderr)[-5000:],flush=True)
sys.exit(any(r['exit_code'] for r in results))
