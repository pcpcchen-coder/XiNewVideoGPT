# SP002 來源筆記：FamilyRecorder

查核日：2026-10-17。來源：公開 repo `pcpcchen-coder/FamilyRecorder`，main 分支 commit `ff76063`
（2026-10-03，「Recover microphone capture after USB disconnects (#10)」）。製作代理（Claude）自己 clone 並逐檔閱讀，
沒有派研究子代理。沒有安裝或執行這個專案，沒有接麥克風實測；以下全部是「文件與程式碼寫了什麼」，不是實機觀察。

## 讀過的檔案

README.md、docs/use-cases.md、docs/privacy.md、docs/speakers.md、docs/getting-started.md、docs/menu-bar.md、
docs/daily-summary.md、docs/architecture.md（部分）、CHANGELOG.md（開頭）、config.example.yaml、pyproject.toml，
以及原始碼 src/family_recorder/summary.py、config.py、cli.py、history.py（開頭）、scripts/install_mac.sh、
packaging/FamilyRecorderUninstaller.swift、menubar/FamilyRecorderMenuBar.swift（以關鍵字查找）。

## 事實與出處

| # | 事實 | 出處 |
|---|---|---|
| 1 | 定位：在 Apple Silicon Mac 上常駐的聲音日誌系統，接 XVF3800 USB 麥克風陣列，持續聆聽、本機辨識，每天固定時間整理成 Markdown 摘要 | README「這是什麼」 |
| 2 | 標語：「家裡的一句叮嚀、課後的一段講解、半夜醒來記得的那個夢 —— 它們只存在幾秒鐘，然後就消失了」 | README 開頭 |
| 3 | 需求：Apple Silicon（arm64）、macOS 13 以上；reSpeaker XVF3800 USB 4-Mic Array；要每日摘要需要可用 Codex 的 ChatGPT 帳號，不需要 API key | README「你需要準備」；docs/getting-started.md |
| 4 | 每段 30 秒（`audio.chunk_seconds: 30`） | config.example.yaml；README「連續 30 秒 chunk」 |
| 5 | 融合語音閘門：RMS、WebRTC VAD、硬體 Speech Energy；判定安靜的片段不建立 WAV、不呼叫 Whisper，只留低容量數值遙測 | README 系統總覽；docs/privacy.md「安靜意味著什麼」 |
| 6 | 本機辨識用 whisper.cpp（安裝腳本預設 v1.8.1），Apple Silicon 開啟 Metal | README 核心功能；scripts/install_mac.sh 第 22 行 |
| 7 | 每日摘要預設 00:10 執行，整理前一天（`summary.hour: 0`、`minute: 10`） | config.example.yaml；docs/use-cases.md 場景一 |
| 8 | 摘要透過官方 Codex CLI 與 ChatGPT 登入，每天只送逐字稿文字；可把 `summary.enabled` 設為 false，整套變成完全離線 | README 隱私承諾；docs/privacy.md「一句話總結」 |
| 9 | 每次呼叫 Codex 用 `--ephemeral`、`--sandbox read-only`、暫存工作目錄、忽略使用者設定與規則；逐字稿走 stdin | src/family_recorder/summary.py 第 344–370 行；docs/privacy.md |
| 10 | 摘要程式沒有讀取或上傳音訊的實作：summary.py 只 import config、history、storage；history.py 自述 no audio, network or summary-client access | summary.py import 區；history.py 第 3 行。docs/privacy.md 寫「只 import config 與 storage」「515 行」，與目前程式（多 import history、522 行）略有出入，影片不引用行數 |
| 11 | 原始 WAV、聲音特徵、DoA 與 Speech Energy、SQLite、被攔截文字都不離開這台 Mac | README 隱私承諾表；docs/privacy.md |
| 12 | 防幻覺：硬體靜音否決、自適應噪音基線、低頻／窄頻固定音、Whisper 信心與無語音機率、壓縮率、跨段相似句；不封鎖任何特定句子；攔截決策寫入稽核表 `transcription_audits` | README 核心功能；config.example.yaml 註解「deterministic Whisper text on silence or steady noise … do not blacklist any particular sentence」；docs/privacy.md |
| 13 | 家庭成員最多 8 位（config.py 第 376 行），每人錄 15 秒樣本（cli `--seconds` 預設 15；docs/speakers.md）；錄音樣本丟棄，只留本機聲音特徵 | config.py；cli.py 第 163 行；config.example.yaml 註解「The enrollment WAV is discarded」 |
| 14 | 方向：XVF3800 回報 DoA 角度；音色與方向是兩份獨立證據並列，不互相取代；方向不是身分或距離 | docs/speakers.md |
| 15 | 逐字稿標示「可能說話者」而非確認身分；不能用於門禁、付款、家長監控、證據 | README「產出長什麼樣」；docs/speakers.md；docs/privacy.md 明確禁止的用途 |
| 16 | 逐字稿範例：「19:40:07–19:40:12 — 可能：家人二（87%）— 方向：左側 92°」「明天記得去拿包裹，九點前要出門。」；摘要範例把它放進事件時間軸與待辦事項 | README「產出長什麼樣」 |
| 17 | 摘要內容包含事件時間軸、待辦事項、100 字內今日摘要等；行事曆候選事件預設逐筆確認，可改成一次同意後自動加入；`calendar.enabled` 預設 false | config.example.yaml prompt；docs/daily-summary.md 第 224、239 行 |
| 18 | 「當下記錄器」：換掉摘要 prompt 就能變成家教課後複習、夢境與靈感記錄；家庭聲音日誌是完整實作，其餘「今天就能用，換掉摘要 prompt 即可」 | README「它可以拿來做什麼」；docs/use-cases.md |
| 19 | 不提供隱蔽錄音；不適用於門禁、付款、家長監控；使用前取得所有可能被錄音者的明確同意，清楚標示正在收音 | README IMPORTANT 區塊；docs/privacy.md |
| 20 | 文件附自我驗證指令（例如用 sqlite3 確認安靜時沒有產生 WAV） | docs/privacy.md「如何自己驗證」 |
| 21 | 選單列可暫停 15 分鐘、1 小時或直到手動恢復 | docs/menu-bar.md 第 42 行 |
| 22 | 解除安裝器先停止服務，再把選定內容移到垃圾桶 | packaging/FamilyRecorderUninstaller.swift 第 58、112 行 |
| 23 | MIT 授權 | LICENSE；README |
| 24 | 版本：pyproject.toml 是 0.16.0；README「專案狀態」仍寫 0.14.4。影片與教材不提版本號 | pyproject.toml 第 7 行；README |
| 25 | 「一台永遠開著麥克風的電腦，值不值得信任，取決於『什麼資料去了哪裡』能不能被驗證，而不是被承諾」 | docs/privacy.md 開頭 |

## 刻意不說的

- 不說誰寫了每一行程式；只說這是爸爸（repo 擁有者）在 GitHub 上公開的開源專案。
- 不說它「保證」不外流：文件自己列出不防護的威脅（能存取這台 Mac 的人、備份、送到 ChatGPT 後的文字）。
- 不說辨識或人別準確率；文件沒有給數字，也說錯認仍可能發生。
- 不示範任何真實錄音、逐字稿或家人資料；畫面上的例句是 README 的範例。
