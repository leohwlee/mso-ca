"""Check a patch of items and apply it to the bank.

    python bank/apply.py check patch.json
    python bank/apply.py apply patch.json
    python bank/apply.py next <module> [count]     # the next unused ids in a module

A patch is a JSON list of items written as bank/FORMAT.md describes, each with
a `quotes` field, {"en": [...], "tc": [...]}, holding one {"doc", "text"} per
statement, and without `options` or `answer`: both are generated from `truth`
by bank/combo.py. An item whose stem states how many statements are true gives
that number as `count`. An item marked `official` (C&ED's own samples) gives
C&ED's options instead.

`apply` replaces an item whose id is already in the bank and adds the others at
the end of their module; it changes nothing else, and moves each item's quotes
into docs/quotes.json. When an existing item's truth values are unchanged, its
option sets and answer index are retained so saved answers still mean the same
thing. `go test ./...` then runs every check on the result.
"""
import json
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import combo  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
TRAPS = {"offlist", "added", "scope", "reversed", "qualifier", "number", "period", "actor", "modal", "name", "condition"}
SIMPLIFIED = "则说这为与应须时实际关条项过发会经务业资产权报单录证据审处规员责负济称纳统计认识义还进对当现并问题获确护险币汇银营类罚级构讯检视让论设读转选阶历场断备节约"
POSITIONAL = re.compile(r"(?i)\bstatements?\s*\(?\d|\b(?:first|second|third|fourth|fifth|sixth|last|other)\s+statements?\b"
                        r"|陳述\s*[（(]?\d|第\s*[\d一二三四五六]\s*[項句]陳述|\b(?:option|answer|choice)\s+[A-E]\b|選項\s*[A-Ea-e1-5]")
DROP = set("“”‘’\"'「」『』＂＇—–‑‐‒―-­－")
HAN = re.compile(r"[一-鿿㐀-䶿]")
BRACKETED_HAN = re.compile(r"\([一-鿿㐀-䶿、，]+\)")
# As questions_test.go's danglingRefs: Chinese 該X needs an X said before it.
DANGLING = [(re.compile(form), ants) for form, ants in (
    (r"該[項宗筆名間位]?(?:金錢服務)?經營者", ["經營者"]),
    (r"該[項宗筆名間位]?客戶", ["客戶"]),
    (r"該[項宗筆名間位]?交易", ["交易", "匯款", "電傳轉帳", "電傳轉賬", "兌換"]),
    (r"該[項宗筆名間位]?機構", ["機構"]),
    (r"該[項宗筆名間位]?公司", ["公司"]),
    (r"該[項宗筆名間位]?業務關係", ["業務關係"]),
    (r"該[項宗筆名間位]?持牌人", ["持牌人"]),
    (r"該[項宗筆名間位]?匯款人", ["匯款人"]),
    (r"該[項宗筆名間位]?申請人", ["申請人"]),
)]


def dangling(read, field):
    """The 該X forms in field with no X in read or earlier in field."""
    out = []
    for form, ants in DANGLING:
        m = form.search(field)
        if m and not any(a in form.sub("", read + field[:m.start()]) for a in ants):
            out.append(m.group())
    return out


def match_key(s):
    """As sources_test.go's matchKey: no whitespace, quote marks or dashes,
    full-width forms folded to ASCII, case folded."""
    out = []
    for c in s:
        if c.isspace() or c in DROP or unicodedata.category(c) == "Co":
            continue
        if "！" <= c <= "～":
            c = chr(ord(c) - 0xFEE0)
        out.append(c.lower())
    return "".join(out)


_texts = {}


def source_text(lang, doc):
    key = (lang, doc)
    if key not in _texts:
        path = ROOT / "docs" / "text" / lang.upper() / f"{doc}.txt"
        _texts[key] = match_key(path.read_text(encoding="utf-8")) if path.exists() else None
    return _texts[key]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path, data):
    with open(ROOT / path, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=1) + "\n")


