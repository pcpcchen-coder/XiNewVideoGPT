"""Author L009 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable. Holds only this lesson's text; authoring/lesson_builder.py writes the files.
After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l009/prepare_content.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lesson_builder  # noqa: E402

LESSON, SLUG, TITLE = 'L009', 'l009-digital-footprint', '個資、照片與數位足跡'
CHECKED = '2026-10-07'

SRC = {
    'curriculum': 'curriculum/catalog.json：L009；來源 V2 Excel 逐堂課程第 9 堂',
    'pdpa': 'https://laws.gov.taipei/law/LawSearch/LawArticleContent/FL010627',
    'eliteracy_pd': 'https://eliteracy.edu.tw/Download.ashx?id=1489',
    'ftc_coppa': 'https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions',
    'apple_location_meta': 'https://support.apple.com/zh-tw/guide/personal-safety/ips0d7a5df82/web',
    'apple_share_iphone': 'https://support.apple.com/zh-tw/guide/iphone/iphf28f17237/27/ios/27',
    'apple_photos_mac': 'https://support.apple.com/zh-tw/guide/photos/pht5156cc968/mac',
    'thinkuknow_home': 'https://www.thinkuknow.org.au/sites/default/files/2020-10/Home%20learning%20activity%20Learning%20about%20personal%20information%20and%20image%20sharing.pdf',
    'thinkuknow_parent': 'https://www.thinkuknow.org.au/sites/default/files/2023-01/ThinkUKnow%20parental%20advice%20for%20posting%20images.pdf',
    'eliteracy_selfie': 'https://eliteracy.edu.tw/Download.ashx?id=1506',
    'eliteracy_corner': 'https://eliteracy.edu.tw/Download.ashx?id=1782',
    'google_photos_location': 'https://support.google.com/photos/answer/6153599?hl=zh-Hant',
    'google_photos_share': 'https://support.google.com/photos/answer/11190100?hl=zh-Hant',
    'ftc_headsup': 'https://consumer.ftc.gov/articles/heads-up',
    'commonsense_trails': 'https://www.commonsense.org/education/digital-citizenship/lesson/digital-trails',
    'eliteracy_footprint': 'https://eliteracy.edu.tw/Download.ashx?id=1865',
    'eliteracy_consent': 'https://eliteracy.edu.tw/Download.ashx?id=1509',
    'iwin': 'https://i.win.org.tw/about.php',
    'catalog_reference': 'https://consumer.ftc.gov/identity-theft-and-online-security/online-privacy-and-security',
}

SOURCE_RECORDS = [
    {'id': 'pdpa', 'title': '個人資料保護法 第 2 條', 'publisher': '臺北市法規查詢系統（官方鏡像；全國法規資料庫禁止自動擷取，未繞過）', 'url': SRC['pdpa'], 'usedFor': '個人資料的法律定義：姓名、出生年月日、國民身分證統一編號、聯絡方式…及其他得以直接或間接方式識別該個人之資料'},
    {'id': 'eliteracy_pd', 'title': '【個人資料正確用】教案', 'publisher': '教育部 中小學數位素養教育資源網', 'url': SRC['eliteracy_pd'], 'usedFor': '給孩子的說法：只要是可以讓別人知道我們身分的資料，都算是個人資料'},
    {'id': 'ftc_coppa', 'title': 'Complying with COPPA: Frequently Asked Questions', 'publisher': 'U.S. Federal Trade Commission（頁面註明規則已於 2025-04-22 修正）', 'url': SRC['ftc_coppa'], 'usedFor': '教材：美國兒童線上隱私規則把含兒童影像的照片、住址、地理位置列為個人資訊（只作對照，不適用台灣）'},
    {'id': 'apple_location_meta', 'title': '個人安全使用手冊「管理『照片』中的位置後設資料」', 'publisher': 'Apple 支援（台灣，2026 年 9 月）', 'url': SRC['apple_location_meta'], 'usedFor': '相機開啟定位服務時，拍攝位置座標會嵌入照片檔；分享時對方可取得位置；分享時在「選項」關閉「位置」；定位服務設定'},
    {'id': 'apple_share_iphone', 'title': 'iPhone 使用手冊「在 iPhone 上分享照片和影片」', 'publisher': 'Apple 支援（台灣，iOS 27 版）', 'url': SRC['apple_share_iphone'], 'usedFor': '分享照片會同時分享日期與時間、位置等後設資料；iOS 27 版這一頁沒有列出「位置」開關（iOS 18、26 版有）'},
    {'id': 'apple_photos_mac', 'title': 'Mac 上的「照片」設定', 'publisher': 'Apple 支援（台灣）', 'url': SRC['apple_photos_mac'], 'usedFor': '教材：「照片」>「設定」>「一般」的「包含位置資訊」'},
    {'id': 'thinkuknow_home', 'title': 'Home learning activity: Learning about personal information and image sharing（8–12 歲）', 'publisher': 'ThinkUKnow（澳洲聯邦警察主導）', 'url': SRC['thinkuknow_home'], 'usedFor': '制服、學校、家門口的照片都可能含有孩子的個人資訊與位置；範例：制服上的校徽、球上的名字、背景的招牌'},
    {'id': 'thinkuknow_parent', 'title': 'Parental advice for posting images', 'publisher': 'ThinkUKnow', 'url': SRC['thinkuknow_parent'], 'usedFor': '檢查背景的招牌、路牌、門牌；考慮把校徽模糊或用貼圖蓋住'},
    {'id': 'eliteracy_selfie', 'title': '【安全自拍與分享】學習單', 'publisher': '教育部 中小學數位素養教育資源網', 'url': SRC['eliteracy_selfie'], 'usedFor': '上傳前確認照片背景沒有個人資訊（如地址、學校名稱）；分享對象分公開、朋友、僅限自己'},
    {'id': 'eliteracy_corner', 'title': '【躲在角落的眼睛】教案（國小三至四年級）', 'publisher': '教育部 中小學數位素養教育資源網', 'url': SRC['eliteracy_corner'], 'usedFor': '教材：合照、名牌、運動服與行程一起貼出造成個資外洩的例子'},
    {'id': 'google_photos_location', 'title': 'Google 相簿說明（相片位置資訊）', 'publisher': 'Google 相簿說明', 'url': SRC['google_photos_location'], 'usedFor': '即使隱藏位置資訊，其他人仍可能根據相片中的地標猜出拍攝地點'},
    {'id': 'google_photos_share', 'title': 'Google 相簿如何保護你的位置資料', 'publisher': 'Google 相簿說明', 'url': SRC['google_photos_share'], 'usedFor': '教材：Google 相簿分享時預設不加入位置詳細資料（透過親友共享功能除外）'},
    {'id': 'ftc_headsup', 'title': 'Heads Up: Stop. Think. Connect.', 'publisher': 'U.S. Federal Trade Commission（2023-08）', 'url': SRC['ftc_headsup'], 'usedFor': '貼出去就收不回來；刪除後仍可能被存下、分享並留在網路上；看到的人可以截圖；隱私設定不是保證；先得到照片中的人同意'},
    {'id': 'commonsense_trails', 'title': 'Digital Trails', 'publisher': 'Common Sense Education', 'url': SRC['commonsense_trails'], 'usedFor': '數位足跡：你在網路上做的事的紀錄，包括造訪的網站與分享的東西'},
    {'id': 'eliteracy_footprint', 'title': '【無法鎖碼的網路內容】教案', 'publisher': '教育部 中小學數位素養教育資源網', 'url': SRC['eliteracy_footprint'], 'usedFor': '數位足跡是指個人在網路上活動時，留下的各類數據與紀錄'},
    {'id': 'eliteracy_consent', 'title': '【安全自拍，安心上傳】教案', 'publisher': '教育部 中小學數位素養教育資源網', 'url': SRC['eliteracy_consent'], 'usedFor': '將他人的照片或影片上傳到網路之前，必須先徵求對方的同意'},
    {'id': 'iwin', 'title': '關於 iWIN', 'publisher': 'iWIN 網路內容防護機構', 'url': SRC['iwin'], 'usedFor': '教材：台灣的兒少網路內容申訴與諮詢單位'},
    {'id': 'catalog_reference', 'title': 'Online Privacy and Security', 'publisher': 'U.S. Federal Trade Commission 消費者網站', 'url': SRC['catalog_reference'], 'usedFor': '課表 R23 主要參考網址；本課引用的是同一網站的「Heads Up」'},
]

SCENES = [
 ('個資、照片與數位足跡', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第九堂，個資、照片與數位足跡，這是依課表製作的課前教學版，並非實際上課錄音。',
  '一張照片裡，除了你想給大家看的東西，還可能藏著你的名字、學校，甚至你家在哪裡。',
  '今天我們要玩照片尋寶，把藏起來的資訊找出來，最後完成一張家庭發布前檢查表。'],
  ['curriculum']),
 ('發布之前的三個步驟', [
  '發布照片之前有三個步驟。第一步是找，把照片裡藏著的個人資料找出來，包括人、地點和文字。',
  '第二步是想，想一想誰會看到這張照片，還有，它以後會不會一直留在網路上。',
  '第三步是決定：這張照片可以公開、需要先處理，還是不要公開。'],
  ['curriculum', 'eliteracy_selfie']),
 ('個資：能認出你是誰的資料', [
  '什麼是個資？個資就是個人資料，只要能讓別人認出你是誰、找得到你，都算是個人資料。',
  '例如姓名、生日、身分證號碼、電話和住址；你的臉、學校和班級，也能讓人認出你。',
  '有些資料單獨看沒什麼，但是合在一起，例如制服加上校名，再加上放學的時間，別人就知道哪裡找得到你。'],
  ['pdpa', 'eliteracy_pd', 'thinkuknow_home']),
 ('照片尋寶：四種藏起來的資訊', [
  '照片裡常常藏著四種資訊。第一種是人，包括臉、名牌和制服；第二種是地點，例如門牌、路牌和有名的建築。',
  '第三種是文字，像是電腦螢幕、桌上的文件，還有車票和證件。',
  '第四種用眼睛看不到，它存在照片的檔案裡，記錄了拍照的時間和地點。'],
  ['thinkuknow_home', 'thinkuknow_parent', 'eliteracy_selfie', 'google_photos_location', 'apple_location_meta']),
 ('看不見的資訊：位置和時間', [
  '用手機拍照的時候，如果相機開著定位功能，拍攝的位置就可能被存進照片的檔案裡。',
  '把照片分享出去的時候，這些看不見的資訊，可能會跟著照片一起送出去。',
  '分享之前可以先把位置資訊關掉；不同的手機和版本做法不太一樣，請和爸爸一起確認。'],
  ['apple_location_meta', 'apple_share_iphone']),
 ('公開範圍：誰看得到？', [
  '接著想一想公開範圍，也就是誰看得到。公開，代表任何人都可以看到，包括你完全不認識的人。',
  '只給朋友看，或是只留給自己，看得到的人就少很多，所以發布之前，要先確認分享的對象。',
  '不過，設成不公開也不是保證，因為看到的人可以截圖，再傳給別人。'],
  ['eliteracy_selfie', 'ftc_headsup']),
 ('數位足跡：貼出去就收不回來', [
  '你在網路上發布的東西，會留下紀錄，這些紀錄叫做數位足跡。',
  '照片一旦貼出去，就很難收回來，因為別人可能已經存下來，或是轉傳出去了。',
  '就算你之後把它刪掉，它也可能還留在別的地方，所以發布之前要想清楚。'],
  ['commonsense_trails', 'eliteracy_footprint', 'ftc_headsup']),
 ('需要處理：三種整理方法', [
  '有些照片只要整理一下就可以分享。方法有三種：把門牌或名牌裁掉、用貼圖遮住校徽和文字，或是換個背景再拍一張。',
  '還有一件事一定要做：照片裡如果有別人，要先問他同不同意。',
  '只要他說不要，就不發布，這是對朋友和家人的尊重。'],
  ['thinkuknow_parent', 'ftc_headsup', 'eliteracy_consent']),
 ('照片尋寶：三張模擬照片', [
  '現在來玩照片尋寶。教材裡有三張畫出來的模擬照片，每一張都藏著好幾個線索，請把找到的個人資料圈出來。',
  '找完之後替照片分類：可以公開、需要處理，還是不要公開，並且說出你的理由。',
  '如果是需要處理的照片，還要說出你會怎麼處理，是裁掉、遮住，還是再拍一張。'],
  ['curriculum']),
 ('換你設計：家庭發布前檢查表', [
  '下半場換你設計一張家庭發布前檢查表，把要檢查的問題寫下來：人、地點、文字、位置資訊，還有誰看得到。',
  '表上一定要有一格，問過了嗎？照片裡的每一個人都同意，才可以發布。',
  '再加一條你們家自己的規則，例如穿制服的照片不公開，或是出門玩的照片，回到家再發。'],
  ['curriculum']),
 ('兩小時的照片尋寶課', [
  '這堂課的時間這樣分配：開場十分鐘，認識個資和照片裡的資訊十五分鐘，接著四十分鐘玩照片尋寶，再休息十分鐘。',
  '下半場用三十分鐘完成檢查表和家庭規則，然後用十分鐘交換角色，由孩子教爸爸怎麼在發布之前檢查。',
  '最後五分鐘錄音總結，替檢查表取名字並存檔，再貼在家裡大家都看得到的地方。'],
  ['curriculum']),
 ('最後一關：教爸爸發布前檢查', [
  '最後一關，請不看稿，拿一張新的照片，帶著爸爸檢查一次：找出藏著的資訊，再決定怎麼分類。',
  '再指出一個限制或安全注意事項，例如就算設成只給朋友看，照片還是可能被截圖轉傳。',
  '今天的作品是家庭發布前檢查表，下次我們要來認識 AI 是什麼、不是什麼；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum', 'ftc_headsup']),
]

VISIBLE = [
 ['第九堂任務', '個資、照片\n與數位足跡', '發布之前先尋寶，找出照片裡藏的資訊', '第九堂  ·  依課表製作的課前教學版'],
 ['發布之前的三個步驟', '先找、再想、然後決定',
  '01 找', '找出藏著的個資\n人、地點、文字', '→',
  '02 想', '誰會看到？\n以後還在網路上嗎？', '→',
  '03 決定', '可公開、需處理\n還是不公開',
  '今天的作品：家庭發布前檢查表'],
 ['個資：能認出你是誰的資料', '能讓別人認出你、找得到你的，都算',
  '01', '直接認出你', '姓名、生日、身分證號碼、你的臉',
  '02', '找得到你', '住址、電話、學校、班級',
  '03', '合起來更清楚', '制服＋校名＋放學時間，就知道你在哪裡'],
 ['照片尋寶：四種藏起來的資訊', '按下分享之前，先把它們找出來', '照片裡可能藏著',
  '人', '臉、名牌、制服', '地點', '門牌、路牌、地標', '文字', '螢幕、文件、票券', '看不見的', '拍攝時間和位置',
  '第四種用眼睛看不到，它存在照片的檔案裡'],
 ['看不見的資訊：位置和時間', '手機拍照時，可能把拍攝位置存進照片檔',
  '你看到的', '一張公園的照片', '＋', '檔案裡還有', '拍攝時間、拍攝位置',
  '分享照片時，這些資訊可能一起送出去',
  '分享前可以關掉位置；怎麼關，請和爸爸一起確認'],
 ['公開範圍：誰看得到？', '發布之前，先確認分享的對象',
  '01 公開', '任何人都看得到', '02 朋友', '你同意的人才看得到', '03 只有自己', '先存著，不分享',
  '設成不公開也不是保證：看到的人可以截圖轉傳'],
 ['數位足跡：貼出去就收不回來', '你在網路上發布的東西，會留下紀錄',
  '發布  →  被存下、被轉傳  →  刪了也可能還在',
  '可以被截圖', '看到的人都能存', '可以被轉傳', '傳給你不認識的人', '可能留很久', '刪掉也不一定消失',
  '發布前問自己：以後的我，還願意讓大家看到嗎？'],
 ['需要處理：三種整理方法', '有些照片整理一下，就可以分享',
  '一、裁掉：把門牌、名牌裁到畫面外\n二、遮住：用貼圖蓋住校徽和文字\n三、重拍：換個背景再拍一張',
  '還要問一個人', '照片裡的人，同意了嗎？', '只要他說不要\n就不發布',
  '暫停影片：說出三種整理照片的方法'],
 ['照片尋寶：三張模擬照片', '找出藏起來的資訊，再決定怎麼分類',
  '第一步：尋寶', '每張照片都藏著線索\n把找到的個資圈出來',
  '第二步：分類', '可公開、需處理、不公開\n說出理由和處理方法',
  '這三張是畫出來的模擬照片，不是真人的照片'],
 ['換你設計：家庭發布前檢查表', '全家人發布照片之前，都用同一張表',
  '01', '寫下要檢查的問題', '人、地點、文字、位置資訊、誰看得到',
  '02', '加上「問過了嗎？」', '照片裡的每個人都同意，才發布',
  '03', '加一條自己的家庭規則', '例如：穿制服的照片不公開、回到家再發'],
 ['兩小時的照片尋寶課', '影片先引路，接下來用檢查表練習把關',
  '00–25', '開場十分＋概念十五分', '25–65', '三張照片尋寶賽', '65–75', '休息十分鐘',
  '75–105', '檢查表＋家庭規則', '105–115', '孩子教爸爸檢查', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：安全，發布之前先找、先想、再決定'],
 ['最後一關：教爸爸發布前檢查', '暫停影片：不看稿示範一次，再指出一個限制或安全注意',
  '01', '完成家庭發布前檢查表', '全家人都看得懂、用得上',
  '02', '當場檢查一張照片', '找出藏著的資訊，說出怎麼分類',
  '03', '指出一個限制或安全注意', '例如：只給朋友看，也可能被截圖',
  '保持好奇，我們下次見！'],
]

BOARD = [
 ('開場：課前教學版揭露、照片裡藏的資訊、尋寶任務與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備模擬照片與紙筆；預告尋寶與檢查表'),
 ('概念：發布前三步（找、想、決定）', '三步流程卡：找 → 想 → 決定', '說出今天要完成的作品'),
 ('概念：個人資料是能直接或間接認出你的資料；合起來更容易認出', '三點條列＋陳犀牛', '說出三項自己的個資種類（不說出內容）'),
 ('概念：照片裡的四種資訊（人、地點、文字、看不見的）', '資訊卡面板四張＋黃字說明', '先猜哪一種最容易被忽略'),
 ('概念：相機開定位時，位置可能存進照片檔並隨分享送出；分享前可關閉', '雙框對照：你看到的 ＋ 檔案裡還有', '和爸爸一起看一張照片的拍攝資訊'),
 ('概念：公開範圍三種；不公開也可能被截圖轉傳', '三張步驟卡：公開／朋友／只有自己', '說出一張照片適合哪一種範圍'),
 ('概念：數位足跡與永久性', '路徑一行（發布→被存下、被轉傳→刪了也可能還在）＋三張卡', '回答：以後的我還願意讓大家看到嗎'),
 ('示範：裁掉、遮住、重拍三種處理；先徵求照片中的人同意', '左側三種方法；右側「還要問一個人」', '暫停影片：說出三種整理照片的方法'),
 ('活動規則：三張模擬照片尋寶並分類', '左右比較卡（尋寶／分類）＋黃字說明是模擬照片', '逐張圈出線索、分類並說理由'),
 ('獨立改造與安全：家庭發布前檢查表、同意、家庭規則', '三點條列＋陳犀牛', '完成檢查表；自訂一條家庭規則'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：當場檢查一張照片，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子教爸爸；錄音回答四個問題；作品命名存檔'),
]

FACT_CHECK = '''# L009 事實查核

查核日：2026-10-07。查核者：製作代理（Claude）與其派出的研究子代理。
方法：子代理下載各來源的原始頁面或 PDF、抽取文字後回報逐字引文（原文見 `source-notes.md`）；主代理再把引文和旁白、投影片、教材逐句比對。
限制：主代理沒有逐頁重讀來源；全國法規資料庫禁止自動擷取，個資法條文取自臺北市法規查詢系統的官方鏡像；
eSafety 的引文只是擷取工具所得、沒有逐字確認，本課沒有依賴它；通訊軟體與社群網站是否移除照片位置資訊，查不到官方說法。

## 主張與來源

| # | 本課的說法（幕） | 來源依據 | 結論 |
|---|---|---|---|
| 1 | 能讓別人認出你是誰、找得到你的，都算個人資料（3） | 個資法第 2 條：「…及其他得以直接或間接方式識別該個人之資料」；教育部數位素養教案：「只要是可以讓別人知道我們身分的資料，都算是『個人資料』。」 | 相符（簡化）；「找得到你」是本課的白話補充 |
| 2 | 例子：姓名、生日、身分證號碼、電話、住址（3） | 個資法第 2 條明列姓名、出生年月日、國民身分證統一編號、聯絡方式 | 相符；「住址」屬聯絡方式與間接識別，條文沒有逐字列出 |
| 3 | 你的臉、學校和班級也能讓人認出你（3） | 個資法「特徵」「教育」與間接識別；ThinkUKnow：制服、學校的照片含有孩子的個人資訊與位置 | 相符；條文沒有逐字列出「照片」「學校」，教材有說明 |
| 4 | 資料合在一起更容易認出你，例如制服、校名、放學時間（3） | 教育部教案【躲在角落的眼睛】：運動服、合照、名牌與行程一起貼出的例子 | 相符（本課改寫的例子） |
| 5 | 照片裡的人：臉、名牌、制服（4） | ThinkUKnow：校徽、球上寫的名字；教育部學習單：穿校服或制服的清晰個人照列為危險行為 | 相符 |
| 6 | 照片裡的地點：門牌、路牌、有名的建築（4） | ThinkUKnow：“public signs, street signs, house numbers”；Google：可能根據相片中的地標猜出拍攝地點 | 相符 |
| 7 | 照片裡的文字：螢幕、文件、車票、證件（4） | 教育部學習單：背景的地址、學校名稱；其餘沒有找到官方兒童教材 | 螢幕、票券、證件是本課自己舉的例子，不是引用 |
| 8 | 相機開著定位功能時，拍攝位置可能存進照片檔（4、5） | Apple：「已為『相機』App 開啟『定位服務』時…座標會嵌入每個照片和影片檔中」 | 相符；旁白用「如果」「可能」，沒有說每張照片都有 |
| 9 | 分享照片時，位置等資訊可能一起送出去（5） | Apple：「分享照片或影片會同時分享其相關聯的後設資料，例如日期與時間、位置、裝置和說明。」 | 相符 |
| 10 | 分享前可以關掉位置；不同手機與版本做法不同（5） | Apple 個人安全使用手冊（2026 年 9 月）：分享時點「選項」，關閉「位置」。iOS 27 的使用手冊同一主題頁面沒有列出這一項 | 相符；影片沒有說出選單名稱，教材寫明版本差異 |
| 11 | 公開代表任何人都看得到；只給朋友或只留給自己，看得到的人較少（6） | 教育部學習單的分享對象：公開、朋友、僅限自己 | 相符 |
| 12 | 設成不公開也不是保證，看到的人可以截圖再傳（6、12） | FTC：“It's impossible to completely control who sees… even if you use privacy settings”；“Anybody who sees your post can take a screenshot or recording.” | 相符 |
| 13 | 在網路上發布的東西會留下紀錄，叫做數位足跡（7） | 教育部教案：「數位足跡是指個人在網路上活動時，留下的各類數據與紀錄。」；Common Sense：a record of what you do online | 相符 |
| 14 | 貼出去就很難收回來；刪掉也可能還留在別的地方（7） | FTC：“Once you post something online, you can't take it back”；刪除後 “could be saved, shared, and live somewhere online — permanently.” | 相符；旁白用「很難」「可能」 |
| 15 | 處理方法：裁掉門牌名牌、用貼圖遮住校徽和文字、換背景再拍（8） | ThinkUKnow：檢查背景的識別資訊；“consider blurring the school logo or covering with an emoji” | 相符；「裁掉」「再拍」是同一目的的做法，本課補充 |
| 16 | 照片裡有別人要先問他同不同意；他說不要就不發布（8、10） | FTC：“Get someone's OK first… If they say no, don't post it.”；教育部教案：「必須先徵求對方的同意。」 | 相符 |

## 刻意避免的說法

- 沒有說通訊軟體或社群網站會自動移除（或一定保留）照片的位置資訊；查不到官方說法，教材請家長自己在分享前關掉。
- 沒有說每張手機照片都有定位，也沒有說關掉位置別人就一定不知道在哪裡（地標仍可能洩漏）。
- 沒有說設成不公開或只給朋友看就安全，也沒有說刪掉就會消失。
- 沒有說個資法逐字列出照片、住址或學校；也沒有把美國 COPPA 說成適用台灣兒童。
- 影片沒有說出任何手機選單的名稱，避免版本不同造成錯誤；選單寫在教材並註明版本。
- 沒有使用任何真人照片；三張模擬照片是畫出來的圖，人名、校名、門牌、車牌、電話都是虛構的。

## 課程與素材

- 課程主題、學習目標、120 分鐘流程（10／15／40／10／30／10／5）、動手任務（對三張模擬照片做「可公開／不可公開／需處理」分類）、
  作品（家庭發布前檢查表）與驗收，依 `curriculum/catalog.json` L009 核對。
- 沒有課堂錄音；本集是**依課表製作的課前教學版**，未虛構逐字稿或父子對話，封面、旁白第一句與說明均已揭露。
- 「照片尋寶」「找、想、決定」是本課的教學包裝（課表好玩機制：尋寶）。
- 課表主要參考網址（R23）是 FTC 消費者網站的線上隱私與安全專區；本課引用的是同一網站的「Heads Up」。
- 課表的三組 YouTube 連結是動態搜尋入口；本次沒有挑選、觀看或引用任何影片。
'''

PLAN = '''# L009 個資、照片與數位足跡

依課表製作的課前教學版；沒有課堂錄音，不製造逐字稿。
沿用原片頭 v2、陳犀牛、深藍／黃／青、12 頁原生可編輯簡報、36 句旁白、zh-TW-YunJheNeural；
教學段落靜態畫面加 0.55 秒淡化，無背景音樂、無推拉鏡頭。

## 課表核對（curriculum/catalog.json L009）

- 模組：M01 數位探險家；難度 2；主軸：數位素養／AI 素養／網路安全。
- 學習目標：理解個資分類、公開範圍、照片中隱藏資訊與永久性。
- 動手任務：對三張模擬照片做「可公開／不可公開／需處理」分類。好玩機制：尋寶。
- 作品：家庭發布前檢查表。生活技能支線：安全。
- 驗收：完成作品；不看稿說出核心原理；指出至少一個錯誤、限制或安全注意事項。

## 120 分鐘（課堂，與影片片長分開）

| 分鐘 | 內容 | 對應影片頁 |
|---|---|---|
| 00–10 | 任務開場：拿模擬照片一問孩子「這張可以貼出去嗎？為什麼？」 | 1–2 |
| 10–25 | 概念示範：個資、照片裡的四種資訊、位置資訊、公開範圍、數位足跡、處理方法 | 3–8 |
| 25–65 | 共同實作：三張模擬照片尋寶並分類 | 9 |
| 65–75 | 休息 | — |
| 75–105 | 孩子獨立改造：家庭發布前檢查表＋一條自選家庭規則 | 10 |
| 105–115 | 角色互換：孩子帶爸爸檢查一張新的照片 | 12 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 11–12 |

## 12 頁

1 開場與揭露｜2 發布前三步｜3 個資是什麼｜4 照片裡的四種資訊｜5 看不見的位置與時間｜6 公開範圍｜7 數位足跡｜
8 三種處理方法與同意｜9 三張模擬照片尋寶｜10 檢查表與家庭規則｜11 兩小時安排｜12 驗收與結尾。

## 設計取捨

- 三張模擬照片是用向量圖畫出來的，不使用任何真人照片；人名、校名、門牌、車牌、電話都虛構，並逐張標示。
- 三張分別對應「可公開（但要先關位置）」「需處理」「不公開」，但教材說明分類沒有唯一答案，說得出理由比較重要。
- 影片不念出手機選單名稱，因為 Apple 的說明在不同系統版本不一致；選單寫在教材並註明版本。
- 不對通訊軟體是否移除位置資訊下結論；教法是「分享前自己關掉」。

## 作品與驗收

- 家庭發布前檢查表（要檢查的問題、問過了嗎、一條家庭規則）。
- 尋寶紀錄表。
- 自選家庭規則卡一張。
- 孩子教爸爸：不看稿當場檢查一張照片，並指出一個限制或安全注意事項。
- 錄音四問（錄音只留私人區）。

## 教材

`classroom/L009_個資照片與數位足跡/`：爸爸先讀、三張照片尋寶賽規則、5 頁列印包（尋寶小抄卡、三張模擬照片、尋寶紀錄表、
家庭發布前檢查表、處理計畫與自選規則卡）、尋寶紀錄（CSV＋說明）、模擬照片解說、自選規則卡、驗收與回顧、發布前尋寶小抄。
由 `authoring/l009/classroom.py` 產生；內容與來源查核見 fact-check.md。
'''

SUMMARY = '''這是依課表製作的課前教學版，不是實際上課錄音，也沒有虛構的課堂對話。

一張照片裡，除了你想給大家看的東西，還可能藏著名字、學校，甚至家在哪裡。陳犀牛帶你玩照片尋寶：發布之前先找、再想、然後決定。
看完影片，用三張畫出來的模擬照片練習找線索、分類，最後完成全家人都用得上的家庭發布前檢查表。

這一集會學到
・個資是能讓別人認出你、找得到你的資料；合在一起更容易認出你
・照片裡藏著四種資訊：人、地點、文字，還有存在檔案裡、看不見的拍攝時間和位置
・公開範圍：公開、朋友、只有自己；設成不公開也可能被截圖轉傳
・數位足跡：貼出去就很難收回來，刪掉也可能還在；照片裡有別人，要先問他同不同意

教材用法（classroom.zip）
先讀「00_爸爸先讀」，列印「02_列印包」（A4 共 5 頁），照「01_活動規則」玩三張照片尋寶賽，用「03_尋寶紀錄」記錄；
解說在「04_模擬照片解說」，下半場完成家庭發布前檢查表和「05_自選規則卡」，最後用「06_驗收與回顧」讓孩子教爸爸。「07_發布前尋寶小抄」可以貼在電腦旁邊。

注意事項
・課堂是 120 分鐘，影片只是課前引導，片長另計。
・教材的三張模擬照片是畫出來的，人名、校名、門牌、電話都是虛構的；練習時不要拿別人的真實照片來討論。
・怎麼關掉照片的位置資訊，會因手機和系統版本而不同，請爸爸對照自己的裝置；不要假設通訊軟體或社群網站會自動幫你移除。
・分類沒有唯一答案，說得出理由比較重要。

來源（查核日 2026-10-07）
個人資料保護法第 2 條（臺北市法規查詢系統）：https://laws.gov.taipei/law/LawSearch/LawArticleContent/FL010627
教育部 中小學數位素養教育資源網：https://eliteracy.edu.tw/
Apple 個人安全使用手冊「管理『照片』中的位置後設資料」：https://support.apple.com/zh-tw/guide/personal-safety/ips0d7a5df82/web
FTC「Heads Up: Stop. Think. Connect.」：https://consumer.ftc.gov/articles/heads-up
ThinkUKnow「Parental advice for posting images」：https://www.thinkuknow.org.au/sites/default/files/2023-01/ThinkUKnow%20parental%20advice%20for%20posting%20images.pdf
Google 相簿說明（相片位置資訊）：https://support.google.com/photos/answer/6153599?hl=zh-Hant
Common Sense Education「Digital Trails」：https://www.commonsense.org/education/digital-citizenship/lesson/digital-trails
'''

if __name__ == '__main__':
    lesson_builder.build(
        lesson=LESSON, slug=SLUG, ordinal='九', title=TITLE, header_en='PHOTO TREASURE HUNT', checked=CHECKED,
        src=SRC, scenes=SCENES, visible=VISIBLE, board=BOARD,
        render_options={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        tts_basis="On 2026-10-07 the user asked to produce L007–L010 'following this process' (the L004–L006 process, which "
                  "sends the public narration script to Edge TTS); stated back to the user before synthesis.",
        source_records=SOURCE_RECORDS,
        source_method='A research subagent downloaded each page/PDF on the check date and reported verbatim quotes '
                      '(production/source-notes.md); the producing agent mapped them to claims. Not a human full read.',
        not_verified=['全國法規資料庫（law.moj.gov.tw）禁止自動擷取；個資法條文取自臺北市法規查詢系統的官方鏡像',
                      '通訊軟體與社群網站是否移除照片的位置資訊：沒有找到任何官方說法',
                      'Apple 的 iOS 27 使用手冊「分享照片」頁面沒有列出「位置」開關；實機畫面沒有查核',
                      'eSafety Commissioner 的引文未逐字確認，未使用', '教育部 eteacher.edu.tw 無法讀取；改用中小學數位素養教育資源網'],
        documents={'fact-check.md': FACT_CHECK, 'plan.md': PLAN, 'delivery-summary.md': SUMMARY,
                   'source-notes.md': (Path(__file__).resolve().parent / 'source-notes.md').read_text(encoding='utf-8')},
        readme=lesson_builder.readme(LESSON, TITLE))
