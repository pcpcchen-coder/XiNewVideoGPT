"""Build the L012 classroom pack (real, usable materials; no private data, no AI account needed).

    ./portable-runtime.sh python authoring/l012/classroom.py

The three "mock answers" are written for this lesson with planted errors; they are not output
from any AI tool. Reference facts come from the official sources listed in production/fact-check.md.
After any change here: rerun pipeline/delivery.py, then verify.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import classroom_pack  # noqa: E402
import printpack  # noqa: E402

KINDS = [('名稱', '人名、地名、書名、東西的名字'), ('數字', '多高、多少、第幾'), ('日期', '哪一年、哪一天'),
         ('引用', '它說資料來自哪本書、哪個網站'), ('說得太肯定', '「一定」「剛好」「所有」「非常確定」')]
# (tag, title, question, mock answer text, [(snippet, kind, verdict, reference fact, source)])
ANSWERS = [
 ('A', '犀牛', '世界上有幾種犀牛？牠們的角是什麼做的？',
  '世界上現存的犀牛一共有六種，分別住在非洲和亞洲。犀牛的角是骨頭做的，所以非常堅硬。白犀牛和黑犀牛都有兩支角，爪哇犀牛則有三支角。'
  '而且犀牛的視力一定非常好。根據《犀牛全知道》（星星出版社，2031 年）的統計，全世界只剩下大約 2,600 隻犀牛。',
  [('一共有六種', '數字', '錯誤', '現存的犀牛是五種：白犀牛、黑犀牛、大獨角犀、爪哇犀牛、蘇門答臘犀牛。', '國際犀牛基金會（IRF）'),
   ('住在非洲和亞洲', '名稱', '正確', '五種犀牛分布在非洲和亞洲。', 'IRF'),
   ('角是骨頭做的', '名稱', '錯誤', '犀牛角是角蛋白，和指甲、頭髮是同樣的材料。', 'IRF'),
   ('白犀牛和黑犀牛都有兩支角', '數字', '正確', '白犀牛、黑犀牛都有兩支角。', 'IRF'),
   ('爪哇犀牛則有三支角', '數字', '錯誤', '爪哇犀牛只有一支角。', 'IRF'),
   ('視力一定非常好', '說得太肯定', '錯誤', '犀牛的嗅覺和聽覺很靈敏，視力不好。', 'IRF；Save the Rhino'),
   ('《犀牛全知道》（星星出版社，2031 年）', '引用', '查不到', '這本書是這堂課編的。出版年份是未來的 2031 年，一看就有問題。', '本課編寫'),
   ('大約 2,600 隻', '數字', '錯誤', '全球大約 26,700 隻（2026 年報告）。', 'IRF《2026 State of the Rhino》；Save the Rhino')]),
 ('B', '玉山和臺灣黑熊', '台灣最高的山是哪一座？臺灣黑熊還有多少隻？',
  '台灣最高的山是玉山，主峰海拔 3,592 公尺。它位在玉山國家公園裡，這座國家公園成立於民國 84 年，是台灣的第一座國家公園。'
  '臺灣黑熊是瀕臨絕種的野生動物，胸前有 V 字形的斑紋。目前全台灣剛好有 1,000 隻臺灣黑熊，這個數字非常確定。',
  [('最高的山是玉山', '名稱', '正確', '玉山主峰是臺灣第一高峰。', '玉山國家公園管理處'),
   ('3,592 公尺', '數字', '錯誤', '玉山主峰海拔 3,952 公尺（回答把兩個數字對調了）。', '玉山國家公園管理處；行政院國情簡介'),
   ('玉山國家公園', '名稱', '正確', '玉山主峰在玉山國家公園內。', '玉山國家公園管理處'),
   ('成立於民國 84 年', '日期', '錯誤', '成立時間是民國 74 年 4 月。', '行政院國情簡介（資料來源：內政部）'),
   ('第一座國家公園', '數字', '錯誤', '玉山國家公園是我國第 2 座國家公園。', '玉山國家公園管理處'),
   ('瀕臨絕種、胸前有 V 字形的斑紋', '名稱', '正確', '臺灣黑熊是瀕臨絕種野生動物；胸前有黃白色 V 字形或新月形斑紋。', '玉山國家公園管理處'),
   ('剛好有 1,000 隻、非常確定', '說得太肯定', '錯誤', '族群數量只有估計：有的官方資料寫「約 200～600 隻」，有的寫「數百隻」，彼此還不一樣。沒有人能說「剛好」幾隻。',
    '玉山國家公園管理處；林業及自然保育署期刊')]),
 ('C', '登陸月球', '第一次有人登上月球是什麼時候？有誰去了？',
  '人類第一次登上月球是在 1979 年 7 月 20 日，這次任務叫做阿波羅 11 號。太空人阿姆斯壯、艾德林和柯林斯三個人都踏上了月球表面。'
  '月球離地球平均大約 38 萬公里，陽光從太陽照到地球大約要 8 秒鐘。到現在為止，一共有 21 個人在月球上走過，'
  '資料來源：NASA 官方網站 www.nasa.example/moon-walkers。',
  [('1979 年 7 月 20 日', '日期', '錯誤', '是 1969 年 7 月 20 日（美國東部時間；換算成台灣時間，踏上月面已經是 7 月 21 日）。', 'NASA'),
   ('阿波羅 11 號', '名稱', '正確', '任務名稱是阿波羅 11 號。', 'NASA'),
   ('三個人都踏上了月球表面', '名稱', '錯誤', '踏上月面的是阿姆斯壯和艾德林；柯林斯留在指揮艙，繞著月球飛。', 'NASA'),
   ('大約 38 萬公里', '數字', '正確', '平均距離是 384,400 公里。', 'NASA Science'),
   ('大約要 8 秒鐘', '數字', '錯誤', '大約 8 分 20 秒。', 'NASA Astrobiology'),
   ('一共有 21 個人', '數字', '錯誤', '一共 12 個人在月球上走過。', 'NASA Science'),
   ('www.nasa.example/moon-walkers', '引用', '查不到', '這個網址是這堂課編的。NASA 的網站是 nasa.gov；「.example」是保留給範例用的，打不開。', '本課編寫')]),
]
COUNTS = {a[0]: (len(a[4]), sum(1 for c in a[4] if c[2] == '錯誤'), sum(1 for c in a[4] if c[2] == '查不到')) for a in ANSWERS}
assert COUNTS == {'A': (8, 5, 1), 'B': (7, 4, 0), 'C': (7, 4, 1)}, COUNTS
for a in ANSWERS:  # every listed snippet's key words must really be in the mock answer
    for c in a[4]:
        for piece in c[0].replace('、', '|').replace('則', '|').split('|'):
            assert piece.strip() in a[3], (a[0], piece)

FACT_CARDS = [
 ('犀牛資料卡', '國際犀牛基金會（International Rhino Foundation）　rhinos.org',
  ['現存的犀牛有五種：白犀牛、黑犀牛、大獨角犀、爪哇犀牛、蘇門答臘犀牛，分布在非洲和亞洲。',
   '白犀牛、黑犀牛、蘇門答臘犀牛有兩支角；大獨角犀和爪哇犀牛只有一支。',
   '犀牛角是角蛋白，和指甲、頭髮是同樣的材料。',
   '犀牛的嗅覺和聽覺很靈敏，視力不好。',
   '2026 年的報告：全球大約 26,700 隻犀牛。']),
 ('玉山和臺灣黑熊資料卡', '玉山國家公園管理處　www.ysnp.gov.tw；行政院國情簡介　www.ey.gov.tw',
  ['玉山主峰海拔 3,952 公尺，是臺灣第一高峰。',
   '玉山國家公園是我國第 2 座國家公園，成立時間是民國 74 年 4 月。',
   '臺灣黑熊是瀕臨絕種野生動物，胸前有黃白色 V 字形或新月形斑紋。',
   '臺灣黑熊有多少隻，只有估計：有的資料寫「約 200～600 隻」，有的寫「數百隻」。']),
 ('登陸月球資料卡', '美國太空總署（NASA）　nasa.gov、science.nasa.gov',
  ['阿波羅 11 號在 1969 年 7 月 20 日（美國東部時間）降落月球。',
   '阿姆斯壯和艾德林踏上月面；柯林斯留在指揮艙，繞著月球飛。',
   '月球和地球的平均距離是 384,400 公里。',
   '一共有 12 個人在月球上走過。',
   '陽光從太陽到地球，大約要 8 分 20 秒。']),
]

FILES = {
'00_爸爸先讀.md': f'''# 父子科技學院 L012：AI 會亂講，幻覺抓錯賽（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在孩子自己圈出需要查證的地方、去查、再判定對錯。

## 這堂課要帶走什麼

- 幻覺：生成式 AI 有時會把錯的、甚至是編的內容，說得通順又有把握。
- 抓錯三步：標記、查證、判定。
- 最需要查的四種東西：名稱、數字、日期、引用；還有第五種，說得太肯定的話。
- 引用也可能是編的：要確認它真的存在、裡面真的這樣寫。
- 至少一個限制或安全注意：有附來源連結的回答也可能出錯；作業和報告的內容先查證再使用。
- 作品：**AI 回答查核表**，另有抓錯紀錄與一條自選偵探規則。

## 三則「模擬回答」是什麼

課表的任務是「請 AI 回答冷門題，孩子找出至少 3 個需驗證點」。各家 AI 工具都有年齡限制，所以這份教材先準備了三則**模擬回答**：

- 它們是這堂課編寫的，**不是任何 AI 工具的輸出**；每一則都標示了「模擬回答・故意藏了錯誤」。
- 三則一共有 {sum(v[0] for v in COUNTS.values())} 個可以查證的地方，其中 {sum(v[1] for v in COUNTS.values())} 個是錯的、{sum(v[2] for v in COUNTS.values())} 個查不到（編出來的書和網址），其餘是對的。
- 孩子要學的是找出「需要查證的地方」，不是只找錯。圈起來的地方有對有錯，查過才知道。
- 請不要把模擬回答當成資料引用，也不要讓它單獨流傳出去。

判定用的參考事實寫在 `04_模擬回答解說.md`，都取自官方來源（國際犀牛基金會、玉山國家公園管理處、行政院、NASA）。

想讓孩子看看真正的 AI 怎麼回答冷門題，請在下半場由你用**自己的帳號**操作，孩子負責找出至少三個需要查證的地方。
各家工具的年齡限制見 L011 的教材；提問時不要輸入姓名、學校、住址等個資。

## 課前準備（約 15 分鐘）

1. 列印 `02_列印包_幻覺抓錯賽.pdf`（A4，共 5 頁，單面）。第 3 頁的三張資料卡先收著，第二回合才拿出來。
2. 讀一遍 `04_模擬回答解說.md`。
3. 準備鉛筆、紅筆（判定用）、螢光筆。
4. 如果要讓孩子上網查：先在瀏覽器開好三個官方網站（rhinos.org、www.ysnp.gov.tw、science.nasa.gov），讓孩子從這三個網站裡找，不必自由搜尋。
5. 課表的課前準備是「確認兒童帳號、家庭備份與瀏覽器可用；準備不含真實個資的範例」。這堂課用不到兒童帳號。
6. 錄音只保存在家裡的私人位置，不直接公開；錄音前先說課次與主題。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：爸爸把模擬回答 A 很有自信地念一遍，問孩子「你覺得哪裡怪怪的？」 | 念得越肯定越好；先不說答案 |
| 10–25 | 看影片，認識幻覺、四種要查的東西和抓錯三步；讀小抄卡 | 回答問題；不知道的就說「我們等一下查」 |
| 25–65 | 幻覺抓錯賽（規則見 `01`） | 當委託人：追問「你怎麼知道？」「去哪裡查的？」 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：設計自己的 AI 回答查核表，加一條偵探規則；可以請爸爸問一題冷門題 | 只在孩子開口時協助；操作自己的帳號 |
| 105–115 | 角色互換：孩子帶爸爸查證一則新的回答 | 當學生，故意說「它有附來源耶，應該是對的吧？」 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 問四個錄音問題 |

## 幾個觀念的依據與限制

- **幻覺**：美國國家標準暨技術研究院（NIST）的說法是，生成式 AI 會產生並有自信地呈現錯誤或虛假的內容，俗稱 hallucination。
  Google 的中文說明寫「Gemini 可能會產生幻覺，將不準確的資訊當做事實」。教育部的注意事項 2.1 沒有用「幻覺」這個詞，它寫的是偏誤、錯誤、虛構。
- **為什麼會這樣**：NIST 寫，這是生成模型的設計造成的自然結果，它們預測句子裡的下一個字。MIT Sloan 的教學資源寫，它的目標是產生看似合理的內容，不是驗證真假。
- **有附來源也會錯**：Google 搜尋的 AI 摘要說明寫「務必多方查證重要資訊」，並寫無法確保 AI 摘要內容皆正確無誤。
  OpenAI 的說明提到搜尋結果與引用可能不完整、過時或不正確（這一句只有擷取工具的摘要，沒有逐字確認）。
- **引用是編的**：2023 年 6 月 22 日，美國紐約南區聯邦地方法院在 Mata v. Avianca 一案的制裁命令裡寫，兩位律師和事務所提交了由 ChatGPT 產生、並不存在的判決與假引文；
  六個判決都不存在；三方**共同**被處以一筆 5,000 美元的罰款（不是每人 5,000）。命令也寫，使用可靠的 AI 工具協助本身沒有不當；問題在沒有查證。
- **「你確定嗎？」**：同一份命令記載，律師回頭問 ChatGPT 那個案例是不是真的，它回答是真的。這只是一個 2023 年的例子，不能說再問一次一定沒用；
  但也沒有任何廠商說再問一次就會更正。所以本課教的是：回頭問它不算查證。
- **怎麼查**：教育部注意事項寫，不能全盤接受生成的內容，需結合其他可靠來源的知識進行查證；有疑慮向老師或家長請教；不可以直接將生成內容作為作業或報告的原始答案。
  教育部數位素養教案寫，統計數據、名言、法條、專有名詞應至原始文件或官方網站核實。
- **估計值**：臺灣黑熊有多少隻，玉山國家公園管理處寫「約200~600隻」，林業期刊寫「數百隻」。官方資料彼此不同，正好用來說明：真實世界的數字常常是估計，說得太精確、太肯定的回答反而要小心。
- 健康、金錢、安全的事要問大人，以及發現錯誤不要轉傳，是本課的建議，沒有逐字的來源。

## 來源（查核日 2026-10-08）

- 教育部「中小學使用『生成式人工智慧』注意事項 2.1」（學生版，115 年 2 月 11 日核定；讀的是師大附中國中部網站轉載的 PDF）
- 教育部 中小學數位素養教育資源網 教案【AI的練習曲】：https://eliteracy.edu.tw/Download.ashx?id=1817
- NIST AI 600-1「Generative Artificial Intelligence Profile」（2024-07）：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- IBM「What Are AI Hallucinations?」：https://www.ibm.com/think/topics/ai-hallucinations
- MIT Sloan「When AI Gets It Wrong: Addressing AI Hallucinations and Bias」：https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/
- Google Gemini 說明「瞭解 Gemini 應用程式的回覆」：https://support.google.com/gemini/answer/16279220?hl=zh-Hant
- Google 搜尋說明（AI 摘要）：https://support.google.com/websearch/answer/14901683?hl=zh-Hant
- Mata v. Avianca, Inc. 制裁命令（2023-06-22；CourtListener 存檔）：https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_3.pdf
- International Rhino Foundation「State of the Rhino」：https://rhinos.org/about-rhinos/state-of-the-rhino/
- Save the Rhino「Rhino population figures」：https://www.savetherhino.org/rhino-info/population-figures/
- 玉山國家公園管理處（地形地質、願景與沿革、臺灣黑熊科普）：https://www.ysnp.gov.tw/
- 行政院國情簡介「國家公園簡介」：https://www.ey.gov.tw/state/4447F4A951A1EC45/dc08391a-c57c-4cf7-af9a-cc0d9e4ebb1c
- NASA Science「Moon Facts」「Moon Walkers」：https://science.nasa.gov/moon/facts/ 、https://science.nasa.gov/moon/moon-walkers/
- NASA「50 Years Ago: Apollo Astronauts Land, Take First Steps on Moon」：https://www.nasa.gov/centers-and-facilities/kennedy/50-years-ago-apollo-astronauts-land-take-first-steps-on-moon/
- NASA Astrobiology「More Quick Facts」：https://astrobiology.nasa.gov/quick-facts/more-quick-facts/

課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
''',

'01_活動規則_幻覺抓錯賽.md': '''# 幻覺抓錯賽：規則

課表的好玩機制是「偵探辦案」。孩子是**抓錯偵探**，爸爸是**委託人**。三則模擬回答是三個案子。

## 準備

- 三則模擬回答（列印包第 2 頁）。它們是這堂課編寫的，裡面故意藏了錯誤。
- 抓錯紀錄表（列印包第 4 頁，或 `03_抓錯紀錄.csv`）、鉛筆、紅筆。
- 查核小抄卡（列印包第 1 頁）放在旁邊；資料卡（第 3 頁）先由爸爸收著。

## 第一回合：標記（一則約 5 分鐘）

1. 孩子把回答念一遍。
2. 用鉛筆把**需要查證的地方**圈起來：名稱、數字、日期、引用，還有說得太肯定的話。每一則**至少圈三個**。
3. 在紀錄表寫下圈了哪一句、它是哪一種。
4. 這一回合不可以看資料卡，也先不說對錯。

## 第二回合：查證和判定（一則約 7 分鐘）

1. 爸爸拿出資料卡。孩子對照資料卡，或是和爸爸一起到官方網站查。
2. 每一個圈起來的地方，用紅筆寫下判定：**正確**、**錯誤**，或是**查不到**。
3. 判定「錯誤」的，把查到的正確說法寫在旁邊。
4. 委託人只問兩個問題：「你去哪裡查的？」「如果只看回答，你看得出來它錯了嗎？」

三個案子辦完，對照 `04_模擬回答解說.md`。

## 計分

- 每圈出一個需要查證的地方，並寫對它是哪一種：1 分。
- 每一個判定和解說相同：2 分。
- 判定「錯誤」而且寫出正確的說法：再加 1 分。
- 圈了對的句子不扣分。**偵探本來就要查過才知道。**
- 找到解說沒有列的地方，而且說得出為什麼要查：一樣給 1 分。

## 加碼（有時間再玩）

- **換你出題**：孩子把資料卡上的一句話改錯，念給爸爸聽，看爸爸抓不抓得到。只能改資料卡上有的事實。
- **真的問一題**：由爸爸用自己的帳號問一題冷門的問題（例如爸爸很熟的專業、家附近一座山的高度），
  孩子找出至少三個需要查證的地方，爸爸負責查。不要輸入任何個資。

## 結算（約 5 分鐘）

- 哪一種錯最多？哪一種最難看出來？
- 有沒有哪一句，你本來覺得是對的，查了才知道是錯的？
- 兩個編出來的引用（一本書、一個網址），你是怎麼發現的？

## 常見卡關

- 孩子只圈數字：提醒他還有名稱、日期和引用；第五種是「說得太肯定」。
- 孩子覺得「看起來很像真的」：這就是今天的重點。回答寫得通順，不代表內容正確。
- 孩子查到資料卡和回答不一樣，卻不敢判定錯誤：問他「哪一邊有寫清楚是誰說的？」
- 孩子問「那資料卡就一定對嗎？」：很好的問題。資料卡是從官方網站整理的，上面有寫出處；有時間就一起打開網址，看原始頁面是不是真的這樣寫。
''',

'03_抓錯紀錄_填寫說明.md': '''# 抓錯紀錄怎麼寫

`03_抓錯紀錄.csv` 可以用 Numbers 或任何試算表開啟；也可以直接寫在列印包第 4 頁。

每圈一個地方寫一列：

- **回答**：A、B 或 C。
- **我圈的那句話**：照抄回答裡的字，短短的就好。
- **哪一種**：名稱、數字、日期、引用、說得太肯定。
- **去哪裡查**：資料卡、哪一個網站，或是問了誰。
- **判定**：正確、錯誤、查不到。
- **正確的說法**：判定錯誤才寫。
- **得分**：照活動規則計分。

每一則回答至少寫三列。紀錄裡不需要寫任何人的姓名、帳號或其他個資。
''',

'04_模擬回答解說.md': '''# 模擬回答解說（爸爸用，第二回合判定完再給孩子看）

三則回答都是這堂課編寫的，不是任何 AI 工具的輸出。下面列出每一則可以查證的地方、建議的判定和依據。
孩子圈了表上沒有的地方，而且說得出為什麼要查，也給分。

''' + ''.join(
    f'## 模擬回答 {a[0]}：{a[1]}\n\n問題：{a[2]}\n\n> {a[3]}\n\n'
    f'可以查證的地方 {COUNTS[a[0]][0]} 個：錯誤 {COUNTS[a[0]][1]}、查不到 {COUNTS[a[0]][2]}、正確 {COUNTS[a[0]][0] - COUNTS[a[0]][1] - COUNTS[a[0]][2]}。\n\n'
    '| 回答裡寫的 | 哪一種 | 判定 | 查到的說法 | 依據 |\n|---|---|---|---|---|\n'
    + ''.join(f'| {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} |\n' for c in a[4]) + '\n' for a in ANSWERS) + '''## 可以追問的問題

- 回答 A：書名和出版社看起來很正常，你是怎麼發現這本書有問題的？如果年份寫的是 2021 年，你會怎麼查？
- 回答 B：3,592 和 3,952 只差在兩個數字對調，為什麼這種錯特別難發現？
- 回答 B：臺灣黑熊的數量，兩份官方資料寫的不一樣。這代表有一份是錯的嗎？
- 回答 C：網址裡有 nasa 四個字，為什麼還不能相信？
- 三則都問：如果沒有資料卡，你會去哪裡查？

## 給爸爸的提醒

- 這三則的錯誤是故意放的，而且放得比較明顯。真正的 AI 回答，錯誤可能只有一個，也可能藏在很有道理的句子裡。
- 「查不到」和「錯誤」不一樣。查不到的東西，先不要當成真的，也不要急著說它一定是假的。
- 參考事實的查核日是 2026-10-08。犀牛數量、黑熊數量這類數字會更新；以後再用這份教材，請先看一下來源有沒有變。
''',

'05_自選偵探規則.md': '''# 孩子獨立改造：我的 AI 回答查核表

下半場做三件事。

## 一、設計自己的查核表

在列印包第 5 頁的空白表格上，自己決定欄位。至少要有這四欄：

- 哪一句話
- 它是哪一種（名稱、數字、日期、引用、說得太肯定）
- 去哪裡查
- 查到的結果（正確、錯誤、查不到）

可以再加自己的欄位，例如「有多重要」「誰幫我查的」「下次要注意什麼」。

## 二、加一條偵探規則

選一條，或自己發明。一次只加一條，才知道它有沒有用。

- 只要是數字，就查兩個地方。
- 看到書名或網址，先確認它真的存在。
- 看到「一定」「所有」「從來沒有」，就多看一眼。
- 查不到的，寫「查不到」，不寫「應該是對的」。
- 要寫進作業的，全部查過才能用。
- 查到不一樣的說法，兩邊都記下來，再問爸爸。

我的規則：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

用一則模擬回答測試：加了這條規則之後，有沒有多抓到什麼？這條規則什麼時候不需要？

## 三、（可以不做）請爸爸問一題冷門題

由爸爸用自己的帳號問，孩子不操作。題目不要有個資。孩子用自己的查核表，找出至少三個需要查證的地方；爸爸幫忙查。
查完之後說一說：真正的回答，和三則模擬回答比起來，錯誤比較多還是比較少？比較好抓還是比較難抓？
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成 AI 回答查核表（欄位自己設計，至少四欄）
- [ ] 不看稿說出抓錯三步：標記、查證、判定
- [ ] 不看稿說出最需要查的四種東西：名稱、數字、日期、引用
- [ ] 抓錯紀錄表三則回答各至少三列，每一列都有判定
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 測試過一條自選偵探規則，並說明要不要保留

## 孩子教爸爸（105–115 分鐘）

請孩子當老師，爸爸當學生。建議順序：

1. 爸爸拿出一則新的回答（加碼回合真的問到的，或是孩子把資料卡改錯出的題）。
2. 孩子帶爸爸做一次：標記、查證、判定。
3. 爸爸故意說：「它有附來源耶，應該是對的吧？」孩子說明為什麼還是要查。
4. 孩子說出一個限制或安全注意事項。
5. 孩子出一題考爸爸，例如：「查不到的東西，可以寫進報告嗎？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

1. 幻覺抓錯賽，是在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：查核表拍照存成 `L012_AI回答查核表_v01`，另存 `L012_抓錯紀錄_v01`，
放進 `文件/Tech Academy/L012_AI會亂講_幻覺抓錯賽/`，存好後再打開一次確認。
三則模擬回答不要單獨存成檔案流傳；要留就連同「模擬回答・故意藏了錯誤」的標示一起留。
''',

'07_查核小抄.md': '''# L012 查核小抄

## 抓錯三步

1. **標記**：把需要查證的地方圈起來。
2. **查證**：到可靠的來源去找。
3. **判定**：正確、錯誤，或是查不到。

## 最需要查的東西

| 種類 | 找什麼 |
|---|---|
''' + ''.join(f'| {k[0]} | {k[1]} |\n' for k in KINDS) + '''
## 怎麼查

- 找**原始的來源**：官方網站、它說的那本書。
- 再找**第二個**可靠的來源，看兩邊說的一不一樣。
- 查不到或看不懂，問爸爸或老師。

## 看到引用，確認兩件事

1. 它真的存在嗎？
2. 裡面真的這樣寫嗎？

## 四個提醒

- 寫得通順、說得有把握，不代表內容正確。
- 有附來源連結的回答，也可能是錯的。
- 回頭問它「你確定嗎」，不算查證。
- 查不到的，先不要當成真的。

我最容易漏掉的一種：＿＿＿＿＿＿　我的偵探規則：＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

SHEET_HEADER = ['回答', '我圈的那句話', '哪一種', '去哪裡查', '判定', '正確的說法', '得分']
SHEET_ROWS = [[a[0]] for a in ANSWERS for _ in range(3)] + [['加碼：爸爸問的冷門題'], ['加碼：爸爸問的冷門題'], ['加碼：爸爸問的冷門題'], ['自選偵探規則測試']]

EXTRA_CSS = '''.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin:0 0 5mm}.steps div{border:1.6pt solid #0b2540;border-radius:3mm;padding:2.5mm 4mm;font-size:11pt}.steps b{font-size:14pt;display:block}
.kd{height:27mm;padding:3mm 5mm}.kd h3{font-size:15pt;margin:0 0 .5mm}.kd p{margin:.6mm 0;font-size:11pt}
.act{border:1.3pt solid #35a9d6;border-radius:3mm;padding:2.5mm 5mm;margin-top:4mm;font-size:11pt}
.mock{border:1.6pt solid #0b2540;border-radius:3mm;padding:3mm 5mm;margin-bottom:4mm}.mock h3{font-size:13pt;margin:0}
.mock .q{font-size:11pt;margin:1.2mm 0 1.5mm;color:#35506b}.mock .a{font-size:12.5pt;line-height:2.05;margin:0;border:.8pt solid #9db7cc;border-radius:2mm;padding:1.5mm 4mm;background:#f6fafd}
.fake{display:inline-block;font-size:9pt;font-weight:400;color:#fff;background:#0b2540;border-radius:1.5mm;padding:.2mm 2mm;margin-left:2mm;vertical-align:middle}
.fc{padding:3.5mm 6mm;margin-bottom:5mm}.fc h3{font-size:14pt;margin:0}.fc .src{font-size:9.5pt;color:#35506b;margin:.6mm 0 1.5mm}.fc li{font-size:11.5pt;margin:.8mm 0}.fc ul{margin:0;padding-left:5mm}
.rec{table-layout:fixed}.rec th{font-size:9.5pt;padding:1mm .8mm;text-align:center}.rec td{height:15.5mm;font-size:10pt}.rec td.no{text-align:center;font-weight:700;vertical-align:middle}
.own{table-layout:fixed}.own th{height:14mm;font-size:9pt;color:#7f9bb3;font-weight:400;vertical-align:top}.own td{height:13mm}
.rule{height:84mm;padding:4mm 6mm;margin-top:5mm}.rule p{margin:1.2mm 0;font-size:11.5pt}'''


def html():
    pages = []
    kd = lambda k: f'<div class="cut kd"><h3>{k[0]}</h3><p>{k[1]}</p></div>'
    pages.append('<h2>查核小抄卡</h2><p class="lead">沿外框剪下，放在電腦旁邊。回答寫得通順、說得有把握，不代表內容正確。</p>'
        '<div class="steps"><div><b>1 標記</b>把需要查證的地方圈起來</div><div><b>2 查證</b>到可靠的來源去找</div><div><b>3 判定</b>正確、錯誤，或是查不到</div></div>'
        '<div class="grid2">' + ''.join(kd(k) for k in KINDS[:4]) + '</div>'
        f'<div class="cut kd" style="height:auto;margin-top:6mm"><h3>第五種：{KINDS[4][0]}</h3><p>{KINDS[4][1]}。真實世界的數字，常常只是估計。</p></div>'
        '<div class="act"><b>怎麼查：</b>找原始的來源（官方網站、它說的那本書）・再找第二個可靠的來源・查不到就問爸爸或老師。<br>'
        '<b>看到引用：</b>它真的存在嗎？裡面真的這樣寫嗎？</div>'
        '<div class="act"><b>記得：</b>有附來源連結的回答也可能是錯的；回頭問它「你確定嗎」不算查證；查不到的，先不要當成真的。</div>')

    mock = lambda a: (f'<div class="mock"><h3>模擬回答 {a[0]}：{a[1]}<span class="fake">模擬回答・這堂課編寫・故意藏了錯誤</span></h3>'
                      f'<p class="q">問題：{a[2]}</p><p class="a">{a[3]}</p></div>')
    pages.append('<h2>三則模擬回答</h2><p class="lead">這三則不是真的 AI 寫的。把需要查證的地方圈起來，每一則至少圈三個。</p>' + ''.join(mock(a) for a in ANSWERS))

    card = lambda c: (f'<div class="cut fc"><h3>{c[0]}</h3><p class="src">出處：{c[1]}</p><ul>' + ''.join(f'<li>{x}</li>' for x in c[2]) + '</ul></div>')
    pages.append('<h2>查證資料卡</h2><p class="lead">第二回合才拿出來。內容整理自官方網站（查核日 2026-10-08）；有時間就打開網址，看原始頁面是不是真的這樣寫。</p>'
                 + ''.join(card(c) for c in FACT_CARDS))

    rows = ''.join(f'<tr><td class="no">{a[0]}</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>' for a in ANSWERS for _ in range(4))
    pages.append('<h2>抓錯紀錄表</h2><p class="lead">每圈一個地方寫一列，每一則至少三列。判定寫：正確、錯誤、查不到。</p>'
        '<table class="rec"><tr><th style="width:7%">回答</th><th style="width:22%">我圈的那句話</th><th style="width:12%">哪一種</th><th style="width:15%">去哪裡查</th>'
        '<th style="width:11%">判定</th><th>正確的說法</th><th style="width:7%">得分</th></tr>' + rows + '</table>'
        '<p class="note" style="margin:3mm 0 0">圈出並寫對種類 1 分；判定和解說相同 2 分；判定錯誤並寫出正確說法再加 1 分。圈了對的句子不扣分。</p>')

    own_rows = ''.join('<tr>' + '<td></td>' * 5 + '</tr>' for _ in range(8))
    pages.append('<h2>作品：AI 回答查核表</h2><p class="lead">欄位由你決定，寫在最上面一列。至少要有：哪一句話、哪一種、去哪裡查、查到的結果。</p>'
        '<table class="own"><tr><th>欄位一</th><th>欄位二</th><th>欄位三</th><th>欄位四</th><th>我自己加的欄位</th></tr>' + own_rows + '</table>'
        '<p class="note" style="margin:2mm 0 0">名稱：L012_AI回答查核表_v＿＿　日期：＿＿＿＿　偵探代號：＿＿＿＿</p>'
        '<div class="cut rule"><h3>我的偵探規則</h3>'
        '<p>規則（一句話）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>它在對付哪一種：□ 名稱　□ 數字　□ 日期　□ 引用　□ 說得太肯定</p>'
        '<p>用一則模擬回答測試，有沒有多抓到什麼？</p><div class="line"></div>'
        '<p>這條規則什麼時候不需要？</p><div class="line"></div>'
        '<p>□ 保留　□ 修改　□ 拿掉　　為什麼？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p></div>')
    return printpack.document('L012 AI 會亂講：幻覺抓錯賽 列印包', '父子科技學院 L012｜AI 會亂講：幻覺抓錯賽', pages, EXTRA_CSS)


if __name__ == '__main__':
    classroom_pack.build(
        slug='l012-ai-hallucination', folder='L012_AI會亂講_幻覺抓錯賽', files=FILES,
        sheet=('03_抓錯紀錄.csv', SHEET_HEADER, SHEET_ROWS),
        pack_html=html(), pack_pdf='02_列印包_幻覺抓錯賽.pdf', pack_pages=5,
        pack_needles=('查核小抄卡', '模擬回答 A', '模擬回答 C', '故意藏了錯誤', '查證資料卡', '抓錯紀錄表', 'AI 回答查核表', '我的偵探規則'),
        authoring_dir=Path(__file__).resolve().parent,
        extra={'mockAnswers': {'count': len(ANSWERS), 'writtenForLesson': True, 'notOutputOfAnyAiTool': True, 'labelledOnEveryAnswer': True,
                               'checkablePoints': {k: v[0] for k, v in COUNTS.items()}, 'plantedErrors': {k: v[1] for k, v in COUNTS.items()},
                               'inventedCitations': {k: v[2] for k, v in COUNTS.items()},
                               'inventedCitationMarkers': 'future publication year 2031; reserved .example domain'},
               'referenceFactsFrom': 'IRF, Save the Rhino, 玉山國家公園管理處, 行政院, NASA (see production/fact-check.md)',
               'needsChildAiAccount': False,
               'answersProvided': 'verdict, reference fact and source for each checkable point; other reasoned points accepted'})
