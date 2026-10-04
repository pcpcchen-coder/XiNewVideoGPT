"""Package this one-off special for live presentation, without external TTS."""
import hashlib, json, shutil, zipfile
from pathlib import Path
E=Path(__file__).resolve().parent
ROOT=E.parents[1]
W=ROOT.parents[1]
OUT=W/'special-output'
PACK=OUT/'SP01_AI_Update_Presentation_Pack'
PACK.mkdir(parents=True,exist_ok=True)
(PACK/'slides').mkdir(exist_ok=True)
(PACK/'sources').mkdir(exist_ok=True)
def sha(p):return hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
ppt=OUT/'SP01_AI_Update_2026-10-04.pptx'
shutil.copy2(ppt,PACK/ppt.name)
opening=ROOT/'assets/opening/開場影片-v2.mp4'
shutil.copy2(opening,PACK/'Opening_v2.mp4')
for p in sorted((E/'assets/slides').glob('*.png')):shutil.copy2(p,PACK/'slides'/p.name)
for name in ['manifest.json','narration.json','sources.json']:shutil.copy2(E/'production'/name,PACK/'sources'/name)
narr=json.loads((E/'production/narration.json').read_text())
src=json.loads((E/'production/sources.json').read_text())
script=['SP01 AI 近期發展：工程團隊怎麼用','資料截至 2026-10-04；分享週 2026-10-05 至 10-11。','建議開場約 1 分鐘，五頁分享約 5–8 分鐘，另留討論時間。','']
for s in narr:
 script += [f"第 {s['slide']} 頁：{s['title']}",*[x['text'] for x in s['sentences']],'']
