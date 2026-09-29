#!/usr/bin/env python3
"""Restore only the three large L003 outputs from the exact verified handoff ZIP."""
import argparse
import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def restore(archive):
    inventory = json.loads((ROOT / 'docs/cloud-migration/file-inventory.json').read_text())
    if digest(archive) != inventory['archive']['sha256']:
        raise ValueError('Archive SHA-256 differs from the verified L003 handoff')
    with zipfile.ZipFile(archive) as z:
        for item in inventory['files']:
            if item['storage'] != 'handoff-archive-only':
                continue
            target = (ROOT / item['path']).resolve()
            if not target.is_relative_to(ROOT.resolve()):
                raise ValueError('Unsafe destination')
            if target.exists():
                if digest(target) != item['sha256']:
                    raise FileExistsError(f'Refusing to replace modified file: {item["path"]}')
                print('Already verified:', item['path'])
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(dir=target.parent) as tmp:
                staged = Path(tmp) / 'restored'
                with z.open('XiNewVideoGPT-academy/' + item['path']) as source, staged.open('wb') as out:
                    shutil.copyfileobj(source, out)
                if staged.stat().st_size != item['bytes'] or digest(staged) != item['sha256']:
                    raise ValueError('Restored content mismatch: ' + item['path'])
                staged.replace(target)
            print('Restored:', item['path'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    restore(parser.parse_args().archive)
