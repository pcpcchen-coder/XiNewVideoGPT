"""Build the L007 classroom pack (real, usable materials; no private data, no real passwords).

    ./portable-runtime.sh python authoring/l007/classroom.py

Accounts, word cards and codes are invented game props. After any change here:
rerun pipeline/delivery.py, then verify (classroom is fingerprinted).
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import classroom_pack  # noqa: E402
import printpack  # noqa: E402

WORDS = ['鯨魚', '雨傘', '火山', '餅乾', '望遠鏡', '腳踏車', '月亮', '積木', '仙人掌', '火車', '圖書館', '雪人',
         '鋼琴', '蝸牛', '紙飛機', '燈塔', '西瓜', '機器人', '彩虹', '襪子', '恐龍', '湯匙', '熱氣球', '鬧鐘']
ACCOUNTS = [('星星信箱', '收信、寄信'), ('恐龍遊戲', '玩遊戲、存進度'), ('彩虹學習網', '交作業、看成績')]
CODES = ['418 207', '936 152', '705 843']
assert len(WORDS) == 24 and len(set(WORDS)) == 24

FILES = {
'00_爸爸先讀.md': '''# 父子科技學院 L007：密碼城堡與雙重驗證（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在孩子自己用紙牌守城、被攻破、再換一種守法，並盤點家裡的帳號。

## 最重要的一條界線

**整堂課不說出、不寫下、不拍到任何真正的密碼或驗證碼。**
遊戲只用詞語牌和虛構帳號；作品「家庭帳號安全清單」只寫服務種類和檢查結果。
真的要調整家裡帳號的設定，請你課後私下處理，不要在錄音或孩子的螢幕錄影裡進行。

## 這堂課要帶走什麼

- 長密碼：長度比花樣更重要；把好幾個不相關的詞接成一句長句子。
- 唯一密碼：每個帳號用不同的密碼，一組外洩才不會被拿去開別的帳號（撞庫）。
- 密碼管理器：幫你產生並記住又長又不重複的密碼。
- 雙重驗證：登入時的第二關；就算密碼被偷，還要再過一關。
- 至少一個限制或安全注意：驗證碼不給任何人；開了雙重驗證也要小心假的登入網頁。
- 作品：**家庭帳號安全清單（不記錄真密碼）**，另有攻防紀錄與自選城堡規則。

## 課前準備（約 20 分鐘）

1. 列印 `02_列印包_密碼城堡.pdf`（A4，共 5 頁，單面）。第 2、3 頁沿線剪開，會得到 24 張詞語牌、3 張帳號卡、
   2 張第二道門卡、3 張驗證碼牌和 1 張外洩名單。沒有印表機可以用便條紙手寫。
2. 讀一遍 `01_活動規則_紙牌密碼攻防.md`，先和自己玩一輪。
3. 自己先想好家裡有哪些帳號要放進清單（只想種類，例如信箱、學習平台、遊戲、影音）。**不要把帳號名稱或密碼寫在任何紙上。**
4. 讀 `04_爸爸課後設定指引.md`，知道課後可以做哪些事。
5. 錄音只保存在家裡的私人位置，不直接公開；錄音前先說課次與主題，不要唸出帳號、密碼、驗證碼或住址。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：帳號像城堡。問孩子「如果你是壞人，會怎麼猜別人的密碼？」 | 聽，不糾正 |
| 10–25 | 看影片、認識四個零件；讀小抄卡 | 用詞語牌示範一組「長句子」密碼 |
| 25–65 | 紙牌密碼攻防（規則見 `01`） | 當攻擊方，再交換；幫忙記錄 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：完成家庭帳號安全清單，加一條自選城堡規則 | 回答「我們家有哪些種類的帳號」，不說出帳號和密碼 |
| 105–115 | 角色互換：孩子教爸爸守城 | 當學生，照孩子說的做，聽不懂就發問 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 問四個錄音問題，協助存檔，檢查清單上沒有真密碼 |

## 幾個觀念的依據與限制

- **長度優先**：美國國家標準暨技術研究院（NIST）的說明寫，密碼至少 15 個字元，而且長度比加上各種符號更重要。
- **數字不只一個**：NIST 與我國數位發展部資通安全署寫 15，美國 CISA 的提示單寫 16，美國聯邦貿易委員會（FTC）寫 12。
  影片取 15，並在畫面註明「各機構的建議從 12 到 16 以上，越長越好」。有些網站另有規定（例如一定要有數字或大小寫），照網站要求。
- **不相關的詞**：CISA 建議用 5 到 7 個不相關的詞組成好記的密語；資安署的簡報寫 4 到 7 個。
- **撞庫**：OWASP 的說明是，很多人重複使用同一組帳號密碼，一旦外洩，攻擊者把它送到其他網站嘗試，就能拿下那些帳號。
- **密碼管理器**：CISA 與 NIST 都建議使用。自 macOS Sequoia 起，Mac 內建「密碼」App，可以產生並儲存高強度密碼。
- **雙重驗證的名稱**：Apple 稱「雙重認證」，Google 與資安署稱「兩步驟驗證」，課表用「雙重驗證」，指的是同一類做法。
- **第二關有強有弱**：FTC 說簡訊或電子郵件收到的驗證碼是最弱的一種，但有總比沒有好；實體安全金鑰最強。
  NIST 的技術指引寫，需要手動輸入的驗證碼不算「防釣魚」，所以開了雙重驗證仍要小心假網頁。
- **不用定期換**：NIST 現行指引要求服務提供者不得強制定期更換密碼；該換的時機是發現外洩或不明登入。本課因此不教「每幾個月換一次」。

## 安全（請一定和孩子聊）

1. 驗證碼不給任何人。Apple 的說明寫：切勿把密碼、驗證碼提供給任何人，Apple 絕對不會要求你提供。
2. 有人用電話、訊息或遊戲私訊要密碼或驗證碼，不管他說他是誰，先停下來找爸爸。
3. 申請新帳號之前先問爸爸。Apple 規定未滿 13 歲（年齡依國家或地區而異）的兒童帳號，必須由家長或監護人建立。
4. 共用的電腦要注意：Apple 的說明寫，Safari 會替任何使用這台 Mac 同一個使用者帳號的人自動填寫密碼。
   讓孩子用自己的 Mac 使用者帳號，離開座位時鎖定螢幕。
5. 練習用的詞語牌組合不要拿來當真正的密碼；印出來的東西等於已經公開。

## 來源（查核日 2026-10-07）

- NIST「How Do I Create a Good Password?」：https://www.nist.gov/cybersecurity-and-privacy/how-do-i-create-good-password
- NIST SP 800-63B-4：https://pages.nist.gov/800-63-4/sp800-63b.html
- CISA「Secure Our World Passwords Tip Sheet」（麻州政府網站上的 PDF 副本）：https://www.mass.gov/files/documents/2023/10/06/Secure-Our-World-Passwords-Tip-Sheet.pdf
- FTC「Creating Strong Passwords and Other Ways To Protect Your Accounts」：https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts
- FTC「Use Two-Factor Authentication To Protect Your Accounts」：https://consumer.ftc.gov/articles/use-two-factor-authentication-protect-your-accounts
- OWASP「Credential stuffing」：https://community.owasp.org/attacks/Credential_stuffing
- Apple 支援「使用『密碼』App…」：https://support.apple.com/zh-tw/120758
- Apple 支援「在 Mac 上的 Safari 中自動填寫使用者名稱與密碼」：https://support.apple.com/zh-tw/guide/safari/ibrwf71ba236/mac
- Apple 支援「『Apple 帳號』的雙重認證」：https://support.apple.com/zh-tw/102660
- Apple 支援「安全性與『Apple 帳號』」：https://support.apple.com/zh-tw/102614
- Apple 支援「為小孩建立『Apple 帳號』」：https://support.apple.com/zh-tw/102617
- Google 帳戶說明「開啟兩步驟驗證功能」：https://support.google.com/accounts/answer/185839?hl=zh-Hant
- 數位發展部資通安全署「強化帳密安全，落實三大防護原則」：https://moda.gov.tw/ACS/press/news/press/18660
- TWCERT/CC「常見的 OTP 驗證」：https://www.twcert.org.tw/newepaper/cp-92-8285-1c028-3.html

課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
''',

'01_活動規則_紙牌密碼攻防.md': '''# 紙牌密碼攻防：規則

課表的好玩機制是「角色扮演」：一個人當**守城的人**，一個人當**攻擊方**，玩完交換。
全部用紙牌和虛構帳號。**不使用、不說出任何真正的密碼。**

## 道具（列印包第 2、3 頁剪開）

- 詞語牌 24 張：每張一個詞，彼此沒有關係。
- 帳號卡 3 張（虛構）：星星信箱、恐龍遊戲、彩虹學習網。
- 第二道門卡 2 張、驗證碼牌 3 張（上面的數字是假的）。
- 外洩名單 1 張、攻防紀錄表（列印包第 4 頁）。

## 暖身：城牆有多高（約 8 分鐘）

1. 守城的人從 24 張詞語牌裡偷偷選 **1 張**當密碼，攻擊方最多猜 10 次。猜中了嗎？
2. 改成選 **2 張**（有順序）。攻擊方還是只能猜 10 次。
3. 一起算：密碼變長，攻擊方最多要猜幾次才一定猜得到？把答案寫在紀錄表。

| 幾張牌 | 最多要猜幾次 | 算法 |
|---|---|---|
| 1 張 | 24 | 24 |
| 2 張 | 552 | 24 × 23 |
| 3 張 | 12,144 | 24 × 23 × 22 |
| 4 張 | 255,024 | 24 × 23 × 22 × 21 |

多一張牌，城牆就高很多。真正的密碼不是從 24 個詞裡選，可以選的更多，所以長度更有用。

## 第一回合：重複密碼（約 10 分鐘）

1. 守城的人選 3 張詞語牌排成一組密碼，寫在自己的小紙條上蓋好。**三個帳號都用這一組。**
2. 丟骰子或抽籤，決定哪一個帳號「資料外洩」。守城的人把那個帳號的密碼抄到外洩名單，交給攻擊方。
3. 攻擊方拿這組密碼去試另外兩個帳號。守城的人照實回答「開了」或「沒開」。
4. 記下被攻破幾個帳號。

## 第二回合：不重複＋第二道門（約 12 分鐘）

1. 守城的人替三個帳號各排一組**不同的**密碼。
2. 選一個最重要的帳號，放上第二道門卡，旁邊蓋一張驗證碼牌（只有守城的人看得到）。
3. 再抽一次外洩的帳號，攻擊方拿到那一組密碼，去試另外兩個帳號。
4. 就算攻擊方手上的密碼剛好能開有第二道門的帳號，守城的人要說：「請輸入驗證碼。」攻擊方沒有，就進不去。
5. 記下被攻破幾個帳號，和第一回合比。

## 加碼回合：假客服（約 5 分鐘）

攻擊方扮演假客服，用各種理由向守城的人要驗證碼，例如：「你的帳號有問題，請把剛收到的六位數告訴我。」
守城的人練習說：「驗證碼不給任何人。」然後告訴爸爸。
如果守城的人把驗證碼念出來，第二道門就被打開了——這就是開了雙重驗證還是要小心的原因。

## 交換角色、結算（約 5 分鐘）

- 兩個人交換角色，再玩第一、第二回合。
- 哪一種守法被攻破最少？差在哪一個零件？
- 孩子說出結論，爸爸只追問「你怎麼知道的？」

## 常見卡關

- 孩子想用自己真正的密碼來玩：立刻停，換成詞語牌。
- 孩子覺得只要夠長就可以重複用：再玩一次第一回合，密碼再長，外洩了也一樣被打開。
- 孩子問「那我怎麼記得住這麼多組」：這就是密碼管理器要解決的問題，回到影片第 6 頁。
''',

'03_家庭帳號安全清單_填寫說明.md': '''# 家庭帳號安全清單怎麼寫

`03_家庭帳號安全清單.csv` 可以用 Numbers 或任何試算表開啟；也可以直接寫在列印包第 5 頁。

## 絕對不寫

- 不寫密碼，也不寫密碼的提示、開頭或長度以外的任何線索。
- 不寫帳號名稱、電子郵件地址、電話號碼。
- 不寫驗證碼、復原碼、安全提示問題的答案。

## 每一個帳號寫一列

- **服務種類**：例如信箱、學習平台、遊戲、影音、雲端相簿。只寫種類就好。
- **誰在用**：爸爸、孩子、全家共用。用稱呼，不寫全名。
- **密碼至少 15 個字元**：是、否、不確定。由知道密碼的人自己回答，不用證明給別人看。
- **和別的帳號重複**：有、沒有、不確定。
- **存在密碼管理器**：有、沒有。
- **雙重驗證已開啟**：有、沒有、這個服務沒有提供。
- **第二關的種類**：簡訊驗證碼、驗證 App、裝置上的確認、安全金鑰。不知道就寫「不確定」。
- **下一步／誰來做／預計完成日**：例如「改成不重複的長密碼／爸爸／這個週末」。

「不確定」是可以接受的答案；它代表下一步是去確認。
清單存檔之後請再看一次：上面沒有任何可以用來登入的資訊。
''',

'04_爸爸課後設定指引.md': '''# 爸爸課後設定指引（私下進行，不錄音、不錄影）

這份指引只整理官方說明裡寫到的事。實際的選單位置會隨系統版本改變，請以你裝置上的畫面和官方說明為準。

## 1. 密碼要多長

| 出處 | 建議 |
|---|---|
| NIST | 至少 15 個字元；長度比複雜度重要 |
| 數位發展部資通安全署 | 至少 15 個字元，或用密碼管理工具產生 |
| CISA | 至少 16 個字元；可用 5 到 7 個不相關的詞 |
| FTC | 至少 12 個字元；用隨機的詞組成密語 |

有些服務有自己的規定。例如 Apple 帳號的密碼要求是至少八個字元，包含大寫和小寫字母，以及至少一個數字。照服務的規定，再盡量加長。

## 2. 什麼時候換密碼

- 服務通知資料外洩，或你發現不明的登入紀錄：立刻換，而且用過同一組密碼的其他帳號也要換。
- 沒有上述情況，不必為了換而換。NIST 的指引要求服務提供者不得強制使用者定期更換密碼。

## 3. 密碼管理器

- 自 macOS Sequoia、iOS 18 起，Apple 裝置內建「密碼」App，可以產生、製作並儲存高強度密碼。
- 已設定 iCloud 鑰匙圈時，在 Safari 第一次按密碼欄位，系統會建議一個獨有且難以猜測的密碼。
- 注意：Safari 會替任何使用這台 Mac 同一個使用者帳號的人自動填寫。孩子請用自己的使用者帳號登入 Mac，你離開時鎖定螢幕。
- 也可以選擇其他密碼管理器；CISA 的說法是，你只需要記住打開管理器的那一組強密碼。

## 4. 雙重驗證

- Apple 帳號稱為「雙重認證」：登入新裝置時，需要一組六位數驗證碼，它會顯示在受信任的裝置上，或傳到受信任的電話號碼。
- Google 帳戶稱為「兩步驟驗證」。
- 可以選擇第二關的種類時：FTC 說實體安全金鑰最強；驗證 App 比簡訊好；簡訊或電子郵件驗證碼最弱，但有總比沒有好。
- 任何需要手動輸入的驗證碼都可能在假網頁被騙走。登入前先看網址，不從訊息裡的連結登入。下一堂課會專門談釣魚訊息。

## 5. 孩子的帳號

- Apple 規定未滿 13 歲（年齡依國家或地區而異）的兒童，必須由家長或監護人為他建立 Apple 帳號。
- 其他服務各有年齡規定，申請前先看該服務的條款。

## 6. 做完之後

回到家庭帳號安全清單，把完成的項目打勾。清單上仍然不寫任何密碼。

來源見 `00_爸爸先讀.md` 最後一節。
''',

'05_自選規則卡.md': '''# 孩子獨立改造：加一條自己的城堡規則

選一條，或自己發明。一次只加一條，才知道它有沒有用。

## 靈感

- 申請新帳號之前，先問爸爸。
- 驗證碼只有自己看，誰來要都不給。
- 有人要密碼或驗證碼，先停下來找爸爸。
- 新的密碼至少用四個不相關的詞。
- 不在別人的電腦上按「記住密碼」。
- 離開電腦就鎖定螢幕。
- 收到「你的帳號有問題」的訊息，不點裡面的連結。

## 我的規則卡

- 規則名稱：＿＿＿＿＿＿＿＿＿＿
- 我的規則（一句話）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 它是在加強哪一個零件？□ 長密碼　□ 唯一密碼　□ 密碼管理器　□ 雙重驗證
- 用紙牌再玩一回合測試，加規則前被攻破：＿＿ 個　加規則後：＿＿ 個
- 我看到的證據：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 這條規則什麼時候會很麻煩？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 要保留、修改，還是拿掉？為什麼？＿＿＿＿＿＿＿＿＿＿＿＿＿＿

規則卡上也不寫任何真正的密碼。
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成家庭帳號安全清單，上面沒有任何真正的密碼、帳號名稱或驗證碼
- [ ] 不看稿說出城堡的四個零件：長密碼、唯一密碼、密碼管理器、雙重驗證
- [ ] 說得出撞庫是什麼，以及為什麼每個帳號要用不同的密碼
- [ ] 攻防紀錄表有兩回合的結果，也有「為什麼」
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 測試過一條自選城堡規則，並說明要不要保留

## 孩子教爸爸（105–115 分鐘）

請孩子當老師，爸爸當學生。建議順序：

1. 孩子用詞語牌示範，怎麼排出一組夠長的密碼。
2. 孩子說明為什麼三個帳號不能用同一組，並重演一次外洩。
3. 孩子替一個帳號加上第二道門，說出第二關是什麼。
4. 爸爸扮演假客服要驗證碼，孩子示範怎麼拒絕。
5. 孩子出一題考爸爸，例如：「開了雙重驗證，為什麼還要小心假網頁？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

錄音時不念出任何帳號、密碼或驗證碼。

1. 密碼城堡與雙重驗證，是在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：`L007_家庭帳號安全清單_v01`、`L007_攻防紀錄_v01`、`L007_自選規則卡_v01`，
放進 `文件/Tech Academy/L007_密碼城堡與雙重驗證/`，存好後再打開一次確認，並再檢查一次上面沒有真密碼。
''',

'07_城堡四零件小抄.md': '''# L007 城堡四零件小抄

| 零件 | 像城堡的 | 做什麼 | 怎麼做 | 小心 |
|---|---|---|---|---|
| 長密碼 | 城牆 | 讓別人猜不到 | 把好幾個不相關的詞接起來，至少 15 個字元 | 不用生日、名字、電話，不用 123456 |
| 唯一密碼 | 一門一把鑰匙 | 一組外洩，別的帳號不受影響 | 每個帳號用不同的密碼 | 重複使用會被撞庫 |
| 密碼管理器 | 鑰匙保管箱 | 產生並記住又長又不重複的密碼 | 例如新版 Mac 內建的「密碼」App，和爸爸一起設定 | 守好打開保管箱的方法 |
| 雙重驗證 | 第二道門 | 密碼被偷，還有一關要過 | 能開就開：驗證碼、驗證 App 或安全金鑰 | 驗證碼不給任何人 |

## 四個提醒

- 長度比花樣重要；各機構的建議從 12 到 16 個字元以上，越長越好。
- 發現外洩或不明登入就立刻換密碼；不必為了換而換。
- 開了雙重驗證，也要小心假的登入網頁，驗證碼可能被騙走。
- 任何清單、紙條、照片上都不寫真正的密碼。

我最想加強的零件：＿＿＿＿＿＿　我的城堡規則：＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

SHEET_HEADER = ['編號', '服務種類（不寫帳號名稱）', '誰在用', '密碼至少15個字元', '和別的帳號重複', '存在密碼管理器',
                '雙重驗證已開啟', '第二關的種類', '下一步', '誰來做', '預計完成日']
SHEET_ROWS = [[str(i)] for i in range(1, 9)]

EXTRA_CSS = '''.key{height:118mm}.key h3{font-size:19pt}.key p{margin:1.5mm 0}.key .like{font-size:11pt;color:#35506b;margin:0 0 1mm}
.key .warn{font-size:10.5pt;color:#35506b;border-top:.8pt solid #9db7cc;padding-top:2mm;margin-top:3mm}
.strip{margin-top:5mm;font-size:11pt}
.words{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}.word{border:1.4pt dashed #0b2540;border-radius:3mm;height:36mm;display:flex;align-items:center;justify-content:center;font-size:21pt;font-weight:700}
.props{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}.prop{border:1.4pt dashed #0b2540;border-radius:3mm;height:66mm;padding:4mm;text-align:center}
.prop h3{font-size:16pt;margin:3mm 0 2mm}.prop p{margin:1mm 0;font-size:11pt}.prop .big{font-size:22pt;font-weight:700;letter-spacing:1.5pt;margin-top:6mm}
.fake{display:inline-block;font-size:9pt;font-weight:400;color:#fff;background:#0b2540;border-radius:1.5mm;padding:.2mm 2mm}
.log td{height:17mm}.log th{font-size:10.5pt}.wall td{height:10mm;text-align:center}.wall th{text-align:center}
.list{table-layout:fixed}.list th{font-size:9.5pt;padding:1mm .8mm;text-align:center}.list td{height:13.5mm}.list td.no{text-align:center;font-weight:700}
.never{border:1.6pt solid #b3261e;border-radius:3mm;padding:2.5mm 4.5mm;color:#7a1712;font-size:11.5pt;margin-bottom:4mm}'''


def html():
    key = lambda name, like, what, how, warn: (
        f'<div class="cut key"><h3>{name}</h3><p class="like">像城堡的：{like}</p><h4>做什麼</h4><p>{what}</p>'
        f'<h4>怎麼做</h4><p>{how}</p><p class="warn">{warn}</p></div>')
    pages = []
    pages.append('<h2>城堡四零件小抄卡</h2><p class="lead">沿外框剪下，放在鍵盤旁邊。四個零件一起用，城堡才守得住。</p><div class="grid2">'
        + key('長密碼', '城牆', '讓別人猜不到。長度比花樣更重要。', '把好幾個不相關的詞接成一句長句子，至少 15 個字元。', '不用生日、名字、電話，也不用 123456 這類常見密碼。')
        + key('唯一密碼', '一門一把鑰匙', '一組密碼外洩，別的帳號不受影響。', '每個帳號用不同的密碼。', '重複使用，壞人會拿外洩的密碼去試別的網站（撞庫）。')
        + key('密碼管理器', '鑰匙保管箱', '幫你產生、記住又長又不重複的密碼。', '例如新版 Mac 內建的「密碼」App，請和爸爸一起設定。', '守好打開保管箱的方法；共用電腦要用自己的使用者帳號。')
        + key('雙重驗證', '第二道門', '就算密碼被偷，還有一關要過。', '能開就開：驗證碼、驗證 App，或實體的安全金鑰。', '驗證碼不給任何人。開了也要小心假的登入網頁。')
        + '</div><p class="strip">任何清單、紙條、照片上，都不寫真正的密碼和驗證碼。</p>')

    pages.append('<h2>詞語牌</h2><p class="lead">共 24 張，沿虛線剪開。這些詞只用來玩遊戲，不要拿來當真正的密碼。</p><div class="words">'
        + ''.join(f'<div class="word">{w}</div>' for w in WORDS) + '</div>')

    fake = '<span class="fake">虛構</span>'
    props = ''.join(f'<div class="prop">{fake}<h3>{n}</h3><p>帳號卡</p><p class="note">{use}</p><p class="note" style="margin-top:6mm">密碼（守城的人另外寫在小紙條上蓋好）</p></div>'
                    for n, use in ACCOUNTS)
    props += ''.join('<div class="prop"><h3>第二道門</h3><p>雙重驗證卡</p><p class="note" style="margin-top:5mm">放在最重要的帳號卡上。<br>有人輸入密碼時，守城的人說：<br>「請輸入驗證碼。」</p></div>' for _ in range(2))
    props += '<div class="prop"><h3>外洩名單</h3><p class="note">外洩的帳號：</p><div class="line"></div><p class="note">它的密碼（詞語牌）：</p><div class="line"></div><div class="line"></div></div>'
    props += ''.join(f'<div class="prop">{fake}<h3>驗證碼牌</h3><p class="big">{c}</p><p class="note" style="margin-top:5mm">只有守城的人可以看。<br>誰來要都不給。</p></div>' for c in CODES)
    pages.append('<h2>帳號卡與攻防道具</h2><p class="lead">帳號和驗證碼都是虛構的遊戲道具。沿虛線剪開。</p>'
                 f'<div class="props">{props}</div>')

    wall = ''.join(f'<tr><th>{n} 張牌</th><td></td><td class="note">{calc}</td></tr>' for n, calc in
                   ((1, '24'), (2, '24 × 23'), (3, '24 × 23 × 22'), (4, '24 × 23 × 22 × 21')))
    log = ''.join(f'<tr><td><b>{a}</b><br><span class="note">{b}</span></td><td></td><td></td><td></td></tr>' for a, b in
                  (('第一回合', '三個帳號同一組密碼'), ('第二回合', '不重複＋第二道門'), ('加碼回合', '假客服要驗證碼'),
                   ('交換後第一回合', '重複密碼'), ('交換後第二回合', '不重複＋第二道門')))
    pages.append('<h2>攻防紀錄表</h2><p class="lead">暖身先算城牆有多高，再記下每一回合的結果。</p>'
        '<table class="wall"><tr><th style="width:22%">密碼用幾張牌</th><th style="width:38%">最多要猜幾次才一定猜到</th><th>算法提示</th></tr>' + wall + '</table>'
        '<table class="log" style="margin-top:6mm"><tr><th style="width:26%">回合</th><th style="width:20%">外洩的帳號</th><th style="width:18%">被攻破幾個</th><th>為什麼</th></tr>' + log + '</table>'
        '<div class="box" style="margin-top:5mm"><b>我的結論</b><p class="note" style="margin:1mm 0">哪一種守法被攻破最少？差在哪一個零件？</p><div class="line"></div><div class="line"></div></div>')

    rows = ''.join(f'<tr><td class="no">{i}</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>' for i in range(1, 9))
    pages.append('<h2>作品：家庭帳號安全清單</h2>'
        '<div class="never"><b>不寫：</b>密碼、密碼提示、帳號名稱、電子郵件地址、電話號碼、驗證碼。只寫服務的種類和檢查結果。</div>'
        '<table class="list"><tr><th style="width:6%">編號</th><th style="width:20%">服務種類<br>例：信箱、遊戲</th><th style="width:11%">誰在用</th>'
        '<th>至少 15<br>個字元</th><th>和別的<br>帳號重複</th><th>存在<br>保管箱</th><th>雙重驗證<br>開了嗎</th><th style="width:22%">下一步<br>誰來做、什麼時候</th></tr>'
        + rows + '</table>'
        '<p class="note" style="margin:2mm 0">填「是／否／不確定」。不確定也可以，它代表下一步是去確認。</p>'
        '<div class="box"><b>我的城堡規則</b><div class="line"></div><b>一個限制或安全提醒</b><div class="line"></div>'
        '<p class="note" style="margin:2mm 0 0">名稱：L007_家庭帳號安全清單_v＿＿　日期：＿＿＿＿　代號：＿＿＿＿</p></div>')
    return printpack.document('L007 密碼城堡與雙重驗證 列印包', '父子科技學院 L007｜密碼城堡與雙重驗證', pages, EXTRA_CSS)


if __name__ == '__main__':
    classroom_pack.build(
        slug='l007-password-castle', folder='L007_密碼城堡與雙重驗證', files=FILES,
        sheet=('03_家庭帳號安全清單.csv', SHEET_HEADER, SHEET_ROWS),
        pack_html=html(), pack_pdf='02_列印包_密碼城堡.pdf', pack_pages=5,
        pack_needles=('城堡四零件小抄卡', '詞語牌', '鯨魚', '帳號卡與攻防道具', '虛構', '攻防紀錄表', '家庭帳號安全清單', '不寫'),
        authoring_dir=Path(__file__).resolve().parent,
        extra={'gameProps': {'wordCards': len(WORDS), 'accounts': [a for a, _ in ACCOUNTS], 'fictional': True},
               'realPasswordsOrAccounts': 'none; the list template records service types and check results only',
               'answersProvided': 'guess-count table for the warm-up only'})
