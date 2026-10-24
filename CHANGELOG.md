# Release notes / 版本更新

## Unreleased

- Removes the branches of the Go tests that were written for the old question bank and no longer run: every item carries a note per statement and may be reordered, and `TestBankIntegrity` rejects anything else, so `TestComboExplanationNamesFalseStatements`, the single-quote form of `docs/quotes.json` and the fixed-item and unannotated-item paths in six other tests never executed. The guard itself stays; `sameSet` becomes the standard library's `slices.Equal`. 120 lines fewer. The 588 questions, answers, scoring, generated pages and source editions are unchanged.
- Simplifies the notes builder (`revision/study-notes/build.py`, `model.py`, `gap_check.py`) without changing the seven parts: one cached reader for the source texts (the build is several times faster), one edition lookup and one original-document link shared by citations, ruling records and the validator, one language-span helper, one title-prefix stripper, and one table renderer shared by the figures and the Numbers page; the unused grouped-table branch, the `g()` helper and three repeated `manifest()` calls go. The seven part pages, `coverage.json` and `bank-source-routes.json` are byte-identical; `amounts.html` now closes every table cell with `</td>`, which browsers already did, so its DOM and rendering are unchanged (checked with Playwright in all three reading languages). 17 lines fewer.
- Simplifies the audit chain (`bank/audit/state.py`, `active_scope.py` and the four report scripts) without changing any report: one newline-variant function behind the hash checks, one evidence-snapshot check instead of five copies, one verifier for `documentation_updates` instead of four loops, one `norm` and one Markdown `table` function instead of two of each, one `emit` function for writing or checking a generated report (it now writes LF on every platform, which is what Git stores), and one `check_reviews` function shared by the active-scope record and its follow-ups; the unused `sha()` helper and unused imports go. `coverage.json`, every generated audit report and the mutation tests are unchanged. 47 lines fewer.
- 刪除Go測試中為舊題庫而寫、已不再執行的分支：每題都有逐句註解並可重排，`TestBankIntegrity`亦不接受其他形式，因此`TestComboExplanationNamesFalseStatements`、`docs/quotes.json`的單引文形式及另外六個測試中的固定次序與無註解分支從未運行。守衛本身保留；`sameSet`改用標準庫的`slices.Equal`。少120行。588道題、答案、評分、生成頁面及來源版次均不變。
- 精簡筆記生成器（`revision/study-notes/build.py`、`model.py`、`gap_check.py`），七個部分的內容不變：來源文本改為一次讀取並快取（生成快數倍），引文、裁決記錄及校驗共用同一個版本查找及原件連結函數，語言span、標題層次前綴及表格各只保留一個寫法，圖表與數字總表共用同一個表格渲染；移除無圖表使用的分組表格分支、未調用的`g()`及三次重複的`manifest()`調用。七個部分頁面、`coverage.json`及`bank-source-routes.json`字節一致；`amounts.html`的每個表格單元格現在都有`</td>`結束標籤（瀏覽器本來就會自動補上），DOM與顯示不變（以Playwright在三種閱讀語言下核對）。少17行。
- 精簡審計鏈（`bank/audit/state.py`、`active_scope.py`及四個報告腳本），報告內容不變：雜湊檢查共用一個換行變體函數，五處題句快照斷言合為一個，四處`documentation_updates`迴圈合為一個校驗函數，`norm`與Markdown表格各只保留一份，生成報告的寫入或`--check`比對合為一個`emit`函數（在任何平台都以LF寫出，即Git儲存的形式），現行範圍記錄及其後續記錄共用一個`check_reviews`函數；移除未使用的`sha()`及未使用的import。`coverage.json`、全部生成的審計報告及變異測試均不變。少47行。

## v1.13.0 — 23 October 2026

