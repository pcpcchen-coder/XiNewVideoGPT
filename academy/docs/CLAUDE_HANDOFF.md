# Claude 製作接手指南

更新：2026-10-07。適用 Claude Code，或具有終端、檔案系統、網路及影音工具的 Claude 工作環境。
此 repo 能提供素材及流程；不能替一般純聊天介面增加 ffmpeg 或執行權限。

## 1. 先核對目前狀態

從最新 `main` 接手。先讀根目錄 CLAUDE.md、AGENTS.md、academy/AGENTS.md、series-policy.json、CLOUD_START_HERE.md。
L004「網路到底是什麼：封包接力賽」是本次下一課。L005 是搜尋技巧、L006 是來源與證據。
SP01 是番外篇，不佔課號。L003 已公開的最新紀錄以 publication 為準。
不需要 ChatGPT Library 登入、不需要舊集大型母帶，也不需要 Google OAuth 就能製作新課。

## 2. 安裝可攜環境

建議 Linux 或 macOS，Windows 用 WSL2。不要複製別的平台 .venv。

```sh
# Debian/Ubuntu，需有系統套件安裝權限；已安裝者跳過
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip ffmpeg libreoffice-impress poppler-utils fontconfig
# Python 必須 3.11+，不足時由環境管理者提供。
```

macOS 可使用現有 Homebrew：`brew install python@3.12 ffmpeg poppler fontconfig`、`brew install --cask libreoffice`。
確保 `soffice` 在 PATH（通常位於 `/Applications/LibreOffice.app/Contents/MacOS/soffice`）。
將 `academy/assets/fonts/NotoSansCJKtc-Regular.otf` 安裝到 `~/Library/Fonts/`，讓 LibreOffice 也能使用；Linux setup 會安裝至使用者 fontconfig 目錄。

```sh
cd academy
./setup-portable.sh
./portable-runtime.sh python pipeline/preflight.py
./portable-runtime.sh python pipeline/status.py --next
./portable-runtime.sh python -m unittest discover -s tests -v
```

setup 建立 .venv、裝 requirements、還原並驗證原片頭。preflight **失敗時 exit 1**，會指出缺字型、軟體或 ffmpeg filter。
不需要 Node、`@oai/artifact-tool`、Presentations skill 或 CODEX 環境變數。
若當前代理提供 Presentations skill，先讀該 skill；本 repo 明確授權無該 skill 的 Claude 使用 OOXML 套版流程，不代表任意改版。
若 Python 套件下載被封鎖，保留阻擋紀錄，請環境提供者安裝，不關閉 TLS。
預留至少 5 GB 可用空間供每集暫存，完成後將大型成品移至持久目錄。

## 3. 初始化與編輯契約

```sh
./portable-runtime.sh python pipeline/academy.py init L004
./portable-runtime.sh python pipeline/academy.py new-episode L004 --slug l004-network-relay --renderer ooxml-template
```

已存在則接續，不重建、不刪除。初始化僅占位稿，驗證應失敗。
若接手已初始化的 artifact-tool-template 草稿，可將本課 manifest 的 deckRenderer 明確設成 ooxml-template，記錄變更，重新建置及驗收。

依 `curriculum/catalog.json` 和 `lessons/L004/lesson.json` 寫：

| 檔案 | 要求 |
|---|---|
| narration.json | 12 幕 × 3 句，繁中，逐幕 sources，指定結尾。可用 tts 欄位標註易誤唸詞，字幕仍用 text |
| slides.json、storyboard.json | 1–12 連續頁碼、真實文案、教學目的、圖解與活動一致 |
| template-text.json | old 是 L001 模板的精確文字，每筆 new 完整改成本課，保留換行／段落數；不得沿用前課教學字句 |
| sources.json、fact-check.md | 原始／官方來源、查核日、與哪個主張對應、限制；YouTube 搜尋入口不能冒充已觀看影片 |
| plan.md | 課表目標、120 分鐘安排、作品、驗收與孩子教爸爸 |
| classroom/ | 實際可用的練習／起始素材、作答紀錄、答案與驗收；禁止私人素材 |
| delivery-summary.md | 本課公開說明、課前教學版揭露、教材用法、來源網址與注意事項，delivery.py 原樣採用 |
| manifest.json | 課號、主題、12 頁、原聲線、無教學 BGM、autoPublish=false；內容完成才設 editorialStatus=authored |

