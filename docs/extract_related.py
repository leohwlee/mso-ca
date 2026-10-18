"""Read companion formats; the command delegates to the unified catalog extractor.

    python docs/extract_related.py

Requires PyMuPDF for PDFs. DOCX and HTML use the Python standard library.
The catalog records raw-source and LF-normalized extracted-text hashes.
"""
import hashlib
from html.parser import HTMLParser
import json
import pathlib
import re
import xml.etree.ElementTree as ET
import zipfile

HERE = pathlib.Path(__file__).resolve().parent


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
    # Legacy command delegates to the single flat-catalog extraction workflow.
    from extract_text import main as extract_all
    return extract_all()


if __name__ == '__main__':
    main()
