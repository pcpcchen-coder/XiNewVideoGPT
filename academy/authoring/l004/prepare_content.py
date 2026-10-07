"""Author L004 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable: rewrites narration/slides/storyboard/template-text/sources/manifest fields
for episodes/academy/l004-network-relay from the text in this file. It never touches
audio, timing, subtitles, video or QC. After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l004/prepare_content.py
"""
from pathlib import Path
import json

R = Path(__file__).resolve().parents[2]
E = R / 'episodes/academy/l004-network-relay'
P = E / 'production'
CHECKED = '2026-10-07'

SRC = {
    'curriculum': 'curriculum/catalog.json：L004；來源 V2 Excel 逐堂課程第 4 堂',
    'rfc1122': 'https://www.rfc-editor.org/rfc/rfc1122',
    'rfc791': 'https://www.rfc-editor.org/rfc/rfc791',
    'rfc1812': 'https://www.rfc-editor.org/rfc/rfc1812',
    'rfc9293': 'https://www.rfc-editor.org/rfc/rfc9293',
    'rfc768': 'https://www.rfc-editor.org/rfc/rfc768',
    'rfc1034': 'https://www.rfc-editor.org/rfc/rfc1034',
    'rfc9110': 'https://www.rfc-editor.org/rfc/rfc9110',
    'rfc6761': 'https://www.rfc-editor.org/rfc/rfc6761',
    'rfc5737': 'https://www.rfc-editor.org/rfc/rfc5737',
    'icann_dns': 'https://www.icann.org/resources/pages/dns-2022-09-13-en',
    'apple_wifi': 'https://support.apple.com/zh-tw/guide/mac-help/mh11935/mac',
    'apple_dns': 'https://support.apple.com/zh-tw/guide/mac-help/mh141272/mac',
    'apple_dhcp': 'https://support.apple.com/zh-tw/guide/mac-help/mchlp2718/mac',
    'ftc_wifi': 'https://consumer.ftc.gov/articles/how-secure-your-home-wi-fi-network',
}

