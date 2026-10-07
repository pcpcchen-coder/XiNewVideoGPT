"""Author L005 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable: rewrites narration/slides/storyboard/template-text/manifest fields for
episodes/academy/l005-search-master from the text in this file. It never touches
audio, timing, subtitles, video or QC. After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l005/prepare_content.py
"""
from pathlib import Path
import json

R = Path(__file__).resolve().parents[2]
E = R / 'episodes/academy/l005-search-master'
P = E / 'production'
CHECKED = '2026-10-07'

SRC = {
    'curriculum': 'curriculum/catalog.json：L005；來源 V2 Excel 逐堂課程第 5 堂',
    'google_refine': 'https://support.google.com/websearch/answer/2466433?hl=zh-Hant',
    'google_tips': 'https://support.google.com/websearch/answer/134479?hl=zh-Hant',
    'google_filters': 'https://support.google.com/websearch/answer/142143?hl=zh-Hant&co=GENIE.Platform%3DDesktop',
    'google_ai_overview': 'https://support.google.com/websearch/answer/14901683?hl=zh-Hant',
    'google_ads_vs_results': 'https://support.google.com/google-ads/answer/1722080?hl=zh-Hant',
    'google_safesearch': 'https://support.google.com/websearch/answer/510?hl=zh-Hant',
    'ddg_syntax': 'https://duckduckgo.com/duckduckgo-help-pages/results/syntax/',
    'apple_safari_search': 'https://support.apple.com/zh-tw/guide/safari/sfrid73436cb/mac',
    'apple_safari_custom': 'https://support.apple.com/zh-tw/guide/safari/ibrwe75c2a3c/mac',
    'cwa_typhoon': 'https://www.cwa.gov.tw/V8/C/P/Typhoon/TY_NEWS.html',
}

