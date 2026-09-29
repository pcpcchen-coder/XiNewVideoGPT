import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
const root=path.resolve(import.meta.dirname,'../..');
const ep=path.resolve(process.argv[process.argv.indexOf('--episode')+1]);
const m=JSON.parse(await fs.readFile(path.join(ep,'production/manifest.json'),'utf8'));
const n=JSON.parse(await fs.readFile(path.join(ep,'production/narration.json'),'utf8'));
const edits=JSON.parse(await fs.readFile(path.join(ep,'production/template-text.json'),'utf8'));
const modules=process.env.RUNTIME_NODE_MODULES,skill=process.env.PRESENTATIONS_SKILL;
if(!modules||!skill)throw new Error('Set RUNTIME_NODE_MODULES and PRESENTATIONS_SKILL');
const {PresentationFile,FileBlob}=await import(path.join(modules,'@oai/artifact-tool/dist/artifact_tool.mjs'));
const {finalizePresentation}=await import(path.join(skill,'container_tools/artifact_tool_utils.mjs'));
const template=path.join(root,m.templateEpisode,'production/presentation',path.basename(m.templateEpisode)+'.pptx');
const p=await PresentationFile.importPptx(await FileBlob.load(template));
const snapshot=(await p.inspect({kind:'slide,textbox',maxChars:150000})).ndjson;
const normalize=r=>({...r,slide:r.slide??(r.slideIndex+1),bbox:r.bbox??(r.position?[r.position.left,r.position.top,r.position.width,r.position.height]:undefined)});
const records=snapshot.split('\n').filter(Boolean).map(x=>normalize(JSON.parse(x)));
const build=path.join(root,'.build-'+m.episode.toLowerCase());await fs.mkdir(build,{recursive:true});
await fs.writeFile(path.join(build,'source-inspection.ndjson'),snapshot);
for(const r of records.filter(r=>r.kind==='textbox')){
 let value;
 if(r.text==='父子科技學院  ·  FIRST WORKSTATION')value=m.seriesHeader||'父子科技學院';
 else if(r.text.startsWith('L001 · '))value=r.text.replace('L001',m.episode);
 else if(r.bbox[1]===687&&r.text==='把 MacBook 變成我的工作站')value=m.title;
 else value=edits.find(x=>x.slide===r.slide&&x.old===r.text)?.new;
 if(value!==undefined && value!==r.text){
  const shape=p.resolve(r.id),before=r.text.split('\n'),after=value.split('\n');
  if(before.length>1){
   if(before.length!==after.length)throw new Error('Multiline replacement requires equal paragraph counts');
   before.forEach((line,i)=>shape.text.replace(line,after[i]));
  }else shape.text.replace(r.text,value);
 }
}
// Keep original layout; reduce timeline numerals only to prevent label contact.
for(const r of records.filter(r=>r.kind==='textbox'&&r.slide===11&&/^\d+–\d+$/.test(r.text)))p.resolve(r.id).text.style={...r.style,fontFamily:'Noto Sans CJK TC',fontSize:25};
for(const e of edits)if(!records.some(r=>r.kind==='textbox'&&r.slide===e.slide&&r.text===e.old))throw new Error('Missing template text: '+e.old);
const updated=(await p.inspect({kind:'textbox',maxChars:150000})).ndjson.split('\n').filter(Boolean).map(x=>normalize(JSON.parse(x)));
for(const e of edits)if(!updated.some(r=>r.slide===e.slide&&r.text===e.new))throw new Error('Replacement failed: '+e.new);
for(let i=0;i<p.slides.items.length;i++)p.slides.items[i].speakerNotes.textFrame.setText(n[i].sentences.map(s=>s.text).join('\n')+'\n\n[Sources]\n'+n[i].sources.join('\n'));
const candidate=path.join(build,'candidate.pptx');await(await PresentationFile.exportPptx(p)).save(candidate);
const stamp=Date.now(),final=path.join(build,'final-output',`final-${stamp}.pptx`);await fs.mkdir(path.dirname(final),{recursive:true});
await finalizePresentation({workspaceDir:root,candidatePath:candidate,finalPath:final,pythonExecutable:process.env.XINEW_PYTHON||path.join(root,'.venv/bin/python'),integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],explicitTotalSlideCount:12,fontPolicy:{basis:'reference',families:['Noto Sans CJK TC'],referencePath:template,referenceSha256:crypto.createHash('sha256').update(await fs.readFile(template)).digest('hex')},verifyArtifactToolImport:true,receiptPath:path.join(build,`validation-${stamp}.json`)});
await fs.copyFile(final,path.join(ep,'production/presentation',path.basename(ep)+'.pptx'));
await fs.copyFile(path.join(build,`validation-${stamp}.json`),path.join(ep,'qc/presentation-validation.json'));
const rendered=await PresentationFile.importPptx(await FileBlob.load(final));
for(let i=0;i<rendered.slides.items.length;i++){
 const blob=await rendered.export({slide:rendered.slides.items[i],format:'png',scale:1.5});
 await fs.writeFile(path.join(ep,`assets/slides/slide_${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));console.log(`Rendered ${i+1}/12`);
}
console.log(final);
