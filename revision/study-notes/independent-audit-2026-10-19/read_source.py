"""Read original extracted pages; does not import manuscripts or question bank."""
import argparse, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
p = argparse.ArgumentParser()
p.add_argument('doc'); p.add_argument('language'); p.add_argument('pages')
a = p.parse_args()
catalog = json.loads((ROOT/'docs/catalog.json').read_text(encoding='utf-8'))
entry = next(d for d in catalog['documents'] if d['id'] == a.doc)
edition = entry['editions'][a.language]
pages = (ROOT/'docs'/edition['text_file']).read_text(encoding='utf-8').split('\f')
print(edition['file'], '| extracted pages:', len(pages))
if a.pages == 'toc':
    for i, page in enumerate(pages):
        print(i+1, re.sub(r'\s+', ' ', page)[:210])
else:
    for span in (f'1-{len(pages)}' if a.pages == 'all' else a.pages).split(','):
        ends = list(map(int, span.split('-')))
        for n in range(ends[0], min(ends[-1], len(pages))+1):
            print(f'\n[PDF page {n}]\n'+re.sub(r'\s+', ' ', pages[n-1]))