def build(item):
    """The item as the bank stores it, with options and answer; raises on a bad item."""
    n = len(item["truth"])
    existing = next((q for q in load("web/questions.json") if q["id"] == item["id"]), None)
    if item.get("official"):
        options = item["options"]
        hits = [i for i, o in enumerate(options) if combo.option_set(o, n) == frozenset(combo.true_set(item["truth"]))]
        answer = hits[0] if len(hits) == 1 else -1
    elif existing and existing["truth"] == item["truth"]:
        options, answer = existing["options"], existing["answer"]
    else:
        options, answer = combo.generate(item["truth"], seed=item["id"], count=item.get("count"))
    out = {"id": item["id"], "module": item["module"], "truth": item["truth"], "options": options, "answer": answer,
           "traps": item["traps"]}
    if item.get("official"):
        out["official"] = item["official"]
    out["source"] = item["source"]
    for lang in ("en", "tc"):
        side = item[lang]
        out[lang] = {"q": side["q"], "statements": side["statements"], "notes": side["notes"]}
        if side.get("explain"):
            out[lang]["explain"] = side["explain"]
    return out


def length_problems(item):
    """The statement-length guards of questions_test.go: within one item the
    statements stay within 40% of their mean length of each other (or 20 English
    / 8 Chinese characters apart), and none stands more than 15% clear of its
    nearest neighbour (or 8 / 3 characters)."""
    out = []
    for lang, floor, near in (("en", 20, 8), ("tc", 8, 3)):
        ss = item.get(lang, {}).get("statements", [])
        if len(ss) < 2:
            continue
        n = sorted(len(s) for s in ss)
        gap, mean = n[-1] - n[0], sum(n) / len(n)
        if gap > floor and gap / mean > 0.40:
            out.append(f"{lang}: statements run from {n[0]} to {n[-1]} characters; keep them within 40% of the mean")
        if n[1] - n[0] > near and n[0] < n[1] * 0.85:
            out.append(f"{lang}: the shortest statement ({n[0]}) stands apart from the next ({n[1]})")
        if n[-1] - n[-2] > near and n[-1] > n[-2] * 1.15:
            out.append(f"{lang}: the longest statement ({n[-1]}) stands apart from the next ({n[-2]})")
    return out


