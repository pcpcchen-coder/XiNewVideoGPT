#!/usr/bin/env python3
"""Build the small text bundle that accompanies a delivered lesson (for a Drive folder or similar).

Large media cannot go through inline-content connectors, so the bundle holds what can:
a read-me, an HTML delivery report, the YouTube description, SRT, narration script,
package checksums and the split-part restore note. Numbers come from delivery.json;
the lesson-specific judgement (what to listen to, design choices, limits) comes from
qc/handover-notes.json written by whoever reviewed the lesson. Nothing is uploaded here.

    ./portable-runtime.sh python pipeline/handover_bundle.py --episode episodes/academy/<slug> --commit <short hash>
"""
from pathlib import Path
import argparse
import html
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
CSS = ('body{font-family:-apple-system,"PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif;max-width:920px;margin:24px auto;'
       'padding:0 16px;color:#10243a;line-height:1.6}h1{font-size:22px;margin-bottom:4px}h2{font-size:17px;border-bottom:2px solid #35a9d6;'
       'padding-bottom:4px;margin-top:28px}table{border-collapse:collapse;width:100%;font-size:14px}th,td{border:1px solid #c5d3df;'
       'padding:6px 8px;text-align:left;vertical-align:top}th{background:#e8f4fb}code{font-family:Menlo,Consolas,monospace;font-size:12.5px;'
       'background:#eef3f7;padding:1px 4px;border-radius:3px;word-break:break-all}.ok{color:#0a7a3d;font-weight:700}'
       '.warn{color:#a35a00;font-weight:700}.sub{color:#51677c;font-size:13px}')


