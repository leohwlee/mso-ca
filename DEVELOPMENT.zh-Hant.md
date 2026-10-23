# 開發說明

[English](DEVELOPMENT.md) · [文件總目錄](docs/INDEX.md)

## 保留甚麼，以及原因

使用者只需下載 `mso-ca.html` 並用瀏覽器開啟；不需要伺服器、資料庫、帳戶或 API 金鑰。

| 檔案 | 用途 |
|---|---|
| `web/` | App 畫面、操作、樣式、字型及552道雙語題。 |
| `main.go`、`go.mod` | 把 App 打包成一個離線 HTML；沒有第三方 Go 依賴。 |
| 四個 `*_test.go` | 檢查打包結果、答案、來源引文、語言及猜題線索。 |
| `tests/` | JavaScript 功能測試及 Python 來源、覆核約束。 |
| `bank/` | 出題工具、停用題號及覆核證據。 |
| `docs/` | 原始文件、擷取文字、引文及必要說明。 |
| `revision/` | 七部分溫習資料、仍可使用的第6部分樣章網址、舊資料歸檔入口及文件矛盾裁決。 |

Go 是打包及品質檢查工具，並非 App 後端。把現有測試改寫成另一種語言只會重做已正常運作的檢查。
JavaScript 負責 App 操作；Python 負責來源擷取、出題及覆核記錄。

## 建置及完整檢查

安裝 Go 1.27 或以上、Node.js 22 或以上及 Python 3.10 或以上，從倉庫根目錄執行：

```bash
go run . -export-html dist/mso-ca.html
go vet ./...
go test ./...
node --test tests/*.test.cjs
python -m unittest discover -s tests -p '*_test.py'
python docs/build_catalog.py --check
python bank/audit/active_scope.py --check
python bank/audit/render_active_scope.py --check
python bank/audit/report.py --check
python bank/audit/terms_report.py --check
python bank/audit/p1_report.py --check
python bank/audit/remaining_report.py --check
go run . -export-html dist/mso-ca.html
```

原文編寫的七部分筆記先執行 `python revision/study-notes/build.py`，再用
`python revision/study-notes/gap_check.py` 另外作題庫查漏；正文生成器不讀題庫。
兩個命令加上 `--check` 可檢查輸出一致性。舊Part 6樣章另以
`python revision/part6-sample/build.py` 維護。CI與公開發佈流程亦會核對七部分閱讀頁，
並建立完整離線學習包。

Python 工具一般只用標準函式庫；重新擷取來源文字才需要 PyMuPDF。
Windows 若 `python` 開啟 Store，可改用 `py -3`；中文輸出有問題時加 `-X utf8`。
建置後開啟 `dist/mso-ca.html`。開發預覽可執行
`python -m http.server 8321 --bind 127.0.0.1 -d web`，再開啟 `http://127.0.0.1:8321`。

## 題庫、來源與證據

修改前閱讀[題目規格](bank/FORMAT.md)、[出題流程](docs/authoring/exam-prep/GUIDE.md)及
[來源維護](docs/SOURCE-MAINTENANCE.zh-Hant.md)。現行報告核驗01–26來源的552題：
先由新至舊還原 `bank/audit/active-followups/` 內每項已覆核改動（各附盲審記錄及改動前題庫存檔），
再按原樣核驗active26記錄。四份舊報告重建各自的歷史題庫，不代表現行覆蓋率。1,526個停用題號仍不可重用。

更改被舊覆核綁定的文件時，先把原始位元組保存在不可改寫的存檔，再新增記錄連接新舊摘要。
不得修改舊摘要來消除錯誤。舊溫習資料的原始碼仍與原覆核摘要核對，但不再日常重建。

## 發佈

更新雙語 `CHANGELOG.md`、完成檢查並開啟 HTML，檢視及提交改動後推送分支。
獲授權發佈時，把該版更新說明存成檔案，再建立未使用的新版本標籤：

```bash
git tag -a vX.Y.Z --cleanup=whitespace -F notes.md
git push origin vX.Y.Z
```

把 `vX.Y.Z` 換成實際版本。自動流程會檢查並從該次提交建立 `mso-ca.html`。
確認 CI 及 Release 成功，再下載附件核對；不可覆蓋已發佈標籤。
舊溫習資料仍可從既有版本及[存檔](revision/README.md)取回，不再重建。
v1.10.0起發佈 `mso-ca.html` 和 `mso-study-bundle.zip`；完整學習包含新版七部分筆記、
練習App及由目錄解析的01–26原件。用 `python scripts/build_study_bundle.py` 建置，
加 `--check` 核對全部成員及閱讀頁連結。全新工作區須先匯出App，再執行Python連結檢查。
`dist/` 及 Python 快取是本機產物。
