"""Author L007 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable. Holds only this lesson's text; authoring/lesson_builder.py writes the files.
After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l007/prepare_content.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lesson_builder  # noqa: E402

LESSON, SLUG, TITLE = 'L007', 'l007-password-castle', '密碼城堡與雙重驗證'
CHECKED = '2026-10-07'

SRC = {
    'curriculum': 'curriculum/catalog.json：L007；來源 V2 Excel 逐堂課程第 7 堂',
    'nist_password': 'https://www.nist.gov/cybersecurity-and-privacy/how-do-i-create-good-password',
    'nist_800_63b': 'https://pages.nist.gov/800-63-4/sp800-63b.html',
    'cisa_tipsheet': 'https://www.mass.gov/files/documents/2023/10/06/Secure-Our-World-Passwords-Tip-Sheet.pdf',
    'ftc_passwords': 'https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts',
    'ftc_2fa': 'https://consumer.ftc.gov/articles/use-two-factor-authentication-protect-your-accounts',
    'owasp_stuffing': 'https://community.owasp.org/attacks/Credential_stuffing',
    'apple_passwords_app': 'https://support.apple.com/zh-tw/120758',
    'apple_safari_autofill': 'https://support.apple.com/zh-tw/guide/safari/ibrwf71ba236/mac',
    'apple_2fa': 'https://support.apple.com/zh-tw/102660',
    'apple_security': 'https://support.apple.com/zh-tw/102614',
    'apple_child': 'https://support.apple.com/zh-tw/102617',
    'google_2sv': 'https://support.google.com/accounts/answer/185839?hl=zh-Hant&co=GENIE.Platform%3DDesktop',
    'moda_acs': 'https://moda.gov.tw/ACS/press/news/press/18660',
    'twcert_otp': 'https://www.twcert.org.tw/newepaper/cp-92-8285-1c028-3.html',
    'catalog_reference': 'https://consumer.ftc.gov/identity-theft-and-online-security/online-privacy-and-security',
}

SOURCE_RECORDS = [
    {'id': 'nist_password', 'title': 'How Do I Create a Good Password?', 'publisher': 'NIST（2025-04-28 建立，2025-08-20 更新）', 'url': SRC['nist_password'], 'usedFor': '密碼至少 15 個字元；長度比複雜度更重要；建議使用密碼管理器；多重驗證在密碼外洩時仍有幫助'},
    {'id': 'nist_800_63b', 'title': 'SP 800-63B-4 Digital Identity Guidelines', 'publisher': 'NIST（2025-08-26 版）', 'url': SRC['nist_800_63b'], 'usedFor': '服務提供者不得強制定期更換密碼或強加組成規則；需手動輸入的驗證碼不算防釣魚'},
    {'id': 'cisa_tipsheet', 'title': 'Secure Our World Passwords Tip Sheet', 'publisher': 'CISA（2023-08-14；讀取自 mass.gov 上的 PDF 副本，cisa.gov 無法直接下載）', 'url': SRC['cisa_tipsheet'], 'usedFor': '至少 16 個字元；5 到 7 個不相關的詞組成密語；密碼管理器只需記住一組強密碼'},
    {'id': 'ftc_passwords', 'title': 'Creating Strong Passwords and Other Ways To Protect Your Accounts', 'publisher': 'U.S. Federal Trade Commission（2024-11）', 'url': SRC['ftc_passwords'], 'usedFor': '至少 12 個字元；隨機詞語組成密語；簡訊或電子郵件驗證碼是最弱的雙重驗證；資料外洩時立刻改密碼'},
    {'id': 'ftc_2fa', 'title': 'Use Two-Factor Authentication To Protect Your Accounts', 'publisher': 'U.S. Federal Trade Commission（2022-09）', 'url': SRC['ftc_2fa'], 'usedFor': '就算知道帳號密碼，沒有第二項憑證也登不進去；不要重複使用帳號密碼；不要把驗證碼給主動找上門的人；安全金鑰最強、簡訊碼聊勝於無'},
    {'id': 'owasp_stuffing', 'title': 'Credential stuffing', 'publisher': 'OWASP', 'url': SRC['owasp_stuffing'], 'usedFor': '撞庫：外洩的帳號密碼被拿去大量嘗試其他網站'},
    {'id': 'apple_passwords_app', 'title': '使用「密碼」App 在 Apple 裝置間製作、管理及共享密碼和通行密鑰', 'publisher': 'Apple 支援（台灣）', 'url': SRC['apple_passwords_app'], 'usedFor': '自 macOS Sequoia 起內建「密碼」App，可產生並儲存高強度密碼'},
    {'id': 'apple_safari_autofill', 'title': '在 Mac 上的 Safari 中自動填寫使用者名稱與密碼', 'publisher': 'Apple 支援（台灣）', 'url': SRC['apple_safari_autofill'], 'usedFor': '教材：Safari 會替任何使用這台 Mac 同一使用者帳號的人自動填寫，共用電腦要注意'},
    {'id': 'apple_2fa', 'title': '「Apple 帳號」的雙重認證', 'publisher': 'Apple 支援（台灣，2026-08-13）', 'url': SRC['apple_2fa'], 'usedFor': '即使有人知道密碼，仍然只有你可以存取帳號；六位數驗證碼顯示在受信任裝置'},
    {'id': 'apple_security', 'title': '安全性與「Apple 帳號」', 'publisher': 'Apple 支援（台灣，2024-09-24）', 'url': SRC['apple_security'], 'usedFor': '切勿把密碼、驗證碼提供給任何人；Apple 不會要求提供'},
    {'id': 'apple_child', 'title': '為小孩建立「Apple 帳號」', 'publisher': 'Apple 支援（台灣，2026-09-21）', 'url': SRC['apple_child'], 'usedFor': '教材：未滿 13 歲（依地區而異）的兒童帳號須由家長或監護人建立'},
    {'id': 'google_2sv', 'title': '開啟兩步驟驗證功能', 'publisher': 'Google 帳戶說明', 'url': SRC['google_2sv'], 'usedFor': '教材：兩步驟驗證又稱雙重驗證；請勿把驗證碼提供給任何人'},
    {'id': 'moda_acs', 'title': '強化帳密安全，落實三大防護原則', 'publisher': '數位發展部資通安全署新聞稿（民國 115 年 1 月 12 日）', 'url': SRC['moda_acs'], 'usedFor': '密碼至少 15 個字元；避免生日、電話；常見弱密碼 123456；啟用兩步驟驗證；駭客以外洩帳密撞庫'},
    {'id': 'twcert_otp', 'title': '常見的 OTP 驗證', 'publisher': 'TWCERT/CC（2024-12-04）', 'url': SRC['twcert_otp'], 'usedFor': '切勿隨意將 OTP 提供給他人'},
    {'id': 'catalog_reference', 'title': 'Online Privacy and Security', 'publisher': 'U.S. Federal Trade Commission 消費者網站', 'url': SRC['catalog_reference'], 'usedFor': '課表 R23 主要參考網址；本課引用的是同一網站的密碼與雙重驗證兩篇文章'},
]

# (scene title, three narration sentences, source keys)
SCENES = [
 ('密碼城堡與雙重驗證', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第七堂，密碼城堡與雙重驗證，這是依課表製作的課前教學版，並非實際上課錄音。',
  '把每一個帳號想成一座城堡，密碼就是城門的鑰匙，今天我們要學會怎麼把城堡守好。',
  '我們會用紙牌玩一場攻防戰，最後完成一張家庭帳號安全清單，而且清單上不會寫下任何真正的密碼。'],
  ['curriculum']),
 ('守城堡的三道防線', [
  '守城堡有三道防線。第一道是長密碼，就像又高又厚的城牆，密碼越長，別人越難猜中。',
  '第二道是不重複，每一個帳號都用不同的密碼，這樣一把鑰匙掉了，其他的門還是安全的。',
  '第三道是雙重驗證，就像城門後面的第二道門，就算有人拿到密碼，還要再過一關才進得來。'],
  ['nist_password', 'ftc_2fa', 'apple_2fa']),
 ('長密碼：城牆越高越難爬', [
  '先說長密碼。專家提醒，密碼的長度比花樣更重要，所以最先要做到的事，就是讓它夠長。',
  '一個好方法，是把好幾個彼此沒有關係的詞接在一起，變成一句只有你記得住的長句子，至少要有十五個字元。',
  '不要用生日、名字、電話，也不要用一二三四五六這種大家都想得到的密碼，這些最容易被猜中。'],
  ['nist_password', 'cisa_tipsheet', 'moda_acs']),
 ('密碼城堡的四個零件', [
  '密碼城堡有四個零件：長密碼是城牆，唯一密碼是每一扇門各有一把鑰匙。',
  '密碼管理器是鑰匙保管箱，幫你記住所有的鑰匙；雙重驗證是第二道門，多一層保護。',
  '四個零件各自擋住不同的攻擊，一起用，城堡才真的守得住。'],
  ['curriculum']),
 ('撞庫攻擊：一把鑰匙開很多門？', [
  '為什麼不能重複用同一組密碼？因為網站有時候會發生資料外洩，帳號和密碼就可能流到壞人手上。',
  '壞人會拿這些外洩的帳號密碼，到別的網站一個一個試，這種攻擊叫做撞庫。',
  '如果你每個帳號的密碼都不一樣，就算其中一組外洩，壞人也沒辦法拿它去開別的帳號。'],
  ['owasp_stuffing', 'ftc_2fa', 'moda_acs']),
 ('密碼管理器：鑰匙保管箱', [
  '可是，這麼多又長又不一樣的密碼，誰記得住？這時候就需要密碼管理器，它像一個鑰匙保管箱。',
  '它可以幫你產生又長又難猜的密碼，替每一個帳號各記一組，需要的時候再幫你填進去。',
  '新版的 Mac 就內建一個叫做密碼的 App；要怎麼設定、誰可以打開，請和爸爸一起決定。'],
  ['cisa_tipsheet', 'nist_password', 'apple_passwords_app']),
 ('雙重驗證：第二道門', [
  '再來是雙重驗證。登入的時候，除了密碼，還要通過第二關，例如輸入一組傳到你裝置上的驗證碼。',
  '第二關有好幾種：驗證碼、手機上的驗證 App，或是實體的安全金鑰；不管哪一種，有開都比沒開安全得多。',
  '最重要的規定：驗證碼不可以給任何人，不管對方說他是客服、老師，還是你的朋友，都不行。'],
  ['apple_2fa', 'ftc_2fa', 'ftc_passwords', 'apple_security', 'twcert_otp']),
 ('紙牌攻防：誰守得住城堡？', [
  '現在用紙牌來演一場攻防戰。一個人當守城的人，用詞語牌替三個帳號各組一組密碼；另一個人當攻擊方。',
  '攻擊方會拿到一張外洩名單，上面有其中一個帳號的密碼，他要拿這組密碼，去試另外兩個帳號。',
  '記得，我們只用紙牌和假的帳號來玩，任何時候都不要把真正的密碼說出來或寫下來。'],
  ['curriculum']),
 ('兩回合比一比：差在哪裡？', [
  '第一回合，守城的人三個帳號都用同一組牌，看看一個帳號外洩之後，攻擊方可以打開幾個。',
  '第二回合，每個帳號換成不同的牌，再替最重要的帳號加上第二道門，同樣的攻擊再來一次。',
  '把兩回合被攻破的帳號數量記下來，比一比差在哪裡，然後兩個人交換角色再玩一次。'],
  ['curriculum']),
 ('換你盤點：家庭帳號安全清單', [
  '下半場換你盤點，完成家庭帳號安全清單：先列出家裡常用的帳號，只寫它是哪一種服務，例如信箱或學習平台，不寫密碼。',
  '每個帳號檢查三件事：密碼夠不夠長？有沒有和別的帳號重複？雙重驗證開了沒有？',
  '再加一條你自己的城堡規則，例如申請新帳號之前先問爸爸，或是驗證碼永遠只有自己看。'],
  ['curriculum']),
 ('兩小時的密碼城堡課', [
  '這堂課的兩小時這樣走：開場十分鐘，認識城堡的零件十五分鐘，接著用四十分鐘玩紙牌攻防戰，再休息十分鐘。',
  '休息之後，用三十分鐘完成安全清單和自己的城堡規則，再花十分鐘交換角色，由孩子教爸爸怎麼守城。',
  '最後五分鐘錄音總結，替清單取名字並存檔，再檢查一次，上面沒有任何真正的密碼。'],
  ['curriculum']),
 ('最後一關：教爸爸守城堡', [
  '最後一關，請不看稿，向爸爸說出城堡的四個零件：長密碼、不重複、密碼管理器，還有雙重驗證。',
  '再指出一個限制或安全注意事項，例如開了雙重驗證，還是要小心假的登入網頁，因為驗證碼也可能被騙走。',
  '今天的作品是家庭帳號安全清單，下次我們要成立釣魚郵件偵探社，學會看穿假訊息；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum', 'nist_800_63b']),
]

# Visible text per slide, in the exact order of the L001 template text boxes.
VISIBLE = [
 ['第七堂任務', '密碼城堡\n與雙重驗證', '城牆、鑰匙、第二道門，一起守住帳號', '第七堂  ·  依課表製作的課前教學版'],
 ['守城堡的三道防線', '每一道防線，擋住不同的攻擊',
  '01 長密碼', '又高又厚的城牆\n越長越難猜', '→',
  '02 不重複', '每個帳號一把鑰匙\n掉了一把也不怕', '→',
  '03 第二道門', '雙重驗證\n有密碼還要再過一關',
  '今天的作品：家庭帳號安全清單（不寫真密碼）'],
 ['長密碼：城牆越高越難爬', '長度最重要，再來才是花樣',
  '01', '把好幾個不相關的詞接起來', '變成一句只有你記得住的長句子',
  '02', '至少十五個字元', '各機構的建議從 12 到 16 以上，越長越好',
  '03', '不用生日、名字、電話', '也不用 123456 這類常見密碼'],
 ['密碼城堡的四個零件', '每一個零件，擋住不同的攻擊', '城堡的四個零件',
  '長密碼', '城牆', '唯一密碼', '一門一把鑰匙', '密碼管理器', '鑰匙保管箱', '雙重驗證', '第二道門',
  '四個零件一起用，城堡才守得住'],
 ['撞庫攻擊：一把鑰匙開很多門？', '重複使用密碼，一個外洩就全部危險',
  '一個網站外洩', '帳號和密碼流出去', '→', '撞庫攻擊', '拿去試別的網站',
  '每個帳號都用不同的密碼',
  '這樣一把鑰匙掉了，只有一扇門有危險'],
 ['密碼管理器：鑰匙保管箱', '幫你產生、記住又長又不重複的密碼',
  '01 幫你產生', '又長又難猜的密碼', '02 幫你記住', '每個帳號各一組', '03 你要守好', '打開保管箱的方法',
  '例如新版 Mac 內建的「密碼」App，請和爸爸一起設定'],
 ['雙重驗證：第二道門', '就算密碼被偷，還有一關要過',
  '輸入密碼  →  通過第二關  →  進門',
  '驗證碼', '傳到你的裝置', '驗證 App', '在手機上確認', '安全金鑰', '實體的小鑰匙',
  '驗證碼不給任何人：客服、老師、朋友都不行'],
 ['紙牌攻防：誰守得住城堡？', '一人守城，一人當攻擊方，玩完再交換',
  '一、用詞語牌替三個帳號組密碼\n二、攻擊方拿到一張外洩名單\n三、拿這組密碼去試別的帳號',
  '角色扮演：攻與守', '只用紙牌，不用真密碼', '帳號也是假的\n真密碼不說也不寫',
  '暫停影片：先分好守城的人和攻擊方'],
 ['兩回合比一比：差在哪裡？', '同樣的攻擊，換一種守法再試一次',
  '第一回合：重複密碼', '三個帳號用同一組牌\n一個外洩，能打開幾個？',
  '第二回合：不重複＋第二道門', '每個帳號不同的牌\n最重要的帳號再加一道門',
  '記下每一回合被攻破幾個帳號，再交換角色'],
 ['換你盤點：家庭帳號安全清單', '只寫是哪一種服務和檢查結果，不寫真密碼',
  '01', '列出家裡常用的帳號', '只寫種類，例如：信箱、學習平台、遊戲',
  '02', '每個帳號檢查三件事', '夠長嗎？有重複嗎？雙重驗證開了嗎？',
  '03', '加一條自己的城堡規則', '例如：新帳號先問爸爸、驗證碼只有自己看'],
 ['兩小時的密碼城堡課', '影片先引路，接下來用清單檢查家裡的城堡',
  '00–25', '開場十分＋概念十五分', '25–65', '紙牌密碼攻防戰', '65–75', '休息十分鐘',
  '75–105', '安全清單＋自選規則', '105–115', '孩子教爸爸守城', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：安全，清單上絕對不寫真正的密碼'],
 ['最後一關：教爸爸守城堡', '暫停影片：不看稿示範一次，再指出一個限制或安全注意',
  '01', '完成家庭帳號安全清單', '上面沒有任何真正的密碼',
  '02', '說出城堡的四個零件', '長密碼、不重複、密碼管理器、雙重驗證',
  '03', '指出一個限制或安全注意', '例如：開了雙重驗證，也要小心假網頁',
  '保持好奇，我們下次見！'],
]

BOARD = [
 ('開場：課前教學版揭露、城堡比喻與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備紙牌與紙筆；預告攻防戰與安全清單'),
 ('概念：三道防線（長密碼、不重複、雙重驗證）', '三步流程卡：長密碼 → 不重複 → 第二道門', '說出今天要完成的作品'),
 ('概念：長度優先、用不相關的詞組成長句、避開個人資訊與常見密碼', '三點條列＋陳犀牛', '用詞語牌排出一組夠長的練習密碼'),
 ('概念：長密碼、唯一密碼、密碼管理器、雙重驗證各自的作用', '零件卡面板：四張卡', '說出每個零件像城堡的哪個部分'),
 ('概念：資料外洩與撞庫；每個帳號用不同密碼', '雙框流程：一個網站外洩 → 撞庫攻擊', '說說看為什麼一把鑰匙不能開所有的門'),
 ('概念：密碼管理器產生並記住密碼；Mac 內建「密碼」App；由家長一起設定', '三張步驟卡：幫你產生／幫你記住／你要守好', '和爸爸看一次 Mac 上的「密碼」App（不念出內容）'),
 ('概念：雙重驗證的第二關與種類；驗證碼不給任何人', '路徑一行（輸入密碼→通過第二關→進門）＋三張卡', '練習對索取驗證碼的人說「不行」'),
 ('活動規則：紙牌攻防的角色與安全界線', '左側三步驟；右側角色扮演重點', '暫停影片：分好守城的人和攻擊方'),
 ('共同實作與比較：重複密碼對上不重複加第二道門', '左右比較卡＋黃字說明要記錄並交換角色', '兩回合各記下被攻破的帳號數量'),
 ('獨立改造與安全：家庭帳號安全清單、三項檢查、自選規則', '三點條列＋陳犀牛', '完成清單；自訂一條城堡規則'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：說出四個零件，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子教爸爸；錄音回答四個問題；作品命名存檔'),
]

FACT_CHECK = '''# L007 事實查核

查核日：2026-10-07。查核者：製作代理（Claude）與其派出的研究子代理。
方法：子代理下載各來源的原始頁面或 PDF、抽取文字後回報逐字引文（原文見 `source-notes.md`）；主代理再把引文和旁白、投影片、教材逐句比對。
限制：主代理沒有逐頁重讀來源；cisa.gov 無法直接下載，CISA 的引文來自麻州政府網站上的同一份提示單 PDF；來源多為英文，中文是本課轉述；
165 全民防騙網與教育部沒有找到可用的密碼指引頁面。

## 主張與來源

| # | 本課的說法（幕） | 來源依據 | 結論 |
|---|---|---|---|
| 1 | 密碼的長度比花樣更重要（3） | NIST：“it's more important for the password to be long, so that should be your main priority.” | 相符 |
| 2 | 至少十五個字元（3） | NIST：“at least 15 characters long”；資安署：「密碼長度至少15個字元」；CISA 提示單：16；FTC：12 | 取 NIST 與資安署的 15；投影片註明各機構建議從 12 到 16 以上，沒有說成唯一標準 |
| 3 | 把好幾個不相關的詞接在一起（3） | CISA 提示單：“Create a memorable passphrase of 5-7 unrelated words”；資安署簡報：「運用4到7個無關聯的單字組成」 | 相符；本課沒有指定詞數 |
| 4 | 不用生日、名字、電話，不用 123456（3） | 資安署：「避免使用個人生日、電話等易被猜測資訊」；常見弱密碼「123456」 | 相符；「名字」是本課加的同類例子 |
| 5 | 每個帳號用不同密碼（2、4、5） | FTC：“a reason to never reuse the same username and password” | 相符 |
| 6 | 外洩的帳密會被拿去試別的網站，叫做撞庫（5） | OWASP：外洩的憑證被送到其他網站嘗試；資安署簡報：「駭客購買大量外洩帳密後，採撞庫攻擊登入」 | 相符；沒有引用發生頻率 |
| 7 | 密碼都不一樣時，一組外洩，壞人沒辦法拿它開別的帳號（5） | FTC：撞庫 “works only if you use the same username and password in more than one place” | 相符；只針對撞庫這一種攻擊 |
| 8 | 密碼管理器產生並記住又長又不重複的密碼（4、6） | CISA 提示單：“A password manager creates, stores and fills passwords for us automatically.”；NIST：“highly recommend that you use a password manager” | 相符 |
| 9 | 新版 Mac 內建「密碼」App（6） | Apple：「自 iOS 18、iPadOS 18、macOS Sequoia 和 visionOS 2 起，『密碼』App 能協助管理密碼…可以產生、製作並儲存高強度密碼」 | 相符；「新版」指 macOS Sequoia 起，教材有寫明 |
| 10 | 雙重驗證：就算有人拿到密碼，還要再過一關（2、7） | Apple：「確保即使有人知道你的密碼，仍然只有你可以存取帳號」；FTC：沒有第二項憑證就登不進去 | 相符 |
| 11 | 第二關有驗證碼、驗證 App、安全金鑰等；有開比沒開安全得多（7） | FTC：簡訊或電子郵件驗證碼是最不安全的一種、但 “better than nothing”；安全金鑰最強；NIST：多一項驗證通常讓帳號更安全 | 相符；影片沒有細分強弱，教材有說明 |
| 12 | 驗證碼不可以給任何人（7、10） | Apple：「切勿將…驗證碼…提供給任何人。Apple 絕對不會要求你提供這些資訊。」；Google：「請勿將驗證碼提供給任何人」；TWCERT/CC：「切勿隨意將OTP資訊提供給他人」 | 相符；本課沒有說「所有公司都不會問」 |
| 13 | 開了雙重驗證仍要小心假登入網頁，驗證碼也可能被騙走（12） | NIST SP 800-63B-4：需手動輸入的驗證碼 “SHALL NOT be considered phishing-resistant” | 相符 |
| 14 | 清單不寫真密碼；遊戲只用紙牌與假帳號（1、8、10、11） | 課表：作品「家庭帳號安全清單（不記錄真密碼）」 | 依課表；本課的安全界線 |

## 刻意避免的說法

- 沒有說「每三個月換一次密碼」。NIST 現行指引要求服務提供者不得強制定期更換；教材寫的是「發現外洩或不明登入時立刻換」。
- 沒有說強密碼一定要有符號和數字；教材說明有些網站仍有這類規定，照網站要求即可。
- 沒有把 15 個字元說成唯一的官方標準，也沒有說開了雙重驗證就絕對安全。
- 沒有說簡訊驗證碼沒用；也沒有說驗證 App 不會被釣魚。
- 沒有說 Apple 的「密碼」App 有主密碼；影片只說「打開保管箱的方法要守好」。
- 沒有示範任何真實帳號的登入畫面，也沒有出現任何可用的密碼。

## 課程與素材

- 課程主題、學習目標、120 分鐘流程（10／15／40／10／30／10／5）、動手任務（用紙牌組合密碼強度，模擬撞庫攻擊與 2FA 防守）、
  作品（家庭帳號安全清單，不記錄真密碼）與驗收，依 `curriculum/catalog.json` L007 核對。
- 沒有課堂錄音；本集是**依課表製作的課前教學版**，未虛構逐字稿或父子對話，封面、旁白第一句與說明均已揭露。
- 「城堡、城牆、鑰匙、保管箱、第二道門」是本課原創的教學比喻（課表好玩機制：角色扮演）。
- 教材的三個帳號（星星信箱、恐龍遊戲、彩虹學習網）與詞語牌都是虛構的遊戲道具；沒有做商標或名稱檢索。
- 各家名稱不同：Apple 寫「雙重認證」，Google 與資安署寫「兩步驟驗證」；本課依課表用「雙重驗證」，教材有對照。
- 課表主要參考網址（R23）是 FTC 消費者網站的線上隱私與安全專區；本課引用的是同一網站的密碼與雙重驗證兩篇文章。
- 課表的三組 YouTube 連結是動態搜尋入口；本次沒有挑選、觀看或引用任何影片。
'''

PLAN = '''# L007 密碼城堡與雙重驗證

依課表製作的課前教學版；沒有課堂錄音，不製造逐字稿。
沿用原片頭 v2、陳犀牛、深藍／黃／青、12 頁原生可編輯簡報、36 句旁白、zh-TW-YunJheNeural；
教學段落靜態畫面加 0.55 秒淡化，無背景音樂、無推拉鏡頭。

## 課表核對（curriculum/catalog.json L007）

- 模組：M01 數位探險家；難度 1；主軸：數位素養／AI 素養／網路安全。
- 學習目標：理解長密碼、唯一密碼、密碼管理器與 2FA 的作用。
- 動手任務：用紙牌組合密碼強度，模擬撞庫攻擊與 2FA 防守。好玩機制：角色扮演。
- 作品：家庭帳號安全清單（不記錄真密碼）。生活技能支線：安全。
- 驗收：完成作品；不看稿說出核心原理；指出至少一個錯誤、限制或安全注意事項。

## 120 分鐘（課堂，與影片片長分開）

| 分鐘 | 內容 | 對應影片頁 |
|---|---|---|
| 00–10 | 任務開場：帳號像城堡，問孩子「城堡怎麼守？」 | 1–2 |
| 10–25 | 概念示範：長密碼、唯一密碼、撞庫、密碼管理器、雙重驗證 | 2–7 |
| 25–65 | 共同實作：紙牌密碼攻防（城牆有多高、重複密碼、不重複加第二道門、假客服） | 8–9 |
| 65–75 | 休息 | — |
| 75–105 | 孩子獨立改造：家庭帳號安全清單＋一條自選城堡規則 | 10 |
| 105–115 | 角色互換：孩子教爸爸守城 | 12 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 11–12 |

## 12 頁

1 開場與揭露｜2 三道防線｜3 長密碼｜4 四個零件｜5 撞庫｜6 密碼管理器｜7 雙重驗證｜8 紙牌攻防規則｜
9 兩回合比較｜10 安全清單、三項檢查與自選規則｜11 兩小時安排｜12 驗收與結尾。

## 設計取捨

- 全程不出現、不記錄任何真實密碼：遊戲用詞語牌和虛構帳號，清單只寫服務種類與檢查結果。
- 真的要改家裡帳號的設定，由爸爸課後私下處理，不在錄音或影片裡進行。
- 密碼長度各機構的數字不同（12、15、16），影片取 15 並在畫面註明範圍，教材列出各自的出處。
- 不教「定期換密碼」；改成「發現外洩或不明登入時立刻換」。

## 作品與驗收

- 家庭帳號安全清單（服務種類、誰在用、三項檢查、下一步）；清單上沒有任何真密碼。
- 紙牌攻防紀錄表。
- 自選城堡規則卡一張。
- 孩子教爸爸：不看稿說出四個零件，並指出一個限制或安全注意事項。
- 錄音四問（錄音只留私人區，不念出任何帳號或密碼）。

## 教材

`classroom/L007_密碼城堡與雙重驗證/`：爸爸先讀、紙牌密碼攻防規則、5 頁列印包（城堡四零件小抄卡、詞語牌、帳號卡與攻防道具、
攻防紀錄與安全清單、自選規則與安全提醒）、安全清單（CSV＋說明）、清單寫法與檢查表、自選規則卡、驗收與回顧、四零件小抄。
由 `authoring/l007/classroom.py` 產生；內容與來源查核見 fact-check.md。
'''

SUMMARY = '''這是依課表製作的課前教學版，不是實際上課錄音，也沒有虛構的課堂對話。

帳號就像一座城堡，密碼是城門的鑰匙。陳犀牛帶你認識守城的四個零件：長密碼、每個帳號不重複的密碼、密碼管理器，還有雙重驗證。
看完影片，用紙牌玩一場攻防戰，看看「重複密碼」和「不重複加第二道門」差在哪裡，最後完成一張不寫真密碼的家庭帳號安全清單。

這一集會學到
・密碼的長度比花樣更重要；把好幾個不相關的詞接成一句長句子
・每個帳號用不同的密碼，一組外洩才不會被拿去開別的帳號（撞庫）
・密碼管理器幫你產生並記住密碼；雙重驗證是第二道門
・驗證碼不給任何人；開了雙重驗證也要小心假的登入網頁

教材用法（classroom.zip）
先讀「00_爸爸先讀」，列印「02_列印包」（A4 共 5 頁）並剪下紙牌，照「01_活動規則」玩紙牌密碼攻防；
下半場用「03_家庭帳號安全清單」和「04_清單寫法與檢查表」盤點，完成「05_自選規則卡」，最後用「06_驗收與回顧」讓孩子教爸爸。「07_城堡四零件小抄」可以放在鍵盤旁邊。

注意事項
・課堂是 120 分鐘，影片只是課前引導，片長另計。
・全程不要說出、寫下或拍到任何真正的密碼和驗證碼；遊戲只用紙牌和虛構帳號。
・真的要調整家裡帳號的設定，請爸爸課後私下處理。各家名稱不同：Apple 稱「雙重認證」，Google 稱「兩步驟驗證」。
・密碼長度各機構建議不同（12 到 16 個字元以上），越長越好；有些網站另有規定，照網站要求。

來源（查核日 2026-10-07）
NIST「How Do I Create a Good Password?」：https://www.nist.gov/cybersecurity-and-privacy/how-do-i-create-good-password
CISA「Secure Our World Passwords Tip Sheet」（PDF 副本）：https://www.mass.gov/files/documents/2023/10/06/Secure-Our-World-Passwords-Tip-Sheet.pdf
FTC「Creating Strong Passwords」：https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts
FTC「Use Two-Factor Authentication」：https://consumer.ftc.gov/articles/use-two-factor-authentication-protect-your-accounts
OWASP「Credential stuffing」：https://community.owasp.org/attacks/Credential_stuffing
Apple 支援「密碼」App：https://support.apple.com/zh-tw/120758
Apple 支援「Apple 帳號的雙重認證」：https://support.apple.com/zh-tw/102660
數位發展部資通安全署「強化帳密安全，落實三大防護原則」：https://moda.gov.tw/ACS/press/news/press/18660
'''

if __name__ == '__main__':
    lesson_builder.build(
        lesson=LESSON, slug=SLUG, ordinal='七', title=TITLE, header_en='PASSWORD CASTLE', checked=CHECKED,
        src=SRC, scenes=SCENES, visible=VISIBLE, board=BOARD,
        # Literal spacing on slides; burned captions break after punctuation.
        render_options={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        tts_basis="On 2026-10-07 the user asked to produce L007–L010 'following this process' (the L004–L006 process, which "
                  "sends the public narration script to Edge TTS); stated back to the user before synthesis.",
        source_records=SOURCE_RECORDS,
        source_method='A research subagent downloaded each page/PDF on the check date and reported verbatim quotes '
                      '(production/source-notes.md); the producing agent mapped them to claims. Not a human full read.',
        not_verified=['cisa.gov 網頁無法直接下載；CISA 的引文取自 mass.gov 上的提示單 PDF 副本',
                      '165 全民防騙網、教育部：沒有找到可用的密碼或雙重驗證指引頁面',
                      '台灣兒童建立 Apple 帳號的確切年齡門檻沒有查核'],
        documents={'fact-check.md': FACT_CHECK, 'plan.md': PLAN, 'delivery-summary.md': SUMMARY,
                   'source-notes.md': (Path(__file__).resolve().parent / 'source-notes.md').read_text(encoding='utf-8')},
        readme=lesson_builder.readme(LESSON, TITLE))
