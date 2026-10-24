"""Build and validate selected reading folders and the reference archive."""
import hashlib
import json
import pathlib
import posixpath
import sys
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
PRIORITIES = {'high': ('高', 'High'), 'medium': ('中', 'Medium'), 'low': ('低', 'Low')}

def primary_path(doc, lang):
    e = doc['editions'][lang]
    return e.get('path', f'{lang}/{e["file"]}')

def active(item):
    return item.get('reading_status', 'active') == 'active'

def title(doc, lang):
    value = doc['title'][lang]
    return value + (' · ' + doc['circular'] if doc.get('circular') else '')

def link(path, label, archive=False):
    return f'[{label}](<{posixpath.relpath(path, "archive") if archive else path}>)'

def count(catalog, wanted):
    return sum(active(d)==wanted for d in catalog['documents'])


def render(catalog, lang):
    tc=lang=='TC';docs=catalog['documents']
    def text(zh,en):return zh if tc else en
    lines=[text('# MSO 精簡閱讀目錄','# MSO focused reading directory'),'',
           text('[English →](README.md)','[繁體中文 →](README.zh-Hant.md)'),'',
           text('日常閱讀共 **26項材料，連續編號01–26**，配套文件也各佔一個編號。全部原件直接放在[中文資料夾](TC/)及[英文資料夾](EN/)，每個資料夾26份。兩部雙語法例在兩個資料夾各放一份。','**26 daily publications, continuously numbered 01–26.** Companions each have their own number. Originals are directly in [TC](TC/) and [EN](EN/), 26 files per folder. Both bilingual laws are copied into both folders.'),'',
           text('按檔名排序，就是「01–09高優先級 → 10–19中重點 → 20–26中選讀」。不留空號，也沒有另一套來源ID。第16項通函後接第17項完整第34章；第22項通函後接第23項完整第629章。歷史參考材料接續編為27–47，放在archive內。','Filename order is 01–09 High → 10–19 Medium Essential → 20–26 Medium Selected, without gaps or separate source IDs. Circular 16 is followed by the full Cap. 34 as 17; circular 22 is followed by the full Cap. 629 as 23. Reference publications continue as 27–47 under archive.'),'',
           text('**最先掌握03、04、05**：反洗錢指引、第615章及牌照指引。01、02先快速了解考試及試題；06至09用來補足實際應用和明確監管要求。完成高優先級後，先讀「中重點」，再按薄弱範圍讀「中選讀」。','**Master 03, 04 and 05 first:** the AML/CFT Guideline, Cap. 615 and Licensing Guide. Skim 01-02 for exam setup and examples; use 06-09 for application and specific expectations. After High, finish Medium Essential before selecting weaker topics from Medium Selected.'),'',
           text('依據：[官方《能力評核須知》第5.2至6.1段](https://eservices.customs.gov.hk/MSOS/download/licensing/Guidance_Notes_on_the_Competence_Assessment_for_Money_Service_Operators_zh_TW.pdf)。七個單元涵蓋法例、核心指引、其他指引及通函；以下是復習建議，並非官方出題權重。','Basis: [official Guidance Notes, paragraphs 5.2-6.1](https://eservices.customs.gov.hk/MSOS/download/licensing/Guidance_Notes_on_the_Competence_Assessment_for_Money_Service_Operators_en.pdf). The seven-module syllabus includes law, core and other guidelines, and circulars. These are study recommendations, not official exam weights.'),'',
           text('從47項收錄材料中移出21項：完整法例已覆蓋的摘錄、舊期通知、重複培訓、歷史決議及較遠離核心範圍的材料，見[移出清單及原因](archive/README.zh-Hant.md)。原件及題庫證據仍保留；移出不代表失效或不會考，現行題庫只用01–26，這些材料只供歷史參考。','21 of the 47 publications have been removed from daily reading: covered extracts, old notices, repeat training, historical resolutions and lower-priority extensions. See [the decisions and reasons](archive/README.md). Originals and question evidence remain. Archiving does not establish withdrawal or exam exclusion; the current question bank uses only 01–26; archived material is historical reference.'),'']
    lines += [text('v1.13.2的[七部分溫習筆記](../revision/study-notes/index.html)保留高優先級原文的清單、條件及例外；[覆核範圍與限制](../revision/study-notes/README.md)另列。離線閱讀請從[版本頁](https://github.com/leohwlee/mso-ca/releases/tag/v1.13.2)下載完整學習包。這次沒有更新來源版次或擴大01–26範圍。','The v1.13.2 [seven-part notes](../revision/study-notes/index.html) retain lists, conditions and exceptions from the High-priority originals; see [review scope and limits](../revision/study-notes/README.md). Download the complete study bundle from the [release page](https://github.com/leohwlee/mso-ca/releases/tag/v1.13.2) for offline reading. This release does not update source editions or extend the 01–26 selection.'),'']
    for focus,zh,en in [('core','01–09 · 高優先級','01–09 · High priority'),('focus','10–19 · 中重點','10–19 · Medium essential'),('select','20–26 · 中選讀','20–26 · Medium selected')]:
        lines += ['## '+text(zh,en),'',text('| 編號 | 文件及本地原件 | 它是甚麼 | 閱讀重點 |','| Number | Publication and original | What it is | Reading focus |'),'|---|---|---|---|']
        for d in docs:
            if not active(d) or d['study_focus']!=focus:continue
            note=' **英文原文，非中文譯本**' if tc and d['editions'][lang].get('language')=='EN' else ''
            if d.get('parent_document'):note+=' · '+text('第'+d['parent_document']+'項的配套','Companion to '+d['parent_document'])
            anchors=f'<a id="doc-{d["id"]}"></a><a id="related-{d["id"]}"></a>'
            lines.append(f'| {anchors}{d["id"]} | {link(primary_path(d,lang),title(d,lang))}{note} | {d["summary"][lang]} | {d["reading"][lang]} |')
        lines += ['']
    lines += [text('## App 範圍以外的延伸閱讀','## External reading beyond the app scope'),'',text('第19項所指的兩份2026年6月19日FATF聲明及6月全體會議成果仍沒有完整本地副本，不納入 App 出題範圍。若另作延伸閱讀，名單可能更新，應核對最新版本。','The two FATF statements dated 19 June 2026 and June plenary outcomes linked by item 19 have no complete local copies and are outside the app question scope. For separate further reading, check for newer versions.'),'']
    for d in docs:
        if active(d):
            for r in d.get('online_references',[]):lines.append(f'- {d["id"]} · [{r["title"][lang]}]({r["url"]})')
    lines += ['',text('## 使用及維護','## Use and maintenance'),'',text('[使用指南](USAGE.zh-Hant.md) · [文件總目錄](INDEX.md)','[User guide](USAGE.md) · [Documentation index](INDEX.md)'),'',
              text('第24項在中文資料夾直接放英文原件，明確標示非中文譯本。第30項附表摘錄只作歷史參考，完整第34章在第17項。','Item 24 gives the English original in TC, explicitly marked as such. Item 30 is a reference extract; use the full Cap. 34 in item 17.'),'',
              text('使用者已指定01–26為唯一出題範圍。原有23份來源標記只作歷史證據；題庫已清理歸檔來源，新增題目另有覆核記錄。第24項中文題目為學習譯文，引文保留英文原文。','The owner has approved only 01–26 for active questions. The original 23-source flag records history; archived-source questions are retired and additions have separate review evidence. Chinese questions using item 24 are labelled study translations and retain English deciding quotes.'),'',
              text('[來源維護說明](SOURCE-MAINTENANCE.zh-Hant.md) · [題庫來源對照](QUESTION-SOURCES.zh-Hant.md) · [完整資料登記](catalog.json)','[Source maintenance](SOURCE-MAINTENANCE.md) · [Question source mapping](QUESTION-SOURCES.md) · [Complete register](catalog.json)'),'',
              text('官方原件的權利仍屬發布機構；本庫MIT授權不授予這些原文的使用權。見[內容授權](../LICENSE-CONTENT.md)。','Rights remain with the publishers; the repository MIT licence does not license their texts. See [content licensing](../LICENSE-CONTENT.md).'),'']
    return '\n'.join(lines)

