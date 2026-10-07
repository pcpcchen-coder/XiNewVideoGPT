# 雲端逐集製作教學

ChatGPT 以外環境請優先讀 [Claude 可攜製作指南](CLAUDE_HANDOFF.md)，避免使用此文的專屬 artifact-tool 路徑。

更新：2026-09-29。以下命令均在 repo 的 `academy/` 執行。目標是可靠地接續 L001–L192；每次只做指定課次。

## 1. 環境與素材

需求：Python 3.11+（雜湊還原工具使用 `hashlib.file_digest`）、Node 22+、ffmpeg／ffprobe、中文字型；Python 套件見 `requirements-cloud.txt`。套件支援狀態以當次 doctor 為準。`faster-whisper` 僅在真實錄音轉錄時使用。

```sh
cd academy
chmod +x cloud-runtime.sh
./cloud-runtime.sh python -m pip install --target .cloud-deps -r requirements-cloud.txt
./cloud-runtime.sh python pipeline/academy.py doctor
```

`cloud-runtime.sh` 優先使用 `CODEX_PRIMARY_RUNTIME_PYTHON`、`CODEX_PRIMARY_RUNTIME_NODE`、`CODEX_PRIMARY_RUNTIME_NODE_MODULES`；可用 `RUNTIME_PYTHON`、`RUNTIME_NODE`、`RUNTIME_NODE_MODULES` 覆寫。`python`／`python3` 會映射至選定 Python，不再誤用系統 Python。

共用片頭以多個 `assets/opening/opening-v2.mp4.partNN` 保存，避免單次寫入介面大小限制。啟動器首次執行會依 `assets/opening/manifest.json` 核對每段並還原原始 MP4；分段檔必須一起 clone。若要重新核對已還原片頭，執行 `./cloud-runtime.sh python pipeline/restore_shared_assets.py --verify`。還原出的完整檔不再重複納入 Git。

`PRESENTATIONS_SKILL` 指向本工作階段的 Presentations skill 實體目錄；預設路徑只是環境預設，不保證所有平台相同。必須確認以下檔案存在：

- `$RUNTIME_NODE_MODULES/@oai/artifact-tool/dist/artifact_tool.mjs`
- `$PRESENTATIONS_SKILL/container_tools/artifact_tool_utils.mjs`
- `assets/fonts/NotoSansCJKtc-Regular.otf`
- `assets/opening/開場影片-v2.mp4`
- `episodes/academy/l001-mac-workstation/production/presentation/l001-mac-workstation.pptx`

中文字型可安裝到目前使用者的 fontconfig 字型目錄再執行 `fc-cache`；不可假定系統有中文字型。Edge-TTS 需要可用網路。若憑證錯誤，查系統信任根，使用合法 CA；保留 TLS 憑證驗證。不要把 Mac 的 `.venv` 複製到 Linux。

## 2. 核對課表，建立草稿

```sh
./cloud-runtime.sh python pipeline/status.py --next
./cloud-runtime.sh python pipeline/academy.py init L004
./cloud-runtime.sh python pipeline/academy.py new-episode L004 --slug l004-network-relay
```

`init` 建立 `lessons/L004/lesson.json`、brief 與私人／編輯區；已存在時拒絕覆寫。若是接續工作，直接使用既有課次，不重跑 init。
`new-episode` 使用 `pipeline/templates/academy/`，產出 12 幕／36 句占位稿及逐段套版映射，**不會產生影片、不會複製舊 QC、不會上傳**。課號與 slug 必須相符；新草稿應無法通過 validate。

## 3. 完成內容與教具

| 檔案（相對 episode） | 內容與完成條件 |
|---|---|
| `production/manifest.json` | 正確課號、主題、來源模式、聲線、品牌；編輯完成後設 `editorialStatus: authored` |
| `production/narration.json` | 12 幕，每幕 3 句；每幕附來源；最後固定結尾 |
| `production/slides.json` | 每頁主題與可見文案契約；不可殘留前一課內容 |
| `production/storyboard.json` | 每幕的教學目的、畫面、實作提示、動作 |
| `production/template-text.json` | L001 原文字 → 本課新文字；`old` 必須命中，跨段落保留段落數 |
| `production/sources.json`、`fact-check.md` | 官方操作來源、查核日期、結論、限制 |
| `production/plan.md` | 120 分鐘安排、作品、驗收、孩子教爸爸環節 |
| `classroom/` | 可真正開啟使用的練習檔、起始副本、計時或評量紀錄 |
| `authoring/lxxx/` | 本課可重跑的內容／教材／交付建置程式（如需要） |

沒有錄音：明確標示「依課表製作的課前教學版」。有錄音：先放 `lessons/Lxxx/private/`，保留時間及講者，經訂正後才改寫公開稿。課堂 120 分鐘和影片片長分開管理。

