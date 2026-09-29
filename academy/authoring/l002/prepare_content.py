from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]; E=R/'episodes/academy/l002-file-treasure'; P=E/'production'
S={'curriculum':'父子科技學院_V2_192堂_YouTube教材庫.xlsx／逐堂課程／總課次2', 'extensions':'https://support.apple.com/zh-tw/guide/mac-help/mchlp2304/mac','path':'https://support.apple.com/zh-tw/guide/mac-help/mchlp1774/mac','search':'https://support.apple.com/zh-tw/guide/mac-help/-mh15155/mac','keys':'https://support.apple.com/zh-tw/102650','rename':'https://support.apple.com/zh-tw/guide/mac-help/mchlp1144/mac'}
scenes=[
('檔案與資料夾尋寶',[
'歡迎回到父子科技學院，我是陳犀牛，上一堂我們建立工作站，今天要進入資料夾迷宮，找回十二個線索。',
'爸爸用 Mac mini 示範，你用 MacBook Air 操作；這次比的不只是速度，還要說得出檔案在哪裡、為什麼選它。',
'最後你會留下能重複使用的資料夾結構，學會看檔名、找路徑，並分清楚複製、移動和備份。'],['curriculum']),
('十二個線索，三項本領',[
'爸爸先把十二個線索檔放進森林、海岸和太空三個資料夾，每個線索都藏著下一站的位置。',
'先靠路徑找到檔案，再依檔名與副檔名辨認它，最後把找到的結果整理成自己的尋寶紀錄。',
'先求正確，再挑戰自己的完成時間；只在本課練習資料夾內操作，不搬動爸爸的正式文件。'],['curriculum']),
('讀懂一個檔名',[
'看畫面上的「L002 底線尋寶紀錄底線 v01 點 txt」，前面是課次，中間是內容，版本號幫你分辨修改先後。',
'最後的點和字母叫副檔名，可以提示檔案類型；例如 txt 是純文字，rtf 可以保留文字格式。',
'改名時保留正確副檔名；把文字檔改叫 png，並不會把裡面的文字變成圖片。'],['extensions','rename']),
('副檔名是類型線索',[
'文字、圖片和影片，都可能是檔案；今天先認識純文字、格式文字、文件和圖片四種常見類型。',
'如果看不到副檔名，在 Finder 的設定裡選進階，再勾選顯示所有檔案副檔名。',
'本課線索使用 txt 和 rtf 兩種文字格式；遇到陌生檔案，先確認來源，再和爸爸決定怎麼打開。'],['extensions','curriculum']),
('路徑是檔案的地址',[
'同樣叫線索零一的檔案，可以住在不同資料夾，所以檔名相同，不代表它就是同一個檔案。',
'從本課的尋寶地圖進入零一森林，再找到線索零一點 txt，這一串由外到內的位置就是路徑。',
'在 Finder 選顯示方式，再選顯示路徑列，選取檔案後看看底部，確認你現在站在哪一層。'],['path','curriculum']),
('複製、移動、備份',[
'複製是多出一份，移動是更換位置，而備份是為了讓原本的資料出問題時，仍有機會找回內容。',
'在同一台電腦多放一份練習檔，方便你重新挑戰，卻不能防止整台電腦故障造成的資料遺失。',
'先把這三個動作說給爸爸聽，再預測操作後，來源和目的地各會留下什麼東西。'],['curriculum']),
('尋寶地圖，開始闖關',[
'在文件裡的 Tech Academy 建立 L002 尋寶，放入本課教材包的尋寶地圖，先保留一份原始練習包。',
'地圖分成零一森林、零二海岸、零三太空，每區四個線索；從森林的線索零一開始，照內容前往下一站。',
'每找到一站，就記下檔名、類型、所在路徑與密碼字；暫停影片，和爸爸一起完成十二站。'],['curriculum']),
('找不到，就縮小搜尋',[
'如果忘了某個線索藏在哪裡，先打開尋寶地圖，再用 Finder 的搜尋欄輸入檔名中記得的部分。',
'確認搜尋範圍是本課資料夾或這台 Mac；結果太多時，可以按加號，加入名稱或種類的條件。',
'找到結果後還要查看所在路徑；查不到也不等於檔案消失，先檢查拼字、搜尋範圍和實際資料夾。'],['search','path']),
('親手比較複製與移動',[
'選一個練習檔，按 Command 加 C，到另一個練習資料夾按 Command 加 V，這是複製，請檢查兩邊是否都有檔案。',
'要練習移動，先選剛才的副本並按 Command 加 C，再到目的資料夾按 Option、Command 加 V。',
'操作後確認原位置少了副本，目的地多了副本；若出現同名取代提示，先取消，重新命名後再試。'],['keys','curriculum']),
('備份，也要驗證',[
'把今天的尋寶紀錄存成第一版，再請爸爸協助複製到另外的備份位置，例如外接儲存裝置或另一台電腦。',
'打開備份副本，確認十二站的紀錄真的存在；只有看到檔名，還不能保證內容完整。',
'最後自己增加一個規則，例如每次修改就更新版本號，並說明這條規則如何幫未來的你節省找檔時間。'],['curriculum']),
('兩小時的尋寶挑戰',[
'前十分鐘說明任務，十五分鐘示範檔名與路徑，再用四十分鐘和爸爸一起完成十二個線索，接著休息十分鐘。',
'後半段用三十分鐘自己改造資料夾規則，再用十分鐘交換角色，由你出題，爸爸照你的路徑去尋寶。',
'最後五分鐘錄下今天怎麼找檔案、哪裡容易錯，以及下次想加什麼，並把作品命名、存檔與備份。'],['curriculum']),
('最後一關：換你出題',[
'現在請爸爸挑一個檔案，你說出名稱、類型和路徑，再示範複製與移動，讓爸爸檢查兩個位置的變化。',
'接著指出一個常見錯誤，例如亂改副檔名，或把同一台電腦上的副本當成完整備份，說明怎麼避免。',
'能自己找到作品，也能讓別人照規則找到，你的尋寶任務就通關；我是陳犀牛，保持好奇，我們下次見！'],['curriculum','extensions'])]
def write(n,v):(P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def spoken(t):
 for a,b in [('MacBook Air','麥克筆電 Air'),('Mac mini','麥克迷你'),('Mac','麥克'),('L002','L 零零二'),('txt','T X T'),('rtf','R T F'),('png','P N G'),('v01','V 零一')]:t=t.replace(a,b)
 return t
write('narration.json',[{'slide':i,'title':t,'sentences':[{'text':x,'tts':spoken(x)} for x in lines],'sources':[S[r] for r in refs],'sourceType':'curriculum-based-original-script'} for i,(t,lines,refs) in enumerate(scenes,1)])
m=json.loads((R/'episodes/academy/l001-mac-workstation/production/manifest.json').read_text());m.update(episode='L002',slug=E.name,title='檔案與資料夾尋寶',subtitle='父子科技學院 第二堂｜檔名、路徑、搜尋與備份',lessonIds=['L002'],sources={'curriculum':S['curriculum'],'official':[u for u in S.values() if u.startswith('https')]},templateEpisode='episodes/academy/l001-mac-workstation',deckRenderer='artifact-tool-template',layoutProfile='academy-native-v1');write('manifest.json',m)
write('slides.json',[{'slide':i,'title':t,'eyebrow':'父子科技學院 FILE TREASURE','sourceType':'curriculum'} for i,(t,_,_) in enumerate(scenes,1)])
write('storyboard.json',[{'slide':i,'title':t,'purpose':t,'visual':'沿用 L001 可編輯教學版型與陳犀牛角色','motion':'static + 0.55s fade'} for i,(t,_,_) in enumerate(scenes,1)])
write('sources.json',S)
(P/'plan.md').write_text('# L002 檔案與資料夾尋寶\n\n依 192 堂課表第二堂原創課前教學版；非實際課堂錄音逐字稿。涵蓋檔名、副檔名、路徑、搜尋、複製、移動與備份，搭配 12 線索實作。沿用 L001 原生簡報、片頭、角色與聲音。\n')
(P/'narration-script.md').write_text('# 第二堂旁白稿\n\n'+'\n\n'.join('## '+a+'\n\n'+'\n\n'.join(b) for a,b,_ in scenes))
(P/'fact-check.md').write_text('# 內容來源\n\n'+'\n'.join('- '+u for u in S.values())+'\n\n各幕來源亦保存在旁白 JSON 與簡報講者備註。\n')
print('Authored',sum(len(t) for _,lines,_ in scenes for t in lines),'characters')
