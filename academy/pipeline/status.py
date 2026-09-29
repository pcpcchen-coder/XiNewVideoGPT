#!/usr/bin/env python3
"""Validate the 192-lesson registry and display the next requested-work candidate."""
import argparse
import json
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--next', action='store_true')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = records()
    if args.write:
        (ROOT / 'docs/PRODUCTION_STATUS.md').write_text(render(data), encoding='utf-8')
        print('Updated docs/PRODUCTION_STATUS.md (192 lessons)')
    if args.next:
        candidate = next((x for x in data if x['productionStatus'] not in {'verified', 'completed_historical'}), None)
        print(json.dumps(candidate, ensure_ascii=False, indent=2))
    if not (args.next or args.write):
        print('192 lessons / 576 search entries; registry valid')
