# 父子科技學院：雲端接續起點

接續日期：2026-09-27。此包移交已完成的課程製作專案；本次不開始第三集或重複上傳。

## 先讀
1. docs/production-and-publication-sop.md（最新流程）
2. curriculum/catalog.json 與原始 V2 Excel：192 堂、576 組搜尋入口。
3. lessons/L001/lesson.json、lessons/L002/lesson.json（已更新公開狀態）
4. episodes/academy/l002-file-treasure/publication/youtube-receipt.json。
5. docs/repository-audit.md、docs/pipeline-integration.md 與 pipeline/academy.py。

L001 公開網址：https://youtu.be/JrYLz3D-7p4
L002 公開網址：https://youtu.be/soztdVd9Xys
頻道：犀牛說，UCLAQhbdu5MFIDoUPH6bDQuQ。

本機原任務：(科技學院)整合 XiNewVideoGPT 課程製作流程。
雲端接續任務：父子科技學院｜雲端製作工作室。
前兩集實測驗收和發布是在 2026-09-22 完成；本包不代表雲端已重新跑通。

## 已打包
完整課表、SOP、可重用程式、字體及授權、陳犀牛角色、原片頭、前兩集可編輯 PPTX、旁白音訊、SRT、母帶、字幕成片、封面、尋寶練習包及 QC/發布紀錄。authoring/l002 留存一次性內容生成來源作參考。

省略：本機 .venv、機器快取、重複 delivery ZIP、舊 season-01 EP10 素材與私人資料。舊 EP10 專用腳本仍保留作架構參考，其素材不在本包。沒有搬移瀏覽器登入、憑證、ChatGPT 記憶或完整聊天逐字歷史；本檔與 SOP 保留必要工作脈絡。

## 課程與風格
每週 120 分鐘：開場10、示範15、共同實作40、休息10、獨立改造30、孩子教爸爸10、錄音整理5。孩子 MacBook Air，爸爸 Mac mini。AI、寫 code、科技、生活技能。沿用陳犀牛、深藍/黃/青、原片頭 v2、zh-TW-YunJheNeural、靜態畫面與平滑淡化、教學段落無背景音樂。
L002 是「檔案與資料夾尋寶」，不是舊系列二進位 EP02。無錄音時稱課前教學版。

## 雲端驗收
先解壓、核對 SHA256SUMS.json，再盤點 Python、Node、ffmpeg、ffprobe、artifact-tool、Presentations skill、中文字體及 Edge-TTS 網路。requirements.txt 不含 ffmpeg 及 artifact-tool；不要宣稱只 pip install 就能完整重製。
使用雲端實際執行環境路徑；設 RUNTIME_NODE、RUNTIME_NODE_MODULES、PRESENTATIONS_SKILL、XINEW_PYTHON。原 docs、manifest、收據內 /Users 路徑屬歷史記錄，必須依當前環境調整執行參數，不可假裝可讀本機。一次性 classroom.py 用 macOS textutil 驗證 RTF，雲端需等價檢查或沿用已打包練習檔。
可先跑 python pipeline/academy.py doctor 和 python -m unittest discover -s tests -v。不要為移交而重建影片。修改任何 production/audio/subtitles/output/slides 後須重新 verify 再 package。
新課以 L001 editable PPTX 為模板，逐段替換多行文字並檢查新文字存在；最終所有投影片均需視覺驗收。雲端若無 artifact-tool，明確列為待補依賴，不擅自降級成不可編輯截圖簡報。

YouTube 登入不隨雲端移交。未來發布必須依實際授權及可用登入執行，取得「影片已發布」與網址才算完成。前兩集已有公開網址，勿重複上傳。自訂縮圖曾受手機驗證限制。只做使用者指定課次。
