"""Render this audit's evidence indexes; does not certify source meaning automatically."""
import csv, hashlib, json, sys
from collections import Counter
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent
ROOT = NOTES.parents[1]
sys.path.insert(0, str(NOTES))
import build

def write(name, text):
    (HERE/name).write_text(text.rstrip()+'\n', encoding='utf-8', newline='\n')

def section(n, key):
    return next(s for s in build.PARTS[n]['sections'] if s['id']==key)

def original(doc, lang='TC'):
    if doc=='24': lang='EN'
    ed=build.DOCS[doc]['editions'][lang]
    return '['+ed['file']+'](../../../docs/'+quote(ed['path'],safe='/')+')'

def references(refs):
    return '<br>'.join(original(r['doc'])+' — '+r['locator']['tc']+'<br>'+original(r['doc'],'EN')+' — '+r['locator']['en'] for r in refs)

findings=json.loads((HERE/'findings.json').read_text(encoding='utf-8'))
new=[
    ('F24',6,'wire-receiving','P1','欠缺本地電傳的完整定義，法定最低資料與指引處理缺漏的責任亦未分清。','補明整條機構鏈均須是位於香港的AMLO金融機構；分開附表2第12(6)/(9)條與指引第10.11–10.12、10.20段。',[section(6,'wire-receiving')['blocks'][0]]),
    ('F25',2,'inspection-investigation','P1','查察／調查不遵從、虛假資料及詐騙意圖三層刑責未完整列明。','補責任人、構成條件及兩種定罪程序的刑罰；避免誤套第5條的簡易程序刑罰。',[section(2,'inspection-investigation')['blocks'][0]]),
    ('F26',4,'assessment','P1','通過人士離任及重考安排省略重要期限、例外及起算事件。','補離任通知日起30日、180日續牌分支、獨資例外、重考30日後和續牌到期前限制。',[section(4,'assessment')['blocks'][0]]),
    ('F27',4,'assessment','P2','新牌應考期限寫成籠統「面見後」。','依中文第4.5段改為面見當日起計；重考分別保留中文成績通知發出及英文notification的措辭。',[section(4,'assessment')['blocks'][0]]),
    ('F28',4,'assessment','P1','筆記沒有直接解釋官方來源清單與01–26選定範圍的差別。','補第6.1段的主要依據及樣題不能限定範圍的說明。',[section(4,'assessment')['blocks'][0]]),
    ('F29',4,'assessment','P1','成績及覆檢14日期限被弱化為「通常」，覆檢回覆起點亦未在正文說明。','依第12.1–12.4段刪除通常，明示考試結束、成績通知發出日期及接獲覆檢要求三個不同起點；同步表格。',[section(4,'assessment')['blocks'][1]]),
    ('F35',6,'wire-transfers','P1','cover payment被譯作「掩蓋付款」，容易把付款機制誤認為隱瞞／洗錢。','回03第10.3段中英核實，改為官方中文「直接撥付機制」，保留MT202COV例子及適用規則。',[section(6,'wire-transfers')['blocks'][3]]),
    ('F36',4,'application','P2','公司文件只寫相應成立／周年申報表，不能辨認表格編號及適用公司類型。','回05第16.1–16.3段核對，參考層補NAR1、NNC1、NNC1G、NN3、NN1的對應及與MSO半年申報的區別。',[section(4,'application')['blocks'][1]]),
]
for fid,n,sid,priority,issue,impact,blocks in new:
    row=dict(id=fid,part=n,section=sid,priority=priority,issue=issue,impact=impact,before=None,after=blocks,refs=blocks[0]['refs'],status='fixed')
    findings=[x for x in findings if x['id']!=fid]+[row]
for f in findings:
    f['note_location']=f"part-{f['part']}.html#{f['section']}"
    f['evidence_level']='原文含義對照；不以文字anchor或測試代替'
    for r in f['refs']:
        r['filenames']={lang:build.DOCS[r['doc']]['editions']['EN' if r['doc']=='24' else lang]['file'] for lang in ('TC','EN')}
findings.sort(key=lambda f:int(f['id'][1:]))
write('findings.json',json.dumps(findings,ensure_ascii=False,indent=2))
lines=['# 本輪具體發現及處理','', 'P1：會影響規則適用或重要概念；P2：理解、定位或閱讀問題。這是本輪發現清單，不是未知錯漏數為零的證明。修改前文稿及所有舊審核紀錄保存在 baseline.zip。詳細前後文字見 findings.json。','', '| 編號／優先級 | 筆記位置 | 問題及學習影響 | 原文文件及定位 | 處理 |','|---|---|---|---|---|']
for f in findings:
    lines.append(f"| {f['id']} / {f['priority']} | [Part {f['part']} · {f['section']}](../{f['note_location']}) | {f['issue']} | {references(f['refs'])} | 已修正：{f['impact']} |")
