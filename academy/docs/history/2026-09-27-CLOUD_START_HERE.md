> 歷史快照：不代表目前授權或操作入口。現行規則見 ../../series-policy.json。

# 父子科技學院：L003 雲端接續

本副本為 2026-09-27 依 v2 接續包重做 L003 的雲端工作成果。
先讀 docs/cloud-migration/README.md，再讀 docs/production-and-publication-sop.md。

## 本次範圍

使用者已授權製作並公開 L003「鍵盤忍者：快捷鍵競速」。不重傳 L001/L002，不自動製作其他課。
沒有課堂錄音，L003 明確標示依課表製作的課前教學版。
歷史公開：L001 https://youtu.be/JrYLz3D-7p4；L002 https://youtu.be/soztdVd9Xys。
頻道「犀牛說」UCLAQhbdu5MFIDoUPH6bDQuQ。雲端不繼承原 Mac Chrome 登入。
L003 的實際發布狀態以 episodes/academy/l003-keyboard-ninja/publication 為準。

## 素材與模板

v2 是部分接續包：50 個已列檔案通過 SHA-256，另 151 個清單檔案未包含。
原 L001 PPTX 不在包內；本副本的 L001 PPTX 從原 build_l001.mjs 和原角色素材還原，只作套版。
沒有重製 L001 影片，也沒有雲端重驗 L001/L002 舊 QC。
詳細缺項見 docs/cloud-migration/archive-verification.json。

## 從這裡繼續

- curriculum/catalog.json：192 堂、每堂三個動態搜尋入口，共 576 組；並非 576 支人工精選影片。
- lessons/L003/lesson.json：本課課表來源。
- authoring/l003：內容、教材與交付附檔的可重複建置腳本。
- episodes/academy/l003-keyboard-ninja：本課簡報、旁白、字幕、影片、教材、QC 與發布狀態。
- docs/cloud-migration/cloud-porting.patch：必要雲端移植差異。

先設定當地 Python、Node、artifact-tool modules 及 Presentations skill；不要複用本機 .venv。
cloud-runtime.sh 會使用 CODEX_PRIMARY_RUNTIME_*，也允許 RUNTIME_* 與 PRESENTATIONS_SKILL 覆寫。
Python 依賴依 requirements.txt 在當地安裝；edge-tts 本次 7.2.8，可安裝到 .cloud-deps。
公開影片不需要重跑；只在內容修改後重新建置並 verify。deck 保留原逐段替換檢查。

```sh
./cloud-runtime.sh python3 pipeline/academy.py run validate --episode episodes/academy/l003-keyboard-ninja
./cloud-runtime.sh python3 pipeline/academy.py run deck --episode episodes/academy/l003-keyboard-ninja
./cloud-runtime.sh python3 pipeline/academy.py run tts --episode episodes/academy/l003-keyboard-ninja
./cloud-runtime.sh python3 pipeline/academy.py run assemble --episode episodes/academy/l003-keyboard-ninja
./cloud-runtime.sh python3 authoring/l003/delivery.py
./cloud-runtime.sh python3 pipeline/academy.py run verify --episode episodes/academy/l003-keyboard-ninja
```

以上 Python 指令在非原雲端環境須換為當地已安裝依賴的 Python；deck 必須使用當地可用的 artifact-tool 與 Presentations skill。
原 new-episode 指令仍依賴 v2 未附的舊 EP10 seed，因此本課由 authoring/l003 在相同目錄契約建立；未宣稱所有新課次的一鍵初始化都已移植。
production/audio/subtitles/output/slides 任一變動後都要重跑 verify，不能沿用舊指紋。
