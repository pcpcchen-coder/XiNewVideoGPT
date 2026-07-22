# 工具替代策略

這個版本已把原 Kimi 專用環境改造成一般 GitHub／Codex 環境可重建的產線。

| 能力 | 原來源依賴 | 本集採用 | 後續可替代 |
|---|---|---|---|
| 投影片生圖 | Kimi image generation | 保留已驗證教學底圖 | OpenAI image generation、Stable Diffusion／ComfyUI、人工 SVG／PPT |
| IP 一致角色 | 無固定角色管線 | 參考圖約束生成＋四姿勢透明素材 | 角色 LoRA、3D rig、Live2D |
| TTS | Kimi audio generation | 沿用已完成且通過 ASR 的第一集音訊 | OpenAI TTS、ElevenLabs、Azure Speech、本地 Piper／Qwen TTS |
| ASR | faster-whisper small | 沿用來源 ASR 驗證紀錄 | faster-whisper、WhisperX、OpenAI transcription |
| 影片組裝 | FFmpeg | FFmpeg H.264/AAC＋微量 zoompan | Remotion、MoviePy、Premiere／Resolve |
| 字幕字型 | 沙盒內 Noto CJK | 倉庫自帶 Noto Sans CJK TC | 系統 Noto CJK、思源黑體 |
| 品質檢查 | 17 項來源驗收 | 數量／alpha／codec／尺寸／decode 自動檢查 | 加入 OCR、字幕重疊偵測、VMAF、人工抽幀 |

第一集的優先目標是驗證「IP 講師＋既有教材」的融合效果，所以音訊內容不做重新配音；第二集起可把 TTS 聲線也固定為 XiNew 專屬聲音，並在 manifest 記錄 provider、voice、seed 與版本。