write('FINDINGS.md','\n'.join(lines))

# Correct working-inventory locators after reading the originals; older reviews are untouched.
rows=list(csv.DictReader((HERE/'source-inventory.tsv').open(encoding='utf-8'),delimiter='\t'))
fixes={
    ('1','六組法例、犯罪與披露責任及刑罰'):'1.14–1.27;6.1–6.18',
    ('4','表格、業務計劃政策、聲明見證與支援文件'):'4.14–5.11;16.1–16.3',
    ('5','獨立審核與員工篩選'):'3.11–3.14',
    ('5','集團資訊分享、海外較高標準及不能遵從時處理'):'03 3.15–3.19;04 Sch.2 s.22',
    ('6','原有客戶四觸發、匿名帳戶、同等司法管轄區'):'4.12–4.16',
    ('6','現金、匯款、身分、借貸等可疑指標'):'7.9–7.11',
    ('7','完整重組交易、身分/分析/通訊、格式及獲取'):'03 8.1–8.12;04 Sch.2 ss.20–21',
    ('7','5年不同起點、書面延長、培訓3年、Cap34 12月'):'03 8.3–8.12,9.7;04 Sch.2 ss.20–21;17 s.4',
    ('7','獨立審核四範疇、直接董事高層及補救'):'3.11–3.13',
    ('7','半年電子申報、期間期限、各欄位口徑'):'05 11.2;15全文及附錄',
    ('7','SAFE四步及不能機械決定懷疑'):'7.11',
}
for row in rows:
    row['locator']=fixes.get((row['part'],row['topic']),row['locator'])
    row['topic']=row['topic'].replace('獨立審核四範疇、直接董事高層及補救','獨立審核四範疇、直接高層溝通及相稱頻率').replace('培訓四基本內容五員工群','培訓五基本內容五員工群')
    row['original_files']='; '.join(build.DOCS[d]['editions']['EN' if d=='24' else 'TC']['file'] for d in row['original'].split(','))
    row['review_status']='所列核心概念已對原文及相應正文作含義比較；不代表全文件逐條覆蓋'
with (HERE/'source-inventory.tsv').open('w',encoding='utf-8',newline='') as out:
    w=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)

official=[
    ('有關打擊洗錢及恐怖分子資金籌集與打擊擴散資金籌集的常識','03第1、6章；09、19、22–26；04附表1','概念、法例分工、風險與跨境現金；第25份採相關章節選讀'),
    ('《打擊洗錢條例》第1至7部','04第1–7部（含5A–5C）；03第1章；05','MSO刑責、查察、發牌、紀律及覆核；其他行業對象、監管、條件與期限差異列參考；不搬錄全部行政程序'),
    ('《打擊洗錢條例》的附表','04附表1、2、3–3K、4；03；05','定義、CDD、特別情況、費用、審裁處；3A–3K補用途和條件，其他行業逐項費表／過渡程序保留原文參考'),
    ('海關頒布的指引','01、02、05、06、10–13、16、17、20、21','考核及發牌、適當人選、罰款因素及兌換保障'),
    ('MSO系統及管控(i)：機構層面管治及策略','03第2–3章；07、09、14、20、21','機構及客戶評估、治理、CO/MLRO、集團及政策'),
    ('MSO系統及管控(ii)：AML/CFT管控範疇','03第4–6、10–11章及7.9–7.11；04附表2；06–09、14、18、24、25、26','CDD、BO、PEP、中介、監察、制裁、匯款與警號'),
    ('MSO系統及管控(iii)：證明符合規定及監察合規水平','03第7–9章及3.11–3.14；04附表2；05、06、15、17、21','STR、紀錄、獨立審核、培訓及半年申報'),
]
lines=['# 官方要求 → 選定原文 → 筆記位置','', '官方模組依第01份第5.2段；每個模組五題。下表的原文歸類和學習優先級是本次整理判斷，並非官方逐項考點清單或權重。每項完整文件名在下方原文索引及具體發現中列明。','', '| Part／官方模組 | 原文依據 | 本輪判斷／邊界 | 筆記 |','|---|---|---|---|']
for n,(title,src,limit) in enumerate(official,1):
    lines.append(f'| {n} {title} | {src} | {limit} | [Part {n}](../part-{n}.html) |')
