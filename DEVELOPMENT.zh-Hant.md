# 開發說明

[English version →](DEVELOPMENT.md)

## 模擬試

本專案存放程式的組成部分（`web/`）及一個小型 Go 程式，用以把它們合併成單一檔案。只需 Go 1.27 或以上，別無其他依賴。

```bash
go test ./...                          # 題庫檢查 + vet
go run . -export-html dist/mso-ca.html # 產生單一檔案
go run .                               # 或：開發時在本機提供 web/
```

`build.cmd`（Windows）或 `./build.sh`（Mac/Linux）效果相同。

題庫為 `web/questions.json`。`go test ./...` 並非只檢查格式，而是防範一些會悄悄毀掉題庫的問題——每一項檢查都是在審核中真的發現了該問題之後才加入的。

| 檢查項目 | 防範甚麼 |
|---|---|
| 各單元題數、4 或 5 個選項、中英文齊備、出處齊備 | 題目遺失或只寫了一半 |
| 選項長度平衡、位次、分布及突出 | 「一律揀最長」——這招曾經足以通過 64% 的模擬試卷 |
| 出處須有定位 | 只列文件名稱，讀者無從翻查 |
| 法定中文用語 | 使用官方中文本從未採用的字眼 |
| ML/TF 對應 | 中文漏掉「恐怖分子資金籌集」那一半 |
| 不得以位置稱呼選項 | 解釋寫「選項二」，但選項是隨機排列的 |
| 不得有重複題幹，不同單元不得有相同答案 | 同一條問題被問兩次 |
| 組合題陳述中的絕對用語 | 「一律」、「絕不」成為辨認錯誤陳述的線索 |
| 選項標點一致 | 一個分號洩露了正確答案 |
| 組合題格式 | 選項須與官方印本逐字相同，答案字母須分布平均 |
| 題幹須說明條文內容；選項不得只是條文編號 | 問「第 N 條規定甚麼」或「某規定載於哪一條」——考的是背條號，不是規定本身 |

上表背後的做法——如何依據一組固定文件編寫雙語題庫、如何蒙著答案覆核、以及如何量度那些讓考生不必讀懂教材也能猜中的表面線索——已整理成一份可重用的 skill，見 [`.claude/skills/exam-question-bank/SKILL.md`](.claude/skills/exam-question-bank/SKILL.md)。它並不限於本考試。

字型：DM Sans 及 DM Mono 以 SIL Open Font License 內嵌；中文使用作業系統字型。

## 溫習資料

溫習資料由 [`revision/`](revision/README.md) 產生，只需 Python 3 標準程式庫：

```bash
python revision/pack_build.py dist/mso-revision-pack.html
```

各頁的結構、須遵守的規則及檢查工具，見 [`revision/README.md`](revision/README.md)。

## 發佈

發佈以標籤觸發。推送以 `v` 開頭的標籤，會執行 [`release.yml`](.github/workflows/release.yml)：先 vet 及測試題庫，再從該 commit 產生檔案，連同由 `revision/` 產生的溫習資料一併附加到 GitHub release。測試在產生檔案之前執行，所以未通過檢查的標籤不會變成可供下載的版本。

```bash
git tag v1.6.1
git push origin v1.6.1
```
