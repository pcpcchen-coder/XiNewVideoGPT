#!/usr/bin/env python3
"""Build lesson-independent delivery attachments AFTER assembly, BEFORE verify.

Authored classroom files and summary are inputs, not invented from the previous lesson.
"""
from pathlib import Path
import argparse
import json
import subprocess
import zipfile
import academy as a

def build(ep):
    a.media_check(ep)
    p=ep/'production'; m=a.read(p/'manifest.json'); t=a.read(p/'timing.json')
    assembly=a.read(ep/'qc/assembly.json'); n=a.read(p/'narration.json')
    intro=float(assembly['opening']['seconds']); cursor=intro
    chapters=[{'seconds':0,'title':'陳犀牛系列片頭'}]
    for s in t['scenes']:
        chapters.append({'seconds':round(cursor,3),'title':s['title']}); cursor+=s['duration']
    def stamp(seconds):
        total=int(seconds); h,rest=divmod(total,3600); mm,ss=divmod(rest,60)
        return f'{h:02d}:{mm:02d}:{ss:02d}' if h else f'{mm:02d}:{ss:02d}'
    lines='\n'.join(f'{stamp(c["seconds"])} {c["title"]}' for c in chapters)+'\n'
    summary=(p/'delivery-summary.md').read_text(encoding='utf-8').strip()
    if not summary or '待編寫' in summary: raise ValueError('Author delivery-summary.md first')
    if not (p/'fact-check.md').is_file(): raise ValueError('Missing fact-check.md')
    files=sorted(f for f in (ep/'classroom').rglob('*') if f.is_file())
    if not files: raise ValueError('Author actual classroom materials first')
    allowed={'.md','.txt','.csv','.json','.html','.pdf','.pptx','.xlsx','.png','.jpg','.jpeg','.svg'}
    for f in files:
        if f.is_symlink() or f.suffix.lower() not in allowed or any(x.startswith('.') or x=='private' for x in f.relative_to(ep/'classroom').parts):
            raise ValueError('Unexpected classroom file: '+str(f))
    with zipfile.ZipFile(ep/'output/classroom.zip','w',zipfile.ZIP_DEFLATED) as z:
        for f in files: z.write(f,f.relative_to(ep/'classroom'))
    description=f"父子科技學院 {m['episode']}｜{m['title']}\n\n{summary}\n\n章節\n{lines}\n"
    description+='旁白：Edge-TTS zh-TW-YunJheNeural 合成語音。字幕已燒入影片，開啟 CC 可能重疊。\n'
    (p/'chapters.txt').write_text(lines,encoding='utf-8')
    (p/'youtube-description.txt').write_text(description,encoding='utf-8')
    a.write(p/'youtube-metadata.json',{'title':f"父子科技學院 {m['episode']}｜{m['title']}",
         'description':description,'chapters':chapters,'privacyStatus':'private',
         'madeForKids':None,'reviewStatus':'needs-parent-review','publicationMode':'manual-user-upload'})
    (p/'narration-script.md').write_text('\n\n'.join(f"## {s['slide']:02d} {s['title']}\n\n"+'\n\n'.join(x['text'] for x in s['sentences']) for s in n)+'\n',encoding='utf-8')
    (p/'START_HERE.md').write_text(f"# {m['episode']} {m['title']}\n\n{summary}\n\n"
        f"播放 {ep.name}-zh-TW.mp4，實測 {assembly['masterDuration']:.2f} 秒。\n"
        f"全片字幕 zh-TW.srt 已含實測片頭 {intro:.3f} 秒；不可使用 source SRT 替代。\n\n"
        'classroom.zip 是練習教材。課堂 120 分鐘與影片片長分開。\n'
        '母帶無燒錄字幕，簡報可編輯，另附純旁白、文字稿、章節、來源與 QC。\n'
        '本包未上傳 YouTube，由使用者播放檢查及上傳。\n',encoding='utf-8')
    inputs=sum([['-i',str(ep/s['audio'])] for s in t['scenes']],[])
    count=len(t['scenes'])
    fc=''.join(f"[{i}:a]apad,atrim=duration={s['duration']:.9f},asetpts=PTS-STARTPTS[p{i}];" for i,s in enumerate(t['scenes']))
    fc+=''.join(f'[p{i}]' for i in range(count))+f'concat=n={count}:v=0:a=1,loudnorm=I=-16:TP=-1.5:LRA=11[a]'
    subprocess.run(['ffmpeg','-y','-v','error',*inputs,'-filter_complex',fc,'-map','[a]','-ar','48000','-ac','2','-b:a','192k',str(ep/'output/narration-only.mp3')],check=True)
    print('Delivery attachments built. Review, then run verify and package.')
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--episode',required=True)
    args=p.parse_args();build((a.ROOT/args.episode).resolve())
