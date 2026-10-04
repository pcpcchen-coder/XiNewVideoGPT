import json,subprocess
from pathlib import Path
import numpy as np
from scipy.signal import correlate
E=Path(__file__).resolve().parent
a=json.loads((E/'qc/assembly.json').read_text());t=json.loads((E/'production/timing.json').read_text());cur=a['opening']['seconds'];results=[]
def pcm(p,start,duration):
 b=subprocess.check_output(['ffmpeg','-v','error','-ss',str(start),'-i',str(p),'-t',str(duration),'-ac','1','-ar','8000','-f','f32le','-'])
 return np.frombuffer(b,dtype='<f4')
for s in t['scenes']:
 mid=s['duration']/2
 ref=pcm(E/s['audio'],mid,3)
 actual=pcm(E/'output'/f'{E.name}-master.mp4',cur+mid-.25,3.5)
 c=correlate(actual,ref,mode='valid',method='fft')
 lag=np.argmax(c)/8000-.25
 results.append({'slide':s['slide'],'offsetSeconds':round(float(lag),5),'passed':bool(abs(lag)<.06)})
 cur+=s['duration']
(E/'qc/audio-sync.json').write_text(json.dumps({'method':'Cross-correlate scene midpoint audio against decoded master at measured scene offset; 8 kHz mono; tolerance 60 ms','probes':results,'passed':all(r['passed']for r in results)},indent=2)+'\n')
print(results)
assert all(r['passed']for r in results)
