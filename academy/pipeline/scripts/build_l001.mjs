import fs from 'node:fs/promises';
import path from 'node:path';
const modules=process.env.RUNTIME_NODE_MODULES;
if(!modules) throw new Error('Set RUNTIME_NODE_MODULES to the artifact-tool runtime node_modules');
const { Presentation, PresentationFile, FileBlob }=await import(path.join(modules,'@oai/artifact-tool/dist/artifact_tool.mjs'));

const root=path.resolve(import.meta.dirname,'../..');
const ep=path.join(root,'episodes/academy/l001-mac-workstation');
const build=path.join(root,'.build-l001');
await fs.mkdir(build,{recursive:true});
const skill=process.env.PRESENTATIONS_SKILL;
if(!skill) throw new Error('Set PRESENTATIONS_SKILL to the presentations skill directory');
const py=process.env.XINEW_PYTHON || path.join(root,'.venv/bin/python');
const {finalizePresentation}=await import(path.join(skill,'container_tools/artifact_tool_utils.mjs'));
const n=JSON.parse(await fs.readFile(path.join(ep,'production/narration.json'),'utf8'));
const refPath=path.join(root,'episodes/season-01/ep10-ai-and-our-future/production/presentation/ep10-ai-and-our-future.pptx');
// Cloud restoration: original EP10 reference is absent; the builder never used it for layout.
await fs.writeFile(path.join(build,'restoration-note.txt'),'Restored from supplied build_l001.mjs and original assets. Original L001 PPTX and narration absent.');
const p=Presentation.create({slideSize:{width:1280,height:720}});
const C={navy:'#041222',blue:'#1982C4',orange:'#FFC12F',cyan:'#46C8FF',white:'#F7F7F8',gray:'#A8B8C9',panel:'#101B28'};
const font='Noto Sans CJK TC';
function shape(s,x,y,w,h,fill,line='none',round=0){return s.shapes.add({geometry:round?'roundRect':'rect',position:{left:x,top:y,width:w,height:h},fill,line:{fill:line,width:line==='none'?0:1.5},...(round?{borderRadius:round}:{})});}
function text(s,t,x,y,w,h,size=28,color=C.white,bold=false){const a=shape(s,x,y,w,h,'none');a.text=t;a.text.style={fontFamily:font,typeface:font,fontSize:size,bold,color,autoFit:'none',verticalAlignment:'middle',wrap:true};return a;}
function line(s,x,y,w,color=C.blue){return shape(s,x,y,w,1.5,color);}
function title(s,t,sub=''){text(s,t,58,110,1150,72,46,C.white,true);if(sub)text(s,sub,60,185,1130,45,22,C.gray);}
async function rhino(s,pose='pointer',x=955,y=325,w=290){s.images.add({blob:new Uint8Array(await fs.readFile(path.join(root,`assets/characters/cutouts/xinew-${pose}.png`))),contentType:'image/png',alt:`陳犀牛 ${pose}`,fit:'contain',position:{left:x,top:y,width:w,height:w/1.777}});}
function note(s,t){text(s,t,62,548,1150,36,24,C.orange,true);}
function row(s,num,label,desc,y,width=820){text(s,num,64,y,65,57,38,C.orange,true);text(s,label,149,y,width-100,50,30,C.white,true);if(desc)text(s,desc,149,y+51,width-100,43,22,C.gray);}
function box(s,x,y,w,h,label,detail,color=C.cyan){shape(s,x,y,w,h,C.panel,color,14);text(s,label,x+20,y+17,w-40,48,30,color,true);if(detail)text(s,detail,x+20,y+74,w-40,h-85,24,C.white);}
function arrow(s,x,y){text(s,'→',x,y,48,45,34,C.cyan,true);}

