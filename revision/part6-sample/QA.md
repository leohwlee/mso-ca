# Sample verification / 樣章檢查

Production date / 製作日期: 18 October 2026.

## Content / 內容

- 14 topics, 7 process diagrams, 69 comparison rows, 98 citation groups.
- 100 unique existing Part 6 question IDs mapped to a topic; no question, answer,
  quotation or historical review evidence was changed.
- Citations resolve through `docs/catalog.json` to the actual local edition and
  display its complete filename. Source 24 uses the English original in both views
  and labels Chinese summaries as study translations.
- Source-context/bilingual author self-review included CDD thresholds and linkage,
  ownership/control and trust definitions, delayed verification, recognised digital
  ID, PEP categories and former PEPs, intermediary retention, screening parties,
  third-party payment acceptance, transfer data and card exclusions.
- In particular, FAQ24's six screening parties were checked in the original FAQ;
  the card exception retains ATM withdrawal/cash-advance examples, not purchases
  only; PEP approval does not add an unsupported independence requirement.
- Applied existing source decisions, including B14 (statutory BO definition), B16
  (occasional CDD timing), E17 (first payment) and E41 (both transaction-condition
  groups together). Other relevant decision IDs are in `coverage.json`.

14個主題、7個流程圖、69行對照內容及98組引用。100道現有第6部分題目已建立
主題對應；並未改動題庫、答案、引文或歷史覆核證據。已自行對照來源上下文及
雙語內容，特別核對門檻、名單、條件及例外。本檢查不屬獨立語義覆核，不宣稱
逐句覆蓋全部100題或完整官方考綱。

## Page / 頁面

- Browser rendering checked at 390, 768 and 1280 pixels in Chinese, English and
  combined views: no page overflow or overflowing rule/table cells in any of the
  nine combinations.
- Desktop and mobile layouts visually inspected. Narrow-screen navigation is a
  horizontal topic strip; tables become labelled cards. Source filenames wrap.
- English mode hides Chinese content; all 14 topics remain directly visible in
  every language. Search controls were removed at the owner's request.
- Chapter navigation reaches the intended anchor. No browser console warnings
  or errors were reported in the checked page.
- Structural checks verify unique IDs, source files and paragraph markers,
  internal links, complete bilingual fields, scope and deterministic regeneration.
- CSS includes print styling. The operating-system print dialog/output was not
  separately inspected; no PDF is a deliverable of this sample. The explicit Print
  button and its event handler were subsequently removed at the owner's request;
  regeneration and structural checks passed. Offline-file browser inspection was
  unavailable because the browser tool blocks file URLs; no new visual check is
  claimed for that button removal.
- Browser-comment edits: branding changed to `MSO Competence Assessment Study Note`; header
  controls reduced to 28px tall; the source-summary section and its navigation
  link removed. All 98 inline citation groups remain. Desktop and 390px layouts
  were rechecked without horizontal overflow; the preview image was refreshed.
- The main heading now uses the Part 6 topic title. The former slogan, subtitle,
  sample metadata, search area and green introductory panel were removed. The
  nine viewport/language combinations were rechecked; no console errors reported.

已在390、768及1280像素寬度，分別檢查中文、英文及雙語顯示，九種組合均沒有
頁面或表格／流程框文字溢出。另目視檢查桌面及手機版，並測試語言切換及章節
定位。搜尋欄已按使用者要求移除。列印樣式已加入，但未另外檢查系統列印
輸出；本次交付不包含PDF。
其後已按要求移除列印按鈕及其操作程式，重新建立及結構檢查通過。瀏覽器工具
不允許檢查離線檔案網址，因此這次按鈕移除未另作瀏覽器目視核驗。

已按瀏覽器批註更改頁首名稱、縮小操作按鈕，並移除末尾來源匯總及其導覽連結；
98組正文引用保留。桌面及390像素寬度均重新檢查，未見水平溢出。
主標題已改用第6部分的主題名稱，並移除原宣傳標語、副標題、樣章標籤、搜尋欄
及綠色說明框；三種寬度配合三種語言的九種組合均重新檢查。

## Impeccable + Frontend Design refinement / 設計調整

