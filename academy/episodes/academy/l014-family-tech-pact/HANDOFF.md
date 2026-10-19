# L014 接續交接（HANDOFF）

- lessonId：L014「我們家的科技公約」
- episodePath：`episodes/academy/l014-family-tech-pact`
- 撰寫：2026-10-19，製作代理 Claude（雲端工作階段）
- 起點 commit：`4bda615`（main）；本次成果在分支 `claude/epic-einstein-wl86uv` 的下一個 commit（見 `git log -- episodes/academy/l014-family-tech-pact`）
- 狀態：**未完成、未驗收、不可上傳**。production-status 記為 `deck_ready`；沒有影片、沒有音訊、沒有 verify、沒有 package。

## 最後成功階段

1. preflight：`ready: true`（Python、ffmpeg+libass/loudnorm/ebur128、LibreOffice、字型、原片頭 v2、edge-tts 7.3.1）。
2. 內容：`authoring/l014/prepare_content.py` → 12 幕／36 句、118 筆套版對應、與前集旁白不重複檢查通過；`run validate` 通過。
3. 簡報：`run deck`（ooxml-template）→ 最終 PPTX 與 12 張 PNG；`qa/deck_check.py` 通過（原生可編輯文字、36 句 notes）。
4. 逐頁視覺檢查：`qc/slide-visual-review.md`（第 7 頁修正一次後重建）。
5. 字幕靜態預檢：`qa/subtitle_precheck.py` 通過。
6. 教材：`authoring/l014/classroom.py` → 9 個檔、列印包 6 頁，逐頁檢視並修正三處版面。

## 已保存成品（皆已進 Git，小檔）

| 檔案 | bytes | SHA-256 |
|---|---|---|
| production/presentation/l014-family-tech-pact.pptx | 2509057 | 9b04a03a64b26f3599910702a75d50854524024499e10b91c2c3456f15048fe3 |
| classroom/L014_我們家的科技公約/02_列印包_科技公約.pdf | 1262416 | 06dba8d2f1c50a4c98d36052c5737696b48b597fedc9b85229646182269faba2 |
| production/narration.json（TTS 輸入） | — | 671e2f0399007123d44d0c93aeffd35d01b3e411cc536966c143f8241e72820b |
| production/template-text.json | — | 3b7f0e850a550527825d4627e283289b8c2ceb7c1c94d5f84e383509701d9f82 |

（PDF 由 Chromium 產生，含時間戳，重跑雜湊會不同；PPTX 在同一環境重跑應相同。）

## 阻擋

1. **Edge TTS 連不上（真正阻擋）。** 本工作階段的網路政策拒絕 `speech.platform.bing.com`：
   `curl https://speech.platform.bing.com/` → `CONNECT tunnel failed, response 403`；
   2026-10-19T02:46Z 以一句公開旁白試 edge-tts 7.3.1 → `SkewAdjustmentError: No server date in headers.`（代理回 403、沒有 Date 標頭）。
   只試了一次，沒有繞過代理、沒有換聲線。之後的 tts、media-check、assemble、delivery、manual review、verify、package、持久交付都依賴音訊，全部沒做。
2. **官方來源讀不到。** 同一政策擋住 safety.google、support.apple.com、healthychildren.org、i.win.org.tw、教育部 PDF 等；擷取工具回 ENOTFOUND。
   查核改用先前課次的逐字引文＋本次搜尋摘要，`production/fact-check.md` 與 `source-notes.md` 已逐條標示。
   **有網路的環境請先重讀這些頁面**，確認引文仍成立再交付（至少教育部注意事項 2.1、Apple 螢幕使用時間／購買前詢問、AAP Family Media Plan、iWIN）。

解法：在環境設定的 Network access 加入 `speech.platform.bing.com`（與上列來源網域），或改用網路較寬的環境，開新工作階段接續。

## 下一條命令（在 `academy/`）

```sh
EP=episodes/academy/l014-family-tech-pact
./portable-runtime.sh python pipeline/preflight.py
curl -sS -o /dev/null -w "%{http_code}\n" https://speech.platform.bing.com/   # 不是 403 才繼續
# （若重讀來源後改了旁白：先跑 authoring/l014/prepare_content.py 與 run deck，重看 12 頁）
nohup ./portable-runtime.sh python pipeline/academy.py run tts --episode "$EP" > /tmp/l014-tts.log 2>&1 &
```

之後依 `docs/CLAUDE_HANDOFF.md` 第 4 節：合成後先整幕語音辨識檢查「AI」與破音字 → media-check → assemble（背景）→ delivery →
manual-review → verify → write_report → package `delivery/L014-v1` → split_delivery → record_delivery → status.py --write → commit。

## 是否需要重驗

- 目前沒有任何 verify 結果；接續後全部下游都要第一次跑。
- 旁白、投影片或教材若因重讀來源而修改，要重跑 prepare_content／deck／classroom，並重看逐頁 PNG 與列印包。
- 不要沿用 L013 或其他課的音訊、字幕時間、QC 或發布紀錄。

## 授權與邊界

- 使用者在本次指令同意把 L014 公開旁白稿送 Microsoft Edge TTS（zh-TW-YunJheNeural），不送私人錄音或其他私人資料；已寫入 manifest。
- 不使用付費 LLM API；不登入、不上傳、不公開 YouTube。