lines+=['','## 原文先行核心清單','',f'共{len(rows)}組核心概念；這是學習單元數，不是覆蓋率。先建立清單，再與文稿比較；核對後更正本輪清單定位。高＝決定規則適用、法定責任或核心定義；中＝重要理解或必要參考。未推算出題頻率。','', '| Part | 概念／學習方式 | 原文與定位 | 筆記位置 |','|---|---|---|---|']
for row in rows:
    src='<br>'.join(original(d) for d in row['original'].split(','))+'<br>'+row['locator']
    links='、'.join(f"[{key}](../part-{row['part']}.html#{key})" for key in row['note_section'].split(','))
    lines.append(f"| {row['part']} | {row['topic']}<br>{row['priority']}：{row['learning']} | {src} | {links} |")
lines+=['',f"## 所有{sum(len(p['sections']) for p in build.PARTS.values())}個主題的文稿入口",'', '以下是筆記引用的導航清單；自動列出引用不構成另一份語義審核證明。核心清單與SOURCE-REVIEW.md才界定本輪閱讀範圍。','']
for n,part in build.PARTS.items():
    lines.append(f'### Part {n}\n')
    for s in part['sections']:
        docs=sorted({r['doc'] for b in s['blocks'] for r in b['refs']})
        lines.append(f"- [{s['title']['tc']}](../part-{n}.html#{s['id']})：原文{', '.join(docs)}。")
write('COVERAGE.md','\n'.join(lines))

reviews={
    '01':('TC/EN全文；重點5.1–5.3、6.1、7及考核期限。','官方格式及七模組已核；最新性見REPORT，不以存檔日期佐證。'),
    '02':('TC/EN全文七例。','只分析多陳述組合、條件及單一答案題型；不從樣題推算完整範圍。'),
    '03':('EN全部77頁；TC全部87頁，含附錄、腳註及詞彙。','核心術語、完整清單、AND/OR、門檻及起算已與Part1–7比較；按既定衝突決定處理語言差異。'),
    '04':('EN目錄及全部正文／附表已讀（實體PDF頁25–456）；原先待查106–296及401–447已補讀。TC核心及新增定義／條件逐項對照，包括ss.10/13、電傳、TCSP、VA、DPMS。','完成全冊英文內容的學習範圍重評與核心比較；第5A–5C部及3A–3K採制度／條件參考層，不逐項搬錄其他行業費表、審計呈報、介入及歷史過渡程序。TC並非全冊逐行翻譯審校。'),
    '05':('TC全部24頁及EN全部28頁；費用EN第26頁另看PDF表格。','發牌、場所、帳戶、提名／續牌、定期申報及2026年5月費用已比較；行政申請附件維持參考層級。'),
    '06':('TC/EN整份存檔Markdown：AML問答1–28、發牌及技術問題。','關鍵身份、BO、PPTA、PEP、監察與記錄例外已對照；電話／瀏覽器／上載限制屬操作參考，不要求背誦。未把存檔日期當網站最新證明。'),
    '07':('TC/EN全文及三個附錄。','客戶風險、BO及代表客戶者的實際缺失，補入Part5/6。'),
    '08':('TC/EN全文及腳註。','八項警號、十二項管控、第三方及低風險例外已比較；非無條件接受第三方付款。'),
    '09':('TC/EN全文及註。','PF評估、制裁及舉報；2021文件的歷史背景與一般責任分開。'),
    '10':('TC/EN全文。','適當人選的法定與額外考慮；不把單項因素當自動不合格。'),
    '11':('TC/EN全文，6(a)–(r)十八例。','完整項目核對；正文合併相近因素，但保留持續符合及個案判斷。'),
    '12':('TC/EN全文。','第43條制度；四因素組及細項、阻嚇／財政資源等。'),
    '13':('TC/EN全文。','第21條制度；不可把最高三倍與實際罰額自動掛鈎。'),
    '14':('TC/EN全文及腳註。','使用交付渠道前評估、持續覆核、境外行為及舉報。'),
    '15':('TC/EN全部5頁；附錄PDF第3–5頁直接查看。','交易期間／截止日分開；兌換、匯款、比例100%、STR／命令及資產估值欄位。'),
    '16':('TC/EN全文。','與17配對核對；修訂日期保留為該通函記載。'),
    '17':('雙語原件全部17頁；第14頁交易單PDF另查看。','100000適用界線、單據六資料、撤銷條件／3日、12月紀錄、匯率及17指定貨幣。'),
    '18':('TC/EN全文。','TBML四類風險、要求及STR；細指標由24英文原件核。'),
    '19':('TC/EN全部3頁及腳註。','明標2026年7月3日通函／6月19日聲明；不當作2026年10月現行國家名單認證。'),
    '20':('TC/EN全文17項表格。','全部項目已列；申請支援細節參考，責任／資金流／渠道保持正文。'),
    '21':('TC/EN全文19項表格。','全部項目及政策應包含的操作內容已比較；舊詞語依03/04及既定衝突處理。'),
    '22':('TC/EN全文。','配23釐清旅客、貨物及嚴格大於120000。'),
    '23':('雙語原件全部47頁，包括附表1–5及貨物條文重新核對。','管有、幼年人、同批次合併、申報責任與法定例外；表格欄位列參考。'),
    '24':('英文原件全部10頁；四組35項指標（12/7/8/8）。','沒有官方中文版。TC文稿明示學習譯文，兩語引用均指向英文實際檔名；例子不是定罪準則。'),
    '25':('EN全197頁已讀（含空頁、其他行業及附件）；TC對照核心及新增概念相應段落。PDF頁24–26、79、143風險圖另查看。','已完成全報告的主題取捨重評：補跨行業戶口／法人／支付機制、TF及PF；行政統計、機構沿革及其他行業細節保留參考，不當作MSO必背清單。完整閱讀不等於所有文字均納入筆記或每張圖逐像素核對。'),
    '26':('EN全文3頁；TC第1頁文字加第2–3頁PDF直接查看。','TC提取文字不完整，未改原件／提取檔／舊哈希；按PDF核對制裁預警及相關責任。'),
}
lines=['# 原文閱讀範圍與剩餘項','', '日期：2026-10-19。以下是本輪實際閱讀界線，不援引舊QA或舊review作內容正確證明。頁碼指實體PDF頁序；文稿引用優先使用段落／條文，兩者不要混同。第06份是Markdown而非PDF。','', '| 原件（完整檔名） | 本輪已讀／核對 | 覆蓋判斷及未完成範圍 |','|---|---|---|']
for doc,(scope,limit) in reviews.items():
    lines.append(f'| {original(doc)}<br>{original(doc,"EN")} | {scope} | {limit} |')
