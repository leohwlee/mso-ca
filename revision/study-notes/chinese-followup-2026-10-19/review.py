"""Read archived originals and current note claims; no question-bank input."""
import sys,json,re,zipfile,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
NOTES=HERE.parent
ROOT=NOTES.parents[1]
sys.path.insert(0,str(NOTES))
import build
cat=json.loads((ROOT/'docs/catalog.json').read_text(encoding='utf-8'))
def edition(doc,lang):
    return next(x for x in cat['documents'] if x['id']==doc)['editions'][lang]
if sys.argv[1]=='baseline':
    files=[p for p in NOTES.rglob('*') if p.is_file() and HERE not in p.parents and p.suffix not in ('.zip','.png','.pyc')]
    target=HERE/'baseline.zip'
    assert not target.exists()
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for p in files:z.write(p,str(p.relative_to(ROOT)))
    (HERE/'baseline.json').write_text(json.dumps({str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},ensure_ascii=False,indent=2),encoding='utf-8')
    print('Saved',len(files),'files')
elif sys.argv[1]=='notes':
    for n,part in build.PARTS.items():
        for s in part['sections']:
            for bi,b in enumerate(s['blocks']):
                if any(r['doc']==sys.argv[2] for r in b['refs']):
                    if len(sys.argv)>3 and n!=int(sys.argv[3]):continue
                    if len(sys.argv)>4 and s['id'] not in sys.argv[4].split(','):continue
                    print('\n',n,s['id'],bi,b['title'])
                    for i,p in enumerate(b['points']):print(i,p['tc'],'\nEN',p['en'])
                    print(b['refs'])
elif sys.argv[1] in ('pages','index'):
    ed=edition(sys.argv[2],sys.argv[3]);pages=(ROOT/'docs'/ed['text_file']).read_text(encoding='utf-8').split('\f')
    print(ed['file'],len(pages),'PDF pages')
    for span in sys.argv[4].split(','):
        ends=list(map(int,span.split('-')))
        for n in range(ends[0],min(ends[-1],len(pages))+1):
            t=re.sub(r'\s+',' ',pages[n-1]).strip()
            if sys.argv[1]=='index':t=t[:80]
            print(f'\n[{n}] {t}')
