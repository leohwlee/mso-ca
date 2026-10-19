"""Record the completed manual review; the inventory itself is not semantic proof."""
import json, sys, re
from pathlib import Path
from urllib.parse import quote
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
import build

def save(name, value):
    (HERE/name).write_text(value,encoding='utf-8')
def source(doc,lang):
    ed=build.DOCS[doc]['editions'][lang]
    return f"[{ed['file']}](../../../docs/{quote(ed['path'],safe='/')})"

findings=json.loads((HERE/'findings.json').read_text(encoding='utf-8'))
# Statute/paragraph locators are stable and preferred to mixed physical/page labels.
for f in findings:
    f['evidence']=re.sub(r'（(?:TC|EN|兩語)[^）]*(?:PDF|同條|同段|同名段落)[^）]*）','',f['evidence'])
    doc='25' if f['id'] in ('C01','C02','C03','C04','C05') else '04'
    f['source_files']={lang:build.DOCS[doc]['editions'][lang]['file'] for lang in ('TC','EN')}
    f['source_doc']=doc
save('findings.json',json.dumps(findings,ensure_ascii=False,indent=2)+'\n')

rows=[]
for n,part in build.PARTS.items():
    for s in part['sections']:
        for i,b in enumerate(s['blocks']):
            refs=[r for r in b['refs'] if r['doc'] in ('04','25')]
            if refs:
                rows.append(dict(part=n,section=s['id'],title=b['title'],block=i+1,
                    point_pairs=len(b['points']),refs=refs,type='正文',
                    review='已對照中文原文核對含義，並比較英文條件及例外'))
        for panel in build.PANELS.get(n,{}).get(s['id'],[]):
            refs=[r for r in panel['refs'] if r['doc'] in ('04','25')]
            if refs:
                rows.append(dict(part=n,section=s['id'],title=panel['title'],id=panel['id'],
                    refs=refs,type='圖表',review='已對照中文原文核對含義，並比較英文條件及例外'))
for row in rows:
    for r in row['refs']:
        r['files']={lang:build.DOCS[r['doc']]['editions'][lang]['file'] for lang in ('TC','EN')}
