"""Build the L006 classroom pack (real, usable materials; no private data).

    ./portable-runtime.sh python authoring/l006/classroom.py

The five practice cards are invented and say so on every card. After any change here:
rerun pipeline/delivery.py, then verify (classroom is fingerprinted).
"""
from pathlib import Path
import csv
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import printpack  # noqa: E402

R = Path(__file__).resolve().parents[2]
E = R / 'episodes/academy/l006-source-evidence'
D = E / 'classroom/L006_來源與證據偵探'
PRINT = Path(__file__).resolve().parent / 'print'
PDF = D / '02_列印包_來源偵探.pdf'

# Invented practice items. (tag, where it appears, text, type, why)
CARDS = [
 ('A', '犀牛角電腦公司的官方網站｜公告日期：2026 年 9 月 1 日',
  '犀牛角筆電的「學習模式」更新已經推出。更新說明與版本編號列在本頁下方。',
  '原始來源', '公司自己公告自己的產品，是第一手紀錄；有日期，也有可以回頭看的更新說明。提醒：原始來源也有立場，公司通常只講優點。'),
 ('B', '家人群組裡的轉傳訊息｜沒有日期',
  '聽說下個月開始，所有咕嚕平板都要付錢才能開機！我朋友的朋友在公司上班說的，快轉給大家！',
  '二手來源', '轉了好幾手的說法，沒有出處、沒有日期，只有「聽說」，還催你趕快轉傳。可信度很低，先不要轉。'),
 ('C', '影片下方的說明欄｜2026 年 8 月',
  '這款彩虹雲 App 讓你的打字速度變三倍！點下面的連結下載。#合作 #贊助',
  '廣告', '有「合作」「贊助」標示，目的是要你下載。「變三倍」沒有說是誰測的、怎麼測的，不能當證據。'),
 ('D', '影片底下的留言｜昨天',
  '閃電果手機是史上最好看的手機，其他的都很醜。',
  '意見', '好不好看是個人的感覺，每個人可以不一樣，沒有辦法查出對或錯。可以聽，但不是事實。'),
 ('E', '小報報科技週刊的報導｜2026 年 9 月 3 日',
  '根據犀牛角電腦公司 9 月 1 日的官方公告，「學習模式」更新已經推出（文末附公告連結）。記者試用後覺得新功能很方便。',
  '二手來源', '記者整理別人的公告，是二手來源；有日期、有出處，可以點回原始來源。最後一句「很方便」是記者的意見。'),
]

