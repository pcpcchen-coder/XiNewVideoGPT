> 歷史移交紀錄；現行雲端流程請以 academy/docs/CLOUD_PRODUCTION_GUIDE.md 為準。

# XiNewVideoGPT 附件盤點

盤點日期：2026-09-22。依據實際解壓檔案與原對話，不依早期 README 推測附件版本。

## 來源與版本

原對話的 `/mnt/data/XiNewVideoGPT.zip` 在本機不存在。同名原始附件位於 `~/Downloads/Kimi_Agent_继续制作下一集/XiNewVideoGPT.zip`，SHA-256 為 `29a70fff81eb9e214bb59b743767cb3ccf7a8d8bea92ed6f4ab265dee005f69f`。ZIP 有 113 筆 entry；排除目錄、macOS resource fork 與 `.DS_Store` 後保留 79 個實際來源檔。解壓工作副本還原了未標 UTF-8 的中文檔名，並檢查解壓路徑不超出目標資料夾。

`work/XiNewVideoGPT` 是另外一份乾淨 Git checkout，HEAD `fb3da36`，主要含 EP01、EP02。它與附件不同；沒有拿它取代附件。附件沒有根 README、Makefile、requirements 或 Git 歷史，主要入口是 `開集SOP.md` 與 EP10 README。SOP 列出 EP01–EP10 進度，但附件只含 EP10；不能據此宣稱已取得全部十集資產。

## 原始目錄

```text
XiNewVideoGPT/
├── 開集SOP.md
├── assets/
│   ├── opening/開場影片-v2.mp4
│   ├── characters/                 四種透明姿勢、主視覺、三視圖
│   ├── fonts/                     Noto Sans CJK TC、OFL
│   └── xinew-brand-identity.png
├── episodes/season-01/ep10-ai-and-our-future/
│   ├── production/                manifest、slides、narration、storyboard、plan
│   │   └── presentation/          可編輯 PPTX
│   ├── assets/visuals/            六張本集插圖
│   ├── assets/slides/             slide-XX、slide_XX 兩套名稱
│   ├── audio/                     十二段旁白
│   ├── music/                     歷史配樂與主題曲音檔
│   ├── subtitles/                 零基準 SRT、含片頭偏移 SRT
│   ├── output/                    母帶、燒字幕版、封面、contact sheet
│   └── qc/                        原有驗收與人工檢視紀錄
└── pipeline/scripts/              五支 EP10 專用腳本
```

EP10 README 的 `assets/audio/` 與實際 `audio/` 不一致，以實際檔案及腳本為準。

## 腳本與資料流

| 模組 | 真正做的事 | 重用方式與限制 |
|---|---|---|
| `generate_visuals_ep10.py` | Pillow 畫六張「AI 未來」插圖 | 具體圖解與 Linux 字型路徑寫死；保留為 EP10 原件，不自動套入其他課 |
| `build_deck_ep10.py` | python-pptx 生成 12 頁 PPT、逐句講者備註 | 色彩、版面、角色可重用；頁次決定版型，插圖檔名寫死，未內建來源追溯 |
| 外部匯出步驟 | LibreOffice 轉 PDF，pdftoppm 轉 PNG | 附件只有 SOP 說明，沒有一支完整匯出入口；本次補入 render 階段 |
| `synthesize_narration_ep10.py` | 每句 Edge TTS、暖聲處理、逐幕合併與 loudnorm | 呼叫缺失的 `/app/.agents/.../tts-converter.js`；原 manifest 的 speed/pitch 數值並未傳给 converter |
| `assemble_episode_ep10.py` | 開場影片＋12 靜態場景、fade、旁白串接、响度處理、字幕燒入 | 片頭路徑、集數、暫存目錄、偏移寫死；只看暫存檔存在就跳過，改稿後可能用舊素材 |
| `verify_episode_ep10.py` | 18 項結構與影音檢查 | 失敗仍以 0 結束；只對母帶完整 decode；母帶與字幕版大小不同不能嚴格證明字幕正確 |

實際入口是「已完成企劃／劇本／投影片 JSON」，沒有錄音、ASR、課程 Excel 匯入與 YouTube 上傳功能。`tts-manifest.json` 記錄音檔雜湊，但原驗收未重算比對。原成品的 18/18 歷史報告本次已重新執行驗證，詳見 validation.md。

## 風格應以新版附件為準

- 12 幕 × 3 句，繁體中文，陳犀牛主講。兩小時課堂可拆成多支此規格短片。
- 藏青漸層 `#041222 → #071F37`；橘 `#FFC12F`、藍 `#1982C4`、青 `#46C8FF`、白 `#F7F7F8`、灰 `#A8B8C9`、面板 `#101B28`。
- 頁首 CHEN XiNew、集數／頁次、頁尾 XINEW SAYS；PPT 沿用主題字型。字幕使用 repo 的 Noto Sans CJK TC。
- 靜態鏡頭、0.55 秒 fade。保留原本色彩微調與暗角，不導入早期版本的推鏡、掃描光或教學背景音樂。
- 聲線 `zh-TW-YunJheNeural`，正片只有旁白，主題曲只在開場。逐幕 −18 LUFS、全片目標 −16 LUFS。這是兩階段處理，不等同有量測參數回填的 two-pass loudnorm。
- 正式片頭實測 60.266667 秒。原始素材的「Stay Curius」拼字依 SOP 保留，不擅自重做品牌片頭。
- 固定結尾：「我是陳犀牛，保持好奇，我們下次見！」。SOP 說揮手，但实际 EP10 manifest 使用 `open-palms`，附件也無獨立 wave 素材；沿用已有姿勢並標記差異。
- SOP 的字幕安全區文字有歧義：新稿應以實際字幕版畫面覆核，不能只靠像素描述自動判定安全。

## 依賴與可重用模組

核心 Python 套件為 Pillow、python-pptx、lxml（python-pptx 的依賴）、Edge-TTS。影音需要 FFmpeg/FFprobe；PPT 匯出需要 LibreOffice 與 Poppler。原先 Node 只服務外部 TTS converter；新增版直接呼叫 Python Edge-TTS，不再依賴舊 `/app` 路徑。

新增 openpyxl 只讀取 Excel，不存回檔案；原格式、驗證清單與條件格式不受影響。可選 faster-whisper 接本地模型，或匯入既有轉錄器的 SRT／segments JSON。沒有為這次工作下載模型或上傳家庭錄音。

旁邊 `video-production-skill-kimi` 的流程是另一個接口：slides_prompts、config、ASR words、JS assemble/burn 與 44.1 kHz。它可提供未來語音複核思路，但不能直接接本系列 48 kHz＋句級 timing 契約。早期 XiNew repo 的 Pillow 字幕備援是獨立模組，本次沿用它處理 macOS FFmpeg 缺 libass 的情況；字幕樣式與速度仍須另驗收。

## 課程來源確認

使用者 Downloads 中 V2 原 Excel 有 8 張工作表：使用說明、4年路線圖、逐堂課程、教學紀錄、儀表板、資源庫、內容製作流程、YouTube教材庫。實際逐堂課程 192 筆（29 欄），教材庫 576 筆（15 欄），每課 3 筆。不是先前構想中的 15 張表或 576 支已人工精選影片。

第一課是「開學任務：把 MacBook 變成我的工作站」，與 XiNew EP01 及本附件 EP10 不同。採用 L001–L192 課次識別碼與獨立 episodePaths 對照；不推斷現有十集對應哪十堂課。
