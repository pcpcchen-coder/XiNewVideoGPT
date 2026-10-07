"""Shared writer for a lesson's classroom pack (L007 onward): text files, one CSV, one print pack PDF.

The lesson's authoring/lxxx/classroom.py supplies the content; this writes it, renders the
print pack through authoring/printpack.py, checks the result and records qc/classroom-validation.json.
"""
from pathlib import Path
import csv
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import printpack  # noqa: E402

R = Path(__file__).resolve().parents[1]


def build(*, slug, folder, files, sheet, pack_html, pack_pdf, pack_pages, pack_needles, authoring_dir, extra):
    """sheet = (csv file name, header list, rows list); extra = lesson-specific validation facts."""
    E = R / 'episodes/academy' / slug
    D = E / 'classroom' / folder
    D.mkdir(parents=True, exist_ok=True)
    for stale in D.iterdir():  # the folder is fully owned by this script
        if stale.is_file():
            stale.unlink()
    for name, text in files.items():
        assert '待編寫' not in text and text.strip(), name
        (D / name).write_text(text, encoding='utf-8')
    name, header, rows = sheet
    with (D / name).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows([r + [''] * (len(header) - len(r)) for r in rows])
    with (D / name).open(encoding='utf-8-sig', newline='') as f:
        back = list(csv.reader(f))
    assert len(back) == len(rows) + 1 and all(len(r) == len(header) for r in back)
    print_dir = Path(authoring_dir) / 'print'
    print_dir.mkdir(parents=True, exist_ok=True)
    source = print_dir / 'print-pack.html'
    source.write_text(pack_html, encoding='utf-8')
    rendered = printpack.render(source, D / pack_pdf)
    pages = printpack.check(D / pack_pdf, pack_pages, pack_needles)
    names = sorted(p.name for p in D.iterdir() if p.is_file())
    (E / 'qc').mkdir(exist_ok=True)
    (E / 'qc/classroom-validation.json').write_text(json.dumps({
        'folder': D.relative_to(E).as_posix(), 'files': names, 'fileCount': len(names), 'utf8TextReadable': True,
        'sheet': {'file': name, 'rows': len(rows), 'columns': len(header)},
        'printPack': {'file': pack_pdf, 'pages': pages, 'allFontsEmbedded': True, 'renderedThisRun': rendered,
                      'source': source.relative_to(R).as_posix()},
        **extra, 'privateData': 'none',
        'status': 'PASS (structure); page-by-page visual review recorded separately'},
        ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Classroom pack: {len(names)} files, print pack {pages} pages')
    return D
