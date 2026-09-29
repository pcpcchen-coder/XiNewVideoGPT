> 歷史移交紀錄；現行雲端流程請以 academy/docs/CLOUD_PRODUCTION_GUIDE.md 為準。

# 父子科技學院整合與操作手冊

## 課程目標與兩條時間軸

保留原規劃：每週一次兩小時，每年 48 堂、4 年共 192 堂，另留 4 週彈性。MacBook Air 是孩子動手操作與作品展示的機器；Mac mini 負責爸爸示範、錄音保存與影音製作。主軸持續涵蓋 AI、寫 code、科技與生活技能，保留 Scratch、Python、Web、感測、Git、資料科學、電池能源、機器學習、機器人與 AI Agent 等內容。

課堂仍按原 Excel 的 120 分鐘活動走：10 分鐘任務開場、15 分鐘示範、40 分鐘共同實作、10 分鐘休息、30 分鐘孩子改造、10 分鐘孩子教爸爸、5 分鐘錄音總結。影片是課後整理的教學精華，不要求兩小時課堂全部變成 TTS。

每課至少保存作品、孩子的問題、一次卡關與修正、孩子用自己的話解釋原理。影片維持附件的 12 幕 × 3 句風格；一課可拆多集，或先只做一支概念短片，再補操作展示。不要為湊滿 192 支影片壓縮實作與生活技能。

## 標準流程與責任

| 階段 | 輸入 | 輸出 | 執行方式／離開條件 |
|---|---|---|---|
| 課程匯入 | 原 Excel V2 | catalog.json | 已實作；核對 L001–L192、每課 3 筆、總共 576 搜尋入口，保留其他工作表資料 |
| 課前準備 | 指定課次 | lesson.json、brief.md | 已實作；保留學習目標、120 分鐘流程、作品與錄音提問 |
| 錄音 | 父子教學、操作畫面 | 原始音檔、作品／螢幕錄影 | 人工錄製；說出當課主題與問題，收尾讓孩子自述；原檔保存於 private |
| ASR／匯入 | 真實錄音或 SRT/JSON | private/transcript/raw.json | 本地模型轉錄接口或已有轉錄器匯入；保留秒數、段落 ID；不推測說話者 |
| 編輯與教學整理 | 原稿＋課程 brief＋作品 | cleaned.md、fact-check.md、teaching-notes.md | 爸爸／AI 編輯；保留不確定詞、引用段落 ID，補充知識與實際對話分開 |
| 腳本與視覺企劃 | 核對後教學稿 | manifest、narration、slides、storyboard、plan、教學插圖 | 編輯階段；12 幕每幕一個任務，3 句旁白，保留固定結尾 |
| PPT | slides、narration、插圖 | 可編輯 PPTX | 沿用附件版型建構器；不是對原始逐字稿直接機械切頁 |
| PNG | PPTX | 12 張 1920×1080 PNG | 新增 render 入口；父親逐頁檢查內容、文字溢出、字幕安全區 |
| TTS | narration 的 text／tts | 12 段音訊、timing、tts-manifest、source SRT | 可攜 Edge-TTS 腳本；保留原暖聲鏈；需網路；文字改動後重跑 |
| SRT／組裝 | 靜態 PNG、逐幕 TTS、正式片頭 | 無字幕母帶、燒字幕版、全片 SRT | 偏移依當次片頭實測，不按檔名猜秒數；正片無配樂 |
| 驗收 | 全部產物 | qc/report.json、verified-inputs.json | 原 18 項＋字幕版 decode、30 fps、全字幕時間／文字比對；另驗 TTS 真實 SHA-256 |
| 發布包 | 通過技術驗收的產物 | 母帶、成片、PPT、SRT、封面、YouTube 草稿 | 白名單複製，記錄雜湊；不含 private；不會自動上傳 |
| YouTube | 爸爸複核後的發布包 | 影片網址 | 目前人工上傳；確認標題、說明、觀眾設定與可見性，回填原教學紀錄 |

## 本次新增結構

```text
XiNewVideoGPT-academy/
├── README.md、requirements.txt、.gitignore
├── curriculum/catalog.json          192 課＋576 入口、原始欄位與其餘工作表
├── lessons/L001/
│   ├── lesson.json                  課程資料＋episodePaths（一對多）
│   ├── brief.md                     當堂 120 分鐘與錄音重點
│   ├── private/recordings/           原錄音，排除 Git 與發布包
│   ├── private/transcript/raw.json   實際匯入後才產生
│   ├── editorial/                    cleaned、fact-check、teaching-notes
│   └── publication/
├── episodes/academy/<slug>/          new-episode 才建立的待編寫模板
├── pipeline/academy.py              課程、逐字稿、階段執行、發布入口
├── pipeline/scripts/
│   ├── *_ep10.py                    附件原腳本，未改
│   ├── build_deck.py                參數化集數，沿用固定 12 幕版型
│   ├── synthesize_narration.py       Python Edge-TTS、獨立暫存
│   ├── assemble_episode.py          相對片頭路徑、實測偏移、獨立暫存
│   ├── verify_episode.py            失敗非零結束、擴充驗證
│   └── burn_subtitles_pillow.py      缺 libass 時的字幕備援
├── tests/test_academy.py
└── docs/                            盤點、手冊、驗證與來源清單
```