def problems(item):
    out = []
    iid = item.get("id", "?")
    m = item.get("module")
    if not isinstance(m, int) or not 1 <= m <= 7 or not str(iid).startswith(f"m{m}-"):
        out.append(f"id {iid!r} and module {m!r} do not agree")
    if iid in load("bank/retired-ids.json")["ids"]:
        out.append(f"id {iid!r} is retired and must not be reused")
    if item.get("fixed"):
        out.append("all items need independent statement notes and must allow reordering")
    truth = item.get("truth")
    if not isinstance(truth, list) or not all(isinstance(t, bool) for t in truth) or not 4 <= len(truth) <= 6:
        return out + ["truth must list 4 to 6 true/false values"]
    n = len(truth)
    src = item.get("source", {})
    for lang in ("en", "tc"):
        if not re.search(r"\d", src.get(lang, "")):
            out.append(f"source.{lang} has no locator")
    traps = item.get("traps")
    if not isinstance(traps, list) or len(traps) != n:
        out.append(f"traps must list {n} entries")
    else:
        for i, (t, tr) in enumerate(zip(truth, traps)):
            if t and tr is not None:
                out.append(f"statement {i + 1} is true but has the trap {tr!r}")
            if not t and tr not in TRAPS:
                out.append(f"statement {i + 1} is false and needs a trap from {sorted(TRAPS)}, not {tr!r}")
        for i, s in enumerate(item.get("en", {}).get("statements", [])[:n]):
            if traps[i] == "name" and "financial investigation unit" in s.lower():
                out.append(f"statement {i + 1} is false on the JFIU's name alone; C&ED's own sample keys "
                           "'Joint Financial Investigation Unit' true (register B21)")
    for lang in ("en", "tc"):
        side = item.get(lang, {})
        if not side.get("q", "").strip():
            out.append(f"{lang}: empty stem")
        for field in ("statements", "notes"):
            vals = side.get(field, [])
            if len(vals) != n or not all(isinstance(v, str) and v.strip() for v in vals):
                out.append(f"{lang}: {field} must hold {n} non-empty strings")
        for field in ("notes",):
            for i, v in enumerate(side.get(field, [])):
                if POSITIONAL.search(v):
                    out.append(f"{lang} note {i + 1} refers to a statement or option by position: {POSITIONAL.search(v).group()!r}")
        if lang == "tc":
            for v in [side.get("q", ""), side.get("explain", "")] + side.get("statements", []) + side.get("notes", []) + [src.get("tc", "")]:
                bad = [c for c in v if c in SIMPLIFIED]
                if bad:
                    out.append(f"tc has the simplified character {bad[0]!r} in {v[:30]!r}")
            if not item.get("official"):
                stem, ss, ns = side.get("q", ""), side.get("statements", []), side.get("notes", [])
                checks = [("stem", "", stem), ("explain", stem + "".join(ss), side.get("explain", ""))]
                checks += [(f"statement {i + 1}", stem, s) for i, s in enumerate(ss)]
                checks += [(f"note {i + 1}", stem + (ss[i] if i < len(ss) else ""), v) for i, v in enumerate(ns)]
                for where, read, v in checks:
                    for form in dangling(read, v):
                        out.append(f"tc {where}: {form} has nothing before it to refer back to: {v[:40]!r}")
        else:
            for v in [side.get("q", ""), side.get("explain", "")] + side.get("statements", []) + side.get("notes", []):
                if re.search(r"[一-鿿]", v):
                    out.append(f"en has Chinese text in {v[:40]!r}")
    if not item.get("official"):
        out += length_problems(item)
    quotes = item.get("quotes", {})
    for lang in ("en", "tc"):
        qs = quotes.get(lang)
        if not isinstance(qs, list) or len(qs) != n:
            out.append(f"quotes.{lang} must hold {n} quotes")
            continue
        for i, q in enumerate(qs):
            doc, text = q.get("doc", ""), q.get("text", "")
            st = source_text(lang, doc)
            if st is None:
                out.append(f"quotes.{lang}[{i}]: no document {doc!r}")
            elif not text.strip() or match_key(text) not in st:
                out.append(f"quotes.{lang}[{i}]: not found in docs/text/{lang.upper()}/{doc}.txt: {text[:60]!r}")
            elif (lang == "tc") != bool(HAN.search(BRACKETED_HAN.sub("", text))):
                out.append(f"quotes.{lang}[{i}]: the quote is in the wrong language: {text[:60]!r}")
            elif lang == "en" and not 3 <= len(text.split()) <= 60:
                out.append(f"quotes.en[{i}]: {len(text.split())} words; keep a quote to 3 to 60: {text[:60]!r}")
            elif lang == "tc" and not 6 <= len(match_key(text)) <= 140:
                out.append(f"quotes.tc[{i}]: {len(match_key(text))} characters; keep a quote to 6 to 140: {text[:30]!r}")
    if out:
        return out
    try:
        built = build(item)
    except (ValueError, AssertionError) as e:
        return [str(e)]
    return [f"options: {p}" for p in combo.problems(built)]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) >= 3 and sys.argv[1] == "next":
        m, count = int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 1
        used = {q["id"] for q in load("web/questions.json")} | set(load("bank/retired-ids.json")["ids"])
        nums = [int(i.split("-")[1]) for i in used if i.startswith(f"m{m}-") and i.split("-")[1].isdigit()]
        start = max(nums, default=0) + 1
        print(" ".join(f"m{m}-{k}" for k in range(start, start + count)))
        return
    if len(sys.argv) != 3 or sys.argv[1] not in ("check", "apply"):
        print(__doc__)
        sys.exit(2)
    patch = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
    bad = 0
    for item in patch:
        ps = problems(item)
        for p in ps:
            print(f"{item.get('id')}: {p}")
        bad += bool(ps)
    print(f"{len(patch)} items, {bad} with problems")
    if bad or sys.argv[1] == "check":
        sys.exit(1 if bad else 0)

    bank, quotes = load("web/questions.json"), load("docs/quotes.json")
    index = {q["id"]: i for i, q in enumerate(bank)}
    for item in patch:
        built = build(item)
        quotes[item["id"]] = item["quotes"]
        if item["id"] in index:
            bank[index[item["id"]]] = built
        else:
            at = max((i for i, q in enumerate(bank) if q["module"] <= item["module"]), default=-1) + 1
            bank.insert(at, built)
            index = {q["id"]: i for i, q in enumerate(bank)}
    save("web/questions.json", bank)
    save("docs/quotes.json", quotes)
    print(f"applied {len(patch)} items")


if __name__ == "__main__":
    main()