# (scene title, three narration sentences, source keys)
SCENES = [
 ('網路到底是什麼：封包接力賽', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第四堂，封包接力賽，這是依課表製作的課前教學版，並非實際上課錄音。',
  '今天我們來當網路偵探，查清楚一件事：螢幕上看到的一張圖片，是怎麼從遠方的電腦送到你面前的。',
  '我們會用信封、地址卡和路由站來扮演網路，親手把一張圖片送出去，最後畫出一張自己家的網路圖。'],
  ['curriculum']),
 ('案件：一張圖片怎麼送到？', [
  '網際網路是許多網路互相連接而成的大網路，你的裝置先連上家裡的路由器，再經過外面的網路，連到保存圖片的伺服器。',
  '圖片不是整張一次送過來的，資料會分成許多小份，每一份叫做封包，由路由器一站接著一站，往目的地轉送。',
  '所以今天的案件有三個線索：誰送出要求、誰負責轉送、誰回應要求，請你邊看邊在紙上記下這三個角色。'],
  ['curriculum', 'rfc1122', 'rfc9293', 'rfc9110']),
 ('IP 位址：封包要送到哪裡', [
  '要把封包送對地方，網路需要位址；連上網路的裝置會有一個 IP 位址，它是一組編號，標示封包從哪裡來、要送到哪裡。',
  '每個封包都帶著來源位址和目的地位址，路由器查看目的地位址，決定下一站要交給誰，並不需要讀懂圖片的內容。',
  '這很像信封上的收件地址，不過 IP 位址不是你家的門牌，連到不同的網路時，拿到的位址通常也不一樣。'],
  ['rfc791', 'rfc1812', 'apple_dhcp']),
 ('接力賽的四個角色', [
  '接力賽有四個角色：裝置是起點也是終點，像你的電腦或手機，負責送出要求，也負責把收到的封包組回圖片。',
  '路由器是轉運站，每次只決定下一站；DNS 像網路的通訊錄，用名稱查出位址；伺服器保存資料，並回應裝置的要求。',
  '四個角色各有各的工作，等一下的接力賽，你和爸爸要輪流扮演，親自體驗每個角色做了什麼。'],
  ['rfc1122', 'rfc1812', 'icann_dns', 'rfc9110']),
 ('DNS 通訊錄：用名稱查出位址', [
  '人比較容易記住名稱，網路卻要靠位址來送封包，所以裝置會先問 DNS：這個網域名稱，對應的 IP 位址是什麼？',
  'DNS 回答之後，裝置才把封包送往那個位址；畫面上的範例名稱和範例位址，都是保留給文件使用的，不是真實的對應。',
  'DNS 只負責查位址，不負責運送圖片；如果名稱打錯了，可能查不到，也可能被帶到不是你想去的地方。'],
  ['icann_dns', 'apple_dns', 'rfc1034', 'rfc6761', 'rfc5737']),
 ('封包：切開、標記、重組', [
  '再來看封包本身，第一步是切開：圖片的資料會分成許多小份，網路就能一份一份地傳送，出了問題也只要處理其中一小份。',
  '第二步是標記：每個封包除了位址，還會帶著編號這類資訊，讓接收的一方知道它排在第幾個。',
  '第三步是重組：封包到達後，裝置依照編號排回正確的順序，全部到齊了，才能還原成你看到的那張圖片。'],
  ['rfc9293', 'rfc1122']),
 ('封包接力賽：道具與賽道', [
  '現在把桌面變成網路，準備信封、地址卡，還有一張簡單的圖片；圖片請用自己畫的圖，不要用含有個人資料的照片。',
  '賽道上有四個點：孩子當裝置，爸爸當伺服器，中間放兩個路由站，可以用椅子或紙盒代替，並各放一張轉送表。',
  '每個信封就是一個封包，地址卡代表 IP 位址，路由站就是路由器，只看信封上的目的地，把它交給下一站。'],
  ['curriculum', 'rfc1812']),
 ('第一案：把圖片完整送到', [
  '第一案開始，孩子先查通訊錄卡，找到伺服器的位址，再寫一張要求卡裝進信封，經過兩個路由站，送到爸爸手上。',
  '爸爸扮演伺服器，把圖片剪成六片，每個信封寫上來源和目的地，還有第幾片、共幾片，然後一次送出一個信封。',
  '孩子收齊六個信封後，依照編號把圖片拼回來，再回傳一張確認卡，告訴伺服器，六片全部收到了。'],
  ['curriculum', 'rfc9293']),
 ('第二、三案：亂序與遺失', [
  '第二案，路由器會分別處理每一個封包，所以同一張圖片的封包不一定走同一條路，到達的順序也可能被打亂，這時要靠編號排回來。',
  '第三案，封包在途中也可能遺失；爸爸悄悄抽走一個信封，孩子要從編號找出少了哪一片，再請伺服器重送那一片。',
  '要記得，網路本身不保證每個封包都送到，是某些傳送規則加上了確認和重送；也有些規則比較簡單，並不負責重送。'],
  ['rfc1122', 'rfc791', 'rfc9293', 'rfc768']),
 ('換你設計：新規則＋家庭網路圖', [
  '下半場換你設計，替接力賽增加一條自己的規則，例如多一個路由站或限時送完；先預測，再測試，把證據寫進偵探筆記。',
  '接著畫家庭網路手繪圖，畫出家裡有哪些裝置、路由器放在哪裡，以及通往外面網路的那一條連線。',
  '想找線索，可以請爸爸打開系統設定，在 Wi-Fi 的詳細資訊查看 IP 位址和路由器位址；Wi-Fi 密碼和住址，不要寫在圖上。'],
  ['curriculum', 'apple_wifi', 'ftc_wifi']),
 ('兩小時的網路偵探課', [
  '兩小時這樣安排：前十分鐘說明案件，十五分鐘認識六個名詞和四個角色，再用四十分鐘一起完成三個案件，然後休息十分鐘。',
  '後半段用三十分鐘，測試自己的新規則，並完成家庭網路手繪圖，再用十分鐘交換角色，由孩子教爸爸封包怎麼旅行。',
  '最後五分鐘錄下今天的發現，替作品命名並存檔，把手繪圖、偵探筆記和規則卡，收進本課的資料夾。'],
  ['curriculum']),
 ('最後一關：換你當老師', [
  '最後一關，請不看稿，向爸爸說明一張圖片的旅程：DNS 查出位址，資料分成封包，路由器一站一站轉送，裝置再把它重組回來。',
  '再指出一個限制或安全注意事項，例如信封只是比喻，封包可能亂序或遺失，還有家裡的 Wi-Fi 密碼不可以公開。',
  '今天的作品是家庭網路手繪圖，下次我們要練習搜尋，把大問題拆成好問題；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum', 'ftc_wifi']),
]

