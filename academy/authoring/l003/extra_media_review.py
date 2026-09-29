"""Source-audio comparisons and representative final captioned frames."""
from pathlib import Path
import json, subprocess
import numpy as np
from scipy.signal import correlate

R=Path(__file__).resolve().parents[2]
E=R/'episodes/academy/l003-keyboard-ninja'
t=json.loads((E/'production/timing.json').read_text())
a=json.loads((E/'qc/assembly.json').read_text())
master=E/f'output/{E.name}-master.mp4'
zh=E/f'output/{E.name}-zh-TW.mp4'
q=E/'qc/video-frames';q.mkdir(exist_ok=True)
def pcm(path,start,duration,channels=1):
    raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(start),'-i',str(path),'-t',str(duration),'-vn','-ar','48000','-ac',str(channels),'-f','f32le','-'])
    return np.frombuffer(raw,dtype=np.float32).reshape(-1,channels)
intro_src=pcm(R/'assets/opening/開場影片-v2.mp4',0,30,2)
intro_out=pcm(master,0,30,2)
intro_corr=[float(np.corrcoef(intro_src[:,i],intro_out[:len(intro_src),i])[0,1]) for i in range(2)]
results=[];cursor=a['opening']['seconds']
for scene in t['scenes']:
    # A ten-second spoken sample, avoiding scene edges and initial silence.
    expected=pcm(E/scene['audio'],2,min(10,scene['duration']-3))[:,0]
    actual=pcm(master,cursor+1.3,len(expected)/48000+1.4)[:,0]
    lag=int(np.argmax(correlate(actual,expected,mode='valid',method='fft')))
    aligned=actual[lag:lag+len(expected)]
    corr=float(np.corrcoef(expected,aligned)[0,1])
    results.append({'slide':scene['slide'],'sampleSeconds':len(expected)/48000,'correlation':corr,'offsetVsTimingSeconds':round(lag/48000-.7,6)})
    subprocess.run(['ffmpeg','-y','-v','error','-ss',str(cursor+4),'-i',str(zh),'-frames:v','1',str(q/f"slide_{scene['slide']:02d}.png")],check=True)
    cursor+=scene['duration']
for label,when in [('opening',30),('opening-transition',60.6)]:
    subprocess.run(['ffmpeg','-y','-v','error','-ss',str(when),'-i',str(zh),'-frames:v','1',str(q/f'{label}.png')],check=True)
report={'analysisSampleRate':48000,'openingFirst30SecondsChannelCorrelations':intro_corr,'narrationSamples':results,'scope':'Audio correlation confirms matching sampled source content; not a full human listening review or YouTube copyright result.','passed':min(intro_corr)>=.99 and min(x['correlation'] for x in results)>=.99}
(E/'qc/audio-provenance.json').write_text(json.dumps(report,indent=2)+'\n')
print('Opening correlations:',intro_corr)
print('Narration minimum correlation:',min(x['correlation'] for x in results))
assert report['passed']
