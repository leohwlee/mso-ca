"""Write the text of every document in docs/EN and docs/TC to docs/text/EN|TC/NN.txt.

The question bank's tests check each question's deciding quote against these
files, so run this again whenever a document in docs/ is added or replaced:

    python docs/extract_text.py

Needs PyMuPDF (pip install pymupdf). Pages are separated by a form feed, so the
page of a match is the number of form feeds before it, plus one. CJK
compatibility ideographs, which some of the Chinese PDFs use for common
characters (行 as U+FA08, 金 as U+F90A), are mapped to their unified forms,
and private-use characters, which some PDFs use to draw list bullets, are
dropped; nothing else is changed.

It also writes docs/text/manifest.json, which records the SHA-256 of the file
each text came from, so the tests can tell when a document has been replaced
without its text being extracted again.
"""
import hashlib
import json
import pathlib
import sys
import unicodedata

import pymupdf

DOCS = pathlib.Path(__file__).resolve().parent


def unify(text):
    out = []
    for c in text:
        if '' <= c <= '':
            continue  # private-use glyphs: list bullets drawn from a symbol font, not text
        out.append(unicodedata.normalize('NFKC', c) if '豈' <= c <= '﫿' else c)
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
                    pages = [page.get_text() for page in pdf]
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
