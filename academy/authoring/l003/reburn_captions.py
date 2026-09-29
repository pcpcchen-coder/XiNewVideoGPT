"""Apply verified cloud libass margins to the completed master."""
from pathlib import Path
import json, subprocess
R=Path(__file__).resolve().parents[2]
E=R/'episodes/academy/l003-keyboard-ninja'
style=json.loads((E/'qc/subtitle-layout.json').read_text())['style']
src=E/f'output/{E.name}-master.mp4'
out=E/f'output/{E.name}-zh-TW.mp4'
stage=out.with_name(out.stem+'-staged.mp4')
subprocess.run(['ffmpeg','-y','-v','error','-threads','2','-i',str(src),'-filter_threads','2','-vf',f"subtitles='{E}/subtitles/zh-TW.srt':fontsdir='{R}/assets/fonts':force_style='{style}'",'-c:v','libx264','-threads','4','-preset','medium','-crf','17','-c:a','copy','-movflags','+faststart',str(stage)],check=True)
stage.replace(out)
p=E/'qc/assembly.json';a=json.loads(p.read_text());a['subtitleRenderer']='libass';a['subtitleStyle']=style;a['subtitleLayoutCheck']='qc/subtitle-layout.json';p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print('Captioned video rebuilt with verified safe margins')