12 頁可按：開場目標、概念、例子、示範、活動規則、共同實作、錯誤修正、比較、獨立改造、作品驗收、120 分鐘安排、回顧結尾。
以本課需要調整。模板圖形只是起點；不適合的圖解不能硬套，需明確另製可編輯版面並重新驗收。
L004 備課重點：封包／路由器／IP／DNS／伺服器各自職責、封包接力實作、亂序／遺失情境；不要將「所有封包必走同一路線」或「所有網路協定都保證送達」當成事實。
不預寫假來源查核，也不把本文件當成完整 L004 教案。

## 4. 逐階段製作

以下命令均在 academy/；EP 是當次實際 episode 路徑。

```sh
EP=episodes/academy/l004-network-relay
./portable-runtime.sh python pipeline/academy.py run validate --episode "$EP"
./portable-runtime.sh python pipeline/academy.py run deck --episode "$EP"
# 此時檢視最終 PPTX 重新渲染出的 12 張 assets/slides PNG，逐頁修正
./portable-runtime.sh python pipeline/academy.py run tts --episode "$EP"
./portable-runtime.sh python pipeline/academy.py run media-check --episode "$EP"
./portable-runtime.sh python pipeline/academy.py run assemble --episode "$EP"
./portable-runtime.sh python pipeline/delivery.py --episode "$EP"
# 完成視聽檢查，寫 qc/manual-review.md 後才進下列步驟
./portable-runtime.sh python pipeline/academy.py run verify --episode "$EP"
./portable-runtime.sh python pipeline/academy.py package --episode "$EP" --output delivery/L004-v1
```

TTS 將公開講稿送到 Microsoft Edge TTS，需要該執行環境允許的網路及本次製作授權。SP01 的舊同意只屬 SP01，不拿來冒充未來課次同意；本次啟動 prompt 可明確包含授權。
不需另買 LLM API：Claude 負責撰稿、改檔和呼叫工具。Edge TTS 可用性不是 repo 能保證的；失敗保留稿件及錯誤，不擅換聲線。
目前 tts 重跑會重建本課音訊，未提供逐句持久快取；成功後不要無故重跑。

portable deck 保留原 PPTX 媒體與文字樣式、寫入本課 notes，LibreOffice 將**最終 PPTX** 渲染為 12 張 1920×1080 PNG。
結構驗證不能證明沒有溢字或視覺錯誤，必須逐頁看圖。長句放不下時先精簡，不能略過渲染。

## 5. 驗收與真正交付

- verify 保留原有 23 項媒體檢查，新增 PPTX 原生可編輯文字與 36 句 notes 一致性檢查，共 25 項：片頭、音訊、句級字幕、全檔解碼、30 fps、音量、靜態畫面等。
- 另逐頁核對文字／圖解／notes／旁白；檢查所有字幕，音畫同步至少前中後段，音訊專有名詞抽聽。manual-review 寫檢查方法、發現、修正與限制，未聽完不可宣稱全片聽審。
- package 必須有事實查核、講稿、章節、說明、教材 ZIP、純旁白與人工／代理檢視記錄；未齊全就拒絕。
- 修改 production/audio/subtitles/output/assets/slides/classroom 任一內容後必須重驗。教材修改先重跑 delivery，再 verify。
- package 產生版本化資料夾與 checksums.json。壓縮為 ZIP，放在使用者能持久取得的位置。Claude Code 可交付本機絕對路徑；遠端環境須提供真實下載，不得杜撰 URL。
- 大型 MP4 不進 Git。記錄檔名、bytes、SHA-256、版本、持久取得方法於本課 delivery.json。
- 保存成功後更新 production-status.json 對應課為 verified / awaiting_user_upload、episodePath、evidence，再跑 status.py --write。不要變動其他課狀態。
- commit 本課來源、教材、腳本、QC／交接、狀態與 delivery.json；排除 .venv、暫存、錄音、憑證和大型成品。以 git diff 檢查後 push。

## 6. 批次範圍與中斷接續

只按使用者指定起訖課號順序完成。每集保存＋驗收＋commit 後才能進下一集，避免額度中斷造成多集半成品。
不存在「把帳號剩餘額度用完」的可讀取 API 承諾；到指定末課、出現配額／網路阻擋或無法完成驗收時停止並交接，不背景循環。
下次先讀本課 HANDOFF.md，核對輸入雜湊、git 狀態和實際檔案，再接續缺失階段。

HANDOFF.md 必須含：lessonId、episodePath、最後成功階段、當前 commit、已保存成品及 SHA-256、待辦／阻擋、下條可執行命令、是否需要重驗。不要記 token／cookie。
參考 [可直接貼入的批次指令](CLAUDE_BATCH_PROMPT.md)。
