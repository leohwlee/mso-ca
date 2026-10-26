#!/usr/bin/env python3
"""Archive, extract and search source documents.

    sources.py extract FILE... --out DIR [--lang LANG]   per-page text, one file per document
    sources.py manifest DIR [--out manifest.json]        size, pages and SHA-256 of every file
    sources.py find DIR "phrase" [--doc NN] [--lang LANG] [--context 160]

Extracted text keeps the source's bytes as far as the extractor allows, with a
`=== page N ===` line before each page; searching normalises both sides (NFKC,
quotes and dashes, whitespace, and whitespace inside CJK text), so a term that
is present is found. PDF needs PyMuPDF (`pip install pymupdf`) or pypdf; DOCX,
HTML, Markdown and text need only the standard library.
"""
import argparse
import hashlib
import html
import json
import re
import sys
import unicodedata
import zipfile
from html.parser import HTMLParser
from pathlib import Path

QUOTES = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-",
                        "—": "-", "−": "-", "­": None, " ": " ",
                        "「": '"', "」": '"', "『": '"', "』": '"'})
LOW_TEXT = 40   # characters on a page below which it is probably an image


def norm(text):
    t = unicodedata.normalize("NFKC", text or "").translate(QUOTES).lower()
    t = re.sub(r"\s+", " ", t).strip()
    return re.sub(r"(?<=[^\x00-\x7f]) (?=[^\x00-\x7f])", "", t)


def norm_with_map(text):
    """Normalised text plus, for each of its characters, the index in `text` it came
    from, so a hit can be shown in the original."""
    out, src = [], []
    prev_space = True
    for i, ch in enumerate(text):
        for c in unicodedata.normalize("NFKC", ch).translate(QUOTES).lower():
            if c.isspace():
                if prev_space:
                    continue
                c, prev_space = " ", True
            else:
                prev_space = False
            out.append(c)
            src.append(i)
    # drop single spaces between two non-ASCII characters (CJK line breaks)
    keep_out, keep_src = [], []
    for j, c in enumerate(out):
        if c == " " and 0 < j < len(out) - 1 and ord(out[j - 1]) > 127 and ord(out[j + 1]) > 127:
            continue
        keep_out.append(c)
        keep_src.append(src[j])
    return "".join(keep_out), keep_src


# ---------------------------------------------------------------- extract


def pdf_pages(path):
    try:
        import fitz  # PyMuPDF
        with fitz.open(path) as doc:
            return [page.get_text() for page in doc]
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
    except ImportError:
        raise SystemExit("PDF extraction needs PyMuPDF or pypdf: pip install pymupdf")
    return [p.extract_text() or "" for p in PdfReader(str(path)).pages]


def docx_pages(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = re.sub(r"<w:tab/>", "\t", xml)
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r'<w:br w:type="page"/>|<w:lastRenderedPageBreak/>', "\f", xml)
    text = html.unescape(re.sub(r"<[^>]+>", "", xml))
    return [p for p in text.split("\f")] or [text]


class _Text(HTMLParser):
    BLOCK = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "section", "article", "td", "th"}

    def __init__(self):
        super().__init__()
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.skip += 1
        if tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def html_pages(path):
    p = _Text()
    p.feed(Path(path).read_text(encoding="utf-8", errors="replace"))
    text = re.sub(r"\n\s*\n+", "\n\n", "".join(p.parts))
    return [text.strip()]


def text_pages(path):
    text = Path(path).read_text(encoding="utf-8-sig", errors="replace")
    pages = re.split(r"^=== page \d+ ===$", text, flags=re.M)
    return [p.strip("\n") for p in pages if p.strip()] if len(pages) > 1 else text.split("\f")


def extract_one(path):
    ext = path.suffix.lower()
    if ext == ".pdf":
        return pdf_pages(path)
    if ext == ".docx":
        return docx_pages(path)
    if ext in (".html", ".htm"):
        return html_pages(path)
    if ext in (".txt", ".md", ".markdown", ".csv", ".srt", ".vtt"):
        return text_pages(path)
    raise SystemExit(f"{path}: no extractor for {ext}; convert it to PDF, DOCX, HTML or text first")


def doc_number(path, n):
    m = re.match(r"(\d+)", path.stem)
    return m.group(1) if m else f"{n:02d}"


