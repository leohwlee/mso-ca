# Seven-part study notes / 七部分溫習筆記

Open [index.html](index.html) and select Part 1–7. The source-authored notes retain
the B blue-gray reference style and Traditional Chinese, English and bilingual
reading. Keep this folder inside the repository so original-file and practice
links work. Alternatively, download [v1.10.1's complete study bundle](https://github.com/leohwlee/mso-ca/releases/tag/v1.10.1),
extract it fully and open its root `index.html`. Reading pages embed their styles and font and work offline.

開啟 [index.html](index.html)，選擇Part 1–7。筆記以01–26原文整理，保留B風格、
繁體中文／英文／雙語與離線閱讀。保留於repo內，或下載[v1.10.1完整學習包](https://github.com/leohwlee/mso-ca/releases/tag/v1.10.1)
並完整解壓、開啟根目錄的`index.html`，原件及練習連結才可正常使用。

## Current audit / 本輪審核

The [20 October depth review](depth-review-2026-10-20/REPORT.md) reassesses all seven
Parts, prioritising complete lists, operative conditions and source modality in the
High-priority documents. The consolidated notes have 75 topics and 621 bilingual
point pairs; the 11 tables and 22 diagrams remain. These counts are not coverage
percentages. The report distinguishes source reading, meaning checks, selected
statutory coverage, automated checks and actual browser inspection.

[10月20日深度審核](depth-review-2026-10-20/REPORT.md)重新檢查七個Part，優先補足高優先級原文
的完整清單、適用條件及措辭強度。整合後有75主題、621組雙語要點，保留11張表及22個圖解；
數量不代表覆蓋率。報告明列已讀原文、含義核對、法例選定範圍、自動檢查及實際頁面檢視。

The [subsequent visual review](visual-refinement-2026-10-20/REPORT.md) inspects all
33 figures, with two independent assessments. It replaces the CDD trigger tree
with non-exclusive cases, preserves two genuine decision trees, exposes nested
AND conditions, and improves narrow-width tables, accessible headings and anchor
visibility. The 621 prose point pairs are unchanged by this visual refinement.
[Current previews](visual-refinement-2026-10-20/preview.html).

[隨後的視覺審核](visual-refinement-2026-10-20/REPORT.md)逐項檢查33個圖表，並採用兩項獨立評審。
CDD觸發圖改為可同時適用的情況圖，保留另外兩棵真正的決策樹；內層AND、窄屏表格、
輔助閱讀表頭及跳轉位置一併改善。本輪未刪改621組正文要點。
[本版預覽](visual-refinement-2026-10-20/preview.html)。

### Previous reviews / 先前審核

The previous omitted-content review of documents 04/25 adds 15 source-backed groups
(36 bilingual point pairs), including the owner-approved closeout. They cover predicate-offence proof, intelligence versus
prosecution, the significant controllers register, cross-sector laundering methods,
VA safeguards/offences/cooperation, and the non-Hong Kong DPMS cash-report contents.
After that approved visual upgrade, the result had 75 topics, 533 bilingual point pairs,
11 tables and 22 diagrams (including three decision trees).
These are size counts, not completeness measures.
See the [approval and final closeout](approval-closeout-2026-10-19/REPORT.md),
the [preceding omission report](omissions-review-2026-10-19/REPORT.md),
[source-based inclusion decisions](omissions-review-2026-10-19/DISPOSITION.md),
and [findings with source locations](omissions-review-2026-10-19/FINDINGS.md).

第04／25份未納入內容的後續審核連同本次收尾已落實15組補充，共36組雙語要點，
並重新生成七個Part。當時已批准的視覺優化後共有75個主題、533組雙語要點、11張表及22個示意圖（包括3棵決策樹）；
數量不是覆蓋率。[當輪收尾報告](approval-closeout-2026-10-19/REPORT.md)列出實際核對範圍、
取捨及驗證，並把需要理解的核心概念和其他行業參考分開。
歷史統計、其他行業行政費表／程序仍保留原文參考，不是因為未被引用便排除。
這不是所有條文逐字翻譯審校，也不保證涵蓋未知官方試題；官方出題來源不限於01–26。

The [visual upgrade report](visual-upgrade-2026-10-19/REPORT.md) records all seven parts,
the disposition of all 20 prior panels, 13 additions, independent reviews and actual
browser verification. It also records a source-confirmed correction to the English
cargo aggregation rule. [Preview gallery](visual-upgrade-2026-10-19/preview.html).

[可視化實施報告](visual-upgrade-2026-10-19/REPORT.md)逐項記錄原有20個圖表的處理、13個新增圖解、
兩項獨立評審及實際顯示驗證，另修正貨物合併規則的英文錯誤。
[代表頁面預覽](visual-upgrade-2026-10-19/preview.html)。

Earlier evidence is preserved: [Chinese-source follow-up (17 findings)](chinese-followup-2026-10-19/REPORT.md),
[independent audit (36 findings)](independent-audit-2026-10-19/REPORT.md),
[official scope and original coverage map](independent-audit-2026-10-19/COVERAGE.md),
and [visual decisions](independent-audit-2026-10-19/VISUAL-REVIEW.md).
先前17項中文核對及36項獨立審核記錄原樣保留，不作本輪正確性的替代證據。

Exact repository filenames and paragraph/section/page locators appear in citations.
Document 24 has no official Chinese edition: Chinese is a labelled study translation
and both modes cite the English original. Historical risk findings and FATF lists
retain their dates. Current exam-guidance checks and current-law checks are reported
separately; the archived legislation is not represented as live-verified law.

引用顯示實際檔名及定位。第24份中文明標學習譯文並連到英文原件；風險報告、
名單及歷史統計保留年份。官方考試要求的最新性與法例版本的核實分開報告。

## Maintain / 維護

`part1.py`–`part7.py` hold the consolidated manuscripts, including the former
second-pass additions. `essentials.py` is an empty compatibility module; it no longer
adds a second layer of prose. `memory_panels.py` holds explicit source references for
the selected comparisons. `visual_panels.py` adapts/adds source-bound diagrams;
`visual_render.py` provides native, offline HTML rendering. `build.py` validates
and renders without reading the bank.

`part1.py`至`part7.py`保存整合後文稿；舊第二輪補充已併入相應主題，
`essentials.py`只保留空白兼容入口。`memory_panels.py`的圖表有明確原文引用。
`visual_panels.py`處理圖解內容及改編，`visual_render.py`負責離線HTML表達；生成器不讀題庫。

`gap_check.py` separately checks 525 identifiers and source routes after authoring;
it cannot establish semantic completeness. Its current output is
`visual-refinement-2026-10-20/bank-source-routes.json`. Earlier outputs remain historical evidence. Manual question-stem concept
checking is described in the audit report; no question content supplies the notes.

題庫只於最後作題幹概念及來源路徑查漏，發現問題後回原文核實；
不把自動來源對應稱為525題每個陳述均已覆蓋。題目、答案及評分未改。

```text
python revision/study-notes/build.py
python revision/study-notes/gap_check.py
python revision/study-notes/build.py --check
python revision/study-notes/gap_check.py --check
```

Build the practice target with `go run . -export-html dist/mso-ca.html`.
See [current visual checks](visual-refinement-2026-10-20/REPORT.md), the
[depth review checks](depth-review-2026-10-20/REPORT.md) and the preserved
[earlier verification](independent-audit-2026-10-19/VERIFICATION.md) for actual results.

## Preserved evidence / 保留證據

The starting state is preserved in
`independent-audit-2026-10-19/baseline.zip`, with the initial working-tree state and
387 file hashes in `baseline.json`. Existing QA, COMPLETENESS, review JSON, gap-audit
and history ZIPs remain evidence of their own versions. They were not used as proof
of current content correctness. `coverage.json` is the current generated manifest.

本輪基線保留原有改動及歷史紀錄；舊QA、COMPLETENESS、review、gap-audit及歷史ZIP
不改寫、不作本版正確性的背書。早期Part 6樣章不作正式文稿來源。
公開發佈版本與下載方式見根目錄[版本記錄](../../CHANGELOG.md)；上述審核日期及歷史結論不因發佈而改寫。
