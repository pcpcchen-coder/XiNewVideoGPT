"""Author L006 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable: rewrites narration/slides/storyboard/template-text/manifest fields for
episodes/academy/l006-source-evidence from the text in this file. It never touches
audio, timing, subtitles, video or QC. After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l006/prepare_content.py
"""
from pathlib import Path
import json

R = Path(__file__).resolve().parents[2]
E = R / 'episodes/academy/l006-source-evidence'
P = E / 'production'
CHECKED = '2026-10-07'

SRC = {
    'curriculum': 'curriculum/catalog.json：L006；來源 V2 Excel 逐堂課程第 6 堂',
    'loc_primary': 'https://loc.gov/programs/teachers/getting-started-with-primary-sources',
    'cor_three_questions': 'https://cor.inquirygroup.org/blog/get-started-now',
    'princeton_lateral': 'https://libguides.princeton.edu/medialiteracy/lateralreading',
    'ifla_fake_news': 'https://www.ifla.org/?p=110161',
    'ftc_disclosures': 'https://ftc.gov/system/files/documents/plain-language/1001a-influencer-guide-508_1.pdf',
    'ftc_disclosures_blog': 'https://www.ftc.gov/business-guidance/blog/2019/11/disclosures-101-new-ftc-resources-social-media-influencers',
    'ftc_phishing': 'https://consumer.ftc.gov/consumer-alerts/2025/04/protect-yourself-phishing-scams',
    'google_ads_vs_results': 'https://support.google.com/google-ads/answer/1722080?hl=zh-Hant',
    'tfc': 'https://tfc-taiwan.org.tw/?p=104895',
    'catalog_reference': 'https://consumer.ftc.gov/identity-theft-and-online-security/online-privacy-and-security',
}

# (scene title, three narration sentences, source keys)
SCENES = [
 ('真真假假：來源與證據偵探', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第六堂，來源與證據偵探，這是依課表製作的課前教學版，並非實際上課錄音。',
  '網路上的消息真真假假，今天我們要當偵探：先看這句話是誰說的，再看證據在哪裡。',
  '我們會分析五則科技消息，替每一則的可信度打分數，最後完成一張來源可信度評分表。'],
  ['curriculum']),
 ('偵探三問：每則消息都要問', [
  '偵探辦案有三個問題。第一問，誰說的？找出這則消息背後的人或單位，看他對這件事了解多少。',
  '第二問，證據呢？看看有沒有可以回頭檢查的東西，例如出處、日期、數字，或是原始照片。',
  '第三問，別人也這麼說嗎？離開這一頁，找找看有沒有另一個可靠的來源，說法是不是一致。'],
  ['cor_three_questions']),
 ('兩種來源：原始與二手', [
  '先認識兩種來源。原始來源是第一手的紀錄，例如官方公告、當事人自己的說明，或是現場拍下的原始照片。',
  '二手來源是別人整理或轉述的內容，例如整理消息的報導、懶人包，還有朋友轉貼過來的訊息。',
  '二手來源很方便，但是轉述的過程可能漏掉重點，或加進別的意思，遇到重要的事，記得回頭找原始來源。'],
  ['loc_primary']),
 ('把消息分成四類', [
  '接下來，把看到的消息分成四類：原始來源、二手來源、廣告，還有意見，分對了，才知道該怎麼檢查。',
  '廣告的目的，是讓你想買東西或下載程式；意見是一個人的感覺和看法，每個人可以不一樣，所以不能直接當成事實。',
  '同一則消息常常混著好幾類，例如一篇開箱文，可能有事實、有意見，同時還是和廠商合作的廣告。'],
  ['curriculum', 'ftc_disclosures']),
 ('意見，還是可以檢查的說法？', [
  '怎麼分辨意見和可以檢查的說法？聽聽這兩句：這支手機最好用；這支手機重一百八十公克。',
  '第一句是意見，每個人的答案可能不同；第二句可以檢查，查官方規格，或是拿秤量一量，就知道對不對。',
  '所以看到一句話，先問自己：這句話有辦法查出對或錯嗎？查得出來的，才能拿來當證據。'],
  ['curriculum']),
 ('廣告與業配：先找標示', [
  '再來看廣告。廣告和廠商合作的內容，通常會有標示，例如廣告、贊助、合作這些字，先把它找出來。',
  '接著想一想目的：這則內容是不是希望你買東西、下載程式，或是點進某一個連結？',
  '不過，沒有標示不代表一定不是廣告，所以重要的決定，要再找一個和廠商沒有合作關係的來源來比較。'],
  ['ftc_disclosures', 'ftc_disclosures_blog', 'google_ads_vs_results']),
 ('證據：可以回頭檢查的東西', [
  '證據是可以回頭檢查的東西。好的消息會告訴你出處，讓你點進去看原文，而不是只說聽說，或是有人說。',
  '還要看日期，舊消息被重新轉貼，很容易讓人以為是剛發生的事；數字和照片，也要查得到是從哪裡來的。',
  '要記得，很多人轉貼、很多人按讚，只代表它很熱門，不代表它是真的。'],
  ['ifla_fake_news']),
 ('找第二來源：離開這一頁去查', [
  '找第二來源有個好方法：不要只停在同一頁，開一個新分頁，搜尋這個網站或作者的名字，看看別人怎麼說。',
  '再找另一個彼此沒有關係的來源，比一比兩邊的說法；如果只是互相轉貼，那其實還是同一個來源。',
  '如果找不到第二來源，先不要急著相信或轉傳，在評分表上老實寫下：還不確定。'],
  ['princeton_lateral', 'cor_three_questions']),
 ('偵探競速：快分類，慢判斷', [
  '現在開始偵探競速。第一回合比快：五張練習卡，限時三分鐘，分出原始來源、二手來源、廣告和意見。',
  '第二回合比準，不比快：替每一則消息打五項分數，來源、日期、證據、目的，還有第二來源。',
  '每一項零到二分，滿分十分；分數旁邊一定要寫理由，因為偵探靠的是證據，不是感覺。'],
  ['curriculum']),
 ('換你當主審：來源可信度評分表', [
  '下半場換你當主審，自己完成來源可信度評分表，把五則消息的分數、理由和第二來源都填上去。',
  '再加一條你自己的偵探規則，例如沒有日期就先扣分，或是轉傳之前，一定要先查過來源。',
  '也要記下評分表的限制：分數高不保證一定是真的，查不到的時候，寫不確定，比亂猜更厲害。'],
  ['curriculum']),
 ('兩小時的來源偵探課', [
  '這堂課兩小時：開場十分鐘，概念十五分鐘，接著四十分鐘，父子一起分析五則消息，然後休息十分鐘。',
  '休息回來，用三十分鐘完成評分表和自選規則，再用十分鐘交換角色，換孩子教爸爸怎麼查證。',
  '最後五分鐘錄音總結，替作品取名字、存好檔案，把評分表收進這一課的資料夾。'],
  ['curriculum']),
 ('最後一關：教爸爸當偵探', [
  '最後一關，請不看稿，拿一則新的消息，對爸爸示範偵探三問：誰說的？證據呢？別人也這麼說嗎？',
  '再說出一個限制或安全注意事項，例如可疑的連結不要亂點，要求輸入密碼或個人資料的頁面，先停下來問爸爸。',
  '今天的作品是來源可信度評分表，下次我們要蓋密碼城堡，認識雙重驗證；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum', 'ftc_phishing']),
]

