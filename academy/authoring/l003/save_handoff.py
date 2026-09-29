"""Build a portable, verified L003 handoff; never include credentials/private audio."""
from pathlib import Path
import argparse,hashlib,json,shutil,zipfile,datetime

R=Path(__file__).resolve().parents[2]
E=R/'episodes/academy/l003-keyboard-ninja'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,required=True)
O=parser.parse_args().output.resolve()
if O.is_relative_to(R):
    raise ValueError('Use an output directory outside academy to avoid packaging the archive itself')
O.mkdir(parents=True,exist_ok=False)
report=json.loads((E/'qc/report.json').read_text())
assert report['passed']==report['total']==23
assert json.loads((E/'qc/subtitle-layout.json').read_text())['passed']
assert json.loads((E/'qc/editable-deck-check.json').read_text())['passed']
assert json.loads((E/'qc/audio-provenance.json').read_text())['passed']
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for part in iter(lambda:f.read(1024*1024),b''):h.update(part)
    return h.hexdigest()
fingerprint=json.loads((E/'qc/verified-inputs.json').read_text())
assert all((E/p).is_file() and sha(E/p)==h for p,h in fingerprint.items())
sources=[E/'output/l003-keyboard-ninja-zh-TW.mp4',E/'production/presentation/l003-keyboard-ninja.pptx',E/'subtitles/zh-TW.srt',E/'output/classroom.zip']
for p in sources:shutil.copy2(p,O/p.name)
skip={'.cloud-deps','.venv','.git','__pycache__','private','delivery'}
files=[]
for p in sorted(R.rglob('*')):
    rel=p.relative_to(R)
    if not p.is_file() or p.is_symlink() or any(x in skip or x.startswith('.build-') for x in rel.parts):continue
    if rel.as_posix()=='SHA256SUMS.json' or p.suffix in ('.pyc','.tmp'):continue
    if p.name.startswith(('.env','client_secret')) or p.name=='token.json':continue
    files.append(p)
manifest={p.relative_to(R).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in files}
manifest_path=O/'SHA256SUMS.json'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
archive=O/f'Academy_Cloud_Handoff_{datetime.datetime.now(datetime.timezone.utc).date()}_L003.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:
        z.write(p,Path('XiNewVideoGPT-academy')/p.relative_to(R))
    z.write(manifest_path,'XiNewVideoGPT-academy/SHA256SUMS.json')
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for rel,expected in manifest.items():
        data=z.read('XiNewVideoGPT-academy/'+rel)
        assert len(data)==expected['bytes'] and hashlib.sha256(data).hexdigest()==expected['sha256'],rel
out={'createdAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archiveFileCount':len(files)+1,'manifestEntries':len(manifest),'archiveManifestVerification':'PASS','files':{p.name:{'bytes':p.stat().st_size,'sha256':sha(p)} for p in [*(O/p.name for p in sources),archive]}}
(O/'checksums.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
