#!/usr/bin/env python3
"""Zip a packaged delivery folder and split the ZIP into chat-attachment-sized parts.

Chat attachments are limited to 30 MiB per file, so a ~160 MB delivery ZIP is handed
over as 28 MiB parts plus a restore note. The parts are joined again here and compared
with the ZIP before anything is reported. Nothing is uploaded.

    ./portable-runtime.sh python pipeline/split_delivery.py \
        --package delivery/L005-v1 --name "L005-v1_父子科技學院_課名_2026-10-07"

Writes delivery/<name>.zip, delivery/parts/<name>.zip.partNN,
delivery/parts/<package>_還原說明_RESTORE.txt and prints a JSON summary.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PART = 28 * 1024 * 1024


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package', required=True, type=Path)
    p.add_argument('--name', required=True, help='ZIP base name without .zip')
    a = p.parse_args()
    pkg = (ROOT / a.package).resolve()
    if not (pkg / 'checksums.json').is_file():
        raise SystemExit(f'Not a packaged delivery folder: {pkg}')
    out = pkg.parent
    target = out / f'{a.name}.zip'
    files = sorted(x for x in pkg.iterdir() if x.is_file())
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_STORED) as z:  # media is already compressed
        for f in files:
            z.write(f, f'{pkg.name}/{f.name}')
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None and len(z.namelist()) == len(files)
    size, digest = target.stat().st_size, sha256(target)

    parts_dir = out / 'parts'
    parts_dir.mkdir(exist_ok=True)
    for old in parts_dir.glob(f'{a.name}.zip.part*'):
        old.unlink()
    parts = []
    with open(target, 'rb') as src:
        while True:
            block = src.read(PART)
            if not block:
                break
            part = parts_dir / f'{a.name}.zip.part{len(parts) + 1:02d}'
            part.write_bytes(block)
            parts.append(part)
    joined = hashlib.sha256()
    for part in parts:
        joined.update(part.read_bytes())
    assert joined.hexdigest() == digest, 'joined parts differ from the ZIP'
    rows = [(sha256(x), x.name, x.stat().st_size) for x in parts]

    zip_name = target.name
    win = '+'.join(f'"{n}"' for _, n, _ in rows)
    zh = next((f.name for f in files if f.name.endswith('-zh-TW.mp4')), '字幕版 MP4')
    note = parts_dir / f'{pkg.name}_還原說明_RESTORE.txt'
    note.write_text(f'''父子科技學院 {pkg.name} 交付包：分段檔還原說明

對話附件單檔上限 30 MiB，所以完整交付包切成 {len(parts)} 段。全部下載到同一個資料夾後：

macOS / Linux（終端機，先 cd 到該資料夾）：
  cat "{zip_name}".part* > "{zip_name}"
  shasum -a 256 "{zip_name}"

Windows（PowerShell）：
  cmd /c copy /b {win} "{zip_name}"
  Get-FileHash "{zip_name}" -Algorithm SHA256

還原後的 ZIP 必須是 {size:,} bytes，SHA-256：
  {digest}
不符就代表有分段沒下載完整，請重新下載該段，不要使用。

各分段的 SHA-256：
''' + ''.join(f'{h}  {n}\n' for h, n, _ in rows) + f'''
解壓縮後先讀 {pkg.name}/START_HERE.md 與 UPLOAD_README.md；包內 checksums.json 列有每個檔案的 SHA-256。
上傳 YouTube 用 {zh}（字幕已燒入）；本包尚未上傳，也沒有公開。
''', encoding='utf-8')
    print(json.dumps({'zip': zip_name, 'bytes': size, 'sha256': digest, 'entries': len(files),
                      'partBytes': PART, 'restoreVerified': True, 'restoreNote': note.name,
                      'parts': [{'name': n, 'bytes': b, 'sha256': h} for h, n, b in rows]},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
