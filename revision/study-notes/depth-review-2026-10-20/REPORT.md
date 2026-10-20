# 七Part學習深度再審核 — 2026-10-20

本輪確實發現了概括過度、具體清單不足、條件及兩語強度不一致；已修正正式內容並重新生成七個Part。新增不是把所有細節同等加長，而是優先補足High原文的定義、清單、責任、邊界和例外。現有75主題、621組雙語要點（基線533，淨增88），11張表及22個圖解（含3棵決策樹）；這些是規模，不是覆蓋率。

[開始閱讀](../index.html) · [實際頁面預覽](preview.html) · [主審32組具體發現](GUIDELINE-REVIEW.md) · [發牌／FAQ獨立覆核](licensing-review.md) · [法例／通函獨立覆核](statutory-review.md)

## 官方要求、選定來源、現有內容三者不同

本輪重新沿[海關發牌頁](https://eservices.customs.gov.hk/MSOS/common/licissus?request_locale=en)的評核須知連結，打開的[官方PDF](https://eservices.customs.gov.hk/MSOS/download/licensing/Guidance_Notes_on_the_Competence_Assessment_for_Money_Service_Operators_en.pdf)仍標December 2022。不是以repo存檔日或網頁更新日證明版本有效；本次未找到較新評核須知，但沒有窮盡核查全站每項補充公告。第03份官方下載仍為June 2023；這不等於已核實第04份為今日最新法例。

第01份兩語原件第5.1–5.3、6.1及第7節已重新閱讀：35題單選、75分鐘、七模組各5題；每模組最多錯2題 **AND** 全卷至少25分。主要出題來源列五類：AMLO、AML/CFT指引、牌照指引、其他海關指引及通函。樣題說明辨認名稱／組合及適用要求的考查方式，不能代表完整範圍，也不能推論考點頻率。

01–26是擁有人選定閱讀範圍；High／Medium是項目閱讀優先級，並非官方權重。筆記以官方模組整理，但同一規則可在一個Part列法定要求、另一Part列履行方法。以下是本輪對照，不沿用舊覆蓋率結論。

| 官方模組 | 01–26內的原文單位 | 正式筆記的核心內容 |
|---|---|---|
| Part 1：AML/CFT及打擊擴散資金籌集常識 | 03第1章／用語表；04附表1；09、19、22–26 | [Part 1](../part-1.html)：ML／TF／PF、三階段、法例分工、FATF、風險報告、CBNI |
| Part 2：AMLO第1至7部 | 04主體法例；05、10–13 | [Part 2](../part-2.html)：刑責、查察／調查、牌照、變更／終止、處分、覆核；其他制度作界線參考 |
| Part 3：AMLO附表 | 04附表1–4及其他附表的選定界線；03履行細節 | [Part 3](../part-3.html)：定義、四CDD、法定例外／高風險、保存、費用、審裁處 |
| Part 4：海關頒布的指引 | 01–02、05–06、10–13、16–17；20–21在Part 5 | [Part 4](../part-4.html)：處所、申請、適當人選、評核、變更、罰款因素、兌換展示 |
| Part 5：機構層面的管治及策略 | 03第2–3章；07、09、14、20–21 | [Part 5](../part-5.html)：風險評估、制度、CO／MLRO、集團、業務計劃／政策 |
| Part 6：AML/CFT管控範疇 | 03第4–6、10–11章及7.10／附錄A；04附表2；06–09、14、18–19、24、26 | [Part 6](../part-6.html)：CDD具體履行、監察、制裁、第三方／渠道、匯款及警號 |
| Part 7：證明符合規定及監察合規水平 | 03第3、7–9章；04附表2；05、15、25選定背景 | [Part 7](../part-7.html)：STR、同意／通風報訊、紀錄、審計、訓練、執法、定期申報 |

所有編號的實際原件檔名列於文末；具體段落／條文與修正位置見三份分工報告及`findings.json`。正式頁面每個內容組亦顯示實際檔名及定位。

## 這次優先修了甚麼

- **Part 1**：ML目的、FATF作用及FI定義語境；2022報告Hawala結算、四級監管優次及非實地監察的具體做法，保留年份及參考層級。
- **Part 2–3**：牌照條件生效取較後時間、續牌待決與例外、牌照必載三類、處分通知五項、第17條獨立罪行／刑罰、第53條發現或知悉起點、五種身分核實來源與代表人四種來源、律師代表權。
- **Part 4**：處所用途與住宅大廈限制、LMO／LPS、申請相片與見證、表6十四項、續牌無效三種情況、拒批／撤吊清單、罰款因素欠列項及考核例外。
- **Part 5**：風險因素與框架、簡化制度三條件、CO四職能／MLRO三職能／八項支援條件、因素上升後必須重新評估而非自動最高風險；政策提交資料。
- **Part 6**：低風險因素及五類簡化方法、18種潛在高風險因素及六類可能EDD措施、PPTA四／五項資料、香港PEP類別、身份文件、SOW／中介／核證界線；第三方付款八警號與政策五內容；六組43警號；電傳角色／強度；貿易指標兩處實質誤述。
- **Part 7**：五類訓練內容及五組人員、真誠不報的條件、JFIU確認與同意分別、業務通信最低內容、限制令動作、內報／保存／審計的must／should及既定兩語差異。

**第26份新差異已按擁有人決定落實**：中文「已足以」及英文「may constitute」並列，不擅自統一。新決定另記於CONFLICT-CALLS；原有所有決定保留，透過新的維護記錄證明前後內容，而不是修改歷史雜湊。

## 學習層次及沒有無差別擴寫的理由

1. **應記住**：定義／縮寫名稱、四CDD、法定來源清單、門檻比較符號、相連交易、起算事件、誰批准／誰報告、AND／OR及例外；角色和提交資料的完整分類。
2. **應理解**：機構／客戶風險如何連接CDD程度、SDD與BO豁除不同、控制權不限持股、SOW／SOF、中介協助不轉移責任、STR與同意／抗辯不同。
3. **要能認識的例子**：43警號、第三方八警號及TBML具體模式。保留足夠細節辨識，但非全部必做、非封閉清單、非單一警號自動證明犯罪。
4. **參考**：聯絡資料、舊年檢查／活動統計、部門合作次數、表格外觀及網站登入步驟。其存在與取捨已記錄，不因沒有筆記引用便排除；凡改變適用判斷的條件仍留正文。

## 已讀、已核對、未全面重讀

| 原文 | 本輪實際範圍與邊界 |
|---|---|
| 01、02、05、06 | 兩語全文；05費用／附件表另看六頁原件圖像；全部FAQ分類對照，見licensing-review |
| 03 | 英文第1–11章、附錄A／用語表；中文新改動及相關條件段落直接核對。不是全份兩語逐字翻譯審校 |
| 04 | 第1–53條MSO主體制度及附表2主要單位以英文重新閱讀，新增／關鍵條文與中文比對；第17–19及53條已補讀完整兩語。其他行業全套制度、所有附表及全部TC未逐條重新審讀，詳statutory-review |
| 07–14、16–19、22、26 | 兩語全文；17為同一雙語原件；26另看PDF第2–3頁。名單／歷史結論不宣稱現行 |
| 15 | 正文及附件提取／轉錄文字；未重新對全部附件圖片欄位逐格視覺核實 |
| 20、21 | 主審補完兩語全文，填補分工報告當時的未讀範圍；17／19項逐組對照 |
| 23 | 第1–7條及第8條部分等核心CBNI範圍；後續程序未全面重讀 |
| 24 | 英文六頁及腳註；沒有官方中文，中文為學習譯文 |
| 25 | 摘要／方法及MSO章兩語；EN 7.8–7.45、8.1–8.36、9.1–9.46再作遺漏判斷；TC新增相關段落核對。其他行業全部統計、EN7.1–7.7、TC第7–9章全篇及全部附錄未重新通讀 |

因此，本輪完成的是七Part的**核心學習深度及已列明原文單位的再審核和修正**，不是每份大型法例／報告每一頁的全量雙語審校；不能據此保證已窮盡01–26或所有未知官方試題。上述未全面重讀範圍仍是驗證邊界，不能把「現在有引用」等同已完成新一輪含義核對。

第25份沒有只因不是MSO章就排除：公司／信託透明度、TF／NPO、PF範圍及跨行業機制已檢視並對照現稿；本輪另補Hawala及監管矩陣。其他行業歷史數量不提升為每日必背；已存在的跨行業案例不據舊報告判定正確。

## 01–26以外：另列，不混入正式筆記

官方第6.1段涵蓋海關其他指引／通函，故只看01–26筆記不等於覆蓋官方全部可能來源。下列優先級是建議，不能稱為必考：

| 範圍外原件與定位 | 與現有材料的差距／建議優先級 | 是否影響只看筆記 |
|---|---|---|
| `41_歷史參考_通函_機構層面的洗錢及恐怖分子資金籌集風險評估（2018年8月13日）.pdf` 全文 | 本輪讀存檔全文；四組因素及五項程序在03第2章／Part 5已有較後完整對應。補充閱讀中，未發現須新增一套規則 | 核心概念已有；不把未選通函當不存在 |
| `42_歷史參考_通函_與金錢服務經營者有關的欺詐網站及社交媒體平台（2025年4月24日）.pdf` 第1頁 | 存檔全文明示資料保安、仿冒警覺、疑似冒用業務身分時建議通知公眾及向海關／警方報案。建議中優先級；[官方連結](https://eservices.customs.gov.hk/MSOS/downloadFile?id=452990)本次工具未能開啟，不能聲稱線上版本已比對 | 此具體防冒用回應未加入01–26正式內容，是已識別的範圍差距 |
| `43_歷史參考_通函_提交旅客資料電子表格（現金類物品）（2025年6月23日）.pdf` 第1頁；44用戶手冊 | 已讀存檔並開啟[官方43 PDF](https://eservices.customs.gov.hk/MSOS/downloadFile?id=459116)：預填、取得QR、現場出示完成申報。低至中優先級的操作補充，沒有改寫12萬法定界線 | 現有CBNI原則仍可學；不包含這項較後操作途徑 |
| 28–29、31、34–40及45–47 | 主要是延伸指引、培訓、決議或諮詢材料；本輪未對各全文重新完成知識差距盤點。31版本、45–47諮詢文件不能自動當香港現行義務；39／40可作日後補充理解 | 不宣稱無缺口；沒有把這些內容混入正文／題庫 |

## 最後題庫查漏的實際深度

在原文優先修正後才讀題庫作概念提示：Part 1／5／6共240題的題幹與來源；Part 2／3共140題題幹，其中20題再看陳述；Part 4／7共145題題幹與704條中文陳述。合計525題入口，不是525題所有選項／答案的重新語義覆審。所有疑似缺口均回原文確認後寫入，未從題幹／答案解釋複製正文。

查漏實際促成FI定義語境、牌照必載資料、通知清單、真誠不報、JFIU回應、業務通信、限制令動作、政策資料及2022監管描述等補充。見`bank-gap-parts1-5-6.md`、`bank-gap-parts2-3.md/json`、`bank-gap-parts4-7.md`。最後一份列出的BG47-01至07及跨Part指引已由主審全部合入，不停留在代理建議稿。

`bank-source-routes.json`只證明525 ID可找到來源路徑，不能證明知識完整。

## 視覺、驗證及證據

保留既有B風格、11表／22圖；本輪沒有為加圖而把清單改成複雜流程。Visual Explainer的條件緊貼規則原則用於同步處所比較、角色職責及報告圖的內容。決策樹繼續只處理適合分支的CDD等問題；完整清單放正文，圖不冒充全部條件。

已實際執行42個頁面案例（7Part×3語言×2視窗）、21個練習入口案例及6個首頁案例，並查看七Part代表截圖；所有語言切換、排版溢出、離線外部請求及練習返回檢查通過。後續圖中文字修正另重跑受影響頁面，見最終驗證記錄。自動驗證、文字定位、人工含義核對及限定範圍覆核是四種不同證據。

項目檢查輸出在`automatic-checks-initial.json`及`automatic-checks-final.json`。初跑四項歷史檢查因新增26決定使CONFLICT-CALLS變動而失敗；已依現有維護機制新增一份前後證據記錄，原有記錄／雜湊不動，再重跑。未弱化測試條件。原件、題庫、答案、ID、評分程式及歷史證據的保留驗證見`final-state.json`。本輪未推送或發布。

## 原文檔名索引

- 01：`01_High_Guidance Notes on the Competence Assessment (Dec 2022).pdf`<br>`01_高_能力評核須知（2022年12月）.pdf`
- 02：`02_High_Competence Assessment - Sample Questions (12 May 2021).pdf`<br>`02_高_金錢服務經營者適用的能力評核_參考試題（2021年5月12日）.pdf`
- 03：`03_High_Guideline on AML-CFT for Money Service Operators (Jun 2023).pdf`<br>`03_高_打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）（2023年6月）.pdf`
- 04：`04_High_AMLO Cap 615 - Consolidated (24 Sep 2026).pdf`<br>`04_高_打擊洗錢及恐怖分子資金籌集條例（第615章）（2026年9月24日綜合版）.pdf`
- 05：`05_High_Licensing Guide (May 2026).pdf`<br>`05_高_牌照指引（2026年5月）.pdf`
- 06：`06_High_FAQ applicable to all MSOs (C&ED portal).md`<br>`06_高_適用於所有金錢服務經營者的常見問題（海關網站）.md`
- 07：`07_High_Circular - Supervisory Findings on Customer Due Diligence (22 Nov 2023).pdf`<br>`07_高_通函_客戶盡職審查相關監管工作中的發現（2023年11月22日）.pdf`
- 08：`08_High_Circular - ML-TF Risks of Third Party Payments (17 Sep 2024).pdf`<br>`08_高_通函_第三方支付涉及的洗錢及恐怖分子資金籌集風險（2024年9月17日）.pdf`
- 09：`09_High_Circular - Identification and Mitigation of Proliferation Financing Risks (22 Dec 2021).pdf`<br>`09_高_通函_識別和緩解大殺傷力武器擴散融資風險（2021年12月22日）.pdf`
- 10：`10_Medium-Essential_Guideline on Criteria for Determining Fitness and Propriety (Apr 2018).pdf`<br>`10_中重點_有關適當人選準則的指引（2018年4月）.pdf`
- 11：`11_Medium-Essential_Supplementary Guideline on Fitness and Propriety (Jan 2020).pdf`<br>`11_中重點_有關適當人選準則的補充指引（2020年1月）.pdf`
- 12：`12_Medium-Essential_Disciplinary Action Guideline on Pecuniary Penalty (Apr 2018).pdf`<br>`12_中重點_施加罰款紀律行動指引（2018年4月）.pdf`
- 13：`13_Medium-Essential_Disciplinary Fining Guideline (May 2018).pdf`<br>`13_中重點_紀律處分罰款指引（2018年5月）.pdf`
- 14：`14_Medium-Essential_Circular - ML-TF Risks of Delivery Channels (13 Dec 2021).pdf`<br>`14_中重點_通函_與交付渠道有關的洗錢及恐怖分子資金籌集風險（2021年12月13日）.pdf`
- 15：`15_Medium-Essential_Circular - E-submission of the Periodic Return (30 May 2025).pdf`<br>`15_中重點_通函_經金錢服務經營者牌照系統提交電子版交易報告定期申報表（2025年5月30日）.pdf`
- 16：`16_Medium-Essential_Circular - Amendments to the Money Changers Ordinance Cap 34 (17 Nov 2025).pdf`<br>`16_中重點_通函_貨幣兌換商條例第34章之修訂（2025年11月17日）.pdf`
- 17：`17_Medium-Essential_Full Money Changers Ordinance, Cap. 34 (2025-08-24, Bilingual).pdf`<br>`17_中重點_貨幣兌換商條例全文（第34章） (2025-08-24, Bilingual).pdf`
- 18：`18_Medium-Essential_Circular - Trade-based Money Laundering Guidance (20 Jan 2026).pdf`<br>`18_中重點_通函_打擊以貿易進行洗錢活動指引（2026年1月20日）.pdf`
- 19：`19_Medium-Essential_Circular - Statements issued by the FATF (3 Jul 2026).pdf`<br>`19_中重點_通函_財務行動特別組織的聲明（2026年7月3日）.pdf`
- 20：`20_Medium-Selected_Guidelines for Submission of Business Plan (Ver 12-2019).pdf`<br>`20_中選讀_遞交業務計劃的指引（12-2019版）.pdf`
- 21：`21_Medium-Selected_Guidelines for Submission of AML-CFT Policy (Ver 12-2019).pdf`<br>`21_中選讀_遞交打擊洗錢及恐怖分子資金籌集政策的指引（12-2019版）.pdf`
- 22：`22_Medium-Selected_Circular - Cross-boundary Movement of Currency Ordinance Cap 629 (31 Jul 2018).pdf`<br>`22_中選讀_通函_實體貨幣及不記名可轉讓票據跨境流動條例（2018年7月31日）.pdf`
- 23：`23_Medium-Selected_Full Cross-boundary Movement of Physical Currency and Bearer Negotiable Instruments Ordinance, Cap. 629 (2026-07-31, Bilingual).pdf`<br>`23_中選讀_實體貨幣及不記名可轉讓票據跨境流動條例全文（第629章） (2026-07-31, Bilingual).pdf`
- 24：`24_Medium-Selected_Trade-Based Money Laundering Risk Indicators - FATF and Egmont (Mar 2021).pdf`<br>`24_中選讀_貿易洗錢風險指標（2021年3月_英文原文）.pdf`
- 25：`25_Medium-Selected_Hong Kong Money Laundering and Terrorist Financing Risk Assessment Report (2022).pdf`<br>`25_中選讀_香港洗錢及恐怖分子資金籌集風險評估報告（2022年）.pdf`
- 26：`26_Medium-Selected_Circular - United Nations Sanctions - Principles and Early Alerts (7 Feb 2018).pdf`<br>`26_中選讀_通函_聯合國制裁_原則及預警機制（2018年2月7日）.pdf`
