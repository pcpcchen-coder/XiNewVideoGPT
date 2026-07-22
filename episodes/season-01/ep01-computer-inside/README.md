# EP01《電腦裡面有什麼？》完整重製版

這一版不再沿用第一版的十幕旁白與白底教材，而是以「跟著一筆資料旅行」為主線，重新製作劇本、TTS、PPT、教學視覺、動畫、字幕與音樂；陳犀牛仍是全片固定講師。

## 教學進程

1. 電腦不是黑盒子。
2. 五個單元的資料主線。
3. 電腦＝資料廚房。
4. 輸入與輸出。
5. CPU 的取得、理解、執行循環。
6. RAM 的暫時工作空間。
7. SSD 的長期保存。
8. 主機板的資料道路。
9. GPU、電源與散熱。
10. 一次按鍵的完整資料旅程。
11. 相同架構如何縮進手機。
12. 情境題與下一集鉤子。

## 交付內容

- `production/presentation/ep01-computer-inside.pptx`：12 頁 16:9 可編輯簡報，含 12 頁講者備註。
- `production/narration.json`：12 幕、36 句全新劇本。
- `production/timing.json`：依 TTS 實際音長產生的句級時間碼。
- `audio/slide_01.mp3` 至 `slide_12.mp3`：全新離線中文 TTS。
- `music/data-kitchen-loop.wav`：32 秒原創科技氛圍循環。
- `output/ep01-computer-inside-master.mp4`：動畫、旁白與音樂母帶。
- `output/ep01-computer-inside-zh-TW.mp4`：燒入繁中字幕的主交付。
- `output/thumbnail.jpg`：1280×720 封面。
- `qc/contact-sheet.jpg`：12 幕總覽。
- `qc/report.md`：18 項驗收結果。

## 影音規格

| 項目 | 規格 |
|---|---|
| 片長 | 425.73 秒 |
| 畫面 | 1920×1080、H.264、30 fps |
| 聲音 | AAC、48 kHz、雙聲道、-16.0 LUFS |
| 字幕 | zh-TW、36 段、燒入版＋獨立 SRT |
| 動畫 | 微推鏡、掃描光、六種輪替轉場 |
| 音樂 | 原創、80 BPM、旁白 sidechain ducking |

舊版來源投影片與 ASR 紀錄移至 `archive/v1-first-cut/`，保留可追溯性但不再參與新版產線。
