#!/usr/bin/env python3
"""Check, measure and review a question bank written to the exam-prep schema.

    bank_tool.py check   SPEC BANK [--sources DIR] [--notes FILE] [--json]
    bank_tool.py tells   SPEC BANK [--papers N] [--seed S]
    bank_tool.py options SPEC BANK [--write] [--regenerate] [--seed S]
    bank_tool.py packet  SPEC BANK --lang L --out FILE [--ids a,b | --ids-file F] [--seed S]
    bank_tool.py compare SPEC BANK ANSWERS [--json]
    bank_tool.py stats   SPEC BANK

The schema is described in references/formats.md. `check` exits 1 when it finds
an error, so it can gate a build. Standard library only.
"""
import argparse
import difflib
import hashlib
import html
import itertools
import json
import math
import random
import re
import statistics
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

KINDS = {"single", "multi", "tf", "combo", "match", "order", "cloze", "numeric", "short", "essay"}
OBJECTIVE = KINDS - {"short", "essay"}
ALL, NONE = "all", "none"
TRAP_CODES = {"offlist", "added", "scope", "reversed", "qualifier", "degree", "number", "period",
              "actor", "modal", "name", "condition"}

# ---------------------------------------------------------------- loading


def load_json(path):
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def load(spec_path, bank_path):
    spec = load_json(spec_path)
    raw = load_json(bank_path)
    if isinstance(raw, list):
        bank = {"items": raw, "cases": {}}
    else:
        bank = {"items": raw.get("items", []), "cases": raw.get("cases", {})}
    return spec, bank, raw


def langs(spec):
    return list(spec.get("languages") or ["en"])


def loc(value, lang, fallback=None):
    """A localised string: one string for every language, or {lang: string}."""
    if value is None:
        return fallback
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        if lang in value:
            return value[lang]
        return fallback
    return fallback


def kind_conf(spec, item, key, default=None):
    if key in item:
        return item[key]
    return (spec.get("kinds") or {}).get(item.get("kind"), {}).get(key, default)


def shuffles(spec, item):
    """Whether the app reorders anything in this item at draw time."""
    if item.get("official") or item.get("fixed"):
        return False
    k = item.get("kind")
    if k in ("single", "multi"):
        return bool(kind_conf(spec, item, "shuffle", True))
    if k == "combo":
        return bool(kind_conf(spec, item, "shuffle_statements", True))
    return k in ("order", "match")


# ---------------------------------------------------------------- text


def is_cjk_char(ch):
    o = ord(ch)
    return (0x3040 <= o <= 0x30FF or 0x3400 <= o <= 0x4DBF or 0x4E00 <= o <= 0x9FFF
            or 0xF900 <= o <= 0xFAFF or 0xAC00 <= o <= 0xD7AF or 0x20000 <= o <= 0x2FFFF)


def is_cjk(text):
    letters = [c for c in text if c.isalnum()]
    return bool(letters) and sum(is_cjk_char(c) for c in letters) / len(letters) > 0.3


QUOTES = str.maketrans({"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u2013": "-",
                        "\u2014": "-", "\u2212": "-", "\u00ad": None, "\u00a0": " ",
                        "\u300c": '"', "\u300d": '"', "\u300e": '"', "\u300f": '"'})


def norm(text):
    """For comparing and searching: NFKC, unified quotes and dashes, lower case,
    whitespace collapsed, and removed between CJK characters."""
    t = unicodedata.normalize("NFKC", text or "").translate(QUOTES).lower()
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"(?<=[^\x00-\x7f]) (?=[^\x00-\x7f])", "", t)
    return t


def strip_pages(text):
    return re.sub(r"^=== page \d+ ===$", " ", text, flags=re.M)


def tlen(text):
    return len(re.sub(r"\s+", " ", (text or "").strip()))


def tokens(text):
    t = norm(text)
    if is_cjk(t):
        chars = [c for c in t if c.isalnum()]
        return {a + b for a, b in zip(chars, chars[1:])}
    return {w for w in re.findall(r"\w+", t) if len(w) > 2}


def shingles(text, n=4):
    t = norm(text)
    if is_cjk(t):
        chars = "".join(c for c in t if c.isalnum())
        return {chars[i:i + n] for i in range(max(1, len(chars) - n + 1))}
    words = re.findall(r"\w+", t)
    return {" ".join(words[i:i + n]) for i in range(max(1, len(words) - n + 1))}


def jaccard(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


# Word-level cues a test-wise candidate can see. Projects add their own languages
# with spec.cues = {"fr": {"absolutes": [...], "hedges": [...], "negations": [...]}}.
CUES = {
    "en": {
        "absolutes": r"\b(only|solely|exclusively|always|never|need not|in all cases|without exception|under no circumstances|at no time|regardless|none)\b",
        "hedges": r"\b(reasonabl[ey]|appropriate(ly)?|generally|usually|normally|typically|practicable|sufficient|adequate|where necessary|if necessary|may|might)\b",
        "negations": r"\b(not|no|never|neither|nor|without|cannot)\b|n't\b",
    },
    "zh": {
        "absolutes": r"只|僅|仅|一律|無須|无须|毋須|總是|总是|從不|从不|絕不|绝不|唯一|完全|必定|任何情況|任何情况",
        "hedges": r"合理|適當|适当|適切|一般|通常|可能|盡快|尽快|足夠|足够|視乎|视乎|酌情|可以|可",
        "negations": r"不|沒有|没有|無|无|非|未|毋|勿",
    },
}
MONEY = r"[$€£¥]|\b(hk\$|us\$|usd|hkd|eur|gbp|rmb|cny)\b|元|圓"


def cue_patterns(spec, lang):
    extra = (spec.get("cues") or {}).get(lang)
    if extra:
        return {k: re.compile("|".join(re.escape(w) for w in v), re.I) for k, v in extra.items()}
    base = CUES["zh"] if lang.lower().startswith(("zh", "ja")) else CUES.get(lang.split("-")[0].lower())
    if not base:
        return {}
    return {k: re.compile(v, re.I) for k, v in base.items()}


def cues(text, pats):
    t = norm(text)
    out = {k: bool(p.search(t)) for k, p in pats.items()}
    out["digits"] = bool(re.search(r"\d", t))
    out["money"] = bool(re.search(MONEY, t))
    out["paren"] = "(" in t or "（" in (text or "")
    out["semicolon"] = ";" in t or "；" in (text or "")
    return out


# Positional references break when the app reorders options or statements.
POSITIONAL = [
    re.compile(r"(?i:\b(option|answer|choice|alternative))\s*\(?[A-H1-9]\)?(?![\w']|[,.]\d)"),
    re.compile(r"(?i:\bstatements?)\s*\(?\d"),
    re.compile(r"(?i:\b(?:item|point))\s*\(?\d+\)?\s*(?i:above|below)"),
    re.compile(r"選項\s*[A-Ha-h甲乙丙丁戊1-9]|选项\s*[A-Ha-h甲乙丙丁戊1-9]|第\s*[一二三四五六七八九1-9]\s*(項|项|句|個陳述|个陈述)|陳述\s*[1-9]|陈述\s*[1-9]|句子\s*[1-9]"),
]
LEANING = [
    re.compile(r"(?i:\b(the (above|former|latter)|as (stated|mentioned) above|the previous statement)\b)"),
    re.compile(r"上述|上列|前述|前者|後者|后者|以上各項|以上各项"),
]
ALLNONE = re.compile(r"(?i:\b(all|none|both|neither) of the (above|options|statements)\b)|以上皆|以上都|以上均|以上全|皆非|皆是|都不是|都是對|都正确|都正確")


# ---------------------------------------------------------------- combination options

TEMPLATES = {
    3: [("ones-pairs", [[1], [2], [1, 3], [2, 3]], 0.5),
        ("pairs-ones", [[1, 2], [1, 3], [2], [3]], 0.5)],
    4: [("triples", [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], 0.45),
        ("pairs", [[1, 2], [1, 3], [2, 4], [3, 4]], 0.15),
        ("pairs-triples", [[1, 2], [1, 2, 3], [1, 3, 4], [3, 4]], 0.15),
        ("ones-triples", [[1], [1, 2, 3], [2, 3, 4], [4]], 0.10),
        ("ones-pairs", [[1], [1, 2], [3], [3, 4]], 0.15)],
    5: [("fours", [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5]], 0.41),
        ("triples-fours", [[1, 2, 3], [1, 2, 4], [1, 3, 4, 5], [2, 3, 4, 5]], 0.20),
        ("triples", [[1, 2, 3], [1, 2, 4], [1, 3, 5], [1, 4, 5]], 0.13),
        ("pairs-triples", [[1, 2], [1, 3], [2, 4, 5], [3, 4, 5]], 0.09),
        ("pairs-triples-b", [[1, 2], [1, 3, 4], [2, 3, 5], [4, 5]], 0.09),
        ("ones-pairs", [[1], [2], [3, 4], [3, 5]], 0.08)],
    6: [("fives", [[1, 2, 3, 4, 5], [1, 2, 3, 4, 6], [1, 2, 3, 5, 6], [1, 2, 4, 5, 6]], 0.40),
        ("fours-fives", [[1, 2, 3, 4], [1, 2, 3, 5, 6], [1, 2, 4, 5, 6], [3, 4, 5, 6]], 0.20),
        ("fours", [[1, 2, 3, 4], [1, 2, 3, 5], [1, 4, 5, 6], [2, 4, 5, 6]], 0.20),
        ("triples-fours", [[1, 2, 3], [1, 2, 3, 4], [1, 4, 5, 6], [4, 5, 6]], 0.15),
        ("triples", [[1, 2, 3], [1, 4, 5], [2, 4, 6], [3, 5, 6]], 0.05),
        ("pairs-triples", [[1, 2], [3, 4], [1, 2, 5], [3, 4, 6]], 0.05),
        ("ones-pairs", [[1], [2], [3, 4], [5, 6]], 0.05)],
}


