> **父子科技學院 L001–L192（2026-09-29 更新）**：請從 [academy/README.md](academy/README.md) 與 [雲端接續入口](academy/CLOUD_START_HERE.md) 開始。L003 已製作並保留驗收資料；後續採「雲端製作、使用者自行上傳」。以下為原 EP 系列紀錄，與學院課號／製作規格分開管理。

# XiNewVideoGPT

以 **陳犀牛 Chen XiNew** 為固定講師的 AI 教學影片製作倉庫。專案融合 [`video-production-skill-kimi`](https://github.com/pcpcchen-coder/video-production-skill-kimi) 的影片製作方法，與 [`XiNewIPs`](https://github.com/pcpcchen-coder/XiNewIPs) 的角色／品牌設定，建立可延伸的完整製作線。

## 第二集：為什麼電腦只懂 0 和 1？

- 講師：陳犀牛 Chen XiNew；沿用第一集的深海藍、探索橙與 12 幕教學結構。
- 內容：從兩種可靠狀態、電晶體、bit／byte 與二進位卡，延伸到文字、圖片、聲音如何編碼。
- 語音：全片固定使用 Microsoft Edge TTS `zh-TW-YunJheNeural`，36 句皆有實際音檔時間碼與 SHA-256。
- 片頭：以五幕 XiNew IP／課程視覺，接上指定 `30Sec.m4a` 來源檔的完整內容（媒體實長 1:00）。
- 正片：4:09；含片頭總長 5:09。1920×1080、H.264、AAC 48 kHz、繁中燒錄字幕。
- 教學音訊：投影片講解過程只保留 Edge-TTS 旁白，不使用背景音樂。
- PPT：12 頁可編輯簡報，逐頁含三句講者備註與來源。
- 驗收：23 項自動檢查全數通過；包含穩定畫格差異檢查，整片 decode 零錯誤。

主要交付：

- [繁中字幕成品](episodes/season-01/ep02-binary-data/output/ep02-binary-data-zh-TW.mp4)
- [無字幕母帶](episodes/season-01/ep02-binary-data/output/ep02-binary-data-master.mp4)
- [無片頭課程版](episodes/season-01/ep02-binary-data/output/ep02-binary-data-lesson.mp4)
- [可編輯 PPTX](episodes/season-01/ep02-binary-data/production/presentation/ep02-binary-data.pptx)
- [完整劇本](episodes/season-01/ep02-binary-data/production/narration.json)
- [YouTube 封面](episodes/season-01/ep02-binary-data/output/thumbnail.jpg)
- [驗收報告](episodes/season-01/ep02-binary-data/qc/report.md)

## 第一集完整重製成果

- 主題：跟著一筆資料，理解電腦的五大基本單元。
- 對象：七年級學生與親子共學。
- 講師：陳犀牛 Chen XiNew。
- 片長：7 分 06 秒，共 12 幕。
- 規格：1920×1080、H.264、AAC 48 kHz、繁中字幕。
- 劇本：全新 12 幕腳本、36 個句級字幕段落。
- 語音：全片重新以離線中文 TTS 合成，具可重建 manifest 與時間碼。
- PPT：12 頁 16:9 可編輯簡報，每頁含完整講者備註。
- 視覺：六組新教學插圖、四種 XiNew 角色姿勢、IP 品牌舞台。
- 動態：逐幕微推鏡、掃描光與六種輪替轉場。
- 音樂：原創 80 BPM《Data Kitchen》科技氛圍配樂，旁白期間自動 ducking。
- 驗收：18 項自動檢查全部通過；整體音量 -16.0 LUFS，decode 零錯誤。

主要交付：

- [繁中字幕成品](episodes/season-01/ep01-computer-inside/output/ep01-computer-inside-zh-TW.mp4)
- [無字幕母帶](episodes/season-01/ep01-computer-inside/output/ep01-computer-inside-master.mp4)
- [可編輯 PPTX](episodes/season-01/ep01-computer-inside/production/presentation/ep01-computer-inside.pptx)
- [完整劇本](episodes/season-01/ep01-computer-inside/production/narration.json)
- [YouTube 封面](episodes/season-01/ep01-computer-inside/output/thumbnail.jpg)
- [驗收報告](episodes/season-01/ep01-computer-inside/qc/report.md)
- [人工視聽檢查](episodes/season-01/ep01-computer-inside/qc/manual-review.md)

## 倉庫結構

```text
XiNewVideoGPT/
├── assets/
│   ├── characters/                  # IP 設定與四種透明講師姿勢
│   ├── fonts/                       # Noto Sans CJK TC 與授權
│   └── xinew-brand-identity.png
├── docs/                            # 製作架構與工具替代策略
├── episodes/
│   └── season-01/ep01-computer-inside/
│       ├── production/
│       │   ├── manifest.json        # 集數、TTS、音樂、轉場與輸出規格
│       │   ├── narration.json       # 12 幕／36 句完整劇本
│       │   ├── slides.json          # PPT 可見文案
│       │   ├── storyboard.json      # 教學目的、視覺與動作
│       │   ├── timing.json          # 實際 TTS 句級時間碼
│       │   ├── tts-manifest.json    # 引擎、參數、音檔雜湊
│       │   └── presentation/        # 可編輯 PPTX
│       ├── assets/
│       │   ├── visuals/             # 六組新教學視覺
│       │   └── slides/              # 12 張 1920×1080 影片畫面
│       ├── audio/                   # 12 段全新 TTS
│       ├── music/                   # 原創背景音樂與說明
│       ├── subtitles/               # 來源與最終 SRT
│       ├── output/                  # 母帶、字幕版、封面
│       ├── qc/                      # 自動報告與 contact sheet
│       └── archive/v1-first-cut/    # 第一版可追溯素材
├── pipeline/scripts/                # TTS、音樂、渲染、合成、驗收
├── Makefile
├── package.json
└── requirements.txt
```

## 一鍵重製影音

需求：Node.js 20+、Python 3.10+、Pillow、Edge-TTS、FFmpeg、FFprobe。

```bash
make install
make all             # 預設重製第二集
```

個別執行：

```bash
make tts         # 以 manifest 指定的 Edge-TTS 聲線重建旁白與句級時間碼
make tts-offline # 第一集舊版離線 TTS 相容入口
make music       # 以 FFmpeg 振盪器重建本集原創背景循環
make render      # 從 12 張投影片建立封面與 contact sheet
make assemble    # 穩定畫面、平滑淡化、片頭蒙太奇與字幕燒入
make verify      # PPT、語音、片頭、字幕、編碼、尺寸、decode 完整檢查
```

PPTX 與 12 張投影片 PNG 為已驗證的創作原件並直接提交。更新簡報內容時，同步修改 `production/slides.json`、PPTX 與 `assets/slides/`，再執行 `make assemble verify`。

## 後續影片放置規則

每支影片固定使用：

```text
episodes/<season>/epNN-<slug>/
```

新集數至少準備：

1. `production/manifest.json`：集數、講師、姿勢、TTS、音樂與輸出規格。
2. `production/narration.json`：幕 → 句的旁白結構；可另填 TTS 專用發音。
3. `production/slides.json`：觀眾實際看見的低密度文案。
4. `production/storyboard.json`：每幕唯一教學任務、視覺與動作。
5. `production/presentation/*.pptx` 與 `assets/slides/slide_NN.png`。
6. `audio/`、`music/`、`subtitles/`、`output/` 與 `qc/`。

驗收門檻：幕數與備註一致、1920×1080、H.264/AAC 48 kHz、字幕可讀、音量適合網路影片、全片可 decode、成品小於 GitHub 單檔限制。

## 素材與來源

- 第一版的教材與製作方法參考 `video-production-skill-kimi`，完整重製版的劇本、語音、PPT 內容、教學視覺、動畫時間軸與音樂皆重新製作。
- 角色外觀與品牌規則取自 `XiNewIPs`；四種講師姿勢以 IP 設定圖作為嚴格參考生成，再以 chroma key 去背。
- 六組電腦教學視覺以 OpenAI 圖像生成製作，不含品牌標誌或生成文字。
- 第一集背景音樂由專案腳本程式化合成；第二集教學段落不使用背景音樂。
- 繁中文字型為 Noto Sans CJK TC；授權資訊見 [Google Noto CJK](https://github.com/notofonts/noto-cjk)。
