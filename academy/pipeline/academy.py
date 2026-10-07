#!/usr/bin/env python3
"""Local curriculum bridge. Editorial work remains explicit, never fabricated."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "pipeline/templates/academy"


def read(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def write(p, data):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(p)


def sha(p):
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def run(cmd):
    subprocess.run([str(x) for x in cmd], check=True)


def import_curriculum(source, dest):
    import openpyxl
    wb = openpyxl.load_workbook(source, data_only=False)
    def rows(name):
        data = list(wb[name].values)
        return [dict(zip(data[0], r)) for r in data[1:] if r[0] is not None]
    lessons, videos = rows("逐堂課程"), rows("YouTube教材庫")
    ids = [r["總課次"] for r in lessons]
    if len(ids) != 192 or set(ids) != set(range(1, 193)):
        raise ValueError("Expected unique lesson IDs 1–192")
    keys = [(r["總課次"], r["影片序號"]) for r in videos]
    if len(keys) != 576 or set(keys) != {(i, j) for i in ids for j in (1, 2, 3)}:
        raise ValueError("Expected exactly 3 distinct resources per lesson")
    for r in lessons:
        for j in (1, 2, 3):
            if not r.get(f"YouTube 關鍵字 {j}") or not str(r.get(f"YouTube 連結 {j}", "")).startswith("https://www.youtube.com/results?"):
                raise ValueError(f"Missing search entry: {r['總課次']} / {j}")
    data = {"schemaVersion": 1, "source": {"file": Path(source).name, "sha256": sha(source)},
            "lessons": [{"lessonId": f"L{r['總課次']:03d}", "sourceRow": r,
                         "resources": [v for v in videos if v["總課次"] == r["總課次"]]} for r in lessons],
            "supportSheets": {s.title: list(s.values) for s in wb if s.title not in ("逐堂課程", "YouTube教材庫")}}
    if Path(dest).exists() and read(dest) != data:
        raise ValueError("Destination differs; import to a new versioned path")
    write(dest, data)
    print("192 lessons / 576 search entries imported; source workbook unchanged")


def init_lesson(catalog, lesson_id):
    if not re.fullmatch(r"L\d{3}", lesson_id):
        raise ValueError("Use L001–L192")
    lesson = next(x for x in read(catalog)["lessons"] if x["lessonId"] == lesson_id)
    dest = ROOT / "lessons" / lesson_id
    dest.mkdir(parents=True, exist_ok=False)
    for folder in ("private/recordings", "private/transcript", "editorial", "publication"):
        (dest / folder).mkdir(parents=True)
    write(dest / "lesson.json", {**lesson, "curriculumSha256": sha(catalog), "episodePaths": [],
                                "minutes": 120, "status": "planned"})
    r = lesson["sourceRow"]
    (dest / "brief.md").write_text(f"# {lesson_id} {r['課程主題']}\n\n{r['2 小時課程流程']}\n\n"
        f"## 當堂作品\n{r['作品／交付']}\n\n## 驗收\n{r['驗收標準']}\n\n"
        f"## 錄音提問\n{r['錄音重點']}\n\n"
        "公開短片與兩小時課堂分開管理。課程可對應多支影片；episodePaths 由內容核對後填寫。\n", encoding="utf-8")
    (dest / "editorial/README.md").write_text(
        "# 編輯交接\n\n先匯入真實逐字稿，保留 segment ID、時間碼與聽不清楚標記。\n"
        "另寫 cleaned.md、fact-check.md、teaching-notes.md；不要覆寫 raw.json。\n"
        "保留孩子的問題、卡關、修正方法、作品與生活技能，教材新增內容標示為補充。\n"
        "依 docs/pipeline-integration.md 的 12 幕契約編寫 production 檔案；"
        "不要把模板第十集旁白冒充本課錄音。\n", encoding="utf-8")
    print(dest)


def validate_segments(data):
    segments = data["segments"]
    if not segments:
        raise ValueError("Empty transcript")
    last = -1.0
    for i, s in enumerate(segments):
        a, b = float(s["start"]), float(s["end"])
        if not math.isfinite(a + b) or a < 0 or b <= a or a < last or not str(s["text"]).strip():
            raise ValueError(f"Invalid segment {i + 1}")
        last = a  # overlapped speakers are permitted
    return segments


def ingest(lesson_id, source, recording=None):
    dest = ROOT / "lessons" / lesson_id / "private/transcript/raw.json"
    if not (dest.parents[2] / "lesson.json").exists():
        raise ValueError("Initialize lesson first")
    if dest.exists():
        raise FileExistsError("Raw transcript already exists; use a new lesson session copy")
    source = Path(source)
    if source.suffix.lower() == ".srt":
        def seconds(t):
            h, m, s, ms = map(int, re.split(r"[:,]", t))
            return h * 3600 + m * 60 + s + ms / 1000
        segments = []
        for block in re.split(r"\n\s*\n", source.read_text(encoding="utf-8-sig").strip()):
            lines = block.splitlines()
            a, b = lines[1].split(" --> ")
            segments.append({"start": seconds(a), "end": seconds(b), "text": "\n".join(lines[2:])})
    else:
        segments = read(source)["segments"]
    validate_segments({"segments": segments})
    data = {"schemaVersion": 1, "lessonId": lesson_id,
            "source": {"file": source.name, "sha256": sha(source)},
            "segments": [{**s, "id": f"seg-{i:05d}"} for i, s in enumerate(segments, 1)]}
    if recording:
        recording = Path(recording)
        target = dest.parents[1] / "recordings" / recording.name
        if target.exists():
            raise FileExistsError(target)
        data["recording"] = {"file": recording.name, "sha256": sha(recording)}
        shutil.copy2(recording, target)
    write(dest, data)
    print(f"Imported {len(segments)} segments: {dest}")


def transcribe(lesson_id, recording, model):
    from faster_whisper import WhisperModel
    if not Path(model).is_dir():
        raise ValueError("Supply an existing local model directory; no implicit download")
    engine = WhisperModel(str(Path(model).resolve()), device="cpu", compute_type="int8", local_files_only=True)
    segments, info = engine.transcribe(str(recording), language="zh", vad_filter=True)
    data = {"segments": [{"start": s.start, "end": s.end, "text": s.text} for s in segments]}
    with tempfile.TemporaryDirectory() as t:
        source = Path(t) / "asr.json"
        write(source, data)
        ingest(lesson_id, source, recording)


def validate_episode(ep):
    m = read(ep / "production/manifest.json")
    n = read(ep / "production/narration.json")
    s = read(ep / "production/slides.json")
    b = read(ep / "production/storyboard.json")
    if not len(n) == len(s) == len(b) == m["slideCount"] == 12:
        raise ValueError("Current series profile requires 12 scenes")
    edits = read(ep / "production/template-text.json") if m.get("deckRenderer") in {"artifact-tool-template", "ooxml-template"} else []
    if "待編寫" in json.dumps([m, n, s, b, edits], ensure_ascii=False):
        raise ValueError("Unfinished editorial placeholders")
    if m.get("editorialStatus") == "draft":
        raise ValueError("Editorial draft must be reviewed before production")
    for seq in (n, s, b):
        if [x["slide"] for x in seq] != list(range(1, 13)):
            raise ValueError("Scene IDs must be consecutive 1–12")
    if any(len(x["sentences"]) != 3 or any(not y.get("text", "").strip() for y in x["sentences"]) for x in n):
        raise ValueError("Each scene requires 3 nonempty sentences")
    if "我是陳犀牛，保持好奇，我們下次見！" not in n[-1]["sentences"][-1]["text"]:
        raise ValueError("Missing series signoff")
    if m["tts"]["voice"] != "zh-TW-YunJheNeural":
        raise ValueError("Unexpected series voice")
    if m.get("layoutProfile") == "academy-native-v1":
        if any(not x.get("title") or not x.get("eyebrow") for x in s):
            raise ValueError("Missing academy title or eyebrow")
        print("Academy editorial structure valid (not visual acceptance)")
        return
    # Existing supplied layout uses these named fields and illustrations.
    required = {1: ["subtitle", "takeaway"], 2: ["subtitle", "steps", "takeaway"],
                3: ["subtitle", "labels"], 4: ["bullets", "takeaway"],
                5: ["subtitle", "steps", "takeaway"], 6: ["leftTitle", "leftItems", "rightTitle", "rightItems", "takeaway"],
                7: ["bullets", "takeaway"], 8: ["subtitle", "labels"],
                9: ["leftTitle", "leftItems", "rightTitle", "rightItems", "takeaway"],
                10: ["columns"], 11: ["subtitle", "steps", "takeaway"],
                12: ["answer", "explain", "recap", "next", "signoff"]}
    for slide in s:
        for key in ["title", "eyebrow", *required[slide["slide"]]]:
            if key not in slide:
                raise ValueError(f"Slide {slide['slide']} missing {key}")
    print("Editorial structure valid (not factual or visual acceptance)")


def media_check(ep):
    validate_episode(ep)
    timing = read(ep / "production/timing.json")
    if len(timing["scenes"]) != 12:
        raise ValueError("Missing audio scenes")
    tts = read(ep / "production/tts-manifest.json")
    if tts.get("narrationSha256") and tts["narrationSha256"] != sha(ep / "production/narration.json"):
        raise ValueError("Narration or pronunciation changed since TTS: regenerate audio")
    for scene in tts["scenes"]:
        p = ep / scene.get("audio", scene.get("file", ""))
        if sha(p) != scene["sha256"]:
            raise ValueError(f"Audio hash mismatch: {p}")
    n = read(ep / "production/narration.json")
    for i, scene in enumerate(timing["scenes"]):
        validate_segments({"segments": scene["sentences"]})
        if [x["text"] for x in scene["sentences"]] != [x["text"] for x in n[i]["sentences"]]:
            raise ValueError("Narration changed since TTS: regenerate audio")
        if max(x["end"] for x in scene["sentences"]) > scene["duration"] + .1:
            raise ValueError("Subtitle extends beyond scene")
    print("Actual audio hashes and narration/timing match")


def export_slides(ep):
    deck = ep / "production/presentation" / f"{ep.name}.pptx"
    with tempfile.TemporaryDirectory(prefix="xinew-render-") as t:
        t = Path(t)
        run(["soffice", f"-env:UserInstallation={(t / 'profile').as_uri()}", "--headless", "--convert-to", "pdf", "--outdir", t, deck])
        run(["pdftoppm", "-png", "-scale-to-x", "1920", "-scale-to-y", "1080", t / f"{ep.name}.pdf", t / "slide"])
        images = sorted(t.glob("slide-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
        if len(images) != 12:
            raise ValueError("Expected 12 rendered pages")
        (ep / "assets/slides").mkdir(parents=True, exist_ok=True)
        for i, p in enumerate(images, 1):
            shutil.copy2(p, ep / f"assets/slides/slide_{i:02d}.png")


def package(ep, dest):
    media_check(ep)
    report = read(ep / "qc/report.json")
    if not report.get("checks") or any(x.get("status") != "PASS" for x in report["checks"]):
        raise ValueError("Run verification successfully before packaging")
    attestation = read(ep / "qc/verified-inputs.json")
    if attestation != fingerprint(ep):
        raise ValueError("Inputs or deliverables changed after verification; run verify again")
    required = ["production/fact-check.md", "production/START_HERE.md", "production/chapters.txt",
                "production/sources.json", "production/youtube-metadata.json", "production/youtube-description.txt",
                "production/narration-script.md", "output/narration-only.mp3", "output/classroom.zip", "qc/manual-review.md"]
    for rel in required:
        if not (ep / rel).is_file() or not (ep / rel).stat().st_size:
            raise ValueError("Incomplete delivery: " + rel)
    if dest.exists():
        raise FileExistsError(dest)
    # Explicit allowlist; no recordings, transcripts, or unrelated episode files.
    files = [ep / "output" / f"{ep.name}-{suffix}.mp4" for suffix in ("master", "zh-TW")]
    files += [ep / "subtitles/zh-TW.srt", ep / "output/thumbnail.png", ep / "production/presentation" / f"{ep.name}.pptx"]
    for p in files:
        if not p.is_file():
            raise FileNotFoundError(p)
    dest.mkdir(parents=True)
    for p in files:
        shutil.copy2(p, dest / p.name)
    for rel in ("README.md", "production/narration-script.md", "production/youtube-description.txt",
                "production/fact-check.md", "production/START_HERE.md", "production/chapters.txt",
                "production/sources.json", "production/youtube-metadata.json",
                "output/narration-only.mp3", "output/classroom.zip", "qc/report.json", "qc/report.md",
                "qc/manual-review.md"):
        source = ep / rel
        if source.is_file():
            shutil.copy2(source, dest / ("repo-guide.md" if rel == "README.md" else source.name))
    m = read(ep / "production/manifest.json")
    metadata = {"title": m["title"], "description": m.get("subtitle", ""), "chapters": []}
    authored = ep / "production/youtube-metadata.json"
    if authored.is_file():
        content = read(authored)
        metadata.update({k: content[k] for k in ("title", "description", "chapters") if k in content})
    metadata.update(privacyStatus="private", madeForKids=None, reviewStatus="needs-parent-review",
                    publicationMode="manual-user-upload", publicationStatus="awaiting_user_upload",
                    note="Confirm audience, sources and privacy before manual YouTube upload.")
    write(dest / "youtube-draft.json", metadata)
    (dest / "UPLOAD_README.md").write_text(
        f"# {m['episode']} 使用者上傳包\n\n"
        f"上傳 `{ep.name}-zh-TW.mp4`，搭配 `zh-TW.srt`（已含片頭偏移）。\n"
        "標題、說明與章節見 youtube-metadata.json／youtube-description.txt。\n"
        "thumbnail.png 為封面；classroom.zip 為教材。先播放成片再上傳。\n"
        "youtube-draft.json 的 private 是本機草稿預設，並非線上狀態。\n"
        "使用者負責登入、受眾判斷、版權檢查與最後公開。\n"
        "公開後回報影片 URL；沒有 URL／發布證據前，不得標成已公開。\n",
        encoding="utf-8")
    write(dest / "checksums.json", {p.name: sha(p) for p in dest.iterdir() if p.is_file()})
    print(f"Local publication draft: {dest}; not uploaded")


def fingerprint(ep):
    paths = []
    for folder in ("production", "audio", "subtitles", "output", "assets/slides", "classroom"):
        paths.extend(p for p in (ep / folder).rglob("*") if p.is_file())
    return {p.relative_to(ep).as_posix(): sha(p) for p in sorted(paths)}


def new_episode(lesson_id, slug, renderer=None):
    if not re.fullmatch(r"L(?:00[1-9]|0[1-9]\d|1[0-8]\d|19[0-2])", lesson_id):
        raise ValueError("Use L001–L192")
    if not re.fullmatch(re.escape(lesson_id.lower()) + r"-[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("Slug must start with the matching lesson ID, e.g. l004-network-relay")
    lesson_path = ROOT / "lessons" / lesson_id / "lesson.json"
    lesson = read(lesson_path)
    # Load the portable seed before creating any destination; no absent EP10 dependency.
    manifest = read(TEMPLATE / "manifest.json")
    replacements = read(TEMPLATE / "template-text.json")
    ep = ROOT / "episodes/academy" / slug
    ep.mkdir(parents=True, exist_ok=False)
    for folder in ("production/presentation", "assets/slides", "assets/visuals", "audio", "subtitles", "output", "qc", "classroom", "publication"):
        (ep / folder).mkdir(parents=True)
    manifest.update(episode=lesson_id, slug=slug, title=lesson["sourceRow"]["課程主題"],
                    subtitle=lesson["sourceRow"]["學習目標"], lessonIds=[lesson_id], editorialStatus="draft")
    if renderer is not None: manifest["deckRenderer"] = renderer
    manifest["sources"] = {"curriculum": f"lessons/{lesson_id}/lesson.json"}
    write(ep / "production/manifest.json", manifest)
    write(ep / "production/narration.json", [
        {"slide": i, "title": "待編寫", "sentences": [{"text": "待編寫"} for _ in range(3)],
         "sources": [f"lessons/{lesson_id}/lesson.json"], "sourceType": "curriculum-based-preclass"}
        for i in range(1, 13)])
    write(ep / "production/slides.json", [
        {"slide": i, "title": "待編寫", "eyebrow": "父子科技學院"} for i in range(1, 13)])
    write(ep / "production/storyboard.json", [
        {"slide": i, "title": "待編寫", "purpose": "待編寫", "visual": "待編寫",
         "motion": "static + 0.55s fade", "narrationSentences": 3} for i in range(1, 13)])
    write(ep / "production/template-text.json", replacements)
    write(ep / "production/sources.json", manifest["sources"])
    write(ep / "publication/status.json", {"lessonId": lesson_id, "status": "not_uploaded",
          "publicationMode": "manual-user-upload", "publisher": "user", "videoUrl": None})
    (ep / "production/plan.md").write_text((lesson_path.parent / "brief.md").read_text(encoding="utf-8"), encoding="utf-8")
    (ep / "assets/visuals/README.md").write_text(
        "依本課主題與分鏡新增圖解；沿用陳犀牛角色、原片頭及配色。\n"
        "模板只保留版型，不把 L001 或 L003 的內容當成本課教材。\n", encoding="utf-8")
    lesson["episodePaths"].append(ep.relative_to(ROOT).as_posix())
    write(lesson_path, lesson)
    print(f"Created draft only: {ep}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    a = sub.add_parser("import-curriculum"); a.add_argument("source", type=Path); a.add_argument("--output", type=Path, default=ROOT / "curriculum/catalog.json")
    a = sub.add_parser("init"); a.add_argument("lesson"); a.add_argument("--catalog", type=Path, default=ROOT / "curriculum/catalog.json")
    a = sub.add_parser("new-episode"); a.add_argument("lesson"); a.add_argument("--slug", required=True); a.add_argument("--renderer", choices=["artifact-tool-template", "ooxml-template"])
    a = sub.add_parser("ingest"); a.add_argument("lesson"); a.add_argument("source", type=Path); a.add_argument("--recording", type=Path)
    a = sub.add_parser("transcribe"); a.add_argument("lesson"); a.add_argument("recording", type=Path); a.add_argument("--model", type=Path, required=True)
    a = sub.add_parser("run"); a.add_argument("stage", choices=["validate", "media-check", "deck", "render", "tts", "assemble", "verify"]); a.add_argument("--episode", type=Path, required=True)
    a = sub.add_parser("package"); a.add_argument("--episode", type=Path, required=True); a.add_argument("--output", type=Path, required=True)
    sub.add_parser("doctor")
    args = p.parse_args()
    if hasattr(args, "lesson") and not re.fullmatch(r"L(?:00[1-9]|0[1-9]\d|1[0-8]\d|19[0-2])", args.lesson):
        raise ValueError("Use L001–L192")
    if args.command == "import-curriculum": import_curriculum(args.source, args.output)
    elif args.command == "init": init_lesson(args.catalog, args.lesson)
    elif args.command == "new-episode": new_episode(args.lesson, args.slug, args.renderer)
    elif args.command == "ingest": ingest(args.lesson, args.source, args.recording)
    elif args.command == "transcribe": transcribe(args.lesson, args.recording, args.model)
    elif args.command == "doctor":
        import importlib.util
        result = {x: shutil.which(x) for x in ("ffmpeg", "ffprobe", "soffice", "pdftoppm")}
        result.update({x: bool(importlib.util.find_spec(x)) for x in ("PIL", "pptx", "openpyxl", "edge_tts", "faster_whisper")})
        modules = os.environ.get("RUNTIME_NODE_MODULES", "")
        skill = os.environ.get("PRESENTATIONS_SKILL", "")
        result.update({
            "node": os.environ.get("RUNTIME_NODE") or shutil.which("node"),
            "artifact_tool": bool(modules) and (Path(modules) / "@oai/artifact-tool/dist/artifact_tool.mjs").is_file(),
            "presentations_skill_helpers": bool(skill) and (Path(skill) / "container_tools/artifact_tool_utils.mjs").is_file(),
            "chinese_font_file": (ROOT / "assets/fonts/NotoSansCJKtc-Regular.otf").is_file(),
            "opening_v2": (ROOT / "assets/opening/開場影片-v2.mp4").is_file(),
            "restored_l001_template": (ROOT / "episodes/academy/l001-mac-workstation/production/presentation/l001-mac-workstation.pptx").is_file(),
        })
        print(json.dumps(result, indent=2))
        print("faster_whisper is optional when importing an existing transcript")
    else:
        ep = (ROOT / args.episode).resolve()
        if args.command == "package": package(ep, args.output.resolve()); return
        validate_episode(ep)
        if args.stage == "media-check": media_check(ep)
        elif args.stage in ("deck", "render") and read(ep / "production/manifest.json").get("deckRenderer") == "ooxml-template":
            from portable_deck import build
            build(ep)
        elif args.stage in ("deck", "render") and read(ep / "production/manifest.json").get("deckRenderer") == "artifact-tool-template":
            node = os.environ.get("RUNTIME_NODE") or shutil.which("node")
            if not node: raise ValueError("Set RUNTIME_NODE")
            run([node, ROOT / "pipeline/scripts/build_template.mjs", "--episode", ep])
        elif args.stage in ("deck", "render") and read(ep / "production/manifest.json").get("deckRenderer") == "artifact-tool":
            if ep.name != "l001-mac-workstation":
                raise ValueError("Native deck builder is currently authored for L001 only")
            node = os.environ.get("RUNTIME_NODE") or shutil.which("node")
            if not node:
                raise ValueError("Set RUNTIME_NODE to the bundled Node executable")
            run([node, ROOT / "pipeline/scripts/build_l001.mjs"])
        elif args.stage == "render": export_slides(ep)
        elif args.stage != "validate":
            if args.stage in ("assemble", "verify"): media_check(ep)
            script = {"deck": "build_deck", "tts": "synthesize_narration", "assemble": "assemble_episode", "verify": "verify_episode"}[args.stage]
            run([sys.executable, ROOT / "pipeline/scripts" / f"{script}.py", "--episode", ep])
            if args.stage == "verify": write(ep / "qc/verified-inputs.json", fingerprint(ep))


if __name__ == "__main__":
    main()