def option_set(opt, n):
    if opt == ALL:
        return frozenset(range(1, n + 1))
    if opt == NONE:
        return frozenset()
    return frozenset(opt)


def canonical(options, n):
    """Display order: smaller sets first, then by number; all/none last."""
    sets = sorted((sorted(o) for o in options if o not in (ALL, NONE)), key=lambda o: (len(o), o))
    return sets + [o for o in options if o in (ALL, NONE)]


def relabel(members, member, key, n, rng):
    src_in, src_out = sorted(member), [i for i in range(1, n + 1) if i not in member]
    dst_in, dst_out = sorted(key), [i for i in range(1, n + 1) if i not in key]
    rng.shuffle(dst_in)
    rng.shuffle(dst_out)
    m = dict(zip(src_in + src_out, dst_in + dst_out))
    return [sorted(m[x] for x in s) for s in members]


def generate_options(truth, rng, none_share=0.05):
    """Four symmetric subsets and an all/none option, with the key placed on a
    random member of its size. Returns (options, answer)."""
    n = len(truth)
    key = {i + 1 for i, t in enumerate(truth) if t}
    k = len(key)
    if n not in TEMPLATES:
        raise ValueError(f"{n} statements: generated option sets cover 3 to 6; give options by hand")
    templates = TEMPLATES[n]
    if 0 < k < n:
        weights = [w * sum(1 for s in mem if len(s) == k) for _, mem, w in templates]
        if not any(weights):
            raise ValueError(f"no template has a {k}-of-{n} option; give options by hand")
        _, members, _ = rng.choices(templates, weights=weights)[0]
        member = rng.choice([s for s in members if len(s) == k])
        body = relabel(members, member, key, n, rng)
        token = NONE if rng.random() < none_share else ALL
    else:
        _, members, _ = rng.choices(templates, weights=[w for _, _, w in templates])[0]
        perm = list(range(1, n + 1))
        rng.shuffle(perm)
        body = [sorted(perm[x - 1] for x in s) for s in members]
        token = ALL if k == n else NONE
    options = canonical(body + [token], n)
    hits = [i for i, o in enumerate(options) if option_set(o, n) == frozenset(key)]
    assert len(hits) == 1, (options, key)
    return options, hits[0]


def option_label(opt, lang):
    zh = lang.lower().startswith("zh")
    if opt == ALL:
        return "以上皆是" if zh else "All of the above"
    if opt == NONE:
        return "以上皆非" if zh else "None of the above"
    xs = [str(x) for x in opt]
    if len(xs) == 1:
        return f"只有 {xs[0]}" if zh else f"{xs[0]} only"
    return ("、".join(xs[:-1]) + " 及 " + xs[-1]) if zh else (", ".join(xs[:-1]) + " and " + xs[-1])


# ---------------------------------------------------------------- check


class Report:
    def __init__(self):
        self.errors, self.warnings, self.info = [], [], []

    def err(self, iid, msg):
        self.errors.append((iid, msg))

    def warn(self, iid, msg):
        self.warnings.append((iid, msg))


def lang_fields(item, lang):
    v = item.get(lang)
    return v if isinstance(v, dict) else None


def same_len(rep, iid, item, ls, field, need=True, minimum=1):
    lens = {}
    for lang in ls:
        f = lang_fields(item, lang) or {}
        v = f.get(field)
        if v is None:
            if need:
                rep.err(iid, f"{lang}: missing '{field}'")
            continue
        if not isinstance(v, list):
            rep.err(iid, f"{lang}: '{field}' must be a list")
            continue
        if len(v) < minimum:
            rep.err(iid, f"{lang}: '{field}' needs at least {minimum} entries")
        if any(not isinstance(x, str) or not x.strip() for x in v):
            rep.err(iid, f"{lang}: '{field}' has an empty or non-text entry")
        lens[lang] = len(v)
    if len(set(lens.values())) > 1:
        rep.err(iid, f"'{field}' lengths differ between languages: {lens}")
    return next(iter(lens.values()), None)


def check_kind(rep, spec, item, ls):
    iid, k = item.get("id"), item.get("kind")
    if k in ("single", "multi"):
        n = same_len(rep, iid, item, ls, "options", minimum=2)
        same_len(rep, iid, item, ls, "option_notes", need=False)
        if n is None:
            return
        a = item.get("answer")
        if k == "single":
            if not isinstance(a, int) or isinstance(a, bool) or not 0 <= a < n:
                rep.err(iid, f"answer must be an option index 0-{n - 1}")
        else:
            if (not isinstance(a, list) or not a or len(set(a)) != len(a)
                    or not all(isinstance(x, int) and not isinstance(x, bool) and 0 <= x < n for x in a)):
                rep.err(iid, f"answer must be a non-empty list of distinct option indexes 0-{n - 1}")
        pin = item.get("pin_last", 0)
        if not isinstance(pin, int) or not 0 <= pin < n:
            rep.err(iid, "pin_last must be a count smaller than the number of options")
        if shuffles(spec, item):
            for lang in ls:
                opts = (lang_fields(item, lang) or {}).get("options") or []
                for j, o in enumerate(opts):
                    if isinstance(o, str) and ALLNONE.search(o) and j < n - pin:
                        rep.err(iid, f"{lang}: option {j} reads as all/none of the above but is shuffled; pin it with pin_last or reword")
    elif k == "tf":
        if not isinstance(item.get("answer"), bool):
            rep.err(iid, "answer must be true or false")
        tr = item.get("traps")
        if tr is not None and not isinstance(tr, (str, type(None), list)):
            rep.err(iid, "traps must be a code or null")
    elif k == "combo":
        n = same_len(rep, iid, item, ls, "statements", minimum=2)
        same_len(rep, iid, item, ls, "statement_notes", need=False)
        truth = item.get("truth")
        if not isinstance(truth, list) or not all(isinstance(t, bool) for t in truth):
            rep.err(iid, "truth must be a list of true/false")
            return
        if n is not None and len(truth) != n:
            rep.err(iid, f"truth has {len(truth)} values for {n} statements")
            return
        n = len(truth)
        traps = item.get("traps")
        if traps is not None:
            if not isinstance(traps, list) or len(traps) != n:
                rep.err(iid, "traps must list one code (or null) per statement")
            else:
                for t, c in zip(truth, traps):
                    if t and c is not None:
                        rep.err(iid, "a true statement has a trap code")
                    if not t and c is None:
                        rep.warn(iid, "a false statement has no trap code")
                    if c is not None and c not in TRAP_CODES:
                        rep.warn(iid, f"trap code '{c}' is not one of the standard codes")
        opts = item.get("options")
        if opts is None:
            rep.err(iid, "no options: run 'bank_tool.py options' to generate them from truth")
            return
        if not isinstance(opts, list) or len(opts) < 2:
            rep.err(iid, "options must be a list of statement sets and all/none")
            return
        seen, tokens_seen = set(), False
        for j, o in enumerate(opts):
            if o in (ALL, NONE):
                tokens_seen = True
                key = o
            elif isinstance(o, list) and o and all(isinstance(x, int) and not isinstance(x, bool) for x in o):
                if tokens_seen:
                    rep.err(iid, f"option {j}: all/none must come after every statement set")
                if o != sorted(set(o)) or o[0] < 1 or o[-1] > n:
                    rep.err(iid, f"option {j}: {o} is not a sorted list of statement numbers 1-{n}")
                if len(set(o)) == n and not item.get("official"):
                    rep.warn(iid, f"option {j} lists every statement; 'all' says the same")
                key = tuple(o)
            else:
                rep.err(iid, f"option {j}: {o!r} is neither a statement set nor all/none")
                continue
            if key in seen:
                rep.err(iid, f"option {j}: {o} appears twice")
            seen.add(key)
        true_set = frozenset(i + 1 for i, t in enumerate(truth) if t)
        hits = [j for j, o in enumerate(opts) if (o in (ALL, NONE) or isinstance(o, list)) and option_set(o, n) == true_set]
        if len(hits) != 1:
            rep.err(iid, f"{len(hits)} options equal the true statements {sorted(true_set)}")
        elif item.get("answer") != hits[0]:
            rep.err(iid, f"answer is {item.get('answer')}, but option {hits[0]} equals the true statements")
    elif k == "match":
        nl = same_len(rep, iid, item, ls, "left", minimum=2)
        nr = same_len(rep, iid, item, ls, "right", minimum=2)
        a = item.get("answer")
        if nl is None or nr is None:
            return
        if a is None:
            if nl != nr:
                rep.err(iid, "left and right differ in length, so answer must map each left entry to a right index")
        elif (not isinstance(a, list) or len(a) != nl
              or not all(isinstance(x, int) and 0 <= x < nr for x in a)):
            rep.err(iid, f"answer must give a right index (0-{nr - 1}) for each of the {nl} left entries")
        elif len(set(a)) != len(a):
            rep.warn(iid, "two left entries map to the same right entry")
    elif k == "order":
        same_len(rep, iid, item, ls, "items", minimum=2)
    elif k == "cloze":
        for lang in ls:
            f = lang_fields(item, lang) or {}
            blanks = sorted({int(m) for m in re.findall(r"\{\{(\d+)\}\}", f.get("stem", ""))})
            ans = f.get("answers")
            if not blanks:
                rep.err(iid, f"{lang}: the stem has no {{{{1}}}} blank")
                continue
            if blanks != list(range(1, len(blanks) + 1)):
                rep.err(iid, f"{lang}: blanks must be numbered 1..n, found {blanks}")
            if (not isinstance(ans, list) or len(ans) != len(blanks)
                    or not all(isinstance(a, list) and a and all(isinstance(s, str) and s.strip() for s in a) for a in ans)):
                rep.err(iid, f"{lang}: answers must list accepted strings for each of {len(blanks)} blanks")
                continue
            ch = f.get("choices")
            if ch is not None:
                if not isinstance(ch, list) or len(ch) != len(blanks):
                    rep.err(iid, f"{lang}: choices must have one list per blank")
                else:
                    for b, (acc, opts) in enumerate(zip(ans, ch)):
                        if not any(norm(x) in {norm(o) for o in opts} for x in acc):
                            rep.err(iid, f"{lang}: blank {b + 1} has no accepted answer among its choices")
    elif k == "numeric":
        a = item.get("answer")
        if not isinstance(a, (int, float)) or isinstance(a, bool):
            rep.err(iid, "answer must be a number")
        for key in ("tolerance", "tolerance_pct"):
            v = item.get(key)
            if v is not None and (not isinstance(v, (int, float)) or v < 0):
                rep.err(iid, f"{key} must be a non-negative number")
    elif k in ("short", "essay"):
        total = None
        for lang in ls:
            f = lang_fields(item, lang) or {}
            if not (f.get("model_answer") or "").strip():
                rep.err(iid, f"{lang}: missing model_answer")
            rub, lev = f.get("rubric"), f.get("levels")
            if not rub and not lev:
                rep.err(iid, f"{lang}: a written answer needs a rubric (points) or levels")
                continue
            if rub:
                if not all(isinstance(r, dict) and r.get("text") and isinstance(r.get("marks"), (int, float)) for r in rub):
                    rep.err(iid, f"{lang}: every rubric point needs text and marks")
                    continue
                t = sum(r["marks"] for r in rub)
            else:
                if not all(isinstance(r, dict) and r.get("text") and isinstance(r.get("marks"), (int, float)) for r in lev):
                    rep.err(iid, f"{lang}: every level needs text and marks")
                    continue
                t = max(r["marks"] for r in lev)
            if total is not None and t != total:
                rep.err(iid, "mark schemes differ in total between languages")
            total = t
        pts = item.get("points")
        if total is not None and pts is not None and total < pts:
            rep.err(iid, f"points is {pts} but the mark scheme allows only {total}")


