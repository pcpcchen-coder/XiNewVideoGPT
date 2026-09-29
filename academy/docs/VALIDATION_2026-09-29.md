# 2026-09-29 repo 整合驗證

## 本次實際執行

| 檢查 | 結果 |
|---|---|
| L003 接續 ZIP | 171 個內容檔案含清單；170 個列檔大小／SHA-256 全部符合 |
| 課表 | L001–L192 連續、無重複；每堂 3 組資源，共 576 組搜尋入口 |
| 單元／整合測試 | `python -m unittest discover -s tests -v`：10/10 通過 |
| 草稿初始化 | L004、L192 成功；課號／slug 不符、L193、路徑跳脫、重複初始化會拒絕 |
| 防止誤交付 | 含待編寫／未完成模板映射的草稿拒絕驗證；不複製舊音訊或 QC |
| L003 配音來源 | 12 段音檔雜湊與旁白、時間表一致 |
| 大型成品還原 | 三個省略輸出成功從精確原包還原；原檔未變更 |
| 共用片頭分段 | 從 Git 分段檔重組至暫存工作區，與原片頭大小／SHA-256 完全一致；不需要手動拼接 |
| 原驗收指紋 | 本集 production/audio/subtitles/output/assets/slides 全部與原 verified-inputs.json 相符 |
| 白名單封裝 | 成功建立本機測試交付包；包含字幕片、母帶、PPTX、SRT、教具、說明與雜湊 |
| 過期驗收拒絕 | 在暫存副本修改 thumbnail 後 package 拒絕，未建立交付資料夾 |
| 文件／語法 | 現行教學內部連結皆可解析；修改的 Python 可編譯；shell 語法通過 |
| 接續狀態 | 下一課 L004，尚未製作；正式 lessons 仍只有 L001–L003 |

## 驗證邊界

- 本次是移植整理、教學與接續程式修正；沒有重新渲染影片或呼叫 TTS。
- L003 的 23/23 技術 QC、−17.2 LUFS、398.848 秒等是原雲端製作證據，本次以雜湊確認相同檔案；不冒充新的人類全片聽審。
- 當次 doctor 可用 ffmpeg、ffprobe、Pillow、python-pptx、openpyxl；Edge-TTS 未安裝，下一次配音前依 requirements-cloud.txt 安裝並測試連線。ASR 未測試，沒有新課堂錄音。
- L004／L192 只測試初始化與草稿門檻；尚無這兩課的影片或教學內容，不能宣稱 192 支成片已完成。
- 沒有登入、上傳或公開 YouTube；L003 狀態是 awaiting_user_upload。平台版權檢查未知。
- 本機測試交付資料夾是封裝驗證中間檔；已保存的原 L003 MP4／接續 ZIP 才是先前交付原件。

執行位置：`academy/`。標準復驗命令：

```sh
./cloud-runtime.sh python -m unittest discover -s tests -v
./cloud-runtime.sh python pipeline/status.py
./cloud-runtime.sh python pipeline/academy.py doctor
```
