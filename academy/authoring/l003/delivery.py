from pathlib import Path
import json, subprocess

R=Path(__file__).resolve().parents[2]
E=R/'episodes/academy/l003-keyboard-ninja'
P=E/'production'
t=json.loads((P/'timing.json').read_text())
a=json.loads((E/'qc/assembly.json').read_text())
chapters=[{'seconds':0,'title':'陳犀牛系列片頭'}]
cursor=a['opening']['seconds']
for s in t['scenes']:
    chapters.append({'seconds':round(cursor,3),'title':s['title']})
    cursor+=s['duration']
lines='\n'.join(f'{int(c["seconds"])//60:02d}:{int(c["seconds"])%60:02d} {c["title"]}' for c in chapters)
description='''父子科技學院 L003｜鍵盤忍者：快捷鍵競速

爸爸用 Mac mini 示範，孩子用 MacBook Air 跟做。本片依 192 堂課表製作，適合國中生與家長課前暖身、暫停實作。這是課前教學版，不是實際授課錄音。

五項任務：複製貼上、復原、切換 App、Spotlight 搜尋、區域截圖並找到檔案。
先暖身，再進行三輪計時：第一輪建立紀錄、第二輪從相同起點重做、第三輪孩子設計題目給爸爸。五項結果正確才停表，修正時間也算入；不同題目分開記錄。

章節
'''+lines+'''

兩小時課堂：開場10分、示範15分、共同實作40分、休息10分、獨立改造30分、孩子教爸爸10分、錄音整理5分。
今日作品：快捷鍵小抄、三輪紀錄、任務截圖、孩子出題卡。

可以自行建立練習文字：
我的忍者代號：竹風
我會先確認位置，再使用快捷鍵。
今天的目標：五項操作都做對。

第一堂：https://youtu.be/JrYLz3D-7p4
第二堂：https://youtu.be/soztdVd9Xys
Apple 官方操作參考：
https://support.apple.com/zh-tw/102650
https://support.apple.com/zh-tw/102646

講師角色：陳犀牛 Chen XiNew
旁白：Edge-TTS zh-TW-YunJheNeural 合成語音
画面為教學圖解，並非 macOS 操作錄屏；按鍵行為可能依系統、App 與自訂設定而異。
只使用練習文件，截圖前關閉私人視窗與通知，完成後檢查實際結果。
字幕已燒入影片；另有繁中 CC 字幕軌時，開啟 CC 可能看到重疊字幕。
'''.replace('画面','畫面')
(P/'youtube-description.txt').write_text(description,encoding='utf-8')
(P/'chapters.txt').write_text(lines+'\n',encoding='utf-8')
(P/'youtube-metadata.json').write_text(json.dumps({'title':'父子科技學院 L003｜鍵盤忍者：快捷鍵競速','description':description,'chapters':chapters,'privacyStatus':'public','madeForKids':False,'audienceBasis':'以國中生與家長為一般受眾的科技操作課程','reviewStatus':'user-authorized-publication','channelId':'UCLAQhbdu5MFIDoUPH6bDQuQ'},ensure_ascii=False,indent=2)+'\n')
duration=a['masterDuration']
(P/'START_HERE.md').write_text(f'''# L003 鍵盤忍者：快捷鍵競速

先播放 l003-keyboard-ninja-zh-TW.mp4，約 {int(duration)//60} 分 {round(duration)%60:02d} 秒，包含原系列片頭 v2。
這是依課表製作的課前教學版，可暫停實作，沒有真實課堂錄音。

解壓縮 classroom.zip，先讀「爸爸先讀.txt」。教材含練習原稿與工作副本、五項任務、小抄、三輪紀錄、孩子出題卡、驗收與回顧，共 8 個檔案。

交付內容：字幕成片、無字幕母帶（仍含簡報文字與原片頭）、全片時間軸 SRT、12 頁可編輯 PPTX、純旁白 MP3、文字稿、封面、章節、來源、練習包、QC 與雜湊。
SRT 已含本次組裝實測片頭偏移 {a['opening']['seconds']:.3f} 秒；不要把 source SRT 上傳到含片頭的影片。

120 分鐘：開場10、示範15、共同實作40、休息10、獨立改造30、孩子教爸爸10、錄音整理5。
完成條件：五項操作能獨立完成，能解釋一個卡點與解法，爸爸能照孩子出題卡完成。

v2 接續包缺少原 L001 PPTX，本集以包內原 build_l001.mjs 及原素材還原版型，再用原 template renderer 編輯。並未宣稱取得原 PPTX 實體檔或重驗 L001/L002 成片。
YouTube 實際狀態以 publication 收據為準；youtube-draft.json 的 private 是原封裝器預設，不代表線上狀態。
''',encoding='utf-8')
(E/'README.md').write_text('''# 父子科技學院 L003

依 V2 課表製作的課前教學版，主題「鍵盤忍者：快捷鍵競速」。
請先讀 production/START_HERE.md；製作來源、旁白、PPTX、練習包與 QC 均留在本課次。
不含課堂私人錄音，也沒有偽造逐字稿。
''',encoding='utf-8')
inputs=sum([['-i',str(E/s['audio'])] for s in t['scenes']],[])
fc=''.join(f'[{i}:a]apad,atrim=duration={t["scenes"][i]["duration"]:.9f},asetpts=PTS-STARTPTS[p{i}];' for i in range(12))
fc+=''.join(f'[p{i}]' for i in range(12))+'concat=n=12:v=0:a=1,loudnorm=I=-16:TP=-1.5:LRA=11[a]'
subprocess.run(['ffmpeg','-y','-v','error',*inputs,'-filter_complex',fc,'-map','[a]','-ar','48000','-ac','2','-b:a','192k',str(E/'output/narration-only.mp3')],check=True)
print(f'Delivery metadata and narration-only audio complete; {duration:.3f}s')
