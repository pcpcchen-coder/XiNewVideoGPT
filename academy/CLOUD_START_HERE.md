# 新工作階段從這裡接手

**L003 最新例外：** 使用者於 2026-09-29 20:35（台北）要求改用本機接手上傳。處理本集發布時，先讀 [本機交接](docs/LOCAL_UPLOAD_L003.md) 與 [本次請求](publication/L003-local-upload-request.json)；下方自行上傳規則仍為其他課次預設。尚未確認本機連線或平台上傳完成。

更新：2026-09-29。先讀 [AGENTS.md](AGENTS.md) 與 [series-policy.json](series-policy.json)。

**雲端完成製作及交付；使用者負責 YouTube 上傳。** 此決定取代 9/27 manifest 與舊 SOP 的代理自動公開設定。不要重試 Google 登入，也不要把上傳作為製作成功的前提。

1. 以此 repo 的最新版本為起點，進入 `academy/`；不要在根目錄執行學院命令。
2. 讀 [製作教學](docs/CLOUD_PRODUCTION_GUIDE.md)、[進度表](docs/PRODUCTION_STATUS.md)。
3. 共用片頭已分段保存在 Git；啟動器首次執行時自動還原並核對 SHA-256。跑 `./cloud-runtime.sh python pipeline/academy.py doctor`，查當次 Node、artifact-tool、Presentations skill、中文字型、ffmpeg 與 Edge-TTS。
4. 跑 `./cloud-runtime.sh python pipeline/status.py --next`。目前應是 L004，仍須依使用者指定課次工作。
5. 核對課表，初始化草稿，編寫 12 頁／36 句、教材、來源、驗收，再逐階段製作。
6. 通過驗收後封裝、保存可下載檔案，更新製作進度與檔案清單。將影片留為 `awaiting_user_upload`。

## 已知檔案與限制

- 原始完整 v1 ZIP 未成功讀取；實際接手的 v2 ZIP 缺 151 個清單檔案。
- L001 的可編輯模板是從原建置程式及角色還原，不能宣稱與原始 PPTX 相同。
- 已保存的 `Academy_Cloud_Handoff_2026-09-27_L003.zip` 有 171 個內容檔案（含清單），170 個列檔皆已驗證。
- `pipeline/academy.py new-episode` 已改用隨 repo 保存的學院 seed，不再依賴缺少的 EP10。
- L003 大型輸出可由接續 ZIP 還原；`restore_handoff_media.py` 驗證整包及各檔雜湊，拒絕覆寫被修改的輸出。
- 歷史 QC 保存原驗收證據；程式或成品改變後必須產生新的驗收，不得改舊雜湊冒充相同版本。

後續每次「做下一集」可貼 [指令模板](docs/NEXT_EPISODE_PROMPT.md)。
