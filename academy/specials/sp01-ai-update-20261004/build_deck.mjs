import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
const root=path.resolve(import.meta.dirname,'../..');
const ep=import.meta.dirname;
const workspace=path.resolve(root,'../..');
const build=path.join(workspace,'special-build');
const modules=process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
const skill='/root/.codex/skills/builtins/presentations';
const {PresentationFile,FileBlob}=await import(path.join(modules,'@oai/artifact-tool/dist/artifact_tool.mjs'));
const {finalizePresentation}=await import(path.join(skill,'container_tools/artifact_tool_utils.mjs'));
const src=path.join(root,'episodes/academy/l001-mac-workstation/production/presentation/l001-mac-workstation.pptx');
const p=await PresentationFile.importPptx(await FileBlob.load(src));
const records=(await p.inspect({kind:'slide,textbox,image,layout',maxChars:200000})).ndjson.split('\n').filter(Boolean).map(JSON.parse);
const selected=[0,2,4,8,11];
const edits={
 0:{'開學任務':'團隊分享番外篇','把 MacBook\n變成我的工作站':'AI 近期發展\n工程團隊怎麼用','設定好工具，存好作品，自己找回來':'工作代理、模型成本與多模態協作','第一堂  ·  可暫停跟做':'資料截至 2026/10/04'},
 2:{'先有自己的登入帳號':'工作代理開始持續接手任務','已有自己的帳號，就確認能登入，不必重建':'09/29 OpenAI dots：依方案與市場逐步推出','爸爸開啟系統設定':'持續接手工作','使用者與群組 → 加入使用者':'使用雲端電腦，連接既有工具','孩子使用標準帳號':'跨工具完成任務','自己的桌面、檔案與設定':'協助追蹤問題、分析資料、準備修改','爸爸保留管理者帳號':'權限與驗收仍是必要條件','密碼不出現在教學錄影中':'團隊先定義可做什麼、做到什麼程度'},
 4:{'中英文都打得出來':'模型能力與每件任務的成本','系統設定 → 鍵盤 → 文字輸入「編輯」→ 加入輸入方式':'09/28 Sonnet 5.5、09/29 GPT-6.1 Sol；下列為原廠公告','繁體中文':'GPT-6.1 Sol','我的探險基地':'標準 API：輸入 $2／輸出 $10','英文':'Claude Sonnet 5.5','Hello':'標準 API：輸入 $2／輸出 $10','從選單列切換，或試試 Control + 空白鍵':'相同單價，仍要比較任務完成率與人工修正時間','快速鍵可能因設定不同；能切換並打出文字才算過關':'美元／百萬 tokens；另計快取、重試與工具成本'},
 8:{'多一份，不一定是備份':'語音、畫面與長任務','先保留版本，再讓重要作品多一個安全的去處':'Google：Gemini 3.8 Live（09/15）與 Gemini 4 Argon（09/30）','同一台電腦上的副本':'即時互動：3.8 Live','可保留修改前的內容\n電腦故障時，可能一起不見':'理解即時畫面並呼叫工具\n邊對話、邊執行背景任務','另外的備份位置':'長任務：4 Argon','例如外接儲存裝置\n或爸爸管理的另一部電腦':'強化長流程推理與程式工作\n目前限 Fairwind 受信任組織','爸爸協助備份；完成後打開副本，確認內容正確':'團隊提案：輔助判讀測試畫面，工程師確認結論'},
 11:{'最後一關：你來教爸爸':'團隊試行：一個可驗收任務','暫停影片，完成動作，再說明你自己的整理規則':'兩週試行提案，驗收門檻由團隊確認','打開常用工具':'規格比對：20 組公開樣本','說出 App 和檔案的差別':'輸出差異表，每項附原文頁碼','切換中英文':'同題比較：完成率與總成本','打出「我的探險基地」和 Hello':'納入重試、工具費用與人工修正時間','重新打開基地介紹':'擴大條件：關鍵錯誤 0 件','指出原檔與備份的位置':'引用可追溯 100%，再評估是否擴大'}
};
for(const r of records.filter(r=>r.kind==='textbox'&&selected.includes(r.slideIndex))){
 let to=edits[r.slideIndex]?.[r.text];
 if(r.text==='父子科技學院  ·  FIRST WORKSTATION')to='犀牛說  ·  AI UPDATE SPECIAL';
 if(r.text.startsWith('L001 · '))to=`SP01 · ${String(selected.indexOf(r.slideIndex)+1).padStart(2,'0')}/05`;
 if(r.position.top===687&&r.text==='把 MacBook 變成我的工作站')to='AI 發展番外篇　資料截至 2026/10/04';
 if(r.slideIndex===4&&r.text==='→'){p.delete(r.id);continue;}
 if(to===undefined)continue;
 const sh=p.resolve(r.id);
 const a=r.text.split('\n'), b=to.split('\n');
 if(a.length!==b.length)throw Error('Paragraph contract mismatch: '+r.text);
 a.forEach((v,i)=>sh.text.replace(v,b[i]));
}
for(const [i,m]of Object.entries(edits))for(const old of Object.keys(m))if(!records.some(r=>r.slideIndex===Number(i)&&r.text===old))throw Error('Missing text: '+old);
p.slides.keep(selected);
// Add concise model differences in unused space inside the existing template panels.
// These are editable evidence text, preserving the source panel geometry.
const cost=p.slides.items[2];
for(const [text,left,width]of [['部分評測接近 Astra，單價 1/5',82,440],['比 Sonnet 5 快 30%+（輸出）',679,505]]){
 const sh=cost.shapes.add({geometry:'textbox',position:{left,top:434,width,height:30},fill:'none',line:{fill:'none',width:0}});
 sh.text=text;sh.text.style={typeface:'Noto Sans CJK TC',fontSize:21,color:'#A8B8C9',autoFit:'none'};
}
const narration=JSON.parse(await fs.readFile(path.join(ep,'production/narration.json'),'utf8'));
const notesExtra=[
 '開場提問：如果 AI 能接手一件你每週都要做的工作，你會先交出哪一件？本次涵蓋 2026/09/15–10/04 可核對的官方發布。',
 '解讀：代理能力與帳號授權、外部系統可用性是不同條件。先將輸入、輸出和失敗時處置寫清楚。dots 推出範圍以官方方案與市場說明為準。',
 '標準 API 美元單價／百萬 tokens。GPT-6.1 Sol 快取輸入 $0.10，Sonnet 5.5 快取讀取 $0.20，未納入此頁的标准輸入價。速度 30%+ 指 Sonnet 5.5 相對 Sonnet 5 的輸出生成速度，並非整個專案縮時。Astra 對照為標準輸入 $10、輸出 $50。能力接近及速度均為原廠評測，不能解讀為所有任務等效。',
 'Live 與 Argon 是不同模型與使用情境。Argon 截至查核時先限 Fairwind 計畫，未宣稱一般使用者能立即使用。測試畫面輔助判讀是本簡報提出的團隊試驗，不是已有電池或 BMS 場域驗證。',
 '試行設計：先由工程師建立 20 組公开規格差異的標準答案。任務成功須內容、頁碼、單位、結論全部正確。記錄成功件數／20、含重試總費用、人工修正分鐘。0 件關鍵錯誤、100% 引用可追溯為提議門檻，不是模型已達成的實績。小樣本通過後再擴增資料。'
];
for(let i=0;i<5;i++)p.slides.items[i].speakerNotes.textFrame.setText(narration[i].sentences.map(s=>s.text).join('\n\n')+'\n\n講者補充\n'+notesExtra[i]+'\n\n[Sources] 查核 2026-10-04\n'+narration[i].sources.join('\n'));
await fs.mkdir(build,{recursive:true});
const candidate=path.join(build,'sp01-candidate.pptx');
await(await PresentationFile.exportPptx(p)).save(candidate);
const version=Date.now();
const final=path.join(build,'final',`sp01-${version}.pptx`);await fs.mkdir(path.dirname(final),{recursive:true});
await finalizePresentation({workspaceDir:workspace,candidatePath:candidate,finalPath:final,pythonExecutable:process.env.CODEX_PRIMARY_RUNTIME_PYTHON,integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],explicitTotalSlideCount:5,fontPolicy:{basis:'reference',families:['Noto Sans CJK TC'],referencePath:src,referenceSha256:crypto.createHash('sha256').update(await fs.readFile(src)).digest('hex')},verifyArtifactToolImport:true,receiptPath:path.join(build,`presentation-validation-${version}.json`)});
const deliver=path.join(workspace,'special-output','SP01_AI_Update_2026-10-04.pptx');
await fs.copyFile(final,deliver);
await fs.copyFile(final,path.join(ep,'production/presentation',path.basename(ep)+'.pptx'));
const rendered=await PresentationFile.importPptx(await FileBlob.load(final));
await fs.writeFile(path.join(build,'final.ndjson'),(await rendered.inspect({kind:'slide,textbox,notes,image',maxChars:160000})).ndjson);
for(let i=0;i<5;i++){
 const blob=await rendered.export({slide:rendered.slides.items[i],format:'png',scale:1.5});
 await fs.writeFile(path.join(ep,`assets/slides/slide_${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));
 console.log(`Rendered ${i+1}/5`);
}
console.log(deliver);
