"""Build the L011 classroom pack (real, usable materials; no private data, no AI account needed).

    ./portable-runtime.sh python authoring/l011/classroom.py

The role play has the father act as a literal-minded robot, so the child practises prompt
writing on paper. After any change here: rerun pipeline/delivery.py, then verify.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import classroom_pack  # noqa: E402
import printpack  # noqa: E402

BOXES = [('任務', '要它做什麼？', '寫一張科普卡，告訴我機器人是什麼'),
         ('背景', '給誰看？用在哪裡？', '給國小三年級的同學看'),
         ('限制', '幾句話？不要什麼？', '只要三個小知識，每個一句話，不用太難的詞'),
         ('格式', '答案排成什麼樣子？', '排成卡片：標題、三點、最後一個小問題')]
# (round, what is added, prompt so far, how the literal robot answers, what the child should notice)
ROUNDS = [
 ('0', '什麼都還沒加', '介紹機器人',
  '（機器人隨便猜）機器人。有很多種。',
  '只有五個字，機器人不知道要寫多少、寫給誰看，所以隨便交差。也可以反過來寫一大段很難的話。'),
 ('1', '任務', '請寫一張科普卡，告訴我機器人是什麼。',
  '機器人是可以用來做事的機器。有些機器人可以自己工作，有些一定要有人告訴它怎麼做。機器人的用途很多，例如探索其他星球的太空船和探測車也是機器人，人們用電腦傳送指令給它們，它們再照著做……（故意寫成一長段，而且不分段）',
  '知道要做什麼了，但是不知道給誰看，所以寫得又長又擠。'),
 ('2', '背景', '請寫一張科普卡，告訴我機器人是什麼。這張卡片是給國小三年級的同學看的。',
  '機器人是可以幫人做事的機器。有的機器人可以自己工作，有的要有人告訴它怎麼做。到火星探險的探測車也是機器人。人用電腦把指令傳給它，它再照著做。（句子變簡單了，但是還是一整段）',
  '用詞變簡單了。可是沒有說要幾句、排成什麼樣子，所以還是一整段。'),
 ('3', '限制', '（接上一輪）只要三個小知識，每個一句話，不要用太難的詞。',
  '機器人是可以幫人做事的機器。有的機器人自己工作，有的要人告訴它怎麼做。到火星探險的探測車也是機器人。',
  '變短了，剛好三句。但是看起來還不像一張卡片。'),
 ('4', '格式', '（接上一輪）請排成一張卡片：最上面是標題，中間是三點，最後加一個小問題。',
  '【機器人是什麼？】　1. 機器人是可以幫人做事的機器。　2. 有的機器人自己工作，有的要人告訴它怎麼做。　3. 到火星探險的探測車也是機器人。　小問題：你家裡有機器人嗎？它是自己工作，還是要人告訴它怎麼做？',
  '四格都有了，機器人做出一張可以用的兒童科普卡。'),
]
VAGUE = ['介紹恐龍', '寫一個故事', '為什麼會下雨', '幫我想生日卡片', '介紹台灣', '教我摺紙飛機', '寫一首詩', '介紹犀牛']
assert len(ROUNDS) == 5 and len(VAGUE) == 8

FULL_PROMPT = ('請寫一張科普卡，告訴我機器人是什麼。這張卡片是給國小三年級的同學看的。'
               '只要三個小知識，每個一句話，不要用太難的詞。請排成一張卡片：最上面是標題，中間是三點，最後加一個小問題。')

FILES = {
'00_爸爸先讀.md': f'''# 父子科技學院 L011：第一個好提示詞（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在孩子自己寫提示詞、看「機器人」照字面做出什麼、再一格一格補上去。

## 這堂課要帶走什麼

- 提示詞：你交代給生成式 AI 的話。它不會讀心，你沒寫的，它只能猜。
- 三個步驟：寫、試、改。提示詞通常要來回改幾次。
- 四個格子：任務（要它做什麼）、背景（給誰看、用在哪）、限制（幾句話、不要什麼）、格式（答案排成什麼樣）。
- 一輪只加一格，才看得出哪一格有用。
- 至少一個限制或安全注意：提示詞寫得再清楚，答案還是可能出錯；不把個資寫進去。
- 作品：**Prompt 四格卡**，另有四輪紀錄、一格自選規則與一條使用約定。

## 這堂課的角色扮演：你來當機器人

課表的好玩機制是角色扮演。做法是：**孩子寫提示詞，爸爸扮演一台只會照字面做事的機器人**，把「答案」寫在紙上。
這樣孩子不需要登入任何 AI 工具，就能看出少寫一格，答案會差多少。機器人怎麼演，寫在 `04_機器人示範與解說.md`。

想讓孩子看看真正的 AI 怎麼回答，請在四輪玩完之後，由你用**自己的帳號**操作，把最後一版提示詞貼進去，孩子在旁邊出主意。
提示詞裡不要有姓名、學校、住址、照片等個資。各家工具的年齡限制：

- 教育部「中小學使用『生成式人工智慧』注意事項 2.1」：學生應遵守各平臺註冊年齡限制；在校由教師引導，非在校使用請家長陪伴。它沒有寫出年齡數字。
- Claude：Anthropic 的說明寫，消費者產品僅供 18 歲以上使用。
- Gemini：Google 的說明寫，個人或學校帳號須年滿 13 歲（或所在國家適用的年齡）。Google 關於受監護兒童帳號的幾個頁面說法不一致，台灣的情形這次沒有查核。
- Copilot：Microsoft 的條款寫，至少 13 歲，依各國法律可能更高。
- ChatGPT：條款寫須年滿 13 歲，未滿 18 歲需家長或監護人同意。這一條只有擷取工具的摘要，沒有逐字確認，請以官方頁面為準。

## 課前準備（約 15 分鐘）

1. 列印 `02_列印包_Prompt四格卡.pdf`（A4，共 5 頁，單面）。第 1 頁的小抄卡和守則卡可以剪下來；第 5 頁的題目卡剪開。
2. 讀一遍 `04_機器人示範與解說.md`，練習一次「照字面回答」。重點是**不要幫孩子把話補完**。
3. 準備鉛筆、橡皮擦、計時器（每一輪機器人作答限時兩分鐘，節奏比較好）。
4. 課表的課前準備是「確認兒童帳號、家庭備份與瀏覽器可用；準備不含真實個資的範例」。這堂課用不到兒童帳號；
   如果最後要用真的工具試，先確認你自己的帳號可以登入。
5. 錄音只保存在家裡的私人位置，不直接公開；錄音前先說課次與主題。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：孩子只說「介紹機器人」，爸爸當機器人照字面回答（第 0 輪） | 故意答得很敷衍，問孩子「這是你要的嗎？」 |
| 10–25 | 看影片，認識三個步驟和四個格子；讀小抄卡 | 回答問題；提醒這四格是這堂課的整理 |
| 25–65 | 四輪提示詞改造賽（規則見 `01`） | 當機器人：只做寫到的事、沒寫到的亂猜、不可以反問 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：換一個主題完成自己的 Prompt 四格卡，加一格自選規則，寫一條使用約定 | 只在孩子開口時協助 |
| 105–115 | 角色互換：孩子教爸爸把一句模糊的話改清楚 | 抽一張題目卡，故意只補一格，讓孩子指出還缺什麼 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 問四個錄音問題，一起檢查卡片上沒有個資 |

## 「四個格子」的依據與限制

「任務、背景、限制、格式」是課表的說法，也是這堂課的整理，**不是任何一家公司的官方公式**。各家的說法是：

| 來源 | 它列的項目 |
|---|---|
| OpenAI Academy「Prompting」（課表的參考網址，寫給上班族） | 說清楚任務、提供有用的背景、描述理想的輸出 |
| OpenAI 家長指南「ChatGPT at home」 | Task、Context、Output；Context 一列提到 audience 與 constraints |
| Google Workspace「How to write effective prompts」 | Persona、Task、Context、Format；並說不必每次都用齊 |
| Microsoft「Get started writing prompts in Microsoft Copilot」 | Goal、Context、Source、Expectations；並說只有清楚的目標是必要的 |
| Anthropic「Prompting best practices」（開發者文件） | 清楚直接、提供背景、善用範例、指定輸出格式與限制、給角色 |

對照起來：任務、背景、格式三格各家都有；「限制」沒有任何一家單獨列成一項。Google 的 Persona（要它扮演誰）和 Microsoft 的 Source（要它參考什麼）不在這四格裡，
孩子的「自選規則」可以拿這兩項來用。

用詞：這堂課照課表說「提示詞」。教育部的文件寫的是「提示（Prompt）」或「提問」。

## 幾個觀念的依據

- **來回修改**：OpenAI Academy 寫，第一次的答案不太對，就在對話中補充或調整，不必從頭開始。Microsoft 寫，要有來回對話的心理準備。
- **同一句話，答案可能不同**：教育部《中小學數位教學指引 3.0 版》寫，「同樣的提示（Prompt）可能會有不同的結果」。Microsoft 也這樣寫。
- **寫清楚有用，但不保證正確**：Anthropic 寫，你說得越精確，結果越好；同一家的條款也寫，輸出即使看起來很詳細也可能不正確。
  OpenAI Academy 寫，沒有唯一「完美」的寫法。沒有任何一家說好的提示詞能保證答案正確。
- **個資**：教育部注意事項（學生版）寫，不可以將自己或他人的姓名、照片、聯絡方式、住址、學號等個人資料，或家庭、學校的機密資訊輸入生成式 AI 工具。
- **用了要說**：同一份文件寫，完成作業或報告時如依老師或學校規定使用，應依規定註明所使用的工具及用途，不得將生成內容直接當作自己原創作品繳交。
- **示範科普卡的內容**取自 NASA 給幼兒園到四年級學生的「What Is Robotics?」：機器人是可以用來做事的機器；有些能自己工作，有些一定要有人告訴它怎麼做；
  探索火星的探測車是機器人。那一頁是 2009 年的，本課只用其中不會過時的句子。

## 來源（查核日 2026-10-08）

- 教育部「中小學使用『生成式人工智慧』注意事項 2.1」（學生版，115 年 2 月 11 日核定；讀的是師大附中國中部網站轉載的 PDF）
- 教育部《中小學數位教學指引 3.0 版》（2025 年 1 月；讀的是學校網站轉載的 PDF）
- 教育部 中小學數位素養教育資源網 手冊《你不可不知的生成式AI 國小高年級學生版》：https://eliteracy.edu.tw/Handbooks.aspx
- OpenAI Academy「Prompting」：https://academy.openai.com/public/clubs/work-users-ynjqu/resources/prompting
- OpenAI「ChatGPT at home」：https://cdn.openai.com/pdf/chatgpt-at-home.pdf
- Google Workspace「How to write effective prompts」：https://workspace.google.com/resources/ai/writing-effective-prompts/
- Microsoft Support「Get started writing prompts in Microsoft Copilot」：https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-writing-prompts-in-microsoft-365-copilot
- Anthropic「Prompting best practices」：https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Google Be Internet Awesome「Understanding AI: Foundational AI literacy for Grades 2nd-8th」：https://services.google.com/fh/files/misc/bia_ai-literacy-guide_en.pdf
- Anthropic「Consumer Terms of Service」：https://www.anthropic.com/legal/consumer-terms
- Claude Help Center「Age assurance on Claude」：https://support.claude.com/en/articles/15171100-age-assurance-on-claude
- Google「What you need to sign in to Gemini Apps」：https://support.google.com/gemini/answer/13278668?hl=en
- Microsoft「Copilot Terms of Use」：https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse
- NASA「What Is Robotics? (Grades K-4)」：https://www.nasa.gov/learning-resources/for-kids-and-students/what-is-robotics-grades-k-4/

課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
''',

'01_活動規則_四輪提示詞改造賽.md': '''# 四輪提示詞改造賽：規則

孩子是**提示詞工程師**，爸爸是**只會照字面做事的機器人**。目標：把「介紹機器人」這五個字，改成能做出兒童科普卡的提示詞。

## 準備

- 機器人守則卡與四格小抄卡（列印包第 1 頁）。
- 四輪紀錄表（列印包第 2 頁，或 `03_四輪紀錄.csv`）、機器人回答紙（列印包第 3 頁）、鉛筆、計時器。

## 機器人守則（爸爸要守，孩子可以抓犯規）

1. **只做提示詞寫到的事。** 沒寫要幾句，就自己決定；沒寫給誰看，就不管對方看不看得懂。
2. **沒寫到的，就隨便猜一個。** 而且每次可以猜得不一樣。
3. **不可以反問。** 不能問「你要給誰看？」，也不能用表情暗示。

孩子抓到機器人犯規（偷偷幫忙補了沒寫的東西），這一輪機器人要再答一次。

## 第一回合：機器人上場（約 25 分鐘）

1. **第 0 輪**：孩子只寫「介紹機器人」。機器人在回答紙上作答（限時兩分鐘）。一起看：這是你要的嗎？缺了什麼？
2. **第 1 輪：加任務。** 孩子在紀錄表寫下要它做什麼。機器人再答一次。
3. **第 2 輪：加背景。** 寫下這是給誰看的。機器人再答一次。
4. **第 3 輪：加限制。** 寫下幾句話、不要什麼。機器人再答一次。
5. **第 4 輪：加格式。** 寫下答案要排成什麼樣子。機器人再答一次。

每一輪**只加一格**。孩子想一次加兩格時，提醒他：這樣就看不出是哪一格起了作用。
每一輪結束，孩子在紀錄表寫一句「這一輪和上一輪哪裡不一樣」。

## 第二回合：比一比（約 10 分鐘）

把五張答案（第 0 到第 4 輪）排成一排。

- 哪一格加上去之後，答案變得最多？
- 有沒有哪一格，加了好像沒差？為什麼？
- 如果只能留兩格，你會留哪兩格？

## 計分（不比快，比說得出理由）

- 每一輪確實只加一格：1 分。
- 每一輪說出和上一輪哪裡不一樣：1 分。
- 抓到機器人犯規：每次 1 分。
- 第二回合三個問題各說出理由：每題 1 分。

## 加碼：請爸爸用真的工具試（約 5 分鐘，可以不做）

由爸爸用自己的帳號，把第 4 輪的完整提示詞貼進去。孩子比較：真的工具和爸爸機器人，哪裡一樣、哪裡不一樣？
再按一次重新產生，看看同一句提示詞會不會得到不同的答案。提示詞裡不要有任何個資；它給的內容不要直接相信，下一堂課就要學怎麼抓錯。

## 常見卡關

- 孩子不知道「背景」要寫什麼：問他「這張卡片要貼在哪裡？誰會看？」
- 孩子把四格擠成一句很長的話：可以，只要四件事都有說到。四格是幫忙檢查有沒有漏掉，不是規定句型。
- 爸爸忍不住幫忙：把守則卡放在自己面前；孩子可以舉牌說「機器人犯規」。
- 孩子覺得機器人很笨：這正是重點。它不是笨，是不會讀心。
''',

'03_四輪紀錄_填寫說明.md': '''# 四輪紀錄怎麼寫

`03_四輪紀錄.csv` 可以用 Numbers 或任何試算表開啟；也可以直接寫在列印包第 2 頁。

每一輪寫一列：

- **這一輪加了哪一格**：任務、背景、限制、格式（第 0 輪寫「沒有」）。
- **我加上的那句話**：只寫新加的那一句。
- **機器人的答案**：不用全部抄，寫下最明顯的樣子，例如「一長段」「三句」「有標題」。
- **和上一輪哪裡不一樣**：一句話。
- **得分**：照活動規則計分。

最後一列「真的工具」可以不填；有請爸爸用真的工具試才寫。
紀錄裡不要寫任何人的姓名、學校、帳號或其他個資。
''',

'04_機器人示範與解說.md': '''# 機器人示範與解說（爸爸用）

下面是用「介紹機器人」走完四輪的一個示範。你不必照抄，照守則演就可以：只做寫到的事、沒寫到的亂猜、不可以反問。
示範答案裡關於機器人的內容，取自 NASA 給幼兒園到四年級學生的「What Is Robotics?」。

| 輪 | 加了哪一格 | 提示詞 | 機器人的答案（示範） | 孩子應該看到 |
|---|---|---|---|---|
''' + ''.join(f'| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |\n' for r in ROUNDS) + f'''
## 四輪加起來的完整提示詞

> {FULL_PROMPT}

對照四個格子：

| 格子 | 問自己 | 這個例子寫的是 |
|---|---|---|
''' + ''.join(f'| {b[0]} | {b[1]} | {b[2]} |\n' for b in BOXES) + '''
## 演機器人的小技巧

- **沒寫字數**：第 0 輪可以只答兩三個字，也可以寫滿半頁。兩種都演一次，孩子最有感覺。
- **沒寫對象**：故意用大人的詞，例如「自動化裝置」「感測器」。孩子說「看不懂」，就是補上背景的時機。
- **沒寫格式**：全部擠成一段，不要自己加標題和編號。
- **孩子寫得很清楚時**：就照做，而且做得很好。讓他看到寫清楚的回報。
- **孩子的寫法和示範不同**：沒關係。同一個格子有很多種寫法，重點是答案有沒有變成他要的樣子。

## 可以追問的問題

- 第 0 輪：機器人答錯了嗎？還是它只是不知道你要什麼？
- 第 2 輪：你怎麼知道它是寫給三年級看的？哪些詞變了？
- 第 3 輪和第 4 輪：「限制」和「格式」差在哪裡？（一個管多少、不要什麼；一個管排成什麼樣子。）
- 全部做完：四格都寫了，答案就一定正確嗎？要怎麼知道？

## 要記得告訴孩子的事

你演的機器人不會亂編內容，真正的生成式 AI 卻可能把錯的事情說得很有把握。提示詞寫得再清楚，內容還是要查證。這是下一堂課的主題。
''',

'05_自選規則與使用約定.md': '''# 孩子獨立改造：我的 Prompt 四格卡

下半場做三件事。

## 一、換一個主題，四格都填滿

選一個你喜歡的主題（恐龍、太空、昆蟲、火車、你正在看的書……），在列印包第 4 頁的四格卡上寫：

- **任務**：要它做什麼？
- **背景**：給誰看？用在哪裡？
- **限制**：幾句話？不要什麼？
- **格式**：答案排成什麼樣子？

寫好後，把四格連成一段完整的提示詞，請爸爸機器人照著做一次。

## 二、加一格自己的規則

選一條，或自己發明。一次只加一格，才知道它有沒有用。

- **角色**：請你當一位動物園的解說員。
- **語氣**：要有一點好笑／要像在說故事。
- **舉例**：每個小知識都要舉一個生活裡的例子。
- **反問**：最後反問我一題，看我有沒有看懂。
- **不確定就說**：不確定的地方，請直接說不確定。
- **先問我**：開始之前，先問我一個你需要知道的問題。（這一條可以讓機器人反問一次。）

加了之後再請機器人做一次，寫下：有沒有比較好？這一格什麼時候不需要？

## 三、寫一條使用約定

選一條，或自己發明：

- 作業如果用了 AI，要照老師的規定說明用了什麼、用在哪裡。
- AI 寫的東西，不直接當成自己的作品交出去。
- 提示詞裡不寫姓名、學校、住址，也不貼照片。
- 要用真的 AI 工具，請爸爸操作，我在旁邊出主意。
- AI 說的重要事情，要再查一個可靠的來源。

我的約定：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

把自選規則和約定都寫在四格卡下方。
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成 Prompt 四格卡（四格都有內容，連成一段完整的提示詞）
- [ ] 不看稿說出四個格子：任務、背景、限制、格式
- [ ] 不看稿說出三個步驟：寫、試、改
- [ ] 四輪紀錄表每一輪都寫了「和上一輪哪裡不一樣」
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 加了一格自選規則和一條使用約定，並說明要不要保留

## 孩子教爸爸（105–115 分鐘）

請孩子當老師，爸爸當學生。建議順序：

1. 爸爸從題目卡抽一張模糊的話，例如「介紹恐龍」。
2. 孩子帶爸爸一格一格補：任務、背景、限制、格式。爸爸故意只補一格就說「好了」。
3. 孩子指出還缺哪幾格，並說明少了那一格，答案會怎麼樣。
4. 孩子說出一個限制或安全注意事項，爸爸故意問：「我寫得這麼清楚，它還會錯嗎？」
5. 孩子出一題考爸爸，例如：「提示詞裡可以寫我們家的地址嗎？為什麼？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

1. 第一個好提示詞，是在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：四格卡拍照存成 `L011_Prompt四格卡_v01`，另存 `L011_四輪紀錄_v01`，
放進 `文件/Tech Academy/L011_第一個好提示詞/`，存好後再打開一次確認。拍照之前先檢查：卡片上沒有姓名、學校、住址。
''',

'07_四格小抄.md': '''# L011 四格小抄

## 三個步驟

1. **寫**：把要它做的事寫下來。
2. **試**：看它照你的話做出了什麼。
3. **改**：哪裡不對，補一句再試。

## 四個格子

| 格子 | 問自己 | 例子 |
|---|---|---|
''' + ''.join(f'| {b[0]} | {b[1]} | {b[2]} |\n' for b in BOXES) + '''
這四格是這堂課的整理，不是官方公式。不必每次都寫滿，缺哪一格就補哪一格。

## 三件要注意的事

- **不寫個資**：姓名、學校、住址、照片都不寫進去。
- **答案要查證**：寫得再清楚，答案也可能出錯。
- **有年齡限制**：要用真的工具，請爸爸用他的帳號操作。

## 提醒

- 它不會讀心。你沒寫的，它只能猜。
- 同一句提示詞，每次的回答可能不一樣。
- 作業用了 AI，要照老師的規定說明；它寫的不能直接當成自己的作品。

我最常漏掉的一格：＿＿＿＿＿＿　我的自選規則：＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

SHEET_HEADER = ['輪', '這一輪加了哪一格', '我加上的那句話', '機器人的答案', '和上一輪哪裡不一樣', '得分']
SHEET_ROWS = [['第 0 輪', '沒有', '介紹機器人'], ['第 1 輪', '任務'], ['第 2 輪', '背景'], ['第 3 輪', '限制'], ['第 4 輪', '格式'],
              ['自選規則'], ['真的工具（爸爸操作，可不填）']]

EXTRA_CSS = '''.box4{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.bx{height:36mm;padding:3mm 5mm}.bx h3{font-size:16pt;margin:0 0 .5mm}.bx p{margin:.6mm 0;font-size:11pt}.bx .eg{font-size:10pt;color:#35506b;border-top:.8pt solid #9db7cc;padding-top:1.2mm;margin-top:1.5mm}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin:0 0 5mm}.steps div{border:1.6pt solid #0b2540;border-radius:3mm;padding:2.5mm 4mm;font-size:11pt}.steps b{font-size:14pt;display:block}
.rule{padding:3.5mm 6mm;margin-top:5mm}.rule h3{font-size:14pt;margin:0 0 1mm}.rule p{margin:.8mm 0;font-size:11.5pt}
.act{border:1.3pt solid #35a9d6;border-radius:3mm;padding:2.5mm 5mm;margin-top:4mm;font-size:11pt}
.rec{table-layout:fixed}.rec th{font-size:9.5pt;padding:1mm .8mm;text-align:center}.rec td{height:33mm;font-size:10pt}.rec td.no{text-align:center;font-weight:700;vertical-align:middle}.rec td.pre{font-size:9.5pt;color:#35506b}
.ans{display:grid;grid-template-columns:1fr 1fr;gap:4mm}.ans div{border:1.3pt solid #0b2540;border-radius:3mm;height:72mm;padding:2.5mm 4mm}.ans b{font-size:11.5pt}.ans span{font-size:9pt;color:#4a6a88;margin-left:2mm}
.ans .wide{grid-column:1 / span 2;height:66mm}
.card{border:2pt solid #0b2540;border-radius:4mm;padding:5mm 6mm;height:236mm}.card h3{font-size:19pt;text-align:center;margin:0 0 3mm}
.card .g{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}.card .g div{border:1.4pt solid #35a9d6;border-radius:3mm;height:50mm;padding:2.5mm 4mm}
.card .g b{font-size:14pt}.card .g span{font-size:9.5pt;color:#35506b;margin-left:2mm}
.card p{font-size:11.5pt;margin:3mm 0 0}
.vg{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}.vc{border:1.4pt dashed #0b2540;border-radius:3mm;height:30mm;padding:2.5mm 3mm}
.vc span{font-size:9pt;color:#fff;background:#0b2540;border-radius:1.5mm;padding:.1mm 2mm}.vc h3{font-size:14pt;margin:3mm 0 0}
.pact{height:112mm;padding:4mm 6mm;margin-top:6mm}.pact p{margin:1.3mm 0;font-size:11.5pt}'''


def html():
    pages = []
    bx = lambda b: f'<div class="cut bx"><h3>{b[0]}</h3><p>{b[1]}</p><p class="eg">例如：{b[2]}</p></div>'
    pages.append('<h2>四格小抄卡與機器人守則</h2><p class="lead">沿外框剪下。四格是這堂課的整理，缺哪一格就補哪一格。</p>'
        '<div class="steps"><div><b>1 寫</b>把要它做的事寫下來</div><div><b>2 試</b>看它照你的話做出了什麼</div><div><b>3 改</b>哪裡不對，補一句再試</div></div>'
        '<div class="box4">' + ''.join(bx(b) for b in BOXES) + '</div>'
        '<div class="cut rule"><h3>機器人守則（爸爸扮演機器人時要守）</h3><p>一、只做提示詞寫到的事。</p><p>二、沒寫到的，就隨便猜一個。</p>'
        '<p>三、不可以反問，也不可以偷偷幫忙。</p></div>'
        '<div class="act"><b>三件要注意的事：</b>不寫個資（姓名、學校、住址、照片）・答案要查證（寫得再清楚也可能錯）・有年齡限制（要用真的工具，請爸爸用他的帳號）。</div>')

    rows = ''.join(f'<tr><td class="no">{n}</td><td class="no">{b}</td><td class="pre">{pre}</td><td></td><td></td><td></td></tr>'
                   for n, b, pre in (('0', '—', '介紹機器人'), ('1', '任務', ''), ('2', '背景', ''), ('3', '限制', ''), ('4', '格式', '')))
    pages.append('<h2>四輪紀錄表</h2><p class="lead">每一輪只加一格。寫下新加的那句話、機器人答案的樣子，還有和上一輪哪裡不一樣。</p>'
        '<table class="rec"><tr><th style="width:6%">輪</th><th style="width:9%">加哪一格</th><th style="width:30%">我加上的那句話</th>'
        '<th style="width:22%">機器人答案的樣子</th><th>和上一輪哪裡不一樣</th><th style="width:7%">得分</th></tr>' + rows + '</table>'
        '<p class="note" style="margin:3mm 0 0">每輪只加一格 1 分；說出哪裡不一樣 1 分；抓到機器人犯規每次 1 分。</p>')

    pages.append('<h2>機器人回答紙</h2><p class="lead">爸爸當機器人，把每一輪的答案寫在這裡。只做寫到的事，沒寫到的就亂猜。</p>'
        '<div class="ans"><div><b>第 0 輪</b><span>介紹機器人</span></div><div><b>第 1 輪</b><span>加了任務</span></div>'
        '<div><b>第 2 輪</b><span>加了背景</span></div><div><b>第 3 輪</b><span>加了限制</span></div>'
        '<div class="wide"><b>第 4 輪</b><span>加了格式：照孩子指定的樣子排</span></div></div>')

    pages.append('<h2>作品：Prompt 四格卡</h2><p class="lead">換一個你喜歡的主題。四格都填滿，再連成一段完整的提示詞。</p>'
        '<div class="card"><h3>我的 Prompt 四格卡　主題：＿＿＿＿＿＿＿</h3><div class="g">'
        '<div><b>任務</b><span>要它做什麼？</span></div><div><b>背景</b><span>給誰看？用在哪裡？</span></div>'
        '<div><b>限制</b><span>幾句話？不要什麼？</span></div><div><b>格式</b><span>答案排成什麼樣子？</span></div></div>'
        '<p><b>我的自選規則：</b></p><div class="line"></div>'
        '<p><b>連成一段完整的提示詞：</b></p><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div>'
        '<p><b>我的使用約定：</b></p><div class="line"></div>'
        '<p class="note" style="margin:3mm 0 0">名稱：L011_Prompt四格卡_v＿＿　日期：＿＿＿＿　這張卡上不要寫姓名、學校和住址。</p></div>')

    pages.append('<h2>模糊句題目卡與使用約定卡</h2><p class="lead">題目卡沿虛線剪開，孩子教爸爸時抽一張來改。下面的約定卡寫好後貼在電腦旁邊。</p>'
        '<div class="vg">' + ''.join(f'<div class="vc"><span>題目卡 {i}</span><h3>{v}</h3></div>' for i, v in enumerate(VAGUE, 1)) + '</div>'
        '<div class="cut pact"><h3>我們家的 AI 使用約定</h3>'
        '<p>□ 提示詞裡不寫姓名、學校、住址，也不貼照片。</p>'
        '<p>□ 要用真的 AI 工具，請爸爸用他的帳號操作，我在旁邊出主意。</p>'
        '<p>□ AI 說的重要事情，要再查一個可靠的來源。</p>'
        '<p>□ 作業如果用了 AI，照老師的規定說明；它寫的不直接當成自己的作品。</p>'
        '<p>我自己加的一條：</p><div class="line"></div><div class="line"></div>'
        '<p>這條約定什麼時候不適用？</p><div class="line"></div>'
        '<p>全家人簽名：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿　日期：＿＿＿＿＿＿</p></div>')
    return printpack.document('L011 第一個好提示詞 列印包', '父子科技學院 L011｜第一個好提示詞', pages, EXTRA_CSS)


if __name__ == '__main__':
    classroom_pack.build(
        slug='l011-first-good-prompt', folder='L011_第一個好提示詞', files=FILES,
        sheet=('03_四輪紀錄.csv', SHEET_HEADER, SHEET_ROWS),
        pack_html=html(), pack_pdf='02_列印包_Prompt四格卡.pdf', pack_pages=5,
        pack_needles=('四格小抄卡', '機器人守則', '四輪紀錄表', '機器人回答紙', 'Prompt 四格卡', '題目卡 8', '使用約定'),
        authoring_dir=Path(__file__).resolve().parent,
        extra={'rolePlay': {'robotPlayedBy': 'father, following three literal-robot rules', 'rounds': len(ROUNDS),
                            'startingPrompt': '介紹機器人', 'vagueTopicCards': len(VAGUE)},
               'needsChildAiAccount': False,
               'demoCardFactsFrom': 'NASA "What Is Robotics? (Grades K-4)" (2009), read directly by the producing agent',
               'answersProvided': 'a worked five-round example with what the child should notice; other wordings accepted'})