lines+=['','## 第25份的取捨結論','',
'只保留行政摘要、方法及MSO章節不足以支持「看筆記便能理解主要機制」：跨行業法人／戶口濫用、貿易洗錢、貸款與科技手法，以及TF渠道、NPO脆弱性和PF制裁風險容易整塊缺席。本輪已從第4、7、8、9章補入相關機制、典型例子及PACE，全部保留2022年背景。', '',
'補讀其餘行業後，另補遙距身分認證與真人傀儡帳戶的區別、多重支付中介／第三者資金流、產品功能差異與虛假VA投資例子。銀行、證券、保險、其他金融服務與DNFBP的詳細統計、制度沿革及附錄索引不放主閱讀位置；學習效益低於MSO義務、通用風險和可疑行為。此為本輪學習排序，不是官方排除。2022年VA／DPMS提案與04所存已成文制度分開。','',
'## 範圍內仍不能認定完整的部分','',
'- 第04份：英文原文已讀完；其他行業詳細費用、財務報表細目、審計／介入行政程序及過渡安排未逐條寫成筆記。優先級低至中，制度基本界線已補。官方沒有明文排除這些內容，所以本套是經取捨的MSO參考筆記，不是條例逐條替代品。',
'- 第25份：英文全報告已重評；其他行業每項統計、機構沿革、案例金額及未採用圖中細節不逐一列入筆記。優先級低，保留2022年原文查考，不宣稱這些文字不可能被問及。',
'- 中文語義核對並非第04、25份全冊逐行翻譯審校；已修改條文和核心決定條件有中英對照，其他頁段不冒稱完成。',
'- 01–26外官方新通函的具體內容、即時制裁名單和最新整部法例，不能靠本套固定版本筆記替代。見REPORT的獨立缺口表。']
write('SOURCE-REVIEW.md','\n'.join(lines))

lines=['# 範圍外原件索引','', '這些資料沒有加入正式筆記／題庫。官方網址來自原件目錄；網址存在不代表本輪已成功重新下載每一份。實際閱讀深度及已識別缺口見REPORT.md。','', '| 編號 | repo原件 | 官方來源 | 本輪閱讀深度 |','|---|---|---|---|']
for num in range(27,48):
    doc=f'{num:02d}';d=build.DOCS[doc]
    lang=next(l for l in ('TC','EN','ZH','BI') if l in d['editions']);ed=d['editions'][lang]
    depth='目錄層面；未深入逐條審核'
    if num in (33,41,42,43):depth='TC全文（1頁）及與01–26的內容比較'
    if num in (39,40):depth='主題／目錄及所列重點定位；未全份視覺核對'
    if num==45:depth='官方英文通函內容已讀；諮詢不等於現行本地規定'
    lines.append(f"| {doc} | {original(doc,lang)} | [官方網址]({ed['url']}) | {depth} |")
