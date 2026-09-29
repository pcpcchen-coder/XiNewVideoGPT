# 父子科技學院 × XiNewVideoGPT

以 2026-09-22 找到的使用者附件 `XiNewVideoGPT.zip` 為來源，建立獨立工作副本。保留附件第十集的全部原始檔案與五支 `*_ep10.py` 腳本。新增的課程工具與可攜腳本放在旁邊，不覆寫來源 ZIP、Excel、早期 Git repo 或專案 `sources/`。

- [結構盤點](docs/repository-audit.md)：附件實際內容、流程、風格、依賴與問題。
- [整合與操作手冊](docs/pipeline-integration.md)：每週教學、目錄、命令、驗收、遷移與限制。
- [本次驗證](docs/validation.md)：已驗證範圍與尚未驗證項目。
- [來源檔案與 SHA-256](docs/archive-inventory.json)。

新增工具：`pipeline/academy.py`。現有課程已完整匯入 `curriculum/catalog.json`，第一堂的教學工作資料夾位於 `lessons/L001/`。所有 576 個連結仍是搜尋入口，尚未聲稱是 576 支已挑選影片。

```sh
python3 pipeline/academy.py doctor
python3 pipeline/academy.py --help
python3 -m unittest discover -s tests -v
```

既有 EP10 可走 `validate → media-check → verify → package`；新課程先取得真實錄音／逐字稿並完成教材編輯，再走 `deck → render → tts → assemble → verify → package`。`package` 只產生本機發布草稿，不會上傳 YouTube。

此版本提供可執行的課程銜接與影音工具，但不把自動辨識、教材事實查核與人工視聽驗收包裝成無人值守的一鍵完成。詳見操作手冊。
