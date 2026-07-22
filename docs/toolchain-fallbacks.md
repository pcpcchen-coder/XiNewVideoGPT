# 工具替代策略

完整重製版已把 Kimi 專用流程改造成一般 GitHub／Codex 環境可重建的產線。

| 能力 | 完整重製版採用 | 限制／處理 | 後續可替代 |
|---|---|---|---|
| 教學視覺 | OpenAI 圖像生成＋人工版面 | 圖中不生成文字，標籤留給 PPT | Stable Diffusion／ComfyUI、3D、攝影素材 |
| IP 一致角色 | 設定圖約束＋四姿勢透明素材 | 每次生成需檢查單角、三個琥珀環與服裝 | 角色 LoRA、3D rig、Live2D |
| PPT | Artifact Tool 可編輯物件＋Noto CJK | 最終 PPTX、講者備註與 PNG 都提交 | PowerPoint、Keynote、Google Slides |
| TTS | meSpeak/eSpeak 離線中文＋拼音聲調 | 聲線較偏 AI／機械感，以 EQ、壓縮、空間感修飾 | OpenAI TTS、Azure Speech、ElevenLabs、Piper／Qwen TTS |
| 字幕 | TTS 句級實際音長 | 改稿後必須重跑 `make tts` | WhisperX、faster-whisper、人工校時 |
| 音樂 | FFmpeg 正弦振盪器原創合成 | 32 秒循環，無外部取樣 | DAW 原創、授權音樂、音樂生成模型 |
| 動畫 | FFmpeg zoompan、掃描光、xfade | 保持教學文字可讀，不做過量動態 | Remotion、After Effects、Resolve |
| 混音 | loudnorm＋sidechaincompress | 旁白優先，成品 -16 LUFS | 專業 DAW／人工混音 |
| 品質檢查 | 18 項結構、影音與 decode 檢查 | 另做 PPT 全尺寸與影片抽幀人工檢查 | OCR、字幕碰撞、VMAF、CI |

目前 TTS 供應商已被限制在 `manifest.json` 與單一合成腳本中。日後換成神經網路聲線時，只需保持 `audio/slide_NN.mp3`、`timing.json` 與 `tts-manifest.json` 的介面，不必重寫影片組裝流程。
