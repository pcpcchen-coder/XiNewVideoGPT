from pathlib import Path
import json, subprocess
from PIL import Image
E=Path('episodes/academy/l002-file-treasure');Q=E/'qc/caption-review';Q.mkdir(exist_ok=True)
a=json.loads((E/'qc/assembly.json').read_text());t=json.loads((E/'production/timing.json').read_text());cursor=a['opening']['seconds']
for s in t['scenes']:
    sentence=s['sentences'][1];at=cursor+(sentence['start']+sentence['end'])/2
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(at),'-i',str(E/'output/l002-file-treasure-zh-TW.mp4'),'-frames:v','1',str(Q/f'{s["slide"]:02d}.png')],check=True)
    cursor+=s['duration']
sheet=Image.new('RGB',(1920,810))
for i,p in enumerate(sorted(Q.glob('*.png'))):
    sheet.paste(Image.open(p).resize((480,270)),((i%4)*480,(i//4)*270))
sheet.save(E/'qc/caption-review.jpg')
print('12 captioned scene frames extracted')
