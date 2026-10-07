# 檔案、程式與交付清單

所有路徑以 `academy/` 為根。原包逐檔大小及 SHA-256 見 [file-inventory.json](cloud-migration/file-inventory.json)，原始完整清單見 [l003-handoff-SHA256SUMS.json](cloud-migration/l003-handoff-SHA256SUMS.json)。它們描述原接續包；整合後修改的文件／程式以 Git commit 為版本依據。

## 主要目錄

| 路徑 | 用途 | 保存方式 |
|---|---|---|
| `curriculum/catalog.json` | 192 堂完整欄位／576 組搜尋入口 | Git，權威課表 |
| `curriculum/*.xlsx` | 原始課表試算表 | Git，保持來源不變 |
| `curriculum/production-status.json` | 製作／發布分開追蹤 | Git，每集更新 |
| `CLOUD_CURRICULUM_INDEX.md` | 全部主題及目標索引 | Git |
| `assets/characters/` | 固定陳犀牛角色 | Git |
| `assets/fonts/` | 繁中字型及授權 | Git |
| `assets/opening/manifest.json`、`opening-v2.mp4.part01..38` | 共用原片頭，89,043,634 bytes | 分段檔進 Git；啟動器自動原樣還原 `開場影片-v2.mp4`，逐段／全檔 SHA-256 核對 |
| `pipeline/academy.py` | 初始化、驗證、TTS、合成、封裝入口 | Git |
| `pipeline/scripts/` | 原 renderer、TTS、影音與 QC 程式 | Git，EP10 檔僅歷史參考 |
| `pipeline/templates/academy/` | 新集 manifest／文字映射 seed | Git，不含舊旁白或舊 QC |
| `pipeline/status.py` | 192 堂狀態驗證、下一課、人讀表 | Git |
| `pipeline/restore_shared_assets.py` | 從 Git 分段檔還原共用片頭 | 啟動器自動執行；`--verify` 可核對既有檔 |
| `pipeline/restore_handoff_media.py` | 驗證並取回 L003 大型輸出 | Git |
| `authoring/l003/` | 本集內容、教具、附檔及修復腳本 | Git，本集專用 |
| `lessons/L001..L003/` | 已初始化課次的教學資料 | Git；private 忽略 |
| `episodes/academy/l001-mac-workstation/` | 從原程式還原的 L001 版型 | Git；不是 L001 完整成片 |
| `episodes/academy/l003-keyboard-ninja/` | L003 完整來源、PPT、音檔、PNG、SRT、教具及 QC | 大部分 Git；三個大型輸出見下表 |
| `docs/history/`、`docs/cloud-migration/` | 移交證據、舊規則、環境、清單 | Git；舊授權不能復用 |
| `delivery/`、`.cloud-deps/`、`.build-*` | 本機交付／依賴／建置中間檔 | Git 忽略；交付另存 |

## L003 大型輸出（原檔未變更）

| 檔案 | Bytes | SHA-256 |
|---|---:|---|
| `l003-keyboard-ninja-master.mp4` | 79,267,446 | `75bc239c179201b7b2e425566e9b08cfe685975cfa9b27c730c590a8c5cffee1` |
| `l003-keyboard-ninja-zh-TW.mp4` | 76,593,749 | `fabc3fc9d865e6ca92a3d85cdaff7c1a4bba4ca24f8b38e31fbee7bcf286271c` |
| `narration-only.mp3` | 8,126,829 | `9d8fc6df6cf541c57569325c4aa7d0fbe8abece55f1b0f663b938b48586c8ba2` |

以上三檔沒有新增至 Git。精確原件保存在 `Academy_Cloud_Handoff_2026-09-27_L003.zip`；字幕 MP4 也單獨保存為 `l003-keyboard-ninja-zh-TW.mp4`。未建立公開 Release 下載網址，勿編造連結。

## L004 大型輸出（L004-v1，2026-10-07）

| 檔案 | Bytes | SHA-256 |
|---|---:|---|
| `l004-network-relay-zh-TW.mp4` | 78,240,692 | `4c7e79396a6fe635e05d4058f0638157e5251b2f1e412d58f8ea55d34aacfddb` |
| `l004-network-relay-master.mp4` | 80,742,543 | `f8079597920871e54c02505e9c4a593e5beaf65d56b848271afd4bbe3620aba0` |
| `narration-only.mp3` | 8,641,773 | `6e635b402a3e8ebba29188c31876250b1be34b0dc0e1129c405f54f99ec8fc67` |
| `L004-v1_父子科技學院_網路到底是什麼_封包接力賽_2026-10-07.zip`（完整交付包） | 166,314,066 | `c45306c0584192380e0cc148e557009653ecf166a7dfa1f254eb50f0ee480f8e` |

以上未進 Git。交付包以 6 個分段檔交付在製作當次的 Claude 對話附件中（單檔上限 30 MiB），各段雜湊、還原命令與包內 20 個檔案的雜湊見
`episodes/academy/l004-network-relay/delivery.json`。本 repo 為公開，未建立 Release，勿編造下載連結。
L004 的來源、PPTX、12 張 PNG、12 段 TTS 音檔、SRT、教材與 QC 都在 Git；附件無法取得時可依 delivery.json 的命令重新組裝，重建結果須作新版本並重新驗收。

## 新工作區取回 L003

1. 在 ChatGPT Library 按完整檔名找 `Academy_Cloud_Handoff_2026-09-27_L003.zip`；由 Library 能力下載到工作區。一般本機使用者則下載本對話已交付的同名 ZIP。
2. 大小必須是 295,998,099 bytes，SHA-256 必須為 `b7366b204bdc0bf09ab5939e73d9dc0f3b2a023d118f13c1416f17bdb622f463`。
3. 在 `academy/` 執行（替換成實際 ZIP 路徑）：

```sh
./cloud-runtime.sh python pipeline/restore_handoff_media.py --archive /absolute/path/Academy_Cloud_Handoff_2026-09-27_L003.zip
./cloud-runtime.sh python pipeline/academy.py package --episode episodes/academy/l003-keyboard-ninja --output delivery/L003-user-upload-v1
```

還原器只補三個被省略的輸出，不覆寫 repo 更新的文件。既有檔案同雜湊則略過，不同雜湊則拒絕覆寫。封裝還會比對全部原驗收指紋。若修改過本集 production 或成品，先重建並 verify，再用新的交付版本號。

如果接續包暫時不可取得，共用片頭、原始本集 PNG／TTS 音檔與模板已在 Git，可依製作手冊重新 assemble、產生交付附檔並 verify。新輸出可能因工具版本不同而有不同位元雜湊，必須作新版本記錄。

## 使用腳本時的界線

- `authoring/l003/repair_audio_timing.py`、`reburn_captions.py` 是當時的修復操作，正常重建已整合到 pipeline，不要每次再套一次。
- `authoring/l003/save_handoff.py` 為歷史封裝腳本；執行前必須指定新的輸出資料夾，不能覆寫原包。
- 來源包的舊 manifest、舊公開授權、舊本機路徑只作證據。現行政策見 `series-policy.json`。
- 任何新集的大型成品都另記檔名、大小、SHA-256、可存取位置及保存結果；切勿只留下暫存絕對路徑。
