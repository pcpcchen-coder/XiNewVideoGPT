# SP01 AI 近期發展：工程團隊怎麼用

2026-10-04 建立，供 2026-10-05–10-11 團隊分享。一次性番外篇，沿用原陳犀牛角色、深藍／黃／青與原開場 v2。

## 例外範圍

- 本次明確要求 **5 頁投影片**，含封面，取代一般課次的 12 頁規格。
- 共 15 段講稿。屬官方消息整理與工程試行提案，不是課堂錄音逐字稿。
- 使用 `SP01`，不占用 L001–L192，不更動課表、課程狀態與系列預設。
- 本次未授權 YouTube 公開。

## 交付狀態

已完成：5 頁可編輯 PPTX、逐頁講稿、官方來源、原版有聲片頭、離線播放入口。

**正文未合成新旁白，尚無完整配音 MP4。** 原 Edge-TTS 流程需將講稿傳至 Microsoft 外部語音服務，自動審核因本次未明確授權外送而拒絕。未重試或改走另一外部服務。若使用者明確同意，才接續 `zh-TW-YunJheNeural`。

## 使用

下載交付包後全部解壓縮，用瀏覽器開啟 `START_PRESENTATION.html`，按「播放開場」。片頭結束後程式接續第 1 頁，方向鍵切換五頁，按「講稿」查看本頁內容。正文由分享者口頭講解。

PPTX 的五頁皆可編輯，備註保存講稿與來源。片頭是包內獨立 MP4，未嵌入 PPTX。若用 PowerPoint 分享，先播放片頭再開簡報。HTML 使用預渲染圖片維持原外觀，不取代可編輯 PPTX。

## 重建

在 repo 的 `academy/` 執行：

```sh
./cloud-runtime.sh python pipeline/academy.py doctor
./cloud-runtime.sh "$CODEX_PRIMARY_RUNTIME_NODE" specials/sp01-ai-update-20261004/build_deck.mjs
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
