#!/usr/bin/env python3
"""Validate the 192-lesson registry and display the next requested-work candidate."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION = {'planned', 'authoring', 'deck_ready', 'audio_ready', 'assembled', 'verified', 'completed_historical'}
PUBLICATION = {'not_uploaded', 'awaiting_user_upload', 'uploaded_private', 'published_user_reported', 'published_verified', 'published_historical'}


def records():
    catalog = json.loads((ROOT / 'curriculum/catalog.json').read_text())['lessons']
    data = json.loads((ROOT / 'curriculum/production-status.json').read_text())['lessons']
    expected = [f'L{i:03d}' for i in range(1, 193)]
    if [x['lessonId'] for x in catalog] != expected or [x['lessonId'] for x in data] != expected:
        raise ValueError('Catalog and registry must contain L001–L192 exactly once in order')
    for source, entry in zip(catalog, data):
        if source['sourceRow']['課程主題'] != entry['title'] or len(source['resources']) != 3:
            raise ValueError('Catalog title/resource mismatch: ' + entry['lessonId'])
        if entry['productionStatus'] not in PRODUCTION or entry['publicationStatus'] not in PUBLICATION:
            raise ValueError('Unknown status: ' + entry['lessonId'])
        if entry['publicationStatus'].startswith('published_') and not entry.get('videoUrl'):
            raise ValueError('Published state requires video URL: ' + entry['lessonId'])
    return data


def render(data):
    lines = ['# 192 堂製作與發布進度', '',
             '由 `pipeline/status.py --write` 依 production-status.json 產生。製作與發布是兩個獨立狀態。', '',
             '- `completed_historical`／`published_historical`：使用者移交紀錄，本次未重驗。',
             '- `verified`：有本集驗收證據；不表示已上傳。',
             '- `awaiting_user_upload`：交給使用者上傳。',
             '- `published_user_reported`：使用者回報；`published_verified`：另有實際觀察證據。',
             '- `planned`：只規劃，尚未製作。下列課表不會觸發背景執行。', '',
             '| 課號 | 主題 | 製作 | 發布 | 影片 |', '|---|---|---|---|---|']
    for x in data:
        url = f"[YouTube]({x['videoUrl']})" if x.get('videoUrl') else '—'
        title = x['title'].replace('|', '\\|')
        lines.append(f"| {x['lessonId']} | {title} | {x['productionStatus']} | {x['publicationStatus']} | {url} |")
    return '\n'.join(lines) + '\n'


# --- generated status blocks in hand-written docs -------------------------------------------
# Docs carry <!-- academy-status:NAME --> … <!-- /academy-status:NAME --> markers; --write
# refills them from the registry and each delivered lesson's delivery.json, so the prose never
# has to be edited by hand after a delivery.
STATUS_DOCS = ['../CLAUDE.md', 'AGENTS.md', 'CLOUD_START_HERE.md', 'README.md', 'docs/CLAUDE_BATCH_PROMPT.md',
               'docs/CLAUDE_HANDOFF.md', 'docs/NEXT_EPISODE_PROMPT.md', 'docs/FILE_MANIFEST.md']
MARK = re.compile(r'(<!-- academy-status:([a-z-]+) -->)(.*?)(<!-- /academy-status:\2 -->)', re.S)


def _ranges(ids):
    numbers, out = sorted(int(x[1:]) for x in ids), []
    for n in numbers:
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return '、'.join(f'L{a:03d}' if a == b else f'L{a:03d}–L{b:03d}' for a, b in out)


def status_blocks(data):
    delivered = []
    for x in data:
        record = ROOT / (x.get('episodePath') or '_') / 'delivery.json'
        if x['productionStatus'] == 'verified' and x['publicationStatus'] == 'awaiting_user_upload' and record.is_file():
            delivered.append((x, json.loads(record.read_text(encoding='utf-8'))))
    nxt = next((x for x in data if x['productionStatus'] not in {'verified', 'completed_historical'}), None)
    following = f"{nxt['lessonId']}「{nxt['title']}」" if nxt else '（192 堂皆已製作）'
    ids = _ranges(x['lessonId'] for x, _ in delivered) or '（尚無）'
    sentence = (f'{ids} 已由 Claude 製作並交付（verified／awaiting_user_upload，尚未上傳），不重製；'
                f'下一堂是 {following}，接手仍讀狀態表。')
    lines, files = [], []
    for x, d in delivered:
        ep, v = x['episodePath'], d['validation']
        lines.append(f"- {x['lessonId']}「{x['title']}」：{d['createdAt']} 由 Claude 以可攜流程製作，verify {v['passed']}/{v['total']}、"
                     f"逐頁與逐段檢視完成，{d['version']} 已交付；尚未上傳。紀錄見 [delivery.json]({ep}/delivery.json)、"
                     f"[manual-review.md]({ep}/qc/manual-review.md)。")
        rows = ''.join(f"| `{f['filename']}` | {f['bytes']:,} | `{f['sha256']}` |\n" for f in d['largeFiles'])
        pkg = d['package']
        files.append(f"## {x['lessonId']} 大型輸出（{d['version']}，{d['createdAt']}）\n\n| 檔案 | Bytes | SHA-256 |\n|---|---:|---|\n{rows}"
                     f"| `{pkg['filename']}`（完整交付包） | {pkg['bytes']:,} | `{pkg['sha256']}` |\n\n"
                     f"以上未進 Git。交付包以 {len(d['persistence']['parts'])} 個分段檔交付在製作當次的 Claude 對話附件中，"
                     f"各段雜湊、還原命令與包內檔案雜湊見 `{ep}/delivery.json`。\n")
    if nxt:
        lines.append(f"- {nxt['lessonId']}–L192：課表與製作骨架可接續，並非影片已完成，也沒有啟動批次製作。")
        lines.append(f'- 下一堂 {following}。')
    return {'sentence': sentence, 'list': '\n' + '\n'.join(lines) + '\n',
            'large-files': '\n' + '\n'.join(files) + '\n本 repo 為公開，未建立 Release，勿編造下載連結。'
                           '附件無法取得時可依各課 delivery.json 的命令重新組裝，重建結果須作新版本並重新驗收。\n'}


def sync_docs(data):
    blocks, changed = status_blocks(data), []
    for name in STATUS_DOCS:
        path = (ROOT / name).resolve()
        text = path.read_text(encoding='utf-8')
        if not MARK.search(text):
            raise ValueError(f'No academy-status marker in {name}')
        fresh = MARK.sub(lambda m: m.group(1) + blocks[m.group(2)] + m.group(4), text)
        if fresh != text:
            path.write_text(fresh, encoding='utf-8')
            changed.append(name)
    return changed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--next', action='store_true')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = records()
    if args.write:
        (ROOT / 'docs/PRODUCTION_STATUS.md').write_text(render(data), encoding='utf-8')
        print('Updated docs/PRODUCTION_STATUS.md (192 lessons)')
        print('Status blocks refreshed in:', ', '.join(sync_docs(data)) or 'nothing to change')
    if args.next:
        candidate = next((x for x in data if x['productionStatus'] not in {'verified', 'completed_historical'}), None)
        print(json.dumps(candidate, ensure_ascii=False, indent=2))
    if not (args.next or args.write):
        print('192 lessons / 576 search entries; registry valid')
