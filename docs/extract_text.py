"""Write the text of every document in docs/EN and docs/TC to docs/text/EN|TC/NN.txt.

The question bank's tests check each question's deciding quote against these
files, so run this again whenever a document in docs/ is added or replaced:

    python docs/extract_text.py

Needs PyMuPDF (pip install pymupdf). Pages are separated by a form feed, so the
page of a match is the number of form feeds before it, plus one. CJK
compatibility ideographs, which some of the Chinese PDFs use for common
characters (行 as U+FA08, 金 as U+F90A), are mapped to their unified forms,
and private-use characters, which some PDFs use to draw list bullets, are
dropped. The Ordinance's running footer ("Last updated date … Verified Copy",
最後更新日期 … 經核證文本) is removed from every page, so a passage that runs
across a page break reads as one and a quote can span the break. Nothing else is
changed.

It also writes docs/text/manifest.json, which records the SHA-256 of the file
each text came from, so the tests can tell when a document has been replaced
without its text being extracted again.
"""
import hashlib
import json
import pathlib
import re
import sys
import unicodedata

import pymupdf

DOCS = pathlib.Path(__file__).resolve().parent

# The footer the Ordinance prints at the foot of every page, in each language.
FOOTERS = [
    re.compile(r'Last updated date\n\d{1,2}\.\d{1,2}\.\d{4}\nAnti-Money Laundering and Counter-Terrorist '
               r'Financing Ordinance\n(?:[^\n]*\n){0,8}?Verified Copy\n'),
    re.compile(r'最後更新日期\n\d{1,2}\.\d{1,2}\.\d{4}\n《打擊洗錢及恐怖分子資金籌集條例》\n'
               r'(?:[^\n]*\n){0,8}?經核證文本\n'),
]


def strip_footers(page):
    for footer in FOOTERS:
        page = footer.sub('', page)
    return page


def unify(text):
    out = []
    for c in text:
        if '\ue000' <= c <= '\uf8ff':
            continue  # private-use glyphs: list bullets drawn from a symbol font, not text
        out.append(unicodedata.normalize('NFKC', c) if '\uf900' <= c <= '\ufaff' else c)
    return ''.join(out)


def main():
    manifest = {}
    for lang in ('EN', 'TC'):
        out = DOCS / 'text' / lang
        out.mkdir(parents=True, exist_ok=True)
        for src in sorted((DOCS / lang).iterdir()):
            num = src.name[:2]
            if not num.isdigit():
                continue
            if src.suffix == '.pdf':
                with pymupdf.open(src) as pdf:
                    pages = [strip_footers(page.get_text()) for page in pdf]
                text = '\f'.join(pages)
            elif src.suffix == '.md':
                text = src.read_text(encoding='utf-8')
            else:
                continue
            text = unify(text).replace('\r\n', '\n')
            (out / f'{num}.txt').write_text(text, encoding='utf-8', newline='\n')
            # Hash with Windows line endings folded, as git may check a text source
            # (the FAQ page) out either way; the tests hash it the same way.
            digest = hashlib.sha256(src.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
            manifest[f'{lang}/{num}.txt'] = {'source': src.name, 'sha256': digest}
            print(f'{lang}/{num}.txt  {len(text):>9,} characters  from {src.name}', file=sys.stderr)
    (DOCS / 'text' / 'manifest.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
