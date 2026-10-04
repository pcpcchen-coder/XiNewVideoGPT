import json,subprocess
from pathlib import Path
from PIL import Image,ImageDraw
E=Path(__file__).resolve().parent
q=E/'qc/subtitle-frames';q.mkdir(parents=True,exist_ok=True)
a=json.loads((E/'qc/assembly.json').read_text())
t=json.loads((E/'production/timing.json').read_text())
cur=a['opening']['seconds'];k=0;strips=[]
for scene in t['scenes']:
 for s in scene['sentences']:
  k+=1;sec=cur+(s['start']+s['end'])/2
  p=q/f'{k:02}.png'
  subprocess.run(['ffmpeg','-y','-v','error','-ss',str(sec),'-i',str(E/'output'/f'{E.name}-zh-TW.mp4'),'-frames:v','1',str(p)],check=True)
  im=Image.open(p).convert('RGB');strip=im.crop((0,865,1920,1040)).resize((960,88));strips.append(strip)
 cur+=scene['duration']
out=Image.new('RGB',(960,len(strips)*108),(20,25,30));d=ImageDraw.Draw(out)
for i,im in enumerate(strips):
 d.text((4,i*108),f'{i+1:02}',fill='white');out.paste(im,(0,i*108+20))
out.save(q/'all-caption-strips.png')
print(q/'all-caption-strips.png')
