"""Find a phrase in the source texts and print where it is, with context.

    python bank/find.py <EN|TC> <doc|all> <phrase> [--context N]

    python bank/find.py EN 03 "target market"
    python bank/find.py TC 04 "顯眼地方" --context 300

Matching ignores whitespace, case and line breaks (CJK text in the extracts
breaks lines mid-word), so copy a distinctive 5-9 word phrase rather than a
section number, which mostly lands in the table of contents. Pages are counted
from the form feeds docs/extract_text.py writes between them.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def squash(s):
    """The text with whitespace removed and case folded, and a map back to offsets."""
    out, where = [], []
    for i, c in enumerate(s):
        if not c.isspace():
            out.append(c.lower())
            where.append(i)
    return "".join(out), where


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    context = 160
    if "--context" in args:
        i = args.index("--context")
        context = int(args[i + 1])
        del args[i:i + 2]
    if len(args) != 3:
        print(__doc__)
        sys.exit(2)
    lang, doc, phrase = args[0].upper(), args[1], args[2]
    files = sorted((ROOT / "docs" / "text" / lang).glob("*.txt"))
    if doc != "all":
        files = [f for f in files if f.stem == doc.zfill(2)]
    needle, _ = squash(phrase)
    hits = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        flat, where = squash(text)
        for m in re.finditer(re.escape(needle), flat):
            start, end = where[m.start()], where[m.end() - 1] + 1
            page = text.count("\f", 0, start) + 1
            before = text[max(0, start - context):start].replace("\f", " ")
            after = text[end:end + context].replace("\f", " ")
            snippet = re.sub(r"\s+", " ", before + "【" + text[start:end] + "】" + after)
            print(f"--- {lang}/{f.stem} p.{page}: …{snippet}…")
            hits += 1
    print(f"{hits} match{'es' if hits != 1 else ''}")


if __name__ == "__main__":
    main()
