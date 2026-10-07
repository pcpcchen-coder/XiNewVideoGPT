"""Build the L008 classroom pack (real, usable materials; no private data, no real phishing content).

    ./portable-runtime.sh python authoring/l008/classroom.py

All eight message cards are invented; organisations are made up and domains use the reserved
.example TLD. After any change here: rerun pipeline/delivery.py, then verify.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import classroom_pack  # noqa: E402
import printpack  # noqa: E402

FLAGS = ['語氣很急', '假寄件者', '怪網址', '可疑附件', '要錢要密碼']
# (tag, channel, sender line, subject or None, body, link/attachment line or None, verdict, flags found, safe action, note)
CARDS = [
 ('A', '電子郵件', '彩虹學習網 客服　&lt;prize@free-gift.example&gt;', '【緊急】你的帳號將在 24 小時內停用',
  '親愛的用戶：系統發現你的帳號有異常。請立刻點下面的連結，輸入密碼確認身分，否則帳號將永久停用。',
  '連結文字：彩虹學習網登入　→　真正的網址：rainbow.free-gift.example/login',
  '釣魚', ['語氣很急', '假寄件者', '怪網址', '要錢要密碼'],
  '不點、不回。自己打開彩虹學習網的 App 或輸入原本知道的網址查看；告訴爸爸。',
  '名字說是彩虹學習網，地址和連結卻是 free-gift；還催你 24 小時內輸入密碼。「親愛的用戶」沒有叫出名字。'),
 ('B', '簡訊', '+00 開頭的陌生號碼', None,
  '恭喜！你抽中恐龍遊戲 10000 顆寶石！請在今天內點連結，輸入遊戲帳號和密碼領取，逾期作廢。',
  '連結：dino-gift.example/claim',
  '釣魚', ['語氣很急', '假寄件者', '怪網址', '要錢要密碼'],
  '不點、不回，刪除前先告訴爸爸。想知道有沒有活動，自己打開遊戲裡的公告。',
  '沒參加抽獎卻中獎，好到不像真的；陌生號碼、今天內、要帳號密碼。'),
 ('C', '通訊軟體訊息', '顯示名稱：阿哲（新帳號，沒有共同聊天紀錄）', None,
  '是我啦，我換新帳號了。我在買遊戲點數差一點錢，可以先幫我買禮物卡，再把卡片背面的號碼拍給我嗎？很急，晚點還你。',
  None,
  '釣魚', ['語氣很急', '假寄件者', '要錢要密碼'],
  '不買、不拍、不回。用你原本就有的方式（打電話、當面問）找阿哲本人確認；告訴爸爸。',
  '新帳號沒辦法確認是不是本人；很急；要你買禮物卡並給號碼。'),
 ('D', '電子郵件', '星星市立圖書館　&lt;notice@library.star-city.example&gt;', '借閱到期提醒',
  '你借的《恐龍百科》將在 10 月 20 日到期。可以到圖書館櫃台，或自行登入圖書館網站辦理續借。',
  None,
  '看起來正常', [],
  '不必點信裡的任何東西。要續借就自己打開圖書館網站或到櫃台。',
  '名字和地址相符，沒有催促、沒有要密碼、沒有附件。但「看起來正常」不等於一定是真的，所以還是用自己的管道處理。'),
 ('E', '電子郵件', '快遞通知　&lt;delivery@fast-box.example&gt;', '您的包裹無法送達',
  '您好，您的包裹因地址不完整無法送達。請打開附件填寫資料，否則包裹將退回。',
  '附件：領取單.zip',
  '釣魚', ['語氣很急', '可疑附件'],
  '不開附件、不回。問爸爸家裡最近有沒有訂東西；有的話，從購物網站自己查物流。',
  '沒有預期會收到的附件；沒有說是哪一件包裹、寄給誰。'),
 ('F', '簡訊（連續兩則）', '第一則：星星信箱　第二則：陌生號碼', None,
  '第一則：你的星星信箱驗證碼是 418207。第二則：不好意思，我把驗證碼傳錯到你的手機了，可以回傳給我嗎？謝謝！',
  None,
  '釣魚', ['要錢要密碼'],
  '驗證碼不給任何人，不回。告訴爸爸：自己沒有在登入卻收到驗證碼，請他一起檢查帳號。',
  '有人想騙走驗證碼。語氣很客氣、沒有連結，還是釣魚。'),
 ('G', '電子郵件', '彩虹國小 三年二班導師　&lt;class302@rainbow-school.example&gt;', '下週五校外教學通知',
  '各位家長好：下週五校外教學，請在聯絡簿上簽名。回條交給導師即可，不需要回覆這封信。',
  None,
  '看起來正常', [],
  '照聯絡簿處理。有疑問就在學校當面問老師，或用學校原本公布的電話。',
  '名字和地址相符，沒有連結、沒有要資料，還請你用聯絡簿處理。仍然可以用聯絡簿確認。'),
 ('H', '電子郵件', '星星影音 會員中心　&lt;billing@starvideo-member.example&gt;', '付款資料更新通知',
  '您好：您的付款資料已經過期。請於三日內透過下方按鈕更新信用卡資料，以免服務中斷。感謝您的支持。',
  '按鈕文字：更新付款資料　→　真正的網址：starvideo.pay-update.example/login',
  '釣魚', ['語氣很急', '怪網址', '要錢要密碼'],
  '不點。請爸爸自己打開星星影音的 App 或官方網站，看付款資料是不是真的有問題。',
  '沒有錯字、很有禮貌，但用連結要你更新付款資料。網址最後面是 pay-update.example，不是星星影音。'),
]
assert len(CARDS) == 8 and sum(1 for c in CARDS if c[6] == '釣魚') == 6

FILES = {
'00_爸爸先讀.md': '''# 父子科技學院 L008：釣魚郵件偵探社（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在孩子自己檢查訊息卡、圈出紅旗、說出安全動作和理由。

## 這堂課要帶走什麼

- 釣魚訊息：假裝成你認識的公司或朋友，想騙走密碼、個人資料或錢。
- 五面紅旗：語氣很急、假寄件者、怪網址、可疑附件、向你要錢要密碼要驗證碼。
- 安全動作：不點連結、不開附件、不回覆；用自己原本就知道的官方管道查證；告訴爸爸。
- 已經點了或輸入密碼：馬上說，不要怕被罵；改密碼並確認雙重驗證有開。
- 至少一個限制或安全注意：沒有錯字、找不到紅旗的訊息也可能是釣魚。
- 作品：**釣魚訊息紅旗海報**，另有辦案紀錄與自選偵探規則。

## 課前準備（約 20 分鐘）

1. 列印 `02_列印包_釣魚偵探社.pdf`（A4，共 5 頁，單面），把第 2、3 頁的八張訊息卡剪開。
   八張卡的機構、人名、網址**全部是虛構的**，網址結尾用的是保留給範例的 `.example`。
2. 課表寫的是「爸爸準備真假訊息卡」。這八張卡已經夠用；想加入家裡真的收過的例子，請用**截圖列印**，
   先遮掉姓名、電話、帳號和完整網址。不要把真正的釣魚訊息轉寄給孩子，也不要在孩子面前打開裡面的連結。
3. 讀一遍 `04_訊息卡解說.md`，知道每張卡的紅旗和建議的安全動作。
4. 準備一張大一點的紙（A3 或兩張 A4 黏起來）和彩色筆，下半場畫海報；也可以直接用列印包第 5 頁。
5. 先和自己約定：孩子說出「我之前點過奇怪的連結」時，不責備，先謝謝他說出來。
6. 錄音只保存在家裡的私人位置，不直接公開；錄音前先說課次與主題，不要唸出帳號、密碼或住址。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：拿 A 卡問孩子「你會點嗎？為什麼？」 | 聽，不糾正 |
| 10–25 | 看影片、認識五面紅旗和安全動作；讀小抄卡 | 在自己的 Mac 上示範一次「指標停在連結上看網址」（用安全的網頁） |
| 25–65 | 真假訊息卡偵探賽（規則見 `01`） | 當委託人發卡、追問理由、幫忙記錄 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：畫釣魚訊息紅旗海報，加一條自選偵探規則 | 只在孩子開口時協助 |
| 105–115 | 角色互換：孩子教爸爸辨識一張新的訊息卡 | 當學生，故意問「為什麼不能點？」 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 問四個錄音問題，一起決定海報貼哪裡 |

## 幾個觀念的依據與限制

- **釣魚是什麼**：美國聯邦貿易委員會（FTC）的說明是，詐騙者用電子郵件或簡訊，想偷走你的密碼、帳號等資料；附件和連結可能裝進惡意軟體。
- **紅旗**：Apple 的說明列出寄件人與公司名稱不符、連結的網址與公司網站不符、要求提供個人資訊、無故寄來且包含附件。
  Gmail 的說明提醒語氣急迫或許諾好處的郵件要特別留意。英國國家網路安全中心（NCSC）把「限你 24 小時內回應」列為警訊。
- **錯字不再可靠**：NCSC 說，以前的詐騙常有錯字和奇怪的文法，但現在越做越精緻，連專家都可能被騙。所以本課不教「有錯字才是假的」。
- **寄件者可以造假**：Gmail 建議檢查電子郵件地址與寄件者名稱是否相符；Microsoft 的說明提到，寄件地址本身也可能被偽造。
- **看網址**：Apple 寫，在 Mac 上把指標停留在連結上方即可查看 URL；Safari 的狀態列沒顯示時，選「顯示方式」>「顯示狀態列」。
  在 iPhone 或 iPad 上是按住連結。這只能幫你發現「對不上」，**不能證明連結安全**。
- **安全動作**：FTC 的建議是不點可疑訊息裡的連結、不下載附件；覺得可能是真的，就用你確定是真的電話、信箱或網站聯絡對方。
- **正當公司不會這樣要**：Apple 寫，切勿把 Apple 帳號密碼或驗證碼與任何人分享，Apple 絕不會為了提供支援而要求這些資訊。
  FTC 寫，正當公司不會用電子郵件或簡訊附連結要你更新付款資料。但正當公司還是可能寄信給你，所以判斷重點是「它要你做什麼」。

## 遇到真的釣魚訊息時（給爸爸）

1. 不點、不開、不回。需要確認就用自己原本知道的管道。
2. 已經輸入密碼：立刻改掉，用過同一組密碼的其他帳號也要改，並確認雙重驗證有開。
3. 已經打開附件或裝了東西：更新系統與安全軟體，並請熟悉電腦的人協助檢查。
4. 檢舉：
   - 看起來像 Apple 寄來的可疑電子郵件，Apple 請你轉寄到 reportphishing@apple.com。
   - Gmail 電腦版：打開郵件，按「回覆」圖示旁邊的「更多」，再按「回報為網路釣魚郵件」。
   - 台灣：對訊息有詐騙疑慮，可以撥「165」反詐騙專線，或到內政部警政署 165 全民防騙網（https://165.npa.gov.tw/）檢舉。
5. 涉及金錢或信用卡，直接聯絡銀行或發卡機構（用卡片背面或官方網站上的電話）。

## 來源（查核日 2026-10-07）

- FTC「How To Recognize and Avoid Phishing Scams」：https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams
- FTC「Protect yourself from phishing scams」（2025-06-04）：https://consumer.ftc.gov/consumer-alerts/2025/04/protect-yourself-phishing-scams
- FTC「How to Recognize and Report Spam Text Messages」：https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages
- FTC 兒童講義「Filling Your Digital Toolbox」：https://consumer.ftc.gov/system/files/consumer_ftc_gov/pdf/FillingYourDigitalToolbox-508.pdf
- Apple 支援「辨識及防範社交工程詐騙，包括網路釣魚訊息、假的支援電話和其他詐騙」：https://support.apple.com/zh-tw/102568
- Gmail 說明「防範及檢舉網路釣魚電子郵件」：https://support.google.com/mail/answer/8253?hl=zh-Hant
- UK NCSC「How to spot a scam email, text message or call」：https://www.ncsc.gov.uk/collection/phishing-scams/spot-scams
- UK NCSC「If you've shared sensitive information」：https://www.ncsc.gov.uk/collection/phishing-scams/what-to-do
- Microsoft 支援「Outlook 中的網路釣魚和可疑行為」：https://support.microsoft.com/zh-TW/Outlook/mail/phishing-and-suspicious-behavior-in-outlook
- 行政院新聞（民國 112 年 11 月 20 日，165 反詐騙專線與 165 全民防騙網）：https://www.ey.gov.tw/Page/9277F759E41CCD91/752cb47e-7aab-478f-87da-2946b0ce3c5b

165 全民防騙網的網頁內文這次讀不到，以上說法取自行政院的新聞稿；網站上的實際操作請以畫面為準。
課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
''',

'01_活動規則_真假訊息卡偵探賽.md': '''# 真假訊息卡偵探賽：規則

課表的好玩機制是「偵探辦案」。爸爸是**委託人**，孩子是**偵探**。每一張訊息卡是一個案子。

## 準備

- 八張訊息卡（列印包第 2、3 頁，全部虛構），洗牌後蓋著。
- 辦案紀錄表（列印包第 4 頁，或 `03_辦案紀錄.csv`）、筆。
- 五面紅旗小抄卡（列印包第 1 頁）放在旁邊。

## 每一個案子怎麼辦（一張卡約 4 分鐘）

1. **停**：翻開卡片，先讀一遍，什麼都不做。
2. **看**：在卡片上圈出看到的紅旗，並在紀錄表勾選是哪幾面。
3. **判斷**：寫下「釣魚」「看起來正常」或「不確定」。
4. **查**：說出你會做的安全動作，以及理由。
5. 委託人只問兩個問題：「你怎麼知道的？」「那你接下來要做什麼？」

## 計分

- 每找到一面解說裡有的紅旗：1 分。
- 安全動作正確，而且說得出理由：2 分。
- 把釣魚卡判斷成「看起來正常」：這一案 0 分，回頭再看一次。
- 把正常的卡判斷成「不確定」並說出要怎麼確認：一樣給滿分。**小心過頭不扣分。**

八個案子辦完，對照 `04_訊息卡解說.md`。

## 加碼（有時間再玩）

- **反過來出題**：孩子用空白訊息卡自己寫一張釣魚訊息，至少藏三面紅旗，讓爸爸來辦案。
  規則：只能用虛構的名字和 `.example` 結尾的網址。
- **沒有紅旗的陷阱**：再看一次 F 卡。它沒有連結、語氣客氣，為什麼還是釣魚？

## 結算（約 5 分鐘）

- 哪一面紅旗最常出現？哪一張最難？
- 有沒有哪一張，一開始覺得是真的，後來改變想法？
- 孩子說出結論，爸爸只追問「你怎麼知道的？」

## 常見卡關

- 孩子只看有沒有錯字：拿 H 卡，沒有錯字、很有禮貌，還是釣魚。
- 孩子把所有訊息都當成釣魚：拿 D、G 卡，討論「看起來正常時，我怎麼用自己的管道確認」。
- 孩子說「我點一下看看就知道了」：點下去就可能中招。偵探用看的和查的，不用點的。
- 孩子問網址怎麼看：先看有沒有和它說的機構對不上；看不懂就當成不確定，交給爸爸。
''',

'03_辦案紀錄_填寫說明.md': '''# 辦案紀錄怎麼寫

`03_辦案紀錄.csv` 可以用 Numbers 或任何試算表開啟；也可以直接寫在列印包第 4 頁。

每一張訊息卡寫一列：

- **五面紅旗**：語氣很急、假寄件者、怪網址、可疑附件、要錢要密碼。有看到就寫「有」，沒有就留空。
- **我的判斷**：釣魚、看起來正常、不確定。
- **我的安全動作**：例如「不點，自己打開 App 查」「告訴爸爸」「打電話問本人」。
- **理由**：為什麼這樣判斷。
- **得分**：照活動規則計分。

「不確定」是可以接受的判斷，只要後面有寫出要怎麼確認。
紀錄裡不要寫家人真正收到的訊息內容、電話或帳號。
''',

'04_訊息卡解說.md': '''# 訊息卡解說（爸爸用，辦完案再給孩子看）

八張卡全部虛構。「看起來正常」的意思是卡片上找不到紅旗，不代表真實世界裡同樣的訊息一定是真的。

| 卡 | 管道 | 建議判斷 | 紅旗 | 建議的安全動作 | 說明 |
|---|---|---|---|---|---|
''' + ''.join(f"| {c[0]} | {c[1]} | {c[6]} | {'、'.join(c[7]) or '找不到'} | {c[8]} | {c[9]} |\n" for c in CARDS) + '''
孩子找到表上沒有列的疑點，而且說得出道理，也給分。例如 A 卡的「親愛的用戶」沒有叫出名字。

## 可以追問的問題

- A 卡：名字寫「彩虹學習網 客服」，為什麼還不能相信？
- B 卡：沒有參加抽獎卻中獎，你覺得對方想要什麼？
- C 卡：如果真的是阿哲呢？你要怎麼確認又不會被騙？
- D、G 卡：找不到紅旗的時候，最安全的做法是什麼？
- F 卡：對方很有禮貌，也沒有連結，為什麼還是不能給？
- H 卡：它沒有錯字。那我們是靠什麼發現的？
''',

'05_自選規則卡.md': '''# 孩子獨立改造：加一條自己的偵探規則

選一條，或自己發明。一次只加一條，才知道它有沒有用。

## 靈感

- 看到「立刻」「馬上」「24 小時內」，先深呼吸十秒。
- 有人要密碼或驗證碼，一律不給，先找爸爸。
- 連結先看網址，對不上就不點。
- 沒有預期會收到的附件，不打開。
- 朋友用新帳號來借錢或要禮物卡，先打電話問本人。
- 中獎、免費送，先問自己：我有參加嗎？
- 不確定就截圖給爸爸看，不轉傳給同學。

## 我的規則卡

- 規則名稱：＿＿＿＿＿＿＿＿＿＿
- 我的規則（一句話）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 它是在對付哪一面紅旗？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 用兩張訊息卡測試，加規則前得：＿＿ 分　加規則後：＿＿ 分
- 我看到的證據：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 這條規則什麼時候不適用？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 要保留、修改，還是拿掉？為什麼？＿＿＿＿＿＿＿＿＿＿＿＿＿＿

把這條規則也寫到海報上。
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成釣魚訊息紅旗海報（五面紅旗、三個安全動作、一條自己的偵探規則）
- [ ] 不看稿說出五面紅旗：語氣很急、假寄件者、怪網址、可疑附件、要錢要密碼
- [ ] 不看稿說出安全動作：不點、不開、不回；用自己知道的管道查；告訴爸爸
- [ ] 辦案紀錄表八個案子都有判斷、安全動作和理由
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 測試過一條自選偵探規則，並說明要不要保留

## 孩子教爸爸（105–115 分鐘）

請孩子當老師，爸爸當學生。建議順序：

1. 爸爸拿出一張新的訊息卡（自己寫的，或加碼回合孩子出的題）。
2. 孩子帶爸爸做「停、看、查」，爸爸照著回答。
3. 孩子說出這張卡有哪幾面紅旗，爸爸故意問：「可是它看起來很像真的啊？」
4. 孩子示範安全動作，並說出如果已經點了要怎麼辦。
5. 孩子出一題考爸爸，例如：「沒有錯字的訊息，就一定是真的嗎？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

1. 釣魚郵件偵探社，是在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：海報拍照存成 `L008_釣魚訊息紅旗海報_v01`，另存 `L008_辦案紀錄_v01`、`L008_自選規則卡_v01`，
放進 `文件/Tech Academy/L008_釣魚郵件偵探社/`，存好後再打開一次確認。紙本海報貼在全家人都看得到的地方。
''',

'07_五面紅旗小抄.md': '''# L008 五面紅旗小抄

| 紅旗 | 長什麼樣子 | 怎麼檢查 |
|---|---|---|
| 語氣很急 | 「立刻」「24 小時內」「否則停用」；或是好到不像真的 | 越急越要先停下來 |
| 假寄件者 | 顯示的名字和完整的地址對不上 | 把完整的電子郵件地址打開來看 |
| 怪網址 | 連結上寫的字，和真正要去的網址不一樣 | 在 Mac 上把指標停在連結上，先不要按 |
| 可疑附件 | 沒有預期會收到的檔案 | 不打開、不下載 |
| 要錢要密碼 | 要密碼、驗證碼、付款資料、禮物卡 | 一律先不給，找爸爸 |

## 安全動作

1. **不點**連結、**不開**附件、**不回**覆。
2. 想確認真假：自己打開官方 App 或網站，或打原本就知道的電話。
3. 告訴爸爸。檢舉之後再刪除。

## 已經點了怎麼辦

馬上告訴爸爸，不要怕被罵。輸入過密碼就立刻改，並確認雙重驗證有開。

## 三個提醒

- 沒有錯字、看起來很專業，也可能是釣魚。
- 寄件地址看起來對，也可能是偽造的；還要看它要你做什麼。
- 把指標停在連結上只能發現「對不上」，不能證明連結安全。

我最容易忽略的紅旗：＿＿＿＿＿＿　我的偵探規則：＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

SHEET_HEADER = ['訊息卡', '語氣很急', '假寄件者', '怪網址', '可疑附件', '要錢要密碼', '我的判斷', '我的安全動作', '理由', '得分']
SHEET_ROWS = [[c[0]] for c in CARDS] + [['自己出的題'], ['自選規則測試']]

EXTRA_CSS = '''.flag{height:50mm;padding:4mm 5mm}.flag h3{font-size:16pt;margin:0 0 1mm}.flag p{margin:1mm 0;font-size:11.5pt}
.flag .how{font-size:10.5pt;color:#35506b;border-top:.8pt solid #9db7cc;padding-top:1.5mm;margin-top:2mm}
.act{border:1.6pt solid #0b2540;border-radius:3mm;padding:3mm 5mm;margin-top:4mm;font-size:12pt}
.msg{height:119mm;padding:4mm 5mm}.msg h3{font-size:13pt;margin:0}.msg .meta{font-size:10pt;color:#35506b;margin:1.2mm 0 0}
.msg .body{font-size:12pt;margin:2.5mm 0;border:.8pt solid #9db7cc;border-radius:2mm;padding:2.5mm 3mm;background:#f6fafd;min-height:30mm}
.msg .extra{font-size:9pt;margin:0;font-family:"Noto Sans Mono","Menlo",monospace;word-break:break-all}
.msg .pick{font-size:9pt;margin:2mm 0 0;border-top:.8pt solid #9db7cc;padding-top:1.5mm}
.fake{display:inline-block;font-size:9pt;font-weight:400;color:#fff;background:#0b2540;border-radius:1.5mm;padding:.2mm 2mm;margin-left:2mm;vertical-align:middle}
.case{table-layout:fixed}.case th{font-size:9pt;padding:1mm .6mm;text-align:center}.case td{height:14.5mm}.case td.no{text-align:center;font-weight:700}
.blank{height:62mm;padding:3mm 5mm}.blank h3{font-size:12.5pt;margin:0}.blank p{font-size:10pt;margin:1mm 0}
.poster{border:2pt solid #0b2540;border-radius:4mm;padding:5mm 6mm;height:232mm}.poster h3{font-size:20pt;text-align:center;margin:0 0 3mm}
.five{display:grid;grid-template-columns:repeat(5,1fr);gap:2.5mm}.five div{border:1.2pt dashed #7f9bb3;border-radius:3mm;height:62mm;padding:2mm;text-align:center;font-size:11pt;font-weight:700}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;margin-top:4mm}.three div{border:1.2pt solid #35a9d6;border-radius:3mm;height:40mm;padding:2mm 3mm;font-size:11pt;font-weight:700}'''


def html():
    flag = lambda name, look, how: (f'<div class="cut flag"><h3>{name}</h3><p>{look}</p><p class="how">怎麼檢查：{how}</p></div>')
    pages = []
    pages.append('<h2>五面紅旗小抄卡</h2><p class="lead">沿外框剪下，放在電腦旁邊。紅旗越多越可疑；找不到紅旗，不確定時還是要查證。</p><div class="grid2">'
        + flag('一、語氣很急', '「立刻」「24 小時內」「否則停用」，或是好到不像真的。', '越急越要先停下來。')
        + flag('二、假寄件者', '顯示的名字和完整的地址對不上。', '把完整的電子郵件地址打開來看。')
        + flag('三、怪網址', '連結上寫的字，和真正要去的網址不一樣。', '在 Mac 上把指標停在連結上，先不要按。')
        + flag('四、可疑附件', '沒有預期會收到的檔案。', '不打開、不下載。')
        + '</div><div class="cut flag" style="height:auto;margin-top:6mm"><h3>五、要錢要密碼</h3><p>向你要密碼、驗證碼、付款資料，或要你買禮物卡。</p><p class="how">怎麼檢查：一律先不給，找爸爸。</p></div>'
        '<div class="act"><b>安全動作：</b>不點連結、不開附件、不回覆　→　自己打開官方 App 或網站查　→　告訴爸爸，檢舉後再刪除。<br>'
        '<b>已經點了：</b>馬上告訴爸爸，不要怕被罵；輸入過密碼就立刻改。</div>')

    def card(c):
        tag, channel, sender, subject, body, extra = c[:6]
        subj = f'<p class="meta">主旨：{subject}</p>' if subject else ''
        ext = f'<p class="extra">{extra.replace("　→　", "<br>").replace("真正的網址：", "真正的網址：<br>")}</p>' if extra else ''
        sender = sender.replace('　&lt;', '<br>&lt;')
        return (f'<div class="cut msg"><h3>訊息卡 {tag}<span class="fake">虛構</span></h3><p class="meta">管道：{channel}</p>'
                f'<p class="meta">寄件者：{sender}</p>{subj}<p class="body">{body}</p>{ext}'
                '<p class="pick">圈紅旗：語氣・寄件者・網址・附件・要錢要密碼<br>我的判斷：□ 釣魚　□ 看起來正常　□ 不確定</p></div>')
    for part, label in ((CARDS[:4], 'A–D'), (CARDS[4:], 'E–H')):
        pages.append(f'<h2>訊息卡 {label}</h2><p class="lead">機構、人名和網址全部是虛構的，只用來練習。沿外框剪下。</p>'
                     '<div class="grid2" style="gap:4mm">' + ''.join(card(c) for c in part) + '</div>')

    rows = ''.join(f'<tr><td class="no">{c[0]}</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>' for c in CARDS)
    blank = ('<div class="cut blank"><h3>空白訊息卡（自己出題，只能用虛構的名字和 .example 網址）</h3><p>管道：＿＿＿＿＿＿　寄件者：＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
             '<p>內容：</p><div class="line"></div><div class="line"></div><div class="line"></div><p>我藏了哪幾面紅旗：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p></div>')
    pages.append('<h2>辦案紀錄表</h2><p class="lead">每張卡：有看到的紅旗打勾，寫下判斷、安全動作和得分。</p>'
        '<table class="case"><tr><th style="width:6%">卡</th><th>語氣<br>很急</th><th>假寄<br>件者</th><th>怪網址</th><th>可疑<br>附件</th><th>要錢<br>要密碼</th>'
        '<th style="width:15%">我的判斷</th><th style="width:30%">我的安全動作和理由</th><th style="width:7%">得分</th></tr>' + rows + '</table>'
        '<div style="height:5mm"></div>' + blank)

    pages.append('<h2>作品：釣魚訊息紅旗海報</h2><p class="lead">可以直接畫在這一頁，也可以照這個排法畫在大張的紙上。</p>'
        '<div class="poster"><h3>小心！這些是釣魚訊息的紅旗</h3><div class="five">'
        + ''.join(f'<div>{f}<br><span class="note" style="font-weight:400">畫出來</span></div>' for f in FLAGS) + '</div>'
        '<div class="three"><div>安全動作一</div><div>安全動作二</div><div>安全動作三</div></div>'
        '<p style="margin:4mm 0 0;font-size:12pt"><b>不確定的時候：</b></p><div class="line"></div>'
        '<p style="margin:3mm 0 0;font-size:12pt"><b>我的偵探規則：</b></p><div class="line"></div>'
        '<p style="margin:3mm 0 0;font-size:12pt"><b>已經點了怎麼辦：</b></p><div class="line"></div>'
        '<p class="note" style="margin:3mm 0 0">名稱：L008_釣魚訊息紅旗海報_v＿＿　日期：＿＿＿＿　偵探代號：＿＿＿＿</p></div>')
    return printpack.document('L008 釣魚郵件偵探社 列印包', '父子科技學院 L008｜釣魚郵件偵探社', pages, EXTRA_CSS)


if __name__ == '__main__':
    classroom_pack.build(
        slug='l008-phishing-detectives', folder='L008_釣魚郵件偵探社', files=FILES,
        sheet=('03_辦案紀錄.csv', SHEET_HEADER, SHEET_ROWS),
        pack_html=html(), pack_pdf='02_列印包_釣魚偵探社.pdf', pack_pages=5,
        pack_needles=('五面紅旗小抄卡', '訊息卡 A', '訊息卡 H', '虛構', 'free-gift.example', '辦案紀錄表', '釣魚訊息紅旗海報'),
        authoring_dir=Path(__file__).resolve().parent,
        extra={'messageCards': {'count': len(CARDS), 'phishing': 6, 'looksNormal': 2, 'fictional': True,
                                'domains': 'reserved .example only', 'labelledOnEveryCard': True},
               'answersProvided': 'suggested verdict, flags and safe action for the eight invented cards'})
