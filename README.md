# XiNewVideoGPT

以 **陳犀牛 Chen XiNew** 為固定講師的 AI 教學影片製作倉庫。第一個里程碑，是融合 [`video-production-skill-kimi`](https://github.com/pcpcchen-coder/video-production-skill-kimi) 的十步影片產線，與 [`XiNewIPs`](https://github.com/pcpcchen-coder/XiNewIPs) 的角色／品牌設定，重製第一集《電腦裡面有什麼？》。

## 第一集成果

- 主題：電腦的五大基本單元與廚房比喻
- 對象：七年級學生
- 講師：陳犀牛 Chen XiNew
- 規格：1920×1080、H.264/AAC、繁中字幕、十幕
- 特色：四種一致角色姿勢、IP 色彩系統、科技教室舞台、字幕安全區、逐幕微動態
- 成品：[`episodes/season-01/ep01-computer-inside/output/ep01-computer-inside-zh-TW.mp4`](episodes/season-01/ep01-computer-inside/output/ep01-computer-inside-zh-TW.mp4)
- 封面：[`episodes/season-01/ep01-computer-inside/output/thumbnail.jpg`](episodes/season-01/ep01-computer-inside/output/thumbnail.jpg)
- 驗收：[`episodes/season-01/ep01-computer-inside/qc/report.md`](episodes/season-01/ep01-computer-inside/qc/report.md)

## 倉庫結構

```text
XiNewVideoGPT/
├── assets/
│   ├── characters/                  # 角色設定、可重用透明講師姿勢
│   ├── fonts/                       # 繁中字幕字型
│   └── xinew-brand-identity.png     # IP 品牌色與標誌參考
├── docs/
│   ├── architecture.md              # 產線、檔案責任與資料流
│   └── toolchain-fallbacks.md       # 缺工具時的替代策略
├── episodes/
│   └── season-01/
│       └── ep01-computer-inside/
│           ├── README.md
│           ├── production/          # 計畫、旁白、分鏡、來源投影片、manifest
│           ├── assets/slides/       # 品牌化後逐幕畫面
│           ├── audio/               # 每幕語音
│           ├── subtitles/           # 可上傳 YouTube 的 SRT
│           ├── output/              # 最終影片與封面
│           └── qc/                  # ASR 與影音驗收報告
├── pipeline/
│   ├── scripts/                     # 渲染、組裝、驗收
│   └── templates/                   # 後續集數範本
├── Makefile
└── requirements.txt
```

## 一鍵重製

需求：Python 3.10+、Pillow、FFmpeg、FFprobe。

```bash
python3 -m pip install -r requirements.txt
make all
```

個別執行：

```bash
make render      # 產生十張品牌化投影片、封面與 contact sheet
make assemble    # 合成影片並燒入繁中字幕
make verify      # 數量、透明度、編碼、解析度、decode test
```

## 後續影片放置規則

每支影片固定使用：

```text
episodes/<season>/epNN-<slug>/
```

新增一集時，複製 `pipeline/templates/episode/`，至少準備：

1. `production/manifest.json`：集數、標題、講師姿勢分配、輸出規格。
2. `production/narration.json`：一幕一段旁白。
3. `production/storyboard.json`：每幕的教學目的與視覺錨點。
4. `production/source_slides/slide_NN.png`：無講師的教學底圖。
5. `audio/slide_NN.mp3`：與旁白一一對應的配音。
6. `subtitles/zh-TW.srt`：最終字幕。

驗收門檻：幕數一致、1920×1080、H.264/AAC、字幕可讀、全片可 decode、成品小於 GitHub 單檔限制。

## 素材與來源

- 課程腳本、原始投影片、配音與字幕取自 `video-production-skill-kimi` 第一集，重製版保留已驗證的教學內容與 ASR 結果。
- 角色外觀與品牌規則取自 `XiNewIPs`。
- 新增的四種講師姿勢以 IP 設定圖作為嚴格參考生成，再以 chroma key 去背。
- 繁中文字型為 Noto Sans CJK TC；授權資訊見 [Google Noto CJK](https://github.com/notofonts/noto-cjk)。

