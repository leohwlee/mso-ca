# Archived revision pack / 已歸檔的舊溫習資料

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
