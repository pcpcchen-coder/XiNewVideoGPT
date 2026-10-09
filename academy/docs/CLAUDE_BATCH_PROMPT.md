# 貼給 Claude 的逐集製作指令

以下示範 L004–L006，共三集。George 可把停止課號改成希望的範圍。
<!-- academy-status:sentence -->L004、L010–L013 已由 Claude 製作並交付（verified／awaiting_user_upload，尚未上傳），不重製；下一堂是 L014「我們家的科技公約」，接手仍讀狀態表。 L005–L009 已發布，影片網址及觀察證據見狀態表，不重複上傳。<!-- /academy-status:sentence -->
再次使用時請把起始課號改成下一堂，並同步修改不重製的清單。
此文件是待使用者貼出的指令模板，本身不啟動背景製作，也不宣稱已取得未來課次 TTS 授權。

```text
請接手 https://github.com/pcpcchen-coder/XiNewVideoGPT 最新 main。
本次依序製作父子科技學院 L004、L005、L006，完成 L006 後停止。
先讀 CLAUDE.md、AGENTS.md、academy/AGENTS.md、academy/series-policy.json、
academy/CLOUD_START_HERE.md 和 academy/docs/CLAUDE_HANDOFF.md。

請直接執行製作，不要只給計畫。先跑 preflight 和狀態檢查，
從已存在且可驗證的成果接續；未開始者才初始化。
使用 portable-runtime.sh 和 ooxml-template 保留原系列可編輯模板。
每集內容依 catalog 核對，沒有錄音就製作明確標示的課前教學版。
維持 12 頁／36 句、原片頭 v2、陳犀牛、深藍黃青、指定聲線，
教學畫面靜態加淡化，無背景音樂與推拉鏡頭。

本次同意將這三集的公開旁白稿送到 Microsoft Edge TTS，
以 zh-TW-YunJheNeural 合成；不傳送私人錄音或其他私人資料。
不使用付費 LLM API，不自動購買額度。

每集完成內容與教材、官方來源查核、PPTX 與逐頁 QA、配音／字幕、
影片、delivery、verify、版本化 package、持久保存及 repo commit 後，
才進入下一集。不要只改上一集標題，不可沿用前集音訊或 QC。
請逐頁及逐段檢視並如實記錄方法與限制，未完成不得標 verified。

交付字幕 MP4、無字幕母帶、SRT、可編輯 PPTX、純旁白 MP3、
講稿、封面、章節說明、來源、可用教材、QC、SHA-256 和接續來源。
大型檔保存於持久可下載位置；程式、教材、文字來源、驗收與
delivery.json、狀態表 commit 並 push 回 repo。
YouTube 由我上傳，不登入、不上傳、不公開，也不重製 L001–L003 或 SP01。

若遇額度限制或真正阻擋，保存已完成資料並寫本課 HANDOFF.md，
附最後成功階段、SHA-256、阻擋與下一條命令；不要無限重試。
先做好可完成的部分。不要聲稱能讀取我的帳號剩餘額度。
```

中斷後只需補充：

```text
請接續上次 L004–L006 任務，先 pull 最新 repo 並讀對應 HANDOFF.md。
核對已保存成果與指紋，從第一個未完成或失效階段繼續。
已完成且未改動的課不重製，範圍仍到 L006，YouTube 仍由我上傳。
```
