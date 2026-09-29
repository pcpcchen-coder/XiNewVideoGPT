"""Author L003 in the supplied repository contract; no recording is implied."""
from pathlib import Path
import json

R = Path(__file__).resolve().parents[2]
E = R / 'episodes/academy/l003-keyboard-ninja'
P = E / 'production'
for d in ('production/presentation','assets/slides','assets/visuals','audio','subtitles','output','qc','publication'):
    (E/d).mkdir(parents=True,exist_ok=True)
S = {
 'curriculum':'curriculum/catalog.json：L003；來源 V2 Excel 逐堂課程第 3 堂',
 'keys':'https://support.apple.com/zh-tw/102650',
 'screenshot':'https://support.apple.com/zh-tw/102646',
}
scenes = [
('鍵盤忍者：快捷鍵競速',[
 '歡迎回到父子科技學院，我是陳犀牛，今天是第三堂，鍵盤忍者，這是依課表製作的課前教學版，並非實際上課錄音。',
 '爸爸用 Mac mini 示範，孩子用 MacBook Air 跟做，一起練習複製貼上、復原、切換應用程式、Spotlight 搜尋與截圖。',
 '準備一份沒有個人資料的練習文件，先熟悉五個動作，再進行三輪計時挑戰，最後由孩子設計題目給爸爸。'],['curriculum']),
('三輪挑戰，先求正確',[
 '第一輪記下完成時間與錯誤，第二輪從相同起點重做，第三輪交換出題；可以看小抄，做錯先修正，再繼續計時。',
 '先找到 Command 鍵，按住它再按指定的按鍵，完成後放開，觀察目前使用中的應用程式有沒有出現預期結果。',
 '爸爸示範時可以暫停，等五個動作都做對再比較時間，目標是看見自己的進步，不用和別人的速度比。'],['curriculum','keys']),
('複製貼上，先確認位置',[
 '在練習文件選取「我的忍者代號：竹風」這一行，按 Command 加 C，將選取的文字放進剪貼板。',
 '接著點到下一行，確認插入游標在目的位置，再按 Command 加 V，原來的文字會保留，這裡多出一份。',
 '請檢查兩行是不是相同，有沒有漏字或貼錯位置，再向爸爸說明選取內容和放置游標各自有什麼作用。'],['keys','curriculum']),
('復原，回到修改前',[
 '在文字後面加上「測試」兩個字，再按 Command 加 Z，觀察剛才的修改是否被復原，讓文件回到前一個狀態。',
 '想重做時，常見組合是 Shift、Command 加 Z，但哪些動作可以復原，仍要看目前的應用程式與選單。',
 '這四組按鍵幫你編輯文字，今天只用練習副本操作，重要作品仍要存檔與備份，不能把復原當成萬能保險。'],['keys']),
('切換 App，讓工具接力',[
 '先開啟文字編輯與 Finder，按住 Command，再按 Tab，畫面會讓你選擇已經開啟的應用程式。',
 '保持按住 Command，繼續按 Tab 移動選擇，選到需要的程式後放開 Command，就能完成切換。',
 '請在文字編輯和 Finder 之間來回兩次，這個動作切換的是應用程式，不一定是同一程式中的不同視窗。'],['keys']),
('Spotlight 幫你找工具',[
 '按 Command 加空白鍵，通常會開啟 Spotlight，輸入「文字編輯」，確認搜尋結果，再開啟需要的工具。',
 '如果按鍵變成切換輸入法，或沒有作用，先和爸爸到系統設定的鍵盤快速鍵，查看 Spotlight 的設定與按鍵衝突。',
 '快捷鍵可以被調整，所以卡住時先觀察畫面與設定，再試一次，完成後回到剛才的練習文件。'],['keys']),
('截圖，只留下需要的範圍',[
 '按 Shift、Command 加四，指標會變成十字，拖出需要的範圍，放開滑鼠或觸控式軌跡板，就會拍攝截圖。',
 '選錯範圍可以按 Escape 取消；如果要拍整個螢幕，則使用 Shift、Command 加三。',
 '今天只截取練習文字，先關閉會露出私人資料的視窗和通知，再確認選取範圍，避免把帳號或其他人的資訊拍進去。'],['screenshot']),
('截圖完成，還要找得到',[
 '按 Shift、Command 加五，開啟截圖工具，在選項裡查看儲存位置，今天練習拍照，不需要啟動錄影。',
 '截圖預設通常存在桌面，也可以改到其他位置，找不到時先確認目前設定，再去對應資料夾尋找。',
 '找到後打開截圖，確認文字完整而且沒有私人資訊，再把作品收進本課資料夾，按完快捷鍵還要檢查結果。'],['screenshot','curriculum']),
('第一、二輪：和自己比',[
 '暖身後開始第一輪，依序完成複製貼上、加字再復原、切換應用程式、用 Spotlight 找工具，以及區域截圖並打開確認。',
 '爸爸在五項結果都正確後停表，記下秒數、錯誤與提示次數，再把練習文字恢復成相同起點，進行第二輪。',
 '兩輪都可以看小抄，修正時間也要算進去，最後比較相同任务的完成時間，說出最常卡住的一步與改善方法。'],['curriculum']),
('第三輪：孩子設計挑戰',[
 '第三輪換孩子出題，至少組合三種今天學到的動作，寫清楚開始時有哪些工具和文件，以及完成後要看到什麼結果。',
 '例如複製忍者代號，加上測試字再復原，最後截圖留下證據；先自己試做，確認題目能完成，再請爸爸計時挑戰。',
 '爸爸做題時先觀察，不急著代操作，記下容易誤解的地方，再修改題目；不同題目的時間分開記錄，不拿來直接比快。'],['curriculum']),
('兩小時的快捷鍵挑戰',[
 '前十分鐘說明任務，十五分鐘由爸爸示範，再用四十分鐘共同練習並完成前兩輪計時，接著休息十分鐘。',
 '後半段用三十分鐘整理自己的快捷鍵小抄並設計第三輪題目，再用十分鐘交換角色，讓孩子教爸爸完成挑戰。',
 '最後五分鐘錄下今天卡在哪裡、怎麼解決，把小抄、計時紀錄、挑戰題和截圖收好，留下下次可以接著練習的作品。'],['curriculum']),
('最後一關：能做，也能教',[
 '請獨立完成五項操作，再向爸爸說明一個曾經卡住的原因，例如貼錯位置、按鍵衝突，或忘記截圖存在哪裡。',
 '今天的作品是自己的快捷鍵小抄，搭配三輪紀錄、任務截圖與一張孩子出題卡，讓別人也能照著你的說明完成。',
 '下次我們將用封包接力賽認識網路，今天先把工具練順手；我是陳犀牛，保持好奇，我們下次見！'],['curriculum']),
]
# Traditional Chinese consistency, including retained spoken text.
scenes=[(t,[x.replace('任务','任務') for x in lines],refs) for t,lines,refs in scenes]
def write(name,value):
    (P/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def spoken(t):
    for a,b in [('MacBook Air','麥克筆電 Air'),('Mac mini','麥克迷你'),('App','應用程式'),('L003','L 零零三')]:
        t=t.replace(a,b)
    return t
write('narration.json',[{'slide':i,'title':t,'sentences':[{'text':x,'tts':spoken(x)} for x in lines],'sources':[S[k] for k in refs],'sourceType':'curriculum-based-preclass'} for i,(t,lines,refs) in enumerate(scenes,1)])
write('manifest.json',{
 'schemaVersion':1,'episode':'L003','slug':E.name,'title':'鍵盤忍者：快捷鍵競速',
 'subtitle':'父子科技學院 第三堂｜依課表製作的課前教學版','lessonIds':['L003'],
 'editorialStatus':'authored','recordingSource':None,'slideCount':12,'transitionSeconds':0.55,
 'deckRenderer':'artifact-tool-template','templateEpisode':'episodes/academy/l001-mac-workstation',
 'templateProvenance':'Original PPTX absent from v2 ZIP; restored from supplied build_l001.mjs and original assets.',
 'layoutProfile':'academy-native-v1','seriesHeader':'父子科技學院  ·  KEYBOARD NINJA',
 'tts':{'engine':'edge-tts','voice':'zh-TW-YunJheNeural','persona':'陳犀牛 Chen XiNew','rate':'+0%','pitch':'+0Hz'},
 'music':{'backgroundMusic':'none — narration only under teaching slides','opening':'assets/opening/開場影片-v2.mp4'},
 'signoff':{'text':'我是陳犀牛，保持好奇，我們下次見！'},'sources':S,
 'publicationMode':'manual-user-upload',
 'authorization':{'produceL003':True,'publishWhenVerified':False,'channelId':'UCLAQhbdu5MFIDoUPH6bDQuQ','reuploadL001L002':False}
})
write('slides.json',[{'slide':i,'title':t,'eyebrow':'父子科技學院 KEYBOARD NINJA','sourceType':'curriculum'} for i,(t,_,_) in enumerate(scenes,1)])
write('storyboard.json',[{'slide':i,'title':t,'purpose':t,'visual':'L001 原建置程式還原的可編輯版型與原陳犀牛角色','motion':'static + 0.55s fade','narrationSentences':3} for i,(t,_,_) in enumerate(scenes,1)])
write('sources.json',S)
(P/'plan.md').write_text('# L003 鍵盤忍者：快捷鍵競速\n\n依課表製作的課前教學版；沒有課堂錄音，不製造逐字稿。五項技能、三輪計時、孩子出題。沿用原片頭 v2、角色、配色、12 頁原生簡報及指定聲音。\n\n120 分鐘：10／15／40／10／30／10／5。\n')
(P/'narration-script.md').write_text('# L003 旁白稿\n\n依課表製作的課前教學版，非真實授課錄音。\n\n'+'\n\n'.join(f'## {i:02d} {t}\n\n'+'\n\n'.join(lines) for i,(t,lines,_) in enumerate(scenes,1))+'\n')
(P/'fact-check.md').write_text('''# L003 事實核對

2026-09-27，依 Apple 官方文件核對。這是教學圖解，並非 macOS 錄屏。

| 操作 | 核對結果 | 來源 |
|---|---|---|
| 複製／貼上 | Command-C／Command-V；先選文字、再確認目的位置 | https://support.apple.com/zh-tw/102650 |
| 復原／重做 | Command-Z／Shift-Command-Z；依 App 與可復原操作而異 | 同上 |
| 切換 App | 按住 Command，以 Tab 選擇已開啟的 App，放開後切換 | 同上 |
| Spotlight | Command-空白鍵；可能遇到自訂設定或輸入法衝突 | 同上 |
| 截圖 | Shift-Command-3 全螢幕、4 區域、5 截圖工具，Esc 取消選取 | https://support.apple.com/zh-tw/102646 |
| 截圖位置 | 預設桌面，可在截圖工具的選項更改，以當次設定為準 | 同上 |

課程安排、三輪挑戰及作品規格來自 V2 課表 L003。本課原創練習，不宣稱實際父子上課成果。三組 YouTube 入口仍為動態搜尋，未宣稱人工精選影片。
''')
new = [
 ['第三堂任務','鍵盤忍者\n快捷鍵競速','複製貼上、切換工具、留下截圖','第三堂  ·  依課表製作的課前教學版'],
 ['三輪挑戰，先求正確','先熟悉五個動作，再開始計時','01 第一次計時','完成五項任務\n記下時間與錯誤','→','02 相同起點','再做相同任務\n比較自己的進步','→','03 孩子出題','先試做，再教爸爸\n不同題目分開記錄','Command：先按住，再按指定鍵，最後看結果'],
 ['複製貼上，先確認位置','只用練習文字，完成後比較前後兩行','01','選取要複製的文字','我的忍者代號：竹風','02','按 Command + C','先選內容，才知道要複製什麼','03','移到下一行，按 Command + V','確認游標位置，檢查有沒有漏字'],
 ['復原，回到修改前','先加上「測試」兩字，再復原並檢查','四组常用編輯鍵：Cmd 就是 Command','Cmd + C','複製','Cmd + V','貼上','Cmd + Z','復原','Shift-Cmd-Z','重做','可復原哪些動作，依 App 而異；重要作品仍要備份'],
 ['切換 App，讓工具接力','先開啟文字編輯與 Finder','文字編輯','回到練習文件','→','Finder','查看課程資料夾','按住 Command，用 Tab 選擇，放開後切換','來回兩次；切換 App 不一定會切換同一 App 的視窗'],
 ['Spotlight 幫你找工具','Command + 空白鍵：開啟搜尋','01 開啟搜尋','確認搜尋框出現','02 輸入名稱','輸入「文字編輯」','03 確認結果','開啟需要的工具','沒有作用？查看「鍵盤快速鍵」中的 Spotlight 設定'],
 ['截圖，只留下需要的範圍','先關閉私人視窗與通知，再選取練習文字','區域截圖：Shift + Command + 4','拖出範圍','放開後拍攝','Esc','取消這次選取','全螢幕截圖','Shift + Command + 3','暫停影片：只截取練習文字，避開帳號與通知'],
 ['截圖完成，還要找得到','Shift + Command + 5：開啟截圖工具','查看：儲存位置\n找到：剛才的截圖\n打開：檢查內容','截圖工具「選項」','預設桌面，可自行更改','今天只練習拍照\n不需要開始錄影','找不到先查儲存設定；確認文字完整、沒有私人資訊'],
 ['第一、二輪：和自己比','兩輪都可看小抄，修正時間也算入','第一輪：建立紀錄','五項任務都完成才停表\n記錄秒數、錯誤與提示','第二輪：相同起點','還原練習文字，再做一次\n先比正確，再比完成時間','五項：複製貼上、復原、切 App、搜尋、截圖並檢查'],
 ['第三輪：孩子設計挑戰','至少組合三種動作，先自己試做','01','寫出起點與完成條件','例如：複製代號、復原修改、截圖','02','爸爸計時挑戰','記下時間與結果，觀察哪一步卡住','03','把題目改清楚','不同題目分開記錄，不直接比快'],
 ['兩小時的快捷鍵挑戰','爸爸示範，孩子實作，最後交換出題','00–25','開場 10 分＋示範 15 分','25–65','共同練習＋前兩輪','65–75','休息十分鐘','75–105','整理小抄＋設計題目','105–115','孩子教爸爸挑戰','115–120','錄音整理＋存檔','今日生活技能：觀察結果，遇到問題先找原因'],
 ['最後一關：能做，也能教','完成五項操作，再解釋一個卡點與解法','01','自己的快捷鍵小抄','寫下按鍵、用途與常見失誤','02','三輪紀錄與任務截圖','結果正確，也知道作品存在哪裡','03','一張孩子出題卡','爸爸能照著完成，再修正說明','保持好奇，我們下次見！'],
]
new=[[x.replace('四组','四組') for x in page] for page in new]
records=[json.loads(x) for x in (R/'.build-l001/source-inspection.ndjson').read_text().splitlines() if x]
for x in records:
    if 'slideIndex' in x: x.setdefault('slide',x['slideIndex']+1)
    if 'position' in x:
        q=x['position'];x.setdefault('bbox',[q['left'],q['top'],q['width'],q['height']])
edits=[]
for i,values in enumerate(new,1):
    old=[x for x in records if x['kind']=='textbox' and x['slide']==i and 100<x['bbox'][1]<680]
    assert len(old)==len(values),(i,len(old),len(values))
    for x,v in zip(old,values):
        assert x['text'].count('\n')==v.count('\n'),(i,x['text'],v)
        edits.append({'slide':i,'old':x['text'],'new':v})
write('template-text.json',edits)
lp=R/'lessons/L003/lesson.json'
l=json.loads(lp.read_text());l['episodePaths']=[E.relative_to(R).as_posix()];l['status']='preclass-production'
lp.write_text(json.dumps(l,ensure_ascii=False,indent=2)+'\n')
print(f'Authored {len(scenes)} scenes / {sum(len(x[1]) for x in scenes)} sentences; {len(edits)} template mappings')
