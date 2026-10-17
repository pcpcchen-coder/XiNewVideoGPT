"""Shared builder for special episodes (SP…) that use the 12-scene lesson template.

Specials are not curriculum lessons: they have no lessons/Lxxx/lesson.json, no 120-minute class
and no "依課表製作的課前教學版" disclosure. They live under specials/<slug>/ and otherwise go
through the same portable pipeline (deck, TTS, assembly, verify, package) as lessons.

A special's authoring/spxxx/prepare_content.py holds only its own text and calls build().
This module creates the episode skeleton on first run, then writes the production sources:
template mapping, narration/slides/storyboard/manifest, sources and written records. It checks
the template mapping, the fixed sign-off, the special's own disclosure and that no narration
sentence is reused from any lesson or special. It never touches audio, video or QC.
"""
from pathlib import Path
import json

import lesson_builder as lb

R = lb.R


def _dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def ensure_skeleton(special, slug):
    """Create specials/<slug>/ like pipeline/academy.py new-episode does for lessons (no lesson record)."""
    E = R / 'specials' / slug
    if (E / 'production/manifest.json').is_file():
        return E
    for folder in ('production/presentation', 'assets/slides', 'assets/visuals', 'audio', 'subtitles', 'output', 'qc',
                   'classroom', 'publication'):
        (E / folder).mkdir(parents=True, exist_ok=True)
    m = json.loads((R / 'pipeline/templates/academy/manifest.json').read_text(encoding='utf-8'))
    m.update(episode=special, slug=slug, lessonIds=[], editorialStatus='draft')
    _dump(E / 'production/manifest.json', m)
    _dump(E / 'publication/status.json', {'lessonId': special, 'status': 'not_uploaded',
                                          'publicationMode': 'manual-user-upload', 'publisher': 'user', 'videoUrl': None})
    return E


def build(*, special, slug, title, header_en, cover_disclosure, first_sentence_needles, summary_prefix, checked, src,
          scenes, visible, board, render_options, tts_basis, source_records, source_method, not_verified,
          documents, readme, content_mode, delivery_label, classroom_note):
    E = ensure_skeleton(special, slug)
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
    assert all(v in lb.TEMPLATE_TEXT_ALLOWED for _, v in same), same
    assert cover_disclosure in visible[0][-1], 'cover must carry the special disclosure'
    _dump(P / 'template-text.json', edits)

    narration = [{'slide': i, 'title': t, 'sentences': [{'text': s, 'tts': s} for s in sentences],
                  'sources': [src[k] for k in keys], 'sourceType': content_mode}
                 for i, (t, sentences, keys) in enumerate(scenes, 1)]
    assert all(len(x['sentences']) == 3 for x in narration)
    first, last = narration[0]['sentences'][0]['text'], narration[-1]['sentences'][-1]['text']
    assert all(n in first for n in first_sentence_needles), 'first sentence must disclose'
    assert lb.SIGNOFF in last, 'fixed sign-off missing'
    mine = {x['text'] for s in narration for x in s['sentences']}
    assert len(mine) == 36
    others = list((R / 'episodes/academy').glob('*/production/narration.json')) + list((R / 'specials').glob('*/production/narration.json'))
    for other in sorted(others):
        if other.parent.parent == E:
            continue
        data = json.loads(other.read_text(encoding='utf-8'))
        seen = {x['text'] for s in data for x in s.get('sentences', []) if isinstance(x, dict) and 'text' in x}
        assert not (seen - {'待編寫'}) & mine, f'narration reused from {other.parent.parent.name}'
    _dump(P / 'narration.json', narration)
    eyebrow = f'父子科技學院 {header_en}'
    _dump(P / 'slides.json', [{'slide': i, 'title': scenes[i - 1][0], 'eyebrow': eyebrow, 'visibleText': visible[i - 1],
                               'sourceType': content_mode} for i in range(1, 13)])
    _dump(P / 'storyboard.json', [{'slide': i, 'title': scenes[i - 1][0], 'purpose': board[i - 1][0],
                                   'visual': board[i - 1][1] + '（L001 還原版型的原生可編輯文字與圖形）',
                                   'activity': board[i - 1][2], 'motion': 'static + 0.55s fade', 'narrationSentences': 3}
                                  for i in range(1, 13)])

    m = json.loads((P / 'manifest.json').read_text(encoding='utf-8'))
    assert m['episode'] == special and m['slug'] == slug
    m.update(title=title, subtitle=f'父子科技學院 番外篇 {special}｜{delivery_label}', seriesHeader=f'父子科技學院  ·  {header_en}',
             editorialStatus='authored', deckRenderer='ooxml-template', contentMode=content_mode,
             recordingSource=None, autoPublish=False, renderOptions=render_options, sources=dict(src),
             deliveryLabel=delivery_label, classroomNote=classroom_note,
             factCheck={'checkedAt': checked, 'record': 'production/fact-check.md', 'sources': 'production/sources.json'},
             authorization={f'produce{special}': True,
                            'ttsConsent': {'grantedBy': 'user', 'grantedAt': checked, 'service': 'Microsoft Edge TTS',
                                           'voice': 'zh-TW-YunJheNeural', 'scope': f'{special} public narration script only',
                                           'basis': tts_basis, 'excluded': 'private recordings or any other private data'},
                            'paidLlmApi': False, 'uploadToYouTube': False, 'publish': False})
    _dump(P / 'manifest.json', m)

    used = {k for _, _, keys in scenes for k in keys}
    assert used <= set(src), used - set(src)
    ids = {r['id'] for r in source_records}
    assert set(src) <= ids, set(src) - ids
    _dump(P / 'sources.json', {'schemaVersion': 1, 'lessonId': special, 'checkedAt': checked, 'method': source_method,
                               'sources': source_records, 'notVerified': not_verified})
    for name, text in documents.items():
        assert name in ('fact-check.md', 'plan.md', 'delivery-summary.md', 'source-notes.md'), name
        assert '待編寫' not in text
        (P / name).write_text(text, encoding='utf-8')
    for required in ('fact-check.md', 'plan.md', 'delivery-summary.md'):
        assert required in documents, required
    assert documents['delivery-summary.md'].startswith(summary_prefix)
    (E / 'README.md').write_text(readme, encoding='utf-8')
    print(f'{special}: authored 12 scenes / 36 sentences ({sum(len(x) for x in mine)} characters); {len(edits)} template mappings')
    return E