save('coverage-review.json',json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
counts={doc:sum(x['type']=='正文' and any(r['doc']==doc for r in x['refs']) for x in rows) for doc in ('04','25')}
panels=sum(x['type']=='圖表' for x in rows)
coverage=['# 第04／25份中文原文與筆記對照','',
    '日期：2026-10-19。這是本輪已實讀及比較後的定位表；由文稿抽取引用，只用來列明範圍，不能自行證明含義正確。正文組含有其他來源時，本表只確認04／25支持的陳述。', '',
    f"正文：04有{counts['04']}組，25有{counts['25']}組；相關圖表{panels}張。定位與實際檔名如下。修正詳見[報告](REPORT.md)，沒有發現需修改的內容予以保留。",'']
for n in range(1,8):
    coverage += [f'## Part {n}','']
    subset=[x for x in rows if x['part']==n]
    if not subset:coverage+=['本Part沒有直接引用04／25的正文或圖表。','']
    for x in subset:
        coverage += [f"### {x['title']['tc']}（{x['type']}）",'',
            f"筆記：[Part {n} / {x['section']}](../part-{n}.html#{x['section']})。{x['review']}。",'']
        for r in x['refs']:
            for lang,key in [('TC','tc'),('EN','en')]:
                coverage += [f"- {source(r['doc'],lang)}：{r['locator'][key]}。"]
        coverage+=['']
save('COVERAGE.md','\n'.join(coverage))

report=['# 第04／25份中文原文後續核對：完成報告','',
    '日期：2026-10-19。已完成下述筆記範圍的中文含義及中英文條件／例外核對，落實17組修正並重新生成七個Part。沒有把已確定問題留作待辦；沒有新增須由使用者裁決的原文衝突。','',
    '## 核對範圍及版本','',
    f"本輪包含全部直接引用04／25的正文組（04：{counts['04']}組；25：{counts['25']}組），以及{panels}張相關圖表。逐組位置、兩語原件檔名和條文／段落見[COVERAGE.md](COVERAGE.md)。本表中的已核對是原文含義比較，不是只找得到文字。",'',
    '第04份按2026年9月24日綜合版存檔；第25份按2022年報告。這次沒有重新核實即時法例版本，也不把2022年的風險評級、統計或名單稱為現況。官方考試範圍核實與法例版本核實是不同工作；前輪官方範圍及01–26外缺口記錄保留於[獨立審核報告](../independent-audit-2026-10-19/REPORT.md)，本輪沒有新增範圍外正文。','',
    '本輪中文閱讀涵蓋04的核心正文、MSO發牌／執法、覆核／保密、附表1–4，以及筆記所採用的TCSP、VA、DPMS制度和適用界線。25涵蓋前言、摘要、方法、MSO全章、已採用的案例／腳註、其他行業比較、法人、TF及PF段落。未將原書每項其他行業費表、行政細節、歷史統計全部改寫為筆記；也不聲稱對兩冊所有未採用文字完成逐行翻譯審校。','',
    '第25份不能只保留摘要與MSO章：方法／評級、cash kiting犯罪得益、跨行業脆弱性、法人、非牟利組織與TF／PF會影響理解。本輪已核對這些現有內容並修正條件；其他行業逐項歷史統計保留原文參考，沒有把其取捨宣稱為官方不考。','',
    '## 已落實發現','',
    'P1表示會改變適用條件、責任、權力或法律結論；P2表示定義理解、定位或版本表述問題。這是修正優先級，不是官方考點權重。','']
for f in findings:
    report += [f"### {f['id']} · {f['priority']} · {f['location']}",'',
        f"問題及影響：{f['problem']}",'',f"處理：{f['result']}",'',
        f"原文定位：{f['evidence']}。",'',
        f"- {source(f['source_doc'],'TC')}",f"- {source(f['source_doc'],'EN')}",'',
        '狀態：已修改內容源並重新生成。','']
report += ['## 歷史記錄及視覺表達','',
    'C09明確更正前輪F07的錯誤判斷。舊F07、原始哈希、QA及其他審核記錄均未覆寫，不能再以舊結論支持「已開始刑事程序」或「免費查閱」。本輪另存70檔修改前基線，見baseline.zip及baseline.json。','',
    '保留現有B風格、18張對照表及2個示意圖。本輪修正實益擁有人表的信託列，使受益人類別、既得財產權益及控制條件與正文一致；手機繼續將每一類的規則及例外放在一起。其他行業適用界線採參考文字清單，避免把AND／OR條件硬畫成流程。本輪沒有新增、刪除或用裝飾卡片替換圖表。','',
    '目前75個主題、497組雙語要點；本輪開始為75個主題、488組。這些是規模數據，不能當覆蓋率。','',
    '## 實際驗證及其界線','',
    '- 原文含義：完成上述正文組和相關圖表的中文核對及英文條件比較；原件圖示／表格另查看25中文PDF第25、93頁及04中文PDF第399頁。',
    '- 自動檢查：目錄原件哈希、生成一致性、來源定位及題庫路徑檢查通過；Python 16項測試、JavaScript 8項測試及Go測試通過。詳見[verification.json](verification.json)及[supplemental-checks.json](supplemental-checks.json)。',
    '- 瀏覽器：七Part × 三種語言 × 電腦／手機，共42組；另24組修正重點、21個實際練習入口及6個索引組合通過。離線測試無遠端請求，未發現橫向溢出或語言混顯。詳見[browser-checks.json](browser-checks.json)、[correction-display.json](correction-display.json)、[integration-checks.json](integration-checks.json)。',
    '- 實際查看：已查看七Part的三語／雙屏幕預覽拼圖，另看取走紀錄雙語桌面、信託表雙語手機、NPO中文手機、適用界線英文桌面。這不是逐像素查看每一長頁的聲明。',
    '- 保護檢查：348個原基線中的筆記以外檔案及54個本輪受保護檔案未變，包括來源、題目／答案／ID及舊審核證據。',
    '- 最後題庫查漏僅重新檢查525個ID及來源路徑；沒有把路徑通過當成525題語義全部覆蓋，也沒有從答案解釋補寫內容。','',
    '自動定位成功不等於含義正確；測試通過不等於沒有未知遺漏。本輪完成的是上述明確範圍，不能保證涵蓋每道未知官方考題。沒有修改題庫、評分或歷史成績兼容性，沒有推送或公開發佈。','',
    '## 閱讀與預覽','',
    '- [七Part入口](../index.html)',
    '- [Part 3三語及電腦／手機預覽](previews/part-3-all-modes.png)',
    '- [信託對照表：雙語手機](previews/correction-trust-both-mobile.png)',
    '- [紀錄保留條件：雙語桌面](previews/correction-retained-records-both-desktop.png)','']
save('REPORT.md','\n'.join(report))
working=(HERE/'WORKING.md').read_text(encoding='utf-8')
working=working.replace('待落實的有據修正：','以下是修正前工作筆記（全部已處理；不作最終措辭依據）：')
working=working.replace('最終結果見REPORT.md。','最終結果見[REPORT.md](REPORT.md)。17組發現全部已修正、重新生成及驗證；下文保留工作過程，最終恐襲級別用中文原文「中（moderate）」。')
save('WORKING.md',working)
print(json.dumps({'blocks':counts,'related_visuals':panels,'findings':len(findings)},ensure_ascii=False))