def cmd_extract(a):
    out = Path(a.out) / a.lang if a.lang else Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for n, f in enumerate(a.files, 1):
        path = Path(f)
        pages = extract_one(path)
        num = doc_number(path, n)
        body = "\n".join(f"=== page {i} ===\n{p.rstrip()}" for i, p in enumerate(pages, 1)) + "\n"
        target = out / f"{num}.txt"
        target.write_text(body, encoding="utf-8")
        thin = [i for i, p in enumerate(pages, 1) if len(re.sub(r"\s", "", p)) < LOW_TEXT]
        msg = f"{path.name} -> {target} ({len(pages)} pages)"
        if thin:
            shown = ", ".join(map(str, thin[:15])) + (" …" if len(thin) > 15 else "")
            msg += f"; little or no text on page(s) {shown}: read them as images"
        print(msg)
    return 0


# ---------------------------------------------------------------- manifest


def cmd_manifest(a):
    root = Path(a.dir)
    rows = []
    for p in sorted(x for x in root.rglob("*") if x.is_file()):
        data = p.read_bytes()
        row = {"path": p.relative_to(root).as_posix(), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        if p.suffix.lower() == ".txt":
            row["pages"] = len(re.findall(r"^=== page \d+ ===$", data.decode("utf-8", "replace"), flags=re.M)) or None
        rows.append(row)
    text = json.dumps(rows, ensure_ascii=False, indent=1) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        print(f"{len(rows)} files -> {a.out}")
    else:
        print(text, end="")
    return 0


# ---------------------------------------------------------------- find


def cmd_find(a):
    root = Path(a.dir)
    files = sorted(root.rglob("*.txt"))
    if a.lang:
        files = [f for f in files if f.parent.name.lower() == a.lang.lower()
                 or f.parent.name.lower() == a.lang.lower().split("-")[0]]
    if a.doc:
        def same_doc(stem):
            m = re.match(r"([0-9A-Za-z]+)", stem)
            d = m.group(1) if m else stem
            return d == a.doc or (d.isdigit() and a.doc.isdigit() and int(d) == int(a.doc))
        files = [f for f in files if same_doc(f.stem)]
    want = norm(a.phrase)
    squeezed = re.sub(r"\s", "", want)
    hits = 0
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        page_starts = [(m.start(), int(m.group(1))) for m in re.finditer(r"^=== page (\d+) ===$", text, flags=re.M)]
        t, src = norm_with_map(text)
        found = [(m.start(), m.end()) for m in re.finditer(re.escape(want), t)]
        if not found and squeezed != want:
            ns = [(c, s) for c, s in zip(t, src) if not c.isspace()]
            st = "".join(c for c, _ in ns)
            found = [(None, None, ns[m.start()][1], ns[m.end() - 1][1] + 1) for m in re.finditer(re.escape(squeezed), st)]
        for hit in found:
            if len(hit) == 2:
                s, e = src[hit[0]], src[hit[1] - 1] + 1
            else:
                s, e = hit[2], hit[3]
            page = max((p for pos, p in page_starts if pos <= s), default=None)
            lo, hi = max(0, s - a.context), min(len(text), e + a.context)
            ctx = re.sub(r"=== page \d+ ===", " ", text[lo:hi])
            ctx = re.sub(r"\s+", " ", ctx).strip()
            print(f"{f.relative_to(root).as_posix()} p.{page}: …{ctx}…\n")
            hits += 1
            if hits >= a.max:
                print(f"(stopped at {a.max} hits; --max to raise)")
                return 0
    if not hits:
        print("not found (searched normalised text; try a shorter or more distinctive phrase, "
              "and read image pages before concluding the point is absent)")
        return 1
    return 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract", help="per-page text from PDF, DOCX, HTML, Markdown or text")
    e.add_argument("files", nargs="+")
    e.add_argument("--out", required=True)
    e.add_argument("--lang", help="write into OUT/LANG/, the layout bank_tool.py check --sources reads")
    e.set_defaults(fn=cmd_extract)
    m = sub.add_parser("manifest", help="hashes of every file under a folder")
    m.add_argument("dir")
    m.add_argument("--out")
    m.set_defaults(fn=cmd_manifest)
    f = sub.add_parser("find", help="search the extracted text")
    f.add_argument("dir")
    f.add_argument("phrase")
    f.add_argument("--doc")
    f.add_argument("--lang")
    f.add_argument("--context", type=int, default=160)
    f.add_argument("--max", type=int, default=20)
    f.set_defaults(fn=cmd_find)
    a = p.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
