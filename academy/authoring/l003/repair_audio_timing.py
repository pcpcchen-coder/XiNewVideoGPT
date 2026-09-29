"""Pad decoded MP3 segments to declared scene durations, preserving video bytes."""
from pathlib import Path
import json,subprocess,tempfile

R=Path(__file__).resolve().parents[2]
E=R/'episodes/academy/l003-keyboard-ninja'
t=json.loads((E/'production/timing.json').read_text())
a=json.loads((E/'qc/assembly.json').read_text())
q=E/'qc'
old=q/'audio-provenance.json'
if old.exists(): (q/'audio-provenance-before-timing-repair.json').write_bytes(old.read_bytes())
def run(cmd):subprocess.run(cmd,check=True)
with tempfile.TemporaryDirectory(prefix='l003-aligned-audio-') as tmp:
    tmp=Path(tmp);intro=tmp/'intro.m4a'
    run(['ffmpeg','-y','-v','error','-i',str(R/'assets/opening/開場影片-v2.mp4'),'-vn','-ar','48000','-ac','2','-c:a','aac','-b:a','192k',str(intro)])
    parts=[intro]+[E/s['audio'] for s in t['scenes']]
    durations=[a['opening']['seconds']]+[s['duration'] for s in t['scenes']]
    inputs=sum([['-i',str(p)] for p in parts],[])
    fc=''.join(f'[{i}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,apad,atrim=duration={durations[i]:.9f},asetpts=PTS-STARTPTS[a{i}];' for i in range(len(parts)))
    fc+=''.join(f'[a{i}]' for i in range(len(parts)))+f'concat=n={len(parts)}:v=0:a=1[aout]'
    base=tmp/'base.m4a';norm=tmp/'normed.wav'
    run(['ffmpeg','-y','-v','error',*inputs,'-filter_complex',fc,'-map','[aout]','-c:a','aac','-b:a','192k',str(base)])
    analysis=subprocess.run(['ffmpeg','-hide_banner','-i',str(base),'-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
    stats=json.loads(analysis.stderr[analysis.stderr.rfind('{'):])
    print('Loudness first pass:',json.dumps(stats),flush=True)
    filter2=('loudnorm=I=-16:TP=-1.5:LRA=11:linear=true:'
             f"measured_I={stats['input_i']}:measured_TP={stats['input_tp']}:"
             f"measured_LRA={stats['input_lra']}:measured_thresh={stats['input_thresh']}:offset={stats['target_offset']}")
    # Preserve the supplied opening waveform when constant gain meets the user's loudness range.
    gain=min(-16-float(stats['input_i']),-1.5-float(stats['input_tp'])-.1)
    predicted=float(stats['input_i'])+gain
    if -18<=predicted<=-14:
        filter2=f'volume={gain:.6f}dB'
        method='measured constant gain; peak headroom preserved within accepted loudness range'
    else:
        method='two-pass loudnorm'
    run(['ffmpeg','-y','-v','error','-i',str(base),'-af',filter2,'-c:a','pcm_s16le',str(norm)])
    (q/'loudness-normalization.json').write_text(json.dumps({'method':method,'analysis':stats,'secondPassFilter':filter2,'predictedIntegratedLUFS':predicted,'requestedRangeLUFS':[-18,-14]},indent=2)+'\n')
    master=E/f'output/{E.name}-master.mp4';fixed=tmp/'master.mp4'
    run(['ffmpeg','-y','-v','error','-i',str(master),'-i',str(norm),'-map','0:v','-map','1:a','-c:v','copy','-ar','48000','-ac','2','-c:a','aac','-b:a','192k','-movflags','+faststart',str(fixed)])
    import shutil
    shutil.copyfile(fixed,master)
    zh=E/f'output/{E.name}-zh-TW.mp4';captioned=tmp/'captioned.mp4'
    run(['ffmpeg','-y','-v','error','-i',str(zh),'-i',str(master),'-map','0:v','-map','1:a','-c','copy','-movflags','+faststart',str(captioned)])
    shutil.copyfile(captioned,zh)
a['loudnessNormalization']=method
a['audioTiming']='Decoded segments padded/trimmed to declared scene duration before concatenation; compensates MP3 encoder padding.'
a['masterDuration']=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(master)],text=True))
(q/'assembly.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print('Repaired audio timing without re-encoding either video stream; duration',a['masterDuration'])
