# Claude 製作接手指南

更新：2026-10-07。適用 Claude Code，或具有終端、檔案系統、網路及影音工具的 Claude 工作環境。
此 repo 能提供素材及流程；不能替一般純聊天介面增加 ffmpeg 或執行權限。

## 1. 先核對目前狀態

從最新 `main` 接手。先讀根目錄 CLAUDE.md、AGENTS.md、academy/AGENTS.md、series-policy.json、CLOUD_START_HERE.md。
<!-- academy-status:sentence -->L004、L012–L013 已由 Claude 製作並交付（verified／awaiting_user_upload，尚未上傳），不重製；下一堂是 L014「我們家的科技公約」，接手仍讀狀態表。 L005–L011 已發布，影片網址及觀察證據見狀態表，不重複上傳。<!-- /academy-status:sentence -->實作後的備註見第 7、8 節與各集 delivery.json。下方以 L004 為例的命令，換成實際課號與 slug 使用。
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

## 7. L004 實作後的環境備註（2026-10-07）

以下是第一次用本指南完整做完一集時實際遇到的事，下一集可直接避開。

- **Edge TTS 與代理：** 有些雲端環境的對外連線必須走 HTTPS 代理，而 aiohttp 預設不讀 `HTTPS_PROXY`。`synthesize_narration.py` 現在會把 `XINEW_TTS_PROXY`／`HTTPS_PROXY` 明確交給 edge-tts；沒有代理的環境行為不變。
  代理對 `speech.platform.bing.com` 偶爾回 403，腳本每句最多試 5 次；整段失敗時先看代理狀態，確認是政策封鎖才停下來交接，不要繞過，也不要換聲線。
- **組裝很久：** 2 核心機器上 assemble 約 25 分鐘，會超過一般命令的時間上限。請用 `nohup … &` 在背景跑並輪詢 log；被中斷就清掉暫存後重跑，不會留下半成品。
- **課別專用程式放 `authoring/lxxx/`：** L004 的內容、教材、字幕預檢、影音量測與語音辨識腳本都在 `authoring/l004/`，可當寫法參考；**內容不可沿用**。
  `subtitle_precheck.py` 可在 TTS 之前就用實際燒字樣式檢查 36 句字幕會不會遮到投影片。
- **機器聽檢不是聽審：** `asr_review.py` 需要另外準備本機 faster-whisper 模型，照字幕時間切音逐條辨識，可證明每句都在、音畫對位正確；聲調與咬字仍要人聽。
- **套版文字：** LibreOffice 在英數與中文之間會多加間距，英文字後面接全形標點特別鬆；時間表與標題盡量用國字數字、避免「英文＋全形冒號」。
- **大型檔保存：** 本 repo 是公開的，影片不要放 GitHub Release。Claude 對話附件單檔上限 30 MiB，L004 把交付 ZIP 切成 6 段位元一致的分段檔，並在 delivery.json 記錄每段雜湊與還原命令。

## 8. L005 之後新增的共用工具與選項（2026-10-07）

做第二集時把只寫給 L004 的檢查改成共用版，並補了三個實際遇到的洞。舊集不受影響，選項都要在該集 manifest 明確開啟。

- **共用檢查（取代每課複製一份）：** `pipeline/qa/subtitle_precheck.py`、`deck_check.py`、`media_review.py`、`asr_review.py`，都用 `--episode episodes/academy/<slug>`。
  它們會寫入該集的 `qc/`；**不要拿已交付的舊集試跑**，會覆寫那一集的 QC 紀錄。
- **TTS 截斷防護：** Edge TTS 的連線若在句子唸完前關閉，edge-tts 不報錯，只會得到一段比較短的音檔（L005 第一次合成有一句 45 字只有 5 秒）。
  `synthesize_narration.py` 現在逐句核對邊界中繼資料是否涵蓋全文、音訊長度是否到最後一個邊界，不符就重試，五次都失敗才停。
  合成後仍請看一眼每句的語速（字數÷秒數），明顯偏快就是被截斷。
- **`renderOptions.asianLatinAutoSpace=false`：** LibreOffice 預設會在中文與英數之間自動加間距，畫面會把 `蘋果 -手機` 顯示成減號兩側都有空隙。
  投影片要呈現「照著打」的字串時開啟這個選項（PPTX→ODP→關閉自動間距→PDF）；開啟後畫面上的空格就是輸入的空格。