# Visible text per slide, in the exact order of the L001 template text boxes
# (pipeline/templates/academy/template-text.json). Line breaks = paragraph breaks.
VISIBLE = [
 ['第六堂任務', '真真假假\n來源與證據偵探', '先看誰說的，再看證據在哪裡', '第六堂  ·  依課表製作的課前教學版'],
 ['偵探三問：每則消息都要問', '先問清楚，再決定要不要相信',
  '01 誰說的？', '找出背後的人或單位\n他了解這件事嗎？', '→',
  '02 證據呢？', '出處、日期、數字\n可以回頭檢查嗎？', '→',
  '03 別人呢？', '別人也這麼說嗎？\n找第二個來源',
  '今天的作品：一張來源可信度評分表'],
 ['兩種來源：原始與二手', '第一手的紀錄，和別人整理過的內容',
  '01', '原始來源：第一手的紀錄', '官方公告、當事人的說明、現場原始照片',
  '02', '二手來源：別人的整理', '整理消息的報導、懶人包、轉貼的訊息',
  '03', '重要的事，回頭找原始來源', '轉述可能漏掉重點，或加進別的意思'],
 ['把消息分成四類', '分對了，才知道該怎麼檢查', '消息的四種類型',
  '原始來源', '第一手紀錄', '二手來源', '別人的整理', '廣告', '想要你買東西', '意見', '個人的看法',
  '同一則消息，常常混著好幾類'],
 ['意見，還是可以檢查的說法？', '查得出對或錯的，才能拿來當證據',
  '意見', '這支手機最好用', '≠', '可以檢查的說法', '這支手機重 180 公克',
  '意見可以聽，但不能直接當成事實',
  '先問自己：這句話有辦法查出對或錯嗎？'],
 ['廣告與業配：先找標示', '和廠商有合作關係的內容，應該清楚說明',
  '01 找標示', '廣告、贊助、合作', '02 想目的', '要你買、下載或點連結？', '03 再比較', '找沒有合作關係的來源',
  '沒有標示，不代表一定不是廣告'],
 ['證據：可以回頭檢查的東西', '只說「聽說」或「有人說」，還不算證據',
  '有出處  →  有日期  →  查得到',
  '看出處', '點進去看原文', '看日期', '是不是舊消息？', '看數字和照片', '查得到出處嗎？',
  '很多人轉貼或按讚，只代表熱門，不代表是真的'],
 ['找第二來源：離開這一頁去查', '開一個新分頁，看看別人怎麼說',
  '一、開新分頁，搜尋網站或作者\n二、找另一個沒有關係的來源\n三、比一比，兩邊說法一致嗎？',
  '第二來源（橫向查證）', '互相轉貼，還是同一個來源', '找不到第二來源時\n先寫下「還不確定」',
  '暫停影片：替一則消息找出第二來源'],
 ['偵探競速：快分類，慢判斷', '分類可以比快；可信度要慢慢打分',
  '第一回合：快分類', '五張練習卡，限時三分鐘\n原始、二手、廣告還是意見？',
  '第二回合：慢判斷', '五項各 0 到 2 分，滿分 10 分\n來源、日期、證據、目的、第二來源',
  '每個分數旁邊都要寫理由：偵探靠證據，不靠感覺'],
 ['換你當主審：來源可信度評分表', '分數要有理由，查不到就老實寫',
  '01', '完成來源可信度評分表', '五則消息的分數、理由與第二來源',
  '02', '加一條自己的偵探規則', '例如：沒有日期先扣分、轉傳之前先查來源',
  '03', '記下評分表的限制', '高分不保證是真的；查不到就寫「不確定」'],
 ['兩小時的來源偵探課', '影片先引路，接下來用評分表證明你會查證',
  '00–25', '開場十分＋概念十五分', '25–65', '五則消息偵探賽', '65–75', '休息十分鐘',
  '75–105', '評分表＋自選規則', '105–115', '孩子教爸爸查證', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：資訊判讀，轉傳之前先查來源和證據'],
 ['最後一關：教爸爸當偵探', '暫停影片：不看稿示範一次，再指出一個限制或安全注意',
  '01', '完成來源可信度評分表', '五則消息都有分數和理由',
  '02', '示範偵探三問', '誰說的？證據呢？別人也這麼說嗎？',
  '03', '指出一個限制或安全注意', '例如：可疑連結不亂點；不輸入個資',
  '保持好奇，我們下次見！'],
]

# Teaching purpose, on-screen diagram and the hands-on prompt for every scene.
BOARD = [
 ('開場：課前教學版揭露、偵探任務與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備紙筆與瀏覽器；預告偵探三問與來源可信度評分表'),
 ('概念：偵探三問（誰說的、證據呢、別人也這麼說嗎）', '三步流程卡：誰說的？ → 證據呢？ → 別人呢？', '說出今天要完成的作品'),
 ('概念：原始來源與二手來源；重要的事回頭找原始來源', '三點條列＋陳犀牛：原始來源、二手來源、回頭找原始來源', '各舉一個原始來源與二手來源的例子'),
 ('概念：原始來源、二手來源、廣告、意見四類；同一則消息可能混合多類', '類型卡面板：原始來源、二手來源、廣告、意見', '替最近看到的一則消息分類'),
 ('例子：意見與可檢查的說法；可檢查的才能當證據', '雙框對照：意見 ≠ 可以檢查的說法', '各說一句意見和一句可以檢查的說法'),
 ('概念與例子：廣告與合作內容的標示、目的；沒有標示不代表不是廣告', '三張步驟卡：找標示／想目的／再比較', '在一則內容裡找出標示並說出目的'),
 ('概念：證據＝可回頭檢查；出處、日期、數字與照片；熱門不等於真實', '路徑一行（有出處→有日期→查得到）＋三張檢查卡', '替一則消息找出處與日期'),
 ('示範：橫向查證找第二來源；互相轉貼不算第二來源；查不到就寫不確定', '左側三步驟；右側第二來源重點與做法', '暫停影片：替一則消息找出第二來源'),
 ('活動規則：競速只用在分類；可信度評分五項各 0 到 2 分並寫理由', '左右比較卡（快分類／慢判斷）＋黃字說明要寫理由', '第一回合限時分類；第二回合逐則評分'),
 ('獨立改造與資訊判讀：評分表、自選偵探規則、評分表的限制', '三點條列＋陳犀牛：評分表、自選規則、限制', '完成評分表；自訂一條規則並測試'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：示範偵探三問，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子教爸爸；錄音回答四個問題；作品命名存檔'),
]

EYEBROW = '父子科技學院 SOURCE DETECTIVE'


def write(name, data):
    (P / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    assert len(SCENES) == len(VISIBLE) == len(BOARD) == 12
    seed = json.loads((R / 'pipeline/templates/academy/template-text.json').read_text(encoding='utf-8'))
    edits = []
    for i, values in enumerate(VISIBLE, 1):
        old = [x['old'] for x in seed if x['slide'] == i]
        assert len(old) == len(values), (i, len(old), len(values))
        for o, v in zip(old, values):
            assert o.count('\n') == v.count('\n'), (i, o, v)
            assert v.strip() and '待編寫' not in v, (i, v)
            edits.append({'slide': i, 'old': o, 'new': v})
    # Teaching text must be new; only counters, arrows, clock ranges and the fixed
    # series labels (break / signoff) may equal the L001 reference text.
    same = [(e['slide'], e['new']) for e in edits if e['old'] == e['new']]
    allowed = {'→', '01', '02', '03', '00–25', '25–65', '65–75', '75–105', '105–115', '115–120',
               '休息十分鐘', '保持好奇，我們下次見！'}
    assert all(v in allowed for _, v in same), same
    write('template-text.json', edits)

    narration = [{'slide': i, 'title': t,
                  'sentences': [{'text': s, 'tts': s} for s in sentences],
                  'sources': [SRC[k] for k in keys], 'sourceType': 'curriculum-based-preclass'}
                 for i, (t, sentences, keys) in enumerate(SCENES, 1)]
    assert all(len(x['sentences']) == 3 for x in narration)
    assert '我是陳犀牛，保持好奇，我們下次見！' in narration[-1]['sentences'][-1]['text']
    # Must not reuse any narration sentence of an earlier lesson.
    for prev in ('l003-keyboard-ninja', 'l004-network-relay', 'l005-search-master'):
        old_n = json.loads((R / 'episodes/academy' / prev / 'production/narration.json').read_text(encoding='utf-8'))
        seen = {x['text'] for s in old_n for x in s['sentences']}
        assert not seen & {x['text'] for s in narration for x in s['sentences']}, prev
    write('narration.json', narration)

    write('slides.json', [{'slide': i, 'title': SCENES[i - 1][0], 'eyebrow': EYEBROW,
                           'visibleText': VISIBLE[i - 1], 'sourceType': 'curriculum-based-preclass'}
                          for i in range(1, 13)])
    write('storyboard.json', [{'slide': i, 'title': SCENES[i - 1][0], 'purpose': BOARD[i - 1][0],
                               'visual': BOARD[i - 1][1] + '（L001 還原版型的原生可編輯文字與圖形）',
                               'activity': BOARD[i - 1][2], 'motion': 'static + 0.55s fade',
                               'narrationSentences': 3} for i in range(1, 13)])

    m = json.loads((P / 'manifest.json').read_text(encoding='utf-8'))
    m.update(
        title='真真假假：來源與證據偵探',
        subtitle='父子科技學院 第六堂｜依課表製作的課前教學版',
        seriesHeader='父子科技學院  ·  SOURCE DETECTIVE',
        editorialStatus='authored', deckRenderer='ooxml-template',
        contentMode='curriculum-based-preclass', recordingSource=None, autoPublish=False,
        # Literal spacing on slides (no automatic CJK/Latin gap on top of typed spaces); burned
        # captions break after punctuation instead of libass' character-count balance.
        renderOptions={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        sources={k: v for k, v in SRC.items()},
        factCheck={'checkedAt': CHECKED, 'record': 'production/fact-check.md', 'sources': 'production/sources.json'},
        authorization={
            'produceL006': True,
            'ttsConsent': {'grantedBy': 'user', 'grantedAt': CHECKED, 'service': 'Microsoft Edge TTS',
                           'voice': 'zh-TW-YunJheNeural', 'scope': 'L006 public narration script only',
                           'basis': "Session launch prompt consented to sending 'these three lessons' public narration to Edge TTS; "
                                    "the user then asked in the same session to continue with the next two lessons; this is the third lesson of the session.",
                           'excluded': 'private recordings or any other private data'},
            'paidLlmApi': False, 'uploadToYouTube': False, 'publish': False})
    write('manifest.json', m)

    lp = R / 'lessons/L006/lesson.json'
    lesson = json.loads(lp.read_text(encoding='utf-8'))
    lesson['episodePaths'] = [E.relative_to(R).as_posix()]
    lesson['status'] = 'preclass-production'
    lp.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Authored {len(SCENES)} scenes / {sum(len(x[1]) for x in SCENES)} sentences; {len(edits)} template mappings')


if __name__ == '__main__':
    main()
