"""Produce this round's evidence index without modifying prior rounds."""
from pathlib import Path
import json,sys,hashlib
HERE=Path(__file__).resolve().parent;NOTES=HERE.parent;ROOT=HERE.parents[2]
sys.path.insert(0,str(NOTES))
import build
rows=json.loads((HERE/'findings.json').read_text(encoding='utf-8'))
intro='''# 第04、25份未納入內容：具體發現

本輪14組補充已寫入內容源並生成頁面。優先級為學習用途排序，不是官方考點權重。
每組位置指向正式閱讀頁；條件與例外已對照中英文原文核對，不以文字定位成功代替含義核對。

'''
before={
'O01':'只有洗錢定義及階段，缺「處理」範圍與上游罪行無須另證的意思。',
'O02':'法律名稱已有，但限制、沒收／充公及凍結用途、門檻及例外不夠自足。',
'O03':'STR義務已有，缺JFIU分析與獨立檢控的分工，易把懷疑門檻混成定罪證據。',
'O04':'跨境合作未有可學習的情報／法律程序區分。',
'O05':'跨境現金規則已有，缺申報合規與洗錢來源判斷分開的原文例子。',
'O06':'帳戶模式只見部分例子，未完整列出第4.63段七類觀察。',
'O07':'跨行業風險已有概括，未充分解釋保險、物業與專業服務如何介入洗錢。',
'O08':'未解釋SCR，讀者難理解公開查冊、公司控制名冊、執法權與MSO取得資料的不同。',
'O09':'「客戶資產有獨立保障」未說保障針對哪種執行，及合法申索／留置權例外。',
'O10':'VA只介紹定義、發牌與無牌罰則，欠兩項不限於無牌提供者的行為罪行。',
'O11':'第13A–13E條未有說明，缺跨境VA執法／監管協助的條件與資料保障。',
'O12':'已教非香港DPMS報告責任及期限，未列附表3J要求報告的資料。',
'O13':'RBA只談相稱資源，缺與de-risking的分別及不能因此免除CDD失敗處理的限制。',
'O14':'只泛稱證券代名投資，缺上游市場操縱與利用證券清洗其他罪行得益的區分。',
}
for row in rows:
    n=row['part'];s=row['section'];intro+=f"## {row['id']} · {row['priority']} · {row['title']}\n\n"
    intro+=f"位置：[Part {n} #{s}](../part-{n}.html#{s})。\n\n原有問題：{before[row['id']]}\n\n影響／取捨：{row['impact']}\n\n"
    b=next(b for se in build.PARTS[n]['sections'] if se['id']==s for b in se['blocks'] if b['title']['tc']==row['title'])
    intro+=f"處理：已補入{len(b['points'])}組雙語要點；{'參考層' if b['kind']=='reference' else '主要閱讀層'}。中英文條件、角色、數字、例外已逐點核對。\n\n原文：\n\n"
    for r in row['refs']:
        for lang in ('TC','EN'):
            ed=build.DOCS[r['doc']]['editions'][lang]
            intro+=f"- `{ed['file']}`：{r['locator'][lang.lower()]}。\n"
    intro+='\n結果：已處理；沒有留下待補寫的已確認重要缺口。\n\n'
(HERE/'FINDINGS.md').write_text(intro,encoding='utf-8')

clarification='''# 25%措辭核對及判斷更正

日期：2026-10-19。本輪初見第25份中文「25%以上」及英文「more than 25%」時，
曾把日常中文對「以上」的習慣理解視為可能的邊界衝突，並請擁有人選擇。
擁有人追問法例與海關指引後，直接回查原文，發現這是官方文件持續使用的中英對應，
並非已證實的兩套不同門檻。先前的衝突判斷及待決提問已在對話中撤回；
沒有把擁有人的追問記成批准，也沒有增寫虛構的CONFLICT-CALLS決定。

核對位置：

- `04_高_打擊洗錢及恐怖分子資金籌集條例（第615章）（2026年9月24日綜合版）.pdf`，附表2第1條實益擁有人定義，中文「25%以上」。
- `04_High_AMLO Cap 615 - Consolidated (24 Sep 2026).pdf`，Schedule 2 s.1，英文“more than 25%”。
- `03_高_打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）（2023年6月）.pdf`，第4.4.6、4.4.9段，中文同一表述。
- `03_High_Guideline on AML-CFT for Money Service Operators (Jun 2023).pdf`，¶4.4.6、4.4.9，英文同一表述。
- `25_中選讀_香港洗錢及恐怖分子資金籌集風險評估報告（2022年）.pdf`，第7.24段，印刷126／PDF144頁；已查看原頁圖像。
- `25_Medium-Selected_Hong Kong Money Laundering and Terrorist Financing Risk Assessment Report (2022).pdf`，¶7.24，印刷148／PDF166頁；已查看原頁圖像。

公司註冊處[中文FAQ](https://www.cr.gov.hk/tc/legislation/scr/faq.htm)與
[英文FAQ](https://www.cr.gov.hk/en/legislation/scr/faq.htm)的控制條件亦採同樣對應。
[中文SCR指引](https://www.cr.gov.hk/tc/publications/docs/Guidelines_scr_c.pdf)同樣如此。
這些網頁只作措辭核查，不把2025年加入的經遷冊公司等現行內容混入第25份2022年摘要。
香港電子法例的第622章頁面未成功提供條文內容（轉到client configuration頁）；
不能據此聲稱已核實第622章現行全文。

筆記的清楚寫法：>25%／超過25%。25.1%、25.5%符合比例條件，恰好25%不符合；
不能改寫成≥26%。其他控制條件仍須檢查。SCR與AMLO實益／最終擁有人是不同定義及用途，
不是僅因比例相同便合併兩個制度。正式筆記引用第25份及第03份本身，沒有引入範圍外新規則。
'''
(HERE/'WORDING-25-PERCENT.md').write_text(clarification,encoding='utf-8')

