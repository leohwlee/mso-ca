# Part 6 study sample / 第6部分溫習樣章

For v1.10.1, read [the maintained Part 6](../study-notes/part-6.html). This historical sample is not the current manuscript or a release asset; its original review describes its own version.

v1.10.1請閱讀[正式第6部分](../study-notes/part-6.html)。本頁為歷史樣章，不是現行文稿，也不隨發佈附送；原審核只適用於當時版本。

The [complete seven-part reading material](../study-notes/index.html) now uses the
selected B design. This earlier URL remains supported; its maintained stylesheet
is [the shared reading stylesheet](../study-notes/style.css).

新版[七部分溫習資料](../study-notes/index.html)已採用 B 設計；本樣章網址仍可使用，
現行樣式來自[共用閱讀樣式](../study-notes/style.css)。

Open [the bilingual sample](index.html). It reads without a server or network.
Keep it in this folder to preserve the relative links to original files in `docs/`.
The practice link uses the existing locally built `dist/mso-ca.html`.

開啟[雙語樣章](index.html)，毋須伺服器或網絡即可閱讀。保留本資料夾與
`docs/` 的相對位置，原件連結才可使用。練習連結使用已在本地建立的
`dist/mso-ca.html`。

## Contents / 內容

The sample covers customer due diligence, ownership and control, identification
evidence, delayed/remote verification, risk-based measures and PEPs, intermediary
reliance, monitoring, screening, third-party payments, transfers, delivery channels,
trade risks and the related suspicious-reporting process. Chinese, English and
combined views contain the same authored topics. There is no hidden-answer mode
or new quiz. Source references show real repository filenames and precise locators.

樣章涵蓋客戶盡職審查、擁有權及控制權、身分證據、延後及遙距核實、風險為本
措施及政治人物、中介人、監察、篩查、第三方支付、轉帳、交付渠道、貿易風險及
相關可疑交易報告流程。設中文、英文及雙語閱讀；直接顯示全部內容，不設隱藏
答案或新增測驗。引用列明實際檔名及具體定位。

This is a format/content sample within the selected documents 01–26, not a complete
official syllabus. All 100 existing Part 6 question IDs are associated with topics
in [coverage.json](coverage.json). This is a topic map, not proof that every statement
of every question has been taught or re-reviewed. Source 24's Chinese summaries are
study translations and link to the English original. Advanced statutory lists
should be read in full in the linked source; the tables identify their conditions
without claiming to reproduce every subparagraph.

這是01–26指定範圍內的格式及內容樣章，不是完整官方考綱。現有100道第6部分
題目的主題對應見 [coverage.json](coverage.json)；這不等於已逐句講解或重新
覆核全部題目。第24號中文摘要為學習譯文，連往英文原件。較長法定名單仍應
在連結原件內完整閱讀；對照表不宣稱抄錄全部分段。

## Maintain / 維護

`content.py` contains the authored bilingual content; `build.py` resolves source
editions through the catalog and creates the HTML and mapping. `../study-notes/style.css` holds
the maintained layout and typography and is embedded in the output HTML, along
with the existing bundled DM Sans font. The design decisions are in
[DESIGN.md](DESIGN.md). Run from repo root:

`content.py` 為雙語內容；`build.py` 按文件目錄解析版次，建立HTML及對照。
`../study-notes/style.css` 為共用排版樣式，會連同現有 DM Sans 字型嵌入HTML；設計說明見
[DESIGN.md](DESIGN.md)。從倉庫根目錄執行：

```text
python revision/part6-sample/build.py
python revision/part6-sample/build.py --check
```

The check validates bilingual fields, citation/file/paragraph existence, internal
links, 100 unique question mappings and deterministic output. It does not establish
semantic correctness. `coverage.json` records source and manuscript hashes plus
the applicable conflict-decision IDs. Author source-context/bilingual self-review
is not independent review; no separate reviewer is claimed. Legacy pack files and
historical review hashes remain untouched. The new sample is not attached to
releases by the existing workflow.

檢查涵蓋雙語欄位、引用及檔案／段落存在、內部連結、100個不重複題號對應及
輸出一致性；不代表語義必然正確。`coverage.json` 記錄來源及內容雜湊，以及
適用的既有矛盾裁決。作者已自行對照來源及雙語內容，並未宣稱獨立覆核。
現有發佈流程尚未包含此樣章。

[usage.json](usage.json) records account-wide rounded usage before/after production;
other chats and reporting delays can affect the difference.

[usage.json](usage.json) 記錄製作前後的帳戶整數用量；其他聊天及回報延遲可能
影響差值。顯示不變不能證明完全沒有消耗。
