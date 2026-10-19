"""Display current source manuscript, including supplements; never reads bank."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
import build
n=int(sys.argv[1])
for s in build.PARTS[n]['sections']:
    if len(sys.argv)>2 and s['id'] not in sys.argv[2].split(','):continue
    print('\n##',s['id'],s['title']['tc'])
    for bi,b in enumerate(s['blocks']):
        print('BLOCK',bi,b['title'])
        for i,p in enumerate(b['points']):print(i,p['tc'],'\nEN:',p['en'])
        print('SOURCE:',[(r['doc'],r['locator']['en']) for r in b['refs']])
