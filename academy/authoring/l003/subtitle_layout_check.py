"""Render every cue with the actual libass style and measure its occupied band."""
from pathlib import Path
import json, subprocess, tempfile
import numpy as np
from PIL import Image

R=Path(__file__).resolve().parents[2]
E=R/'episodes/academy/l003-keyboard-ninja'
n=json.loads((E/'production/narration.json').read_text())
style='FontName=Noto Sans CJK TC,FontSize=16,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H7A000000,BackColour=&H7A000000,BorderStyle=1,Outline=1.2,Shadow=0,Alignment=2,MarginV=20,MarginL=24,MarginR=24'
results=[]
with tempfile.TemporaryDirectory(prefix='l003-subtitle-layout-') as tmp:
    tmp=Path(tmp)
    for scene in n:
        slide=E/f"assets/slides/slide_{scene['slide']:02d}.png"
        base=np.asarray(Image.open(slide).convert('RGB')).astype(int)
        for i,sentence in enumerate(scene['sentences'],1):
            srt=tmp/'cue.srt';srt.write_text('1\n00:00:00,000 --> 00:00:10,000\n'+sentence['text']+'\n')
            out=tmp/'frame.png'
            subprocess.run(['ffmpeg','-y','-v','error','-i',str(slide),'-vf',f"subtitles='{srt}':fontsdir='{R}/assets/fonts':force_style='{style}'",'-frames:v','1',str(out)],check=True)
            final=np.asarray(Image.open(out).convert('RGB')).astype(int)
            ys,xs=np.where(np.max(np.abs(final-base),axis=2)>8)
            assert len(xs),f'No subtitle pixels: slide {scene["slide"]} sentence {i}'
            bounds=[int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())]
            ok=bounds[1]>=890 and bounds[3]<1025 and bounds[0]>=80 and bounds[2]<1840
            results.append({'slide':scene['slide'],'sentence':i,'bounds':bounds,'safe':ok})
report={'style':style,'safeBand':[890,1025],'cueCount':len(results),'passed':all(r['safe'] for r in results),'cues':results}
(E/'qc/subtitle-layout.json').write_text(json.dumps(report,indent=2)+'\n')
assert report['passed'],[r for r in results if not r['safe']]
print(f'{len(results)}/36 subtitle layouts within safe band; top={min(r["bounds"][1] for r in results)}, bottom={max(r["bounds"][3] for r in results)}')