script += ['官方參考來源（查核 2026-10-04）']
for s in src['sources']:script += [f"{s['id']} {s['date']} {s['publisher']}：{s['title']}",s['url'],s['claim'],'']
script += ['第 5 頁是兩週試行建議，數量與門檻皆為提案，不是已達成實績。']
(PACK/'Speaker_Notes_and_Sources.txt').write_text('\n'.join(script)+'\n')
html=r'''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SP01 AI 近期發展</title>
<style>*{box-sizing:border-box}body{margin:0;background:#041222;color:#f7f7f8;font:16px system-ui,sans-serif}main{height:calc(100vh - 62px);display:flex;align-items:center;justify-content:center}video,img{max-width:100%;max-height:100%;object-fit:contain}img{width:100%;height:100%}[hidden]{display:none!important}nav{height:62px;display:flex;align-items:center;justify-content:center;gap:14px;padding:8px;background:#101b28}button{font:inherit;color:#f7f7f8;background:#19324a;border:1px solid #46c8ff;border-radius:6px;padding:8px 14px;cursor:pointer}button:hover{background:#28516c}#start{position:fixed;inset:0 0 62px;display:flex;align-items:center;justify-content:center;background:#041222e8}#start section{max-width:660px;text-align:center;padding:30px}h1{font-size:38px;line-height:1.3;margin:0 0 20px}#play{background:#ffc12f;color:#041222;border:0;font-weight:700;padding:14px 24px}p{color:#a8b8c9;line-height:1.8}dialog{max-width:760px;width:90vw;background:#101b28;color:#f7f7f8;border:1px solid #46c8ff;border-radius:12px;padding:30px}dialog::backdrop{background:#000b}#noteText{white-space:pre-line;line-height:1.9}#counter{min-width:100px;text-align:center}@media(max-width:600px){nav{gap:6px}button{padding:8px;font-size:13px}h1{font-size:28px}}</style>
<main id="stage"><video id="opening" src="Opening_v2.mp4" controls playsinline preload="metadata"></video><img id="slide" alt="投影片" hidden></main>
<div id="start"><section><h1>AI 近期發展<br>工程團隊怎麼用</h1><p>犀牛說番外篇 SP01<br>原版開場約 60 秒，接續五頁簡報</p><button id="play">播放開場</button><p><button id="skip">直接開始簡報</button></p></section></div>
<nav><button id="previous" aria-label="上一頁">← 上一頁</button><span id="counter">開場</span><button id="next" aria-label="下一頁">下一頁 →</button><button id="notes">講稿</button><button id="fullscreen">全螢幕</button><button id="restart">重播開場</button></nav>
<dialog id="dialog"><h2 id="noteTitle"></h2><div id="noteText"></div><p><button id="close">關閉</button></p></dialog>
<script>const notes=__NOTES__;let index=-1;const $=s=>document.getElementById(s);const v=$('opening'),im=$('slide');
function show(i){index=Math.max(0,Math.min(4,i));v.pause();v.hidden=true;im.hidden=false;im.src='slides/slide_'+String(index+1).padStart(2,'0')+'.png';im.alt=notes[index].title;$('start').hidden=true;$('counter').textContent=(index+1)+' / 5';}
async function start(){index=-1;im.hidden=true;v.hidden=false;v.currentTime=0;$('counter').textContent='開場';$('start').hidden=true;try{await v.play()}catch(e){$('start').hidden=false;}}
$('play').onclick=start;$('restart').onclick=start;$('skip').onclick=()=>show(0);v.onended=()=>show(0);$('next').onclick=()=>show(index+1);$('previous').onclick=()=>show(index-1);
$('notes').onclick=()=>{if(index<0){$('noteTitle').textContent='開場';$('noteText').textContent='播放原版開場後，將自動接到第 1 頁。';}else{$('noteTitle').textContent=notes[index].title;$('noteText').textContent=notes[index].sentences.map(s=>s.text).join('\n\n');}$('dialog').showModal();};$('close').onclick=()=>$('dialog').close();
$('fullscreen').onclick=async()=>{if(document.fullscreenElement)await document.exitFullscreen();else if(document.documentElement.requestFullscreen)await document.documentElement.requestFullscreen();};
document.addEventListener('keydown',e=>{if($('dialog').open)return;if(e.key==='ArrowRight'||e.key==='PageDown'){e.preventDefault();show(index+1);}if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();show(index-1);}if(e.key==='Home')show(0);if(e.key==='End')show(4);});</script></html>'''.replace('__NOTES__',json.dumps(narr,ensure_ascii=False).replace('</','<\\/'))
(PACK/'START_PRESENTATION.html').write_text(html)
readme='''SP01 AI 近期發展：工程團隊怎麼用

這是一次性番外篇，共五頁（含封面），不占用 L001–L192 課程編號。
資料截至 2026/10/04，供 10/05–10/11 團隊分享使用。

現場播放
1. 解壓縮整個 ZIP，保留檔案相對位置。
2. 以 Chrome、Edge 或 Safari 開啟 START_PRESENTATION.html。
3. 點「播放開場」。原片頭 v2 約 60 秒，有原音軌。
4. 片頭結束自動進入第 1 頁。方向鍵或下方按鈕換頁。
5. 簡報正文由你口頭分享，可按「講稿」查看逐頁內容。
6. 點「全螢幕」方便投影；可隨時跳過或重播開場。

PowerPoint 使用
SP01_AI_Update_2026-10-04.pptx 是五頁可編輯簡報，備註含講稿與官方來源。
開場 MP4 為獨立檔，未嵌入 PPTX。可先播放 Opening_v2.mp4，再切到 PowerPoint。
若中文字型不同，建議安裝 repo 隨附 Noto Sans CJK TC，或使用離線播放頁以維持外觀。

內容
1. AI 近期發展與工程團隊
2. OpenAI dots 工作代理
3. GPT-6.1 Sol 與 Claude Sonnet 5.5 的成本
4. Gemini 即時互動與長任務
5. 兩週規格比對試行提案

配音狀態
原開場有聲音。五頁正文尚未合成新旁白，也沒有產生完整配音影片。
自動審核拒絕將本次講稿傳給 Microsoft TTS，需明確同意外送這份講稿後才能接續原聲線配音。
Speaker_Notes_and_Sources.txt 已備妥講稿與來源。

未上傳或公開到 YouTube。
'''
video=E/'output'/f'{E.name}-zh-TW.mp4'
if video.exists():
 report=json.loads((E/'qc/report.json').read_text())
 assert report['passed']==report['total'], 'Video verification must pass before packaging'
 for rel,digest in report['fingerprints'].items():assert sha(E/rel)==digest, 'Verified input changed: '+rel
 (PACK/'audio').mkdir(exist_ok=True)
 for f in (E/'audio').glob('slide_*.mp3'):shutil.copy2(f,PACK/'audio'/f.name)
 (PACK/'qc').mkdir(exist_ok=True)
 for name in ['report.json','assembly.json','loudness-normalization.json','audio-sync.json','manual-review.md']:shutil.copy2(E/'qc'/name,PACK/'qc'/name)
 readme=readme.replace('原開場有聲音。五頁正文尚未合成新旁白，也沒有產生完整配音影片。\n自動審核拒絕將本次講稿傳給 Microsoft TTS，需明確同意外送這份講稿後才能接續原聲線配音。', '完整配音影片已完成，使用原聲線 zh-TW-YunJheNeural。\n2026-10-04 使用者已同意將本次講稿送交 Microsoft TTS。\n直接播放 SP01_AI_Update_2026-10-04_zh-TW.mp4，可觀看含原開場、五頁配音及繁中字幕的完整影片。')
 for suffix,filename in [('zh-TW','SP01_AI_Update_2026-10-04_zh-TW.mp4'),('master','SP01_AI_Update_2026-10-04_master.mp4')]:
  shutil.copy2(E/'output'/f'{E.name}-{suffix}.mp4',PACK/filename)
 shutil.copy2(E/'subtitles/zh-TW.srt',PACK/'SP01_AI_Update_2026-10-04.srt')
 for name in ['timing.json','tts-manifest.json']:shutil.copy2(E/'production'/name,PACK/'sources'/name)
(PACK/'README.txt').write_text(readme)
manifest=[{'path':str(p.relative_to(PACK)),'bytes':p.stat().st_size,'sha256':sha(p)}for p in sorted(PACK.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.json']
(PACK/'SHA256SUMS.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
zipout=OUT/'SP01_AI_Update_Presentation_Pack.zip'
with zipfile.ZipFile(zipout,'w',zipfile.ZIP_DEFLATED,compresslevel=3)as z:
 for p in sorted(PACK.rglob('*')):
  if p.is_file():z.write(p,PACK.name+'/'+str(p.relative_to(PACK)))
assert sha(opening)==sha(PACK/'Opening_v2.mp4')
print(json.dumps({'pptx':str(ppt),'package':str(zipout),'openingSha256':sha(opening),'fileCount':len(manifest),'bytes':zipout.stat().st_size},ensure_ascii=False))
