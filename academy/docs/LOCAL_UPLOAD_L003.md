# L003：接到本機並完成 YouTube 上傳

> 最新結果（2026-09-29 21:20，台北）：L003 已由本機完成上傳及公開，唯一影片為 [nhWH6BQna5A](https://youtu.be/nhWH6BQna5A)。標題、說明、13 個章節時間戳、原縮圖與繁中 CC 均已保存並核對。**著作權檢查仍在進行且超出預期，未宣稱通過。後續只接續此影片，不得重新上傳。** 詳見[本機發布驗收](../episodes/academy/l003-keyboard-ninja/publication/local-upload-review.md)。下方為原始交接背景；歷史「尚未查看／未取得本機連線」描述已由本次觀測取代。

更新：2026-09-29 20:35（Asia/Taipei）。

## 本次指令與範圍

使用者表示人工上傳不完整，要求代理改用這台本機，接手上傳到 https://www.youtube.com/@xinew-says 。
此指令取代 L003 的「使用者自行上傳」分工，並延續先前完成第三集公開的要求。例外只適用 L003，不自動延伸到其他課次。

- 課程：L003「鍵盤忍者：快捷鍵競速」
- 頻道：犀牛說；預期 ID：`UCLAQhbdu5MFIDoUPH6bDQuQ`，必須在登入後的 Studio 再核對。
- 目標：以本機已登入的瀏覽器完成上傳、必要資訊、縮圖、字幕及公開驗收。
- 平台現況：尚未查看本機 Studio；不知道是否已有草稿、上傳中項目或公開影片。先檢查，再決定續做或新建。
- 本次雲端只完成連線盤點及交接，沒有轉成本機、沒有登入、沒有新上傳或公開。

## 接到本機工作階段

1. 在這台 Mac 的 ChatGPT 桌面 App 選擇 **Work locally／在本機工作**。若既有雲端對話沒有切換選項，開新 Work 對話，先選本機，再貼下方指令。
2. 選可操作本機 Chrome 的連線；需要檔案選擇器時，使用當次支援檔案上傳的瀏覽器能力或已核准的 Computer Use。桌面內建瀏覽器不一定支援自動上傳。
3. 開始時核對執行環境與瀏覽器清單。只有雲端 CDP 瀏覽器時，不得宣稱已接上 Mac。
4. 已登入就沿用；遇到登入或驗證流程，依當次登入能力交接給使用者完成。不要要求把密碼或驗證碼貼到對話，也不要匯出登入 cookie。
5. 本機切換與必要 App／OS 權限由使用者操作；不能透過雲端對話假設已切換，也不自動操作 ChatGPT 自己的介面。

## 本機接手指令

```text
請用這台 Mac 的本機 Work 接手父子科技學院 L003 上傳。
先確認本機瀏覽器／Computer Use 可用，使用已登入 YouTube 的本機 Chrome。

Repo：https://github.com/pcpcchen-coder/XiNewVideoGPT
先讀 academy/docs/LOCAL_UPLOAD_L003.md、
academy/publication/L003-local-upload-request.json、
academy/episodes/academy/l003-keyboard-ninja/production/youtube-metadata.json。

本次我已授權你接手第三集，完成上傳及公開到
https://www.youtube.com/@xinew-says（犀牛說）。
本次指令取代 L003 先前由我自行上傳的分工；其他集不在這次範圍。

先在 YouTube Studio 查找 L003／鍵盤忍者，核對頻道及既有影片。
若已有本集草稿或未完成上傳，先補齊，不要直接重複建立。
不要刪除既有影片；不能確認是否同一集時，保留並向我指出具體差異。
如果完全沒有本集，才使用雜湊符合的既有成片建立上傳。

從已保存檔案取回 l003-keyboard-ninja-zh-TW.mp4，
並從 repo 取得縮圖、zh-TW.srt、標題、說明及章節。
核對影片 SHA-256，沿用驗收過的成片，無須重新製作。

完成縮圖、繁中字幕、說明與章節，檢查平台處理／版權狀態後完成公開。
需要我登入或完成驗證時交給我，完成後繼續。
最後回報真實影片 URL、公開狀態、各欄位完成情形及平台限制，
並回寫 publication/status.json、192 集進度表與驗收紀錄。
```

## 需要的檔案

所有 repo 路徑以 `academy/episodes/academy/l003-keyboard-ninja/` 為基準。

| 用途 | 來源 |
|---|---|
| 成片 | 已保存的 `l003-keyboard-ninja-zh-TW.mp4`；先找本機或 ChatGPT Library 的同名檔 |
| 備援完整交接包 | 已保存的 `Academy_Cloud_Handoff_2026-09-27_L003.zip`；取回及還原方法見 [FILE_MANIFEST.md](FILE_MANIFEST.md) |
| 標題／欄位 | `production/youtube-metadata.json` |
| 完整說明與章節 | `production/youtube-description.txt`、`production/chapters.txt` |
| 縮圖 | `output/thumbnail.png` |
| 字幕 | `subtitles/zh-TW.srt`，已加片頭偏移；不要用 `zh-TW-source.srt` |
| 技術驗收 | `qc/report.json`、`qc/verified-inputs.json` |

成片：76,593,749 bytes，398.848 秒，1920×1080。
SHA-256：`fabc3fc9d865e6ca92a3d85cdaff7c1a4bba4ca24f8b38e31fbee7bcf286271c`。

```sh
shasum -a 256 /實際本機路徑/l003-keyboard-ninja-zh-TW.mp4
```

文字資料與縮圖已在 Git；影片不在 Git，須從已保存檔案取得。檔案傳到本機後，記錄實際本機路徑，不沿用雲端 /workspace 路徑。下載已有檔案不等於重新產生影片。

## 防止重複上傳與驗收

- 先查 Studio 的「內容」，以 L003／鍵盤忍者、標題、片長及預覽辨識本集；記下既有 video ID、狀態及缺項。
- 已有本集且影片完整：補齊中繼資料、縮圖、字幕及公開設定。
- 上傳仍可續傳：依 Studio 顯示續做；失敗且不能恢復時，先記錄狀態再建立新的上傳，保留舊項目，不自行刪除。
- 既有影片內容、片長或課號不符：不要覆寫／刪除；指出差異後再決定。
- 標題為「父子科技學院 L003｜鍵盤忍者：快捷鍵競速」。
- 使用已核對的 metadata，逐項核對實際受眾與介面欄位；不要只因角色是卡通就改受眾設定。
- 繁中字幕需含片頭時間，預覽前、中、後段；成片已有燒錄字幕，額外 CC 可能重疊。
- 章節已包含於說明；不得編造教材下載網址。
- 記錄 YouTube 實際顯示的處理與版權結果；不能把原 23/23 技術 QC 當成平台版權通過。
- 只有看到公開狀態、可開啟影片 URL，並完成必要欄位核對，才回報完成；仍在處理的項目要明列。

現有 `publication/status.json` 和進度表是先前交付時的紀錄，不是本次登入 Studio 後的觀測。此交接的新授權及等待狀態存於 `academy/publication/L003-local-upload-request.json`。本機接手後核對真實平台狀態，再同步更新原紀錄，不預填成功。

## 官方操作依據（2026-09-29 查閱）

- [選擇 Work locally](https://learn.chatgpt.com/docs/get-started-with-work)
- [本機與雲端工作邊界](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-local-security)
- [本機 Chrome 與 Computer Use](https://learn.chatgpt.com/use-cases/use-your-computer-with-codex)

本次實際連線盤點：只有雲端 Chrome／CDP 與空白頁，原生 App 清單為空，執行環境為 Linux；尚未取得這台 Mac 的操作連線。沒有提供可由代理呼叫的「將本對話切換成本機」功能。