# Visible text per slide, in the exact order of the L001 template text boxes
# (pipeline/templates/academy/template-text.json). Line breaks = paragraph breaks.
VISIBLE = [
 ['第四堂任務', '網路到底是什麼\n封包接力賽', '把圖片分成封包，一站一站送到', '第四堂  ·  依課表製作的課前教學版'],
 ['案件：一張圖片怎麼送到？', '當網路偵探，記下三個角色各做了什麼',
  '01 我的裝置', '送出要求\n收下封包', '→',
  '02 路由器', '看目的地位址\n轉給下一站', '→',
  '03 伺服器', '保存圖片等資料\n回應裝置的要求',
  '網際網路＝許多網路互相連接；封包＝分成小份的資料'],
 ['IP 位址：封包要送到哪裡', '像信封上的地址，但不是你家的門牌',
  '01', '裝置連上網路，會有 IP 位址', '一組編號，標示封包從哪裡來、要送到哪裡',
  '02', '每個封包帶著兩個位址', '來源位址＋目的地位址',
  '03', '路由器查看目的地位址', '決定下一站；不需要讀懂圖片內容'],
 ['接力賽的四個角色', '每個角色只做自己的工作', '封包接力賽角色卡',
  '裝置', '送出與接收', '路由器', '轉送到下一站', 'DNS', '用名稱查位址', '伺服器', '回應要求',
  '你和爸爸輪流扮演：先說出職責，再開始接力'],
 ['DNS 通訊錄：用名稱查出位址', '人記名稱，網路靠位址；先查位址，再送封包',
  '網域名稱（範例）', 'example.com', '→', 'IP 位址（範例）', '192.0.2.1',
  '裝置先向 DNS 查出位址，才送出封包',
  '兩者都是保留給文件使用的範例，不是真實對應；DNS 不運送圖片'],
 ['封包：切開、標記、重組', '大資料分成小份，到達後再拼回來',
  '01 切開', '圖片資料分成許多小份', '02 標記', '帶著位址與編號', '03 重組', '依編號排回原來的樣子',
  '你來想一想：如果信封上沒有編號，會發生什麼事？'],
 ['封包接力賽：道具與賽道', '圖片用自己畫的圖，不放個人資料',
  '裝置  →  路由站 A  →  路由站 B  →  伺服器',
  '信封＝封包', '每個裝一片圖片', '地址卡＝IP 位址', '寫上來源與目的地', '路由站＝路由器', '看目的地，交給下一站',
  '暫停影片：排好四個點，放好轉送表，再開始第一案'],
 ['第一案：把圖片完整送到', '孩子當裝置，爸爸當伺服器，路由站照轉送表轉送',
  '查：通訊錄卡找位址\n送：要求卡過兩站\n拼：依編號拼回圖片',
  '信封上要寫', '第三片，共六片', '來源：伺服器的位址\n目的地：裝置的位址',
  '暫停影片：六片都拼好，再回傳「全部收到」確認卡'],
 ['第二、三案：亂序與遺失', '先找證據，再想修正方法',
  '第二案：順序亂了', '封包不一定走同一條路\n靠編號排回正確順序',
  '第三案：少了一片', '從編號找出缺了哪一片\n請伺服器重送那一片',
  '網路不保證每個封包都送到；確認與重送是某些傳送規則加上的'],
 ['換你設計：新規則＋家庭網路圖', '先預測，再測試；作品不寫密碼與住址',
  '01', '增加一條自己的規則', '例如：多一個路由站、多一條路線、限時送完',
  '02', '預測、測試、記下證據', '寫進偵探筆記，再決定要不要保留',
  '03', '畫出家庭網路手繪圖', '線索：系統設定 → Wi-Fi → 詳細資訊（IP 位址、路由器）'],
 ['兩小時的網路偵探課', '影片先引路，接下來用接力賽和手繪圖證明你懂了',
  '00–25', '開場十分＋概念十五分', '25–65', '三個案件接力賽', '65–75', '休息十分鐘',
  '75–105', '新規則＋家庭網路圖', '105–115', '孩子教爸爸封包旅程', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：數位公民，分享前先想哪些資訊不該公開'],
 ['最後一關：換你當老師', '暫停影片：不看稿說一次，再指出一個限制或安全注意',
  '01', '完成家庭網路手繪圖', '有裝置、路由器與對外連線；不寫密碼與住址',
  '02', '說出一張圖片的旅程', 'DNS 查位址 → 分成封包 → 路由器轉送 → 重組',
  '03', '指出一個限制或安全注意', '例如：封包可能遺失；密碼不公開',
  '保持好奇，我們下次見！'],
]

# Teaching purpose, on-screen diagram and the hands-on prompt for every scene.
BOARD = [
 ('開場：課前教學版揭露、今日案件與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備紙筆，預告信封、地址卡、路由站與家庭網路圖'),
 ('概念：網際網路是互連的網路；資料以封包一站一站轉送', '三步流程卡：我的裝置 → 路由器 → 伺服器', '邊看邊記下三個角色各做了什麼'),
 ('概念：IP 位址標示來源與目的地；路由器只看目的地決定下一站', '三點條列＋陳犀牛：位址、兩個位址、路由器看目的地', '說出「地址」比喻哪裡不像真實門牌'),
 ('例子：四個角色的職責（裝置、路由器、DNS、伺服器）', '角色卡面板：四張卡，各一句職責', '先口頭說出每個角色的工作，再分配扮演'),
 ('示範：DNS 用名稱查位址；範例名稱與位址是文件保留值', '雙框流程：網域名稱（範例）→ IP 位址（範例）', '指出 DNS 做什麼、不做什麼'),
 ('示範：封包的切開、標記、重組', '三張步驟卡：切開／標記／重組', '回答：沒有編號會發生什麼事'),
 ('活動規則：道具與賽道，比喻對照（信封＝封包等）', '賽道路徑一行＋三張道具對照卡', '暫停影片：排好四個點、放好轉送表'),
 ('共同實作：第一案正常送達（查位址、送要求、分片送回、重組、確認）', '左側三步驟口訣；右側信封標示範例', '暫停影片：六片拼好並回傳確認卡'),
 ('錯誤修正與比較：亂序靠編號排回；遺失靠確認與重送；不是所有規則都重送', '左右比較卡：第二案亂序／第三案遺失', '找證據：到達順序、缺少的編號；決定修正方法'),
 ('獨立改造：自選一條新規則並測試；完成家庭網路手繪圖', '三點條列＋陳犀牛：新規則、預測測試、手繪圖線索', '寫偵探筆記；畫手繪圖，不寫密碼與住址'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：不看稿說出旅程，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子教爸爸；錄音回答四個問題；作品命名存檔'),
]

EYEBROW = '父子科技學院 PACKET RELAY'


def write(name, data):
    p = P / name
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


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
        title='網路到底是什麼：封包接力賽',
        subtitle='父子科技學院 第四堂｜依課表製作的課前教學版',
        seriesHeader='父子科技學院  ·  PACKET RELAY',
        editorialStatus='authored', deckRenderer='ooxml-template',
        contentMode='curriculum-based-preclass', recordingSource=None, autoPublish=False,
        sources={k: v for k, v in SRC.items()},
        factCheck={'checkedAt': CHECKED, 'record': 'production/fact-check.md', 'sources': 'production/sources.json'},
        authorization={
            'produceL004': True,
            'ttsConsent': {'grantedBy': 'user', 'grantedAt': CHECKED, 'service': 'Microsoft Edge TTS',
                           'voice': 'zh-TW-YunJheNeural', 'scope': 'L004 public narration script only',
                           'excluded': 'private recordings or any other private data'},
            'paidLlmApi': False, 'uploadToYouTube': False, 'publish': False})
    write('manifest.json', m)

    lp = R / 'lessons/L004/lesson.json'
    lesson = json.loads(lp.read_text(encoding='utf-8'))
    lesson['episodePaths'] = [E.relative_to(R).as_posix()]
    lesson['status'] = 'preclass-production'
    lp.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Authored {len(SCENES)} scenes / {sum(len(x[1]) for x in SCENES)} sentences; {len(edits)} template mappings')


if __name__ == '__main__':
    main()
