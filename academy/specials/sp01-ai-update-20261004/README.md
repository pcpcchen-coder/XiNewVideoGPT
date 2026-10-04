# SP01 AI 近期發展：工程團隊怎麼用

**發布更新（2026-10-04）：** 使用者在本機上傳工作階段明確要求上傳並選擇「公開（和 L003 一樣）」。本集已公開：[6Bq4jI0Xook](https://youtu.be/6Bq4jI0Xook)。原封面、六段章節、來源說明與繁中 CC 已保存；YouTube 著作權檢查顯示未發現任何問題。詳見[本機發布驗收](publication/local-upload-review.md)。後續只接續此影片，不得重複上傳。

2026-10-04 建立，供 2026-10-05–10-11 團隊分享。一次性番外篇，沿用原陳犀牛角色、深藍／黃／青與原開場 v2。

## 例外範圍

- 本次明確要求 **5 頁投影片**，含封面，取代一般課次的 12 頁規格。
- 共 15 段講稿。屬官方消息整理與工程試行提案，不是課堂錄音逐字稿。
- 使用 `SP01`，不占用 L001–L192，不更動課表、課程狀態與系列預設。
- 製作階段未授權 YouTube 公開；已由上述本機工作階段的新授權取代，僅適用 SP01。

## 交付狀態

已完成：5 頁可編輯 PPTX、逐頁講稿、官方來源、原版有聲片頭、離線播放入口。

2026-10-04 11:16:35（台北）使用者明確回覆「同意配音」，同意將本次講稿送交 Microsoft TTS。已解除本次 SP01 配音阻擋，使用原聲線 `zh-TW-YunJheNeural`。最新成片狀態與驗收見 `delivery.json`、`qc/report.json`。這項同意僅用於本次講稿，不代表新增 YouTube 公開授權。

## 使用

下載交付包後全部解壓縮，用瀏覽器開啟 `START_PRESENTATION.html`，按「播放開場」。片頭結束後程式接續第 1 頁，方向鍵切換五頁，按「講稿」查看本頁內容。正文由分享者口頭講解。

PPTX 的五頁皆可編輯，備註保存講稿與來源。片頭是包內獨立 MP4，未嵌入 PPTX。若用 PowerPoint 分享，先播放片頭再開簡報。HTML 使用預渲染圖片維持原外觀，不取代可編輯 PPTX。

## 重建

在 repo 的 `academy/` 執行：

```sh
./cloud-runtime.sh python pipeline/academy.py doctor
./cloud-runtime.sh "$CODEX_PRIMARY_RUNTIME_NODE" specials/sp01-ai-update-20261004/build_deck.mjs
./cloud-runtime.sh python pipeline/scripts/synthesize_narration.py --episode specials/sp01-ai-update-20261004
./cloud-runtime.sh python specials/sp01-ai-update-20261004/assemble_special.py --episode specials/sp01-ai-update-20261004
./cloud-runtime.sh python specials/sp01-ai-update-20261004/verify_special.py --episode specials/sp01-ai-update-20261004
./cloud-runtime.sh python specials/sp01-ai-update-20261004/package_special.py
```

依當次 Presentations skill，在首次簡報建置前執行其 create 標記與字型設定。建置會重用 repo 內還原的 L001 第 1、3、5、9、12 頁，保留模板與角色。不宣稱使用已遺失的遷移前原始 PPTX。

`production/manifest.json` 記錄例外、規格與查核日，`narration.json` 為講稿，`sources.json` 為官方事實來源。`build_deck.mjs` 建置五頁，`package_special.py` 封裝播放器、片頭和內容。輸出位於 checkout 父目錄的 `special-output/`。

## 已做檢查與限制

- 五頁數量、五頁備註、PPTX 結構／幾何／可重新匯入檢查通過。
- 五頁渲染逐頁目檢，文字和角色正常，無 L001／MacBook 殘留。
- 原片頭檔案逐位元雜湊相符，SHA-256 `1acd858b2a0e624f99c267620b15db5e637f7f6ac7fa057b7e5a9df492a7d04a`。
- 全部模型消息來自原廠公告。成本為 API 美元／百萬 tokens，模型效果限定原廠評測。第 5 頁樣本數與驗收門檻為提案。
- 未在使用者的 PowerPoint 或瀏覽器實機播放。雲端 Chromium 測試器因下載失敗無法完成播放 UI 實測，不能標記為已通過。

大型交付的檔名、大小、雜湊和保存定位見 `delivery.json`。

## 配音版交付

完整字幕片 `SP01_AI_Update_2026-10-04_zh-TW.mp4` 含原片頭與五頁旁白。無字幕母帶、SRT、PPTX 與製作時間資料放在更新的交付包。字幕字級與邊界依本次畫面調整，其他系列設定沿用原組裝器。`verify_special.py` 是本次五頁／15 段的獨立檢查器，不改動 L001–L192 的一般驗收規格。
