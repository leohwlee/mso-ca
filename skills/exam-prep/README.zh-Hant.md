# exam-prep——把原始資料變成溫習資料及模擬試的技能

[English](README.md)

`exam-prep` 是一個 [Agent Skill](https://agentskills.io)：一個載有說明、參考文件、
腳本及範本的資料夾。能讀取 `SKILL.md` 的代理（例如 Claude Code）在有人要求把文件
或文案變成溫習筆記、練習題或模擬試時載入它。它適用於任何科目、任何一種或兩種
語言，以及任何考試形式：單選及多選題、組合題（K 型）、是非題、配對、排序、填充、
數值題、附評分準則的短答及論述題，以及個案題組。

它提煉自本 repo 的發展歷程：為香港金錢服務經營者能力評核製作雙語題庫及溫習筆記，
八個星期內發佈 43 個版本，以及每個版本所需的修正。方法及數據見
[`references/case-study.md`](references/case-study.md)。此技能是通用的；本 repo
自身的出題規則仍以 [`docs/authoring/exam-prep/GUIDE.md`](../../docs/authoring/exam-prep/GUIDE.md)
及 [`bank/FORMAT.md`](../../bank/FORMAT.md) 為準。

## 產出

| 產品 | 做法 |
|---|---|
| 溫習筆記 | 以 [`assets/notes-template.html`](assets/notes-template.html) 製作的離線 HTML：學習層次、規則旁的易錯提示、標明項數的清單卡、數字表、流程圖、層次篩選、語言切換及默記模式 |
| 題庫 | 依 [`references/formats.md`](references/formats.md) 格式的 JSON，每題有出處、決定答案的原文及每個選項或陳述的解釋 |
| 模擬試 | 由 `scripts/build_app.py` 生成的單一離線 HTML：按真實抽題及合格規則計時作答、分部分練習、錯題本、文字答案自行評分、可匯出及匯入的紀錄 |
| 檢查 | `scripts/bank_tool.py`：硬性錯誤、表面線索報告（含自學猜題器及模擬試卷）、盲審題包及比對 |

## 安裝

把 `exam-prep` 資料夾複製到代理的技能資料夾，例如 Claude Code 的
`~/.claude/skills/exam-prep/`（所有項目）或 `<項目>/.claude/skills/exam-prep/`（單一項目）。
然後直接提出要求，例如：「把這些 PDF 做成溫習筆記和一份 40 題的模擬試」。

腳本只需 Python 3.9 或以上；如已安裝 PyMuPDF 或 pypdf，會用來抽取 PDF 文字。

## 試用示例

```bash
python scripts/selftest.py
python scripts/bank_tool.py check assets/example/spec.json assets/example/bank.json --sources assets/example/sources
python scripts/build_app.py assets/example/spec.json assets/example/bank.json -o example-exam.html
```

把 `assets/notes-template.html` 複製到 `example-exam.html` 旁並命名為 `notes.html`，
應用程式的「在筆記中閱讀」連結即可使用。

## 測試

`scripts/selftest.py` 證明每項內置檢查都能報錯。`evals/` 有三個行為測試：把政策做成20題離線模擬試、
把簡體中文生物講義做成筆記及判斷題、把產品文案做成組合題及速查表。每個測試附提示詞、輸入檔及評分準則，
格式符合 `claude plugin eval`；在此資料夾執行 `claude plugin eval . --scaffold --allow-tools Write,Edit,Bash`
即可分別在使用及不使用技能的情況下運行。這些是真實、需計費的模型運行。

## 授權

MIT，與本 repo 的程式碼相同。