for(let i=1;i<=12;i++){
 const s=p.slides.add();s.background.fill='linear(135deg, #041222 0%, #071F37 62%, #041222 100%)';
 shape(s,0,0,1280,8,C.orange);text(s,'CHEN',56,29,100,40,24,C.white,true);text(s,'XiNew',151,29,108,40,24,C.orange,true);
 text(s,'父子科技學院  ·  FIRST WORKSTATION',288,37,640,32,16,C.gray);
 text(s,`L001 · ${String(i).padStart(2,'0')}/12`,1054,35,175,33,17,C.orange,true);line(s,56,86,1168);
 text(s,'把 MacBook 變成我的工作站',58,687,620,23,12,C.gray);text(s,'XINEW SAYS',1088,687,151,23,12,C.orange,true);
 s.speakerNotes.textFrame.setText(`${n[i-1].title}\n${n[i-1].sentences.map(x=>x.text).join('\n')}\n\n[Sources]\n${n[i-1].sources.join('\n')}\n\n教學示意；不是系統截圖。依課程表原創，非實際課堂逐字稿。`);
 if(i===1){
  text(s,'開學任務',62,128,640,55,28,C.orange,true);
  text(s,'把 MacBook\n變成我的工作站',59,200,900,160,61,C.white,true);
  text(s,'設定好工具，存好作品，自己找回來',64,399,790,55,29,C.white);
  text(s,'第一堂  ·  可暫停跟做',64,493,700,44,25,C.cyan,true);
  await rhino(s,'point-up',830,344,412);
 }else if(i===2){
  title(s,'三個任務，解鎖工作站','每完成一項，就向爸爸說明你做了什麼');
  box(s,62,292,310,207,'01 個人帳號','有自己的設定\n知道誰能管理');arrow(s,385,368);
  box(s,438,292,310,207,'02 常用工具','找得到 App\n能切換中英文');arrow(s,761,368);
  box(s,814,292,390,207,'03 作品的家','建立課程資料夾\n儲存後重新打開',C.orange);
  note(s,'先取一個探險代號，例如「海洋探險家」');
 }else if(i===3){
  title(s,'先有自己的登入帳號','已有自己的帳號，就確認能登入，不必重建');
  row(s,'01','爸爸開啟系統設定','使用者與群組 → 加入使用者',262);
  row(s,'02','孩子使用標準帳號','自己的桌面、檔案與設定',370);
  row(s,'03','爸爸保留管理者帳號','密碼不出現在教學錄影中',478);
  await rhino(s,'open-palms',952,318,275);
 }else if(i===4){
  title(s,'桌面是工作桌，Dock 是工具入口','開啟 App → Control 點按圖示 → 選項 → 保留在 Dock');
  shape(s,63,263,1140,254,C.panel,C.blue,16);
  text(s,'Dock 教學示意',84,280,470,35,20,C.gray);
  const labels=[['Finder','整理檔案'],['Safari','瀏覽網頁'],['文字編輯','寫下想法'],['系統設定','調整電腦']];
  labels.forEach((v,k)=>{const x=94+k*280;shape(s,x,345,245,118,'#092944',k===0?C.orange:C.blue,13);text(s,v[0],x+18,359,220,44,30,k===0?C.orange:C.white,true);text(s,v[1],x+18,410,220,40,23,C.gray);});
  note(s,'試試拖曳排列順序；移除 Dock 圖示不等於刪除 App');
 }else if(i===5){
  title(s,'中英文都打得出來','系統設定 → 鍵盤 → 文字輸入「編輯」→ 加入輸入方式');
  box(s,62,283,480,190,'繁體中文','我的探險基地',C.cyan);
  arrow(s,577,346);box(s,659,283,545,190,'英文','Hello',C.orange);
  text(s,'從選單列切換，或試試 Control + 空白鍵',66,510,1090,45,28,C.white,true);
  note(s,'快速鍵可能因設定不同；能切換並打出文字才算過關');
 }else if(i===6){
  title(s,'工具、作品、位置','先說出它的用途，再記住它的圖示');
  box(s,62,291,330,224,'App 是工具','例如：文字編輯');
  box(s,421,291,355,224,'檔案是作品','例如：基地介紹');
  box(s,805,291,399,224,'資料夾是位置','例如：02_作品',C.orange);
  note(s,'你來指一指：哪個工具，做出了哪個作品？');
 }else if(i===7){
  title(s,'替作品安排固定的家','先到 Finder 的「文件」，再用「檔案 → 新增檔案夾」建立');
  text(s,'文件 / Tech Academy / L001_工作站',65,254,1130,55,31,C.orange,true);
  const v=[['01_素材','參考資料'],['02_作品','完成的內容'],['03_紀錄','心得與卡關']];
  v.forEach((x,k)=>box(s,64+k*385,350,355,159,x[0],x[1],k===1?C.orange:C.cyan));
  note(s,'暫停影片：建立後，再自己走一次完整路徑');
 }else if(i===8){
  title(s,'存檔後，要找得回來','打開文字編輯，先寫三句基地介紹');
  text(s,'我的基地叫＿＿＿\n我想學會＿＿＿\n下次想做＿＿＿',73,275,610,192,32,C.white);
  text(s,'檔案 → 儲存',751,270,400,53,30,C.orange,true);
  text(s,'L001_基地介紹_v01.rtf',751,344,438,46,26,C.white,true);
  text(s,'存進 L001_工作站 / 02_作品\n副檔名依 App 的格式保留',751,414,449,90,22,C.gray);
  note(s,'暫停影片：關閉文件，再用 Finder 把它找回來');
 }else if(i===9){
  title(s,'多一份，不一定是備份','先保留版本，再讓重要作品多一個安全的去處');
  box(s,63,274,536,253,'同一台電腦上的副本','可保留修改前的內容\n電腦故障時，可能一起不見',C.cyan);
  box(s,634,274,570,253,'另外的備份位置','例如外接儲存裝置\n或爸爸管理的另一部電腦',C.orange);
  note(s,'爸爸協助備份；完成後打開副本，確認內容正確');
 }else if(i===10){
  title(s,'你的工作站，你的規則','保留好找、好讀的空間，也放進自己的興趣');
  row(s,'01','選一張基地桌布','系統設定 → 背景圖片',259,855);
  row(s,'02','說明你的命名規則','為什麼素材、作品、紀錄要分開？',371,855);
  row(s,'03','和爸爸一起試試 AI','請提供三個海洋探險基地的名稱',483,855);
  await rhino(s,'thumbs-up',961,327,260);
 }else if(i===11){
  title(s,'兩小時的父子挑戰','影片先引路，接下來用作品證明你學會了');
  const bands=[['00–25','任務開場＋示範'],['25–65','父子共同實作'],['65–75','休息十分鐘'],['75–105','孩子獨立改造'],['105–115','孩子教爸爸'],['115–120','錄音總結＋存檔']];
  bands.forEach((b,k)=>{let x=k<3?65:669,y=259+(k%3)*101;line(s,x,y+79,540);text(s,b[0],x,y,180,53,29,k===2?C.gray:C.orange,true);text(s,b[1],x+220,y,330,53,26,C.white);});
  note(s,'今日生活技能：管理自己的工具與成果');
 }else{
  title(s,'最後一關：你來教爸爸','暫停影片，完成動作，再說明你自己的整理規則');
  row(s,'01','打開常用工具','說出 App 和檔案的差別',256,890);
  row(s,'02','切換中英文','打出「我的探險基地」和 Hello',361,890);
  row(s,'03','重新打開基地介紹','指出原檔與備份的位置',466,890);
  await rhino(s,'open-palms',946,301,290);
  text(s,'保持好奇，我們下次見！',650,548,565,39,29,C.orange,true);
 }
}
const buildId=String(Date.now());
const candidate=path.join(build,'candidate.pptx');
await (await PresentationFile.exportPptx(p)).save(candidate);
const final=path.join(build,`final-output/final-${buildId}.pptx`);
await fs.mkdir(path.dirname(final),{recursive:true});
await finalizePresentation({workspaceDir:root,candidatePath:candidate,finalPath:final,pythonExecutable:py,
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],
 explicitTotalSlideCount:12,fontPolicy:{basis:'design',families:[font]},verifyArtifactToolImport:true,
 receiptPath:path.join(build,`validation-${buildId}.json`)});
await fs.copyFile(final,path.join(ep,'production/presentation/l001-mac-workstation.pptx'));
// Render the final PPTX, not a separate visual approximation.
const finalDeck=await PresentationFile.importPptx(await FileBlob.load(final));
await fs.writeFile(path.join(build,'source-inspection.ndjson'),(await finalDeck.inspect({kind:'slide,textbox',maxChars:150000})).ndjson);
for(let i=0;i<finalDeck.slides.items.length;i++){
 const blob=await finalDeck.export({slide:finalDeck.slides.items[i],format:'png',scale:1.5});
 await fs.writeFile(path.join(ep,`assets/slides/slide_${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));
 console.log(`rendered ${i+1}/12`);
}
console.log(final);
