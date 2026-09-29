> 歷史快照：不代表目前授權或操作入口。現行規則見 ../../series-policy.json。

# 父子科技學院：逐集製作與公開流程

本工作副本保存 192 堂課程與 576 組 YouTube 搜尋入口。課次依課表的 L001–L192 識別，不能拿舊系列 EP02 等名稱代替。每次只製作使用者指定課次。

## 固定教學與品牌

每週 120 分鐘：開場 10、示範 15、共同實作 40、休息 10、獨立改造 30、孩子教爸爸 10、錄音整理 5 分鐘。爸爸 Mac mini，孩子 MacBook Air。主軸為 AI、寫 code、科技與生活技能。

沿用陳犀牛角色、CHEN XiNew 深藍/黃/青配色、既有開場影片 v2、Edge-TTS `zh-TW-YunJheNeural`、靜態畫面和平滑淡化。教學段落不加背景音樂。不要自行加入推拉鏡頭或改角色。

## 輸入與內容

1. 先核對 `curriculum` 與 `lessons/Lxxx/lesson.json` 的主題、學習目標、課堂任務。
2. 有課堂錄音時放入課次的 private 區，轉成附時間與講者的逐字稿；人工訂正後才改寫公開旁白。保留來源與編修紀錄，不上傳原始私人錄音。
3. 沒有錄音時，依課表製作課前教學版並明說；不得宣稱是真實授課紀錄。
4. 編寫 12 頁簡報、每頁 3 句旁白、實作提示、120 分鐘安排、作品與驗收條件。操作指引查官方來源，寫入事實核對檔及簡報備註。
5. 若影片提到練習教材，教材必須真的存在並驗證可用；不要在 YouTube 說明放不存在的下載連結。

## 可重複執行命令

在此 repo 根目錄執行。`.venv` 使用 bundled Python，避免系統 Python 的 Xcode 授權阻擋。Node、Node modules、Presentations skill 的路徑由當次 `load_workspace_dependencies` 確認。

```sh
.venv/bin/python pipeline/academy.py init L002
.venv/bin/python pipeline/academy.py new-episode L002 --slug l002-file-treasure
# 填寫 production 的 manifest、slides、narration、storyboard、sources、template-text
.venv/bin/python pipeline/academy.py run validate --episode episodes/academy/l002-file-treasure
.venv/bin/python pipeline/academy.py run deck --episode episodes/academy/l002-file-treasure
.venv/bin/python pipeline/academy.py run tts --episode episodes/academy/l002-file-treasure
.venv/bin/python pipeline/academy.py run assemble --episode episodes/academy/l002-file-treasure
# 完成說明、章節、練習包、純旁白等附加輸出後才 verify
.venv/bin/python pipeline/academy.py run verify --episode episodes/academy/l002-file-treasure
.venv/bin/python pipeline/academy.py package --episode episodes/academy/l002-file-treasure --output delivery/L002-v1
```

`deck` 使用 `RUNTIME_NODE`、`RUNTIME_NODE_MODULES`、`PRESENTATIONS_SKILL`。新課次設定 `deckRenderer: artifact-tool-template`，`templateEpisode` 指向 L001，`seriesHeader` 設定本課英文副標；`template-text.json` 用逐頁舊字/新字映射保留實際原稿的圖形、樣式和版面。跨段落文字必須逐段替換，腳本會再次查驗每段新文字，避免模板舊文字靜默殘留。不同段落數要先調整版面，不可忽略錯誤。

每次 PPT 製作依 Presentations skill 執行操作標記、封裝/幾何檢查、最終重新匯入與逐頁輸出，再人工看完所有頁面。保留可編輯文字與圖形。

## 驗收與封裝

- 12 頁內容與旁白相符，字體無裁切、無模板殘留；字幕不得蓋住主要內容。
- 36 句旁白與 SRT 文字/時間一致，片頭偏移用這次組裝後的實測長度。
- 1080p、30 fps、H.264、AAC 48 kHz 雙聲道；母帶與成片全檔可解碼；音量目標 -16 LUFS，容許 -18 到 -14。
- 靜態畫面差異檢查；ffmpeg vignette 使用 `dither=0`，避免畫面隨時間閃動。
- 本機 ffmpeg 無 libass 時，使用 Pillow 字幕覆蓋；快取每個字幕區段，保留中文字体與換行檢查。
- 生成無字幕母帶、繁中字幕成片、SRT、PPTX、旁白 MP3、封面、章節、來源、練習包及 QC 報告。
- `verify` 保存輸入雜湊；`package` 只收白名單。驗收後任何 production/audio/subtitles/output/slides 更動都必須重新驗收，不能跳過雜湊檢查。
- 自動檢查不能取代內容與畫面檢查，也不代表 YouTube 版權檢查已通過。

## YouTube 公開發布

頻道：犀牛說，`UCLAQhbdu5MFIDoUPH6bDQuQ`。登入使用者自己的 Chrome YouTube Studio，透過 CUA 的檔案選擇器上傳已驗證字幕成片，不索取密碼或 OAuth token。

1. 上傳前比對檔名、課次與 SHA-256，避免重複上傳或上傳舊系列影片。
2. 填入 `父子科技學院 Lxxx｜課程主題`、說明與章節。一般版以國中生與家長為受眾；受眾設定須依實際內容，不以角色可愛與否判定。
3. 在「影片元素 → 字幕 → 新增」上傳 `zh-TW.srt`，選包含時間碼；確認中文（台灣）及「由你提供」後儲存。字幕已燒入的版本可供不開 CC 者觀看，額外字幕軌供搜尋、無障礙與翻譯；開啟 CC 可能重疊。

3. 本次 L002 使用者已明確要求「直接上傳與公開」。後續依各次授權決定公開方式；本機草稿保守設私人，不代表線上發布狀態。
4. 自訂縮圖若要求手機驗證，使用者須自行完成；可先採 YouTube 自動縮圖完成已授權的公開，不要因此把影片留在草稿。
5. 頁面顯示上傳/處理狀態後前進，設定「公開」並發布。必須看到「影片已發布」及影片網址，才可宣稱公開完成。
6. 寫入 `publication/youtube-receipt.json`：影片網址、ID、頻道、公開狀態、實際上傳檔案雜湊、觀察到的版權檢查結果和縮圖方式。未知結果明說未知。
7. 若 Chrome 報告無法選檔，依工具的檔案上傳故障說明讓使用者啟用必要的擴充功能檔案存取；不可自行繞過安全設定。權限已存在時直接沿用。

目前是可重複的本機製作流程加已登入瀏覽器發布，並非無人值守的 YouTube API 排程器。沒有取得新錄音、授權或可用登入時，保留具體成果與阻擋原因。

發布收據存放在各 episode 的 publication 目錄。L001 公開網址：https://youtu.be/JrYLz3D-7p4 。

L002 公開網址：https://youtu.be/soztdVd9Xys 。2026-09-22 已確認「影片已發布」，當時著作權檢查顯示未發現問題；字幕軌已儲存。
