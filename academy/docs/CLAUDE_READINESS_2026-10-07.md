# Claude 接手檢查紀錄

日期：2026-10-07。檢查基線 main：`cc066a7bf1f9494abd9dc30a39f347d5963c1e6d`。

## 結論

原 repo 無法直接保證 Claude 在一般環境完成：deck 預設依賴 ChatGPT 專用 artifact-tool 與 Presentations skill；附檔建置仍綁定 L003；缺少 Claude 入口及跨環境預檢。
本次補齊後，具有終端、Python 3.11+、ffmpeg、LibreOffice、Poppler、網路及持久輸出能力的 Claude 可依指南製作 L004 及使用者指定後續課次。
一般只有文字對話／repo 讀取的介面仍不具備端到端製片能力。

## 修補與實測

| 項目 | 結果 |
|---|---|
| 課表及狀態 | 192 堂、576 搜尋入口完整；下一堂 L004，未更動正式課次狀態 |
| 共用素材 | 原片頭分段成功還原並核對 SHA-256；原角色、字型及 L001 還原 PPTX 都在 repo |
| 安裝 | 真正建立新 .venv，setup-portable.sh 安裝依賴並成功完成 preflight |
| 單元／整合測試 | `.venv` 下 16/16 通過；含原 10 項與新 6 項 |
| 可攜簡報 | 實際經 portable-runtime + academy run deck 產生原生可編輯 PPTX；原圖二進位一致、精確文字替換、notes 含旁白 |
| 渲染 | LibreOffice 讀取最終 PPTX，12 張 PNG 均為 1920×1080；檢視聯絡表確認中文字及品牌有正常顯示 |
| 附檔 | 使用既有 L003 公開音訊及時序作測試 fixture，通用 delivery 產生章節、說明、講稿、教材 ZIP 與純旁白 MP3 |
| 防錯 | 未命中映射／換行數改變／占位稿會失敗；教材變動改變指紋；缺必要交付檔，即使技術 PASS 也拒絕封裝 |
| 媒體驗收 | 保留原 23 項並新增 PPTX 原生文字及 notes 與旁白一致性，共 25 項；本次未宣稱新課成片 25/25 |
| 接續 | CLAUDE.md、可攜指南、L004–L006 指令、逐集保存／停止／恢復規則齊備 |

測試資料只放 `.build-portable-smoke/`，沒有當成 L004 教材、影片或正式驗收。
未重製／重傳 L001–L003、SP01，沒有啟動後续批次。授權範圍由使用者貼出的啟動指令決定。
未實際登入或運行 Claude 帳號，未重新連線合成 TTS，也未全片人工聽審。TTS 服務網路與配額、目標平台依賴安裝、每集內容與渲染品質，必須在實際製作環境確認。

重跑：`./setup-portable.sh`、`./portable-runtime.sh python pipeline/preflight.py`、`./portable-runtime.sh python -m unittest discover -s tests -v`。
本次封裝指紋新增 classroom 範圍；若重新封裝歷史課次，需重新驗收，不拿舊指紋冒充本次結果。
