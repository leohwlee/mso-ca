"""Render selected original pages whose diagrams/tables warrant direct inspection."""
from pathlib import Path
import json,subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
cat=json.loads((ROOT/'docs/catalog.json').read_text(encoding='utf-8'))
out=HERE/'original-previews';out.mkdir(exist_ok=True)
for doc,lang,page in [('25','TC',25),('25','TC',93),('04','TC',399)]:
    ed=next(x for x in cat['documents'] if x['id']==doc)['editions'][lang]
    path=ROOT/'docs'/ed['path']
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','1500','-png','-singlefile',str(path),str(out/f'{doc}-{lang}-{page}')],check=True,capture_output=True)
    print(out/f'{doc}-{lang}-{page}.png')
