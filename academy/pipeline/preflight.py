#!/usr/bin/env python3
"""Portable prerequisites. Exits nonzero on a blocker; never creates lesson output."""
from pathlib import Path
import importlib.util
import json
import shutil
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
def main():
    checks={'python>=3.11':sys.version_info >= (3,11)}
    for exe in ('ffmpeg','ffprobe','soffice','pdftoppm','fc-match'):
        checks[exe]=bool(shutil.which(exe))
    for module in ('PIL','pptx','openpyxl','edge_tts','numpy','scipy','lxml'):
        checks[module]=bool(importlib.util.find_spec(module))
    for file in ('assets/opening/開場影片-v2.mp4','assets/fonts/NotoSansCJKtc-Regular.otf',
                 'episodes/academy/l001-mac-workstation/production/presentation/l001-mac-workstation.pptx'):
        checks[file]=(ROOT/file).is_file()
    if checks['ffmpeg']:
        filters=subprocess.run(['ffmpeg','-hide_banner','-filters'],capture_output=True,text=True,check=True).stdout
        for feature in ('subtitles','loudnorm','ebur128'):
            checks['ffmpeg:'+feature]=feature in filters
    if checks['fc-match']:
        family=subprocess.check_output(['fc-match','-f','%{family}','Noto Sans CJK TC'],text=True)
        checks['installed_cjk_font']='Noto Sans CJK TC' in family
    if checks['soffice']:
        checks['soffice_version']=subprocess.run(['soffice','--headless','--version'],capture_output=True,timeout=45).returncode==0
    result={'checks':checks,'ready':all(checks.values()),
            'notTested':['Edge TTS network/voice availability (tested during authorized TTS)',
                         'visual layout of new lesson', 'free disk space needed for video assembly'],
            'deckRenderer':'ooxml-template','artifactToolRequired':False}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result['ready'] else 1
if __name__=='__main__': sys.exit(main())