bank=json.loads((ROOT/'web/questions.json').read_text(encoding='utf-8'));quotes=json.loads((ROOT/'docs/quotes.json').read_text(encoding='utf-8'))
ids=[q['id'] for q in bank if any(r['doc'] in ('04','25') for lang in ('tc','en') for r in quotes[q['id']][lang])]
(HERE/'bank-concept-check.json').write_text(json.dumps(dict(method='After source-authored additions, read the Chinese topic stems of the 170 items citing 04/25. Topic-level omission screen only; not a re-audit of every statement, option or answer. No new important topic gap established by this screen.',ids=ids,questions_reviewed=len(ids),bank_sha256=hashlib.sha256((ROOT/'web/questions.json').read_bytes()).hexdigest(),new_source_authored_additions_from_bank=0),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='''# 第04、25份未納入內容：後續審核結論

2026-10-19 · 已完成本輪重要遺漏的補寫、重建及驗證。

這次不以舊筆記引用範圍作篩選邊界。重新檢查第04份其他制度／資料保障／附表，
及第25份法律能力、犯罪模式、銀行與證券、其他行業及公司控制資料，
確認只保留行政摘要、方法及MSO章並不足以支援獨立理解。
已在Part 1、2、5、6、7補入14組、35對雙語要點，七個Part全部重新生成。
目前75個主題、532對要點、18張表及2個示意圖；這些只是規模數字。

## 對復習最重要的改變

- 明確說明處理財產及上游罪行的證明要求，並區分限制／沒收／凍結。
- 區分STR情報、調查、檢控及定罪；補跨境情報與正式法律協助的界線。
- 補完整七類帳戶模式、保險／物業／專業服務／證券例子、RBA與迴避風險。
- 補SCR的用途、五類控制條件、資料／查閱責任及海關指引允許MSO取得資料的方法。
- 補VA客戶資產保障的例外、兩項欺詐罪、境外合作條件及非香港DPMS報告資料。

全部具體問題、實際檔名與定位見[FINDINGS.md](FINDINGS.md)。
按原文範圍逐組說明納入／參考原因見[DISPOSITION.md](DISPOSITION.md)。
[25%用語更正記錄](WORDING-25-PERCENT.md)說明為何使用>25%，不是≥25%或≥26%。

## 取捨與限制

核心概念及能改變適用結論的條件進正文；其他行業專用法律說明置明確的「參考」閱讀層。
歷年統計、個案人物／刑期／金額、機構人手、其他行業費表、報表及變更程序仍在原文。
取捨基於是否幫助理解MSO風險／責任、是否會造成規則誤用及重複程度，沒有推斷官方出題頻率。

第04份依repo的2026-09-24存檔；第25份依2022年報告。未把歷史方案或評級寫成現況。
本輪沒有重做官方考試須知現行版本核查，也沒有聲稱完成第622章現行法例核實。
沒有加入27–47或外部新規則。第25份所指2018年報告的延伸價值另列於取捨記錄。

新增內容的兩語決定性原文已核對含義；其他行政條文群已完成學習用途取捨，
但未逐句雙語翻譯審校每個未採用費表、會計附表、過渡條文及所有歷史統計。
這一限制不代表有已確認的重要補寫仍未執行，也不能保證涵蓋每道未知官方試題。

## 閱讀與可視化

保留B風格、三種語言、離線字體和實際檔名引用。沒有增加裝飾性卡片或複雜判斷流程。
本輪不新增／替換／刪除表圖；七類模式用短段分組，五類控制條件明示擇一，
法律保障把例外緊接規則，行政制度標為參考。18張表及2圖保留原有位置。
代表性預覽見previews目錄；七頁各有中文／英文／雙語及桌面／手機截圖。

## 實際驗證

1. **含義核對**：14組35對新增要點按兩語決定性段落核對角色、AND／OR、數字及例外；不是靠搜尋命中判定正確。
2. **定位及生成**：build檢查原文錨點、引用檔名、離線連結與輸出一致性通過；錨點存在本身不證明完整。
3. **自動檢查**：目錄、正式筆記、題庫來源路徑、active scope及四份歷史audit檢查通過；Python 16項、Node 8項及Go測試通過。
4. **瀏覽器**：7 Part × 3語言 × 2尺寸共42種，語言切換、畫面邊界、離線及頁間連結通過；21種實際練習啟動／返回、6種首頁檢查通過。新增內容另作聚焦截圖及目視檢查，結果見source-additions-display.json。
5. **題庫最後查漏**：自動檢查525個ID／來源路徑；另閱讀引用04／25的170題中文題幹作主題查漏。未發現新的重要主題缺口；這不是每個選項／答案陳述的覆蓋證明，題庫沒有用作正文來源。
6. **保留性**：基線保護的362個檔案雜湊不變，包括原文、題庫、應用及先前證據。baseline.zip／baseline.json保存本輪改前狀態，未改寫舊審核。未推送／公開發佈。

詳見[verification.json](verification.json)、[browser-checks.json](browser-checks.json)、
[integration-checks.json](integration-checks.json)及[bank-concept-check.json](bank-concept-check.json)。
初次本地瀏覽器啟動受沙箱限制；以獲准的本地離線檢查重新執行後成功。
'''
(HERE/'REPORT.md').write_text(report,encoding='utf-8')
print('Wrote current report, 14 findings, disposition and wording clarification; prior evidence unchanged')