- Study notes: the toolbar gains a study-tier filter (All; Remember + Understand; Remember only) and a **Ruling marks** switch; the 131 purple ruling numbers and the per-part rulings register are hidden until switched on. A new **Numbers** page (`amounts.html`) lists 70 amounts, shares, periods, fees and penalties in seven groups, each with its starting point or condition, a link to the notes section and the cited passage.
- Figures grow from 34 to 79: 35 list cards that show the number of items in a source list (the four CDD measures, the three STR-system components, the six screening parties, the fourteen Form 6 changes, the nine revocation examples, the section 25 exemptions, the PPTA items and more), four new comparison tables (the six main laws, who does what, SDD versus EDD, wire transfers versus non-wire remittances) and a sanctions-actors table, the renewal line (90, 45, 7 and 30 days), the new-licence route, the CDD route, the STR route from discovery to after disclosure (replacing the former internal-reporting figure), beneficial-owner shareholding examples and the periodic-return clocks. Point text is unchanged.
- Practice app: a **Wrong-answer book** keeps every question answered wrong, in practice or in a mock, until it is answered right twice in a row, with a button to practise it; custom practice draws unseen questions before seen ones and the home page shows how many remain. The stylesheet is one layer instead of a base plus overrides, with no visual change (verified by computed-style comparison).
- Adds 36 independently blind-reviewed questions (588 in total: 68 / 81 / 71 / 89 / 84 / 123 / 72) whose false statements change one number, period, name or actor in an otherwise faithful sentence: the 14-year / $5 million and 3-month / $50,000 penalties, the six main laws' exact names, the Cap. 629 detention periods and the HK$120,000 line, the 2-year licence and 45-day renewal, the 7-day licence return, $1,000,000 against $10,000,000 and $10,000 against $100,000 a day, the 21-day review window, the $120,000 / $8,000 CDD lines, the Schedule 2 product and intermediary rules, the renewal, result and nomination timelines, Cap. 34's 12 months and 3 days, the 102x152 mm photographs, the two penalty guidelines, the two-year institutional review, the 3-business-day originator rule, annual bearer-share declarations, 1 April 2012, the six screening parties, the four identification items, the remittance record items, the JFIU's quarterly report, the STR registers, 3-year training records and the audit function. m5-08 no longer mirrors a statement in m5-103 and m3-324 has its own stem; answers are unchanged.
- Scoring and source editions are unchanged. README previews were captured again from v1.13.0.
- 筆記：工具列新增學習層次篩選（全部／必記＋理解／只看必記）及「裁決標記」開關，131處紫色裁決編號及各部分的裁決登記冊預設隱藏，按下才顯示。新增**數字總表**（`amounts.html`），分七組集中70項金額、比例、期限、費用及刑罰，每行寫明起算點或條件，並連到筆記小節及所引原文。
- 圖表由34個增至79個：35張標明項數的清單卡（四項CDD措施、可疑交易報告制度三項組成、篩查六組相關方、表格6的十四項變更、九類撤牌例子、第25條豁免、PPTA資料等）、四張新對照表（六條主要法例、誰做甚麼、簡化與加強、電傳與非電傳匯款）及制裁角色表、續牌主線（90、45、7、30日）、新牌申請流程、CDD流程、由發現到披露之後的可疑交易報告流程（取代原內部報告圖）、實益擁有人持股例子及定期申報期限。要點文字不變。
- 練習App：新增**錯題本**，練習或模擬試答錯的題目會保留至連續答對兩次，並可一鍵練習；自選練習先抽未做過的題目，首頁顯示尚餘多少題。樣式表合併為一層，視覺不變（以計算樣式逐項比對核實）。
- 新增36道經獨立盲審的題目（合共588題：68／81／71／89／84／123／72），錯誤陳述都只改動原文句子中的一個數字、期限、名稱或主體：監禁14年及罰款五百萬元與監禁3個月及罰款50,000元、六條主要法例的準確名稱、第629章的扣留期限及港幣120,000元界線、2年牌照及45日續期、7日交回牌照、$1,000,000與$10,000,000及每日$10,000與$100,000、21日覆核期限、$120,000及$8,000盡職審查門檻、附表2的產品及中介人規定、續牌、成績及提名時限、第34章的12個月及3天、102x152毫米照片、兩份罰款指引、每兩年的機構風險評估、3個營業日的匯款人資料規定、每年的持票人股份聲明、2012年4月1日、六組篩查相關方、四項識別資料、匯款紀錄項目、財富情報組季度報告、可疑交易報告紀錄冊、3年培訓紀錄及審核職能。m5-08不再與m5-103互為鏡像，m3-324有自己的題幹；答案不變。
- 評分及來源版次均不變。README預覽從v1.13.0重新截取。