write('OUTSIDE-SOURCES.md','\n'.join(lines))

visuals=json.loads((HERE/'visual-review.json').read_text(encoding='utf-8'))
reasons={
 'ml-tf-pf':'以資金來源／目的與核心區別對照ML、TF、PF；尤其防止把TF等同非法來源。保留短表，不暗示三者互斥。',
 'risk-lists':'按發布者與法律／風險作用區分FATF兩類名單及UN制裁；不是國家永久分類，也不以灰名單自動觸發同一措施。',
 'penalty-ceilings':'同欄比較第21與43條的適用原因及罰額上限，避免把100萬元、1000萬元及三倍互換；不是固定罰款價目表。',
 'ownership-boundary':'把超過25%與恰好25%並列，同時緊貼其他控制／代表行事分支；不能用持股比例單獨排除BO。',
 'fee-components':'以收費事項及計費單位比較，每人／每處所／每次清楚；費率保留2026年5月版本。',
 'three-places':'以功能及何時需要比較特定營業處所、LMO、LPS；避免誤認三者必須同時存在。',
 'assessment-pass':'只用AND示意總分及逐Part兩條件；真實同時成立關係，不加入猜題流程。',
 'exchange-rights':'以交易前／後、啟動條件及法律效果對照拒絕交易與撤銷；緊貼違規前提，避免誤認無條件冷靜期。',
 'risk-levels':'以評估對象與用途比較機構、客戶及交易層面；不是高／中／低的互斥分類流程。',
 'review-frequency':'並列機構兩年／事件觸發、較高風險客戶至少每年及風險相稱審核；明示沒有共同起點。',
 'sow-sof':'同維度比較整體財富的形成與特定資金來源；例子幫助辨別索取資料的目的，不列為唯一證據。',
 'pep-categories':'按重要公職所屬地方／組織、風險條件與措施對照三類；前任PEP退出條件保留正文。',
 'reliance-outsourcing':'比較中介依賴與外包的關係及責任；持續監察不可按第18條轉移，兩者都不免除MSO責任。',
}
for v in visuals:
    v['reason']=reasons.get(v['id'],v['reason'])
    v['mobile_bilingual']='保留／重做項已在390px及1440px、TC/EN/雙語檢查；手機表格逐列顯示欄名。刪除項不再渲染。'
write('visual-review.json',json.dumps(visuals,ensure_ascii=False,indent=2))
counts=Counter(v['action'] for v in visuals)
lines=['# 27個原有圖表逐項決定','',f"保留{counts['retain']}、重做{counts['replace']}、刪除{counts['remove']}；結果18張表及2個示意圖。先以三階段、金額界線、期限和電傳資料驗證，再一致套用適合內容。保留B風格，沒有引入外部圖表工具。",'', '| Part／圖表 | 決定 | 比普通段落更清楚之處／刪除原因 |','|---|---|---|']
for v in visuals:
    lines.append(f"| {v['part']} / {v['id']} | {v['action']} | {v['reason']} |")
lines+=['','## 實際畫面檢查','', '七Part × 三語言 × 兩視窗共42個情境，逐頁截圖並查看七份六格預覽；另查看門檻、期限、電傳及紀錄的代表性完整截圖。沒有將自動版面檢查視為學習效果證明：這些圖表的保留理由是能比較同一維度、顯示真正AND／OR或分清各自起算點。','', '手機雙語長表仍較長，但每列保留欄名和緊貼條件；不橫向截斷正文。Part導航容許水平捲動。沒有把所有條件壓縮成複雜判斷流程。']
write('VISUAL-REVIEW.md','\n'.join(lines))

baseline=json.loads((HERE/'baseline.json').read_text(encoding='utf-8'))
changes=[];missing=[]
for name,old in baseline['sha256'].items():
    p=ROOT/name
    if not p.exists(): missing.append(name);continue
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    if digest!=old: changes.append(dict(path=name,before=old,after=digest))
write('baseline-comparison.json',json.dumps(dict(baseline_utc=baseline['captured_utc'],files_compared=len(baseline['sha256']),changed=changes,missing=missing),ensure_ascii=False,indent=2))
print(json.dumps(dict(findings=len(findings),core_groups=len(rows),visuals=dict(counts),changed_baseline_files=len(changes),missing=missing),ensure_ascii=False))