def rows(pairs, width=26):
    e = html.escape
    return ''.join(f'<tr><th style="width:{width}%">{e(a)}</th><td>{e(b)}</td></tr>' for a, b in pairs)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--episode', required=True, type=Path)
    p.add_argument('--commit', required=True)
    a = p.parse_args()
    ep = (ROOT / a.episode).resolve()
    d = json.loads((ep / 'delivery.json').read_text(encoding='utf-8'))
    notes = json.loads((ep / 'qc/handover-notes.json').read_text(encoding='utf-8'))
    manifest = json.loads((ep / 'production/manifest.json').read_text(encoding='utf-8'))
    lesson, version, title, date = d['lessonId'], d['version'], manifest['title'], d['createdAt']
    pkg_dir = ROOT / 'delivery' / version
    out = ROOT / 'delivery' / f'drive-{lesson}'
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    names = {
        'description': f'{lesson}_YouTube說明與章節_youtube-description.txt', 'srt': f'{lesson}_全片字幕_zh-TW.srt',
        'script': f'{lesson}_講稿_12幕36句_narration-script.md', 'sums': f'{version}_交付包內檔案SHA-256_checksums.json',
        'restore': f'{version}_分段檔還原說明_RESTORE.txt', 'report': f'{lesson}_製作交付報告_{date}.html',
        'readme': '00_請先讀_這個資料夾有什麼_缺什麼.txt'}
    shutil.copyfile(pkg_dir / 'youtube-description.txt', out / names['description'])
    shutil.copyfile(pkg_dir / 'zh-TW.srt', out / names['srt'])
    shutil.copyfile(pkg_dir / 'narration-script.md', out / names['script'])
    shutil.copyfile(pkg_dir / 'checksums.json', out / names['sums'])
    shutil.copyfile(ROOT / 'delivery/parts' / f'{version}_還原說明_RESTORE.txt', out / names['restore'])
    pkg, v, parts = d['package'], d['validation'], d['persistence']['parts']
    large = {x['role'].split(' ')[0]: x for x in d['largeFiles']}
    zh = d['largeFiles'][0]
    (out / names['readme']).write_text(f'''父子科技學院 {version}「{title}」（{date}）

這個資料夾放的是文字類交付檔與報告。影片、母帶、MP3、PPTX、教材 ZIP 不在這裡。

為什麼缺大型檔
Claude 的 Google Drive 連接器只能把內容直接寫進請求裡，實際上只放得進幾 KB 的文字；
影片無法由 Claude 上傳。這是工具限制，不是授權問題。

大型檔在哪裡
製作當次的 Claude 對話附件：{len(parts)} 個分段檔加一份還原說明。
全部下載到同一個資料夾，照「{names['restore']}」合併即可。
合併後的 ZIP：{pkg['bytes']:,} bytes
SHA-256：{pkg['sha256']}

想讓這個資料夾完整
把分段檔（或合併、解壓後的 {version} 資料夾）直接拖進來即可。

這裡有的檔案
- {names['report']}：結果、雜湊、檢查方法、限制
- {names['description']}：可直接貼到 YouTube
- {names['srt']}：36 條，時間已含片頭
- {names['script']}
- {names['sums']}
- {names['restore']}

狀態
verify {v['passed']}/{v['total']}；verified／awaiting_user_upload。沒有登入 YouTube、沒有上傳、沒有公開。
沒有真人聽審；上傳前請親耳抽聽，重點見報告。
Git：https://github.com/pcpcchen-coder/XiNewVideoGPT（main，commit {a.commit}）
''', encoding='utf-8')
    e = html.escape
    files = ''.join(f"<tr><td>{e(x['filename'])}（{e(label)}）</td><td>{x['bytes']:,}</td><td><code>{x['sha256']}</code></td></tr>"
                    for x, label in ((d['largeFiles'][0], '上傳用，字幕已燒入'), (d['largeFiles'][1], '無字幕母帶'),
                                     (d['largeFiles'][2], '純旁白'), (d['inGit'][0], '可編輯 PPTX'), (d['inGit'][3], '教材')))
    listen = ''.join(f'<tr><td>{e(t)}</td><td>{e(x)}</td></tr>' for t, x in notes['listen'])
    limits = ''.join(f'<li>{e(x)}</li>' for x in notes['limits'])
    narration = round(d['durationSeconds'] - d['openingSeconds'], 2)
    (out / names['report']).write_text(f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{lesson} 製作交付報告 {date}</title><style>{CSS}</style></head><body>
<h1>父子科技學院 {lesson}「{e(title)}」</h1>
<p class="sub">製作交付報告｜{date}｜依課表製作的課前教學版（無課堂錄音）｜Git main <code>{e(a.commit)}</code></p>
<h2>1. 結論</h2><table>
<tr><th style="width:26%">狀態</th><td><span class="ok">verified</span>／awaiting_user_upload；未登入、未上傳、未公開</td></tr>
<tr><th>技術驗收</th><td><span class="ok">{v['passed']}/{v['total']}</span>；{d['durationSeconds']} 秒（片頭 {d['openingSeconds']}＋教學段落 {narration}）；1080p30 H.264／AAC 48 kHz；{v['integratedLufs']} LUFS</td></tr>
<tr><th>內容</th><td>12 頁／36 句；原片頭 v2、陳犀牛、深藍黃青；{e(d['voice'])}；靜態加淡化；無背景音樂</td></tr>
<tr><th>交付包</th><td><code>{e(pkg['filename'])}</code><br>{pkg['bytes']:,} bytes｜SHA-256 <code>{pkg['sha256']}</code><br>以 {len(parts)} 個分段檔交付在對話附件，還原已測試</td></tr>
<tr><th>需要你做</th><td><span class="warn">親耳抽聽後自行上傳</span>（見第 4 節）</td></tr></table>
<h2>2. 主要檔案</h2><table><tr><th>檔案</th><th>Bytes</th><th>SHA-256</th></tr>{files}</table>
<p class="sub">包內另有 SRT、講稿、封面、章節說明、來源、事實查核、QC 報告、接續說明；完整雜湊見 checksums.json。</p>
<h2>3. 這一課的設計取捨</h2><table>{rows(notes['design'])}</table>
<h2>4. 上傳前請你親耳確認</h2>
<p>沒有真人聽審。機器辨識把下列詞聽成同音或近音字，代表音節大致正確，但聲調與咬字機器判斷不了：</p>
<table><tr><th style="width:22%">時間</th><th>請聽</th></tr>{listen}</table>
<h2>5. 怎麼檢查的</h2><table>
{rows([('逐頁', '12 張 1920×1080 投影片逐張看；PPTX 重新載入確認 12 頁原生文字、備註含 36 句'),
        ('逐段', '從最終字幕版 MP4 在 36 條字幕的時間中點各取一格，全部看過：文字正確、落在對應頁、兩行以內、不遮內容、無行首標點'),
        ('聲音（機器）', f"逐條語音辨識 36 條：字面相似度最低 {v['asrMinSimilarity']}、平均 {v['asrMeanSimilarity']}" + (f"，以拼音比對最低 {v['asrMinSoundSimilarity']}" if 'asrMinSoundSimilarity' in v else '') + f"；逐幕波形與本課旁白檔偏移 {v['sceneAudioMaxLagMs']} ms、相關係數最低 {v['sceneAudioMinCorrelation']}；每幕都有數位靜音視窗（無背景音樂）"),
        ('事實', notes['checks']['facts']), ('教材', notes['checks']['classroom'])])}</table>
<h2>6. 製作中發現並修正</h2><table>{rows(notes['fixes'])}</table>
<h2>7. 限制</h2><ul>{limits}</ul>
</body></html>
''', encoding='utf-8')
    listing = [{'name': f.name, 'bytes': f.stat().st_size} for f in sorted(out.iterdir())]
    print(json.dumps({'folder': out.relative_to(ROOT).as_posix(), 'files': listing}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