def text_fields(item, lang):
    f = lang_fields(item, lang) or {}
    out = []
    for key in ("stem", "explain", "model_answer"):
        if isinstance(f.get(key), str):
            out.append((key, f[key]))
    for key in ("options", "option_notes", "statements", "statement_notes", "left", "right", "items"):
        for j, v in enumerate(f.get(key) or []):
            if isinstance(v, str):
                out.append((f"{key}[{j}]", v))
    return out


def check(spec, bank, sources=None, notes=None):
    rep = Report()
    ls = langs(spec)
    sections = {str(s.get("id")): s for s in spec.get("sections", [])}
    if not sections:
        rep.err("spec", "spec has no sections")
    retired = set(spec.get("retired_ids") or [])
    ids = Counter(i.get("id") for i in bank["items"])
    for iid, c in ids.items():
        if c > 1:
            rep.err(iid, f"id used {c} times")
    pool = Counter()
    full_text = defaultdict(list)
    statements = defaultdict(list)
    for item in bank["items"]:
        iid = item.get("id")
        if not iid or not isinstance(iid, str):
            rep.err(str(iid), "every item needs a string id")
            continue
        if iid in retired:
            rep.err(iid, "id is retired and may not be reused")
        k = item.get("kind")
        if k not in KINDS:
            rep.err(iid, f"kind '{k}' is not one of {sorted(KINDS)}")
            continue
        sec = str(item.get("section"))
        if sec not in sections:
            rep.err(iid, f"section '{item.get('section')}' is not in the spec")
        else:
            pool[sec] += 1
        v = item.get("version", 1)
        if not isinstance(v, int) or v < 1:
            rep.err(iid, "version must be a positive integer")
        for lang in ls:
            f = lang_fields(item, lang)
            if f is None:
                rep.err(iid, f"no '{lang}' content")
                continue
            if not (f.get("stem") or "").strip():
                rep.err(iid, f"{lang}: empty stem")
            src = loc(item.get("source"), lang)
            if not src or not src.strip():
                rep.err(iid, f"{lang}: no source citation")
            elif not re.search(r"\d|§|¶|第|p\.|para|sec|ch\.|slide|page|頁|段|條|节|節", src, re.I):
                rep.warn(iid, f"{lang}: citation '{src}' has no locator a reader can turn to")
        if item.get("case") and item["case"] not in bank["cases"]:
            rep.err(iid, f"case '{item['case']}' is not defined in the bank's cases")
        check_kind(rep, spec, item, ls)
        if k in OBJECTIVE and k not in ("cloze", "numeric"):
            for lang in ls:
                f = lang_fields(item, lang) or {}
                notes_key = {"single": "option_notes", "multi": "option_notes", "combo": "statement_notes"}.get(k)
                if notes_key and not f.get(notes_key) and not f.get("explain"):
                    rep.warn(iid, f"{lang}: no explanations ({notes_key} or explain)")
        if shuffles(spec, item):
            for lang in ls:
                for field, text in text_fields(item, lang):
                    if field.startswith("options[") and k in ("single", "multi"):
                        j = int(field[8:-1])
                        n = len((lang_fields(item, lang) or {}).get("options") or [])
                        if j >= n - item.get("pin_last", 0):
                            continue
                    for p in POSITIONAL:
                        m = p.search(text)
                        if m:
                            rep.err(iid, f"{lang} {field}: positional reference '{m.group(0)}' breaks when the app reorders")
                    if k == "combo" and field.startswith(("statements", "statement_notes")):
                        for p in LEANING:
                            m = p.search(text)
                            if m:
                                rep.warn(iid, f"{lang} {field}: '{m.group(0)}' leans on another statement")
        for lang in ls:
            f = lang_fields(item, lang) or {}
            body = [f.get("stem", "")] + list(f.get("options") or []) + list(f.get("statements") or []) + list(f.get("left") or []) + list(f.get("items") or [])
            full_text[(lang, norm(" | ".join(x for x in body if isinstance(x, str))))].append(iid)
            if k == "combo":
                for s, t in zip(f.get("statements") or [], item.get("truth") or []):
                    if isinstance(s, str):
                        statements[(lang, norm(s))].append((iid, t))
            elif k == "tf" and isinstance(f.get("stem"), str):
                statements[(lang, norm(f["stem"]))].append((iid, item.get("answer")))
        for q in item.get("quotes") or []:
            if not isinstance(q, dict) or not q.get("text") or not q.get("doc"):
                rep.err(iid, "every quote needs doc and text")
    for (lang, _), owners in full_text.items():
        if len(owners) > 1:
            rep.err(owners[0], f"{lang}: same stem and options as {', '.join(owners[1:])}")
    for (lang, _), owners in statements.items():
        if len({o for o, _ in owners}) > 1:
            truths = {t for _, t in owners}
            who = ", ".join(sorted({o for o, _ in owners}))
            if len(truths) > 1:
                rep.err(owners[0][0], f"{lang}: one statement is keyed both true and false across {who}")
            else:
                rep.warn(owners[0][0], f"{lang}: the same statement appears in {who}")
    for sid, s in sections.items():
        draw = s.get("draw", 0) or 0
        if pool[sid] < draw:
            rep.err(f"section {sid}", f"{pool[sid]} items cannot fill a draw of {draw}")
        elif draw and draw < pool[sid] < 3 * draw:
            rep.warn(f"section {sid}", f"{pool[sid]} items for a draw of {draw}: candidates will soon recognise papers")
    near_duplicates(rep, spec, bank)
    near_twins(rep, statements)
    copied_from_quotes(rep, spec, bank)
    if sources:
        check_quotes(rep, spec, bank, Path(sources))
    if notes:
        page = Path(notes).read_text(encoding="utf-8", errors="replace")
        anchors = set(re.findall(r'\bid="([^"]+)"', page))
        for item in bank["items"]:
            a = item.get("notes_anchor")
            if a and a not in anchors:
                rep.err(item.get("id"), f"notes_anchor '{a}' is not an id in {notes}")
        notes_leaks(rep, spec, bank, page)
    return rep


BLOCK_TAGS = r"p|li|td|th|tr|div|section|aside|h[1-6]|dt|dd|caption|figcaption|blockquote|pre|br|hr|table|ul|ol"


def page_segments(page):
    """The readable text of an HTML or Markdown notes page, one string per paragraph,
    list item, heading or table cell, so words from neighbouring cells never join."""
    t = re.sub(r"(?is)<(script|style)\b.*?</\1>", "\n", page)
    t = re.sub(rf"(?is)</?({BLOCK_TAGS})\b[^>]*>", "\n", t)
    t = html.unescape(re.sub(r"(?s)<[^>]+>", "", t))
    return [s for line in t.splitlines() for s in line.split("|") if s.strip()]


