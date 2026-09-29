#!/usr/bin/env python3
"""Reassemble the original shared opening from size-limited Git parts."""
import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def restore(root=ROOT, verify=False):
    folder = root / 'assets/opening'
    manifest = json.loads((folder / 'manifest.json').read_text())
    target = folder / manifest['filename']
    if target.exists():
        if target.stat().st_size != manifest['bytes'] or (verify and digest(target) != manifest['sha256']):
            raise ValueError('Shared opening differs from manifest; refusing to overwrite')
        return target
    with tempfile.TemporaryDirectory(prefix='.restore-', dir=folder) as temp:
        staged = Path(temp) / 'opening.mp4'
        with staged.open('wb') as output:
            for item in manifest['parts']:
                source = folder / item['filename']
                if source.stat().st_size != item['bytes'] or digest(source) != item['sha256']:
                    raise ValueError('Shared opening part mismatch: ' + item['filename'])
                with source.open('rb') as stream:
                    shutil.copyfileobj(stream, output)
        if staged.stat().st_size != manifest['bytes'] or digest(staged) != manifest['sha256']:
            raise ValueError('Reassembled opening failed SHA-256 verification')
        staged.replace(target)
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify', action='store_true', help='Also hash an existing restored opening')
    restore(verify=parser.parse_args().verify)
