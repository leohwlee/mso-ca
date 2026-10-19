# Release notes / 版本更新

## v1.10.0 — 19 October 2026

- Adds a complete offline study bundle: seven-part notes, the practice app and cited originals 01–26. Extract `mso-study-bundle.zip` and open `index.html`; `mso-ca.html` remains available for standalone practice.
- Adds source-authored Traditional Chinese, English and bilingual notes, with 75 topics and 533 point pairs. These counts are not claims of full official-syllabus coverage.
- Applies the blue-gray reading design, 33 comparisons/diagrams and three selected decision trees. Conditions, exceptions, dates and actual source filenames remain visible.
- Preserves 525 question IDs, answers, grading and completed-history compatibility. Source audits and review history are retained, including the separately downloadable large baseline archive.
- 新增完整離線學習包：七部分筆記、練習App及引用的01–26原件。下載並完整解壓 `mso-study-bundle.zip`，開啟 `index.html`；單獨練習仍可下載 `mso-ca.html`。
- 筆記從原文整理，提供繁體中文、英文及雙語，共75個主題、533組雙語要點；數量不代表官方考綱完整覆蓋。
- 採用藍灰閱讀設計、33個對照／圖解及3棵經選擇的決策樹，保留條件、例外、日期及實際原件檔名。
- 保持525題的ID、答案、評分及已完成歷史紀錄兼容；保留來源審核證據，大型基線存檔另附下載。

**Upgrade / 升級：** Export history before replacing or moving the app, then import it in the new copy. 更換或移動App前先匯出紀錄，再匯入新版本。

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
- Preserves completed scores. Unfinished papers containing retired questions restart as full valid papers.
- Replaces obsolete agent-specific configuration with ordinary Markdown authoring instructions. Reorganises English and Chinese documentation around downloading, study, maintenance and release.
- Adds app behaviour and source-boundary tests, current-scope review evidence and checks that preserve earlier audit history.

**Upgrade:** export history from the old app first, then load the backup in the new file.

### 繁體中文

- 現行題庫只限重新整理的閱讀文檔庫 **01–26**。
- 擴充至 **525道中英雙語組合題**，七部分分別為60／75／65／80／80／100／65題。保留354題，移除3道範圍外題目，新增171道已獨立覆核題目。
- 只保留**模擬試**及**自選練習**，可選一個或多個部分。模擬試維持35題、每部分5題、75分鐘。
- 新增有原文依據的干擾項及應用情境，每項陳述均有解析。第24份的中文內容標為學習譯文；2022年報告結論保留年份。
- 保留已完成成績；包含退役題目的未完成試卷須重新開始。
- 移除過時的代理專用配置，改用通用Markdown編寫規範；重新整理中英文下載、溫習、維護及發佈說明。
- 新增功能及來源邊界測試、現行範圍覆核證據，同時保留舊審核的可核驗歷史。

**升級：** 先在舊App匯出紀錄，再於新檔案載入備份。

### Release files / 發佈檔案

- **mso-ca.html** — current 525-question offline app / 現行525題離線App。
- **mso-revision-pack.html** — legacy reference pack with an older source scope; not a third app mode or a complete guide to the current bank / 採用較舊來源範圍的歷史溫習資料，並非第三個模式或現行題庫的完整指南。

[Earlier releases / 較早版本](https://github.com/leohwlee/mso-ca/releases)
