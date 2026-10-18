# 來源文件維護說明

[English →](SOURCE-MAINTENANCE.md)

## 每份材料只有一個編號

閱讀目錄、檔名前綴、引文`doc`、文字檔及轉錄檔，都使用同一兩位數編號。
`catalog.json`是單一清單，配套原件也各佔一個編號：

- 01–09：高優先級。
- 10–19：中重點。
- 20–26：中選讀。
- 27–47：歷史參考，接續同一序列。

第34章全文為**17**，排在通函**16**後；第629章全文為**23**，排在通函**22**後。
`parent_document`只記錄配套關係，不是另一套來源ID。反洗錢指引是**03**，
第615章是**04**；定期申報通函及圖片轉錄現在是**15**。不留空號，也不維護執行時舊號查找。

## 原件、語言及文字

每個版本的`path`是相對`docs/`的現行位置。日常原件在`TC/`和`EN/`，
歷史參考在`archive/LANG/`。文字統一為`text/LANG/NN.txt`，並記錄文字摘要。
BI表示中英雙語；ZH表示官方簡體中文。第**24**項在兩個資料夾直接放英文原件，
中文檔名已註明，不能當作中文譯本。兩部雙語法例在兩個資料夾的PDF位元組完全相同。

PDF、DOCX及HTML摘要按原始位元組計算；Markdown先統一為LF換行。
`extract_text.py`處理全部47項；`text_mode: companion`保留配套原先的擷取方式，
避免改號改變文字。`extract_related.py`是同一流程的相容入口。
`transcripts/15.json`的圖片標籤仍與原PDF摘要綁定。

`original_bank_source`標示既有題庫所用的23份來源。其他材料，包括兩部完整法例，
雖然已獨立編號，仍不能假定已納入出題依據。使用前須核對版本、語言、適用範圍，
並擴充`sources_test.go`的引用識別。歷史參考中的題庫來源仍保留原件及文字供核驗。

## 修改原件或閱讀順序

更換原件後，更新原件摘要、重新擷取文字，覆核受影響引文及圖片轉錄。
`build_catalog.py`同時產生雙語的日常及歷史目錄。
`reading_status`、`study_focus`及雙語`archive_reason`記錄復習取捨。

改閱讀順序時，同步遷移檔名、目錄編號、文字、清單、引文、轉錄、引用規則、報告及例子。
題號、題目、真假值、選項及答案保持不變，避免影響舊作答紀錄。
原始證據保留於`bank/audit/history/`的不可變ZIP快照。先重建每輪舊引文並命中原摘要，
再從只改編號的結果推導新摘要，不能只改摘要消除錯誤。壓縮舊文字須核對ZIP及現行後繼檔案。
歷史新舊對照僅供驗證，不作往後查號使用。

## 檢查

```bash
python docs/extract_text.py
python docs/build_catalog.py --check
go test ./...
python bank/audit/report.py --check
python bank/audit/terms_report.py --check
python bank/audit/p1_report.py --check
python bank/audit/remaining_report.py --check
go run . -export-html dist/mso-ca.html
python revision/pack_build.py dist/mso-revision-pack.html
```

模擬試按題號保存進度，改文件編號不改題號或舊答案。過往證據見[歷史存檔](../bank/audit/history/README.md)。