catalog 是原 Excel 的衍生快照，不取代 Excel 儀表板。import 不回寫 Excel，若來源更新，另存新 catalog 路徑並比對；已建立的 lesson 保留當時課程快照。`episodePaths` 不按課號自動匹配舊 XiNew 季數。教學完成狀態與影片完成狀態分開，避免還沒教完卻顯示課程完成。

## 機器與依賴

在 repo 根目錄執行。使用已安裝且可運行的 Python 3.10+。本機 `/usr/bin/python3` 目前受 Xcode 授權未完成影響，因此本次驗證使用以下 Python；使用者可自行指定自己的 Python 環境。

```sh
cd "<ORIGINAL_MAC_HOME>/.codex/.chatgpt-projects/g-p-6a5e0fd217c48191866a4b61a36b2f46/work/XiNewVideoGPT-academy"
export ACADEMY_PYTHON="<ORIGINAL_MAC_HOME>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
"$ACADEMY_PYTHON" pipeline/academy.py doctor
```

一般部署可在自己的專案虛擬環境安裝，勿修改 Codex bundled dependencies：

```sh
"$ACADEMY_PYTHON" -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
export ACADEMY_PYTHON="$PWD/.venv/bin/python"
```

FFmpeg、FFprobe、LibreOffice `soffice`、Poppler `pdftoppm` 需在 PATH。本次 doctor 找到這四個程式，但尚未重建 PPT 來驗證此機器的字型／匯出。Edge-TTS 與 faster-whisper 尚未在本次驗證環境安裝；既有影音驗收不需要它們。不要把「工具路徑存在」當成端到端新片產製成功。

## 每課命令

1. 首次或新版本 Excel 匯入。首次已執行；相同資料可重跑，不同資料不覆寫舊 catalog。

```sh
"$ACADEMY_PYTHON" pipeline/academy.py import-curriculum "<ORIGINAL_MAC_HOME>/Downloads/父子科技學院_V2_192堂_YouTube教材庫.xlsx"
```

2. 開新課。L001 已建好；下列以 L002 示範。若同課需要重教多次，現版先保存不同錄音 session 副本，不要覆寫 raw.json；多 session 管理尚未自動化。

```sh
"$ACADEMY_PYTHON" pipeline/academy.py init L002
"$ACADEMY_PYTHON" pipeline/academy.py new-episode L002 --slug l002-file-treasure
```

3. 錄音後匯入已有逐字稿。SRT 必須有時間碼；JSON 格式如下。speaker 可省略，不能因只有兩個人就假設聲道代表父／子。

```json
{"segments":[{"start":0.8,"end":4.1,"speaker":"爸爸","text":"這個檔案存在哪裡？"}]}
```

```sh
"$ACADEMY_PYTHON" pipeline/academy.py ingest L002 /實際路徑/逐字稿.srt --recording /實際路徑/課堂錄音.m4a
```

選用本地 ASR：另裝 faster-whisper，準備已下載的模型資料夾。這條路徑尚未用使用者真實錄音驗證，不能保證本台 Mac 的速度或中文準確率。

```sh
.venv/bin/python -m pip install faster-whisper
"$ACADEMY_PYTHON" pipeline/academy.py transcribe L002 /實際路徑/課堂錄音.m4a --model /實際路徑/本地模型
```

4. 完成編輯與六張本課圖解，取代 new-episode 產生的「待編寫」。目前版型按第十集的固定欄位設計，可換文字與圖像內容；不同頁面架構需要擴充建構器，不應直接複製第十集的知識內容。

| 頁次 | 版型欄位（各頁都有 slide、eyebrow、title） |
|---|---|
| 1 | subtitle、takeaway；封面插圖 |
| 2、5、11 | subtitle、steps、takeaway；三或四步驟 |
| 3、8 | subtitle、labels；圖解 |
| 4、7 | bullets、takeaway；插圖＋重點 |
| 6、9 | leftTitle、leftItems、rightTitle、rightItems、takeaway |
| 10 | columns，每欄 title、subtitle |
| 12 | answer、explain、recap、next、signoff |

