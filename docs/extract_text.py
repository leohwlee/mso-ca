"""Extract all catalogued daily and reference publications to text/LANG/NN.txt.

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
changed. Image-only form labels are supplemented from reviewed, page-specific
transcripts in docs/transcripts/NN.json, tied to the PDF's SHA-256. They are
appended to their own page and labelled as transcriptions, not automatic OCR.

The catalog document number is also the filename prefix, quote document number,
extracted-text filename and image-transcript filename.

It also writes docs/text/manifest.json, which records the SHA-256 of the file
each text came from, so the tests can tell when a document has been replaced
without its text being extracted again.
"""
from html.parser import HTMLParser
import xml.etree.ElementTree as ET
import zipfile

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


class HTMLText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ignored = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style'}:
            self.ignored += 1
        if tag in {'p', 'div', 'br', 'h1', 'h2', 'li'}:
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in {'script', 'style'}:
            self.ignored -= 1

    def handle_data(self, data):
        if not self.ignored:
            self.parts.append(data)


def extract(path):
    if path.suffix == '.pdf':
        import pymupdf
        with pymupdf.open(path) as pdf:
            return '\f'.join(page.get_text() for page in pdf)
    if path.suffix == '.docx':
        with zipfile.ZipFile(path) as archive:
            document = ET.fromstring(archive.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        return '\n'.join(''.join(p.itertext()) for p in document.findall('.//w:p', ns))
    if path.suffix == '.html':
        parser = HTMLText()
        parser.feed(path.read_text(encoding='utf8'))
        return re.sub(r'\n\s*\n+', '\n\n', ''.join(parser.parts)).strip() + '\n'
    raise ValueError(f'Unsupported companion: {path}')


def main():
    manifest = {}
    catalog = json.loads((DOCS / 'catalog.json').read_text(encoding='utf8'))
    documents = catalog['documents']
    ids = [document['id'] for document in documents]
    assert ids == [f'{i:02d}' for i in range(1,len(documents)+1)], 'Invalid document order'
    for lang in sorted({lang for d in documents for lang in d['editions']}):
        out = DOCS / 'text' / lang
        out.mkdir(parents=True, exist_ok=True)
        for document in documents:
            if lang not in document['editions']:
                continue
            num = document['id']
            edition = document['editions'][lang]
            src = DOCS / edition.get('path', f'{lang}/{edition["file"]}')
            assert src.name.startswith(num + '_'), src
            companion_mode = document.get('text_mode') == 'companion'
            if companion_mode or src.suffix in {'.docx', '.html'}:
                text = extract(src)
            elif src.suffix == '.pdf':
                with pymupdf.open(src) as pdf:
                    pages = [strip_footers(page.get_text()) for page in pdf]
                transcript = DOCS / 'transcripts' / f'{num}.json'
                if transcript.exists():
                    supplement = json.loads(transcript.read_text(encoding='utf8'))[lang]
                    assert hashlib.sha256(src.read_bytes()).hexdigest() == supplement['source_sha256'], \
                        f'Re-check image transcript against changed PDF: {src.name}'
                    for number, lines in supplement['pages'].items():
                        pages[int(number)-1] += '\n[Verified image transcription]\n' + '\n'.join(lines) + '\n'
                text = '\f'.join(pages)
            elif src.suffix == '.md':
                text = src.read_text(encoding='utf-8')
            else:
                continue
            text = (text if companion_mode else unify(text)).replace('\r\n', '\n')
            target = out / f'{num}.txt'
            if not target.exists() or target.read_text(encoding='utf8') != text:
                target.write_text(text, encoding='utf-8', newline='\n')
            # Hash with Windows line endings folded, as git may check a text source
            # (the FAQ page) out either way; the tests hash it the same way.
            digest = hashlib.sha256(src.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
            text_digest = hashlib.sha256(text.encode('utf8')).hexdigest()
            edition['text_file'] = f'text/{lang}/{num}.txt'
            edition['text_sha256'] = text_digest
            manifest[f'{lang}/{num}.txt'] = {'source': src.name, 'sha256': digest, 'text_sha256': text_digest}
            transcript = DOCS / 'transcripts' / f'{num}.json'
            if src.suffix == '.pdf' and transcript.exists():
                manifest[f'{lang}/{num}.txt']['transcript_sha256'] = hashlib.sha256(
                    transcript.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
            print(f'{lang}/{num}.txt  {len(text):>9,} characters  from {src.name}', file=sys.stderr)
    target = DOCS / 'text' / 'manifest.json'
    content = json.dumps(manifest, ensure_ascii=False, indent=1) + '\n'
    if not target.exists() or target.read_text(encoding='utf8') != content:
        target.write_text(content, encoding='utf-8', newline='\n')
    catalog_target = DOCS / 'catalog.json'
    content = json.dumps(catalog, ensure_ascii=False, indent=2) + '\n'
    if catalog_target.read_text(encoding='utf8') != content:
        catalog_target.write_text(content, encoding='utf8', newline='\n')


if __name__ == '__main__':
    main()