- Installed both requested personal skills and read their design guidance.
  Impeccable skill version: 4.6.0; engine: 0.1.15. The official release binary
  matched its published SHA256 and the standard installed launcher returned
  `impeccable-engine 0.1.15`.
- Revised the maintained stylesheet and rebuilt the self-contained HTML. The
  existing DM Sans variable font is embedded; no remote font or framework was
  added. Kept the requested exact branding, official Part 6 heading, compact
  language controls and all inline filename citations. Print/search controls,
  introductory scope panel and source-summary section remain removed.
- Reduced title scale to 34/28/26px, replaced heavy table stripes and rounded
  enclosures with lighter comparison rules, differentiated common confusions,
  clarified diagram grouping, and added current-topic navigation and a keyboard
  skip link. The phone third-party diagram now shows the stop branch before the
  distinct acceptance branch, avoiding a misleading stop-to-follow-up sequence.
- Rechecked all nine 1280/768/390px × TC/EN/both combinations: 14 visible topics,
  no page overflow and no overflowing table cells, diagram nodes or citations.
  Raw observations: [browser-check.json](browser-check.json). Also checked 320px
  combined-view reflow without page overflow. This is viewport testing, not a
  claim of testing the browser's actual zoom control or every assistive tool.
- Visually inspected desktop and mobile comparisons and the phone third-party
  diagram. Confirmed language-button keyboard traversal with a visible outline,
  correct risk-topic anchor and current-topic state, and no captured console
  warnings/errors. Font loading completed. Preview images were refreshed.
- Main text contrast on white: 13.35:1; secondary text on white: 5.98:1; secondary
  text on the warm surface: 5.59:1; white text on the active-language green:
  7.07:1; white text on the stop surface: 11.81:1.
- Impeccable's static type/layout scan went from 38 findings to one. The remaining
  `oversized-h1` finding incorrectly reports 3872px and combines both language
  strings. Browser-computed sizes are 34/28/26px, with screenshots checked in
  actual language modes. No ignore rule was added and no all-clear detector
  result is claimed. Static scanning is a supplemental check, not visual proof.
- The manuscript and question-bank SHA256 values still match `coverage.json`.
  All 14 topics, 69 comparison rows, 7 diagrams, 100 question mappings and 98
  citation groups remain. Builder validation and deterministic regeneration pass.
  This pass did not repeat the repository-wide source/question tests below,
  because it changes presentation and navigation, not source or bank content.

已安裝並結合兩個 skill，調整標題、字型、對照表、流程圖及導覽。正文和題庫
內容雜湊保持一致，98組檔名引用保留。九種屏幕／語言組合及額外320像素雙語
顯示均未見頁面水平溢出；另目視檢查桌面、手機及第三方支付流程，核對鍵盤
焦點和章節定位，未捕捉到瀏覽器警告或錯誤。重新建立及一致性檢查通過。

靜態設計檢查由38項降至1項；餘下一項把標題誤讀為3872像素，實際瀏覽器
計算為34／28／26像素。沒有加入忽略規則，也不宣稱靜態檢查完全零提示。
本次只調整顯示與導覽，未重跑下列先前已通過的全倉庫內容檢查。

## Repository / 倉庫

Passed: `go vet ./...`, `go test ./...`, all six JavaScript tests, all ten Python
tests, catalog check, active-scope check and render check, and all four historical
audit checks (`report`, `terms_report`, `p1_report`, `remaining_report`). Existing
exam HTML was rebuilt successfully. Python temporary directories were redirected
to ignored `dist/test-temp` after the default sandbox temp location denied access;
the successful ten-test run used that writable directory.

現有Go、JavaScript、Python、文件目錄、現行範圍及四項歷史審核檢查均通過，
練習App的離線HTML已成功建立。Python首次因環境臨時目錄權限失敗，改用
`dist/test-temp` 後10項測試全部通過。

The new sample is deliberately local and is not added to release automation.
The original archived pack remains archived. Usage comparison is in `usage.json`.

新版樣章暫供本地檢視，尚未加入發佈流程；舊版仍保留於歸檔。用量記錄見
`usage.json`。
