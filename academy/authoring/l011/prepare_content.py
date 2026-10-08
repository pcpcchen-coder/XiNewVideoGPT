"""Author L011 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable. Holds only this lesson's text; authoring/lesson_builder.py writes the files.
After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l011/prepare_content.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lesson_builder  # noqa: E402

LESSON, SLUG, TITLE = 'L011', 'l011-first-good-prompt', '第一個好提示詞：任務、背景、限制、格式'
CHECKED = '2026-10-08'

SRC = {
    'curriculum': 'curriculum/catalog.json：L011；來源 V2 Excel 逐堂課程第 11 堂',
    'openai_academy': 'https://academy.openai.com/public/clubs/work-users-ynjqu/resources/prompting',
    'openai_home': 'https://cdn.openai.com/pdf/chatgpt-at-home.pdf',
    'anthropic_prompting': 'https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices',
    'google_workspace': 'https://workspace.google.com/resources/ai/writing-effective-prompts/',
    'microsoft_prompts': 'https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-writing-prompts-in-microsoft-365-copilot',
    'moe_genai': 'https://jr.hs.ntnu.edu.tw/wp-content/uploads/2026/02/中小學使用「生成式人工智慧」注意事項2.1.pdf',
    'moe_guide3': 'https://www2.chjhs.tyc.edu.tw/gov/教育部中小學數位教學指引3.0版1140113.pdf',
    'eliteracy_handbook': 'https://eliteracy.edu.tw/Handbooks.aspx',
    'google_bia': 'https://services.google.com/fh/files/misc/bia_ai-literacy-guide_en.pdf',
    'gemini_privacy': 'https://support.google.com/gemini/answer/13594961?hl=en',
    'anthropic_terms': 'https://www.anthropic.com/legal/consumer-terms',
    'google_mistakes': 'https://support.google.com/gemini/answer/13954172',
    'claude_age': 'https://support.claude.com/en/articles/15171100-age-assurance-on-claude',
    'gemini_signin': 'https://support.google.com/gemini/answer/13278668?hl=en',
    'copilot_terms': 'https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse',
    'openai_terms': 'https://openai.com/policies/row-terms-of-use/',
    'nasa_robotics': 'https://www.nasa.gov/learning-resources/for-kids-and-students/what-is-robotics-grades-k-4/',
}

SOURCE_RECORDS = [
    {'id': 'openai_academy', 'title': 'Prompting（2025-08-06；2026-09-04 更新）', 'publisher': 'OpenAI Academy（課表 R21 的主要參考網址）', 'url': SRC['openai_academy'], 'usedFor': '三個步驟：說清楚任務、提供背景、描述理想的輸出；第一次的答案不理想時在對話中補充或調整；沒有唯一完美的寫法'},
    {'id': 'openai_home', 'title': 'ChatGPT at home（家長指南，PDF 中繼資料 2026-05）', 'publisher': 'OpenAI（圖片式 PDF，由研究代理逐頁判讀）', 'url': SRC['openai_home'], 'usedFor': '好的提示通常有三部分：Task、Context、Output；Context 一列提到 audience 與 constraints；請它用十歲孩子看得懂的方式寫'},
    {'id': 'anthropic_prompting', 'title': 'Prompting best practices', 'publisher': 'Anthropic Claude Platform Docs（開發者文件）', 'url': SRC['anthropic_prompting'], 'usedFor': '說得越精確結果越好；明確指定輸出格式與限制；範例是引導格式、語氣與結構很可靠的方法'},
    {'id': 'google_workspace', 'title': 'How to write effective prompts', 'publisher': 'Google Workspace', 'url': SRC['google_workspace'], 'usedFor': '四個面向：Persona、Task、Context、Format，不必每次都用齊；用後續提示反覆檢視與修正；回應有時無法預測'},
    {'id': 'microsoft_prompts', 'title': 'Get started writing prompts in Microsoft Copilot（2026-09 更新）', 'publisher': 'Microsoft Support', 'url': SRC['microsoft_prompts'], 'usedFor': '四個部分：Goal、Context、Source、Expectations；要有來回對話的心理準備；同一個提示多次使用可能得到不同回應'},
    {'id': 'moe_genai', 'title': '中小學使用「生成式人工智慧」注意事項 2.1（學生版；115 年 2 月 11 日核定）', 'publisher': '教育部（師大附中國中部網站轉載的 PDF；教師版與教育部網站版本文字相同）', 'url': SRC['moe_genai'], 'usedFor': '不可輸入姓名、照片、聯絡方式、住址、學號等個資；不能全盤接受生成內容，需查證；依規定註明使用的工具及用途，不得將生成內容直接當作自己原創作品繳交；遵守各平臺註冊年齡限制，非在校使用請家長陪伴'},
    {'id': 'moe_guide3', 'title': '中小學數位教學指引 3.0 版（封面 2025 年 1 月）', 'publisher': '教育部（學校網站轉載的 PDF；官方下載頁憑證錯誤無法讀取）', 'url': SRC['moe_guide3'], 'usedFor': '教育部的用詞是「提示（Prompt）」與「提問」；同樣的提示可能會有不同的結果；把問題切成小問題一步步提問；答案不如預期要能調整'},
    {'id': 'eliteracy_handbook', 'title': '《你不可不知的生成式AI 國小高年級學生版》《AI與我們的生活 國小中年級學生版》', 'publisher': '教育部 中小學數位素養教育資源網（手冊列表頁）', 'url': SRC['eliteracy_handbook'], 'usedFor': '生成式 AI 的產出品質有賴於正確的提問；人類給予錯誤的要求，就無法生成想要的內容，內容也無法確保正確性'},
    {'id': 'google_bia', 'title': 'Understanding AI: Foundational AI literacy for Grades 2nd-8th（2025-06）', 'publisher': 'Google Be Internet Awesome', 'url': SRC['google_bia'], 'usedFor': '提示是你打字或說出來、告訴 AI 要做什麼的話；訂蛋糕要告訴師傅你要哪一種；使用 AI 要有信任的大人陪同'},
    {'id': 'gemini_privacy', 'title': 'Gemini Apps Privacy Hub（2026-09-24 更新；L010 查核時讀取）', 'publisher': 'Google', 'url': SRC['gemini_privacy'], 'usedFor': '不要輸入你不希望審查人員看到的機密資訊'},
    {'id': 'anthropic_terms', 'title': 'Consumer Terms of Service（2025-10-08 生效）', 'publisher': 'Anthropic', 'url': SRC['anthropic_terms'], 'usedFor': '輸出不一定正確，即使看起來很詳細；須年滿 18 歲'},
    {'id': 'google_mistakes', 'title': 'Gemini Apps Help（生成式 AI 會出錯）', 'publisher': 'Google', 'url': SRC['google_mistakes'], 'usedFor': '生成式 AI 還在發展，會出錯'},
    {'id': 'claude_age', 'title': 'Age assurance on Claude（2026-05-18）', 'publisher': 'Claude Help Center', 'url': SRC['claude_age'], 'usedFor': '教材：Claude 消費者產品僅供 18 歲以上使用'},
    {'id': 'gemini_signin', 'title': 'What you need to sign in to Gemini Apps', 'publisher': 'Google Gemini Apps Help', 'url': SRC['gemini_signin'], 'usedFor': '教材：個人或學校帳號須年滿 13 歲（或所在國家適用的年齡）'},
    {'id': 'copilot_terms', 'title': 'Microsoft Copilot Terms of Use（2026-08-18 生效）', 'publisher': 'Microsoft', 'url': SRC['copilot_terms'], 'usedFor': '教材：至少 13 歲，依各國法律可能更高；Copilot 可能出錯'},
    {'id': 'openai_terms', 'title': 'Terms of Use（2026-01-01 生效）', 'publisher': 'OpenAI（只有擷取工具的摘要，沒有逐字確認）', 'url': SRC['openai_terms'], 'usedFor': '教材：須年滿 13 歲，未滿 18 歲需家長或監護人同意'},
    {'id': 'nasa_robotics', 'title': 'What Is Robotics? (Grades K-4)（2009-11-09）', 'publisher': 'NASA STEM Team（製作代理直接下載原始頁面讀取）', 'url': SRC['nasa_robotics'], 'usedFor': '教材的示範科普卡：機器人是可以用來做事的機器；有些能自己工作，有些要有人告訴它怎麼做；探索火星的探測車是機器人'},
]

SCENES = [
 ('第一個好提示詞', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第十一堂，第一個好提示詞，這是依課表製作的課前教學版，並非實際上課錄音。',
  '你打字告訴 AI，要它做什麼，這些話就叫做提示詞；說得太模糊，它只能用猜的。',
  '今天我們用四個格子，把一句模糊的話，一輪一輪改成一張兒童科普卡的提示詞。'],
  ['curriculum', 'google_bia']),
 ('寫提示詞的三個步驟', [
  '寫提示詞有三個步驟。第一步是寫，把你要它做的事寫下來。',
  '第二步是試，看看它照著你的話，做出了什麼。',
  '第三步是改，哪裡不對，就補上一句再試一次；提示詞通常要這樣來回改幾次，才會越來越好。'],
  ['openai_academy', 'google_workspace', 'microsoft_prompts']),
 ('提示詞：你交代給 AI 的話', [
  '這堂課說的 AI，是會寫字、會畫圖的生成式 AI；你寫給它的話，就是提示詞，可以是一個問題，也可以是一件要它做的事。',
  '它不會讀心，你沒寫出來的，它就只能自己猜。',
  '提示詞寫得清楚，通常比較容易得到你要的東西；不過同樣一句話，每次的回答可能不一樣，內容也還是可能出錯。'],
  ['google_bia', 'anthropic_prompting', 'moe_guide3', 'microsoft_prompts', 'eliteracy_handbook']),
 ('好提示詞的四個格子', [
  '好的提示詞可以分成四個格子。第一格是任務，要它做什麼；第二格是背景，這是給誰看的、要用在哪裡。',
  '第三格是限制，例如最多幾句話、不要用太難的詞；第四格是格式，答案要排成什麼樣子，像是條列、表格，或是一張卡片。',
  '這四個格子是我們這堂課自己的整理方式，各家公司教的名稱不完全一樣，不過意思很接近。'],
  ['curriculum', 'openai_academy', 'openai_home', 'google_workspace', 'microsoft_prompts', 'anthropic_prompting']),
 ('模糊和清楚差在哪裡？', [
  '來看一個例子。如果你只寫五個字：介紹機器人，它不知道要介紹哪一種機器人，也不知道是寫給誰看的。',
  '結果可能是一大篇很難的文章，也可能只有短短一句，因為你沒說的，它只能猜。',
  '所以接下來，我們要一格一格補上去，每補一格就試一次，看看答案有什麼不一樣。'],
  ['curriculum', 'openai_academy']),
 ('一輪加一格', [
  '第一輪加上任務：請寫一張科普卡，告訴我機器人是什麼。現在它知道要做什麼了。',
  '第二輪加上背景：這張卡片是給國小三年級的同學看的。這樣它比較可能改用簡單的說法。',
  '第三輪加上限制和格式：只要三個小知識，每個一句話，最後加一個小問題。每一輪只加一格，才看得出是哪一格起了作用。'],
  ['openai_home', 'anthropic_prompting']),
 ('角色扮演：爸爸當機器人', [
  '現在來玩角色扮演。你負責寫提示詞，爸爸扮演一台只會照字面做事的機器人，把答案寫在紙上。',
  '機器人有三條守則：只做提示詞寫到的事；沒寫到的，就隨便猜一個；而且不可以反過來問你問題。',
  '這樣玩，完全不需要用到 AI，你也能看出來，少寫一格，答案會差多少。'],
  ['curriculum']),
 ('三件要注意的事', [
  '寫提示詞之前，有三件事要注意。第一，不要把個資寫進去，像是姓名、學校、住址和照片，因為寫進去的東西可能被保存下來。',
  '第二，提示詞寫得再好，答案還是可能出錯，重要的事要找可靠的來源再查一次。',
  '第三，這些工具都有年齡限制，真的要試的時候，請爸爸用他自己的帳號操作，你在旁邊出主意。'],
  ['moe_genai', 'gemini_privacy', 'anthropic_terms', 'google_mistakes', 'claude_age', 'gemini_signin', 'copilot_terms']),
 ('四輪提示詞改造賽', [
  '活動分成兩個回合。第一回合，你寫提示詞，爸爸當機器人回答，一共四輪，每一輪只加一格。',
  '第二回合，把四輪的答案排在一起比一比，說出加了哪一格之後，答案變得最多。',
  '如果想試試真正的 AI，請爸爸用他的帳號，把最後一版提示詞貼進去，記得裡面不能有個資。'],
  ['curriculum', 'moe_genai']),
 ('換你設計：我的 Prompt 四格卡', [
  '下半場換你設計自己的提示詞四格卡。換一個你喜歡的主題，把任務、背景、限制和格式四格都填滿。',
  '再加一格你自己的規則，例如指定語氣、請它舉一個例子，或是請它最後反問你一題。',
  '還要寫下一條使用約定：作業如果用了 AI，要照老師的規定說明；它寫的東西，不能直接當成自己的作品交出去。'],
  ['curriculum', 'moe_genai', 'anthropic_prompting']),
 ('兩小時的提示詞課', [
  '兩小時的課這樣走：開場十分鐘，認識四個格子十五分鐘，接著用四十分鐘玩四輪改造，然後休息十分鐘。',
  '休息之後，用三十分鐘完成自己的四格卡，再用十分鐘交換角色，換你教爸爸把一句模糊的話改清楚。',
  '最後五分鐘錄音總結，替四格卡取名字，存檔之前再檢查一次，卡片上沒有任何個資。'],
  ['curriculum']),
 ('最後一關：教爸爸寫提示詞', [
  '最後一關，請不看稿，讓爸爸出一句模糊的話，你當場一格一格補成好的提示詞。',
  '再指出一個限制或安全注意事項，例如提示詞寫得再清楚，答案也可能是錯的。',
  '今天的作品是提示詞四格卡，下次我們要舉辦幻覺抓錯賽，把亂講的答案抓出來；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum', 'anthropic_terms']),
]

VISIBLE = [
 ['第十一堂任務', '第一個\n好提示詞', '任務、背景、限制、格式，一格一格說清楚', '第十一堂  ·  依課表製作的課前教學版'],
 ['寫提示詞的三個步驟', '先寫、再試、然後改',
  '01 寫', '把要它做的事\n寫下來', '→',
  '02 試', '看它照你的話\n做出了什麼', '→',
  '03 改', '哪裡不對\n補一句再試',
  '今天的作品：Prompt 四格卡'],
 ['提示詞：你交代給 AI 的話', '可以是一個問題，也可以是一件要它做的事',
  '01', '它不會讀心', '你沒寫出來的，它只能自己猜',
  '02', '寫清楚比較有用', '通常比較容易得到你要的東西',
  '03', '還是有極限', '同一句話每次回答可能不同，也可能出錯'],
 ['好提示詞的四個格子', '一格說一件事，缺哪一格就補哪一格', '四個格子',
  '任務', '要它做什麼', '背景', '給誰看、用在哪', '限制', '幾句話、不要什麼', '格式', '答案排成什麼樣',
  '四個格子是本課的整理，各家的說法不完全一樣'],
 ['模糊和清楚差在哪裡？', '同一個主題，寫法不同，答案就不同',
  '只寫五個字', '介紹機器人', '→', '補上四個格子', '任務＋背景＋限制＋格式',
  '你沒寫的，它只能用猜的',
  '寫清楚不是寫很多，是把該說的說到'],
 ['一輪加一格', '每補一格就試一次，看答案哪裡不一樣',
  '01 加任務', '寫一張科普卡', '02 加背景', '給三年級同學看', '03 加限制和格式', '三個小知識，各一句',
  '每一輪只加一格，才看得出哪一格有用'],
 ['角色扮演：爸爸當機器人', '不用登入任何工具，也能練習寫提示詞',
  '孩子寫提示詞  →  爸爸照字面回答  →  一起看結果',
  '守則一', '只做寫到的事', '守則二', '沒寫到的就亂猜', '守則三', '不可以反問',
  '少寫一格，答案會差多少？'],
 ['三件要注意的事', '寫提示詞之前，先想到安全',
  '一、不寫個資：姓名、學校、住址、照片\n二、答案要查證：寫得再好也可能錯\n三、有年齡限制：請爸爸用他的帳號',
  '為什麼不寫個資？', '寫進去的東西，可能被保存', '不想被別人看到的\n就不要寫進去',
  '暫停影片：說出這三件要注意的事'],
 ['四輪提示詞改造賽', '孩子寫提示詞，爸爸當機器人',
  '第一回合：機器人上場', '一共四輪，每輪只加一格\n爸爸照字面寫出答案',
  '第二回合：比一比', '四輪答案排在一起\n說出哪一格差最多',
  '想試真正的 AI：請爸爸操作，而且不寫個資'],
 ['換你設計：我的 Prompt 四格卡', '換一個喜歡的主題，再加一格自己的規則',
  '01', '四格都填滿', '任務、背景、限制、格式',
  '02', '加一格自選規則', '例如：語氣、舉例、最後反問我一題',
  '03', '寫下使用約定', '用了要說明；不把它寫的當成自己的作品'],
 ['兩小時的提示詞課', '影片先引路，接下來用四格卡練習把話說清楚',
  '00–25', '開場十分＋概念十五分', '25–65', '四輪提示詞改造賽', '65–75', '休息十分鐘',
  '75–105', '我的四格卡＋自選規則', '105–115', '孩子教爸爸寫提示詞', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：數位公民，話要說清楚，答案要查證'],
 ['最後一關：教爸爸寫提示詞', '暫停影片：不看稿示範一次，再指出一個限制或安全注意',
  '01', '完成 Prompt 四格卡', '四格都有內容，還有一格自選規則',
  '02', '當場改一句模糊的話', '爸爸出題，一格一格補上',
  '03', '指出一個限制或安全注意', '例如：寫得再清楚，答案也可能錯',
  '保持好奇，我們下次見！'],
]

BOARD = [
 ('開場：課前教學版揭露、提示詞是什麼、今天的四個格子與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備四格卡與紙筆；預告角色扮演與作品'),
 ('概念：寫、試、改三個步驟；提示詞要來回修改', '三步流程卡：寫 → 試 → 改', '說出今天要完成的作品'),
 ('概念：提示詞是交代給生成式 AI 的話；它不會讀心；寫清楚有用但有極限', '三點條列＋陳犀牛', '用自己的話說「它不會讀心」是什麼意思'),
 ('概念：四個格子（任務、背景、限制、格式）；這是本課的整理', '面板四張卡＋黃字說明', '各舉一個可以寫進格子的例子'),
 ('示範：只寫「介紹機器人」五個字，缺了什麼', '雙框（只寫五個字 → 補上四個格子）＋白字＋黃字', '先猜它會怎麼回答'),
 ('示範：一輪加一格（任務、背景、限制和格式）', '三張步驟卡＋黃字提醒', '說出每一輪加了什麼'),
 ('活動機制：角色扮演，爸爸當只照字面做事的機器人；三條守則', '路徑一行＋三張守則卡＋黃字提問', '確認三條守則；決定誰先寫'),
 ('安全：不寫個資、答案要查證、年齡限制由爸爸操作', '左側三行；右側「為什麼不寫個資？」', '暫停影片：說出這三件要注意的事'),
 ('活動規則：四輪改造，每輪只加一格；再比較四輪答案', '左右比較卡（機器人上場／比一比）＋黃字', '完成四輪並比較；記錄哪一格差最多'),
 ('獨立改造與數位公民：自己的四格卡、自選規則、使用約定', '三點條列＋陳犀牛', '完成四格卡；寫下一條使用約定'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：當場改一句模糊的話，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子教爸爸；錄音回答四個問題；作品命名存檔'),
]

FACT_CHECK = '''# L011 事實查核

查核日：2026-10-08。查核者：製作代理（Claude）與其派出的研究子代理。
方法：子代理下載各來源的原始頁面或 PDF、抽取文字後回報逐字引文（原文見 `source-notes.md`）；主代理再把引文和旁白、投影片、教材逐句比對。
NASA 的機器人頁面由主代理自己下載原始頁面讀取。
限制：主代理沒有逐頁重讀其餘來源；OpenAI 的說明中心與條款只有擷取工具的摘要，沒有逐字確認；OpenAI 的家長指南是圖片式 PDF，由子代理逐頁判讀；
教育部數位教學指引 3.0 讀的是學校網站轉載的 PDF（官方下載頁憑證錯誤，沒有繞過）；來源多為英文，中文是本課轉述。

## 主張與來源

| # | 本課的說法（幕） | 來源依據 | 結論 |
|---|---|---|---|
| 1 | 你告訴 AI 要它做什麼的那些話叫做提示詞，可以是問題，也可以是要它做的事（1、3） | Google Be Internet Awesome：“Prompts are the words you type or say to tell AI what to do.” | 相符。「提示詞」是常見說法；教育部文件寫作「提示（Prompt）」或「提問」，教材有註明 |
| 2 | 說得太模糊，它只能猜；它不會讀心（1、3、5） | Google Be Internet Awesome：訂蛋糕要告訴師傅你要哪一種；教育部手冊：「如果人類給予錯誤的要求，那麼生成式AI工具也無法生成出人類想要的內容」 | 相符（「不會讀心」「只能猜」是本課的白話說法） |
| 3 | 三個步驟：寫、試、改；提示詞通常要來回改幾次（2） | OpenAI Academy：“if the first answer isn’t quite right, clarify or adjust mid-conversation”；Google：“an iterative process of review and refinement”；Microsoft：“Expect some back-and-forth conversation” | 相符；「寫、試、改」是本課的整理 |
| 4 | 寫得清楚，通常比較容易得到你要的東西（3） | Anthropic：“The more precisely you explain what you want, the better the result.”；教育部手冊：「產出的品質有賴於正確的提問」 | 相符；旁白用「通常」「比較容易」，沒有說保證 |
| 5 | 同樣一句話，每次的回答可能不一樣（3） | 教育部數位教學指引 3.0：「同樣的提示（Prompt）可能會有不同的結果」；Microsoft：“Using the same prompt multiple times can result in different responses.” | 相符 |
| 6 | 寫得再好，內容還是可能出錯，要查證（3、8、12） | Anthropic 條款：輸出 “may contain material inaccuracies even if they appear accurate”；Google：“it can and will make mistakes”；教育部注意事項：「不能全盤接受生成的內容，而需…進行查證」 | 相符 |
| 7 | 四個格子：任務、背景、限制、格式（4） | OpenAI：Task／Context／Output；Google：Persona／Task／Context／Format；Microsoft：Goal／Context／Source／Expectations；Anthropic：“Be specific about the desired output format and constraints.” | 部分相符：任務、背景、格式三格各家都有對應；「限制」不是任何一家單獨列出的項目，只出現在 Anthropic 的 “format and constraints” 與 OpenAI 的 Context 說明裡。課表用的是這四格 |
| 8 | 這四個格子是本課自己的整理方式，各家名稱不完全一樣，意思很接近（4） | 同上；Google：“You don’t need to use all four in every prompt”；OpenAI Academy：“There’s no single ‘perfect’ way to prompt.” | 相符；影片與教材都說明這不是官方標準 |
| 9 | 背景：給誰看；例如給三年級同學看，它比較可能用簡單的說法（4、6） | OpenAI Academy：“who it’s for”；OpenAI 家長指南：“Write this in a way a 10-year-old can understand.” | 相符；「三年級」是本課的例子，旁白用「比較可能」 |
| 10 | 格式：條列、表格或卡片（4） | OpenAI 家長指南：“What should the answer look like: a list, table, text message, plan, script, or checklist?” | 相符；「卡片」是本課的例子 |
| 11 | 只寫「介紹機器人」，可能得到很長很難的文章，也可能只有一句（5） | 沒有來源；這是本課的說明性例子 | 旁白用「可能」；沒有實際拿任何工具測試 |
| 12 | 個資不要寫進提示詞：姓名、學校、住址、照片（8） | 教育部注意事項六（三）：「不可以將自己或他人的姓名、照片、聯絡方式、住址、學號等個人資料…輸入至『生成式人工智慧』工具。」 | 相符；「學校」不在原文列舉內（原文是「學號」與「學校的機密資訊」），屬本課延伸，L009 已教過學校名稱是個資 |
| 13 | 寫進去的東西可能被保存下來（8） | Google Gemini 隱私說明：不要輸入你不希望審查人員看到的機密資訊；教育部注意事項提到資料「可能」被收錄到訓練資料庫（見 L010 查核筆記） | 相符；旁白用「可能」 |
| 14 | 這些工具都有年齡限制，請爸爸用自己的帳號操作（8、9） | Anthropic：Claude 僅供 18 歲以上；Google：Gemini 個人帳號須年滿 13 歲（或所在國家適用年齡）；Microsoft：Copilot 至少 13 歲；OpenAI 條款（摘要）：13 歲並需家長同意；教育部：遵守各平臺註冊年齡限制，非在校使用請家長陪伴 | 相符；影片沒有說出各家的數字，數字寫在教材並註明 OpenAI 那一條沒有逐字確認 |
| 15 | 作業用了 AI 要照老師的規定說明；不能把它寫的直接當成自己的作品交出去（10） | 教育部注意事項六（四）：「應依規定註明所使用的工具及用途，不得將生成內容直接當作自己原創作品繳交。」 | 相符 |
| 16 | 可以請它舉例、指定語氣（10） | Anthropic：範例是引導輸出格式、語氣與結構很可靠的方法；OpenAI Academy：“Tell ChatGPT how you want the response to sound and look.” | 相符；Anthropic 說的是「給它範例」，「請它舉例」「請它反問我一題」是本課的玩法 |
| 17 | 教材示範卡：機器人是可以幫人做事的機器；有些能自己工作，有些要人告訴它怎麼做；探索火星的探測車是機器人（教材） | NASA（2009）：“Robots are machines that can be used to do jobs. Some robots can do work by themselves. Other robots must always have a person telling them what to do.”；“The Mars rovers Spirit and Opportunity are robots.” | 相符；只用這一頁裡不會過時的句子 |

## 刻意避免的說法

- 沒有說「任務、背景、限制、格式」是 OpenAI、Google、Microsoft、Anthropic 或教育部的官方公式。
- 沒有說「提示詞」是教育部的用詞。
- 沒有說好的提示詞能保證答案正確，也沒有說任何一家廠商保證正確。
- 沒有說孩子可以自己開帳號；沒有說 Family Link 能讓台灣的孩子使用 Gemini（Google 的頁面說法互相矛盾，台灣情形沒有查核）。
- 沒有引用任何縮寫口訣（例如 CRAFT）當成權威。
- 影片沒有示範任何真實 AI 工具的畫面或回答；「機器人」的回答是爸爸照守則寫的。

## 課程與素材

- 課程主題、學習目標、120 分鐘流程（10／15／40／10／30／10／5）、動手任務（把「介紹機器人」逐輪改造成能產出兒童科普卡的提示詞）、
  作品（Prompt 四格卡）與驗收，依 `curriculum/catalog.json` L011 核對。
- 沒有課堂錄音；本集是**依課表製作的課前教學版**，未虛構逐字稿或父子對話，封面、旁白第一句與說明均已揭露。
- 課表的好玩機制是角色扮演。本課的做法是爸爸扮演「只照字面做事的機器人」，所以整堂課不需要孩子登入任何 AI 工具。
- 課表主要參考網址（R21）是 OpenAI Academy 的 Prompting 頁面，本課有引用；它是寫給上班族的，列的是三個步驟而不是四格。
- 作品名稱照課表寫作「Prompt 四格卡」；旁白念作「提示詞四格卡」。
- 課表的三組 YouTube 連結是動態搜尋入口；本次沒有挑選、觀看或引用任何影片。
'''

PLAN = '''# L011 第一個好提示詞：任務、背景、限制、格式

依課表製作的課前教學版；沒有課堂錄音，不製造逐字稿。
沿用原片頭 v2、陳犀牛、深藍／黃／青、12 頁原生可編輯簡報、36 句旁白、zh-TW-YunJheNeural；
教學段落靜態畫面加 0.55 秒淡化，無背景音樂、無推拉鏡頭。

## 課表核對（curriculum/catalog.json L011）

- 模組：M01 數位探險家；難度 2；主軸：數位素養／AI 素養／網路安全。
- 學習目標：學會以明確目的與輸出格式和 AI 協作。
- 動手任務：把「介紹機器人」逐輪改造成能產出兒童科普卡的提示詞。好玩機制：角色扮演。
- 作品：Prompt 四格卡。生活技能支線：數位公民。
- 驗收：完成作品；不看稿說出核心原理；指出至少一個錯誤、限制或安全注意事項。

## 120 分鐘（課堂，與影片片長分開）

| 分鐘 | 內容 | 對應影片頁 |
|---|---|---|
| 00–10 | 任務開場：爸爸當機器人，孩子只說「介紹機器人」，看看得到什麼 | 1–2 |
| 10–25 | 概念示範：提示詞是什麼、四個格子、模糊與清楚、一輪加一格、三件要注意的事 | 3–8 |
| 25–65 | 共同實作：四輪提示詞改造賽（孩子寫、爸爸當機器人），再比較四輪答案 | 9 |
| 65–75 | 休息 | — |
| 75–105 | 孩子獨立改造：自己主題的 Prompt 四格卡、一格自選規則、一條使用約定 | 10 |
| 105–115 | 角色互換：孩子教爸爸把一句模糊的話改清楚 | 12 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 11–12 |

## 12 頁

1 開場與揭露｜2 寫、試、改｜3 提示詞是什麼｜4 四個格子｜5 模糊和清楚｜6 一輪加一格｜7 角色扮演守則｜
8 三件要注意的事｜9 四輪改造賽｜10 我的四格卡與使用約定｜11 兩小時安排｜12 驗收與結尾。

## 設計取捨

- 角色扮演＝爸爸當「只照字面做事的機器人」。孩子不需要任何 AI 帳號，就能看出少寫一格答案差多少；想用真的工具，由爸爸用自己的帳號操作。
- 四個格子照課表（任務、背景、限制、格式），影片與教材都說明這是本課的整理：各家廠商的說法是三到四項，名稱不同，「限制」沒有任何一家單獨列出。
- 不說好提示詞保證正確；第 3、8、12 頁都提到答案還是可能出錯。
- 示範主題照課表用「介紹機器人」，示範科普卡的內容只用 NASA 給低年級的機器人說明裡的句子。
- 作品名稱照課表寫「Prompt 四格卡」，旁白念「提示詞四格卡」，避免英文夾在中文裡念得太短。

## 作品與驗收

- Prompt 四格卡（任務、背景、限制、格式＋一格自選規則＋組合起來的完整提示詞）。
- 四輪紀錄表。
- 一條使用約定。
- 孩子教爸爸：不看稿把一句模糊的話一格一格補清楚，並指出一個限制或安全注意事項。
- 錄音四問（錄音只留私人區）。

## 教材

`classroom/L011_第一個好提示詞/`：爸爸先讀、四輪提示詞改造賽規則、5 頁列印包（四格小抄卡與機器人守則、四輪紀錄表、機器人回答紙、
Prompt 四格卡、模糊句題目卡與使用約定卡）、四輪紀錄（CSV＋說明）、機器人示範與解說、自選規則與使用約定、驗收與回顧、四格小抄。
由 `authoring/l011/classroom.py` 產生；內容與來源查核見 fact-check.md。
'''

SUMMARY = '''這是依課表製作的課前教學版，不是實際上課錄音，也沒有虛構的課堂對話。

你交代給 AI 的話叫做提示詞。說得太模糊，它只能用猜的。陳犀牛帶你用四個格子，把「介紹機器人」這五個字，一輪一輪改成一張兒童科普卡的提示詞。
看完影片，和爸爸玩角色扮演：你寫提示詞，爸爸當一台只會照字面做事的機器人。不需要任何 AI 帳號。

這一集會學到
・寫提示詞的三個步驟：寫、試、改
・四個格子：任務（要它做什麼）、背景（給誰看）、限制（幾句話、不要什麼）、格式（答案排成什麼樣）
・一輪只加一格，才看得出哪一格有用
・三件要注意的事：不寫個資、答案要查證、工具有年齡限制

教材用法（classroom.zip）
先讀「00_爸爸先讀」，列印「02_列印包」（A4 共 5 頁），照「01_活動規則」玩四輪提示詞改造賽，用「03_四輪紀錄」記錄；
爸爸怎麼當機器人寫在「04_機器人示範與解說」，下半場完成 Prompt 四格卡和「05_自選規則與使用約定」，最後用「06_驗收與回顧」讓孩子教爸爸。「07_四格小抄」可以貼在電腦旁邊。

注意事項
・課堂是 120 分鐘，影片只是課前引導，片長另計。
・「任務、背景、限制、格式」是這堂課的整理，不是任何一家公司的官方公式；各家的說法是三到四項，名稱不完全一樣。
・提示詞寫得再清楚，答案還是可能出錯，重要的事要再查證。
・各家 AI 工具都有年齡限制。想用真的工具試，請由爸爸用自己的帳號操作，並且不輸入姓名、學校、住址、照片等個資。

來源（查核日 2026-10-08）
教育部「中小學使用『生成式人工智慧』注意事項 2.1」（115 年 2 月核定）
OpenAI Academy「Prompting」：https://academy.openai.com/public/clubs/work-users-ynjqu/resources/prompting
Google Workspace「How to write effective prompts」：https://workspace.google.com/resources/ai/writing-effective-prompts/
Microsoft「Get started writing prompts in Microsoft Copilot」：https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-writing-prompts-in-microsoft-365-copilot
Anthropic「Prompting best practices」：https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
Google Be Internet Awesome「Understanding AI」：https://services.google.com/fh/files/misc/bia_ai-literacy-guide_en.pdf
NASA「What Is Robotics? (Grades K-4)」：https://www.nasa.gov/learning-resources/for-kids-and-students/what-is-robotics-grades-k-4/
'''

if __name__ == '__main__':
    lesson_builder.build(
        lesson=LESSON, slug=SLUG, ordinal='十一', title=TITLE, header_en='FIRST GOOD PROMPT', checked=CHECKED,
        src=SRC, scenes=SCENES, visible=VISIBLE, board=BOARD,
        render_options={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        tts_basis="On 2026-10-08 the user asked to start producing L011–L013 after receiving L007–L010, whose hand-over stated that "
                  "the public narration is sent to Edge TTS on the same basis; restated to the user before synthesis.",
        source_records=SOURCE_RECORDS,
        source_method='A research subagent downloaded each page/PDF on the check date and reported verbatim quotes '
                      '(production/source-notes.md); the producing agent mapped them to claims and downloaded the NASA page itself. '
                      'Not a human full read.',
        not_verified=['OpenAI 說明中心與條款只有擷取工具的摘要，沒有逐字確認',
                      'OpenAI 家長指南是圖片式 PDF，由研究子代理逐頁判讀，沒有可抽取的文字',
                      '教育部數位教學指引 3.0 的官方下載頁憑證錯誤無法讀取，讀的是學校網站轉載的 PDF',
                      '教育部注意事項 2.1 學生版沒有找到教育部網站上的版本，讀的是學校網站轉載的 PDF（教師版與教育部網站版本文字相同）',
                      '台灣適用的各平臺最低年齡沒有官方說明；Family Link 是否讓台灣兒童使用 Gemini 沒有查核',
                      '沒有用任何真實 AI 工具測試本課的示範提示詞'],
        documents={'fact-check.md': FACT_CHECK, 'plan.md': PLAN, 'delivery-summary.md': SUMMARY,
                   'source-notes.md': (Path(__file__).resolve().parent / 'source-notes.md').read_text(encoding='utf-8')},
        readme=lesson_builder.readme(LESSON, TITLE))