每幕 narration 需 `slide`、`title`、`sentences`（3 筆，每筆有 `text`，必要時加 `tts` 發音）。storyboard 需 `slide`，其餘沿用附件欄位。plan 應記錄目標、來源段落、補充事實與孩子作品位置。當引用原話時記錄 seg ID 與來源秒數；這項目前由人工檢查，CLI 不會自動驗證知識正確性或內容來源。

5. 依序製作。每個命令失敗即停止；內容修改後從受影響的階段重跑。TTS 與 assembly 每次使用新的暫存目錄，暫時以保守重建確保正確，未實作全局增量快取與並行執行。

```sh
export ACADEMY_EP="episodes/academy/l002-file-treasure"
"$ACADEMY_PYTHON" pipeline/academy.py run validate --episode "$ACADEMY_EP"
"$ACADEMY_PYTHON" pipeline/academy.py run deck --episode "$ACADEMY_EP"
"$ACADEMY_PYTHON" pipeline/academy.py run render --episode "$ACADEMY_EP"
# 逐頁目檢後繼續
"$ACADEMY_PYTHON" pipeline/academy.py run tts --episode "$ACADEMY_EP"
"$ACADEMY_PYTHON" pipeline/academy.py run assemble --episode "$ACADEMY_EP"
"$ACADEMY_PYTHON" pipeline/academy.py run verify --episode "$ACADEMY_EP"
"$ACADEMY_PYTHON" pipeline/academy.py package --episode "$ACADEMY_EP" --output delivery/L002-v1
```

TTS 會送出編輯好的 narration 給 Edge-TTS，錄音與 raw.json 不在輸入契約內。原 manifest 的 speed=118／pitch=38 是歷史欄位，舊程式未真正傳入。新版明確記錄實際使用的 rate=+0%、pitch=+0Hz，保留暖聲處理，不把原 metadata 當成已套用參數。

SRT 分為 `zh-TW-source.srt`（正片零基準）與 `zh-TW.srt`（全片）。上傳含片頭母帶時要配後者；不能用 source SRT。片頭改長度後必須重組裝與重驗字幕。發布包也帶成片版，實際在 YouTube 使用母帶＋可開關字幕或燒字幕版，擇一上傳即可。

## 驗收標準

技術驗收：192 課 ID 唯一且連續、576 筆每課三筆；逐字稿時間合法、原稿不覆寫；12 幕／36 句、固定結尾；音檔 SHA-256 重新計算一致、劇本與 timing 文字一致；PNG 1920×1080；H.264、30 fps、AAC 48 kHz 立體聲；母帶與字幕版全片 decode 無錯；成片時長與片頭＋旁白相符；每条 SRT 的文字、順序與起訖符合實測片頭偏移；整體響度 −18 至 −14 LUFS。改動任何發布產物後，舊驗收指紋失效，需重跑 verify 才能 package。

人工教學／視聽验收：孩子能完成 Excel 所列作品與說明原理；12 頁文字可讀、沒有遮擋；字幕沒有擠出底部；多音字與英文術語可懂；片頭接正片不突兀；正片沒有非預期音樂；錄音中的不確定敘述已核對；公開版本不露出家庭帳號、學校與其他非教材內容。現有音量、檔案存在或大小檢查都無法代替這些項目。

發布草稿預設 private，madeForKids 留空讓爸爸依實際觀眾選擇。尚未實作 OAuth、API 上傳、排程或 Excel 回寫。完成上傳後，把實際網址、教學日期、作品連結填回原工作簿「教學紀錄」；保留其原儀表板邏輯。

## 遷移與後續優先順序

1. 這次只新增獨立 `XiNewVideoGPT-academy`，早期 repo 乾淨 checkout、原 ZIP、原 Excel 與 `sources/` 均保留。`archive-inspection/` 留原解壓參照；工作副本的 qc 是本次重跑結果。
2. 先用 EP10 現成產物驗證新入口，再挑一堂真實錄音跑最小閉環。不要立即批量產出 192 組空影片。
3. 第一次新課完整成功後，建立版本化依賴 lock、確認 Mac 字型與字幕備援呈現。保留各次發布資料夾，如 L002-v1、L002-v2。
4. 再按需求把固定页次改為 `layout` 欄位，將六張插圖槽位改為自訂路徑；可減少不同課程不必要的版型限制。這次先保留視覺架構。
5. 之後才做多 session 管理、ASR 說話者辨識、語音抽驗、快取指紋與實際 YouTube API／教學紀錄回寫。這些不是本次已完成能力。

移到正式 repo 時，先以 `docs/archive-inventory.json` 的雜湊比對版本，再複製新增的 academy.py、可攜脚本、tests、docs、requirements 與課程衍生檔。不要整包覆蓋已經修改過的集數；原 `*_ep10.py` 和素材保留。回復方式是回到原腳本／原 repo，新增工具沒有改動其呼叫入口。