# (scene title, three narration sentences, source keys)
SCENES = [
 ('搜尋高手：把大問題拆成好問題', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第五堂，搜尋高手，這是依課表製作的課前教學版，並非實際上課錄音。',
  '今天我們來玩搜尋尋寶：寶藏是一個大問題的答案，要找到它，得先把大問題拆成幾個好找的小問題。',
  '我們會練習關鍵字、引號、減號和時間條件，最後做出一張屬於自己的搜尋策略卡。'],
  ['curriculum']),
 ('尋寶地圖：三步找到答案', [
  '尋寶有三步，第一步是拆問題，把一個很大的問題，變成幾個小問題，一次只找一個答案。',
  '第二步是選關鍵字，挑出最重要的幾個詞，需要的時候，再加上今天要學的搜尋工具。',
  '第三步是比結果，看看這一頁是誰寫的、資料新不新、有沒有真的回答你的問題，再決定要不要相信。'],
  ['curriculum', 'google_tips']),
 ('關鍵字：挑出最重要的詞', [
  '先練關鍵字。把想問的事情寫成一句完整的話，例如：為什麼貓會一直抓沙發？',
  '接著圈出二到四個最重要的詞，像是貓、抓沙發、原因；盡量使用網頁上可能出現的說法，不必輸入整句口語。',
  '如果結果不理想，就換個說法再試一次，例如把抓沙發換成磨爪，這不是失敗，這是高手都會做的事。'],
  ['google_tips']),
 ('四把鑰匙，打開不同的寶箱', [
  '搜尋尋寶有四把鑰匙：關鍵字幫你說清楚要找什麼，引號用來找完全相符的句子。',
  '減號可以排除不想看到的字詞，時間條件則幫你找到夠新的資料，每一把鑰匙，適合開不同的寶箱。',
  '今天以 Google 搜尋當例子，別的搜尋引擎也有類似的功能，不過寫法和效果可能不太一樣。'],
  ['google_refine', 'ddg_syntax']),
 ('引號：找一字不差的句子', [
  '第一把特別的鑰匙是引號。在一句話的前後加上引號，就是告訴搜尋引擎：請找出和這些字完全相符的內容。',
  '例如想知道床前明月光出自哪一首詩，把這五個字放進引號裡搜尋，就比較容易找到原文和出處。',
  '引號很適合找一句話的出處、歌名或錯誤訊息；記得照畫面上的寫法，使用半形的雙引號。'],
  ['google_refine']),
 ('減號：把不要的結果排除', [
  '第二把鑰匙是減號。有些字詞有兩種意思，例如搜尋蘋果，你想找水果，結果卻可能出現很多手機的網頁。',
  '這時在不想要的字詞前面加上減號，寫成：蘋果，空一格，再打減號和手機，搜尋引擎就會排除含有手機的結果。',
  '要注意，減號和後面的字詞要緊緊貼在一起，中間不能有空格，不然這把鑰匙可能就沒有效果。'],
  ['google_refine']),
 ('時間條件：找夠新的資料', [
  '第三把鑰匙是時間條件。有些問題需要最新的答案，例如今年的比賽結果；有些知識很久都不會變，就不一定要限定時間。',
  '搜尋之後，點選搜尋框下方的工具，就可以依發布時間篩選；也可以照畫面上的寫法，直接在搜尋框加上日期條件。',
  '不過，看得到哪些工具，會因為搜尋內容和瀏覽器而不同，找不到的時候，先換一種搜尋方式試試看。'],
  ['google_filters', 'google_refine']),
 ('拆問題：大問題變小問題', [
  '鑰匙有了，現在來拆問題。假設大問題是：颱風來之前，我們家要準備什麼？這個問題太大，一次搜尋很難找到完整的答案。',
  '把它拆成三個小問題：颱風警報要在哪裡看？要先準備好哪些東西？停電停水的時候怎麼辦？',
  '每個小問題都要能找到一個可以檢查的答案，一次只搜尋一個，再把找到的答案和來源，寫回你的策略卡。'],
  ['curriculum']),
 ('同一題，三種搜法比一比', [
  '接著做實驗，同一個大問題用三種方法搜尋。第一種是模糊搜尋，只輸入颱風兩個字，數一數前五筆結果，有幾筆真的有用。',
  '第二種是精準搜尋，輸入颱風、防災、準備、清單這幾個關鍵字，再數一次，比較兩次結果差在哪裡。',
  '第三種是分段搜尋，三個小問題各搜一次；最後用同樣的標準評分：相關嗎？誰寫的？資料多新？'],
  ['curriculum']),
 ('換你設計：我的搜尋策略卡', [
  '下半場換你設計，完成自己的搜尋策略卡，寫下小問題、用了哪些關鍵字、哪一把鑰匙，以及結果好不好。',
  '再替自己加一條搜尋規則，例如每個問題至少換兩種說法，或是重要的答案，一定要多看幾個不同的來源。',
  '也要記下搜尋的限制：排在最前面不一定最正確，有些結果是有標示的廣告，AI 摘要也可能出錯，重要的事要多方查證。'],
  ['curriculum', 'google_ads_vs_results', 'google_ai_overview']),
 ('兩小時的搜尋尋寶課', [
  '兩小時這樣安排：前十分鐘說明任務，十五分鐘認識四把鑰匙和拆問題，再用四十分鐘比較三種搜法，然後休息十分鐘。',
  '後半段用三十分鐘，完成搜尋策略卡，並測試自己加的那一條規則，再用十分鐘交換角色，由孩子教爸爸怎麼搜尋。',
  '最後五分鐘錄下今天的發現，替作品命名並存檔，把策略卡和比較紀錄，收進本課的資料夾。'],
  ['curriculum']),
 ('最後一關：教爸爸找寶藏', [
  '最後一關，請不看稿，選一個新的大問題，示範給爸爸看：怎麼拆成小問題、怎麼選關鍵字，再用上一把今天學到的鑰匙。',
  '再指出一個限制或安全注意事項，例如第一筆結果不一定正確，還有，不要把密碼、住址這類個人資料打進搜尋框。',
  '今天的作品是搜尋策略卡，下次我們要當來源與證據偵探，分辨真真假假；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum']),
]

