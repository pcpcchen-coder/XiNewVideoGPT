"""Author L008 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable. Holds only this lesson's text; authoring/lesson_builder.py writes the files.
After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l008/prepare_content.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lesson_builder  # noqa: E402

LESSON, SLUG, TITLE = 'L008', 'l008-phishing-detectives', '釣魚郵件偵探社'
CHECKED = '2026-10-07'

SRC = {
    'curriculum': 'curriculum/catalog.json：L008；來源 V2 Excel 逐堂課程第 8 堂',
    'ftc_phishing': 'https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams',
    'ftc_alert': 'https://consumer.ftc.gov/consumer-alerts/2025/04/protect-yourself-phishing-scams',
    'ftc_spam_text': 'https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages',
    'ftc_kids': 'https://consumer.ftc.gov/system/files/consumer_ftc_gov/pdf/FillingYourDigitalToolbox-508.pdf',
    'apple_phishing': 'https://support.apple.com/zh-tw/102568',
    'gmail_phishing': 'https://support.google.com/mail/answer/8253?hl=zh-Hant',
    'ncsc_spot': 'https://www.ncsc.gov.uk/collection/phishing-scams/spot-scams',
    'ncsc_shared': 'https://www.ncsc.gov.uk/collection/phishing-scams/what-to-do',
    'ms_outlook': 'https://support.microsoft.com/zh-TW/Outlook/mail/phishing-and-suspicious-behavior-in-outlook',
    'ey_165': 'https://www.ey.gov.tw/Page/9277F759E41CCD91/752cb47e-7aab-478f-87da-2946b0ce3c5b',
    'cisa_phishing': 'https://www.cisa.gov/secure-our-world/recognize-and-report-phishing',
}

SOURCE_RECORDS = [
    {'id': 'ftc_phishing', 'title': 'How To Recognize and Avoid Phishing Scams', 'publisher': 'U.S. Federal Trade Commission（2022-09；課表 R22 主要參考網址）', 'url': SRC['ftc_phishing'], 'usedFor': '釣魚用電子郵件或簡訊騙取密碼、帳號資料；附件與連結可能裝進惡意軟體；通用稱呼；檢舉後刪除；正當公司不會用連結要你更新付款資料'},
    {'id': 'ftc_alert', 'title': 'Protect yourself from phishing scams', 'publisher': 'U.S. Federal Trade Commission 消費者提醒（2025-06-04）', 'url': SRC['ftc_alert'], 'usedFor': '不點可疑訊息裡的連結、不下載附件；用自己確定是真的電話、信箱或網站聯絡'},
    {'id': 'ftc_spam_text', 'title': 'How to Recognize and Report Spam Text Messages', 'publisher': 'U.S. Federal Trade Commission（2022-07）', 'url': SRC['ftc_spam_text'], 'usedFor': '連結可能通往看起來很像真的假網站；正當公司不會用簡訊要帳號資料'},
    {'id': 'ftc_kids', 'title': 'Filling Your Digital Toolbox（Youville 兒童講義）', 'publisher': 'U.S. Federal Trade Commission', 'url': SRC['ftc_kids'], 'usedFor': '不回應比較安全；請爸媽或信任的大人幫忙看訊息'},
    {'id': 'apple_phishing', 'title': '辨識及防範社交工程詐騙，包括網路釣魚訊息、假的支援電話和其他詐騙', 'publisher': 'Apple 支援（台灣，2026-06-22）', 'url': SRC['apple_phishing'], 'usedFor': '寄件人與公司名稱不符、連結 URL 與公司網站不符、要求個人資訊、無故寄來的附件；在 Mac 上把指標停在連結上查看 URL；輸入過密碼就立即更改並確認雙重認證；不分享密碼或驗證碼；不用禮物卡付款給他人'},
    {'id': 'gmail_phishing', 'title': '防範及檢舉網路釣魚電子郵件', 'publisher': 'Gmail 說明（頁面註明可能含 AI 翻譯內容）', 'url': SRC['gmail_phishing'], 'usedFor': '語氣急迫或許諾好處要留意；檢查地址與寄件者名稱是否相符；滑鼠懸停看網址；切勿回應索取私人資訊的要求；在電腦上回報為網路釣魚郵件'},
    {'id': 'ncsc_spot', 'title': 'How to spot a scam email, text message or call', 'publisher': 'UK National Cyber Security Centre（2021-11-26，2022-09-05 檢閱）', 'url': SRC['ncsc_spot'], 'usedFor': '限時回應是警訊；詐騙越來越難分辨，錯字不再可靠；銀行不會用電子郵件要個人資料'},
    {'id': 'ncsc_shared', 'title': "Phishing scams: If you've shared sensitive information", 'publisher': 'UK National Cyber Security Centre', 'url': SRC['ncsc_shared'], 'usedFor': '教材：用同一組密碼的其他帳號也要改'},
    {'id': 'ms_outlook', 'title': 'Outlook 中的網路釣魚和可疑行為', 'publisher': 'Microsoft 支援（中文為機器翻譯，本課只取大意）', 'url': SRC['ms_outlook'], 'usedFor': '寄件者地址可以被偽造；看到的地址可能和真正的寄件地址不同'},
    {'id': 'ey_165', 'title': '催繳水電費用是詐騙老梗 慎防「+號境外開頭簡訊」陷阱', 'publisher': '行政院新聞（民國 112 年 11 月 20 日）', 'url': SRC['ey_165'], 'usedFor': '教材：可撥打 165 反詐騙專線或到 165 全民防騙網檢舉詐騙簡訊；切勿點擊連結，務必查證'},
    {'id': 'cisa_phishing', 'title': 'Recognize and Report Phishing', 'publisher': 'CISA（網頁無法直接下載，引文為擷取工具所得、未逐字確認）', 'url': SRC['cisa_phishing'], 'usedFor': '僅作旁證：AI 讓釣魚信的文法與拼字變得完美；不要回覆'},
]

SCENES = [
 ('釣魚郵件偵探社', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第八堂，釣魚郵件偵探社，這是依課表製作的課前教學版，並非實際上課錄音。',
  '有些訊息會假裝成你認識的公司或朋友，想騙走你的密碼或個人資料，這種手法叫做網路釣魚。',
  '今天我們要成立偵探社，學會找出假訊息的五面紅旗，最後做出一張釣魚訊息紅旗海報。'],
  ['curriculum', 'ftc_phishing']),
 ('偵探三步：停、看、查', [
  '偵探辦案有三個步驟。第一步是停，看到奇怪或很急的訊息，先不要點，也不要回。',
  '第二步是看，仔細找出訊息裡的紅旗，例如語氣、寄件者，還有連結的網址。',
  '第三步是查，不用訊息裡的連結，自己打開官方的 App 或網站確認，拿不定主意就問爸爸。'],
  ['ftc_alert', 'ftc_kids']),
 ('釣魚訊息：假裝成你認識的人', [
  '釣魚訊息可能從電子郵件來，也可能是簡訊、社群貼文，或是通訊軟體裡的訊息。',
  '它想要的東西通常是密碼、驗證碼、帳號資料，或是騙你打開連結和附件，讓電腦裝進壞程式。',
  '它很容易讓人上當，因為看起來很像真的，又常常催你趕快做決定，讓你來不及想。'],
  ['ftc_phishing', 'gmail_phishing', 'ncsc_spot']),
 ('五面紅旗：看到就要小心', [
  '釣魚訊息常見五面紅旗。前四面是：語氣很急、寄件者是假的、網址很奇怪，還有沒預期的附件。',
  '第五面紅旗最重要：它向你要錢、要密碼，或是要驗證碼。',
  '紅旗越多越可疑；不過現在的假訊息做得很像真的，就算找不到紅旗，不確定的時候還是要先查證。'],
  ['apple_phishing', 'gmail_phishing', 'ncsc_spot']),
 ('假寄件者：名字可以造假', [
  '先看寄件者。訊息上顯示的寄件者名字可以造假，所以不能只看名字。',
  '要把完整的電子郵件地址打開來看，如果名字說是學習網的客服，地址卻是完全不相干的網站，這就是紅旗。',
  '還要記得，連地址都有可能被偽造，所以地址看起來沒問題，也要再檢查其他的紅旗。'],
  ['gmail_phishing', 'apple_phishing', 'ms_outlook']),
 ('怪網址：連結要去哪裡？', [
  '再來看網址。連結上面寫的字，和它真正要去的地方，可能不一樣。',
  '在 Mac 上，把指標停在連結上面先不要按，就可以看到真正的網址，再比一比是不是那個官方網站。',
  '如果不一樣，或是你看不懂，就不要點；想去那個網站，請自己輸入你原本就知道的網址。'],
  ['apple_phishing', 'gmail_phishing', 'ftc_spam_text']),
 ('語氣、附件和要求', [
  '假訊息喜歡催你、嚇你，例如說二十四小時內不處理，帳號就會被停用，這種很急的語氣就是紅旗。',
  '沒有預期會收到的附件也是紅旗，不要打開，也不要下載。',
  '只要訊息向你要密碼、驗證碼，或是要你付錢、買禮物卡，就先把它當成釣魚，停下來找爸爸。'],
  ['ncsc_spot', 'apple_phishing', 'ftc_phishing']),
 ('安全動作：不點、不開、不回', [
  '發現可疑的訊息，安全動作有三個：不點連結、不開附件、不回覆。',
  '想確認是不是真的，就自己打開官方的 App 或網站，或是打你原本就知道的電話去問。',
  '如果不小心已經點了，或是輸入了密碼，馬上告訴爸爸，不要怕被罵，再一起把密碼改掉，並確認雙重驗證有開。'],
  ['ftc_alert', 'apple_phishing', 'ftc_kids']),
 ('偵探辦案：真假訊息卡', [
  '現在開始辦案。桌上有八張訊息卡，有的是釣魚，有的不是，請你一張一張檢查，把看到的紅旗圈出來。',
  '每一張卡都要說出你會做的安全動作，還要說出理由，說得出理由才算破案。',
  '遇到沒有紅旗的卡片也不能直接放過，要說出你會用什麼方法，確認它是真的。'],
  ['curriculum']),
 ('換你設計：釣魚訊息紅旗海報', [
  '下半場換你設計一張釣魚訊息紅旗海報，把五面紅旗畫出來：語氣、寄件者、網址、附件，還有要錢要密碼。',
  '海報上還要寫出三個安全動作：不點、不開、不回，最後加上一句，不確定就告訴爸爸。',
  '再加一條你自己的偵探規則，例如看到立刻兩個字，就先深呼吸十秒再說。'],
  ['curriculum']),
 ('兩小時的釣魚偵探課', [
  '兩小時的安排是這樣：開場十分鐘，認識紅旗十五分鐘，接著用四十分鐘辦訊息卡的案子，然後休息十分鐘。',
  '休息過後，用三十分鐘畫紅旗海報、訂偵探規則，再用十分鐘交換角色，讓孩子教爸爸怎麼辨識。',
  '最後五分鐘錄音總結，替海報取名字並存檔，把它貼在全家人都看得到的地方。'],
  ['curriculum']),
 ('最後一關：教爸爸抓釣魚', [
  '最後一關，請不看稿，拿一張新的訊息卡，在爸爸面前辦一次案：圈出紅旗，再說出安全動作。',
  '再指出一個限制或安全注意事項，例如沒有錯字、看起來很專業的訊息，也可能是釣魚。',
  '今天的作品是釣魚訊息紅旗海報，下次我們要認識個資、照片與數位足跡；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum', 'ncsc_spot']),
]

VISIBLE = [
 ['第八堂任務', '釣魚郵件\n偵探社', '找出假訊息的五面紅旗，再做出安全動作', '第八堂  ·  依課表製作的課前教學版'],
 ['偵探三步：停、看、查', '越急的訊息，越要先停下來',
  '01 停', '先不點、不回\n越急越要停', '→',
  '02 看', '找出紅旗\n語氣、寄件者、網址', '→',
  '03 查', '自己打開官方管道\n拿不定主意就問爸爸',
  '今天的作品：一張釣魚訊息紅旗海報'],
 ['釣魚訊息：假裝成你認識的人', '用假訊息騙你交出密碼、個人資料或錢',
  '01', '從哪裡來', '電子郵件、簡訊、社群和通訊軟體的訊息',
  '02', '想要什麼', '密碼、驗證碼、帳號資料，或讓你裝進壞程式',
  '03', '為什麼會上當', '看起來很像真的，又催你趕快決定'],
 ['五面紅旗：看到就要小心', '紅旗越多，越可能是釣魚', '釣魚訊息的紅旗',
  '語氣很急', '催你、嚇你', '假寄件者', '名字地址對不上', '怪網址', '不是官方網站', '可疑附件', '沒預期的檔案',
  '第五面紅旗：向你要錢、要密碼、要驗證碼'],
 ['假寄件者：名字可以造假', '不能只看顯示的名字，要看完整的地址',
  '顯示的名字', '彩虹學習網 客服', '≠', '完整的地址', 'prize@free-gift.example',
  '名字和地址對不上，就是紅旗',
  '地址看起來沒問題，也要再檢查其他紅旗'],
 ['怪網址：連結要去哪裡？', '連結上寫的字，和真正要去的地方可能不一樣',
  '01 先不要按', '把指標停在連結上', '02 看真正的網址', '是那個官方網站嗎？', '03 不一樣就停', '自己輸入知道的網址',
  '在 Mac 上，指標停在連結上就能看到網址'],
 ['語氣、附件和要求', '催你、嚇你、向你要東西，都是紅旗',
  '很急  →  嚇你  →  要你馬上做',
  '語氣很急', '「24 小時內」「立刻」', '可疑附件', '沒預期就不打開', '要錢要密碼', '還有驗證碼、禮物卡',
  '真的很急的事，也可以先停下來查證'],
 ['安全動作：不點、不開、不回', '想確認真假，用你原本就知道的管道',
  '一、不點連結，不開附件，不回覆\n二、自己打開官方 App 或網站查\n三、告訴爸爸，檢舉後再刪除',
  '已經點了怎麼辦？', '馬上告訴爸爸，不要怕被罵', '輸入過密碼就立刻改\n並確認雙重驗證有開',
  '暫停影片：說出三個安全動作'],
 ['偵探辦案：真假訊息卡', '圈出紅旗，再說出安全動作',
  '第一步：圈紅旗', '八張訊息卡，有的是釣魚\n每張圈出看到的紅旗',
  '第二步：說安全動作', '說出你會怎麼做\n說得出理由才算破案',
  '沒有紅旗的卡，也要說出你怎麼確認它是真的'],
 ['換你設計：釣魚訊息紅旗海報', '讓全家人一眼就記得紅旗和安全動作',
  '01', '畫出五面紅旗', '語氣、寄件者、網址、附件、要錢要密碼',
  '02', '寫上三個安全動作', '不點、不開、不回；不確定就告訴爸爸',
  '03', '加一條自己的偵探規則', '例如：看到「立刻」，先深呼吸十秒'],
 ['兩小時的釣魚偵探課', '影片先引路，接下來用訊息卡練習辦案',
  '00–25', '開場十分＋概念十五分', '25–65', '真假訊息卡偵探賽', '65–75', '休息十分鐘',
  '75–105', '紅旗海報＋自選規則', '105–115', '孩子教爸爸辨識', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：安全，不確定的訊息先停下來問'],
 ['最後一關：教爸爸抓釣魚', '暫停影片：不看稿示範一次，再指出一個限制或安全注意',
  '01', '完成釣魚訊息紅旗海報', '五面紅旗和三個安全動作',
  '02', '當場辦一個案子', '拿一張新的訊息卡，圈紅旗、說動作',
  '03', '指出一個限制或安全注意', '例如：沒有錯字，也可能是釣魚',
  '保持好奇，我們下次見！'],
]

BOARD = [
 ('開場：課前教學版揭露、什麼是網路釣魚、偵探任務與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備訊息卡與紙筆；預告五面紅旗與海報'),
 ('概念：偵探三步（停、看、查）', '三步流程卡：停 → 看 → 查', '說出今天要完成的作品'),
 ('概念：釣魚訊息的來源、目的與為什麼有效', '三點條列＋陳犀牛', '說說看自己或家人收過哪些奇怪的訊息（不念出個資）'),
 ('概念：五面紅旗總覽；找不到紅旗也要查證', '紅旗卡面板四張＋黃字第五面紅旗', '先猜哪一面紅旗最常見'),
 ('示範：顯示名稱可以造假，要看完整地址；地址也可能被偽造', '雙框對照：顯示的名字 ≠ 完整的地址（保留網域範例）', '在一張訊息卡上找出寄件者名字和地址'),
 ('示範：連結文字與真正網址可能不同；在 Mac 上停留指標查看', '三張步驟卡：先不要按／看真正的網址／不一樣就停', '在爸爸準備的安全範例上練習把指標停在連結上'),
 ('概念：急迫語氣、可疑附件、索取金錢或密碼', '路徑一行（很急→嚇你→要你馬上做）＋三張紅旗卡', '找出一張訊息卡裡催人的字眼'),
 ('示範：三個安全動作；已經點了要立刻告訴爸爸並改密碼', '左側三步驟；右側「已經點了怎麼辦」', '暫停影片：說出三個安全動作'),
 ('活動規則：八張真假訊息卡，圈紅旗並說出安全動作', '左右比較卡（圈紅旗／說安全動作）＋黃字提醒', '逐張辦案並記錄'),
 ('獨立改造與安全：紅旗海報、三個安全動作、自選偵探規則', '三點條列＋陳犀牛', '完成海報；自訂一條規則並測試'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：當場辦一個案子，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子教爸爸；錄音回答四個問題；作品命名存檔'),
]

FACT_CHECK = '''# L008 事實查核

查核日：2026-10-07。查核者：製作代理（Claude）與其派出的研究子代理。
方法：子代理下載各來源的原始頁面或 PDF、抽取文字後回報逐字引文（原文見 `source-notes.md`）；主代理再把引文和旁白、投影片、教材逐句比對。
限制：主代理沒有逐頁重讀來源；cisa.gov 無法直接下載，CISA 的引文只是擷取工具所得、沒有逐字確認，本課只把它當旁證；
165 全民防騙網是 JavaScript 網站，讀不到內文，165 的說法取自行政院 2023 年的新聞稿；Gmail 與 Microsoft 的中文頁面含機器翻譯，只取大意。

## 主張與來源

| # | 本課的說法（幕） | 來源依據 | 結論 |
|---|---|---|---|
| 1 | 釣魚訊息假裝成公司或朋友，想騙走密碼或個人資料（1、3） | FTC：“Scammers use email or text messages to try to steal your passwords, account numbers…”；Gmail：「網路釣魚是指企圖竊取個人資訊或駭入線上帳戶的行為」 | 相符 |
| 2 | 來源包括電子郵件、簡訊、社群貼文、通訊軟體訊息（3） | NCSC：“via email, text, phone call or via social media”；Gmail：「電子郵件、訊息、廣告」 | 相符；沒有使用未查到出處的術語 |
| 3 | 連結和附件可能讓電腦裝進壞程式（3） | FTC：“Attachments and links might install harmful malware.” | 相符 |
| 4 | 紅旗：語氣很急（4、7） | Gmail：「如果郵件內容的語氣急迫，或是許諾提供有違常理的好處，請特別留意」；NCSC：限時回應，例如 “within 24 hours” | 相符 |
| 5 | 紅旗：寄件者名字與地址對不上（4、5） | Apple：「寄件人的電子郵件或電話與其所聲稱的公司名稱不符。」；Gmail：「檢查電子郵件地址與寄件者名稱是否相符。」 | 相符 |
| 6 | 顯示的寄件者名字可以造假；連地址也可能被偽造（5） | Microsoft：欺騙性郵件有偽造的來源地址，看到的地址可能和真正的寄件地址不同；Gmail：檢查「寄件者」標頭 | 相符（大意）；沒有逐字來源說「誰都可以取任何名字」，旁白用「可以造假」 |
| 7 | 紅旗：連結的真正網址和它說的不一樣（4、6） | Apple：「訊息中的連結看似正確，但 URL 與該公司的網站不符。」 | 相符 |
| 8 | 在 Mac 上把指標停在連結上可以看到真正的網址（6） | Apple：「若要在 Mac 上確認連結導向的網站，請將指標停留在連結上方，即可查看 URL。」Safari 沒顯示時要開「顯示狀態列」 | 相符；教材補上狀態列的說明。沒有說這樣就能證明連結安全 |
| 9 | 紅旗：沒預期的附件（4、7） | Apple：「無故寄來的訊息，且包含附件。」 | 相符 |
| 10 | 紅旗：向你要錢、密碼、驗證碼、禮物卡（4、7） | Apple：「訊息內容要求提供個人資訊，例如信用卡號碼或帳號密碼。」「切勿將你的 Apple 帳號密碼或驗證碼與任何人分享。」「請勿使用 Apple Gift Card 支付款項給其他人。」；FTC：正當公司不會用連結要你更新付款資料 | 相符；「先把它當成釣魚」是本課給孩子的判斷原則 |
| 11 | 假訊息越做越像真的，找不到紅旗也要查證；沒有錯字也可能是釣魚（4、12） | NCSC：“scams are getting smarter and some even fool the experts.” 以前常見的錯字文法不再可靠 | 相符 |
| 12 | 安全動作：不點連結、不開附件（2、8） | FTC：“Don't click links or download attachments in unexpected messages.”；Apple：「切勿點開其中的連結，或是打開或儲存附件。」 | 相符 |
| 13 | 安全動作：不回覆（2、8） | FTC 兒童講義：“it's always safer not to respond.”；Gmail：「切勿回應…索取私人資訊的要求。」 | 相符 |
| 14 | 自己打開官方 App 或網站，或打原本就知道的電話確認（2、6、8） | FTC：“contact the company or bank using a phone number, email, or website you know is real.” | 相符 |
| 15 | 檢舉後再刪除（8，畫面） | FTC：“report the message and then delete it.” | 相符；台灣的檢舉管道寫在教材 |
| 16 | 已經點了或輸入密碼：馬上告訴爸爸，改密碼並確認雙重驗證有開（8） | FTC 兒童講義：請爸媽或信任的大人幫忙；Apple：「請立即更改 Apple 帳號密碼，並確認已啟用雙重認證。」；NCSC：用同一組密碼的帳號都要改 | 相符；改密碼與雙重驗證的說法出自 Apple 與 NCSC，不是 FTC |

## 刻意避免的說法

- 沒有說釣魚訊息一定有錯字，也沒有說寄件地址看起來對就安全。
- 沒有說把指標停在連結上就能證明連結安全；只說網址對不上是紅旗。
- 沒有說正當公司從不寄信或從不附連結。
- 沒有把美國的檢舉管道（7726、ReportFraud.ftc.gov 等）當成台灣的做法；也沒有寫出沒查證過的 165 網站選單名稱。
- 沒有使用任何真實的公司、學校或個人當釣魚例子；範例網域都用保留的 `.example`。

## 課程與素材

- 課程主題、學習目標、120 分鐘流程（10／15／40／10／30／10／5）、動手任務（爸爸準備真假訊息卡，孩子圈出紅旗並說明安全動作）、
  作品（釣魚訊息紅旗海報）與驗收，依 `curriculum/catalog.json` L008 核對。
- 課表列出的辨識重點是急迫語氣、偽造寄件者、奇怪網址、附件與付款要求；本課整理成「五面紅旗」，第五面擴大為要錢、要密碼、要驗證碼。
- 沒有課堂錄音；本集是**依課表製作的課前教學版**，未虛構逐字稿或父子對話，封面、旁白第一句與說明均已揭露。
- 「偵探社」「紅旗」「停、看、查」是本課的教學包裝（課表好玩機制：偵探辦案）。
- 教材的八張訊息卡全部虛構並逐張標示；機構名稱是自創的，網域使用保留的 `.example`，沒有做商標或名稱檢索。
- 課表主要參考網址（R22）是 FTC「How To Recognize and Avoid Phishing Scams」，本課已引用。
- 課表的三組 YouTube 連結是動態搜尋入口；本次沒有挑選、觀看或引用任何影片。
'''

PLAN = '''# L008 釣魚郵件偵探社

依課表製作的課前教學版；沒有課堂錄音，不製造逐字稿。
沿用原片頭 v2、陳犀牛、深藍／黃／青、12 頁原生可編輯簡報、36 句旁白、zh-TW-YunJheNeural；
教學段落靜態畫面加 0.55 秒淡化，無背景音樂、無推拉鏡頭。

## 課表核對（curriculum/catalog.json L008）

- 模組：M01 數位探險家；難度 1；主軸：數位素養／AI 素養／網路安全。
- 學習目標：辨識急迫語氣、偽造寄件者、奇怪網址、附件與付款要求。
- 動手任務：爸爸準備真假訊息卡，孩子圈出紅旗並說明安全動作。好玩機制：偵探辦案。
- 作品：釣魚訊息紅旗海報。生活技能支線：安全。
- 驗收：完成作品；不看稿說出核心原理；指出至少一個錯誤、限制或安全注意事項。

## 120 分鐘（課堂，與影片片長分開）

| 分鐘 | 內容 | 對應影片頁 |
|---|---|---|
| 00–10 | 任務開場：拿一張訊息卡問孩子「你會點嗎？為什麼？」 | 1–2 |
| 10–25 | 概念示範：釣魚是什麼、五面紅旗、寄件者、網址、語氣附件與要求、安全動作 | 3–8 |
| 25–65 | 共同實作：八張真假訊息卡偵探賽 | 9 |
| 65–75 | 休息 | — |
| 75–105 | 孩子獨立改造：釣魚訊息紅旗海報＋一條自選偵探規則 | 10 |
| 105–115 | 角色互換：孩子教爸爸辨識一張新的訊息卡 | 12 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 11–12 |

## 12 頁

1 開場與揭露｜2 偵探三步｜3 釣魚是什麼｜4 五面紅旗｜5 假寄件者｜6 怪網址｜7 語氣、附件和要求｜8 安全動作｜
9 訊息卡偵探賽｜10 紅旗海報與自選規則｜11 兩小時安排｜12 驗收與結尾。

## 設計取捨

- 八張訊息卡全部虛構，網域用保留的 `.example`；不讓孩子接觸真正的釣魚連結。爸爸想加真實例子時，用遮掉個資的截圖列印。
- 八張訊息卡裡有兩張找不到紅旗的卡，練習「看起來正常也要用自己的管道確認」，避免孩子學成只會找紅旗。
- 其中一張釣魚卡沒有任何錯字，對應「沒有錯字也可能是釣魚」。
- 台灣的檢舉管道只寫有官方出處的 165 專線與 165 全民防騙網，不寫沒查證過的操作步驟。

## 作品與驗收

- 釣魚訊息紅旗海報（五面紅旗、三個安全動作、一條自選偵探規則）。
- 辦案紀錄表。
- 自選規則卡一張。
- 孩子教爸爸：不看稿當場辦一個案子，並指出一個限制或安全注意事項。
- 錄音四問（錄音只留私人區）。

## 教材

`classroom/L008_釣魚郵件偵探社/`：爸爸先讀、真假訊息卡偵探賽規則、5 頁列印包（五面紅旗小抄卡、八張虛構訊息卡、辦案紀錄表、海報底稿）、
辦案紀錄（CSV＋說明）、訊息卡解說、自選規則卡、驗收與回顧、五面紅旗小抄。
由 `authoring/l008/classroom.py` 產生；內容與來源查核見 fact-check.md。
'''

SUMMARY = '''這是依課表製作的課前教學版，不是實際上課錄音，也沒有虛構的課堂對話。

有些訊息會假裝成你認識的公司或朋友，想騙走密碼、個人資料或錢。陳犀牛帶你成立釣魚郵件偵探社：先停、再看、然後查，找出假訊息的五面紅旗。
看完影片，用八張真假訊息卡練習辦案，圈出紅旗、說出安全動作，最後畫一張全家都看得到的釣魚訊息紅旗海報。

這一集會學到
・五面紅旗：語氣很急、假寄件者、怪網址、可疑附件，還有向你要錢、要密碼、要驗證碼
・顯示的寄件者名字可以造假，要看完整的地址；在 Mac 上把指標停在連結上可以看到真正的網址
・安全動作：不點連結、不開附件、不回覆；用你原本就知道的官方管道查證
・已經點了或輸入密碼，馬上告訴爸爸，改密碼並確認雙重驗證有開

教材用法（classroom.zip）
先讀「00_爸爸先讀」，列印「02_列印包」（A4 共 5 頁）並剪下訊息卡，照「01_活動規則」玩真假訊息卡偵探賽，用「03_辦案紀錄」記錄；
解說在「04_訊息卡解說」，下半場畫海報並完成「05_自選規則卡」，最後用「06_驗收與回顧」讓孩子教爸爸。「07_五面紅旗小抄」可以貼在電腦旁邊。

注意事項
・課堂是 120 分鐘，影片只是課前引導，片長另計。
・教材裡的八張訊息卡全部是虛構的；不要拿真正的釣魚連結給孩子練習。
・現在的假訊息可以做得很像真的，沒有錯字、找不到紅旗也不代表安全，不確定就先查證。
・在台灣遇到可疑訊息，可以撥 165 反詐騙專線查證或檢舉。

來源（查核日 2026-10-07）
FTC「How To Recognize and Avoid Phishing Scams」：https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams
FTC「Protect yourself from phishing scams」：https://consumer.ftc.gov/consumer-alerts/2025/04/protect-yourself-phishing-scams
Apple 支援「辨識及防範社交工程詐騙」：https://support.apple.com/zh-tw/102568
Gmail 說明「防範及檢舉網路釣魚電子郵件」：https://support.google.com/mail/answer/8253?hl=zh-Hant
UK NCSC「How to spot a scam email, text message or call」：https://www.ncsc.gov.uk/collection/phishing-scams/spot-scams
Microsoft 支援「Outlook 中的網路釣魚和可疑行為」：https://support.microsoft.com/zh-TW/Outlook/mail/phishing-and-suspicious-behavior-in-outlook
行政院新聞（165 反詐騙專線）：https://www.ey.gov.tw/Page/9277F759E41CCD91/752cb47e-7aab-478f-87da-2946b0ce3c5b
'''

if __name__ == '__main__':
    lesson_builder.build(
        lesson=LESSON, slug=SLUG, ordinal='八', title=TITLE, header_en='PHISHING DETECTIVES', checked=CHECKED,
        src=SRC, scenes=SCENES, visible=VISIBLE, board=BOARD,
        render_options={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        tts_basis="On 2026-10-07 the user asked to produce L007–L010 'following this process' (the L004–L006 process, which "
                  "sends the public narration script to Edge TTS); stated back to the user before synthesis.",
        source_records=SOURCE_RECORDS,
        source_method='A research subagent downloaded each page/PDF on the check date and reported verbatim quotes '
                      '(production/source-notes.md); the producing agent mapped them to claims. Not a human full read.',
        not_verified=['cisa.gov 網頁無法直接下載；CISA 的引文未逐字確認，只作旁證',
                      '165 全民防騙網（165.npa.gov.tw）是 JavaScript 網站，讀不到內文；165 的說法取自行政院 2023 年新聞稿',
                      'TWCERT/CC、數位發展部、教育部：沒有找到適合一般民眾或兒童的釣魚辨識頁面',
                      'Gmail 的檢舉步驟只查到電腦版；手機版沒有查核'],
        documents={'fact-check.md': FACT_CHECK, 'plan.md': PLAN, 'delivery-summary.md': SUMMARY,
                   'source-notes.md': (Path(__file__).resolve().parent / 'source-notes.md').read_text(encoding='utf-8')},
        readme=lesson_builder.readme(LESSON, TITLE))
