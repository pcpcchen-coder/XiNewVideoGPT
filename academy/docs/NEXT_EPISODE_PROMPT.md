# 交給下一個工作階段的指令

先確認 `curriculum/production-status.json`，填入實際指定的課號。以下課號只是範例（<!-- academy-status:sentence -->L004–L008 已由 Claude 製作並交付（verified／awaiting_user_upload，尚未上傳），不重製；下一堂是 L009「個資、照片與數位足跡」，接手仍讀狀態表。<!-- /academy-status:sentence -->）；課程內容來自 catalog，不從上一集猜測。

```text
請接手 https://github.com/pcpcchen-coder/XiNewVideoGPT 的父子科技學院。
先讀根目錄 AGENTS.md、academy/AGENTS.md、academy/CLOUD_START_HERE.md、
academy/docs/CLOUD_PRODUCTION_GUIDE.md、academy/curriculum/production-status.json。

這次只製作 L004「網路到底是什麼：封包接力賽」。
從 academy/curriculum/catalog.json 核對學習目標、兩小時安排、作品與驗收。
沒有新錄音，請製作明確標示的課前教學版，不捏造逐字稿。

沿用陳犀牛角色、原片頭 v2、深藍／黃／青配色、
zh-TW-YunJheNeural、12 頁可編輯 PPT、每頁 3 句旁白，
教學段落靜態畫面加淡化、不加背景音樂或推拉鏡頭。
核對官方操作與事實來源，練習教材必須實際存在且可用。

請自行完成合理的例行實作與修正，並按階段回報：
內容／教材 → 簡報逐頁 QA → 配音／字幕 → 合成 → 驗收 → 交付。
缺依賴先檢查並處理；無法恢復時保存已完成成果與明確阻擋原因。
驗收後變更任何 production/audio/subtitles/output/assets/slides 都要重驗。

交付字幕 MP4、無字幕母帶、SRT、PPTX、純旁白 MP3、封面、
旁白稿、章節、說明、來源、練習包、QC、SHA-256 及可接續來源。
將程式、文字來源、製作紀錄、狀態表回寫 repo；大型檔保存並提供下載。
更新狀態為 verified / awaiting_user_upload。
YouTube 由我自行上傳；你不要登入、上傳、公開或設定 OAuth。
不要開始 L005，也不要重製或重傳 L001–L003。
```

## 中斷後接續

```text
請接續 Lxxx，先讀本集交接紀錄、production 與 qc。
列出已完成且可由雜湊確認的輸出，從缺失或失效階段恢復。
不要從頭重製未改動的內容，也不要沿用失效的 QC。
雲端交付後由我自行上傳 YouTube。
```

## 使用者上傳後回報

```text
我已上傳 Lxxx，影片網址是［貼上 YouTube URL］。
請將 URL 及我的回報記錄到該集 publication/status.json，
並更新 curriculum/production-status.json 與狀態表。
若你尚未實際確認公開狀態，標示 published_user_reported。
```
