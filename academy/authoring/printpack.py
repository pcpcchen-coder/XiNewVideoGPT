"""Shared helpers for lesson print packs (HTML -> A4 PDF with a headless Chromium/Chrome).

Lesson scripts own their content; this module only renders and checks the PDF.
Without a browser an existing PDF is kept and reported; a missing PDF is an error.
"""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile

BASE_CSS = '''@page{size:A4;margin:0}*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:"Noto Sans CJK TC","PingFang TC","Microsoft JhengHei",sans-serif;color:#0b2540;font-size:12.5pt;line-height:1.5}
section{width:210mm;height:297mm;padding:14mm 15mm;page-break-after:always;position:relative;overflow:hidden}
header{font-size:9.5pt;color:#4a6a88;border-bottom:1.2pt solid #35a9d6;padding-bottom:2mm;margin-bottom:5mm}
h2{font-size:21pt;margin:0 0 2mm;color:#0b2540}h3{font-size:15pt;margin:0 0 2mm}h4{font-size:10.5pt;margin:2mm 0 0;color:#4a6a88}
small{font-size:10pt;color:#4a6a88;font-weight:400;margin-left:3mm}.lead{margin:0 0 4mm;color:#35506b}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6mm}
table{width:100%;border-collapse:collapse;font-size:11.5pt}th,td{border:.8pt solid #7f9bb3;padding:1.4mm 2.5mm;text-align:left;vertical-align:top}th{background:#e3f3fb}
code{font-family:"Noto Sans Mono","Menlo","Consolas",monospace;font-size:12pt;background:#eef5fa;border-radius:1.5mm;padding:.3mm 1.6mm}
.cut{border:1.6pt dashed #0b2540;border-radius:4mm;padding:5mm 6mm}
.box{border:1.3pt solid #0b2540;border-radius:3mm;padding:3mm 4.5mm}
.line{border-bottom:.9pt solid #7f9bb3;height:9mm}
.note{font-size:10.5pt;color:#35506b}
'''


def document(title, header, pages, extra_css=''):
    body = ''.join(f'<section><header>{header}｜列印包 {i}／{len(pages)}</header>{p}</section>' for i, p in enumerate(pages, 1))
    return (f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{BASE_CSS}{extra_css}</style></head><body>{body}</body></html>\n')


def find_browser():
    candidates = [os.environ.get('XINEW_CHROME'), '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                  shutil.which('chromium'), shutil.which('chromium-browser'), shutil.which('google-chrome'),
                  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                  '/Applications/Chromium.app/Contents/MacOS/Chromium',
                  '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge']
    return next((c for c in candidates if c and Path(c).is_file()), None)


def render(html_path, pdf_path):
    """Print html_path to pdf_path. Returns True when rendered in this run."""
    browser = find_browser()
    if not browser:
        if not Path(pdf_path).is_file():
            raise SystemExit('No Chromium/Chrome found and no existing print pack PDF. Set XINEW_CHROME.')
        print('No browser found: kept the existing print pack PDF unchanged')
        return False
    with tempfile.TemporaryDirectory(prefix='xinew-print-') as t:
        out = Path(t) / 'pack.pdf'
        subprocess.run([browser, '--headless', '--no-sandbox', '--disable-gpu', f'--user-data-dir={t}/profile',
                        '--no-pdf-header-footer', f'--print-to-pdf={out}', Path(html_path).as_uri()],
                       check=True, capture_output=True, timeout=180)
        shutil.copyfile(out, pdf_path)
    return True


def check(pdf_path, pages, needles):
    """Assert page count, embedded fonts and expected text; return the page count."""
    info = subprocess.run(['pdfinfo', str(pdf_path)], capture_output=True, text=True, check=True).stdout
    count = int(next(x for x in info.splitlines() if x.startswith('Pages:')).split()[1])
    assert count == pages, (count, pages)
    fonts = subprocess.run(['pdffonts', str(pdf_path)], capture_output=True, text=True, check=True).stdout.splitlines()[2:]
    assert fonts and all(x.split()[-5] == 'yes' for x in fonts), 'font not embedded'
    text = subprocess.run(['pdftotext', str(pdf_path), '-'], capture_output=True, text=True, check=True).stdout
    for needle in needles:
        assert needle in text, needle
    return count
