"""Build the L010 classroom pack (real, usable materials; no private data).

    ./portable-runtime.sh python authoring/l010/classroom.py

The lesson needs no AI account: the child sorts printed function cards. After any change here:
rerun pipeline/delivery.py, then verify.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import classroom_pack  # noqa: E402
import printpack  # noqa: E402

BASKETS = ['固定規則', '機器學習', '生成式 AI', '不是 AI']
# (tag, name, what you see, suggested basket, reason, basis / limit, where it can go wrong)
CARDS = [
 ('1', '計算機 App', '按 12 × 3，它算出 36。', '固定規則', '人寫好的計算步驟，同樣的輸入，每次答案都一樣。',
  'Oak National Academy：計算機每次都用同樣的步驟；它把計算機列為不使用 AI。', '按錯數字，它還是照算；它不會知道你其實想算什麼。'),
 ('2', '鬧鐘', '設定早上七點，時間到就響。', '固定規則', '規則只有一條：「如果到了七點，就響」。',
  '本課自己的例子，沒有官方來源做這個分類。', '放假忘了關，它一樣會響；它不知道今天不用上學。'),
 ('3', '用臉解鎖手機', '看一眼，手機就解鎖。', '機器學習', '手機從你的臉部資料學會比對，沒有人寫「眼睛距離幾公分」這種步驟。',
  'Apple：Face ID 使用原深感測相機與機器學習。', 'Apple 說 13 歲以下兒童被誤認的機率比較高。'),
 ('4', '照片整理', '手機自動把有狗的照片找出來。', '機器學習', '它看過大量的照片，學會認出人物、寵物和場景。',
  'Apple：「照片」用裝置上的機器學習做場景分類、人物與寵物辨識。', '可能把貓認成狗，或漏掉一些照片。'),
 ('5', '垃圾郵件過濾', '信箱自動把可疑的信放進垃圾信匣。', '機器學習', '它看過大量的郵件，學會分辨哪些像垃圾信。',
  'Google（2017）：機器學習幫 Gmail 擋下垃圾郵件與釣魚郵件。', '可能把重要的信丟進垃圾信匣，也可能放過釣魚信（第八堂）。'),
 ('6', '影片推薦', '看完一部，網站推薦下一部。', '機器學習', '它從大量的觀看紀錄裡找規律，猜你可能想看什麼。',
  'UNICEF：推薦引擎多半靠辨認資料規律的機器學習。', '它是照規律猜的，不一定是你需要的，也不一定適合你。'),
 ('7', '聊天機器人寫詩', '請它寫一首關於犀牛的詩，它就寫出來。', '生成式 AI', '它做出原本不存在的新文字。',
  'UNICEF、Microsoft：生成式 AI 依資料裡的規律產生新內容。', '內容可能是錯的，而且說得很有把握。'),
 ('8', '文字變圖片', '輸入「戴帽子的犀牛」，它畫出一張圖。', '生成式 AI', '它做出原本不存在的新圖片。',
  'UNICEF：生成式 AI 能產生語言、圖像和其他媒體的新內容。', '可能畫出奇怪或不合理的細節；畫出來的圖不是真的照片。'),
 ('9', '紙本字典', '翻到那一頁，查一個字。', '不是 AI', '裡面沒有程式；查的人是你。',
  'Oak National Academy：紙本字典不使用 AI。', '字典不會錯在「判斷」，但內容可能過時。'),
 ('10', '電燈開關', '按下去，燈就亮。', '不是 AI', '沒有程式在判斷，只是把電路接通。',
  '本課自己的例子，沒有官方來源做這個分類。', '如果是「有人經過才亮」的感應燈，就多了一條固定規則，可以討論要不要換籃子。'),
]
CHALLENGE = [
 ('A', '語音助理', '對手機說「明天會下雨嗎？」', '不只一個答案',
  '聽出你在叫它，用到機器學習；有些新的助理還會用生成式 AI 來回答。放「機器學習」或「生成式 AI」都可以，要說出是哪一部分。',
  'Apple（2017）：「Hey Siri」偵測器使用深度神經網路；Oak：語音助理使用 AI。本課沒有查核任何一款助理現在的做法。', '可能聽錯你說的話，或回答錯。'),
 ('B', '鍵盤選字', '打「謝」，它建議「謝謝」。', '機器學習',
  '它從大量文字裡學會猜下一個字。原理和生成式 AI 很像，所以放「生成式 AI」並說出這個理由，也算對。',
  'Oak：預測輸入使用 AI；MIT Sloan：生成式 AI 像進階的自動完成。', '常常猜錯，選錯字還是要自己檢查。'),
]
assert len(CARDS) == 10 and [sum(1 for c in CARDS if c[3] == b) for b in BASKETS] == [2, 4, 2, 2]

FILES = {
'00_爸爸先讀.md': '''# 父子科技學院 L010：AI 是什麼、不是什麼（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在孩子自己把功能卡分進籃子、說出理由，再替家裡找到的新功能分類。

## 這堂課要帶走什麼

- AI 是人用程式和資料做出來的電腦系統，背後是計算，沒有魔法。
- 分類三問：它是不是只照人寫好的固定步驟做？是不是從很多例子找規律？會不會做出新的內容？
- 四個籃子：固定規則、機器學習、生成式 AI、不是 AI。
- AI 不是魔法、不是人、不是永遠正確。重要的事要再查證。
- 至少一個限制或安全注意：生成式 AI 的回答可能是錯的；不把個資輸入 AI 工具。
- 作品：**AI 功能分類牆**，另有競速紀錄、自選功能卡與一條家庭 AI 約定。

## 這堂課不需要孩子的 AI 帳號

整堂課用紙卡就能完成，孩子不需要登入任何生成式 AI 工具。各平臺有年齡限制：

- 教育部「中小學使用『生成式人工智慧』注意事項 2.1」：學生應遵守各平臺註冊年齡限制；在校由教師引導，非在校使用請家長陪伴。
- Claude：Anthropic 的說明寫，建立和使用帳號須年滿 18 歲。
- Gemini：Google 的說明寫，13 歲以下（或所在國家適用的年齡）的孩子，要由家長替受監護的帳號開啟才能使用。
  台灣適用的年齡與開放情形這次沒有查核。
- ChatGPT：條款寫須年滿 13 歲，未滿 18 歲需家長或監護人同意。這一條只有擷取工具的摘要，沒有逐字確認，請以官方頁面為準。

想讓孩子看一次生成式 AI 怎麼回答，請由爸爸用**自己的帳號**操作，孩子在旁邊看：
問一個可以在圖鑑或百科查到答案的問題，再一起查證。不輸入姓名、照片、住址、學校等個資。

## 課前準備（約 15 分鐘）

1. 列印 `02_列印包_AI功能分類牆.pdf`（A4，共 6 頁，單面），把第 2 頁的十六張卡剪開（十張功能卡、兩張挑戰卡、四張空白卡），
   再把第 3、4 頁上下黏在一起，就是分類牆的底板。
2. 讀一遍 `04_功能卡解說.md`，知道每張卡建議放哪個籃子、理由和依據。
3. 準備計時器（手機的碼表就可以）、口紅膠或紙膠帶、彩色筆。
4. 課表的課前準備是「確認兒童帳號、家庭備份與瀏覽器可用；準備不含真實個資的範例」。這堂課用不到兒童帳號；
   如果要示範 AI 工具，先確認你自己的帳號可以用，並先想好一個不含個資的問題。
5. 錄音只保存在家裡的私人位置，不直接公開；錄音前先說課次與主題。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：拿「計算機 App」和「聊天機器人寫詩」兩張卡問孩子「哪一個是 AI？你怎麼知道？」 | 聽，不糾正 |
| 10–25 | 看影片，認識分類三問和四個籃子；讀小抄卡 | 回答孩子的問題；不知道的就說「我們等一下查」 |
| 25–65 | 功能分類牆競速（規則見 `01`） | 當計時員和裁判、追問理由、幫忙記錄 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：在家裡找一個新功能，寫功能卡和提醒卡，再加一條家庭 AI 約定 | 只在孩子開口時協助 |
| 105–115 | 角色互換：孩子教爸爸分類一個新功能 | 當學生，故意問「它這麼聰明，為什麼還會錯？」 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 問四個錄音問題，一起決定分類牆貼哪裡 |

## 「固定規則」算不算 AI？（請先知道這件事有爭議）

- 英格蘭的 Oak National Academy（小學四年級課程）說：只照簡單固定步驟做事的，不是 AI；計算機、紅綠燈、紙本字典不使用 AI。
- UNICEF 的指引說，AI 系統的運作方式包括照明確的規則、從例子學習，或靠試誤改進；OECD 也把規則列為 AI 系統的一種做法。
- OECD 自己說，要對 AI 系統的定義取得共識並不容易。台灣的人工智慧基本法第三條另有一個定義。

所以課表把「規則」和「非 AI」分成兩類是合理的教學安排，但不是唯一的分法。
孩子如果說「計算機也算一種很簡單的 AI」，可以回答：「有些專家會這樣算，有些不會；我們今天先看它是怎麼做事的。」

## 幾個觀念的依據與限制

- **機器學習**：OECD 的說明是，機器靠訓練資料找出規律，而不是靠人明確寫出指令。Code.org 的說法是，電腦辨認規律並做決定，而不是被明確地寫好每一步。
- **生成式 AI**：UNICEF 的說明是，它不只辨認和處理資料，還會用統計規律預測語言、圖像等內容接下來是什麼，產生新的內容。
  MIT Sloan 的教學資源形容它像進階的自動完成。「一個字接一個字」是針對文字的簡化說法。
- **會出錯**：Google 給家長的說明寫，Gemini 可能產生幻覺，把不正確的資訊說得像事實。Anthropic 的條款寫，輸出即使看起來很詳細也可能不正確，不應在沒有自行確認的情況下依賴。
- **偏差**：教育部注意事項寫，資料本身有成見或錯誤，結果也會有偏差或錯誤，因為這些工具無法自行判斷結果的正確性和合理性。
- **不是人**：Google 給家長的說明寫，Gemini 雖然很會對話，但不是人，不會自己思考，也沒有情緒。
  UNICEF 建議教孩子把 AI 看成資料驅動的應用，而不是有知覺的機器。這些是廠商與國際組織給家長的提醒，不是某項研究的結論。
- **個資**：教育部注意事項（學生版）寫，不可以將自己或他人的姓名、照片、聯絡方式、住址、學號等個人資料，或家庭、學校的機密資訊輸入生成式 AI 工具；
  輸入的資料「可能」被收錄到訓練資料庫，這是可能，不是一定。
- **功能卡的依據**寫在 `04_功能卡解說.md`。鬧鐘和電燈開關是本課自己的例子，沒有官方來源做這個分類。
  Apple 的說法只針對 Face ID 和 Apple 的「照片」；其他品牌的做法沒有查核。

## 來源（查核日 2026-10-07）

- 教育部「中小學使用『生成式人工智慧』注意事項 2.1」（學生版，115 年 2 月 11 日核定；讀的是師大附中國中部網站轉載的 PDF）
- 人工智慧基本法第三條（總統府公報第 7837 號）：https://www.president.gov.tw/File/Doc/80165b6d-cb49-4b49-952f-56e1e6abe51b
- OECD「Explanatory memorandum on the updated OECD definition of an AI system」（2024-02；讀的是大學網站轉載的 PDF）
- OECD.AI「Updates to the OECD definition of an AI system explained」：https://oecd.ai/en/wonk/ai-system-definition-update
- UNICEF「Guidance on AI and Children 3.0」（2025-12）：https://www.unicef.org/innocenti/media/11991/file/UNICEF-Innocenti-Guidance-on-AI-and-Children-3-2025.pdf
- Oak National Academy「What is artificial intelligence?」：https://www.thenational.academy/pupils/lessons/what-is-artificial-intelligence/video
- Code.org「Introduction to Machine Learning」教案：https://lesson-plans.code.org/csd7-2026/20260324130350/teacher-lesson-plans/Lesson-1-Introduction-to-Machine-Learning.pdf
- Microsoft「How Does Generative AI Work」：https://www.microsoft.com/en-us/ai/ai-101/how-does-generative-ai-work
- MIT Sloan「When AI Gets It Wrong: Addressing AI Hallucinations and Bias」：https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/
- Google「Guide your child's Gemini Apps experience」：https://support.google.com/gemini/answer/16109150?hl=en
- Anthropic「Consumer Terms of Service」：https://www.anthropic.com/legal/consumer-terms
- Claude Help Center「Minimum age requirement & access restriction」：https://support.claude.com/en/articles/13117299-minimum-age-requirement-access-restriction
- Google Workspace Blog（2017-06-01，Gmail 與機器學習）：https://workspace.google.com/blog/product-announcements/keeping-your-company-data-safe-new-security-updates-gmail
- Apple「About Face ID advanced technology」：https://support.apple.com/en-us/102381
- Apple「Photos & Privacy」：https://apple.com/legal/privacy/data/en/photos/
- Apple Machine Learning Research「Hey Siri」（2017-10-01）：https://machinelearning.apple.com/research/hey-siri

課表的主要參考網址是 Day of AI（https://dayofai.org/）。它的課程頁沒有三到六年級的單元，教材需要登入；本課沒有引用它的內容。
課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
''',

'01_活動規則_功能分類牆競速.md': '''# 功能分類牆競速：規則

課表的好玩機制是「競速」。這裡只有第一回合計時；說理由的時候不計時，因為說得通比說得快重要。

## 準備

- 分類牆底板（列印包第 3、4 頁上下黏好）、十張功能卡（列印包第 2 頁，編號 1–10）、兩張挑戰卡（A、B）先放旁邊。
- 計時器、口紅膠或紙膠帶（第一回合先不要黏死，用放的或用紙膠帶）。
- 競速紀錄表（列印包第 5 頁，或 `03_分類紀錄.csv`）、分類小抄卡（列印包第 1 頁）。

## 第一回合：計時分類（約 10 分鐘）

1. 十張功能卡洗牌，蓋著疊好。
2. 爸爸喊開始並計時。孩子一張一張翻開，放進四個籃子的其中一個。
3. 十張都放好就喊停，把秒數記在紀錄表。
4. 先不公布答案。

## 第二回合：說出理由（約 20 分鐘，不計時）

1. 從分類牆上一張一張拿起來，孩子用分類三問說出理由：
   「它是不是只照人寫好的固定步驟做？是不是從很多例子找規律？會不會做出新的內容？」
2. 說完可以換籃子。換了就在紀錄表註明「改放」。
3. 爸爸只問兩個問題：「你怎麼知道的？」「它可能在哪裡出錯？」
4. 十張都說完，再對照 `04_功能卡解說.md`。

## 計分

- 籃子和解說相同，或是不同但理由說得通：每張 2 分。
- 說出它可能在哪裡出錯：每張再加 1 分。
- 第一回合的秒數：最後還放錯的卡，每張加 5 秒。這是「修正後秒數」。

## 第三回合：再跑一次（約 10 分鐘）

把十張卡加上兩張挑戰卡重新洗牌，再計時一次。目標是比自己第一回合的修正後秒數快，而且放錯的更少。
挑戰卡不只一個答案，放好之後一樣要說理由。

## 結算（約 5 分鐘）

- 哪一個籃子的卡最多？為什麼生活裡機器學習這麼常見？
- 哪一張最難分？難在哪裡？
- 孩子說出結論，爸爸只追問「你怎麼知道的？」

## 常見卡關

- 孩子覺得「會動、有螢幕的都是 AI」：拿計算機和鬧鐘，問「它每次做的事有沒有不一樣？是誰決定它怎麼做的？」
- 孩子把固定規則全放進「不是 AI」：可以接受，請他說理由；再告訴他有些專家會把規則也算進 AI。
- 孩子分不出機器學習和生成式 AI：問「它是在認出、分類、挑選已經有的東西，還是做出新的東西？」
- 孩子說「AI 什麼都知道」：回到小抄卡的「AI 不是什麼」，請他說出三件事。
- 孩子只求快亂放：提醒放錯一張加 5 秒。
''',

'03_分類紀錄_填寫說明.md': '''# 分類紀錄怎麼寫

`03_分類紀錄.csv` 可以用 Numbers 或任何試算表開啟；也可以直接寫在列印包第 5 頁。

每一張功能卡寫一列：

- **我放的籃子**：固定規則、機器學習、生成式 AI、不是 AI。
- **理由**：它是怎麼做事的。可以用分類三問來寫。
- **可能在哪裡出錯**：想得到就寫，寫了加分。
- **有沒有改放**：第二回合說理由之後換了籃子，就寫原本放哪裡。
- **得分**：照活動規則計分。

表格最下面記三個數字：第一回合秒數、放錯張數、修正後秒數（每放錯一張加 5 秒）；第三回合再記一次。
紀錄裡不需要寫任何人的姓名、帳號或其他個資。
''',

'04_功能卡解說.md': '''# 功能卡解說（爸爸用，第二回合說完理由再給孩子看）

「建議的籃子」不是唯一答案。孩子放的籃子不同，但理由說得通，就算對。
特別是「固定規則」：有些專家把它算成 AI 的一種，有些不算（見 `00_爸爸先讀.md`）。

| 卡 | 功能 | 看到的樣子 | 建議的籃子 | 理由 | 可能在哪裡出錯 | 依據與限制 |
|---|---|---|---|---|---|---|
''' + ''.join(f'| {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} | {c[6]} | {c[5]} |\n' for c in CARDS) + '''
## 挑戰卡（不只一個答案）

| 卡 | 功能 | 看到的樣子 | 建議的籃子 | 理由 | 可能在哪裡出錯 | 依據與限制 |
|---|---|---|---|---|---|---|
''' + ''.join(f'| {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} | {c[6]} | {c[5]} |\n' for c in CHALLENGE) + '''
## 可以追問的問題

- 卡 1、2：如果我每天按一樣的按鍵，它會不會有一天做出不一樣的事？
- 卡 3、4：是誰教手機認得你的臉？它看過多少例子？
- 卡 5：為什麼有時候重要的信會跑到垃圾信匣？
- 卡 6：它推薦的影片，一定適合你嗎？它是怎麼猜的？
- 卡 7、8：它寫的詩、畫的圖，以前存在嗎？它寫的內容一定正確嗎？
- 卡 9、10：這裡面有沒有程式在幫忙判斷？
- 卡 10：換成「有人經過才亮」的感應燈，你會把它放到哪裡？為什麼？
''',

'05_自選功能與家庭AI約定.md': '''# 孩子獨立改造：擴充分類牆

下半場做三件事。一次只加一個功能、一條約定，才知道它有沒有用。

## 一、找一個家裡的新功能

在家裡走一圈，找一個功能卡上沒有的東西。靈感：

- 電梯的樓層按鈕、洗衣機的行程、冷氣的定時、電鍋的保溫
- 地圖 App 估算幾分鐘會到、翻譯 App、手寫輸入、相機的人像模式
- 遊戲裡的電腦對手、音樂 App 的每日推薦、掃地機器人

用一張空白功能卡寫下：功能名稱、看到的樣子、我放的籃子、理由。
不確定也沒關係，寫下「我猜是＿＿，因為＿＿」，再和爸爸一起查它的官方說明。查不到就寫「還不知道」。

## 二、替它寫一張提醒卡

- 這個功能可能在哪裡出錯？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 出錯的時候，誰會發現？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 我會怎麼檢查它？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

## 三、加一條家庭 AI 約定

選一條，或自己發明：

- 不把自己或別人的姓名、照片、住址、學校輸入 AI 工具。
- 要用生成式 AI，先問爸爸，而且爸爸在旁邊。
- AI 說的重要事情，要再查一個可靠的來源。
- AI 寫的東西，不當成自己寫的交出去。
- 聊天機器人不是人；心裡的事，找家人或朋友說。
- 覺得 AI 的回答怪怪的，就停下來問爸爸。

我的約定：

- 約定（一句話）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 它在防止什麼問題？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 這條約定什麼時候不適用？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 一個星期後回頭看：要保留、修改，還是拿掉？為什麼？＿＿＿＿＿＿＿＿

把新功能卡貼上分類牆，把約定寫在分類牆下方，請家裡每個人簽名。
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成 AI 功能分類牆（十張功能卡都有籃子，每張說得出理由）
- [ ] 不看稿說出分類三問，以及四個籃子的名字
- [ ] 不看稿說出 AI 不是的三件事：不是魔法、不是人、不是永遠正確
- [ ] 競速紀錄表有兩次的秒數和放錯張數
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 加了一個自選功能和一條家庭 AI 約定，並說明要不要保留

## 孩子教爸爸（105–115 分鐘）

請孩子當老師，爸爸當學生。建議順序：

1. 爸爸在家裡指一個功能（功能卡上沒有的）。
2. 孩子帶爸爸問分類三問，爸爸照著回答。
3. 孩子說出它該放哪個籃子和理由，爸爸故意問：「它這麼聰明，為什麼還會錯？」
4. 孩子說出一個限制或安全注意事項。
5. 孩子出一題考爸爸，例如：「聊天機器人說得很通順，就一定是對的嗎？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

1. AI 是什麼、不是什麼，是在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：分類牆拍照存成 `L010_AI功能分類牆_v01`，另存 `L010_分類紀錄_v01`、`L010_家庭AI約定_v01`，
放進 `文件/Tech Academy/L010_AI是什麼不是什麼/`，存好後再打開一次確認。紙本分類牆貼在家裡看得到的地方。
''',

'07_AI分類小抄.md': '''# L010 AI 分類小抄

## 分類三問

1. 它是不是只照著人寫好的**固定步驟**做事？
2. 它是不是看過**很多例子**，自己找出規律？
3. 它會不會**做出新的**文字、圖片或聲音？

三個都不是，它可能根本沒有用到 AI。

## 四個籃子

| 籃子 | 它怎麼做事 | 例子 |
|---|---|---|
| 固定規則 | 照人寫好的步驟，同樣的輸入每次結果都一樣 | 計算機、鬧鐘 |
| 機器學習 | 從很多例子找出規律，再判斷新的東西 | 臉部解鎖、照片整理、垃圾郵件過濾、影片推薦 |
| 生成式 AI | 預測接下來的內容，做出新的文字、圖片、聲音 | 聊天機器人、文字變圖片 |
| 不是 AI | 沒有程式在判斷 | 紙本字典、電燈開關 |

固定規則算不算 AI，專家的分法不一樣。重點是說得出它怎麼做事。

## AI 不是什麼

- **不是魔法**：是程式、資料和電腦計算。
- **不是人**：很會對話，但不是人，也沒有情緒。
- **不是永遠正確**：可能把錯的事說得很有把握。

## 三個提醒

- 重要的事，要再查一個可靠的來源。
- 不把自己或別人的姓名、照片、住址輸入 AI 工具。
- 要用生成式 AI，先問爸爸；各平臺有年齡限制。

我覺得最難分的功能：＿＿＿＿＿＿　我們家的 AI 約定：＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

SHEET_HEADER = ['功能卡', '功能', '我放的籃子', '理由', '可能在哪裡出錯', '有沒有改放', '得分']
SHEET_ROWS = ([[c[0], c[1]] for c in CARDS] + [[f'挑戰 {c[0]}', c[1]] for c in CHALLENGE] + [['自選', '']]
              + [['第一回合秒數'], ['第一回合放錯張數'], ['第一回合修正後秒數'], ['第三回合秒數'], ['第三回合放錯張數'], ['第三回合修正後秒數']])

EXTRA_CSS = '''.q{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}.q div{border:1.6pt solid #0b2540;border-radius:3mm;padding:3mm 4mm;font-size:11.5pt;height:34mm}
.q b{font-size:14pt;display:block;margin-bottom:1mm}
.bk{height:39mm;padding:3mm 5mm}.bk h3{font-size:15pt;margin:0 0 1mm}.bk p{margin:.6mm 0;font-size:11pt}.bk .eg{font-size:10pt;color:#35506b;border-top:.8pt solid #9db7cc;padding-top:1.2mm;margin-top:1.5mm}
.act{border:1.3pt solid #35a9d6;border-radius:3mm;padding:2.5mm 5mm;margin-top:4mm;font-size:11.5pt}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}
.fc{border:1.4pt dashed #0b2540;border-radius:3mm;height:45mm;padding:2.5mm 3mm;position:relative}
.fc .n{font-size:9pt;color:#fff;background:#0b2540;border-radius:1.5mm;padding:.1mm 2mm;display:inline-block}
.fc h3{font-size:13pt;margin:1.5mm 0 1.5mm;line-height:1.25}.fc p{font-size:10pt;margin:0;line-height:1.4}
.fc.ch{border-color:#c98a1b}.fc.ch .n{background:#c98a1b}
.fc.bl p{font-size:9pt;color:#4a6a88;margin:1.2mm 0 0}
.wall div{border:2pt solid #0b2540;border-radius:4mm;height:110mm;padding:3mm 5mm;margin-bottom:4mm}
.wall h3{font-size:17pt;margin:0;display:inline-block}.wall p{font-size:10pt;color:#35506b;margin:0 0 0 4mm;display:inline-block}
.wall .b1{border-color:#35a9d6}.wall .b2{border-color:#2e8b57}.wall .b3{border-color:#c98a1b}.wall .b4{border-color:#7f8c9a}
.rec{table-layout:fixed}.rec th{font-size:9.5pt;padding:1mm .8mm;text-align:center}.rec td{height:12.2mm;font-size:10pt}.rec td.no{text-align:center;font-weight:700;vertical-align:middle}.rec td.nm{font-size:9.5pt;vertical-align:middle}
.time{margin-top:4mm}.time td{height:11mm;font-size:10.5pt;vertical-align:middle}
.half{height:108mm;padding:4mm 6mm}.half p{margin:1.3mm 0;font-size:11.5pt}.half2{height:112mm;padding:4mm 6mm;margin-top:6mm}.half2 p{margin:1.3mm 0;font-size:11.5pt}'''


def html():
    pages = []
    bk = lambda name, how, eg: f'<div class="cut bk"><h3>{name}</h3><p>{how}</p><p class="eg">例如：{eg}</p></div>'
    pages.append('<h2>分類小抄卡</h2><p class="lead">沿外框剪下，放在電腦旁邊。分類的時候看它怎麼做事，不是看它叫什麼名字。</p>'
        '<div class="q"><div><b>1 固定步驟？</b>它是不是只照著人寫好的固定步驟做事？</div><div><b>2 從例子學？</b>它是不是看過很多例子，自己找出規律？</div>'
        '<div><b>3 做新內容？</b>它會不會做出新的文字、圖片或聲音？</div></div><div style="height:5mm"></div><div class="grid2">'
        + bk('固定規則', '照人寫好的步驟做，同樣的輸入，每次結果都一樣。', '計算機、鬧鐘')
        + bk('機器學習', '從很多例子裡找出規律，再判斷新的東西。', '臉部解鎖、照片整理、影片推薦')
        + bk('生成式 AI', '預測接下來的內容，做出新的文字、圖片、聲音。', '聊天機器人、文字變圖片')
        + bk('不是 AI', '沒有程式在幫忙判斷。', '紙本字典、電燈開關')
        + '</div><div class="act"><b>AI 不是什麼：</b>不是魔法（是程式、資料和計算）・不是人（很會對話，但沒有情緒）・不是永遠正確（可能把錯的事說得很有把握）。</div>'
        '<div class="act"><b>記得：</b>重要的事要再查證；不把姓名、照片、住址輸入 AI 工具；固定規則算不算 AI，專家的分法不一樣。</div>')

    card = lambda c, cls='', label='功能卡': f'<div class="fc {cls}"><span class="n">{label} {c[0]}</span><h3>{c[1]}</h3><p>{c[2]}</p></div>'
    blank = '<div class="fc bl"><span class="n">自選功能卡</span><p>功能：</p><p style="margin-top:8mm">看到的樣子：</p><p style="margin-top:9mm">我放的籃子：</p></div>'
    pages.append('<h2>功能卡</h2><p class="lead">沿虛線剪下：十張功能卡、兩張挑戰卡（不只一個答案）、四張空白卡留給自己找到的功能。</p><div class="cards">'
        + ''.join(card(c) for c in CARDS) + ''.join(card(c, 'ch', '挑戰卡') for c in CHALLENGE) + blank * 4 + '</div>')

    pages.append('<h2>作品：AI 功能分類牆（上半）</h2><p class="lead">這一頁和下一頁上下黏在一起就是分類牆。功能卡說完理由、確定了再黏上去。</p><div class="wall">'
        '<div class="b1"><h3>固定規則</h3><p>照人寫好的步驟做，同樣的輸入，每次結果都一樣</p></div>'
        '<div class="b2"><h3>機器學習</h3><p>從很多例子找規律，再判斷新的東西</p></div></div>')
    pages.append('<h2>作品：AI 功能分類牆（下半）</h2><p class="lead">名稱：L010_AI功能分類牆_v＿＿　日期：＿＿＿＿　分類員：＿＿＿＿＿＿</p><div class="wall">'
        '<div class="b3"><h3>生成式 AI</h3><p>預測接下來的內容，做出新的文字、圖片、聲音</p></div>'
        '<div class="b4"><h3>不是 AI</h3><p>沒有程式在幫忙判斷</p></div></div>')

    rows = ''.join(f'<tr><td class="no">{c[0]}</td><td class="nm">{c[1]}</td><td></td><td></td><td></td><td></td></tr>'
                   for c in CARDS + CHALLENGE + [('自選', '')])
    pages.append('<h2>競速紀錄表</h2><p class="lead">第一回合只記秒數；第二回合一張一張說理由，再填這張表。</p>'
        '<table class="rec"><tr><th style="width:7%">卡</th><th style="width:19%">功能</th><th style="width:16%">我放的籃子</th><th>理由（它怎麼做事）</th>'
        '<th style="width:21%">可能在哪裡出錯</th><th style="width:8%">得分</th></tr>' + rows + '</table>'
        '<table class="time"><tr><th style="width:22%"></th><th>秒數</th><th>放錯張數</th><th>修正後秒數（每放錯一張加 5 秒）</th></tr>'
        '<tr><td><b>第一回合</b></td><td></td><td></td><td></td></tr><tr><td><b>第三回合</b></td><td></td><td></td><td></td></tr></table>')

    pages.append('<h2>提醒卡與家庭 AI 約定卡</h2><p class="lead">上半張給自己找到的新功能；下半張沿外框剪下，寫好後貼在分類牆下面。</p>'
        '<div class="box half"><h3>我找到的新功能：提醒卡</h3>'
        '<p>功能名稱：＿＿＿＿＿＿＿＿＿＿　看到的樣子：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>我放的籃子：□ 固定規則　□ 機器學習　□ 生成式 AI　□ 不是 AI　□ 還不知道</p>'
        '<p>理由（它怎麼做事）：</p><div class="line"></div><div class="line"></div>'
        '<p>它可能在哪裡出錯？</p><div class="line"></div>'
        '<p>出錯的時候，我會怎麼檢查？</p><div class="line"></div></div>'
        '<div class="cut half2"><h3>家庭 AI 約定卡</h3>'
        '<p>我們的約定（一句話）：</p><div class="line"></div><div class="line"></div>'
        '<p>它在防止什麼問題？</p><div class="line"></div>'
        '<p>這條約定什麼時候不適用？</p><div class="line"></div>'
        '<p>一個星期後：□ 保留　□ 修改　□ 拿掉　　為什麼？＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>全家人簽名：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p></div>')
    return printpack.document('L010 AI 是什麼、不是什麼 列印包', '父子科技學院 L010｜AI 是什麼、不是什麼', pages, EXTRA_CSS)


if __name__ == '__main__':
    classroom_pack.build(
        slug='l010-what-is-ai', folder='L010_AI是什麼不是什麼', files=FILES,
        sheet=('03_分類紀錄.csv', SHEET_HEADER, SHEET_ROWS),
        pack_html=html(), pack_pdf='02_列印包_AI功能分類牆.pdf', pack_pages=6,
        pack_needles=('分類小抄卡', '功能卡 1', '功能卡 10', '挑戰卡 A', '自選功能卡', 'AI 功能分類牆（上半）', 'AI 功能分類牆（下半）', '競速紀錄表', '家庭 AI 約定卡'),
        authoring_dir=Path(__file__).resolve().parent,
        extra={'functionCards': {'count': len(CARDS), 'challenge': len(CHALLENGE), 'blank': 4,
                                 'suggestedBaskets': {b: [c[0] for c in CARDS if c[3] == b] for b in BASKETS},
                                 'ownExamplesWithoutOfficialSource': ['2', '10']},
               'needsChildAiAccount': False,
               'answersProvided': 'suggested basket, reason, failure mode and basis for 10 cards and 2 challenge cards; other reasoned answers accepted'})
