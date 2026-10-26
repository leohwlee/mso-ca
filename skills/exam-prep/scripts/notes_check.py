#!/usr/bin/env python3
"""Check a notes page written with assets/notes-template.html.

    notes_check.py notes.html [--bank BANK] [--min-langs auto]

Errors (exit 1): duplicate ids; links to #anchors that do not exist; links to
local files that do not exist; a .block without a .cite; a data-tier outside
remember / understand / recognise / reference; on a page with more than one
language, a block missing one of them. With --bank, every notes_anchor in the
bank must name a section or block id on the page. Standard library only.
"""
import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

TIERS = {"remember", "understand", "recognise", "reference"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Node:
    def __init__(self, tag, attrs, parent, line):
        self.tag, self.attrs, self.parent, self.line = tag, dict(attrs), parent, line
        self.children = []

    def classes(self):
        return set((self.attrs.get("class") or "").split())

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], None, 0)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.cur, self.getpos()[0])
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur, self.getpos()[0]))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("page")
    p.add_argument("--bank", help="bank.json whose notes_anchor values must exist on the page")
    a = p.parse_args(argv)
    path = Path(a.page)
    tree = Tree()
    tree.feed(path.read_text(encoding="utf-8"))
    errors, warnings = [], []
    nodes = list(tree.root.walk())
    main_nodes = [n for n in nodes if n.tag == "main"]
    scope = list(main_nodes[0].walk()) if main_nodes else nodes

    ids = {}
    for n in nodes:
        i = n.attrs.get("id")
        if i:
            if i in ids:
                errors.append(f"line {n.line}: id '{i}' also used on line {ids[i]}")
            ids.setdefault(i, n.line)
    for n in nodes:
        href = n.attrs.get("href") if n.tag == "a" else None
        if not href:
            continue
        u = urlparse(href)
        if href.startswith("#"):
            if unquote(href[1:]) not in ids:
                errors.append(f"line {n.line}: link to '{href}', which no element has as its id")
        elif not u.scheme and not u.netloc and u.path:
            target = (path.parent / unquote(u.path)).resolve()
            if not target.exists():
                errors.append(f"line {n.line}: link to '{href}', which does not exist next to the page")

    langs = sorted({n.attrs["lang"] for n in scope if n.attrs.get("lang") and n.tag != "html"})
    blocks = [n for n in scope if "block" in n.classes()]
    for b in blocks:
        where = f"line {b.line}"
        tier = b.attrs.get("data-tier")
        if tier is None:
            warnings.append(f"{where}: block has no data-tier")
        elif tier not in TIERS:
            errors.append(f"{where}: data-tier '{tier}' is not one of {sorted(TIERS)}")
        if not any("cite" in d.classes() for d in b.walk()):
            errors.append(f"{where}: block has no .cite")
        if len(langs) > 1:
            present = {d.attrs.get("lang") for d in b.walk() if d.attrs.get("lang")}
            missing = [l for l in langs if l not in present]
            if missing and present:
                errors.append(f"{where}: block lacks {', '.join(missing)} text")
            elif not present:
                warnings.append(f"{where}: block has no language spans; it shows in every view")
            else:
                counts = {l: sum(1 for d in b.walk() if d.attrs.get("lang") == l) for l in langs}
                if len(set(counts.values())) > 1:
                    warnings.append(f"{where}: language span counts differ {counts}")
    sections = [n for n in scope if n.tag == "section"]
    for s in sections:
        if not s.attrs.get("id"):
            warnings.append(f"line {s.line}: section has no id, so nothing can link to it")
    if a.bank:
        raw = json.loads(Path(a.bank).read_text(encoding="utf-8-sig"))
        items = raw if isinstance(raw, list) else raw.get("items", [])
        for it in items:
            anc = it.get("notes_anchor")
            if anc and anc not in ids:
                errors.append(f"bank item {it.get('id')}: notes_anchor '{anc}' is not an id on the page")
        anchored = sum(1 for it in items if it.get("notes_anchor"))
        if anchored < len(items):
            warnings.append(f"{len(items) - anchored} of {len(items)} bank items have no notes_anchor")
    for e in errors:
        print("ERROR " + e)
    for w in warnings:
        print("warn  " + w)
    tiers = {t: sum(1 for b in blocks if b.attrs.get("data-tier") == t) for t in sorted(TIERS)}
    print(f"{len(sections)} sections, {len(blocks)} blocks {tiers}, languages {langs or ['(none marked)']}: "
          f"{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
