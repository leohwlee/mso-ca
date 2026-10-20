# 本輪證據目錄

本目錄記錄內容深度審核完成時的版本；其後的[視覺修訂及最新預覽](../visual-refinement-2026-10-20/REPORT.md)隨v1.10.1發佈。當時的截圖、三棵決策樹數量和檔案雜湊保留不改；現行版為兩棵決策樹，CDD觸發已改為可並存情況圖。

正式結果以 `REPORT.md`、三份來源覆核、`findings.json` 及最後檢查記錄為準；閱讀入口為上層七個Part。

- `baseline.zip/json` 保存本輪開始時的已提交文稿及檔案指紋。
- `automatic-checks-initial.json` 保留初次結果，包括四個歷史檢查失敗；`automatic-checks-final.json` 是加入新的證據維護記錄及最終內容後的重驗。沒有改舊證據雜湊。
- `browser-checks.json`、`integration-checks.json`、`previews/` 為最終頁面的實際執行／截圖；`final-state.json` 匯總最後狀態及未變更檔案驗證。
- `edit_guideline.py`、`finish_guideline.py`、`clarify_boundaries.py`、`review_corrections.py`、`refine_strength.py`、`integrate.py`、`part7_strength.py`、`glossary_followup.py`、`final_gap_fixes.py` 是**本輪一次性中間編輯記錄**。部分早期提案其後已更正，不能當正式筆記或重新執行（重跑可能重複新增）。`*_additions.py` 同樣是代理提案快照，已由主審合入並修正。
- `write_reports.py` 只編排本輪記錄；`run_checks.py`／`final_checks.py`／`verify_pages.cjs` 記錄實際檢查方法，不是筆記生成來源。

正式生成器只讀上層已整合的內容與視覺文稿，不導入此目錄的草稿。原文已讀、含義已核對、引用已定位、自動檢查通過及限定範圍覆核完成，分別在報告中記錄，不互相替代。
