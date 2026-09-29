from pathlib import Path
import json, zipfile, subprocess
E=Path('episodes/academy/l002-file-treasure'); B=E/'classroom'; C=B/'L002_尋寶'; M=C/'尋寶地圖'
zones=['01_森林','02_海岸','03_太空']; phrase='看懂路徑找到檔案記得備份'
assert len(phrase)==12
paths=[Path(zones[(i-1)//4])/f'線索{i:02d}.{("txt" if i%4 in (1,2) else "rtf")}' for i in range(1,13)]
def rtf(text):
    out=''
    for c in text:
        if c=='\n':out+='\\par\n'
        elif c in '\\{}':out+='\\'+c
        elif ord(c)>127:out+=f'\\u{ord(c) if ord(c)<32768 else ord(c)-65536}?'
        else:out+=c
    return '{\\rtf1\\ansi\\deff0{\\fonttbl{\\f0 Helvetica;}}\\f0\\fs28\\uc1 '+out+'}'
answers=[]
for i,p in enumerate(paths):
    nxt=str(paths[i+1]) if i<11 else '完成！請按站次讀出十二個密碼字。'
    text=f'第 {i+1:02d} 站\n本站密碼字：{phrase[i]}\n請在紀錄表寫下本檔檔名、副檔名和路徑。\n下一站（從尋寶地圖出發）：{nxt}\n先自己找；卡住時再請爸爸提示。\n'
    f=M/p;f.parent.mkdir(parents=True,exist_ok=True)
    f.write_text(rtf(text) if p.suffix=='.rtf' else text,encoding='utf8')
    if p.suffix=='.rtf':
        restored=subprocess.check_output(['/usr/bin/textutil','-convert','txt','-stdout',str(f)]).decode()
        assert f'本站密碼字：{phrase[i]}' in restored
    answers.append({'station':i+1,'path':str(p),'character':phrase[i],'next':str(paths[i+1]) if i<11 else None})
assert len(list(M.rglob('線索*')))==12
assert all((M/p).is_file() for p in paths)
for folder in ['練習A','練習B']:
    (C/folder).mkdir(exist_ok=True);(C/folder/'先讀我.txt').write_text('只在這兩個練習資料夾比較複製與移動。先複製一個線索到練習A，原線索保留。\n')
(C/'L002_尋寶紀錄_v01.txt').write_text('父子科技學院 L002 尋寶紀錄\n姓名：________ 日期：________\n站次 | 檔名 | 副檔名 | 從尋寶地圖出發的路徑 | 密碼字\n'+''.join(f'{i:02d} | _____ | _____ | _____ | _____\n' for i in range(1,13))+'\n十二字密碼：________________________\n我的命名規則：____________________\n備份位置：________________________\n重新開啟副本確認：________________\n')
(B/'爸爸先讀.txt').write_text('第二堂：檔案與資料夾尋寶\n\n解壓縮後，把 L002_尋寶 複製到孩子的 文件/Tech Academy。保留教材原件。\n三個區域各四個線索，共十二個；從 尋寶地圖/01_森林/線索01.txt 開始。\n請勿把本答案檔放進孩子的尋寶地圖。\n\n00–10 回顧；10–25 示範檔名與路徑；25–65 共同尋寶；65–75 休息；75–105 孩子改造規則；105–115 孩子出題；115–120 錄音、存檔、備份。\n\n複製與移動只用練習副本；不要更動原線索或正式文件。遇到取代提示先取消。\n備份到另一台電腦或外接儲存裝置，打開副本核對十二站紀錄。\n驗收：能說出檔名/類型/路徑；完成十二站；正確比較複製與移動；驗證備份。\n\n教師答案：'+phrase+'\n'+''.join(f'{x["station"]:02d}: {x["path"]} → {x["character"]}\n' for x in answers))
(E/'qc/classroom-validation.json').write_text(json.dumps({'clueCount':12,'rtfRoundtripCount':6,'allPathsExist':True,'password':phrase,'route':answers},ensure_ascii=False,indent=2))
with zipfile.ZipFile(E/'output/classroom.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in B.rglob('*'):
        if p.is_file():z.write(p,p.relative_to(B))
print('12 clues, 6 valid RTF roundtrips, all paths verified')