def notes_leaks(rep, spec, bank, page):
    """False statements the notes repeat with their defect: a trap note that quotes
    the wrong version turns practice into recognition."""
    # a bilingual paragraph holds both languages: read it the way each statement is written
    texts = page_segments(page)
    by_script = {True: [seq_tokens(s, cjk=True) for s in texts], False: [seq_tokens(s, cjk=False) for s in texts]}
    if not texts:
        return
    for item in bank["items"]:
        k = item.get("kind")
        for lang in langs(spec):
            f = lang_fields(item, lang) or {}
            if k == "combo":
                false = [s for s, t in zip(f.get("statements") or [], item.get("truth") or []) if t is False]
            elif k == "tf" and item.get("answer") is False:
                false = [f.get("stem")]
            else:
                continue
            qs = [seq_tokens(q["text"]) for q in item.get("quotes") or []
                  if isinstance(q, dict) and isinstance(q.get("text"), str) and q.get("lang", lang) == lang]
            for s in false:
                if not isinstance(s, str) or not qs:
                    continue
                cjk = is_cjk(s)
                st = seq_tokens(s)
                q = max(qs, key=lambda q: covered(st, q, 4 if cjk else 3))
                changed = [op for op in difflib.SequenceMatcher(None, st, q, autojunk=False).get_opcodes() if op[0] != "equal"]
                if not changed:
                    continue
                # the false wording around the defect, and the source's wording it replaced
                ctx = 3 if cjk else 2
                wrong = st[max(0, min(o[1] for o in changed) - ctx):max(o[2] for o in changed) + ctx]
                right = q[max(0, min(o[3] for o in changed) - ctx):max(o[4] for o in changed) + ctx]
                if len(wrong) < (6 if cjk else 4):
                    continue

                def share(a, win):
                    return sum(m.size for m in difflib.SequenceMatcher(None, a, win, autojunk=False).get_matching_blocks() if m.size >= 2) / len(a)
                need = set(wrong)
                width, step = len(wrong) + len(wrong) // 2, max(1, len(wrong) // 3)
                windows = (seg[i:i + width] for seg in by_script[cjk] if seg for i in range(0, max(1, len(seg) - len(wrong) + 1), step))
                for win in windows:
                    if len(need & set(win)) < 0.6 * len(need):
                        continue
                    mw, mr = share(wrong, win), share(right, win)
                    if mw >= 0.6 and mw - mr >= 0.05:
                        near = "".join(win) if cjk else " ".join(win)
                        rep.warn(item.get("id"), f"{lang}: the notes echo a false statement's wrong version ('{near}'); state the rule as the source does instead")
                        break


def near_duplicates(rep, spec, bank, threshold=0.75):
    by_lang = defaultdict(list)
    for item in bank["items"]:
        if item.get("kind") in ("combo",):
            continue
        for lang in langs(spec):
            f = lang_fields(item, lang) or {}
            stem = f.get("stem")
            if isinstance(stem, str) and tlen(stem) > 20:
                by_lang[lang].append((item.get("id"), shingles(stem)))
    for lang, rows in by_lang.items():
        index = defaultdict(set)
        for n, (_, sh) in enumerate(rows):
            for s in sh:
                index[s].add(n)
        reported = set()
        for n, (iid, sh) in enumerate(rows):
            cand = Counter()
            for s in sh:
                for m in index[s]:
                    if m > n:
                        cand[m] += 1
            for m, _ in cand.items():
                j = jaccard(sh, rows[m][1])
                if j >= threshold and (n, m) not in reported:
                    reported.add((n, m))
                    rep.warn(iid, f"{lang}: stem {j:.0%} similar to {rows[m][0]}")


def near_twins(rep, statements, ratio=0.8):
    """Statements in different items that differ by a word or a number and are
    keyed opposite ways: on one paper, the true one marks the other false."""
    rows = defaultdict(list)
    for (lang, text), owners in statements.items():
        for iid, truth in owners:
            if isinstance(truth, bool):
                rows[lang].append((iid, truth, text, shingles(text, 2)))
    for lang, rs in rows.items():
        index = defaultdict(set)
        for n, r in enumerate(rs):
            for s in r[3]:
                index[s].add(n)
        seen = set()
        for n, (iid, truth, text, sh) in enumerate(rs):
            cand = Counter(m for s in sh for m in index[s] if m > n)
            for m, shared in cand.items():
                jid, jtruth, jtext, jsh = rs[m]
                if jid == iid or jtruth == truth or text == jtext or shared < 2 or (iid, jid) in seen:
                    continue
                if difflib.SequenceMatcher(None, text, jtext).ratio() >= ratio:
                    seen.add((iid, jid))
                    rep.warn(iid, f"{lang}: a statement keyed {truth} nearly repeats one keyed {jtruth} in {jid}; on one paper either gives the other away")


def seq_tokens(text, cjk=None):
    """The text as a sequence: characters for CJK, words otherwise (or as `cjk` says)."""
    t = norm(text).lower()
    if is_cjk(t) if cjk is None else cjk:
        return [c for c in t if c.isalnum()]
    return re.findall(r"\w+", t)


def shared_run(a, b):
    """The longest run of consecutive tokens a and b share."""
    if not a or not b:
        return 0
    return difflib.SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b)).size


def covered(a, b, block):
    """How many tokens of a lie in runs of at least `block` tokens shared with b, in
    order: source text that was only cut down or joined counts in full."""
    if not a or not b:
        return 0
    blocks = difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks()
    return sum(m.size for m in blocks if m.size >= block)


def copied_from_quotes(rep, spec, bank):
    """Keys lifted from the source among reworded distractors, and true statements
    copied whole: a candidate finds them by matching the wording, not knowing the rule."""
    for item in bank["items"]:
        k, iid = item.get("kind"), item.get("id")
        for lang in langs(spec):
            qs = [seq_tokens(q["text"]) for q in item.get("quotes") or []
                  if isinstance(q, dict) and isinstance(q.get("text"), str) and q.get("lang", lang) == lang]
            if not qs:
                continue
            f = lang_fields(item, lang) or {}

            def run(s):
                return max(shared_run(seq_tokens(s), q) for q in qs)

            def floor(s):
                return 10 if is_cjk(s) else 6
            if k in ("single", "multi"):
                opts = [o for o in f.get("options") or [] if isinstance(o, str)]
                keys = {item.get("answer")} if k == "single" else set(item.get("answer") or [])
                keys = {j for j in keys if isinstance(j, int) and 0 <= j < len(opts)}
                if not keys or len(keys) == len(opts):
                    continue
                kj = max(keys, key=lambda j: run(opts[j]))
                kr = run(opts[kj])
                dr = max(run(o) for j, o in enumerate(opts) if j not in keys)
                margin = 3 if is_cjk(opts[kj]) else 2
                if kr >= floor(opts[kj]) and dr <= kr - margin:
                    unit = "characters" if is_cjk(opts[kj]) else "words"
                    rep.warn(iid, f"{lang}: the key copies {kr} consecutive {unit} of its quote, {kr - dr} more than any distractor; paraphrase it")
            elif k in ("combo", "tf"):
                pairs = list(zip(f.get("statements") or [], item.get("truth") or [])) if k == "combo" else [(f.get("stem"), item.get("answer"))]
                for n, (s, truth) in enumerate(pairs, 1):
                    if truth is True and isinstance(s, str):
                        st = seq_tokens(s)
                        block = 4 if is_cjk(s) else 3
                        r = max(covered(st, q, block) for q in qs)
                        where = f"statement {n}" if k == "combo" else "the statement"
                        unit = "characters" if is_cjk(s) else "words"
                        if len(st) >= floor(s) and r >= 0.8 * len(st):
                            rep.warn(iid, f"{lang}: {where} is true and {r} of its {len(st)} {unit} are its quote's own text; paraphrase it")
                            continue
                        least = 8 if is_cjk(s) else 6
                        for clause in re.split(r"[,;:，；：、。]", s):
                            ct = seq_tokens(clause)
                            if len(ct) >= least and any(shared_run(ct, q) >= 0.9 * len(ct) for q in qs):
                                rep.warn(iid, f"{lang}: {where} is true and repeats a clause of its quote word for word ('{clause.strip()}'); paraphrase it")
                                break


def source_texts(sources):
    """{(lang or None, doc): text} from DIR/<doc>*.txt or DIR/<lang>/<doc>*.txt."""
    out = {}
    for p in sources.rglob("*.txt"):
        m = re.match(r"([0-9A-Za-z]+)", p.stem)
        if not m:
            continue
        rel = p.relative_to(sources).parts
        lang = rel[0] if len(rel) > 1 else None
        out[(lang, m.group(1))] = p
    return out


def check_quotes(rep, spec, bank, sources):
    files = source_texts(sources)
    cache = {}

    def read(key):
        if key not in cache:
            raw = files[key].read_text(encoding="utf-8", errors="replace")
            t = norm(strip_pages(raw))
            cache[key] = (t, re.sub(r"\s", "", t))
        return cache[key]

    def text_for(lang, doc):
        """The text of `doc` in `lang`: LANG/doc*.txt (folder named by the language
        code or its first part), else doc*.txt, else the only copy there is."""
        cands = [key for key in files if key[1] == doc]
        if not cands:
            return None
        if lang:
            want = lang.lower()
            for key in cands:
                if key[0] and key[0].lower() == want:
                    return read(key)
            for key in cands:
                if key[0] and key[0].lower() == want.split("-")[0]:
                    return read(key)
        for key in cands:
            if key[0] is None:
                return read(key)
        return read(cands[0]) if not lang or len(cands) == 1 else None

    for item in bank["items"]:
        for q in item.get("quotes") or []:
            if not isinstance(q, dict) or not q.get("text"):
                continue
            doc, lang = str(q.get("doc")), q.get("lang")
            got = text_for(lang, doc)
            if got is None:
                rep.err(item.get("id"), f"quote cites document '{doc}', which has no extracted text in {sources}")
                continue
            text, squeezed = got
            nq = norm(q["text"])
            if nq in text or re.sub(r"\s", "", nq) in squeezed:
                continue
            sh = shingles(q["text"])
            hay = text
            hit = sum(1 for s in sh if s in hay) / len(sh) if sh else 0
            if hit >= 0.9:
                rep.warn(item.get("id"), f"quote from {doc} found only approximately ({hit:.0%} of its 4-grams)")
            else:
                rep.err(item.get("id"), f"quote not found in document {doc}: '{q['text'][:60]}…'")


