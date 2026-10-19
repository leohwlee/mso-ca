"""Capture final artifact hashes without changing earlier evidence."""
from pathlib import Path
import hashlib, json
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
baseline=json.loads((HERE/'baseline.json').read_text(encoding='utf-8'))
allowed={'revision/study-notes/'+n for n in ['part6.py','README.md','build.py','gap_check.py','coverage.json','index.html',*[f'part-{n}.html' for n in range(1,8)]]}
unexpected=[n for n,h in baseline.items() if n not in allowed and (not (ROOT/n).exists() or hashlib.sha256((ROOT/n).read_bytes()).hexdigest()!=h)]
assert not unexpected, unexpected
manuscripts=[ROOT/'revision/study-notes'/f'part{i}.py' for i in range(1,8)]
for p in manuscripts:
    text=p.read_text(encoding='utf-8')
    assert '25%以上' not in text and '25%或以上' not in text, p
    assert '持有>25%' not in text, p
result=dict(protected_files=len(baseline)-len(allowed),unexpected_changes=unexpected,formal_wording_check='passed',final_hashes={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(allowed)})
(HERE/'final-state.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Final wording and preservation passed:',result['protected_files'],'protected files unchanged.')
