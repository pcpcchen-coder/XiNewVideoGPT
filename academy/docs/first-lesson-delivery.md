> 歷史移交紀錄；現行雲端流程請以 academy/docs/CLOUD_PRODUCTION_GUIDE.md 為準。

# 第一堂影片交付（2026-09-22）

已由課程表 L001 製作《把 MacBook 變成我的工作站》。原課表、192 堂／576 組教材入口保持原樣；本次影片完成不代表實際授課已完成，lesson.status 仍為 planned。

- 成片：388.138 秒，1920×1080，30fps，H.264／AAC 48kHz 立體聲。
- 12 頁原生可編輯簡報、36 句 Edge-TTS zh-TW-YunJheNeural 旁白、36 段全片字幕。
- 系列片頭、陳犀牛 IP、靜態畫面、0.55 秒淡化；教學段落無背景音樂。
- 23/23 技術檢查通過；12 幕字幕成片畫面抽查與簡報逐頁檢視完成。6 項既有 pipeline 測試通過。
- 全片音量 -17.6 LUFS。人工逐句聽審未計入自動檢查。
- 已產出本機 YouTube 標題、章節、說明草稿；沒有上傳。

交付目錄：delivery/L001-v1；壓縮檔：delivery/父子科技學院_L001_完整教材包.zip。

製作內容與重製命令：episodes/academy/l001-mac-workstation/README.md。

## 本次流程修正

1. 新增 L001 的原生簡報作者 pipeline/scripts/build_l001.mjs，使用 artifact-tool，從最終 PPTX 匯出場景圖片。
2. academy.py 支援 academy-native-v1，deck/render 導向 L001 作者；其他課須先建立各自內容版面。
3. 關閉 FFmpeg vignette 的 dither，避免逐格暗角雜訊；場景穩定性納入驗收。
4. 字幕繪圖快取每句透明圖層，逐像素比對與原繪法相同。
5. 字幕驗收使用轉碼後片頭的實測長度（60.277 秒），並檢查它和原片頭差異不超過一影格。
6. 封裝可攜帶作者編寫的 YouTube 章節與說明，附白名單教材檔案與 SHA-256。

來源 ZIP、sources/ 同步參考、舊 XiNewVideoGPT checkout 均未改寫。