**Download / 下載：** `mso-study-bundle.zip` contains the notes, practice and originals 01–26; extract the entire ZIP and open `index.html`.
完整學習包包含筆記、練習及01–26原件；完整解壓後開啟 `index.html`。

[Download / 下載](https://github.com/leohwlee/mso-ca/releases/tag/v1.13.0)

## v1.12.1 — 23 October 2026

- Corrects the three study-note points that v1.12.0 flagged as not matching the owner's rulings, and removes their amber "Check" notes:
  - Part 3 fees (B6): HK$945 is payable for each person subject to the fit-and-proper test, at grant and again at every renewal. The point no longer calls it a one-off fee, and now also cites Schedule 3 items 4–5.
  - Part 4 fitness (B13): the CCE must also have regard to any other matter it considers relevant. The Chinese no longer says 可 (may).
  - Part 6 simplified CDD (E23): simplified measures stop on doubts about the veracity or adequacy of identification or verification information. The Chinese now includes 充分 (adequacy), and the point also cites Schedule 2 s.3(1)(e).
- The 131 ruling marks and 93 rulings, the 552 questions, answers, scoring and source editions are unchanged. README previews were captured again from v1.12.1.
- 修正v1.12.0標出與擁有人裁決不一致的三個筆記要點，並移除相應的琥珀色「核對」提示：
  - 第3部分費用（B6）：每名受適當人選測試的人士須繳HK$945，批牌及每次續牌均須繳付，不再寫作一次性；另補引附表3第4–5項。
  - 第4部分適當人選（B13）：關長亦須考慮其認為有關的任何其他事宜，中文不再寫「可」。
  - 第6部分簡化盡職審查（E23）：對識別／核實資料的真實性或充分性有疑問，即停止簡化；中文補上「充分」，另補引附表2第3(1)(e)條。
- 131處裁決標記及93項裁決、552道題、答案、評分及來源版次均不變。README預覽從v1.12.1重新截取。

**Download / 下載：** `mso-study-bundle.zip` contains the notes, practice and originals 01–26; extract the entire ZIP and open `index.html`.
完整學習包包含筆記、練習及01–26原件；完整解壓後開啟 `index.html`。

[Download / 下載](https://github.com/leohwlee/mso-ca/releases/tag/v1.12.1)

## v1.12.0 — 23 October 2026

- Marks every place where the seven-part notes apply a source-conflict ruling: 131 purple numbers (118 points and 13 figures) across 93 rulings. The numbers are the owner decisions in `revision/CONFLICT-CALLS.md` (B, W, E, N and the 20 October decision D26). A dashed number means each language keeps its own wording; U1–U4 mark four language differences the text handles that are not yet in CONFLICT-CALLS.
- Each part ends with "Rulings in this part": the question, the decision, every place it is used, links to other parts and the recorded entry, whose document numbers open the cited originals. Exam-trap numbers link there too.
- Three amber "Check" notes flag points that may not match the ruling they apply (B6 in Part 3, B13 in Part 4, E23 in Part 6). Note text, the 552 questions, answers, scoring and source editions are unchanged.
- README previews were captured again from v1.12.0; the Part 6 example now shows ruling numbers. Releases publish only `mso-study-bundle.zip`, which contains the practice app, the seven-part notes and the cited originals 01–26. The standalone `mso-ca.html` was removed from the v1.11.0 release, and the READMEs and user guides link only to the bundle.
- 七部分筆記中每個套用來源矛盾裁決的地方，現都標上紫色編號：共131處（118個要點及13個圖表），涉及93項裁決。編號即`revision/CONFLICT-CALLS.md`中的擁有人裁決（B、W、E、N及10月20日的D26）；虛線編號表示兩語各按本身語文，U1–U4標示正文已處理、但尚未列入CONFLICT-CALLS的四項兩語差異。
- 每部分末設「本部分的裁決」，列出問題、裁決、所有出現位置、其他部分連結及裁決記錄原文；記錄中的文件編號可開啟所引原件。易錯提示的編號亦連到該處。
- 三項琥珀色「核對」提示標出可能與所套用裁決不一致的要點（第3部分B6、第4部分B13、第6部分E23）。筆記文字、552道題、答案、評分及來源版次均不變。
- README預覽從v1.12.0重新截取，第6部分示例可見裁決編號。發佈版只提供 `mso-study-bundle.zip`，內含練習App、七部分筆記及引用的01–26原件；v1.11.0已移除單獨的 `mso-ca.html`，README及使用指南只連結學習包。

**Download / 下載：** `mso-study-bundle.zip` contains the notes, practice and originals 01–26; extract the entire ZIP and open `index.html`.
完整學習包包含筆記、練習及01–26原件；完整解壓後開啟 `index.html`。

[Download / 下載](https://github.com/leohwlee/mso-ca/releases/tag/v1.12.0)

## v1.11.0 — 23 October 2026

- Adds exam-focus study aids to the seven-part notes: six source lists are completed, including the three components of the STR reporting system; every block carries a study tier (Remember, Understand, Recognise, Reference); 69 amber exam traps restate the owner's source-conflict decisions; new figures show similar thresholds, deadline tracks and identity data. The notes have 75 topics, 626 bilingual point pairs, 9 tables and 25 diagrams. Counts are not coverage percentages.
- Adds 27 independently reviewed questions (552 in total: 63 / 75 / 66 / 83 / 81 / 116 / 68). They cover the Guideline's potentially higher and lower risk factor lists, minimum identification data for individuals and trusts, layered beneficial and ultimate ownership, failure to complete CDD, wire transfers below $8,000, the STR system elements, the extent of EDD for PEPs, and near-identical names of the JFIU and of the main ordinances. Ten questions have no true statement, so "None of the above" is now sometimes the answer; five of them test the renewal timeline, the fit and proper criteria, staff training records, delivery-channel risks, and how Hong Kong implements UN sanctions and counter-proliferation financing.
- Corrects 12 existing questions without changing any answer: removes added inferences and clauses missing from the other language, restores a dropped qualifier, says when a rule comes from the Licensing Guide or differs between the Ordinance and the Guideline, replaces two statements that depended on one FATF plenary's list changes, and replaces one hair-splitting distractor.
- Rebuilds the offline study bundle and practice app. Source editions and the selected scope 01–26 are unchanged; saved scores for the 12 corrected questions keep their meaning.
- 七部分筆記加入應試重點：補全六份原文清單，包括可疑交易報告制度的三項組成；每個內容組標上學習層次（必記、理解、認識、參考）；以琥珀色列出69項易錯提示，取自擁有人的來源裁決；新增圖表顯示相近金額、期限及身分資料。筆記現有75主題、626組雙語要點、9張表及25個圖解；數量不是覆蓋率。
- 新增27道已獨立盲審的題目（合共552題：63／75／66／83／81／116／68），涵蓋指引的潛在較高及較低風險因素清單、自然人及信託的最低限度識別資料、多層持股的實益擁有人及最終擁有人、未能完成盡職審查的後果、8,000元以下電傳轉帳須附隨的資料、可疑交易報告制度的元素、對政治人物採取更嚴格盡職審查的程度，以及財富情報組和主要條例的近似名稱。其中10題沒有正確陳述，「以上皆非」不再永遠是錯誤選項；當中5題考核續牌時限、適當人選準則、培訓紀錄、交付渠道風險，以及香港如何執行聯合國制裁及打擊擴散融資。
- 修正12道現有題目，答案不變：刪去原文沒有的推論及只在一種語言出現的子句、補回遺漏的限定詞、註明規則出自《牌照指引》或條例與指引的分別、替換兩項只取決於某次特別組織全體會議名單變動的陳述，以及替換一個過於瑣碎的干擾項。
- 重新打包離線學習包及練習頁面；來源版次及01–26選定範圍不變，12道修正題目的已存成績仍代表相同選項。

**Download / 下載：** `mso-study-bundle.zip` contains the notes, practice and originals 01–26; extract the entire ZIP and open `index.html`.
完整學習包包含筆記、練習及01–26原件；完整解壓後開啟 `index.html`。

[Download / 下載](https://github.com/leohwlee/mso-ca/releases/tag/v1.11.0)

## v1.10.2 — 20 October 2026

- Uses natural Chinese section wording throughout current study notes, navigation, practice buttons and bundle instructions; English text remains in English.
- Rebuilds the offline study bundle and practice app. The 525 questions, answers, grading and source editions are unchanged.
- 現行中文筆記、章節導覽、練習按鈕及學習包說明統一使用「部分」，例如「閱讀七個部分」「第1部分」「每個部分」，避免中英混寫。
- 重新打包離線學習包及練習頁面；525道題、答案、評分及來源版次不變。

**Downloads / 下載：** `mso-study-bundle.zip` for notes, practice and originals 01–26; extract the entire ZIP and open `index.html`. `mso-ca.html` for standalone practice.
完整學習包包含筆記、練習及01–26原件；完整解壓後開啟 `index.html`。單獨練習可下載 `mso-ca.html`。

[Download / 下載](https://github.com/leohwlee/mso-ca/releases/tag/v1.10.2)

## v1.10.1 — 20 October 2026

- Expands the seven-part notes from 533 to 621 bilingual point pairs across 75 topics, prioritising High-source definitions, complete lists, conditions and exceptions. These are size counts, not official-syllabus coverage.
- Reviews all 33 visuals. CDD triggers are shown as potentially overlapping cases; two suitable decision trees remain. Clarifies nested AND/OR conditions, deadlines, training-record guidance and the disciplinary-penalty ceiling.
- Improves narrow-screen and bilingual reading, table headings and anchor positioning. All seven Parts were checked in three language modes at five widths (105 page cases).
- Retains the approved Chinese/English wording difference in source 26 and the separate content and visual audit records. Archived source editions and selected scope 01–26 are unchanged.
- Refreshes all repository README entry points and the bundled instructions. The 525 questions, IDs, answers and grading are unchanged.
- 七部分筆記由533增至621組雙語要點，涵蓋75個主題；優先補足高優先級原文的定義、完整清單、條件及例外。數量不是官方考綱覆蓋率。
- 逐項覆核33個圖表；CDD觸發改為可並存情況圖，保留兩棵適用的決策樹，並釐清內層AND／OR、期限、培訓紀錄指引及紀律罰款上限。
- 改善窄屏、雙語、表頭及跳轉位置；七個部分均經三種語言、五種寬度實測，共105組頁面檢查。
- 保留第26份已批准的中英文措辭差異，以及獨立的內容／視覺審核記錄。原件版次及01–26選定範圍未變。
- 同步更新倉庫所有README入口及學習包說明；525題的ID、題目、答案及評分不變。

**Downloads / 下載：** `mso-study-bundle.zip` contains the updated notes, practice and originals 01–26; extract the entire ZIP and open `index.html`. `mso-ca.html` provides standalone practice.
完整學習包含新版筆記、練習及01–26原件；完整解壓後開啟`index.html`，單獨練習可下載`mso-ca.html`。

Review boundaries: [content](revision/study-notes/depth-review-2026-10-20/REPORT.md), [visuals and previews](revision/study-notes/visual-refinement-2026-10-20/REPORT.md).
No claim is made to cover every unknown official exam question or to have reverified all current law.

[Download / 下載](https://github.com/leohwlee/mso-ca/releases/tag/v1.10.1)

## v1.10.0 — 19 October 2026

- Adds a complete offline study bundle: seven-part notes, the practice app and cited originals 01–26. Extract `mso-study-bundle.zip` and open `index.html`; `mso-ca.html` remains available for standalone practice.
- Adds source-authored Traditional Chinese, English and bilingual notes, with 75 topics and 533 point pairs. These counts are not claims of full official-syllabus coverage.
- Applies the blue-gray reading design, 33 comparisons/diagrams and three selected decision trees. Conditions, exceptions, dates and actual source filenames remain visible.
- Preserves 525 question IDs, answers and grading. Source audits and review history are retained, including the separately downloadable large baseline archive.
- 新增完整離線學習包：七部分筆記、練習App及引用的01–26原件。下載並完整解壓 `mso-study-bundle.zip`，開啟 `index.html`；單獨練習仍可下載 `mso-ca.html`。
- 筆記從原文整理，提供繁體中文、英文及雙語，共75個主題、533組雙語要點；數量不代表官方考綱完整覆蓋。
- 採用藍灰閱讀設計、33個對照／圖解及3棵經選擇的決策樹，保留條件、例外、日期及實際原件檔名。
- 保持525題的ID、答案及評分；保留來源審核證據，大型基線存檔另附下載。

[Download / 下載](https://github.com/leohwlee/mso-ca/releases/tag/v1.10.0)

## v1.9.1 — 18 October 2026

[Download / 下載 mso-ca.html](https://github.com/leohwlee/mso-ca/releases/download/v1.9.1/mso-ca.html)

- Removes the discontinued revision-pack generator and review tools from the active tree and future release builds; exact originals remain in a verified archive.
- Consolidates source extraction into one command and shortens the authoring/development guides; keeps the Go builder and four quality-check files.
- App behaviour, 525 questions, source documents and review verdicts are unchanged.
- 舊溫習資料程式及覆核工具退出日常維護與後續發佈，完整原檔保存在可核驗存檔。
- 合併來源擷取入口、精簡出題及開發指南，保留仍有用途的 Go 打包工具及四份檢查。
- App 操作、525題、來源原件及覆核結論不變。

## v1.9.0 — 18 October 2026

Download **[mso-ca.html](https://github.com/leohwlee/mso-ca/releases/download/v1.9.0/mso-ca.html)** and open it in a browser.
使用時下載 **mso-ca.html**，再用瀏覽器開啟。

### English

- Restricts the active bank to documents **01–26** in the reorganised reading library.
- Expands to **525 bilingual combination questions** across seven parts: 60 / 75 / 65 / 80 / 80 / 100 / 65. Retains 354 questions, retires three outside the selected scope and adds 171 independently reviewed questions.
- Keeps two modes: **Mock exam** and **Custom practice**, with one or multiple parts selectable. Mock papers remain 35 questions, five per part, with 75 minutes.
- Adds source-grounded distractors and application scenarios, with explanations for every statement. Document 24's Chinese material is labelled a study translation; 2022 report findings remain dated.
- Unfinished papers containing retired questions restart as full valid papers.
- Replaces obsolete agent-specific configuration with ordinary Markdown authoring instructions. Reorganises English and Chinese documentation around downloading, study, maintenance and release.
- Adds app behaviour and source-boundary tests, current-scope review evidence and checks that preserve earlier audit history.

### 繁體中文

- 現行題庫只限重新整理的閱讀文檔庫 **01–26**。
- 擴充至 **525道中英雙語組合題**，七部分分別為60／75／65／80／80／100／65題。保留354題，移除3道範圍外題目，新增171道已獨立覆核題目。
- 只保留**模擬試**及**自選練習**，可選一個或多個部分。模擬試維持35題、每部分5題、75分鐘。
- 新增有原文依據的干擾項及應用情境，每項陳述均有解析。第24份的中文內容標為學習譯文；2022年報告結論保留年份。
- 包含退役題目的未完成試卷須重新開始。
- 移除過時的代理專用配置，改用通用Markdown編寫規範；重新整理中英文下載、溫習、維護及發佈說明。
- 新增功能及來源邊界測試、現行範圍覆核證據，同時保留舊審核的可核驗歷史。

### Release files / 發佈檔案

- **mso-ca.html** — current 525-question offline app / 現行525題離線App。
- **mso-revision-pack.html** — legacy reference pack with an older source scope; not a third app mode or a complete guide to the current bank / 採用較舊來源範圍的歷史溫習資料，並非第三個模式或現行題庫的完整指南。

[Earlier releases / 較早版本](https://github.com/leohwlee/mso-ca/releases)