def cmd_check(a):
    spec, bank, _ = load(a.spec, a.bank)
    rep = check(spec, bank, a.sources, a.notes)
    if a.json:
        print(json.dumps({"errors": rep.errors, "warnings": rep.warnings}, ensure_ascii=False, indent=1))
    else:
        for iid, msg in rep.errors:
            print(f"ERROR {iid}: {msg}")
        shown = rep.warnings[: a.max_warnings]
        for iid, msg in shown:
            print(f"warn  {iid}: {msg}")
        if len(rep.warnings) > len(shown):
            print(f"… {len(rep.warnings) - len(shown)} more warnings (--max-warnings)")
        print(f"{len(bank['items'])} items: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 1 if rep.errors else 0


# ---------------------------------------------------------------- tells


def item_options(spec, item, lang):
    """Options as (texts, key index or None) for the kinds a guesser can sit."""
    f = lang_fields(item, lang) or {}
    k = item.get("kind")
    if k == "single":
        return f.get("options") or [], item.get("answer")
    return None, None


def single_features(stem, opts, pats):
    lens = [tlen(o) for o in opts]
    mean = statistics.mean(lens)
    sd = statistics.pstdev(lens) or 1.0
    order = sorted(lens)
    stem_tok = tokens(stem)
    tok = [tokens(o) for o in opts]
    rows = []
    for j, o in enumerate(opts):
        L = lens[j]
        others = [x for i, x in enumerate(lens) if i != j]
        nearest = min(others, key=lambda x: abs(x - L)) if others else L
        longest = L == order[-1]
        shortest = L == order[0]
        c = cues(o, pats)
        conv = statistics.mean(jaccard(tok[j], tok[i]) for i in range(len(opts)) if i != j) if len(opts) > 1 else 0
        rows.append([
            (L - mean) / sd,
            1.0 if longest else 0.0,
            1.0 if shortest else 0.0,
            1.0 if longest and L > nearest * 1.15 and L - nearest >= 8 else 0.0,
            1.0 if shortest and L < nearest / 1.15 and nearest - L >= 8 else 0.0,
            jaccard(stem_tok, tok[j]),
            conv,
        ] + [1.0 if c.get(key) else 0.0 for key in ("absolutes", "hedges", "negations", "digits", "money", "paren", "semicolon")])
    return rows


def statement_features(stem, sts, pats):
    lens = [tlen(s) for s in sts]
    mean = statistics.mean(lens)
    sd = statistics.pstdev(lens) or 1.0
    stem_tok = tokens(stem)
    out = []
    for j, s in enumerate(sts):
        L = lens[j]
        others = [x for i, x in enumerate(lens) if i != j]
        nearest = min(others, key=lambda x: abs(x - L)) if others else L
        c = cues(s, pats)
        out.append([
            (L - mean) / sd,
            1.0 if L == max(lens) and L > nearest * 1.15 else 0.0,
            1.0 if L == min(lens) and L < nearest / 1.15 else 0.0,
            jaccard(stem_tok, tokens(s)),
        ] + [1.0 if c.get(key) else 0.0 for key in ("absolutes", "hedges", "negations", "digits", "money", "paren", "semicolon")])
    return out


def combo_features(stem, sts, options, pats):
    n = len(sts)
    sf = statement_features(stem, sts, pats)
    d = len(sf[0])
    sets = [option_set(o, n) for o in options]
    pop = Counter(s for st in sets for s in st)
    rows = []
    for j, st in enumerate(sets):
        inside = [sf[s - 1] for s in st]
        outside = [sf[s - 1] for s in range(1, n + 1) if s not in st]
        diff = []
        for f in range(d):
            a = statistics.mean(r[f] for r in inside) if inside else 0.0
            b = statistics.mean(r[f] for r in outside) if outside else 0.0
            diff.append(a - b)
        conv = statistics.mean(jaccard(set(st), set(sets[i])) for i in range(len(sets)) if i != j)
        popularity = statistics.mean(pop[s] / len(sets) for s in st) if st else 0.0
        rows.append(diff + [len(st) / n, popularity, conv,
                            1.0 if options[j] == ALL else 0.0, 1.0 if options[j] == NONE else 0.0])
    return rows


def tf_features(stem, pats):
    f = statement_features(stem, [stem], pats)[0]
    return [f, [0.0] * len(f)]


def build_rows(spec, bank, lang):
    """[(item id, section, feature rows, key index, kind)] for single, combo and tf items."""
    pats = cue_patterns(spec, lang)
    out = []
    for item in bank["items"]:
        f = lang_fields(item, lang) or {}
        k = item.get("kind")
        try:
            if k == "single" and f.get("options"):
                out.append((item["id"], str(item.get("section")), single_features(f.get("stem", ""), f["options"], pats), item.get("answer"), k))
            elif k == "combo" and f.get("statements") and item.get("options"):
                out.append((item["id"], str(item.get("section")), combo_features(f.get("stem", ""), f["statements"], item["options"], pats), item.get("answer"), k))
            elif k == "tf" and f.get("stem"):
                out.append((item["id"], str(item.get("section")), tf_features(f["stem"], pats), 0 if item.get("answer") else 1, k))
        except (ValueError, statistics.StatisticsError, IndexError, TypeError):
            continue
    return out


def softmax(scores):
    m = max(scores)
    e = [math.exp(s - m) for s in scores]
    z = sum(e)
    return [x / z for x in e]


def fit_logit(rows, iters=200, lr=0.5, l2=0.01):
    d = len(rows[0][2][0])
    w = [0.0] * d
    n = len(rows)
    for _ in range(iters):
        g = [0.0] * d
        for _, _, X, key, _ in rows:
            p = softmax([sum(wi * xi for wi, xi in zip(w, x)) for x in X])
            for j, x in enumerate(X):
                coef = (1.0 if j == key else 0.0) - p[j]
                if coef:
                    for f in range(d):
                        g[f] += coef * x[f]
        w = [wi + lr * (gi / n - l2 * wi) for wi, gi in zip(w, g)]
    return w


def pick_right(w, X, key):
    s = [sum(wi * xi for wi, xi in zip(w, x)) for x in X]
    best = max(s)
    tied = [j for j, v in enumerate(s) if abs(v - best) < 1e-9]
    return (1.0 / len(tied)) if key in tied else 0.0


def cross_validate(rows, folds=5, seed=1):
    by_kind = defaultdict(list)
    for r in rows:
        by_kind[r[4]].append(r)
    result = {}
    for kind, rs in by_kind.items():
        if len(rs) < 20:
            continue
        rng = random.Random(seed)
        idx = list(range(len(rs)))
        rng.shuffle(idx)
        k = min(folds, len(rs))
        for f in range(k):
            test = [rs[i] for i in idx[f::k]]
            held = set(idx[f::k])
            train = [rs[i] for i in idx if i not in held]
            w = fit_logit(train)
            for r in test:
                result[r[0]] = pick_right(w, r[2], r[3])
    return result


def heuristic(rows, col, sign=1):
    """Share of keys picked by 'choose the option with the highest feature col'."""
    hits, chance = 0.0, 0.0
    for _, _, X, key, _ in rows:
        vals = [sign * x[col] for x in X]
        best = max(vals)
        tied = [j for j, v in enumerate(vals) if abs(v - best) < 1e-9]
        hits += (1.0 / len(tied)) if key in tied else 0.0
        chance += 1.0 / len(X)
    return hits / len(rows), chance / len(rows)


def pass_rule_ok(spec, by_section, earned, maximum):
    rule = (spec.get("paper") or {}).get("pass") or {}
    total = sum(earned.values())
    total_max = sum(maximum.values())
    if rule.get("min_score") is not None and total < rule["min_score"]:
        return False
    if rule.get("min_percent") is not None and total_max and 100 * total / total_max < rule["min_percent"]:
        return False
    for sec, results in by_section.items():
        if rule.get("min_per_section") is not None and earned[sec] < rule["min_per_section"]:
            return False
        if rule.get("max_wrong_per_section") is not None and sum(1 for r in results if not r) > rule["max_wrong_per_section"]:
            return False
    return True


def simulate(spec, bank, chance_of, papers, seed):
    rng = random.Random(seed)
    pools = defaultdict(list)
    retired = set(spec.get("retired_ids") or [])
    for item in bank["items"]:
        if item.get("id") not in retired:
            pools[str(item.get("section"))].append(item)
    passes, scores = 0, []
    for _ in range(papers):
        by_section, earned, maximum = {}, Counter(), Counter()
        for s in spec.get("sections", []):
            sid = str(s.get("id"))
            draw = min(s.get("draw", 0) or 0, len(pools[sid]))
            picked = rng.sample(pools[sid], draw)
            res = []
            for item in picked:
                pts = item.get("points", 1)
                ok = rng.random() < chance_of(item)
                res.append(ok)
                earned[sid] += pts if ok else 0
                maximum[sid] += pts
            by_section[sid] = res
        scores.append(sum(earned.values()))
        passes += pass_rule_ok(spec, by_section, earned, maximum)
    return passes / papers if papers else 0, statistics.mean(scores) if scores else 0


def option_count(item):
    k = item.get("kind")
    if k in ("single", "multi"):
        for v in item.values():
            if isinstance(v, dict) and v.get("options"):
                return len(v["options"])
    if k == "combo":
        return len(item.get("options") or []) or 5
    if k == "tf":
        return 2
    return 0


def cmd_tells(a):
    spec, bank, _ = load(a.spec, a.bank)
    items = bank["items"]
    print(f"# Tells report: {len(items)} items\n")
    print("Chance is what a candidate gets by guessing uniformly. A strategy well above")
    print("chance is a tell to find; state the ceiling with every percentage.\n")
    for lang in langs(spec):
        pats = cue_patterns(spec, lang)
        print(f"## {lang}\n")
        singles = [it for it in items if it.get("kind") == "single" and (lang_fields(it, lang) or {}).get("options")]
        if singles:
            print("### Single-best options\n")
            print("| Section | Items | Key longest | Chance | Key shortest | Standout option is key | Spread > 40% |")
            print("|---|---|---|---|---|---|---|")
            groups = defaultdict(list)
            for it in singles:
                groups[str(it.get("section"))].append(it)
            for sec in sorted(groups) + ["all"]:
                rows = singles if sec == "all" else groups[sec]
                kl = ks = chance = spread = 0.0
                so_n = so_key = 0
                for it in rows:
                    opts = lang_fields(it, lang)["options"]
                    lens = [tlen(o) for o in opts]
                    key = it.get("answer", 0)
                    mx, mn = max(lens), min(lens)
                    kl += (1 / lens.count(mx)) if lens[key] == mx else 0
                    ks += (1 / lens.count(mn)) if lens[key] == mn else 0
                    chance += 1 / len(opts)
                    if (mx - mn) > 0.4 * statistics.mean(lens) and (mx - mn) >= 20:
                        spread += 1
                    srt = sorted(lens)
                    floor = 3 if is_cjk(" ".join(opts)) else 8
                    for j, L in enumerate(lens):
                        others = [x for i, x in enumerate(lens) if i != j]
                        near = min(others, key=lambda x: abs(x - L))
                        if (L == srt[-1] and L > near * 1.15 and L - near >= floor) or (L == srt[0] and L < near / 1.15 and near - L >= floor):
                            so_n += 1
                            so_key += j == key
                n = len(rows)
                so = f"{so_key}/{so_n}" if so_n else "—"
                print(f"| {sec} | {n} | {kl / n:.0%} | {chance / n:.0%} | {ks / n:.0%} | {so} | {spread / n:.0%} |")
            print()
        # statements: combo statements, tf statements, multi options
        rows = []
        for it in items:
            f = lang_fields(it, lang) or {}
            if it.get("kind") == "combo":
                rows += list(zip(f.get("statements") or [], it.get("truth") or []))
            elif it.get("kind") == "tf" and f.get("stem"):
                rows.append((f["stem"], it.get("answer")))
            elif it.get("kind") == "multi":
                keys = set(it.get("answer") or [])
                rows += [(o, j in keys) for j, o in enumerate(f.get("options") or [])]
        if rows:
            base = sum(1 for _, t in rows if t) / len(rows)
            print("### Statements: how often a statement with this cue is true\n")
            print(f"Base rate: {base:.0%} true of {len(rows)} statements.\n")
            print("| Cue | Statements | True | Gap from base |")
            print("|---|---|---|---|")
            for cue in list(pats) + ["digits", "money", "paren", "semicolon"]:
                hit = [t for s, t in rows if cues(s, pats).get(cue)]
                if len(hit) >= 5:
                    r = sum(1 for t in hit if t) / len(hit)
                    flag = " ⚠" if abs(r - base) > 0.15 and len(hit) >= 10 else ""
                    print(f"| {cue} | {len(hit)} | {r:.0%} | {r - base:+.0%}{flag} |")
            print()
        combos = [it for it in items if it.get("kind") == "combo" and it.get("options")]
        if combos and lang == langs(spec)[0]:
            print("### Combination items\n")
            tc = Counter((len(it["truth"]), sum(it["truth"])) for it in combos)
            false_counts = Counter(len(it["truth"]) - sum(it["truth"]) for it in combos)
            print("False statements per item: " + ", ".join(f"{k} false: {v}" for k, v in sorted(false_counts.items())))
            keys = Counter(it["answer"] for it in combos)
            print("Key position: " + ", ".join(f"{'abcdefgh'[k]}) {v / len(combos):.0%}" for k, v in sorted(keys.items())))
            allkey = sum(1 for it in combos if it["options"][it["answer"]] == ALL) / len(combos)
            print(f"'All of the above' is the key in {allkey:.0%} of items.\n")
        rows = build_rows(spec, bank, lang)
        if rows:
            print("### Surface strategies (no source, no knowledge)\n")
            print("| Strategy | Items | Picks the key | Chance |")
            print("|---|---|---|---|")
            s_rows = [r for r in rows if r[4] == "single"]
            c_rows = [r for r in rows if r[4] == "combo"]
            named = []
            if s_rows:
                named += [("single: pick the longest", s_rows, 1, 1), ("single: pick the shortest", s_rows, 2, 1),
                          ("single: most like the other options", s_rows, 6, 1), ("single: most like the stem", s_rows, 5, 1),
                          ("single: pick a hedged option", s_rows, 8, 1), ("single: avoid absolutes", s_rows, 7, -1)]
            if c_rows:
                d = len(statement_features("", ["x", "y"], pats)[0])
                named += [("combo: absolutes false", c_rows, 4, -1), ("combo: hedges true", c_rows, 5, 1),
                          ("combo: negations false", c_rows, 6, -1),
                          ("combo: most popular statements", c_rows, d + 1, 1), ("combo: most like the other options", c_rows, d + 2, 1)]
            for name, rs, col, sign in named:
                if col < len(rs[0][2][0]):
                    hit, ch = heuristic(rs, col, sign)
                    print(f"| {name} | {len(rs)} | {hit:.0%} | {ch:.0%} |")
            print()
            cv = cross_validate(rows, seed=a.seed)
            if cv:
                print("### A guesser learnt from the bank itself\n")
                print("A conditional logit over every surface feature above, trained on the bank's")
                print("own keys and scored only on items it never saw (5-fold cross-validation).\n")
                print("| Kind | Items | Picks the key | Chance |")
                print("|---|---|---|---|")
                for kind in ("single", "combo", "tf"):
                    rs = [r for r in rows if r[4] == kind and r[0] in cv]
                    if rs:
                        hit = sum(cv[r[0]] for r in rs) / len(rs)
                        ch = sum(1 / len(r[2]) for r in rs) / len(rs)
                        print(f"| {kind} | {len(rs)} | {hit:.0%} | {ch:.0%} |")
                print()
                by_id = {it["id"]: it for it in items}

                def guess(item):
                    return cv.get(item["id"], 0.0)

                def blind(item):
                    n = option_count(item)
                    if not n:
                        return 0.0
                    if item.get("kind") == "multi":
                        return 1 / (2 ** n - 1)
                    return 1 / n if item.get("kind") in ("single", "combo", "tf") else 0.0

                p_g, s_g = simulate(spec, bank, guess, a.papers, a.seed)
                p_c, s_c = simulate(spec, bank, blind, a.papers, a.seed)
                print(f"### {a.papers} simulated papers under the spec's draw and pass rule\n")
                print(f"- Learnt guesser: mean score {s_g:.1f}, pass rate {p_g:.2%}.")
                print(f"- Uniform guessing: mean score {s_c:.1f}, pass rate {p_c:.2%}.")
                print("- Items the guesser cannot sit (written, cloze, numeric, order, match) score zero for it.\n")
                _ = by_id
            else:
                print("(Too few items of one kind, under 20, to train a guesser.)\n")
    return 0


# ---------------------------------------------------------------- options


def dump_like(raw, path):
    text = Path(path).read_bytes().decode("utf-8-sig")
    crlf = "\r\n" in text
    out = json.dumps(raw, ensure_ascii=False, indent=2) + "\n"
    if crlf:
        out = out.replace("\n", "\r\n")
    Path(path).write_bytes(out.encode("utf-8"))


def cmd_options(a):
    spec, bank, raw = load(a.spec, a.bank)
    share = (spec.get("kinds") or {}).get("combo", {}).get("none_share", 0.05)
    changed = 0
    for item in bank["items"]:
        if item.get("kind") != "combo" or item.get("fixed") or item.get("official"):
            continue
        if item.get("options") and not a.regenerate:
            continue
        seed = int(hashlib.sha256(f"{a.seed}:{item['id']}".encode()).hexdigest()[:12], 16)
        try:
            opts, ans = generate_options(item["truth"], random.Random(seed), share)
        except (ValueError, KeyError, TypeError) as e:
            print(f"{item.get('id')}: {e}")
            continue
        if item.get("options") != opts or item.get("answer") != ans:
            item["options"], item["answer"] = opts, ans
            changed += 1
            lab = option_label(opts[ans], langs(spec)[0])
            print(f"{item['id']}: key {'abcdefgh'[ans]}) {lab}  options {opts}")
    if a.write and changed:
        dump_like(raw, a.bank)
        print(f"wrote {changed} option sets to {a.bank}")
    else:
        print(f"{changed} option sets {'would change' if changed else 'to change'}; pass --write to save")
    return 0


# ---------------------------------------------------------------- blind packets


def letters(n):
    return [chr(ord("A") + i) for i in range(n)]


def cmd_packet(a):
    spec, bank, _ = load(a.spec, a.bank)
    lang = a.lang
    want = None
    if a.ids:
        want = [x.strip() for x in a.ids.split(",") if x.strip()]
    elif a.ids_file:
        want = [x.strip() for x in Path(a.ids_file).read_text(encoding="utf-8").split() if x.strip()]
    items = [it for it in bank["items"] if want is None or it.get("id") in want]
    if want:
        missing = set(want) - {it.get("id") for it in items}
        if missing:
            print("not in the bank: " + ", ".join(sorted(missing)), file=sys.stderr)
    rng = random.Random(a.seed)
    out = [f"# Blind review packet ({lang})", "",
           "Answer every item from the cited source, in this language only. Do not look",
           "for keys, explanations or the bank. Options are shuffled. For combination",
           "items, rule every statement true or false first, then choose the option.",
           "Record each answer in the answers file next to this packet.", ""]
    mapping, template = {}, []
    for n, it in enumerate(items, 1):
        f = lang_fields(it, lang) or {}
        k = it.get("kind")
        src = loc(it.get("source"), lang, "")
        out.append(f"## {n}. {it['id']} · section {it.get('section')} · {k}")
        out.append(f"Source: {src}")
        if it.get("case"):
            case = loc(bank["cases"].get(it["case"], {}).get(lang, {}).get("text"), lang, "")
            out.append("")
            out.append(f"> Case: {case}")
        out.append("")
        out.append(f.get("stem", "").replace("{{", "[blank ").replace("}}", "]"))
        out.append("")
        row = {"id": it["id"], "answer": None, "second": None, "quote": "", "locator": "", "code": None, "note": ""}
        m = {"kind": k}
        if k in ("single", "multi"):
            opts = f.get("options") or []
            perm = list(range(len(opts)))
            if shuffles(spec, it):
                pin = it.get("pin_last", 0)
                head = perm[:len(opts) - pin]
                rng.shuffle(head)
                perm = head + perm[len(opts) - pin:]
            for L, j in zip(letters(len(opts)), perm):
                out.append(f"{L}. {opts[j]}")
            m["perm"] = perm
            if k == "multi":
                row["answer"] = []
        elif k == "tf":
            out.append("True or false?")
        elif k == "combo":
            sts = f.get("statements") or []
            perm = list(range(len(sts)))
            if shuffles(spec, it):
                rng.shuffle(perm)
            for i, j in enumerate(perm, 1):
                out.append(f"{i}. {sts[j]}")
            out.append("")
            new_of = {j + 1: i + 1 for i, j in enumerate(perm)}
            shown = canonical([o if o in (ALL, NONE) else sorted(new_of[x] for x in o) for o in it.get("options") or []], len(sts)) if shuffles(spec, it) else it.get("options") or []
            for L, o in zip(letters(len(shown)), shown):
                out.append(f"{L}. {option_label(o, lang)}")
            m["perm"], m["shown"] = perm, shown
            row["statements"] = [None] * len(sts)
        elif k == "match":
            left, right = f.get("left") or [], f.get("right") or []
            rp = list(range(len(right)))
            rng.shuffle(rp)
            for i, x in enumerate(left, 1):
                out.append(f"{i}. {x}")
            out.append("")
            for L, j in zip(letters(len(right)), rp):
                out.append(f"{L}. {right[j]}")
            m["perm"] = rp
            row["answer"] = [None] * len(left)
        elif k == "order":
            its = f.get("items") or []
            perm = list(range(len(its)))
            rng.shuffle(perm)
            for L, j in zip(letters(len(its)), perm):
                out.append(f"{L}. {its[j]}")
            m["perm"] = perm
            row["answer"] = ""
        elif k == "cloze":
            ch = f.get("choices")
            if ch:
                for b, opts in enumerate(ch, 1):
                    out.append(f"Blank {b}: " + " / ".join(opts))
            row["answer"] = []
        elif k == "numeric":
            if loc(f.get("unit"), lang):
                out.append(f"Unit: {loc(f.get('unit'), lang)}")
        else:
            out.append("Write the answer you would give; the model answer is compared afterwards.")
            row["answer"] = ""
        out.append("")
        mapping[it["id"]] = m
        template.append(row)
    outp = Path(a.out)
    outp.write_text("\n".join(out), encoding="utf-8")
    base = outp.with_suffix("")
    Path(f"{base}.answers.json").write_text(json.dumps(template, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    Path(f"{base}.map.json").write_text(json.dumps({"lang": lang, "items": mapping}, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{len(items)} items -> {outp}; answers template {base}.answers.json; "
          f"keep {base}.map.json away from the reviewer")
    return 0


def letter_index(x):
    if isinstance(x, int) and not isinstance(x, bool):
        return x
    if isinstance(x, str) and len(x.strip()) == 1 and x.strip().isalpha():
        return ord(x.strip().upper()) - ord("A")
    raise ValueError(f"not an option letter: {x!r}")


def cmd_compare(a):
    spec, bank, _ = load(a.spec, a.bank)
    answers = load_json(a.answers)
    mp = Path(a.answers).with_name(Path(a.answers).name.replace(".answers.json", ".map.json"))
    if a.map:
        mp = Path(a.map)
    packed = load_json(mp)
    mapping, packet_lang = packed["items"], packed.get("lang")
    by_id = {it["id"]: it for it in bank["items"]}
    findings, agree, total = [], 0, 0
    for row in answers:
        iid = row.get("id")
        it, m = by_id.get(iid), mapping.get(iid)
        if not it or not m:
            findings.append((iid, "not in the bank or the packet map"))
            continue
        k = it["kind"]
        note = []
        try:
            ans = row.get("answer")
            if ans is None or ans == "" or ans == []:
                note.append("no answer")
                ok = None
            elif k == "single":
                got = m["perm"][letter_index(ans)]
                ok = got == it["answer"]
                if not ok:
                    note.append(f"answered option {got} (stored order), key is {it['answer']}")
            elif k == "multi":
                got = sorted(m["perm"][letter_index(x)] for x in (ans if isinstance(ans, list) else re.split(r"[,\s]+", ans)) if str(x).strip())
                ok = got == sorted(it["answer"])
                if not ok:
                    note.append(f"answered {got}, key is {sorted(it['answer'])}")
            elif k == "tf":
                got = ans if isinstance(ans, bool) else str(ans).strip().lower() in ("true", "t", "yes", "1", "對", "对", "是")
                ok = got == it["answer"]
                if not ok:
                    note.append(f"answered {got}, key is {it['answer']}")
            elif k == "combo":
                shown = m["shown"]
                chosen = shown[letter_index(ans)]
                n = len(it["truth"])
                back = {i + 1: j + 1 for i, j in enumerate(m["perm"])}
                chosen_set = option_set(chosen, n)
                chosen_stored = frozenset(back[x] for x in chosen_set)
                key = frozenset(i + 1 for i, t in enumerate(it["truth"]) if t)
                ok = chosen_stored == key
                if not ok:
                    note.append(f"chose statements {sorted(chosen_stored)} (stored numbers), true are {sorted(key)}")
                rs = row.get("statements") or []
                for shown_i, verdict in enumerate(rs):
                    if verdict is None:
                        continue
                    stored = m["perm"][shown_i]
                    if bool(verdict) != it["truth"][stored]:
                        note.append(f"ruled stored statement {stored + 1} {bool(verdict)}, keyed {it['truth'][stored]}")
            elif k == "match":
                right = [m["perm"][letter_index(x)] for x in ans]
                key = it.get("answer") or list(range(len(right)))
                ok = right == key
                if not ok:
                    note.append(f"matched {right}, key is {key}")
            elif k == "order":
                seq = [m["perm"][letter_index(c)] for c in re.findall(r"[A-Za-z]", ans)]
                ok = seq == list(range(len(seq))) and len(seq) == len(m["perm"])
                if not ok:
                    note.append(f"ordered {seq} (stored order)")
            elif k == "cloze":
                f = lang_fields(it, packet_lang) or {}
                acc = f.get("answers") or []
                ok = len(ans) == len(acc) and all(norm(x) in {norm(y) for y in A} for x, A in zip(ans, acc))
                if not ok:
                    note.append(f"answered {ans}, accepted {acc}")
            elif k == "numeric":
                tol = it.get("tolerance")
                if tol is None and it.get("tolerance_pct") is not None:
                    tol = abs(it["answer"]) * it["tolerance_pct"] / 100
                ok = abs(float(ans) - it["answer"]) <= (tol or 0)
                if not ok:
                    note.append(f"answered {ans}, key is {it['answer']}")
            else:
                ok = None
                note.append("written answer: compare with the model answer and rubric by hand")
        except (ValueError, IndexError, KeyError, TypeError) as e:
            ok = None
            note.append(f"could not read the answer: {e}")
        total += 1
        agree += ok is True
        if row.get("second"):
            note.append(f"second defensible answer: {row['second']}")
        if row.get("code"):
            note.append(f"code: {row['code']}")
        if row.get("note"):
            note.append(f"note: {row['note']}")
        if ok is not True or note:
            findings.append((iid, "; ".join(note) or "disagrees with the key"))
    if a.json:
        print(json.dumps({"agree": agree, "total": total, "findings": findings}, ensure_ascii=False, indent=1))
    else:
        for iid, msg in findings:
            print(f"{iid}: {msg}")
        print(f"{agree} of {total} answers agree with the key; {len(findings)} items to settle against the source")
    return 0


# ---------------------------------------------------------------- printed papers


def draw_paper(spec, bank, rng, everything=False):
    """Items for one paper under the spec's draw (case sets kept together), or the
    whole bank in section order."""
    retired = set(spec.get("retired_ids") or [])
    out = []
    for s in spec.get("sections", []):
        sid = str(s.get("id"))
        pool = [it for it in bank["items"] if str(it.get("section")) == sid and it.get("id") not in retired]
        if everything:
            out += pool
            continue
        units, cases = [], defaultdict(list)
        for it in pool:
            if it.get("case"):
                cases[it["case"]].append(it)
            else:
                units.append([it])
        units += list(cases.values())
        rng.shuffle(units)
        need = s.get("draw", 0) or 0
        for u in units:
            if need <= 0:
                break
            if len(u) <= need:
                out += u
                need -= len(u)
    return out


PAPER_WORDS = {
    "en": {"time": "Time allowed: {0} minutes. {1} questions.", "tf": "True / False", "source": "Source",
           "answer": "Answer", "marks": "{0} marks", "key": "answer key", "true": "True", "false": "False"},
    "zh-Hant": {"time": "考試時間：{0}分鐘，共{1}題。", "tf": "正確／錯誤", "source": "出處",
                "answer": "答案", "marks": "{0}分", "key": "答案及解釋", "true": "正確", "false": "錯誤"},
    "zh-Hans": {"time": "考试时间：{0}分钟，共{1}题。", "tf": "正确／错误", "source": "出处",
                "answer": "答案", "marks": "{0}分", "key": "答案及解释", "true": "正确", "false": "错误"},
}


def paper_words(spec, lang):
    over = (spec.get("ui") or {}).get(lang) or {}
    if lang in PAPER_WORDS:
        base = PAPER_WORDS[lang]
    elif lang.lower().startswith(("zh-cn", "zh-sg", "zh-hans")):
        base = PAPER_WORDS["zh-Hans"]
    elif lang.lower().startswith("zh"):
        base = PAPER_WORDS["zh-Hant"]
    else:
        base = PAPER_WORDS["en"]
    return {**base, **{k: v for k, v in over.items() if k in base}}


def cmd_paper(a):
    spec, bank, _ = load(a.spec, a.bank)
    lang = a.lang or langs(spec)[0]
    w = paper_words(spec, lang)
    rng = random.Random(a.seed)
    items = draw_paper(spec, bank, rng, a.all)
    title = loc(spec.get("title"), lang) or "Paper"
    minutes = (spec.get("paper") or {}).get("minutes")
    paper = [f"# {title}", ""]
    if minutes:
        paper += [w["time"].format(minutes, len(items)), ""]
    key = [f"# {title} — {w['key']}", ""]
    shown_case = set()
    for n, it in enumerate(items, 1):
        f = lang_fields(it, lang) or {}
        k = it["kind"]
        if it.get("case") and it["case"] not in shown_case:
            c = (bank["cases"].get(it["case"]) or {}).get(lang) or {}
            paper += [f"> **{c.get('title', '')}** {c.get('text', '')}", ""]
            shown_case.add(it["case"])
        stem = f.get("stem", "")
        if k == "cloze":
            stem = re.sub(r"\{\{(\d+)\}\}", lambda m: f"({m.group(1)}) ________", stem)
        paper += [f"**{n}.** {stem}", ""]
        ans, notes = "", []
        if k in ("single", "multi"):
            opts = f.get("options") or []
            perm = list(range(len(opts)))
            if shuffles(spec, it):
                pin = it.get("pin_last", 0)
                head = perm[:len(opts) - pin]
                rng.shuffle(head)
                perm = head + perm[len(opts) - pin:]
            for L, j in zip(letters(len(opts)), perm):
                paper.append(f"- {L}. {opts[j]}")
            keys = [it["answer"]] if k == "single" else list(it["answer"])
            ans = "; ".join(f"{letters(len(opts))[perm.index(x)]} — {opts[x]}" for x in sorted(keys, key=perm.index))
            on = f.get("option_notes") or []
            notes = [f"{letters(len(opts))[i]}. {on[j]}" for i, j in enumerate(perm) if j < len(on)]
        elif k == "tf":
            paper.append(w["tf"])
            ans = w["true"] if it["answer"] else w["false"]
        elif k == "combo":
            sts = f.get("statements") or []
            perm = list(range(len(sts)))
            if shuffles(spec, it):
                rng.shuffle(perm)
            new_of = {j + 1: i + 1 for i, j in enumerate(perm)}
            for i, j in enumerate(perm, 1):
                paper.append(f"{i}. {sts[j]}")
            paper.append("")
            shown = [(o if o in (ALL, NONE) else sorted(new_of[x] for x in o), idx) for idx, o in enumerate(it["options"])]
            if shuffles(spec, it):
                sets = sorted((s for s in shown if s[0] not in (ALL, NONE)), key=lambda s: (len(s[0]), s[0]))
                shown = sets + [s for s in shown if s[0] in (ALL, NONE)]
            for L, (o, _) in zip(letters(len(shown)), shown):
                paper.append(f"- {L}. {option_label(o, lang)}")
            pos = [idx for _, idx in shown].index(it["answer"])
            ans = f"{letters(len(shown))[pos]} — {option_label(shown[pos][0], lang)}"
            sn = f.get("statement_notes") or []
            notes = [f"{i}. {sn[j]}" for i, j in enumerate(perm, 1) if j < len(sn)]
        elif k == "match":
            left, right = f.get("left") or [], f.get("right") or []
            rp = list(range(len(right)))
            rng.shuffle(rp)
            for i, x in enumerate(left, 1):
                paper.append(f"{i}. {x}")
            paper.append("")
            for L, j in zip(letters(len(right)), rp):
                paper.append(f"- {L}. {right[j]}")
            kk = it.get("answer") or list(range(len(left)))
            ans = ", ".join(f"{i}{letters(len(right))[rp.index(x)]}" for i, x in enumerate(kk, 1))
        elif k == "order":
            its = f.get("items") or []
            perm = list(range(len(its)))
            rng.shuffle(perm)
            for L, j in zip(letters(len(its)), perm):
                paper.append(f"- {L}. {its[j]}")
            ans = "".join(letters(len(its))[perm.index(x)] for x in range(len(its)))
        elif k == "cloze":
            ans = "; ".join(f"({b}) " + " / ".join(acc) for b, acc in enumerate(f.get("answers") or [], 1))
        elif k == "numeric":
            unit = loc(f.get("unit"), lang) or ""
            paper.append(f"Answer: ________ {unit}")
            tol = it.get("tolerance")
            ans = f"{it['answer']} {unit}".strip() + (f" (± {tol})" if tol else "")
        else:
            paper.append("[" + w["marks"].format(it.get("points", 1)) + "]")
            ans = f.get("model_answer", "")
            for r in f.get("rubric") or []:
                notes.append(f"{r['text']} ({r['marks']})")
            for r in f.get("levels") or []:
                notes.append(f"{r['marks']}: {r['text']}")
        paper.append("")
        key += [f"**{n}.** {ans}  ", f"{w['source']}: {loc(it.get('source'), lang, '')} · `{it.get('id')}`"]
        key += [f"- {x}" for x in notes]
        if f.get("explain"):
            key.append(f"- {f['explain']}")
        key.append("")
    Path(a.out).write_text("\n".join(paper), encoding="utf-8")
    Path(a.key).write_text("\n".join(key), encoding="utf-8")
    print(f"{len(items)} questions -> {a.out}; key -> {a.key}")
    return 0


# ---------------------------------------------------------------- stats


def cmd_stats(a):
    spec, bank, _ = load(a.spec, a.bank)
    items = bank["items"]
    secs = [str(s.get("id")) for s in spec.get("sections", [])]
    kinds = sorted({it.get("kind") for it in items})
    print("| Section | Draw | " + " | ".join(kinds) + " | Total |")
    print("|---|---|" + "---|" * len(kinds) + "---|")
    draw = {str(s.get("id")): s.get("draw", 0) for s in spec.get("sections", [])}
    for s in secs:
        c = Counter(it.get("kind") for it in items if str(it.get("section")) == s)
        print(f"| {s} | {draw[s]} | " + " | ".join(str(c[k]) for k in kinds) + f" | {sum(c.values())} |")
    quoted = sum(1 for it in items if it.get("quotes"))
    print(f"\n{len(items)} items; {quoted} carry deciding quotes; languages {', '.join(langs(spec))}.")
    pools = Counter(str(it.get("section")) for it in items)
    papers = min((pools[s] // draw[s]) for s in secs if draw[s]) if any(draw.values()) else 0
    print(f"Disjoint papers the smallest section allows: {papers}.")
    return 0


# ---------------------------------------------------------------- main


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="hard errors and warnings")
    c.add_argument("spec")
    c.add_argument("bank")
    c.add_argument("--sources", help="folder of extracted texts (NN.txt or LANG/NN.txt) to find quotes in")
    c.add_argument("--notes", help="notes page whose ids notes_anchor must name; also warns where it echoes a false statement")
    c.add_argument("--json", action="store_true")
    c.add_argument("--max-warnings", type=int, default=60)
    c.set_defaults(fn=cmd_check)
    t = sub.add_parser("tells", help="surface cues, strategies, a learnt guesser and simulated papers")
    t.add_argument("spec")
    t.add_argument("bank")
    t.add_argument("--papers", type=int, default=2000)
    t.add_argument("--seed", type=int, default=1)
    t.set_defaults(fn=cmd_tells)
    o = sub.add_parser("options", help="generate combination option sets from truth")
    o.add_argument("spec")
    o.add_argument("bank")
    o.add_argument("--write", action="store_true")
    o.add_argument("--regenerate", action="store_true", help="replace existing option sets too (not fixed or official items)")
    o.add_argument("--seed", type=int, default=0)
    o.set_defaults(fn=cmd_options)
    k = sub.add_parser("packet", help="a keyless, shuffled blind-review packet for one language")
    k.add_argument("spec")
    k.add_argument("bank")
    k.add_argument("--lang", required=True)
    k.add_argument("--out", required=True)
    k.add_argument("--ids")
    k.add_argument("--ids-file")
    k.add_argument("--seed", type=int, default=7)
    k.set_defaults(fn=cmd_packet)
    m = sub.add_parser("compare", help="a reviewer's answers against the key")
    m.add_argument("spec")
    m.add_argument("bank")
    m.add_argument("answers")
    m.add_argument("--map")
    m.add_argument("--json", action="store_true")
    m.set_defaults(fn=cmd_compare)
    pp = sub.add_parser("paper", help="a printable question paper and a separate answer key, in Markdown")
    pp.add_argument("spec")
    pp.add_argument("bank")
    pp.add_argument("--out", required=True)
    pp.add_argument("--key", required=True)
    pp.add_argument("--lang")
    pp.add_argument("--all", action="store_true", help="every item in section order instead of one drawn paper")
    pp.add_argument("--seed", type=int, default=11)
    pp.set_defaults(fn=cmd_paper)
    s = sub.add_parser("stats", help="items per section and kind")
    s.add_argument("spec")
    s.add_argument("bank")
    s.set_defaults(fn=cmd_stats)
    a = p.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
