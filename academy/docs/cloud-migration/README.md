> 歷史移交紀錄；現行雲端流程請以 academy/docs/CLOUD_PRODUCTION_GUIDE.md 為準。

# 2026-09-27 雲端移植紀錄

## 實際收到的接續包

Academy_Cloud_Handoff_2026-09-27_v2.zip：111,390,770 bytes。
SHA-256：19dbae0281da9b9f22b9f32aa7cc2ea1bcba3ab8b8f06f9850d67016f8cd1541。
這是 v2，不使用先前 v1 的大小或 SHA-256。

解壓後 51 個內容檔案，包含 SHA256SUMS.json。其餘 50 個檔案均符合清單的雜湊與大小。
清單共列 201 個檔案，其中 151 個未包含於這次 ZIP，整體判定 PARTIAL，不能聲稱完整通過。
缺少整個 episodes 目錄，包括原 L001 PPTX、L001/L002 成品、旁白及 publication 收據。
保留原 ZIP 與解壓來源不變；本工作副本另外製作。

## 已確認

- curriculum/catalog.json 有 L001–L192 的主題與學習目標；576 組資源為搜尋入口。
- 角色、品牌、片頭 v2、繁中文字體與製作腳本可讀，現有檔案 SHA-256 一致。
- 原 build_l001.mjs 直接建構可編輯文字與圖形。其 EP10 reference 只用於診斷，沒有參與版面建構。
- 移除對缺少的 EP10 reference 的診斷匯入，以原程式及原素材還原 L001 版型，產出專供 L003 套版的模板。
- 原 L001 旁白未取得；還原模板備註明說缺少。L003 的 36 句與來源已完整改寫至最終簡報備註。
- 雲端 artifact-tool 的 inspect 回傳 slideIndex/position，因此加上轉換層，保留原逐段替換與殘留文字檢查。
- TTS 沿用 zh-TW-YunJheNeural，加入系統 CA 信任根，保留 TLS 憑證驗證。
- 雲端使用現有 Python/Node/ffmpeg/font 與專案依賴，沒有沿用 Mac 的 .venv 或 /Users 路徑。

## 證據邊界

還原模板不是原始 L001 PPTX 實體檔案，雜湊不宣稱一致。L001/L002 本機 QC 與發布紀錄仍屬使用者提供的歷史資訊。
L003 的 qc 另行記錄本次實際檢查結果。技術與畫面檢查不代表 YouTube 版權審查。
沒有取得課堂錄音，不聲稱取得逐字稿；L003 明確標示課前教學版。
此工作只製作已授權 L003，不重製或重傳 L001/L002，不自動製作其他課次。
YouTube 發布需要當次可用登入，不能承接原 Mac Chrome 登入。

雲端 ffmpeg 具備 libass，原 MarginV/左右邊界造成字幕遮蓋內容，已改為 FontSize=16、MarginV=20、MarginL/R=24。全部 36 句以實際 libass 渲染量測，字幕範圍 y=892–1007，位於教學內容下方。另限制 decoder/encoder 執行緒，以符合 8 GiB 環境；不改動畫面或轉場流程。

額外音軌比對發現 MP3 容器時長與解碼後時長每幕約差 0.036 秒，12 幕累積約 0.38 秒。組裝器現於串接前以 apad/atrim 對齊各幕宣告時長，母帶與字幕版音軌同步更新，影片畫面保持 stream copy。字幕仍按本次實測片頭與 timing.json 計算，修復後重新 verify。

音量先量測再決定增益。當固定增益可同時保留峰值餘裕並落在使用者允許的 -18 至 -14 LUFS 範圍時，優先保留原片頭波形；否則使用帶量測參數的雙遍 loudnorm。這避免動態正規化改變原片頭相對音量形狀。逐幕暖聲與 -18 LUFS 的原 TTS 處理保持不變。量測與實際參數保存在 qc/loudness-normalization.json。
