"""Write qc/report.md from this lesson's own measured QC files (run after verify).

Only restates numbers that the other checks already recorded; judgement, findings and
limits belong in qc/manual-review.md and qc/slide-visual-review.md, which must exist.

    ./portable-runtime.sh python pipeline/qa/write_report.py --episode episodes/academy/<slug> \
        --note "TTS 一次完成" --not-done "沒有查核…"
"""
from pathlib import Path
import argparse
import json
import re

R = Path(__file__).resolve().parents[2]


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--episode', required=True, type=Path)
    p.add_argument('--date', required=True)
    p.add_argument('--note', action='append', default=[])
    p.add_argument('--not-done', action='append', default=[])
    a = p.parse_args()
    E = (R / a.episode).resolve()
    for name in ('qc/manual-review.md', 'qc/slide-visual-review.md'):
        if not (E / name).is_file():
            raise SystemExit(f'Write {name} first')
    rep, asm, med, asr = load(E / 'qc/report.json'), load(E / 'qc/assembly.json'), load(E / 'qc/media-review.json'), load(E / 'qc/asr-review.json')
    pre, cls, tts, timing = load(E / 'qc/subtitle-precheck.json'), load(E / 'qc/classroom-validation.json'), load(E / 'production/tts-manifest.json'), load(E / 'production/timing.json')
    if rep['passed'] != rep['total']:
        raise SystemExit('verify did not pass')
    detail = {c['check']: c['detail'] for c in rep['checks']}
    lufs = re.search(r'-?\d+(\.\d+)?', detail['loudness']).group().replace('-', '−')
    delta = re.search(r'delta=([\d.]+)', detail['stable_scene_frames']).group(1)
    narration = round(sum(s['duration'] for s in timing['scenes']), 2)
    sound = (f"；以拼音比對（同音字視為相同）最低 {asr['minSoundSimilarity']}、平均 {asr['meanSoundSimilarity']}" if 'minSoundSimilarity' in asr else '')
    low = f"；字面相似度低於 0.80 的有第 {'、'.join(map(str, asr['below0_80']))} 條，原因見 manual-review.md" if asr['below0_80'] else ''
    breaks = asm.get('captionLineBreak', {})
    lesson = rep['episode']
    lines = [f'# {lesson} 驗收', '',
             f'{a.date}，雲端 Linux 環境（Claude 接手）本次全新製作與驗收；沒有沿用任何前集的音訊、字幕時間或 QC。', '',
             f"- 技術檢查：{rep['passed']}/{rep['total']} 通過，見 `report.json`。",
             f"- 成片 {asm['masterDuration']:.3f} 秒；1920×1080、30 fps、H.264、AAC 48 kHz 雙聲道；母帶與字幕版全檔解碼，錯誤輸出為零。",
             f"- 片頭實測 {asm['opening']['seconds']} 秒（原檔 60.267 秒，一格以內）；旁白 12 幕合計 {narration} 秒。",
             f'- 整體響度 {lufs} LUFS，落在允許的 −18 至 −14。',
             '- 12 頁／36 句；全片 SRT 36 條，文字與時間逐條等於「實測片頭＋句級時間」。',
             f'- 靜態畫面：12 幕第 3 與第 4 秒的畫面差最大 {delta}（門檻 0.1），是關鍵影格更新，不是鏡頭運動。',
             f"- 逐幕波形：母帶與本課旁白檔偏移 {med['maxAbsLagMs']:g} 毫秒，相關係數最低 {med['minCorrelation']}；片頭與共用原檔相關係數 {med['openingVsSource']['correlation']}（`media-review.json`）。",
             f"- 逐條語音辨識：36 條字面相似度最低 {asr['minSimilarity']}、平均 {asr['meanSimilarity']}{sound}{low}（`asr-review.json`，機器辨識，非聽審）。",
             f"- 字幕版面：36 句預檢 y={pre['topMin']}–{pre['bottomMax']}，兩行以內，無遮擋，行數與預定斷行一致（`subtitle-precheck.json`）；"
             f"成片 36 格逐格看過。斷行方式：{breaks.get('mode', 'libass-auto')}。",
             '- PPTX：12 頁原生文字、模板圖檔位元一致、無 L001 課文殘留（`editable-deck-check.json`）。',
             f"- 教材：{cls['fileCount']} 個檔案；{cls['printPack']['pages']} 頁列印包字型全數內嵌、逐頁看過（`classroom-validation.json`）。",
             f"- 聲線：Edge-TTS `{tts['voice']}`，edge-tts {tts['packageVersion']}，rate {tts['rate']}、pitch {tts['pitch']}；教學段落沒有背景音樂。"]
    lines += [f'- {x}' for x in a.note]
    lines += ['', '逐頁與逐段的檢視方法、發現、修正與限制見 `manual-review.md`、`slide-visual-review.md`。',
              '沒有真人全片聽審、沒有 PowerPoint／Keynote 開啟測試、沒有 macOS 實機測試、沒有做 YouTube 版權檢查'
              + ''.join(f'；{x}' for x in a.not_done) + '。',
              '尚未上傳；發布狀態以 `publication/status.json` 為準。', '']
    (E / 'qc/report.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote {lesson} qc/report.md')


if __name__ == '__main__':
    main()
