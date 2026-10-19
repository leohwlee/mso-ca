# Source-first rewrite verification / 原文筆記重寫核驗

Date: 19 October 2026. This record supersedes the bank-derived page claims;
the preceding version is preserved in `history/2026-10-19-bank-derived.zip`.

## Provenance / 來源

Seven manuscripts were authored from the repository's original publications
01–26. The main structure follows the seven assessment Parts in source 01.
Definitions, actors, modal strength, thresholds, deadlines, exceptions and dated
findings are taught directly. The renderer does not load the question/quote bank.
The final build contains 74 topics and 450 bilingual explanatory points, with
25 supplementary comparison tables and two diagrams across all seven Parts.
Recall values retain operators, units, clock starting events, conditions and
exceptions. Selective term emphasis leaves the explanatory text intact.

原文先行，題庫只作事後查漏。文稿以概念及規則為主，不含題幹標題、選項或
真假陳述拆解。各內容塊均保留實際repo檔名及原文定位。

Source reading covered the substantive MSO Guideline 03; relevant AMLO main
Parts and Schedules 1–4 in 04; the assessment/licensing guides; FAQ and circulars;
Cap.34 and Cap.629 provisions relevant to the selected publications; and document
25's executive summary, methodology and MSO sector. It does not claim to condense
every unrelated TCSP/VASP/PMS regime or every sector of the 197-page risk report.
Document 02 supports assessment format only. Document 24's TC text is explicitly
a study translation from its English original. Existing conflict decisions apply.

第25份以行政摘要、方法及MSO行業為重點；第02份只用於題型說明。日期性資料
保留原出版時間，不宣稱已核實repo版本以外的最新法例或名單。

`coverage.json` binds the seven manuscripts and original extracted texts by
SHA-256 and lists each source-to-section route. Anchor checks establish that a
passage can be located; they do not by themselves prove semantic support.
`gap-audit.json` records all 525 bank identifiers for the separate gap pass and
the original-source topics supplemented. No bank content supplies the notes.

## Independent review / 獨立覆核

Review findings and the final bounded verdict are recorded in
`source-review.json`. The reviewer read all seven manuscripts and checked relevant
original passages. It is a source/qualifier review at the stated scope, not a
claim of independently reviewing every page or certifying the entire syllabus.
All 23 reported findings were resolved and read back for that preceding version.
That immutable record does not claim to bind later edits: the version before
recall aids is preserved in `history/2026-10-19-before-memory-visuals.zip`.

The preceding `memory-review.json` independently reviewed all 27 bilingual recall aids
against their relevant stored original passages. All ten reported findings were
resolved and read back. Its scope also covers the targeted Part 2/4 cessation
clock, Part 2 daily fine caps and Part 6 domestic-wire prose corrections. It
binds that preceding snapshot, preserved in
`history/2026-10-19-before-completeness-pass.zip`, without re-certifying later edits.
Original `source-review.json` and `memory-review.json` remain unchanged.

新增對照表及示意圖已另作原文覆核；10項發現均已修正，沒有未解決項目。
覆核範圍及原文定位載於`memory-review.json`；舊覆核紀錄不作事後改寫。

The second source-led pass adds 47 source-authored blocks / 87 bilingual point
pairs from `essentials.py`. It corrects checked-baggage scope in Part1 and dormant
reactivation review in Part6, and adds the seven-day nomination recall row.
`completeness-final-review.json`, `completeness-guideline-final-review.json` and
`completeness-circulars-final-review.json` divide the independent final read-back
of the new material and specified base corrections. Reported material findings
are resolved in their explicit scopes. Whole-file bindings do not broaden those
scopes into an assertion that each reviewer inspected every paragraph.
See `COMPLETENESS.md` and `completeness-audit.json` for the source-by-source route.

第二輪再查核定義、必記清單、責任人及條件，補87組雙語說明。最終覆核按範圍分工，
三份本輪紀錄均保留原文及正文校驗值；不以自動定位檢查冒充語義覆核。

## Verification / 檢查

Final automated and rendered checks are recorded after the final manuscript
corrections in `verification.json`. The bank, deciding quote bank and source
originals remain unchanged. Historical hashes are not replaced.

- Catalog/original hashes, active scope/accounting, four historical audits and
  deterministic note/gap/sample outputs passed.
- Go tests/vet, eight JavaScript tests and sixteen Python tests passed; the
  exam HTML was rebuilt. Python archive tests use a verified workspace temporary
  directory to avoid the sandbox's default temporary-folder permissions. No test
  was disabled.
- All seven reading pages were exercised in TC, EN and Both at actual browser
  widths 390, 768 and 1440: 63 observations, with no page/table overflow,
  question-stem headings or empty visible citation labels. Console warning/error capture
  was empty. Tests also verify every complete explanatory point survives rendering.
- The new Structuring/Smurfing and U-turn definitions were visually inspected.
  The corrected checked-baggage condition was read back in Both on mobile;
  practice links retain Part/language. Prior reading/practice integration evidence
  remains in the preserved verification archive; no score was submitted.
- The earlier `memory-finish-review.md` returned `ship` for the preceding recall
  aids. This content-only pass preserves the same CSS, geometry, controls and
  practice UI and adds fresh rendered checks. That older visual review did not
  certify legal content; original seed-roll/quality-card corroboration was not
  available, and no new visual world was rolled.

Browser inspection uses localhost because the browser tool does not permit
`file:` navigation. Embedded styles/fonts and relative links are checked by the
builder; no live file-protocol test is claimed. Current representative captures
are `.impeccable/review/completeness-*`; `memory-*` and `source-notes-*` record the
preceding passes. Earlier captures are not evidence of the current added text.