def render_archive(catalog,lang):
    tc=lang=='TC'
    def text(zh,en):return zh if tc else en
    lines=[text('# 移出日常閱讀的材料','# Materials removed from daily reading'),'',text('[返回精簡閱讀目錄](../README.zh-Hant.md)','[Back to focused reading](../README.md)'),'',
           text('共21項，保留原件供查閱及驗證歷史題庫；不支援現行題目，也不需要在第一輪逐份閱讀。這是復習取捨，不是判定文件已失效。部分材料仍有獨立例子或歷史資訊；只是不再列入日常閱讀。','21 publications retained for reference and historical bank-source verification. They cannot support active questions and are outside first-pass reading. This is a study selection, not a withdrawal finding. Some contain distinct examples or history; they are not additional daily required reading.'),'',
           text('| 現行編號 | 文件及原件 | 移出原因／改讀甚麼 |','| Current number | Publication and original | Reason / replacement reading |'),'|---|---|---|']
    lines[4:4] = [text('v1.13.2的正式筆記和離線學習包只納入01–26；本目錄的27–47仍供參考，不因本次發佈而納入。見[現行筆記及覆核限制](../../revision/study-notes/README.md)。','The v1.13.2 notes and offline study bundle include only 01–26. This directory remains reference material; publication does not add 27–47 to the selected scope. See [current notes and review limits](../../revision/study-notes/README.md).'),'']
    for d in catalog['documents']:
        if not active(d):
            files=' · '.join(link(primary_path(d,l),l,True) for l in d['editions'])
            lines.append(f'| {d["id"]} | **{title(d,lang)}** · {files} | {d["archive_reason"][lang]} |')
    lines += ['',text('歷史參考資料接續日常材料，統一編為27–47。BI表示中英雙語，ZH表示官方簡體中文；不冒充繁體中文譯本。','Reference materials continue the same sequence as 27–47. BI means bilingual and ZH official Simplified Chinese, not a Traditional Chinese translation.'),'',text('[改號前下載核對歷史](../../bank/audit/history/2026-10-18-download-review-before-continuous-numbering.json)','[Pre-renumbering download history](../../bank/audit/history/2026-10-18-download-review-before-continuous-numbering.json)'),'',text('舊閱讀入口及改號前的原始證據保存在[歷史存檔](../../bank/audit/history/README.md)。原件權利仍屬各發布機構，見[內容授權](../../LICENSE-CONTENT.md)。','Prior reading pointers and original numbering evidence are in the [history archive](../../bank/audit/history/README.md). Rights remain with publishers; see [content licensing](../../LICENSE-CONTENT.md).'),'']
    return '\n'.join(lines)

