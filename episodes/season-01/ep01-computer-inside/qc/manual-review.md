# S01E01 人工視聽檢查

## PPTX

- 使用 Artifact Tool 輸出 12 頁可編輯簡報與講者備註。
- 使用 LibreOffice 實際轉譯 12 頁，繁中 Noto Sans CJK TC 顯示正常。
- `slides_test.py`：PASS，未偵測到畫布溢位。
- 逐頁以全尺寸檢查標題、換行、角色、重點框與圖像裁切；第 8、11 頁修正後複查通過。

## 影片

- 從 425.73 秒字幕版每 35 秒抽幀，共 13 張；12 幕、字幕安全區與 XiNew 角色均正常。
- 動畫包含逐幕微推鏡、掃描光，以及 fade、smoothleft、circleopen、wipeup、dissolve、slideleft 六種輪替轉場。
- FFmpeg 完整 decode：0 errors。

## 聲音

- 12 幕、36 句皆為本次重新合成的離線中文 TTS。
- 背景音樂為原創《Data Kitchen》32 秒循環，無外部取樣。
- 完成版 EBU R128：整體音量 **-16.0 LUFS**、LRA **2.5 LU**、True Peak **-2.1 dBFS**。
- 音訊輸出：AAC、48 kHz、雙聲道。
