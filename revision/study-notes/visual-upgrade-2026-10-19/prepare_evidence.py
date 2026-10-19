"""Record the approved plan, dispositions and new evidence without rewriting history."""
from pathlib import Path
import sys,json,hashlib,datetime,shutil,html
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.path.insert(0,str(HERE.parent))
import build
V=Path('C:/Users/leohw/.codex/visualizations/2026/10/19/01a1529a-1926-73f0-baf0-458d3f97f433')
for src,dest in [('visual-assessment.json','approved-assessment.json'),('visual-semantics-final-review.json','independent-source-review.json')]:
    shutil.copyfile(V/src,HERE/dest)
approved=json.loads((HERE/'approved-assessment.json').read_text(encoding='utf-8'))
previous=json.loads((HERE/'panels-before.json').read_text(encoding='utf-8'))
old={p['id']:p for ss in previous.values() for ps in ss.values() for p in ps}
current={p['id']:(n,s,p) for n,ss in build.PANELS.items() for s,ps in ss.items() for p in ps}
descriptions={
'three-stages':'保留三階段概念；改為同一犯罪得益的三個獨立機制例子，沒有強制順序。',
'ml-tf-pf':'重整為資金來源、核心問題、法律條件的共同維度。',
'risk-lists':'保留對照表；具體名單仍保留日期，沒有畫成永久分類。',
'licence-clocks':'改為獨立事件／時間要求軌；取消會誤導提前期限的統一時間箭頭。',
'penalty-ceilings':'改為兩項上限公式；每日罰款另列，最高額不等於必罰額。',
'money-boundaries':'按CDD／匯款、跨境現金、找換保障分組；各保留對象、符號、觸發及例外。',
'ownership-boundary':'保留公司／合夥／信託定義表，連結Part6角色與25.1%例子。',
'fee-components':'保留收費組件表；明寫基本費＋額外處所＋適用逐人測試費，版本不變。',
'three-places':'保留營業處所／LMO／LPS表；共同維度比流程圖更合適。',
'assessment-pass':'保留既有AND及整體達標但單Part不及格例子，未假稱新增。',
'assessment-clocks':'分申請／人事、結果／重考、覆核成績三組，起算詞保持原意。',
'exchange-rights':'改為交易完成前／後兩條分支；保留第4條違反及3日撤銷條件。',
'risk-levels':'改為機構評估→制度資源、客戶評估→CDD監察的兩層關係。',
'review-frequency':'保留週期與事件觸發對照，不造共同時間軸。',
'party-roles':'公司、BO、PPTA及董事的有向關係；可兼任、25%邊界及信託例外緊貼。',
'sow-sof':'同一人物的整體財富與本次資金兩條來源路徑，銀行只作渠道。',
'pep-categories':'保留身分類別／高風險矩陣，離任狀態跨類別，共同AND措施抽為相鄰圖。',
'transfer-information':'共同必需資料＋達門檻加項；至少一項OR，出生日期AND地點同組。',
'reliance-outsourcing':'保留同維度對照，MSO責任不轉移；不強加箭頭。',
'retention-clocks':'獨立事件／時間要求軌，關係全期＋結束後5年、交易完成後5年與培訓3年分開。'}
ledger=[]
for key,(n,s,p) in current.items():
    ledger.append(dict(id=key,part=n,section=s,kind=p['kind'],status='adapted-or-retained' if key in old else 'added',decision=descriptions.get(key,'新增：'+p['title']['tc']),location=f'part-{n}.html#memory-{key}',sources=[dict(doc=r['doc'],filename={l:build.DOCS[r['doc']]['editions']['EN' if r['doc']=='24' else l]['file'] for l in ('TC','EN')},locator=r['locator']) for r in p['refs']]))
(HERE/'dispositions.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# 七個Part可視化實施記錄','', '本輪把已批准的評估方向應用到正式閱讀頁。原有20個面板全部逐項處理，新增13個，共33個：11張表、22個圖解，其中3棵決策樹（CDD觸發、CDD程度、指明決定生效）。這是規模統計，不是學習成效或完整率。','',
'75個主題及533組雙語正文要點仍完整可見。示例與規則分開；所有圖保留實際原件檔名及定位。沒有引入第三方圖表套件或網絡資源，沒有修改題目、答案、評分、ID、歷史成績或原文。','',
'## 原有20個面板的處理','', '| Part | 面板 | 處理 |','|---|---|---|']
for key in old:
    n,s,p=current[key];lines.append(f'| {n} | [{p["title"]["tc"]}](../part-{n}.html#memory-{key}) | {descriptions[key]} |')