def main():
    cat=json.loads((HERE/'catalog.json').read_text(encoding='utf8'));docs=cat['documents'];tracked=set()
    assert [d['id'] for d in docs]==[f'{i:02d}' for i in range(1,len(docs)+1)]
    assert len(docs)==47 and cat['schema_version']==5
    assert [d['priority'] for d in docs]==['high']*9+['medium']*17+['low']*21
    assert sum(d['original_bank_source'] for d in docs)==23
    assert [d['id'] for d in docs if active(d)]==[f'{i:02d}' for i in range(1,27)]
    assert cat['question_bank_scope']['documents']==[f'{i:02d}' for i in range(1,27)]
    assert [d['study_focus'] for d in docs[:26]]==['core']*9+['focus']*10+['select']*7
    def verify(path,expected,text=False):
        p=(HERE/path).resolve();assert p.is_relative_to(HERE.resolve()) and p.is_file(),path
        assert p not in tracked,f'Duplicate file: {path}'
        tracked.add(p);raw=p.read_bytes();normal=raw.replace(b'\r\n',b'\n') if text else raw
        assert hashlib.sha256(normal).hexdigest()==expected,path
        if p.suffix=='.pdf':assert raw.startswith(b'%PDF-'),path
        if p.suffix=='.docx':
            with zipfile.ZipFile(p) as z:assert 'word/document.xml' in z.namelist()
    for d in docs:
        assert d['priority'] in PRIORITIES
        for lang,e in d['editions'].items():
            path=primary_path(d,lang);assert pathlib.PurePosixPath(path).name==e['file'] and e['file'].startswith(d['id']+'_'),path
            assert str(pathlib.PurePosixPath(path).parent)==(lang if active(d) else f'archive/{lang}'),path
            verify(path,e['sha256'],path.endswith('.md'))
            assert e['text_file']==f'text/{lang}/{d["id"]}.txt'
            verify(e['text_file'],e['text_sha256'],True)
        assert 'companions' not in d, 'Companions need independent numbers'
        if d.get('parent_document'):
            assert int(d['parent_document']) < int(d['id'])
            assert d['parent_document'] in {x['id'] for x in docs if x.get('kind')!='companion'}
    for lang in ['TC','EN']:
        assert {p.resolve() for p in (HERE/lang).iterdir() if p.is_file()}=={p for p in tracked if p.parent==(HERE/lang).resolve()},f'Unexpected files in {lang}'
    actual={p.resolve() for p in (HERE/'archive').rglob('*') if p.suffix in {'.pdf','.docx','.html','.md','.txt'} and p.name not in {'README.md','README.zh-Hant.md'}}
    assert actual=={p for p in tracked if p.is_relative_to((HERE/'archive').resolve())},'Uncatalogued or missing archive files'
    for name,content in [('README.zh-Hant.md',render(cat,'TC')),('README.md',render(cat,'EN')),('archive/README.zh-Hant.md',render_archive(cat,'TC')),('archive/README.md',render_archive(cat,'EN'))]:
        target=HERE/name
        if '--check' in sys.argv:assert target.read_text(encoding='utf8')==content,f'Regenerate {target}'
        elif not target.exists() or target.read_text(encoding='utf8')!=content:target.write_text(content,encoding='utf8',newline='\n')
    print(f'Checked {count(cat,True)} selected publications, {count(cat,False)} reference publications, all original hashes and four directories.')

if __name__=='__main__':main()