L003 的 `authoring/l003/prepare_content.py`、`classroom.py`、`delivery.py` 是**本集專用程式**。未改課號與內容前不可拿來執行 L004。可以參考其欄位、教材與章節算法；不得複製 L003 講稿冒充下一集。

`template-text.json` 的每條 `.old` 以還原的 L001 模板為準，不是上一集新字。若內容無法放入原段落數／幾何，先設計可編輯新版面並重新驗收，不停用殘留文字檢查。不可只改旁白而讓簡報留在上一堂。

## 4. 建置次序

以下以已完成內容編輯的 L004 為例：

```sh
./cloud-runtime.sh python pipeline/academy.py run validate --episode episodes/academy/l004-network-relay
./cloud-runtime.sh python pipeline/academy.py run deck --episode episodes/academy/l004-network-relay
./cloud-runtime.sh python pipeline/academy.py run tts --episode episodes/academy/l004-network-relay
./cloud-runtime.sh python pipeline/academy.py run media-check --episode episodes/academy/l004-network-relay
./cloud-runtime.sh python pipeline/academy.py run assemble --episode episodes/academy/l004-network-relay
```

`deck` 已輸出最終 PPTX 及 12 張 PNG，不需再跑相同 renderer 一次。依 Presentations skill 讀取操作規則、執行必要標記／幾何檢查，重新匯入最終 PPTX，再逐頁目檢。
`tts` 產生真實句級時間與音檔雜湊。組裝器將每幕音訊 pad/trim 到計算時長，避免 MP3 封裝誤差累積；字幕必須加上**本次** `qc/assembly.json` 的片頭實測秒數。

## 5. 交付附檔與驗收

組裝後先產出旁白 MP3、章節、說明、封面、`classroom.zip`、`START_HERE.md`。下一集需建立其自身附檔程式或明確生成這些檔案；目前通用 runner 沒有自動撰寫內容的功能。

L003 原案例（會重建附檔；之後務必重驗）：

```sh
./cloud-runtime.sh python authoring/l003/classroom.py
./cloud-runtime.sh python authoring/l003/delivery.py
```

檢查標準：

- 12 頁／36 句，投影片、備註、旁白一致，沒有前集課文；中文無缺字、裁切或字幕遮擋。
- 原片頭 v2、指定聲線；教學段落靜態／淡化／無背景音樂。
- 1920×1080、30 fps、H.264、AAC 48 kHz 雙聲道；母帶與字幕片全檔可解碼。
- 音量目標 −16 LUFS，允許 −18～−14；需記錄量測，不能只填 PASS。
- 36 條 SRT 與旁白／實測時間相符；檢查前、中、後幕音畫同步，以及全部字幕位置。
- 練習教材數量、內容及格式可用；沒有不存在的下載網址。
- `qc/manual-review.md` 寫出實際視聽檢查方法、時間、發現與限制；人工未聽完就不要宣稱人工全片聽審。

```sh
./cloud-runtime.sh python pipeline/academy.py run verify --episode episodes/academy/l004-network-relay
./cloud-runtime.sh python pipeline/academy.py package --episode episodes/academy/l004-network-relay --output delivery/L004-v1
```

`verify` 保存成品及輸入指紋；`package` 比對目前指紋與 PASS 報告後只複製白名單。任何 `production/audio/subtitles/output/assets/slides` 變動都要重新 verify。補寫上傳說明應在 verify **之前**完成。

## 6. 保存、更新進度、交給使用者

1. 交付資料夾或 ZIP 使用 `Lxxx-vN` 版本；不要默默覆寫已交付版本。
2. 將成品保存到可持續取回的位置；記錄檔名、大小、SHA-256、版本、取得方法。已同步 Git 的程式與文件不用再重複保存副本。
3. 更新 `curriculum/production-status.json`：製作 `verified`，發布 `awaiting_user_upload`，附 episode 路徑及證據。
4. 執行 `./cloud-runtime.sh python pipeline/status.py --write` 更新人讀表。
5. 提供 MP4、PPTX、教材與完整交付包連結，說明尚未由使用者回報上傳。
6. 使用者提供影片 URL 後，寫入該集 `publication/`；若只收到口頭回報，使用 `published_user_reported`，不要冒充代理已驗證。

## 7. 續做與故障恢復

- TTS 失敗：保留文案與已完成音訊；重跑後重建 timing、字幕及影片。不要把其他聲線或前集音軌混入。
- deck 失敗：檢查 artifact-tool／skill 路徑及逐段替換；保留原模板，不輸出全頁截圖假裝可編輯 PPT。
- 字幕遮擋：用本次 renderer 實測。L003 的 libass 參數只當起點，不保證長句在所有課都適用。
- 中斷：記下目前 stage、已通過檢查、待辦、變更檔案；依輸入雜湊判斷可重用哪些輸出。
- YouTube 登入或 502：與製作分開；預設使用者手動上傳，不能讓登入故障阻塞下一課內容準備。
