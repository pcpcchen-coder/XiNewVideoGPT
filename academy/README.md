# 父子科技學院｜雲端製作到 L192

**Claude 接手（2026-10-07）：** 先讀 [跨環境製作指南](docs/CLAUDE_HANDOFF.md)；已提供無 ChatGPT 專用依賴的套版與交付入口。[三集啟動指令](docs/CLAUDE_BATCH_PROMPT.md)可直接交給 Claude。
**目前分工：雲端製作影片、簡報、教材與上傳資料；George 自己上傳 YouTube。**
這個 `academy/` 是獨立製作根目錄，保留原系列角色、片頭與版型。根目錄 EP 系列是早期作品，課號與流程不可混用。

| 要做的事 | 入口 |
|---|---|
| 新對話接手 | [CLOUD_START_HERE.md](CLOUD_START_HERE.md) |
| 每集製作與環境設定 | [雲端製作教學](docs/CLOUD_PRODUCTION_GUIDE.md) |
| 了解這次轉移、L003 與 502 | [遷移及第三集紀錄](docs/MIGRATION_AND_L003.md) |
| 找程式、素材、成片與雜湊 | [檔案清單](docs/FILE_MANIFEST.md) |
| 看 192 堂主題與目標 | [完整課程索引](CLOUD_CURRICULUM_INDEX.md) |
| 看每集製作／發布進度 | [192 堂狀態表](docs/PRODUCTION_STATUS.md) |
| 啟動下一集 | [可複用指令模板](docs/NEXT_EPISODE_PROMPT.md) |
| 自己上傳 YouTube | [上傳教學](docs/MANUAL_YOUTUBE_UPLOAD.md) |
| 本次整合驗證 | [驗證紀錄](docs/VALIDATION_2026-09-29.md) |

## 現況

- L001、L002：移交文字記錄為已公開；本次未重新驗證影片／版權或重傳。
- L003「鍵盤忍者：快捷鍵競速」：成片及 23/23 技術檢查記錄已保存；本次核對原成品雜湊一致，已另行由本機上傳並公開，最新發布紀錄見 CLOUD_START_HERE.md。
<!-- academy-status:list -->
- L004「網路到底是什麼：封包接力賽」：2026-10-07 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L004-v1 已交付；尚未上傳。紀錄見 [delivery.json](episodes/academy/l004-network-relay/delivery.json)、[manual-review.md](episodes/academy/l004-network-relay/qc/manual-review.md)。
- L005「搜尋高手：把大問題拆成好問題」：2026-10-07 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L005-v1 已交付；已發布：[YouTube](https://youtu.be/_vZlGoif3vs)。紀錄見 [delivery.json](episodes/academy/l005-search-master/delivery.json)、[manual-review.md](episodes/academy/l005-search-master/qc/manual-review.md)。
- L006「真真假假：來源與證據偵探」：2026-10-07 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L006-v1 已交付；已發布：[YouTube](https://youtu.be/C5Aw2U88q10)。紀錄見 [delivery.json](episodes/academy/l006-source-evidence/delivery.json)、[manual-review.md](episodes/academy/l006-source-evidence/qc/manual-review.md)。
- L007「密碼城堡與雙重驗證」：2026-10-07 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L007-v1 已交付；已發布：[YouTube](https://youtu.be/5S83wW8ojAk)。紀錄見 [delivery.json](episodes/academy/l007-password-castle/delivery.json)、[manual-review.md](episodes/academy/l007-password-castle/qc/manual-review.md)。
- L008「釣魚郵件偵探社」：2026-10-07 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L008-v1 已交付；已發布：[YouTube](https://youtu.be/tZOsZSzrc34)。紀錄見 [delivery.json](episodes/academy/l008-phishing-detectives/delivery.json)、[manual-review.md](episodes/academy/l008-phishing-detectives/qc/manual-review.md)。
- L009「個資、照片與數位足跡」：2026-10-07 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L009-v1 已交付；已發布：[YouTube](https://youtu.be/YxGX5Ax6YVs)。紀錄見 [delivery.json](episodes/academy/l009-digital-footprint/delivery.json)、[manual-review.md](episodes/academy/l009-digital-footprint/qc/manual-review.md)。
- L010「AI 是什麼、不是什麼」：2026-10-07 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L010-v1 已交付；尚未上傳。紀錄見 [delivery.json](episodes/academy/l010-what-is-ai/delivery.json)、[manual-review.md](episodes/academy/l010-what-is-ai/qc/manual-review.md)。
- L011「第一個好提示詞：任務、背景、限制、格式」：2026-10-08 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L011-v1 已交付；尚未上傳。紀錄見 [delivery.json](episodes/academy/l011-first-good-prompt/delivery.json)、[manual-review.md](episodes/academy/l011-first-good-prompt/qc/manual-review.md)。
- L012「AI 會亂講：幻覺抓錯賽」：2026-10-08 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L012-v1 已交付；尚未上傳。紀錄見 [delivery.json](episodes/academy/l012-ai-hallucination/delivery.json)、[manual-review.md](episodes/academy/l012-ai-hallucination/qc/manual-review.md)。
- L013「文字、圖片、聲音 AI 體驗站」：2026-10-08 由 Claude 以可攜流程製作，verify 25/25、逐頁與逐段檢視完成，L013-v1 已交付；尚未上傳。紀錄見 [delivery.json](episodes/academy/l013-multimodal-stations/delivery.json)、[manual-review.md](episodes/academy/l013-multimodal-stations/qc/manual-review.md)。
- L014–L192：課表與製作骨架可接續，並非影片已完成，也沒有啟動批次製作。
- 下一堂 L014「我們家的科技公約」。
<!-- /academy-status:list -->
- 192 堂共 576 組 YouTube 搜尋入口；沒有把它們標成已精選的 576 支影片。

```sh
cd academy
./cloud-runtime.sh python pipeline/academy.py doctor
./cloud-runtime.sh python pipeline/status.py --next
./cloud-runtime.sh python -m unittest discover -s tests -v
```

共用片頭（分段保存，啟動時自動原樣還原）、角色、字型、還原模板、課表、L003 原稿／音訊／字幕／投影片及 QC 隨 Git 保存。L003 的兩支大型影片與純旁白 MP3 從已保存接續包還原，見檔案清單。歷史原稿與雜湊另存，不能把歷史報告當成本次執行證據。