- **`renderOptions.captionLineBreak="kinsoku"`：** libass 依字數平均斷行，第二行常以「，」「、」開頭或把詞拆開。
  開啟後由 `pipeline/scripts/caption_wrap.py` 在燒字前決定斷行（一行放得下就一行；否則兩行，優先斷在標點之後、不拆英數）。
  只影響燒進畫面的字幕；交付的 SRT 仍是每條一行。`subtitle_precheck.py` 會核對實際行數和預定斷行一致。ffmpeg 沒有 libass 時退回 Pillow 燒字，不套用這個斷行。
- **列印包：** `authoring/printpack.py` 提供共用的 A4 版面、Chromium 轉 PDF 與頁數／字型／文字檢查；各課的 `classroom.py` 只寫內容。
- **封裝之後：** `pipeline/split_delivery.py` 把交付資料夾壓成 ZIP、切成 28 MiB 分段、寫還原說明，並把分段接回去核對雜湊；
  分段實際交給使用者之後，再用 `pipeline/record_delivery.py` 寫 `delivery.json`、`publication/status.json` 和狀態表（它只讀該集自己的 QC 數值，verify 沒過或缺檢視紀錄就停）。
- **組裝可重現：** 同一份來源在同一環境重跑 assemble，母帶位元相同；字幕版只在字幕斷行設定改變時不同。
- **破音字：** 機器辨識分不出聲調。L006 的「拿秤量一量」被聽成「車輛」，另外單獨合成同一句、取字級時間後量基頻走勢，才推斷是二聲；這只能當旁證。
  寫旁白時盡量避開破音字緊接在一起的寫法，避不開就在 `qc/manual-review.md` 列出時間點請使用者親耳確認。
- **L006 沿用的做法：** `authoring/l006/` 以 L005 的結構為底，內容全部重寫；兩個渲染選項都開。練習用的例子全部虛構並逐張標示，不拿真實公司或媒體當可疑例子。

## 9. L007 起的共用工具（2026-10-07）

連做四集時，把每集重複的機械工作收進共用工具；各課的 `authoring/lxxx/` 只留內容。

- **內容**：`authoring/lesson_builder.py` 負責套版對應檢查、旁白／投影片／分鏡／manifest、來源與查核文件，
  並檢查 36 句沒有和任何前集重複。各課的 `prepare_content.py` 只放文字並呼叫 `build()`。
- **教材**：`authoring/classroom_pack.py` 寫文字檔、CSV、列印包 PDF 並記錄 `qc/classroom-validation.json`。
- **來源查核**：可以派研究子代理下載原始頁面、回報逐字引文，原文存成各課 `production/source-notes.md`；
  `fact-check.md` 要寫清楚哪些是逐字讀到、哪些只是擷取摘要，主代理沒有逐頁重讀也要寫。
- **看圖**：`pipeline/qa/review_sheets.py` 產生投影片、列印包、特殊畫格的總表（放暫存區，不是交付物）。
- **驗收報告**：verify 之後用 `pipeline/qa/write_report.py` 由該集自己的 QC 數值產生 `qc/report.md`；
  檢視方法、發現與限制仍要自己寫在 `manual-review.md`、`slide-visual-review.md`。
- **交付文字包**：`pipeline/handover_bundle.py` 依 `delivery.json` 和 `qc/handover-notes.json` 產生說明檔與 HTML 報告，放在 `delivery/drive-Lxxx/`。
- **文件同步**：`pipeline/status.py --write` 會重寫各文件裡 `<!-- academy-status:… -->` 標記之間的已交付清單、下一堂與大型檔表；
  交付後不要手改這些段落。
- **Edge TTS 不穩時**：服務有時連續回「沒有收到音訊」。合成腳本現在會拉長重試間隔（最多七次），
  並把通過完整性檢查的句子存進 `.build-tts-cache/`（以聲線與整句文字為鍵，不進 Git），中斷後重跑不必從頭來。
  合成可能超過十分鐘，請在背景執行。
