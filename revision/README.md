# Archived revision pack / 已歸檔的舊溫習資料

Current release: [v1.10.1](https://github.com/leohwlee/mso-ca/releases/tag/v1.10.1). Use `mso-study-bundle.zip` for the updated seven-part notes, practice and originals 01–26.

現行版本：[v1.10.1](https://github.com/leohwlee/mso-ca/releases/tag/v1.10.1)。下載完整學習包，可離線閱讀更新後的七部分筆記、練習及01–26原件。

The new [seven-part study material](study-notes/index.html) uses the B annotated
reference design, with source-authored bilingual concepts, definitions,
requirements, conditions and exceptions, plus actual repository filenames.
The bank is used only to check omissions. See its [scope and maintenance notes](study-notes/README.md).
The earlier [Part 6 sample URL](part6-sample/index.html) is retained as a historical sample.

新版[七部分溫習資料](study-notes/index.html)採用B批注式設計，從原文提煉概念、定義、
要求、條件及例外，保留雙語及實際檔名引用，題庫只作查漏；見[範圍及維護說明](study-notes/README.md)。
原第6部分樣章另作歷史樣本保留。以下是舊版歸檔說明。

The exam app now has two modes and uses documents 01–26. The separate older
revision pack is no longer built or attached to new releases.
Its generator, page sources and review tools are preserved byte-for-byte in
[the cleanup archive](../bank/audit/history/2026-10-18-before-repository-cleanup.zip).
Existing downloads remain at [v1.9.0](https://github.com/leohwlee/mso-ca/releases/tag/v1.9.0).

舊溫習資料的來源範圍與現行題庫不同，已退出日常建置及後續發佈。
原始程式、內容及覆核工具完整保存在上面的 ZIP；舊版本下載仍可使用。

[Source-conflict decisions](CONFLICT-CALLS.md) remain active authoring guidance.
For historical reproduction, extract the archive into a separate folder and run
`python revision/pack_build.py mso-revision-pack.html` there. The archive's original
`revision/README.md` describes its optional browser review tools.
Do not extract over the current checkout.

[Use the current app / 使用現行 App](../README.md)
