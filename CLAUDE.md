# Claude 接手 XiNewVideoGPT

此 repo 的父子科技學院工作根目錄是 `academy/`。
先讀 `AGENTS.md`、`academy/AGENTS.md`、`academy/series-policy.json`，再讀
`academy/docs/CLAUDE_HANDOFF.md`。Claude 可用的入口是 `academy/portable-runtime.sh`。

- 一般 Claude 環境沒有 ChatGPT 專用 artifact-tool。使用明確選定的 `ooxml-template`，不安裝來路不明的同名套件。
- 此路線保留已追蹤 L001 還原模板的原生文字、圖片及版型，以 LibreOffice 渲染最終 PPTX。
- 先完成 preflight，再做使用者指定的課次。不要將初始化占位稿交付為成品。
- 只有 repo 存取而沒有終端、Python、ffmpeg、LibreOffice、持久檔案輸出的聊天環境，不能完成端到端製片；使用 Claude Code 或具上述能力的工作環境。
- L001–L003 和 SP01 已有發布紀錄，不重製、不重傳。<!-- academy-status:sentence -->L004–L012 已由 Claude 製作並交付（verified／awaiting_user_upload，尚未上傳），不重製；下一堂是 L013「文字、圖片、聲音 AI 體驗站」，接手仍讀狀態表。<!-- /academy-status:sentence -->
- 允許按使用者明確給定範圍逐集做完；沒有指定停止課號就先做本次指定課，不自行跑到 L192。
- 每集完成後保存、驗收、記錄並 commit，再進下一集。額度或工具中斷時寫本課 HANDOFF.md；不要假裝能讀取使用者剩餘額度。
- 預設只交付，YouTube 由 George 上傳。舊集上傳授權不延伸至新集。