- **語音辨識加上拼音比對**：`asr_review.py` 另外算一個以無聲調拼音比對的相似度（數字讀成國字、同音字視為相同），
  需要在辨識用的環境裝 `pypinyin`；`--rescore` 可以不重跑模型、只重算分數。它看不到聲調，破音字仍要人聽。


## 10. L008–L010 實作後的備註（2026-10-07）

- **合成失敗後重跑**：L008 與 L010 各有一次整輪合成在同一句連續失敗後停止（七次重試都沒有音訊）。直接重跑同一條命令即可，
  已通過的句子會從 `.build-tts-cache/` 取回；`tts-manifest.json` 的 `sentencesResumedFromInterruptedRun` 記錄取回幾句，
  `qc/tts-run.log` 保留每一次執行。重跑兩次仍失敗才寫 HANDOFF.md，不要無限重試。
- **夾在中文裡的英文縮寫**：`AI` 緊接著「是」「約定」「工具」這類詞時，聲線只給它約 0.15–0.18 秒，辨識聽成「應該」「要」「一樣」；
  後面接逗號、冒號、句號時約 0.3 秒，就聽得清楚。L010 因此把三句改寫（例如「主題是 AI：它是什麼、不是什麼」「使用 AI 的家庭約定」）。
  做法：合成後、組裝前，先把 `audio/slide_NN.mp3` 丟給本機語音辨識看一遍，有疑慮的詞改寫句子再合成，比組裝完才發現省二十分鐘。
- **畫出來的教材圖**：L009 的三張「模擬照片」是 `authoring/l009/classroom.py` 用內嵌 SVG 畫的，沒有任何真人照片；
  需要「看起來像照片但全部虛構」的教材時可以照這個做法，並在每張圖上標示虛構。
- **列印包頁數不必是五頁**：L010 的分類牆要放得下功能卡，改成兩頁上下黏貼，列印包共六頁；`classroom_pack.build(pack_pages=…)` 照實填。
- **一邊組裝一邊做下一集**：組裝約 15–20 分鐘、吃滿 CPU；合成只吃網路。可以讓前一集在背景組裝，同時寫下一集的內容與教材，
  但同一時間只跑一個組裝。每一集仍然要各自 verify、打包、交付、記錄、commit 之後才算完成。

## 11. L011–L013 實作後的備註（2026-10-08）

- **「AI」後面一律接標點**：L011 再次確認，`AI` 緊接中文（包括「AI 的」）時念得很短、辨識聽不出來；三集全部改成「AI，」「AI：」「AI；」或乾脆不念。
  片名有 AI 的課，旁白第一句可以只念片名的中文部分（L012「幻覺抓錯賽」、L013「我們要逛三個體驗站」），封面與章節仍用原片名。
- **組裝前先整幕辨識**：合成後把 12 幕 `audio/slide_NN.mp3` 丟給本機語音辨識，聽不出來的詞（L013 的「選兩個」「註明用了」）改寫後只重合成那幾句；
  組裝完才發現要再花一次十五到二十分鐘。
- **看畫格時對照投影片用字**：L012 第一次組裝後才發現字幕「說的對不對」和同頁卡片「說得對不對」不一致，只好重新組裝。
  寫旁白時，和同一頁可見文字重複的片語要用同一寫法。
- **先核對課表的時段分配**：L013 第一版把 25–65 分鐘的共同實作挪到下半場、漏了 75–105 分鐘的「增加一個自選規則或功能」；
  寫第 9–11 頁之前，先把 `lessons/Lxxx/lesson.json` 的「2 小時課程流程」逐段對照。
- **不用孩子帳號的做法**：L011 爸爸當只照字面做事的機器人；L012 本課編寫的模擬回答（標示清楚、建置程式檢查錯誤數）；
  L013 三站各有不用工具的做法，暖身題的圖用 SVG 簡單圖形自己畫並標示「不是 AI 生成」。
- **旁白聲線的說法**：可以說「這支影片的旁白是文字轉語音合成的，不是真人錄的」；不要說這個聲音「不是任何真人的聲音」，它怎麼錄製、訓練沒有查核。
- **背景合成要等前一次結束**：同一集的 `run tts` 不要重複啟動；誤觸會在 `tts-run.log` 多一筆全部取回快取的紀錄（L013 有一筆），要在 manual-review 寫明。