FILES = {
'00_爸爸先讀.md': '''# 父子科技學院 L006：真真假假——來源與證據偵探（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在孩子自己替消息分類、打分數、找第二來源，並說出理由。

## 這堂課要帶走什麼

- 偵探三問：誰說的？證據呢？別人也這麼說嗎？
- 四種訊息：原始來源、二手來源、廣告、意見；同一則消息常常混著好幾類。
- 意見和「可以檢查的說法」不一樣；查得出對或錯的，才能當證據。
- 找第二來源的方法：離開這一頁，開新分頁查這個網站或作者，再找另一個沒有關係的來源。
- 至少一個限制或安全注意：分數高不保證是真的、查不到就寫「還不確定」、可疑連結不亂點、不輸入個資。
- 作品：**來源可信度評分表**，另有第二來源紀錄與自選規則卡。

## 課前準備（約 20 分鐘）

1. 列印 `02_列印包_來源偵探.pdf`（A4，共 5 頁，單面）。沒有印表機也可以照著畫在白紙上。
2. 把第 2 頁的五張練習卡剪開。這五張卡的公司、產品和報導**全部是虛構的**，只用來練習分類。
3. 準備第二回合要評分的消息。課表寫的是「分析 5 則科技消息」，建議這樣挑：
   - 一則官方公告或新聞稿（例如作業系統更新說明、產品發表頁）
   - 一則整理別人說法的報導
   - 一則開箱或推薦影片（留意有沒有合作、贊助標示）
   - 一則社群貼文或群組轉傳
   - 一則留言或評論
4. 挑選原則：爸爸**先自己看過**；主題選孩子有興趣的科技消息（新遊戲機、太空任務、新功能）；
   避開驚嚇、災難畫面、醫療偏方與政治爭議；內容不含家人或朋友的姓名、帳號、照片。
5. 來不及準備真實消息時：第二回合直接用五張練習卡，只打前四項分數（滿分 8 分），
   「第二來源」改成口頭回答：「如果這是真的，我會去哪裡查？」然後至少和孩子一起查一則真實消息。
6. 確認孩子的電腦可以上網、瀏覽器可用。查證時由爸爸坐在旁邊。
7. 錄音只保存在家裡的私人位置，不直接公開；錄音前先說課次與主題，不要唸出帳號、密碼或住址。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：拿一則消息問孩子「你相信嗎？為什麼？」 | 觀察，不糾正 |
| 10–25 | 看影片、認識偵探三問與四種訊息；讀小抄卡 | 示範一次「意見」和「可以檢查的說法」 |
| 25–65 | 五則消息偵探賽（規則見 `01_活動規則_五則消息偵探賽.md`） | 計時、幫忙記錄，不代替孩子判斷 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：完成評分表，加一條自選偵探規則並測試 | 只在孩子開口時協助 |
| 105–115 | 角色互換：孩子教爸爸查證一則新消息 | 當學生，照孩子說的做，聽不懂就發問 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 問四個錄音問題，協助存檔 |

## 幾個觀念的依據與限制

- **原始來源與二手來源**：美國國會圖書館的教師指引把原始來源說成歷史的原料，是在事情發生當時留下的原始文件與物品；
  二手來源則是隔了一段時間或距離，重述、分析或解讀事件的說法。本課把它簡化成「第一手的紀錄」和「別人的整理」。
- 同一則內容算原始還是二手，有時要看你想查的是什麼。孩子說得出理由就好，不必硬分。
- **原始來源不等於一定客觀**。公司公告自己的產品是第一手，但通常只講優點。
- **偵探三問**：取自 Digital Inquiry Group 的 Civic Online Reasoning 課程三個核心問題
  （誰在資訊背後？證據是什麼？其他來源怎麼說？）。
- **橫向查證**：大學圖書館的媒體素養指引把它說成「開一個新的瀏覽器分頁」，用其他可信來源的資訊來評估這個來源，
  而不是只看它怎麼介紹自己。
- **廣告與合作標示**：美國聯邦貿易委員會（FTC）給網紅的指引說，和品牌有金錢、僱傭、個人或家庭關係時就要揭露，
  揭露要和推薦內容放在一起，用簡單清楚的說法。這是美國的規定；台灣的相關規範本次沒有查核，
  所以影片只說「通常會有標示」，並提醒沒有標示不代表不是廣告。
- **看日期、看佐證**：國際圖書館協會聯盟（IFLA）的「How To Spot Fake News」列出八個步驟，
  包括想一想來源、查作者、看佐證來源、查日期。
- **評分表只是工具**。分數高不保證是真的，分數低也不代表一定是假的；它幫你把理由寫清楚。

## 查證時的安全（請一定和孩子聊）

1. 不點可疑訊息裡的連結，也不下載附件。想查就自己開新分頁，用搜尋引擎找那個網站或單位。
2. 要求輸入密碼、帳號或個人資料的頁面，先停下來問爸爸。下一堂課會專門談密碼與雙重驗證。
3. 找不到第二來源時，不急著相信，也不急著說它是假的，寫下「還不確定」。
4. 還沒查清楚的消息，不轉傳。
5. 想找人幫忙查核時，台灣事實查核中心（https://tfc-taiwan.org.tw/）是一個可以參考的查核組織；它的查核報告也要看日期和出處。
6. 遇到讓人不舒服的內容，先關掉分頁，告訴爸爸，不必自己處理。

## 來源（查核日 2026-10-07）

- Library of Congress「Getting Started with Primary Sources」：https://loc.gov/programs/teachers/getting-started-with-primary-sources
- Digital Inquiry Group「Getting Started with the Civic Online Reasoning Curriculum」：https://cor.inquirygroup.org/blog/get-started-now
- Princeton University Library「Media Literacy: Lateral Reading」：https://libguides.princeton.edu/medialiteracy/lateralreading
- IFLA「How To Spot Fake News – IFLA in the post-truth society」：https://www.ifla.org/?p=110161
- FTC「Disclosures 101 for Social Media Influencers」：https://ftc.gov/system/files/documents/plain-language/1001a-influencer-guide-508_1.pdf
- FTC 商業指引部落格（2019-11-05）：https://www.ftc.gov/business-guidance/blog/2019/11/disclosures-101-new-ftc-resources-social-media-influencers
- FTC 消費者提醒「Protect yourself from phishing scams」（2025-06-04）：https://consumer.ftc.gov/consumer-alerts/2025/04/protect-yourself-phishing-scams
- Google Ads 說明「Google 搜尋結果與廣告的差別」：https://support.google.com/google-ads/answer/1722080?hl=zh-Hant
- 台灣事實查核中心「TFC連續五年獲得國際認證」：https://tfc-taiwan.org.tw/?p=104895

課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
課表的主要參考網址是 FTC 消費者網站的線上隱私與安全專區，本課引用的是同一網站的釣魚訊息提醒。
''',

'01_活動規則_五則消息偵探賽.md': '''# 五則消息偵探賽：規則

課表的好玩機制是「競速」。這一課只有**分類**比快；**可信度**要慢慢判斷，而且每個分數都要寫理由。

## 準備

- 列印包第 2 頁的五張練習卡（虛構），剪開。
- 爸爸課前挑好的五則真實科技消息（挑法見 `00_爸爸先讀.md`）。
- 列印包第 3 頁「來源可信度評分表」、第 4 頁「第二來源紀錄單」，或用 `03_來源可信度評分表.csv`。
- 計時器、筆。

## 第一回合：快分類（約 10 分鐘）

1. 把五張練習卡蓋起來洗牌。計時三分鐘。
2. 孩子一張一張翻開，說出它是原始來源、二手來源、廣告，還是意見，並說一個理由。
3. 分類正確又說得出理由，得一顆星；只說對分類，得半顆星。
4. 時間到之後一起對 `04_評分標準與練習卡解說.md`。有一張卡混了兩類，找得到嗎？
5. 討論：E 卡能不能當 A 卡的第二來源？（E 是轉述 A，所以不算獨立的第二來源，但它幫你找到原始來源。）

## 第二回合：慢判斷（約 30 分鐘）

每一則真實消息做一樣的事，一則大約五到六分鐘：

1. 先分類，寫在評分表。
2. 問偵探三問，依 `04` 的評分標準打五項分數：來源、日期、證據、目的、第二來源，各 0–2 分。
3. 找第二來源：開新分頁，搜尋這個網站或作者的名字，再找另一個沒有關係的來源，寫進第二來源紀錄單。
4. 每個分數旁邊寫理由。寫不出理由的分數不算。
5. 最後寫下判斷：可信、還不確定，或很可疑。

這一回合不計時。查得仔細、理由清楚的人贏。

## 結算（約 5 分鐘）

- 哪一則分數最高？哪一則最低？差在哪一項？
- 有沒有一則消息，一開始覺得可信，查完之後改變想法？
- 孩子說出結論，爸爸只追問「你怎麼知道的？」

## 常見卡關

- 分不出原始還是二手：問「這是當事人自己說的，還是別人幫他整理的？」
- 找不到是誰說的：看網頁最上面和最下面、「關於我們」，或開新分頁搜尋網站名稱。
- 找到很多篇內容一樣的文章：看它們是不是都引用同一篇，那還是同一個來源。
- 查不到第二來源：寫「還不確定」，這也是正確答案。
- 孩子想點訊息裡的連結：先停，改成自己搜尋。
''',

'03_來源可信度評分表_填寫說明.md': '''# 來源可信度評分表怎麼寫

`03_來源可信度評分表.csv` 可以用 Numbers 或任何試算表開啟；也可以直接寫在列印包第 3 頁。

每一則消息寫一列：

- **消息一句話**：用自己的話寫這則消息在說什麼，不要整段抄。
- **在哪裡看到**：網站名稱、頻道名稱或「群組轉傳」。不要寫家人朋友的姓名或帳號。
- **類型**：原始來源、二手來源、廣告、意見；混著好幾類就都寫。
- **誰說的**：作者、單位或公司；看不出來就寫「不確定」。
- **消息日期**：網頁或訊息上的日期，沒有就寫「無」。
- **五項分數**：來源、日期、證據、目的、第二來源，各 0–2 分，標準見 `04_評分標準與練習卡解說.md`。
- **總分**：五項加起來，滿分 10 分。
- **我找到的第二來源**：寫出是誰；只是互相轉貼就寫「同一個來源」；找不到就寫「無」。
- **理由**：為什麼這樣打分。
- **我的判斷**：可信、還不確定、很可疑。

分數高不保證一定是真的；它只代表你查到的證據比較多。查不到的時候寫「還不確定」。
''',

'04_評分標準與練習卡解說.md': '''# 評分標準與練習卡解說（爸爸用，第一回合結束再給孩子看）

## 五項評分標準（各 0–2 分，滿分 10 分）

| 項目 | 0 分 | 1 分 | 2 分 |
|---|---|---|---|
| 來源：誰說的？ | 看不出是誰 | 知道是誰，但不確定他了不了解這件事 | 是當事人或負責的單位，或清楚交代消息從哪裡來 |
| 日期 | 沒有日期 | 有日期，但很舊，或不確定還適不適用 | 有日期，而且對這件事來說夠新 |
| 證據 | 只有「聽說」「有人說」 | 有提到出處，但點不進去或查不到 | 有出處、數字或照片，而且我自己查得到 |
| 目的 | 想要我買、下載、點連結或趕快轉傳，而且沒有說清楚 | 是廣告或合作內容，但有清楚標示 | 主要是告知或說明 |
| 第二來源 | 找不到 | 找到了，但只是互相轉貼，其實是同一個來源 | 找到彼此沒有關係的來源，說法一致 |

參考判讀（只是參考）：8–10 分，目前查到的證據支持它；5–7 分，還不確定，先不轉傳；0–4 分，很可疑。
分數高不保證一定是真的，分數低也不代表一定是假的。

## 五張練習卡（全部虛構）

| 卡 | 出現的地方 | 建議分類 | 為什麼 |
|---|---|---|---|
''' + ''.join(f'| {t} | {w} | {k} | {y} |\n' for t, w, _, k, y in CARDS) + '''
孩子的分類和這張表不一樣時，先聽理由。說得出道理的答案也算對，例如把 E 卡說成「二手來源加上一點意見」。

## 可以追問的問題

- A 卡是公司自己說的。它一定會把缺點也告訴你嗎？
- B 卡叫你「快轉給大家」。為什麼假消息常常催你趕快轉？
- C 卡說「變三倍」。要看到什麼，你才願意相信這個數字？
- D 卡是意見。你可以舉一句關於同一支手機、可以檢查的說法嗎？
- E 卡和 A 卡講同一件事。它們算兩個來源嗎？
''',

'05_自選規則卡.md': '''# 孩子獨立改造：加一條自己的偵探規則

選一條，或自己發明。一次只加一條，才知道它有沒有用。

## 靈感

- 沒有日期，先扣一分。
- 只有「聽說」「有人說」，證據直接 0 分。
- 轉傳之前，一定先找到第二來源。
- 看到「快轉給大家」，先停十秒。
- 有合作或贊助標示，再找一個沒有合作關係的來源。
- 數字要找得到是誰量的、怎麼量的。
- 截圖不算出處，要找到原來的那一頁。

## 我的規則卡

- 規則名稱：＿＿＿＿＿＿＿＿＿＿
- 我的規則（一句話）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 我預測它會讓評分：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 用同一則消息測試，加規則前：＿＿＿ 分　加規則後：＿＿＿ 分
- 我看到的證據：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 這條規則什麼時候不適用？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 要保留、修改，還是拿掉？為什麼？＿＿＿＿＿＿＿＿＿＿＿＿＿＿

把結果也記到評分表的「自選規則」那一列。
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成來源可信度評分表（五則消息都有分類、五項分數、理由與判斷）
- [ ] 不看稿說出偵探三問：誰說的？證據呢？別人也這麼說嗎？
- [ ] 各舉一個原始來源、二手來源、廣告、意見的例子
- [ ] 至少替一則消息找到第二來源，或誠實寫下「還不確定」並說明查了什麼
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 測試過一條自選規則，並說明要不要保留

## 孩子教爸爸（105–115 分鐘）

請孩子當老師，爸爸當學生。建議順序：

1. 爸爸拿出一則新的消息（先看過、不含個資）。
2. 孩子帶爸爸問偵探三問，爸爸照著回答。
3. 孩子示範怎麼開新分頁找第二來源，並說出為什麼不直接點訊息裡的連結。
4. 一起打分數，孩子說出哪一項最低、為什麼。
5. 孩子出一題考爸爸，例如：「很多人按讚，算不算證據？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

1. 當來源與證據偵探，是在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：`L006_來源可信度評分表_v01`、`L006_第二來源紀錄_v01`、`L006_自選規則卡_v01`，
放進 `文件/Tech Academy/L006_來源與證據偵探/`，存好後再打開一次確認。
''',

'07_偵探三問小抄.md': '''# L006 偵探三問小抄

| 問題 | 要找什麼 | 怎麼查 | 小心 |
|---|---|---|---|
| 誰說的？ | 這則消息背後的人或單位 | 找作者、網站名稱、「關於我們」；開新分頁搜尋他的名字 | 看不出是誰說的，先扣分 |
| 證據呢？ | 可以回頭檢查的東西 | 找出處、日期、數字、原始照片；點進去看原文 | 只有「聽說」「有人說」，還不算證據 |
| 別人也這麼說嗎？ | 另一個沒有關係的來源 | 開新分頁搜尋這件事；比一比兩邊的說法 | 互相轉貼，還是同一個來源 |

## 四種訊息

| 類型 | 是什麼 | 例子 |
|---|---|---|
| 原始來源 | 第一手的紀錄 | 官方公告、當事人的說明、現場原始照片 |
| 二手來源 | 別人整理或轉述的內容 | 整理消息的報導、懶人包、轉貼的訊息 |
| 廣告 | 想要你買東西或下載 | 有「廣告」「贊助」「合作」標示的內容 |
| 意見 | 個人的感覺和看法 | 「這支手機最好用」 |

## 四個提醒

- 意見可以聽，但不能直接當成事實；查得出對或錯的，才能當證據。
- 很多人轉貼、很多人按讚，只代表熱門，不代表是真的。
- 找不到第二來源，先寫「還不確定」，不急著相信，也不急著轉傳。
- 可疑連結不亂點；要求輸入密碼或個人資料的頁面，先停下來問爸爸。

我最常忘記問的是：＿＿＿＿＿＿　我的偵探規則：＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

NOTE_HEADER = ['編號', '消息一句話', '在哪裡看到', '類型', '誰說的', '消息日期', '來源(0-2)', '日期(0-2)', '證據(0-2)',
               '目的(0-2)', '第二來源(0-2)', '總分(0-10)', '我找到的第二來源', '理由', '我的判斷']
NOTE_ROWS = [['消息一'], ['消息二'], ['消息三'], ['消息四'], ['消息五'], ['自選規則測試']]

EXTRA_CSS = '''.key{height:118mm}.key h3{font-size:19pt}.key p{margin:1.5mm 0}
.key .warn{font-size:10.5pt;color:#35506b;border-top:.8pt solid #9db7cc;padding-top:2mm;margin-top:3mm}
.key table{font-size:11pt;margin-top:2mm}.key td,.key th{padding:1.6mm 2mm}
.strip{margin-top:5mm;font-size:11pt}
.pc{height:79mm;padding:4mm 5mm}.pc h3{font-size:13.5pt;margin:0}.pc .where{font-size:9.5pt;color:#4a6a88;margin:1mm 0 2mm}
.pc .say{font-size:12pt;margin:0;min-height:30mm}.pc .pick{font-size:10pt;margin:2mm 0 0;border-top:.8pt solid #9db7cc;padding-top:1.5mm}
.fake{display:inline-block;font-size:9pt;font-weight:400;color:#fff;background:#0b2540;border-radius:1.5mm;padding:.2mm 2mm;margin-left:2mm;vertical-align:middle}
.score{table-layout:fixed}.score th{font-size:9.5pt;padding:1mm .8mm;text-align:center}.score td{height:15mm}.score td.why{height:13mm;font-size:9.5pt;color:#4a6a88}
.score td.no{text-align:center;font-weight:700}
.second{margin-bottom:4mm}.second h3{font-size:13pt;margin-bottom:1mm}.second td{height:10mm}.second th{width:30%}
.rubric td,.rubric th{font-size:10.5pt;padding:1.3mm 2mm}.tick{font-size:10.5pt}'''


def html():
    key = lambda name, what, how, example, warn: (
        f'<div class="cut key"><h3>{name}</h3><h4>要找什麼</h4><p>{what}</p><h4>怎麼查</h4><p>{how}</p>'
        f'<h4>例子</h4><p>{example}</p><p class="warn">{warn}</p></div>')
    pages = []
    pages.append('<h2>偵探三問小抄卡</h2><p class="lead">沿外框剪下，查證時放在鍵盤旁邊。</p><div class="grid2">'
        + key('一、誰說的？', '這則消息背後的人或單位。他了解這件事嗎？', '找作者、網站名稱、「關於我們」；開新分頁搜尋他的名字。', '公司官網的公告，是當事人自己說的。', '看不出是誰說的，先扣分。')
        + key('二、證據呢？', '可以回頭檢查的東西。', '找出處、日期、數字、原始照片；點進去看原文。', '「根據某單位 9 月 1 日的公告」，而且附上連結。', '只有「聽說」「有人說」，還不算證據。')
        + key('三、別人也這麼說嗎？', '另一個彼此沒有關係的來源，說法一致嗎？', '開新分頁搜尋這件事；比一比兩邊的說法。', '官方公告，加上另一家自己查證過的報導。', '互相轉貼，還是同一個來源。')
        + '<div class="cut key"><h3>四種訊息</h3><table><tr><th style="width:30%">原始來源</th><td>第一手的紀錄</td></tr>'
          '<tr><th>二手來源</th><td>別人整理或轉述的內容</td></tr><tr><th>廣告</th><td>想要你買東西或下載</td></tr>'
          '<tr><th>意見</th><td>個人的感覺和看法</td></tr></table>'
          '<p style="margin-top:4mm">同一則消息，常常混著好幾類。</p>'
          '<p class="warn">意見可以聽，但不能直接當成事實。查得出對或錯的，才能當證據。</p></div>'
        + '</div><p class="strip">找不到第二來源？先寫「還不確定」，不急著相信，也不急著轉傳。可疑連結不亂點。</p>')

    pick = '<p class="pick">分類：□ 原始　□ 二手　□ 廣告　□ 意見<br>理由：</p>'
    cards = ''.join(f'<div class="cut pc"><h3>練習卡 {t}<span class="fake">虛構</span></h3><p class="where">{w.replace("｜", "<br>")}</p>'
                    f'<p class="say">{s}</p>{pick}</div>' for t, w, s, _, _ in CARDS)
    cards += ('<div class="cut pc"><h3>我找到的真實消息</h3><p class="where">在哪裡看到：＿＿＿＿＿＿＿＿＿＿＿＿<br>日期：＿＿＿＿＿＿＿＿</p>'
              '<p class="say">用自己的話寫一句：</p>' + pick + '</div>')
    pages.append('<h2>五張練習卡</h2><p class="lead">卡片上的公司、產品和報導全部是虛構的，只用來練習分類。沿外框剪下。</p>'
                 f'<div class="grid2" style="gap:4mm">{cards}</div>')

    rows = ''.join(f'<tr><td class="no" rowspan="2">{n}</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>'
                   '<tr><td class="why" colspan="9">理由與第二來源：</td></tr>' for n in '一二三四五')
    pages.append('<h2>作品：來源可信度評分表</h2><p class="lead">五項各 0–2 分，滿分 10 分。每個分數都要有理由；查不到就寫「還不確定」。</p>'
        '<table class="score"><tr><th style="width:6%">消息</th><th style="width:25%">這則消息在說什麼</th><th style="width:11%">類型</th>'
        '<th>來源<br>0–2</th><th>日期<br>0–2</th><th>證據<br>0–2</th><th>目的<br>0–2</th><th style="width:10%">第二來源<br>0–2</th><th>總分</th><th style="width:13%">我的判斷</th></tr>'
        + rows + '</table>'
        '<div class="box" style="margin-top:4mm"><b>我的偵探規則</b><div class="line"></div><b>評分表的一個限制</b><div class="line"></div>'
        '<p class="note" style="margin:2mm 0 0">名稱：L006_來源可信度評分表_v＿＿　日期：＿＿＿＿　代號：＿＿＿＿</p></div>')

    second = lambda n: (f'<div class="box second"><h3>消息{n}：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</h3>'
        '<table><tr><th>我搜尋了什麼字詞</th><td></td></tr><tr><th>找到的第二來源是誰</th><td></td></tr>'
        '<tr><th>它和原來的來源有關係嗎</th><td class="tick">□ 沒有關係　□ 只是轉貼同一篇　□ 看不出來</td></tr>'
        '<tr><th>兩邊的說法</th><td class="tick">□ 一致　□ 不一致　□ 查不到，還不確定</td></tr></table></div>')
    pages.append('<h2>第二來源紀錄單</h2><p class="lead">離開原來那一頁，開新分頁去查。不點訊息裡的連結，自己搜尋。</p>'
        + second('一') + second('二') + second('三')
        + '<div class="cut" style="padding:4mm 6mm"><h3 style="font-size:14pt;margin:0">自選規則卡</h3>'
          '<p style="margin:1.5mm 0 0;font-size:11pt">我的規則（一句話）</p><div class="line"></div>'
          '<p style="margin:1.5mm 0 0;font-size:11pt">用同一則消息測試：加規則前 ＿＿ 分　加規則後 ＿＿ 分</p>'
          '<p style="margin:1.5mm 0 0;font-size:11pt">要保留、修改，還是拿掉？為什麼？</p><div class="line"></div></div>')

    pages.append('<h2>評分標準與安全提醒</h2><p class="lead">五項各 0–2 分。分數高不保證一定是真的；它代表你查到的證據比較多。</p>'
        '<table class="rubric"><tr><th style="width:17%">項目</th><th>0 分</th><th>1 分</th><th>2 分</th></tr>'
        '<tr><th>來源：誰說的？</th><td>看不出是誰</td><td>知道是誰，但不確定他了不了解這件事</td><td>是當事人或負責的單位，或清楚交代消息從哪裡來</td></tr>'
        '<tr><th>日期</th><td>沒有日期</td><td>有日期，但很舊，或不確定還適不適用</td><td>有日期，而且對這件事來說夠新</td></tr>'
        '<tr><th>證據</th><td>只有「聽說」「有人說」</td><td>有提到出處，但點不進去或查不到</td><td>有出處、數字或照片，而且我自己查得到</td></tr>'
        '<tr><th>目的</th><td>想要我買、下載、點連結或趕快轉傳，而且沒有說清楚</td><td>是廣告或合作內容，但有清楚標示</td><td>主要是告知或說明</td></tr>'
        '<tr><th>第二來源</th><td>找不到</td><td>找到了，但只是互相轉貼，其實是同一個來源</td><td>找到彼此沒有關係的來源，說法一致</td></tr></table>'
        '<div class="grid2" style="margin-top:6mm"><div class="box"><b>第一回合：快分類</b>'
        '<p class="note" style="margin:1mm 0">五張練習卡，限時三分鐘。分類正確又說得出理由，一顆星。</p>'
        '<table><tr><th>卡</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th></tr><tr><th>星</th><td style="height:11mm"></td><td></td><td></td><td></td><td></td></tr></table>'
        '<p class="note" style="margin:2mm 0 0">我用了 ＿＿ 分 ＿＿ 秒，得到 ＿＿ 顆星。</p></div>'
        '<div class="box"><b>參考判讀（只是參考）</b><p style="margin:1mm 0;font-size:11.5pt">8–10 分：目前的證據支持它<br>5–7 分：還不確定，先不轉傳<br>0–4 分：很可疑</p>'
        '<p class="note" style="margin:2mm 0 0">分數低也不代表一定是假的。</p></div></div>'
        '<div class="box" style="margin-top:6mm"><b>查證時的安全</b><p style="margin:1mm 0;font-size:11.5pt">一、不點可疑訊息裡的連結，也不下載附件；自己開新分頁搜尋。<br>'
        '二、要求輸入密碼、帳號或個人資料的頁面，先停下來問爸爸。<br>三、還沒查清楚的消息，不轉傳。<br>四、看到不舒服的內容，關掉分頁，告訴爸爸。</p></div>')
    return printpack.document('L006 來源與證據偵探 列印包', '父子科技學院 L006｜來源與證據偵探', pages, EXTRA_CSS)


def main():
    D.mkdir(parents=True, exist_ok=True)
    PRINT.mkdir(parents=True, exist_ok=True)
    for name, text in FILES.items():
        assert '待編寫' not in text
        (D / name).write_text(text, encoding='utf-8')
    with (D / '03_來源可信度評分表.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f); w.writerow(NOTE_HEADER)
        w.writerows([r + [''] * (len(NOTE_HEADER) - len(r)) for r in NOTE_ROWS])
    source = PRINT / 'print-pack.html'
    source.write_text(html(), encoding='utf-8')
    rendered = printpack.render(source, PDF)

    names = sorted(p.name for p in D.iterdir() if p.is_file())
    for name in FILES:
        assert (D / name).read_text(encoding='utf-8').strip()
    with (D / '03_來源可信度評分表.csv').open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    assert len(rows) == 7 and all(len(r) == len(NOTE_HEADER) for r in rows)
    pages = printpack.check(PDF, 5, ('偵探三問小抄卡', '五張練習卡', '虛構', '來源可信度評分表', '第二來源紀錄單', '評分標準', '犀牛角'))
    (E / 'qc').mkdir(exist_ok=True)
    (E / 'qc/classroom-validation.json').write_text(json.dumps({
        'folder': D.relative_to(E).as_posix(), 'files': names, 'fileCount': len(names),
        'utf8TextReadable': True, 'scoreSheetRows': len(rows) - 1, 'scoreSheetColumns': len(NOTE_HEADER),
        'printPack': {'file': PDF.name, 'pages': pages, 'allFontsEmbedded': True, 'renderedThisRun': rendered,
                      'source': 'authoring/l006/print/print-pack.html'},
        'practiceCards': {'count': len(CARDS), 'fictional': True, 'labelledOnEveryCard': True},
        'answersProvided': 'suggested classification for the five invented practice cards only', 'privateData': 'none',
        'status': 'PASS (structure); page-by-page visual review recorded separately'},
        ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Classroom pack: {len(names)} files, print pack {pages} pages')


if __name__ == '__main__':
    main()