# Visible text per slide, in the exact order of the L001 template text boxes
# (pipeline/templates/academy/template-text.json). Line breaks = paragraph breaks.
VISIBLE = [
 ['第五堂任務', '搜尋高手\n把大問題拆成好問題', '用對關鍵字，一步一步找到寶藏', '第五堂  ·  依課表製作的課前教學版'],
 ['尋寶地圖：三步找到答案', '問題越清楚，搜尋結果越有用',
  '01 拆問題', '大問題變小問題\n一次找一個答案', '→',
  '02 選關鍵字', '挑出重要的詞\n加上搜尋工具', '→',
  '03 比結果', '誰寫的？資料多新？\n有回答問題嗎？',
  '今天的作品：一張自己的搜尋策略卡'],
 ['關鍵字：挑出最重要的詞', '把一整句話，換成網頁上可能出現的字詞',
  '01', '先寫下完整的問題', '例如：為什麼貓會一直抓沙發？',
  '02', '圈出二到四個關鍵詞', '貓　抓沙發　原因',
  '03', '換個說法再試一次', '貓　磨爪　怎麼辦'],
 ['四把鑰匙，打開不同的寶箱', '每一把鑰匙，解決不同的問題', '搜尋尋寶的四把鑰匙',
  '關鍵字', '說清楚找什麼', '引號', '完全相符', '減號', '排除字詞', '時間條件', '找夠新的資料',
  '以 Google 搜尋為例；其他搜尋引擎的寫法可能不同'],
 ['引號：找一字不差的句子', '想找一句話的出處時，請它完全相符',
  '一般搜尋', '床前明月光', '→', '加上引號', '"床前明月光"',
  '引號裡的字詞，要完全相符才算找到',
  '適合找一句話的出處、歌名、錯誤訊息；使用半形雙引號'],
 ['減號：把不要的結果排除', '有些字詞有兩種意思，先排除不要的那一種',
  '01 想找水果', '搜尋：蘋果', '02 出現手機', '同一個詞有兩種意思', '03 加上減號', '蘋果 -手機',
  '減號緊貼著要排除的字詞，中間不要空格'],
 ['時間條件：找夠新的資料', '先想一想：這個問題需要最新的答案嗎？',
  '搜尋之後  →  工具  →  依時間篩選',
  '找最新消息', '選比較近的時間', '找不變的知識', '不一定要限定時間', '直接輸入條件', 'after:2026/01/01',
  '看得到哪些工具，會因搜尋內容和瀏覽器而不同'],
 ['拆問題：大問題變小問題', '每個小問題，都要能找到一個可以檢查的答案',
  '一、颱風警報要在哪裡看？\n二、要先準備好哪些東西？\n三、停電停水時怎麼辦？',
  '大問題（藏寶圖）', '颱風來之前要準備什麼？', '一次只搜尋一個小問題\n答案和來源寫回策略卡',
  '暫停影片：把你的大問題，拆成三個小問題'],
 ['同一題，三種搜法比一比', '評分標準：相關嗎？誰寫的？資料多新？',
  '第一種：模糊搜尋', '只輸入：颱風\n數一數前五筆，有幾筆有用',
  '第二種：精準搜尋', '輸入：颱風 防災 準備 清單\n再數一次，比較差在哪裡',
  '第三種：分段搜尋，三個小問題各搜一次，再用同樣標準評分'],
 ['換你設計：我的搜尋策略卡', '找到答案之後，還要判斷能不能相信',
  '01', '完成我的搜尋策略卡', '小問題、關鍵字、用了哪把鑰匙、結果如何',
  '02', '加一條自己的搜尋規則', '例如：每題換兩種說法、重要答案多看幾個來源',
  '03', '記下搜尋的限制', '前面的不一定最正確；廣告有標示；AI 摘要可能出錯'],
 ['兩小時的搜尋尋寶課', '影片先引路，接下來用策略卡證明你會找答案',
  '00–25', '開場十分＋概念十五分', '25–65', '三種搜法尋寶賽', '65–75', '休息十分鐘',
  '75–105', '策略卡＋自選規則', '105–115', '孩子教爸爸搜尋', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：資訊判讀，找到答案還要看誰寫的、多新'],
 ['最後一關：教爸爸找寶藏', '暫停影片：不看稿示範一次，再指出一個限制或安全注意',
  '01', '完成搜尋策略卡', '三個小問題、關鍵字與用過的鑰匙',
  '02', '示範四把鑰匙', '關鍵字、引號、減號、時間條件',
  '03', '指出一個限制或安全注意', '例如：第一筆不一定對；不輸入個資',
  '保持好奇，我們下次見！'],
]

# Teaching purpose, on-screen diagram and the hands-on prompt for every scene.
BOARD = [
 ('開場：課前教學版揭露、尋寶任務與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備紙筆與瀏覽器；預告四把鑰匙與搜尋策略卡'),
 ('概念：搜尋三步驟（拆問題、選關鍵字、比結果）', '三步流程卡：拆問題 → 選關鍵字 → 比結果', '說出今天要完成的作品'),
 ('概念與例子：把口語問題換成關鍵字，並換說法重試', '三點條列＋陳犀牛：完整問題、圈關鍵詞、換說法', '把自己的一個問題圈出二到四個關鍵詞'),
 ('例子：四種搜尋工具各自的用途；以 Google 為例並說明其他引擎可能不同', '工具卡面板：關鍵字、引號、減號、時間條件', '先猜每把鑰匙適合哪一種情況'),
 ('示範：引號＝完全相符', '雙框對照：一般搜尋 → 加上引號', '用引號找一句話的出處'),
 ('示範：減號＝排除字詞；運算子與字詞之間不可有空格', '三張步驟卡：想找水果／出現手機／加上減號', '實際輸入並比較加減號前後的結果'),
 ('示範：時間條件；工具會因查詢與瀏覽器而異', '路徑一行（搜尋之後→工具→依時間篩選）＋三張情境卡', '判斷自己的問題需不需要最新資料'),
 ('活動規則：把大問題拆成三個可檢查的小問題', '左側三個小問題；右側大問題與做法', '暫停影片：拆自己的大問題'),
 ('共同實作與比較：模糊、精準、分段三種搜法，用同一套標準評分', '左右比較卡（模糊／精準）＋黃字說明分段搜尋與評分', '同一題做三種搜尋，數前五筆並記錄'),
 ('獨立改造與資訊判讀：策略卡、自選規則、搜尋的限制', '三點條列＋陳犀牛：策略卡、自選規則、限制', '完成策略卡；自訂一條規則並測試'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：示範拆題與四把鑰匙，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子教爸爸；錄音回答四個問題；作品命名存檔'),
]

EYEBROW = '父子科技學院 SEARCH QUEST'


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
    for prev in ('l003-keyboard-ninja', 'l004-network-relay'):
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
        title='搜尋高手：把大問題拆成好問題',
        subtitle='父子科技學院 第五堂｜依課表製作的課前教學版',
        seriesHeader='父子科技學院  ·  SEARCH QUEST',
        editorialStatus='authored', deckRenderer='ooxml-template',
        contentMode='curriculum-based-preclass', recordingSource=None, autoPublish=False,
        # Slides show literal search syntax; LibreOffice's automatic CJK/Latin gap would misrepresent it.
        renderOptions={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        sources={k: v for k, v in SRC.items()},
        factCheck={'checkedAt': CHECKED, 'record': 'production/fact-check.md', 'sources': 'production/sources.json'},
        authorization={
            'produceL005': True,
            'ttsConsent': {'grantedBy': 'user', 'grantedAt': CHECKED, 'service': 'Microsoft Edge TTS',
                           'voice': 'zh-TW-YunJheNeural', 'scope': 'L005 public narration script only',
                           'basis': "Session launch prompt consented to sending 'these three lessons' public narration to Edge TTS; "
                                    "the user then asked in the same session to continue with L005.",
                           'excluded': 'private recordings or any other private data'},
            'paidLlmApi': False, 'uploadToYouTube': False, 'publish': False})
    write('manifest.json', m)

    lp = R / 'lessons/L005/lesson.json'
    lesson = json.loads(lp.read_text(encoding='utf-8'))
    lesson['episodePaths'] = [E.relative_to(R).as_posix()]
    lesson['status'] = 'preclass-production'
    lp.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Authored {len(SCENES)} scenes / {sum(len(x[1]) for x in SCENES)} sentences; {len(edits)} template mappings')


if __name__ == '__main__':
    main()
