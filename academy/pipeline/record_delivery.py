#!/usr/bin/env python3
"""Record a verified, packaged and handed-over lesson: delivery.json, publication status, registry.

Run only after verify passed, the package exists, the split ZIP was restore-tested
(pipeline/split_delivery.py) and the parts were actually handed to the user. It reads
measured values from this lesson's own QC files; it measures nothing itself and never
uploads. A failed verify or a missing review record stops it.

    ./portable-runtime.sh python pipeline/record_delivery.py --episode episodes/academy/<slug> \
        --package delivery/L005-v1 --split split.json --attachments attachments.json \
        --session https://claude.ai/code/session_... --not-done "real search results not verified" \
        --next "L006 …"

attachments.json maps each part file name to the id returned when it was handed over.
"""
from pathlib import Path
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = ['qc/report.md', 'qc/manual-review.md', 'qc/slide-visual-review.md']
NOT_DONE = ['human full listening review', 'PowerPoint/Keynote open test', 'macOS hands-on test', 'YouTube copyright check']


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def dump(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def entry(file, **extra):
    return {'filename': file.name, 'bytes': file.stat().st_size, 'sha256': sha256(file), **extra}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--episode', required=True, type=Path)
    p.add_argument('--package', required=True, type=Path)
    p.add_argument('--split', required=True, type=Path, help='JSON printed by split_delivery.py')
    p.add_argument('--attachments', required=True, type=Path)
    p.add_argument('--session', required=True)
    p.add_argument('--date', required=True, help='YYYY-MM-DD of this delivery')
    p.add_argument('--not-done', action='append', default=[])
    p.add_argument('--next', required=True, dest='next_lesson')
    a = p.parse_args()
    ep = (ROOT / a.episode).resolve()
    pkg = (ROOT / a.package).resolve()
    manifest = load(ep / 'production/manifest.json')
    lesson, slug = manifest['episode'], manifest['slug']
    report = load(ep / 'qc/report.json')
    if report['passed'] != report['total']:
        raise SystemExit('verify did not pass; nothing recorded')
    for name in REVIEWS:
        if not (ep / name).is_file():
            raise SystemExit(f'Missing review record: {name}')
    checks = load(pkg / 'checksums.json')
    for name, digest in checks.items():
        if sha256(pkg / name) != digest:
            raise SystemExit(f'Package file changed after packaging: {name}')
    split, attached = load(a.split), load(a.attachments)
    missing = [x['name'] for x in split['parts'] if x['name'] not in attached]
    if missing:
        raise SystemExit(f'Parts without a hand-over id: {missing}')
    assembly, media, asr = load(ep / 'qc/assembly.json'), load(ep / 'qc/media-review.json'), load(ep / 'qc/asr-review.json')
    tts = load(ep / 'production/tts-manifest.json')
    loud = next(c['detail'] for c in report['checks'] if c['check'] == 'loudness')
    lufs = float(re.search(r'-?\d+(\.\d+)?', loud).group())
    zh, master = pkg / f'{slug}-zh-TW.mp4', pkg / f'{slug}-master.mp4'
    zip_name = split['zip']
    authoring = sorted(x.relative_to(ROOT).as_posix() for x in (ROOT / 'authoring' / lesson.lower()).glob('*.py'))
    title = manifest['title']

    dump(ep / 'delivery.json', {
        'schemaVersion': 1, 'lessonId': lesson, 'episodePath': ep.relative_to(ROOT).as_posix(), 'version': pkg.name,
        'createdAt': a.date, 'producedBy': 'Claude (cloud Linux session) via portable-runtime.sh + ooxml-template',
        'status': 'verified', 'publicationStatus': 'awaiting_user_upload',
        'contentMode': 'curriculum-based-preclass (no recording)',
        'durationSeconds': round(assembly['masterDuration'], 3), 'openingSeconds': assembly['opening']['seconds'],
        'voice': tts['voice'], 'ttsEngine': f"edge-tts {tts['packageVersion']}", 'backgroundMusic': 'none under teaching slides',
        'renderOptions': manifest.get('renderOptions', {}),
        'validation': {'passed': report['passed'], 'total': report['total'], 'integratedLufs': lufs,
                       'sceneAudioMaxLagMs': media['maxAbsLagMs'], 'sceneAudioMinCorrelation': media['minCorrelation'],
                       'asrMinSimilarity': asr['minSimilarity'], 'asrMeanSimilarity': asr['meanSimilarity'],
                       'captionLineBreak': assembly.get('captionLineBreak', {}).get('mode', 'libass-auto'),
                       'reviewRecords': REVIEWS, 'notDone': NOT_DONE + a.not_done},
        'package': {'filename': zip_name, 'bytes': split['bytes'], 'sha256': split['sha256'],
                    'contents': f'whitelisted package folder {pkg.name} with checksums.json ({len(checks)} files)',
                    'internalChecksums': checks},
        'largeFiles': [entry(zh, role='captioned video for upload (burned zh-TW subtitles)', inGit=False),
                       entry(master, role='master without burned subtitles', inGit=False),
                       entry(pkg / 'narration-only.mp3', role='narration only, no opening', inGit=False)],
        'inGit': [entry(ep / f'production/presentation/{slug}.pptx', path=f'production/presentation/{slug}.pptx'),
                  entry(ep / 'subtitles/zh-TW.srt', path='subtitles/zh-TW.srt'),
                  entry(ep / 'output/thumbnail.png', path='output/thumbnail.png'),
                  entry(ep / 'output/classroom.zip', path='output/classroom.zip'),
                  entry(ep / 'output/contact-sheet.png', path='output/contact-sheet.png')],
        'persistence': {
            'location': 'Attachments delivered in the Claude session that produced this lesson (private to the account owner)',
            'session': a.session,
            'reason': f"30 MiB per-file attachment limit; the package ZIP was split into {len(split['parts'])} byte-exact parts",
            'parts': [{'filename': x['name'], 'bytes': x['bytes'], 'sha256': x['sha256'],
                       'conversationFileId': attached[x['name']]} for x in split['parts']],
            'restore': f'cat "{zip_name}".part* > "{zip_name}" && shasum -a 256 "{zip_name}"',
            'restoredZip': {'filename': zip_name, 'bytes': split['bytes'], 'sha256': split['sha256']},
            'restoreTested': 'parts re-joined by pipeline/split_delivery.py in the producing session: SHA-256 equals the ZIP; ZIP integrity tested',
            'notUsed': {'gitHubRelease': 'repository is public; a release would make the unpublished video public',
                        'googleDrive': 'connector accepts only inline content; text records only, no large binaries',
                        'git': 'large MP4/MP3 stay out of Git per .gitignore'},
            'ifAttachmentsUnavailable': 'rebuild from Git: audio, slides, PPTX, SRT sources and the shared opening are tracked; '
                                        'run assemble → delivery → verify → package. A rebuild is a new version with new hashes.'},
        'continuation': {
            'state': f'{lesson} complete through package; nothing pending except user playback/listening and manual YouTube upload',
            'rebuildCommands': ['cd academy && ./setup-portable.sh', f'EP={ep.relative_to(ROOT).as_posix()}',
                                './portable-runtime.sh python pipeline/academy.py run media-check --episode "$EP"',
                                './portable-runtime.sh python pipeline/academy.py run assemble --episode "$EP"   # ~20 min on 2 cores; run in background',
                                './portable-runtime.sh python pipeline/delivery.py --episode "$EP"',
                                './portable-runtime.sh python pipeline/academy.py run verify --episode "$EP"',
                                f'./portable-runtime.sh python pipeline/academy.py package --episode "$EP" --output delivery/{lesson}-v2'],
            'doNotRerunWithoutReason': 'run tts (re-synthesises all audio and invalidates timing, subtitles, video and QC)',
            'authoring': authoring,
            'sharedTools': ['pipeline/qa/subtitle_precheck.py', 'pipeline/qa/deck_check.py', 'pipeline/qa/media_review.py',
                            'pipeline/qa/asr_review.py', 'pipeline/split_delivery.py', 'pipeline/record_delivery.py'],
            'nextLesson': a.next_lesson},
        'publication': {'status': 'awaiting_user_upload', 'publisher': 'user', 'uploaded': False, 'videoUrl': None,
                        'uploadFile': zh.name, 'note': 'No login, upload or publication was attempted.'}})

    dump(ep / 'publication/status.json', {
        'lessonId': lesson, 'status': 'awaiting_user_upload', 'publicationMode': 'manual-user-upload', 'publisher': 'user',
        'videoUrl': None, 'targetTitle': f'父子科技學院 {lesson}｜{title}', 'videoFile': zh.name, 'videoSha256': sha256(zh),
        'videoBytes': zh.stat().st_size, 'deliveryVersion': pkg.name, 'deliveryRecord': 'delivery.json',
        'authorizedToUpload': False, 'authorizedToPublish': False,
        'note': f'Produced and packaged {a.date}. Awaiting user playback and manual upload; no YouTube login, upload or publication attempted.'})

    registry_path = ROOT / 'curriculum/production-status.json'
    registry = load(registry_path)
    row = next(x for x in registry['lessons'] if x['lessonId'] == lesson)
    row.update(productionStatus='verified', publicationStatus='awaiting_user_upload', videoUrl=None,
               episodePath=ep.relative_to(ROOT).as_posix(),
               evidence=(f"Produced {a.date} by Claude (portable ooxml-template). verify {report['passed']}/{report['total']}; per-page and "
                         f"per-cue (36) frame review; machine ASR and waveform checks; no human listening review. Package {pkg.name} "
                         f"SHA-256 {split['sha256']} delivered as {len(split['parts'])} session attachments. "
                         f"See {ep.relative_to(ROOT).as_posix()}/delivery.json and qc/manual-review.md."))
    registry['updatedAt'] = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds')
    dump(registry_path, registry)
    print(f"Recorded {lesson} {pkg.name}: verified / awaiting_user_upload; run pipeline/status.py --write")


if __name__ == '__main__':
    main()