lines+=['','## 新增圖解','']
for d in ledger:
    if d['status']=='added':lines.append(f'- Part {d["part"]}：[ {current[d["id"]][2]["title"]["tc"]}](../{d["location"]})。')
lines+=['','## 取捨','',
'期限沒有共用起點，採獨立對照軌，不畫一條橫跨多種事件的時間軸。CO／MLRO可兼任，PEP離任狀態跨類別，圖形沒有暗示互斥。電傳的機構傳遞責任與資料AND／OR分開。AML三階段可重疊，例子不代表唯一方式。',
'SAFE四步沿用原有簡短流程，沒有再加一張重複圖。定期申報的半年涵蓋期與提交截止日保留清楚正文，沒有額外日曆；延遲核實的條件已由CDD圖導向正文，沒有再造多層決策樹。對一般定義、例外及行政細節仍用文字。未加入27–47或新題庫內容。',
'', '## 審查發現及修正','',
'1. **正式原稿錯誤（重要）**：Part1貨物合併英文把多名托運人共用貨代時的貨代當作客戶。已依第23份第10(1)–(4)條改為同一人／同一承運人、同一客戶及同一代運人的正確條件；中英文均明寫「運送或安排運送」。這不是原文衝突，直接修正。',
'2. **新增圖草稿（重要）**：空殼銀行初稿混入一般國際表述。已改用第04份附表2第17條：香港以外成立、銀行許可、無實體經營、不隸屬符合三條件的銀行法團；實體經營為當地處所AND至少一名全職銀行職務員工。',
'3. **新增圖草稿（重要）**：查察用語改為「訂明規定」，調查分清第11(1)(a)合理因由相信可能犯罪與(b)為考慮紀律處分而查究。',
'4. **新增圖草稿（重要）**：CDD基本措施補上「如有BO」「目的性質並非明顯」「代表合理核實」；合理相信追查會通風報訊的例外移到觸發分支旁並連結Part7。',
'5. **新增圖草稿（重要）**：CBNI改為法定批次而非單一consignment；旅客非指定入境／離境保留披露後須申報及豁免條件。',
'6. **圖形含義**：貨值與發票價值差異改用≠；公司架構的箭頭指向被掩藏的控制者／來源。期限取消統一向右箭頭，避免45日前誤讀為45日後。OR改成至少一項；出生日期AND地點保持一組。',
'7. **雙語閱讀**：相同MSO／MLRO／JFIU字樣只顯示一次；真正不同的中英文仍逐個語義單元配對。跨Part圖解連結保留選定語言。',
'','上述第1項原件：`'+build.DOCS['23']['editions']['EN']['file']+'`（與TC同一雙語原件），第10條。其餘圖逐項原件檔名及段落見[dispositions.json](dispositions.json)；獨立來源核對見[independent-source-review.json](independent-source-review.json)。',
'','## 驗證與界線','',
'- 原文定位：生成器核對01–26引用文字錨點、實際原件及頁內連結；這只證明定位成功。',
'- 含義核對：獨立來源評審對CDD、PEP、電傳、STR、保存期、覆核生效、空殼銀行、查察調查及貨物合併核對03／04／23原文；設計評審獨立檢查關係與分支、手機雙語，已處理其全部具體建議。',
'- 顯示：42種整頁組合（7×3語言×2尺寸），198種圖解組合（33×3×2），另21個練習入口及6個首頁組合。實際結果以[verification.json](verification.json)、[browser-checks.json](browser-checks.json)、[visual-display-checks.json](visual-display-checks.json)及[integration-checks.json](integration-checks.json)為準。',
'- Python測試16項、Node測試8項、Go測試及來源／審核檢查記錄於verification.json。最初Python臨時目錄及沙盒瀏覽器啟動失敗屬環境限制；改用可寫臨時目錄及獲准的本機無頭瀏覽器，沒有放寬檢查。',
'- 題庫僅於內容完成後執行525個ID／來源路徑檢查，結果[bank-source-routes.json](bank-source-routes.json)。未用題幹填筆記，這不代表逐題語義完整。',
'- 基線891個檔案雜湊及修改前主檔ZIP保留；[preservation.json](preservation.json)比較本輪前後改動。歷史審核證據不改寫；本輪結論不替代先前官方範圍報告，也不是整套原文再次逐行審核。',
'- 本輪完成範圍是七篇的可視化實施及新增圖示含義復核。未進行真實學習者記憶效果試驗，不能聲稱提高了某個分數，亦不保證未知官方試題。',
'','[代表性預覽](preview.html) · [正式閱讀入口](../index.html)','',
'English summary: Approved visualization changes are implemented across all seven parts. Original prose and qualifications remain visible. Three genuine decision trees are used selectively; other content uses comparisons, relationships, data groups and independent deadline references. Tests, source-location checks, targeted semantic review and learner outcome evidence are explicitly distinguished. No publication or bank mutation was performed.']
(HERE/'REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
selected=[(1,'three-stages','洗錢三階段'),(2,'review-commencement','指明決定生效'),(3,'money-boundaries','金額與適用制度'),(4,'assessment-clocks','評核期限'),(5,'control-responsibilities','CO／MLRO／獨立審計'),(6,'cdd-trigger-tree','CDD觸發條件'),(7,'reporting-route','內部報告及JFIU')]
cards=[]
for n,key,title in selected:
    fn=f'previews/figure-p{n}-memory-{key}-tc-desktop.png'
    cards.append(f'<article><h2>Part {n} · {title}</h2><p><a href="../part-{n}.html?lang=tc#memory-{key}">開啟正式筆記</a> · <a href="{fn}">查看完整預覽</a></p><a href="{fn}"><img src="{fn}" alt="{html.escape(title)}的實際桌面截圖" loading="lazy"></a></article>')
(HERE/'preview.html').write_text('<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>七個Part圖解預覽</title><style>body{margin:0;background:#edf2f6;color:#263e52;font:17px/1.8 "Microsoft JhengHei",sans-serif}main{max-width:1100px;margin:auto;padding:36px 24px}h1,h2,a{color:#173f63}h1{font-size:28px}h2{font-size:22px}article{background:white;margin:28px 0;padding:28px;border-top:2px solid #173f63}img{display:block;width:100%;height:auto;max-height:650px;object-fit:contain;object-position:top}a{overflow-wrap:anywhere}@media(max-width:600px){main{padding:20px 12px}article{padding:18px}}</style><main><h1>七個Part：已套用的圖解</h1><p>以下是正式筆記的實際截圖。三種語言均可在閱讀頁切換；手機按語義單元排列，保留條件與原件引用。</p><p><a href="../index.html">開始閱讀</a> · <a href="REPORT.md">實施及驗證記錄</a></p>'+''.join(cards)+'</main></html>',encoding='utf-8')
# Sync the documented extension without changing primitive tokens or old critique records.
f=ROOT/'.impeccable/design.json';d=json.loads(f.read_text(encoding='utf-8'))
d['generatedAt']=datetime.datetime.now(datetime.timezone.utc).isoformat()
d['narrative']['rules']=[r for r in d['narrative']['rules'] if r['name']!='Source-bound Visual Rule']
d['narrative']['rules'].append(dict(name='Source-bound Visual Rule',section='typography',body='Use labelled relationships, genuine decision branches, separate deadline origins and explicit ALL/AND or AT LEAST ONE/OR. Keep conditions adjacent; label teaching examples. ML stages may overlap. Stack semantic units on phones and render identical bilingual tokens once.'))
d['components']=[c for c in d['components'] if c.get('name')!='Learning decision branch']
d['components'].append(dict(name='Learning decision branch',kind='custom',description='Offline reading diagram with explicit yes outcome and no continuation; source citations remain visible.',html='<div class="branch"><b>Applicable condition</b><p>YES → applicable action</p><p>NO ↓ next condition</p></div>',css='.branch{background:#fff;color:#263e52;border-left:2px solid #d5e0e8;padding:16px 24px;font:17px/1.8 sans-serif}.branch b{color:#173f63}'))
f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Recorded 20 dispositions, 13 additions and source filenames; prepared report and preview.')
