"""Build/check the local, network-independent bilingual study sample.

Run: python revision/part6-sample/build.py [--check]
No official originals, question wording or historic evidence are modified.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from html.parser import HTMLParser

from content import SECTIONS

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CATALOG = json.loads((ROOT / "docs/catalog.json").read_text(encoding="utf-8"))
DOCS = {d["id"]: d for d in CATALOG["documents"]}
BANK = json.loads((ROOT / "web/questions.json").read_text(encoding="utf-8"))
QUESTIONS = {q["id"]: q for q in BANK if q["module"] == 6}
e = html.escape


def pair(p):
    return f'<span class="tc" lang="zh-Hant">{e(p["tc"])}</span><span class="en" lang="en">{e(p["en"])}</span>'


def label(tc, en):
    return pair({"tc": tc, "en": en})


def loc_tc(loc):
    loc = loc.replace("Sch.2", "附表2").replace("beneficial owner", "實益擁有人釋義")
    loc = loc.replace("AML/CFT", "打擊洗錢／恐怖分子資金籌集")
    loc = re.sub(r"Q(\d+)", r"第\1題", loc)
    loc = re.sub(r"¶([\d.]+(?:\([a-z0-9]+\))*(?:[–\-][\d.]+(?:\([a-z0-9]+\))*)?)", r"第\1段", loc)
    loc = re.sub(r"s\.(\d+(?:\([^)]*\))*(?:[–\-]\([^)]*\))*)", r"第\1條", loc)
    loc = re.sub(r"fn(\d+(?:[–\-]\d+)?)", r"註\1", loc)
    return (loc.replace("Appendix A", "附錄A").replace("Appendix", "附錄")
            .replace("Key control standards", "主要管控措施標準第")
            .replace("Key control standard", "主要管控措施標準第")
            .replace("Red flags", "可疑交易訊號").replace("printed pp.", "印刷頁碼第")
            .replace("Areas", "範疇第").replace("Area", "範疇第")
            .replace("standard", "標準第").replace("note", "註").replace("pp.", "頁"))


def edition(doc, lang):
    # 24 has no official Chinese edition: both source links use the actual EN original.
    return DOCS[doc]["editions"]["EN" if doc == "24" else lang.upper()]


def page_number(doc, lang, loc):
    """Only attach a PDF page when an unambiguous marker exists in extracted text."""
    ed = edition(doc, lang)
    if ed.get("format") != "pdf":
        return None
    text = (ROOT / "docs" / ed["text_file"]).read_text(encoding="utf-8")
    marker = None
    match = re.search(r"¶([\d.]+)", loc)
    if doc == "03" and "Appendix A" not in loc and match:
        marker = re.search(r"(?m)^\s*" + re.escape(match[1]) + r"\s*$", text)
    elif doc == "24" and (match := re.search(r"printed pp\.(\d+)", loc)):
        # The printed number occurs in a page header; form feeds preserve PDF order.
        marker = re.search(r"(?m)^.*(?:\| " + match[1] + r"\s*$|^" + match[1] + r" \|)", text)
    return text[:marker.start()].count("\f") + 1 if marker else None


def source_link(doc, lang, loc=""):
    ed = edition(doc, lang)
    url = "../../docs/" + quote(ed["path"], safe="/")
    page = page_number(doc, lang, loc) if loc else None
    if page:
        url += f"#page={page}"
    return url


def refs_html(refs):
    out = []
    for ref in refs:
        doc, loc = ref["doc"], ref["loc"]
        tags = []
        for lang in ("tc", "en"):
            ed = edition(doc, lang)
            translated = " · 學習譯文，英文原件" if lang == "tc" and doc == "24" else ""
            location = loc_tc(loc) if lang == "tc" else loc
            tags.append(f'<span class="{lang}" lang="{"zh-Hant" if lang == "tc" else "en"}">'
                        f'<a href="{e(source_link(doc, lang, loc))}" target="_blank" rel="noopener">'
                        f'{e(doc + "｜" + ed["path"].split("/")[-1])}</a>'
                        f'<span class="locator">{e(location + translated)}</span></span>')
        out.append('<div class="source-citation">' + ''.join(tags) + '</div>')
    return '<div class="citations">' + ''.join(out) + '</div>'


def render_flow(block, sid):
    steps = block["steps"]
    title = '<h3>' + pair(block["title"]) + '</h3>'
    if sid == "monitoring":
        diagram = ('<div class="flow-node">' + pair(steps[0]) + '</div><div class="arrow" aria-hidden="true">↓</div>'
                   '<div class="branches"><div class="flow-node outcome">' + pair(steps[1]) + '</div>'
                   '<div class="flow-node action">' + pair(steps[2]) + '</div></div><nav class="part-nav" aria-label="Parts">' + ''.join(f'<a href="../study-notes/part-{n}.html"' + (' aria-current="page"' if n == 6 else '') + f'>Part {n}</a>' for n in range(1,8)) + '</nav>'
                   '<div class="arrow" aria-hidden="true">↓</div><div class="flow-node">' + pair(steps[3]) + '</div>')
    elif sid == "third-party":
        diagram = ('<div class="branches"><div class="flow-node stop">' + pair(steps[0]) + '</div>'
                   '<div class="flow-node"><div class="step">01</div>' + pair(steps[1]) + '</div></div>'
                   '<div class="arrow" aria-hidden="true">↓</div><div class="flow-node action"><div class="step">02</div>'
                   + pair(steps[2]) + '</div><div class="arrow" aria-hidden="true">↓</div>'
                   '<div class="flow-node outcome"><div class="step">03</div>' + pair(steps[3]) + '</div>')
        # The down arrows belong to the adequate-control branch only.
        diagram = '<div class="third-flow">' + diagram + '</div>'
    elif sid == "start":
        diagram = '<div class="flow-stack">' + ''.join(
            f'<div class="flow-node"><div class="step">{i+1:02}</div>{pair(p)}</div>' for i, p in enumerate(steps)) + '</div>'
    else:
        diagram = '<div class="flow-stack">' + '<div class="arrow" aria-hidden="true">↓</div>'.join(
            f'<div class="flow-node"><div class="step">{i+1:02}</div>{pair(p)}</div>' for i, p in enumerate(steps)) + '</div>'
    key = ""
    if sid in {"monitoring", "third-party"}:
        key = '<p class="legend">' + label("綠色：有解釋／接納後的路線；金色：需要跟進。以框內條件為準。",
            "Green: explained/accepted route. Amber: follow-up action. Read the conditions within each box.") + '</p>'
        if sid == "third-party":
            key = '<p class="legend">' + label("綠色：有解釋／接納後的路線；金色：需要跟進；深色：停止。以框內條件為準。",
                "Green: explained/accepted route. Amber: follow-up action. Dark: stop. Read the conditions within each box.") + '</p>'
    return '<figure class="flow">' + title + diagram + key + refs_html(block["refs"]) + '</figure>'


def render_block(block, sid):
    if block["kind"] == "table":
        headers = block["head"]
        rows = []
        for r in block["rows"]:
            cells = []
            for i, cell in enumerate(r["cells"]):
                tag = "th" if i == 0 else "td"
                scope = ' scope="row"' if i == 0 else ""
                cells.append(f'<{tag}{scope}>' + pair(cell) + f'</{tag}>')
            # Each rule row is followed by its own complete file-name references.
            rows.append('<tbody><tr>' + ''.join(cells) + '</tr><tr class="citation-row"><td colspan="3">'
                        + refs_html(r["refs"]) + '</td></tr></tbody>')
        return ('<div class="table-wrap"><table><thead><tr>'
                + ''.join('<th scope="col">' + pair(h) + '</th>' for h in headers)
                + '</tr></thead>' + ''.join(rows) + '</table></div>')
    if block["kind"] == "flow":
        return render_flow(block, sid)
    heading = label("說明例（非官方案例）", "Illustration (not an official case)") if block["kind"] == "example" else label("記住這個分別", "Keep this distinction")
    return f'<aside class="{block["kind"]}"><h3>{heading}</h3><p>{pair(block["text"])}</p>{refs_html(block["refs"])}</aside>'


CSS = (HERE.parent / "study-notes/style.css").read_text(encoding="utf-8")
FONT = base64.b64encode((ROOT / "web/fonts/dmsans.woff2").read_bytes()).decode("ascii")
FONT_FACE = '@font-face{font-family:"Study Sans";src:url(data:font/woff2;base64,' + FONT + ') format("woff2");font-weight:100 900;font-style:normal;font-display:swap;}'

SCRIPT = r"""
document.querySelectorAll('[data-language]').forEach(button=>button.addEventListener('click',()=>{
  const language=button.dataset.language;document.body.dataset.lang=language;
  document.documentElement.lang=language==='en'?'en':'zh-Hant';
  document.querySelectorAll('[data-language]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
  requestAnimationFrame(updateLocation);
}));
const chapters = [...document.querySelectorAll('.chapter')];
const links = [...document.querySelectorAll('.sidebar a')];
function updateLocation() {
  const current = [...chapters].reverse().find(section => section.getBoundingClientRect().top <= 160) || chapters[0];
  links.forEach(link => {
    if (link.dataset.section === current.id) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
}
let scrollPending = false;
addEventListener('scroll', () => {
  if (scrollPending) return;
  scrollPending = true;
  requestAnimationFrame(() => { updateLocation(); scrollPending = false; });
}, {passive: true});
addEventListener('resize', updateLocation);
updateLocation();
document.fonts.ready.then(updateLocation);
"""


def build_html():
    nav = ''.join(f'<a data-section="{s["id"]}" href="#{s["id"]}"><span class="nav-number" aria-hidden="true">{i+1:02}</span><span>{pair(s["title"])}</span></a>'
                  for i, s in enumerate(SECTIONS))
    body = []
    for i, s in enumerate(SECTIONS):
        body.append(f'<section class="chapter" id="{s["id"]}" aria-labelledby="title-{s["id"]}">'
                    f'<div class="section-heading"><span class="section-number">{i+1:02}</span>'
                    f'<h2 id="title-{s["id"]}">{pair(s["title"])}</h2></div>'
                    f'<p class="intro">{pair(s["intro"])}</p>')
        body.extend(render_block(b, s["id"]) for b in s["blocks"])
        if s["questions"]:
            body.append('<div class="question-map">' + label("現有題庫對照：", "Existing bank cross-reference: ")
                        + ''.join(f'<span class="qid">{e(q)}</span>' for q in s["questions"]) + '</div>')
        body.append('</section>')
    return ('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>MSO · Part 6 · 管控範疇 / Control areas</title><style>' + FONT_FACE + CSS + '</style></head>'
            '<body data-lang="tc"><a class="skip-link" href="#content">' + label("跳至正文", "Skip to content") + '</a><div class="toolbar"><div class="toolbar-inner"><div class="brand">MSO Competence Assessment Study Note</div>'
            '<div class="languages" role="group" aria-label="閱讀語言 / Reading language">'
            '<button data-language="tc" aria-pressed="true">繁體中文</button>'
            '<button data-language="en" aria-pressed="false">English</button>'
            '<button data-language="both" aria-pressed="false">雙語 / Both</button></div>'
            '</div></div>'
            '<div class="layout"><aside class="sidebar"><h2>' + label("本章導航", "In this chapter")
            + '</h2><nav aria-label="章節 / Chapters">' + nav
            + '</nav></aside><main id="content" tabindex="-1"><header class="hero"><h1>'
            + label("第6部分 · 金錢服務經營者的系統及管控措施（二）：打擊洗錢及恐怖分子資金籌集的管控範疇",
                    "Part 6 · MSO systems and controls (ii): AML/CFT control areas") + '</h1></header>'
            + ''.join(body) + '<footer><p>'
            + label("本樣章按 repo 指定版本整理。第03號為核心指引，第04號為條例；相關來源差異按既有裁決整理，版次及來源紀錄見對照檔案。",
            "Prepared from the repo's selected editions. Document 03 is the core Guideline; 04 is the Ordinance. Relevant source differences follow existing project decisions; edition and source records are in the mapping file.")
            + '</p><p><a href="../../dist/mso-ca.html">' + label("開啟練習 App（選擇 Part 6）", "Open practice app (select Part 6)")
            + '</a> · <a href="coverage.json">' + label("查看題目與來源對照", "Question and source mapping")
            + '</a></p></footer></main></div><script>' + SCRIPT + '</script></body></html>\n')


def make_coverage():
    hashes = {}
    for doc in sorted({r["doc"] for s in SECTIONS for b in s["blocks"]
                       for obj in (b.get("rows") or [b]) for r in obj.get("refs", [])} | {"01"}):
        hashes[doc] = {}
        for lang in ("tc", "en"):
            ed = edition(doc, lang)
            original = ROOT / "docs" / ed["path"]
            hashes[doc][lang] = {"path": "docs/" + ed["path"],
                                 "sha256": hashlib.sha256(original.read_bytes()).hexdigest(),
                                 "text_path": "docs/" + ed["text_file"],
                                 "text_sha256": hashlib.sha256((ROOT / "docs" / ed["text_file"]).read_bytes()).hexdigest(),
                                 "study_translation": doc == "24" and lang == "tc"}
    return {"scope": "Part 6 sample; selected repo editions of documents 01–26",
            "mapping_meaning": "Topic association, not full statement-level coverage or a new review of existing questions.",
            "review": "Author source-context and bilingual self-review plus structural/browser checks; no independent semantic review claimed.",
            "author_model": "GPT-6.1 Sol (user-reported selection)",
            "content_sha256": hashlib.sha256((HERE / "content.py").read_bytes()).hexdigest(),
            "question_bank_sha256": hashlib.sha256((ROOT / "web/questions.json").read_bytes()).hexdigest(),
            "source_conflict_decisions": ["B4", "B14", "B16", "B17", "B19", "B20", "B29", "B30", "B31", "B32", "E17", "E21", "E41"],
            "source_files": hashes,
            "sections": [{"id": s["id"], "title": s["title"], "questions": [
                {"id": qid, "stem": {lang: QUESTIONS[qid][lang]["q"] for lang in ("tc", "en")},
                 "source": QUESTIONS[qid]["source"]} for qid in s["questions"]]} for s in SECTIONS]}


class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.scripts = [], [], []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a":
            self.links.append(a.get("href", ""))
        if tag in ("script", "img", "link") and (a.get("src") or a.get("href")):
            self.scripts.append(a.get("src") or a.get("href"))


def validate(text):
    assigned = [q for s in SECTIONS for q in s["questions"]]
    assert set(assigned) == set(QUESTIONS), "Missing or unknown question mappings"
    assert len(assigned) == len(set(assigned)), "Duplicate question mapping"
    assert len(QUESTIONS) == 100
    used_refs = 0
    for s in SECTIONS:
        for b in s["blocks"]:
            objects = b.get("rows") or [b]
            for obj in objects:
                assert obj.get("refs"), f"Uncited block: {s['id']}"
                for r in obj["refs"]:
                    assert "01" <= r["doc"] <= "26"
                    assert r["loc"].strip()
                    for lang in ("tc", "en"):
                        ed = edition(r["doc"], lang)
                        assert (ROOT / "docs" / ed["path"]).is_file()
                        source_text = (ROOT / "docs" / ed["text_file"]).read_text(encoding="utf-8")
                        # Verify every paragraph locator occurs (semantic support is reviewed separately).
                        if r["doc"] == "03" and "Appendix" not in r["loc"]:
                            for marker in re.findall(r"¶([\d.]+)", r["loc"]):
                                assert re.search(r"(?m)^\s*" + re.escape(marker) + r"\s*$", source_text), (r, lang)
                    used_refs += 1
    def pairs(value):
        if isinstance(value, dict):
            if set(value) == {"tc", "en"}:
                assert all(isinstance(v, str) and v.strip() for v in value.values())
            for v in value.values():
                pairs(v)
        elif isinstance(value, list):
            for v in value:
                pairs(v)
    pairs(SECTIONS)
    parser = Inspector()
    parser.feed(text)
    assert len(parser.ids) == len(set(parser.ids)), "Duplicate HTML ID"
    assert not parser.scripts, "External rendering dependencies"
    for href in parser.links:
        if href.startswith("#"):
            assert href[1:] in parser.ids, href
        else:
            target = HERE / unquote(urlsplit(href).path)
            # App is built by the repository's existing build step.
            if target.name not in {"mso-ca.html", "coverage.json"}:
                assert target.is_file(), href
    assert not any(s in text.lower() for s in ('type="password"', 'class="recall"', 'backdrop-filter:blur(4px)'))
    return {"sections": len(SECTIONS), "comparison_rows": sum(len(b.get("rows", [])) for s in SECTIONS for b in s["blocks"]),
            "flows": sum(b["kind"] == "flow" for s in SECTIONS for b in s["blocks"]),
            "question_mappings": len(assigned), "source_references": used_refs,
            "local_link_occurrences": len(parser.links), "unique_ids": len(parser.ids)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = build_html()
    result = validate(text)
    coverage = json.dumps(make_coverage(), ensure_ascii=False, indent=2) + "\n"
    outputs = {"index.html": text, "coverage.json": coverage}
    for name, value in outputs.items():
        path = HERE / name
        if args.check:
            assert path.read_text(encoding="utf-8") == value, f"Stale output: {name}"
        else:
            path.write_text(value, encoding="utf-8", newline="\n")
    print(json.dumps({"status": "checked" if args.check else "built", **result}, ensure_ascii=False))


if __name__ == "__main__":
    main()
