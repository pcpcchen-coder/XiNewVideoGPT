# 使用者自行上傳 YouTube

適用：父子科技學院 L001–L192。2026-09-29 起由使用者操作登入及最後公開；雲端代理準備完整交付包。

## 上傳前取用檔案

| 用途 | 交付檔 |
|---|---|
| 主要上傳影片 | `lxxx-slug-zh-TW.mp4` |
| 可選母帶 | `lxxx-slug-master.mp4`，未燒字幕但仍含簡報文字與原片頭 |
| 字幕軌 | `zh-TW.srt`，已包含本集片頭偏移 |
| 縮圖 | `thumbnail.png` |
| 標題、說明、章節 | `youtube-metadata.json`、`youtube-description.txt`、`chapters.txt` |
| 教材與簡報 | `classroom.zip`、`lxxx-slug.pptx` |
| 核對檔案 | `checksums.json`、QC 報告 |

先播放成片，確認課號、開頭、結尾、音量與字幕。L003 成片 SHA-256：
`fabc3fc9d865e6ca92a3d85cdaff7c1a4bba4ca24f8b38e31fbee7bcf286271c`。
macOS 可用 `shasum -a 256 檔案路徑`；Windows PowerShell 可用 `Get-FileHash -Algorithm SHA256 檔案路徑`。

## 上傳操作

1. 在自己的瀏覽器登入 [YouTube Studio](https://studio.youtube.com/)，確認頻道「犀牛說」及頻道 ID `UCLAQhbdu5MFIDoUPH6bDQuQ`。
2. 「建立 → 上傳影片」，選本集字幕成片。先查看內容清單，避免重複上傳。
3. 貼入 `youtube-metadata.json` 的 title 及 `youtube-description.txt`。L003 標題為「父子科技學院 L003｜鍵盤忍者：快捷鍵競速」。
4. 上傳 `thumbnail.png`（若頻道功能未開通，依 YouTube 提示處理或選自動縮圖）。依本片實際受眾判斷是否兒童專屬；L003 的內容定位是國中生與家長，不僅依卡通角色判斷。
5. 在字幕區選中文（台灣），上傳 `zh-TW.srt`，選「包含時間碼」，預覽後儲存。不要用沒有片頭偏移的 `zh-TW-source.srt`。
6. 檢查說明中的章節、來源及教材連結；沒有公開下載位置就不填虛構網址。章節從 00:00 起，至少三段且每段至少 10 秒，是否顯示也受頻道功能條件影響。
7. 等待處理，查看 YouTube 顯示的版權／限制結果。技術 QC 不等於平台版權審查。
8. 選擇需要的公開方式並儲存／發布，確認完成訊息及可開啟的影片 URL。僅完成上傳、仍為私人／草稿，不等於公開完成。
9. 把 URL 回傳給 ChatGPT，附上是否公開、字幕／縮圖方式、平台檢查結果；未知項目寫未知。

字幕已燒入成片；再開啟 CC 可能重疊。額外 SRT 軌仍可供無障礙、搜尋及翻譯使用。
`youtube-draft.json` 的 private 是本機封裝器的保守草稿設定，不會控制線上影片狀態。

## 官方參考（2026-09-29 核對）

- [電腦上傳影片](https://support.google.com/youtube/answer/57407)
- [新增字幕](https://support.google.com/youtube/answer/2734796)
- [影片章節](https://support.google.com/youtube/answer/9884579)
- [判斷是否為兒童專屬內容](https://support.google.com/youtube/answer/9528076)

YouTube Data API 是可選的未來方案，不是本次依賴。新未審核 API 專案有私人影片限制，不能假定啟用 API 就能自動公開：[官方 videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert)。
