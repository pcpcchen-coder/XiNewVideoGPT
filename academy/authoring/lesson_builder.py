"""Shared builder for lesson production sources (L007 onward).

A lesson's authoring/lxxx/prepare_content.py holds only that lesson's text and calls
build(). This module owns the mechanics: template mapping checks, narration/slides/
storyboard/manifest files, the no-reuse check against every earlier authored lesson,
and the lesson's written records (sources, fact check, plan, delivery summary, README).
It never touches audio, timing, subtitles, video or QC.
"""
from pathlib import Path
import json

R = Path(__file__).resolve().parents[1]
SIGNOFF = '我是陳犀牛，保持好奇，我們下次見！'
DISCLOSURE = '依課表製作的課前教學版'
# Only counters, arrows, clock ranges and fixed series labels may equal the L001 template text.
TEMPLATE_TEXT_ALLOWED = {'→', '01', '02', '03', '00–25', '25–65', '65–75', '75–105', '105–115', '115–120',
                         '休息十分鐘', '保持好奇，我們下次見！'}


def _dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def build(*, lesson, slug, ordinal, title, header_en, checked, src, scenes, visible, board,
          render_options, tts_basis, source_records, source_method, not_verified, documents, readme):
    """Write production sources for one lesson. `ordinal` is the Chinese ordinal, e.g. '七'."""
    E = R / 'episodes/academy' / slug
    P = E / 'production'
    assert len(scenes) == len(visible) == len(board) == 12
    seed = json.loads((R / 'pipeline/templates/academy/template-text.json').read_text(encoding='utf-8'))
    edits = []
    for i, values in enumerate(visible, 1):
        old = [x['old'] for x in seed if x['slide'] == i]
        assert len(old) == len(values), (i, len(old), len(values))
        for o, v in zip(old, values):
            assert o.count('\n') == v.count('\n'), (i, o, v)
            assert v.strip() and '待編寫' not in v, (i, v)
            edits.append({'slide': i, 'old': o, 'new': v})
    same = [(e['slide'], e['new']) for e in edits if e['old'] == e['new']]
    assert all(v in TEMPLATE_TEXT_ALLOWED for _, v in same), same
    assert DISCLOSURE in visible[0][-1], 'cover must disclose the pre-class edition'
    _dump(P / 'template-text.json', edits)

    narration = [{'slide': i, 'title': t, 'sentences': [{'text': s, 'tts': s} for s in sentences],
                  'sources': [src[k] for k in keys], 'sourceType': 'curriculum-based-preclass'}
                 for i, (t, sentences, keys) in enumerate(scenes, 1)]
    assert all(len(x['sentences']) == 3 for x in narration)
    first, last = narration[0]['sentences'][0]['text'], narration[-1]['sentences'][-1]['text']
    assert DISCLOSURE in first and '並非實際上課錄音' in first, 'first sentence must disclose'
    assert SIGNOFF in last, 'fixed sign-off missing'
    mine = {x['text'] for s in narration for x in s['sentences']}
    assert len(mine) == 36
    for other in sorted((R / 'episodes/academy').glob('*/production/narration.json')):
        if other.parent.parent.name == slug:
            continue
        seen = {x['text'] for s in json.loads(other.read_text(encoding='utf-8')) for x in s['sentences']}
        assert not (seen - {'待編寫'}) & mine, f'narration reused from {other.parent.parent.name}'
    _dump(P / 'narration.json', narration)
    eyebrow = f'父子科技學院 {header_en}'
    _dump(P / 'slides.json', [{'slide': i, 'title': scenes[i - 1][0], 'eyebrow': eyebrow, 'visibleText': visible[i - 1],
                               'sourceType': 'curriculum-based-preclass'} for i in range(1, 13)])
    _dump(P / 'storyboard.json', [{'slide': i, 'title': scenes[i - 1][0], 'purpose': board[i - 1][0],
                                   'visual': board[i - 1][1] + '（L001 還原版型的原生可編輯文字與圖形）',
                                   'activity': board[i - 1][2], 'motion': 'static + 0.55s fade', 'narrationSentences': 3}
                                  for i in range(1, 13)])

    m = json.loads((P / 'manifest.json').read_text(encoding='utf-8'))
    assert m['episode'] == lesson and m['slug'] == slug
    m.update(title=title, subtitle=f'父子科技學院 第{ordinal}堂｜{DISCLOSURE}', seriesHeader=f'父子科技學院  ·  {header_en}',
             editorialStatus='authored', deckRenderer='ooxml-template', contentMode='curriculum-based-preclass',
             recordingSource=None, autoPublish=False, renderOptions=render_options, sources=dict(src),
             factCheck={'checkedAt': checked, 'record': 'production/fact-check.md', 'sources': 'production/sources.json'},
             authorization={f'produce{lesson}': True,
                            'ttsConsent': {'grantedBy': 'user', 'grantedAt': checked, 'service': 'Microsoft Edge TTS',
                                           'voice': 'zh-TW-YunJheNeural', 'scope': f'{lesson} public narration script only',
                                           'basis': tts_basis, 'excluded': 'private recordings or any other private data'},
                            'paidLlmApi': False, 'uploadToYouTube': False, 'publish': False})
    _dump(P / 'manifest.json', m)

    used = {k for _, _, keys in scenes for k in keys}
    assert used <= set(src), used - set(src)
    ids = {r['id'] for r in source_records}
    assert (set(src) - {'curriculum'}) <= ids, (set(src) - {'curriculum'}) - ids
    _dump(P / 'sources.json', {
        'schemaVersion': 1, 'lessonId': lesson, 'checkedAt': checked, 'method': source_method,
        'curriculum': src['curriculum'], 'sources': source_records, 'notVerified': not_verified,
        'youtubeSearchEntries': {'status': 'not selected, not watched',
                                 'note': '課表的三組 YouTube 連結是動態搜尋入口，本次未挑選或觀看任何影片，也未在影片或教材中引用。'}})
    for name, text in documents.items():
        assert name in ('fact-check.md', 'plan.md', 'delivery-summary.md', 'source-notes.md'), name
        assert '待編寫' not in text
        (P / name).write_text(text, encoding='utf-8')
    for required in ('fact-check.md', 'plan.md', 'delivery-summary.md'):
        assert required in documents, required
    assert documents['delivery-summary.md'].startswith('這是依課表製作的課前教學版，不是實際上課錄音')
    (E / 'README.md').write_text(readme, encoding='utf-8')

    lp = R / 'lessons' / lesson / 'lesson.json'
    record = json.loads(lp.read_text(encoding='utf-8'))
    record['episodePaths'] = [E.relative_to(R).as_posix()]
    record['status'] = 'preclass-production'
    _dump(lp, record)
    print(f'{lesson}: authored 12 scenes / 36 sentences ({sum(len(x) for x in mine)} characters); {len(edits)} template mappings')


def readme(lesson, title):
    return (f'# 父子科技學院 {lesson}\n\n依 V2 課表製作的課前教學版，主題「{title}」。\n'
            '製作來源、旁白、PPTX、教材與 QC 都留在本課次；先讀 `production/START_HERE.md`。\n'
            '交付版本、檔案雜湊、大型檔取得方式與重建命令見 `delivery.json`；檢視方法與限制見 `qc/manual-review.md`。\n'
            '不含課堂私人錄音，也沒有偽造逐字稿。YouTube 由使用者自行上傳。\n')
