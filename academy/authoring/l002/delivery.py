from pathlib import Path
import json, subprocess
E=Path('episodes/academy/l002-file-treasure')
t=json.loads((E/'production/timing.json').read_text())
a=json.loads((E/'qc/assembly.json').read_text())
chapters=[{'seconds':0,'title':'陳犀牛系列片頭'}]; cursor=a['opening']['seconds']
for s in t['scenes']:
    chapters.append({'seconds':round(cursor,3),'title':s['title']});cursor+=s['duration']
lines='\n'.join(f'{int(c["seconds"])//60:02d}:{int(c["seconds"])%60:02d} {c["title"]}' for c in chapters)
description='''父子科技學院｜L002 檔案與資料夾尋寶

爸爸用 Mac mini 示範，孩子用 MacBook Air 跟做。本片依 192 堂課程表製作，適合國中生與家長課前暖身、暫停實作；不是實際授課錄音紀錄。

本堂任務：
① 讀懂檔名、副檔名與路徑。
② 在森林、海岸、太空三個資料夾找出十二個線索。
③ 用 Finder 搜尋，親手比較複製與移動。
④ 完成尋寶紀錄，另存備份並重新開啟確認。

章節
'''+lines+'''

兩小時課堂：開場10分、示範15分、共同尋寶40分、休息10分、獨立改造30分、孩子出題10分、錄音整理5分。
今日作品：L002_尋寶紀錄_v01.txt 與可重複使用的資料夾規則。
沒有教材包時，家長也可自行建立三個資料夾、各放四個文字線索，讓每個檔案提示下一站。

第一堂：https://youtu.be/JrYLz3D-7p4
Apple 官方操作參考：
顯示副檔名 https://support.apple.com/zh-tw/guide/mac-help/mchlp2304/mac
查看路徑 https://support.apple.com/zh-tw/guide/mac-help/mchlp1774/mac
Mac 鍵盤快捷鍵 https://support.apple.com/zh-tw/102650

講師角色：陳犀牛 Chen XiNew
旁白：Edge-TTS zh-TW-YunJheNeural 合成語音
画面為教學圖解，並非 macOS 操作錄屏；介面文字可能隨系統版本不同。
只操作練習副本，遇到同名取代提示先取消；不要改動正式文件。
'''
description=description.replace('画面','畫面')
(E/'production/youtube-description.txt').write_text(description)
(E/'production/youtube-metadata.json').write_text(json.dumps({'title':'父子科技學院 L002｜檔案與資料夾尋寶','description':description,'chapters':chapters,'privacyStatus':'public','madeForKids':False,'reviewStatus':'user-authorized-publication'},ensure_ascii=False,indent=2)+'\n')
(E/'production/START_HERE.md').write_text('''# 第二堂：檔案與資料夾尋寶

先播放 l002-file-treasure-zh-TW.mp4，約 6 分 12 秒，包含既有系列片頭。這是依課表製作的課前教學版，可以暫停跟做，不是授課錄音紀錄。

解壓縮 classroom.zip，爸爸先讀「爸爸先讀.txt」，再把 L002_尋寶 複製到孩子的 文件/Tech Academy。保留原始教材，從 尋寶地圖/01_森林/線索01.txt 開始。

教材包包含：字幕成片、無字幕母帶（保留片頭和簡報文字）、36 段 SRT、12 頁可編輯 PPTX、純旁白 MP3、文字稿、封面、章節說明、官方來源、練習包、檢查報告與檔案雜湊。

兩小時安排：開場10、示範15、共同尋寶40、休息10、獨立改造30、孩子出題10、錄音整理5分鐘。

驗收：完成十二站紀錄；說出檔名、類型、路徑；比較複製和移動；重新開啟備份確認内容。尋寶教材已檢查十二個路徑及六個 RTF 的文字讀取。

YouTube 的實際公開網址與上傳收據放在 publication 目錄。youtube-draft.json 是封裝時的保守草稿設定，不代表線上公開狀態。
''')
inputs=sum([['-i',str(E/s['audio'])] for s in t['scenes']],[])
fc=''.join(f'[{i}:a]' for i in range(12))+'concat=n=12:v=0:a=1,loudnorm=I=-16:TP=-1.5:LRA=11[a]'
subprocess.run(['ffmpeg','-y','-v','error',*inputs,'-filter_complex',fc,'-map','[a]','-ar','48000','-ac','2','-b:a','192k',str(E/'output/narration-only.mp3')],check=True)
print(description)
