"""Author L010 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable. Holds only this lesson's text; authoring/lesson_builder.py writes the files.
After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l010/prepare_content.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lesson_builder  # noqa: E402

LESSON, SLUG, TITLE = 'L010', 'l010-what-is-ai', 'AI 是什麼、不是什麼'
CHECKED = '2026-10-07'

SRC = {
    'curriculum': 'curriculum/catalog.json：L010；來源 V2 Excel 逐堂課程第 10 堂',
    'oecd_memo': 'https://comite-etica.upc.edu/ca/actualitat/media/8-sti-explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_final_v3.pdf/@@download/file/8%20-%20STI%20-%20Explanatory%20memorandum%20on%20the%20updated%20OECD%20definition%20of%20an%20AI%20system_FINAL_V3.pdf',
    'oecd_wonk': 'https://oecd.ai/en/wonk/ai-system-definition-update',
    'tw_ai_act': 'https://www.president.gov.tw/File/Doc/80165b6d-cb49-4b49-952f-56e1e6abe51b',
    'unicef3': 'https://www.unicef.org/innocenti/media/11991/file/UNICEF-Innocenti-Guidance-on-AI-and-Children-3-2025.pdf',
    'oak': 'https://www.thenational.academy/pupils/lessons/what-is-artificial-intelligence/video',
    'codeorg_ml': 'https://lesson-plans.code.org/csd7-2026/20260324130350/teacher-lesson-plans/Lesson-1-Introduction-to-Machine-Learning.pdf',
    'microsoft_gen': 'https://www.microsoft.com/en-us/ai/ai-101/how-does-generative-ai-work',
    'mit_sloan': 'https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/',
    'google_parent': 'https://support.google.com/gemini/answer/16109150?hl=en',
    'anthropic_terms': 'https://www.anthropic.com/legal/consumer-terms',
    'moe_genai': 'https://jr.hs.ntnu.edu.tw/wp-content/uploads/2026/02/中小學使用「生成式人工智慧」注意事項2.1.pdf',
    'gmail_ml': 'https://workspace.google.com/blog/product-announcements/keeping-your-company-data-safe-new-security-updates-gmail',
    'apple_faceid': 'https://support.apple.com/en-us/102381',
    'apple_photos': 'https://apple.com/legal/privacy/data/en/photos/',
    'apple_siri': 'https://machinelearning.apple.com/research/hey-siri',
    'claude_age': 'https://support.claude.com/en/articles/13117299-minimum-age-requirement-access-restriction',
    'openai_terms': 'https://openai.com/en-GB/policies/row-terms-of-use/',
    'catalog_reference': 'https://dayofai.org/',
}

SOURCE_RECORDS = [
    {'id': 'oecd_memo', 'title': 'Explanatory memorandum on the updated OECD definition of an AI system（2024-02）', 'publisher': 'OECD（大學網站轉載的 PDF）', 'url': SRC['oecd_memo'], 'usedFor': 'AI 系統定義（根據輸入推論出預測、內容、建議或決策）；規則的例子「If the traffic light is red, stop」；機器學習是從訓練資料找出規律，而不是靠人明確寫出指令。注意：OECD 是把規則當成 AI 系統的一種做法'},
    {'id': 'oecd_wonk', 'title': 'Updates to the OECD definition of an AI system explained（2023-11-29）', 'publisher': 'OECD.AI', 'url': SRC['oecd_wonk'], 'usedFor': '要對 AI 系統的定義取得共識並不容易'},
    {'id': 'tw_ai_act', 'title': '人工智慧基本法 第三條（總統府公報第 7837 號，115 年 1 月 14 日）', 'publisher': '總統府', 'url': SRC['tw_ai_act'], 'usedFor': '台灣法律對人工智慧的定義：透過輸入或感測，經由機器學習及演算法，實現預測、內容、建議或決策等產出'},
    {'id': 'unicef3', 'title': 'Guidance on AI and Children 3.0（2025-12）', 'publisher': 'UNICEF Innocenti', 'url': SRC['unicef3'], 'usedFor': 'AI 系統靠明確規則、從例子學習或試誤來運作；生成式 AI 用統計規律預測接下來的內容；推薦引擎多半靠機器學習；把 AI 看成資料驅動的應用而不是有知覺的機器'},
    {'id': 'oak', 'title': 'What is artificial intelligence?（KS2 Year 4 課程影片逐字稿）', 'publisher': 'Oak National Academy（英格蘭）', 'url': SRC['oak'], 'usedFor': '計算機每次用同樣的步驟；計算機、紅綠燈、紙本字典不使用 AI；語音助理、預測輸入、臉部解鎖使用 AI；只照簡單固定步驟的不是 AI；AI 產生答案但並不理解'},
    {'id': 'codeorg_ml', 'title': 'Introduction to Machine Learning（教師教案）', 'publisher': 'Code.org', 'url': SRC['codeorg_ml'], 'usedFor': '機器學習：電腦辨認規律並做決定，而不是被明確地寫好每一步'},
    {'id': 'microsoft_gen', 'title': 'How Does Generative AI Work', 'publisher': 'Microsoft', 'url': SRC['microsoft_gen'], 'usedFor': '生成式 AI 用機器學習分析大量資料，並產生新的內容'},
    {'id': 'mit_sloan', 'title': 'When AI Gets It Wrong: Addressing AI Hallucinations and Bias', 'publisher': 'MIT Sloan Teaching & Learning Technologies', 'url': SRC['mit_sloan'], 'usedFor': '生成式 AI 像進階的自動完成：依觀察到的規律預測下一個字或序列'},
    {'id': 'google_parent', 'title': "Guide your child's Gemini Apps experience", 'publisher': 'Google Gemini Apps Help', 'url': SRC['google_parent'], 'usedFor': 'Gemini 不是人，不會自己思考或有情緒；可能把不正確的資訊說得像事實；13 歲以下須由家長開啟；不要分享住址、校名等個人資訊'},
    {'id': 'anthropic_terms', 'title': 'Consumer Terms of Service（2025-10-08 生效）', 'publisher': 'Anthropic', 'url': SRC['anthropic_terms'], 'usedFor': '輸出不一定正確，即使看起來很詳細；不應在沒有自行確認的情況下依賴輸出'},
    {'id': 'moe_genai', 'title': '中小學使用「生成式人工智慧」注意事項 2.1（學生版；115 年 2 月 11 日核定）', 'publisher': '教育部（師大附中國中部網站轉載的 PDF）', 'url': SRC['moe_genai'], 'usedFor': '資料有成見或錯誤，結果也會有偏差或錯誤；不可以輸入自己或他人的姓名、照片、聯絡方式、住址、學號；遵守各平臺註冊年齡限制，非在校使用請家長陪伴'},
    {'id': 'gmail_ml', 'title': 'Keeping your company data safe with new security updates to Gmail（2017-06-01）', 'publisher': 'Google Workspace Blog', 'url': SRC['gmail_ml'], 'usedFor': 'Gmail 用機器學習擋下垃圾郵件與釣魚郵件（文中的 99.9% 是 2017 年的數字，本課不引用）'},
    {'id': 'apple_faceid', 'title': 'About Face ID advanced technology（2026-09-18）', 'publisher': 'Apple Support', 'url': SRC['apple_faceid'], 'usedFor': 'Face ID 使用原深感測相機與機器學習；13 歲以下兒童的誤認機率較高'},
    {'id': 'apple_photos', 'title': 'Photos & Privacy（2025-12-12）', 'publisher': 'Apple', 'url': SRC['apple_photos'], 'usedFor': '「照片」用裝置上的機器學習整理照片，包括場景分類、人物與寵物辨識'},
    {'id': 'apple_siri', 'title': 'Hey Siri: An On-device DNN-powered Voice Trigger（2017-10-01）', 'publisher': 'Apple Machine Learning Research', 'url': SRC['apple_siri'], 'usedFor': '教材：「Hey Siri」偵測器使用深度神經網路（語音助理挑戰卡）'},
    {'id': 'claude_age', 'title': 'Minimum age requirement & access restriction（2026-03-16 更新）', 'publisher': 'Claude Help Center', 'url': SRC['claude_age'], 'usedFor': '教材：建立和使用 Claude 帳號須年滿 18 歲'},
    {'id': 'openai_terms', 'title': 'Terms of Use（2026-01-01 生效）', 'publisher': 'OpenAI（只有擷取工具的摘要，沒有逐字確認）', 'url': SRC['openai_terms'], 'usedFor': '教材：須年滿 13 歲，未滿 18 歲需家長或監護人同意；請以官方頁面為準'},
    {'id': 'catalog_reference', 'title': 'Day of AI', 'publisher': 'Day of AI（MIT RAISE 發起）', 'url': SRC['catalog_reference'], 'usedFor': '課表 R07 主要參考網址；其教材需登入且沒有三到六年級單元，本課沒有引用其內容'},
]

SCENES = [
 ('AI 是什麼、不是什麼', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第十堂，主題是 AI：它是什麼、不是什麼，這是依課表製作的課前教學版，並非實際上課錄音。',
  '很多東西都說自己有 AI，可是它們做事的方法，其實很不一樣。',
  '今天你要當分類員，把家裡的十個功能分一分，最後做出一面 AI 功能分類牆。'],
  ['curriculum']),
 ('分類的三個問題', [
  '分類的時候，只要問三個問題。第一個問題：它是不是只照著人寫好的固定步驟做事？',
  '第二個問題：它是不是看過很多例子，自己找出規律？',
  '第三個問題：它會不會做出新的文字、圖片或聲音？如果三個都不是，它可能根本沒有用到 AI。'],
  ['curriculum', 'unicef3']),
 ('AI 沒有魔法', [
  '很多人覺得 AI 像魔法。其實 AI 是人工智慧的簡稱，它是一種電腦系統，會根據收到的資料，推算出預測、建議或是內容。',
  '它是人用程式和大量的資料做出來的，背後是電腦在計算，沒有魔法。',
  '連專家對 AI 的定義都不完全一樣，所以今天不背定義，我們來看每個功能是怎麼做事的。'],
  ['oecd_memo', 'tw_ai_act', 'oecd_wonk', 'unicef3']),
 ('分類牆的四個籃子', [
  '今天的分類牆有四個籃子。第一個是固定規則，電腦照著人寫好的步驟做事，同樣的輸入，每次結果都一樣，例如計算機。',
  '第二個是機器學習，電腦從很多例子裡找出規律；第三個是生成式 AI，它會做出新的內容。',
  '第四個籃子留給不是 AI 的東西，裡面沒有程式在幫忙判斷，例如紙本字典；至於固定規則算不算 AI，專家的分法並不一樣。'],
  ['oak', 'unicef3', 'oecd_memo']),
 ('固定規則和機器學習', [
  '固定規則和機器學習差在哪裡？固定規則是人把每一步都寫好，像是這一條：如果紅燈，就停下來。',
  '機器學習不一樣，沒有人把每一步都寫出來，而是給電腦看很多例子，讓它自己找出規律。',
  '例如過濾垃圾郵件，電腦看過大量的郵件之後，學會分辨哪些像垃圾信；例子不夠，或是有偏差，它就會判斷錯。'],
  ['oecd_memo', 'codeorg_ml', 'gmail_ml', 'moe_genai']),
 ('機器學習：生活裡的例子', [
  '生活裡很多功能都用到機器學習。用臉解鎖手機的時候，手機就是用機器學習來比對你的臉。',
  '手機把照片依照人物、寵物和場景整理好，也是靠機器學習。',
  '影片網站推薦下一部給你看，同樣是從大量的觀看紀錄裡找規律；不過這些功能都有可能認錯，或是推薦錯。'],
  ['apple_faceid', 'apple_photos', 'unicef3', 'oak']),
 ('生成式 AI：會做出新內容', [
  '生成式 AI 也是機器學習的一種，不過它不只是分類，還會做出新的內容，像是文字、圖片和聲音。',
  '它的做法是先讀過非常大量的資料，找出裡面的規律，再一個字接一個字，預測接下來最可能出現什麼。',
  '所以它寫出來的句子很通順，可是通順不代表正確。'],
  ['unicef3', 'microsoft_gen', 'mit_sloan']),
 ('AI 不是什麼？', [
  '再來看 AI 不是什麼。第一，它不是魔法，它是程式、資料和電腦計算做出來的。',
  '第二，它不是人。Google 給家長的說明提醒，聊天機器人雖然很會對話，但它不是人，也沒有情緒。',
  '第三，它不是永遠正確。它可能把錯的事情說得很有把握，所以重要的事，一定要再查證。'],
  ['google_parent', 'unicef3', 'anthropic_terms']),
 ('分類牆競速：十張功能卡', [
  '現在來玩分類牆。桌上有十張功能卡，第一回合比速度：按下計時，把每一張卡貼到四個籃子的其中一個。',
  '第二回合不比快，每一張都要說出理由：它是照固定步驟、從例子學，還是會做出新的內容？理由說得通才得分。',
  '有些卡不只一個答案，例如語音助理裡面，可能同時用到好幾種技術，只要說得出理由就算對。'],
  ['curriculum', 'apple_siri']),
 ('換你設計：擴充分類牆', [
  '下半場換你擴充分類牆。先在家裡找一個新的功能，自己判斷它該放進哪個籃子，並且寫下理由。',
  '再替它寫一張提醒卡，想一想它可能在哪裡出錯。',
  '最後加一條使用 AI 的家庭約定，例如教育部提醒學生，不可以把自己或別人的姓名、照片和住址，輸入生成式 AI。'],
  ['curriculum', 'moe_genai']),
 ('兩小時的 AI 分類課', [
  '兩個小時這樣安排：開場十分鐘，認識三種做事的方法十五分鐘，接著用四十分鐘玩分類牆，再休息十分鐘。',
  '下半場用三十分鐘擴充分類牆、寫使用 AI 的家庭約定，然後用十分鐘交換角色，由孩子教爸爸怎麼分類。',
  '最後五分鐘錄音總結，替分類牆取名字、拍照存檔，再貼在家裡看得到的地方。'],
  ['curriculum']),
 ('最後一關：教爸爸分類', [
  '最後一關，請不看稿，在家裡找一個新的功能，當著爸爸的面分類一次，並且說出你的理由。',
  '再指出一個限制或安全注意事項，例如生成式 AI 的回答可能是錯的，重要的事要再查證。',
  '今天的作品是 AI 功能分類牆，下次我們要學怎麼寫出第一個好提示詞；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum', 'anthropic_terms']),
]

VISIBLE = [
 ['第十堂任務', 'AI 是什麼、\n不是什麼', '看它怎麼做事，把家裡的功能分一分', '第十堂  ·  依課表製作的課前教學版'],
 ['分類的三個問題', '看它怎麼做事，不是看它叫什麼名字',
  '01 固定步驟？', '是不是只照著\n人寫好的步驟做', '→',
  '02 從例子學？', '是不是看過很多例子\n自己找出規律', '→',
  '03 做新內容？', '會不會做出新的\n文字、圖片或聲音',
  '今天的作品：AI 功能分類牆'],
 ['AI 沒有魔法', 'AI 是人工智慧的簡稱，是人做出來的電腦系統',
  '01', '它在做什麼', '根據收到的資料，推算出預測、建議或內容',
  '02', '它是怎麼來的', '人用程式和大量資料做出來的',
  '03', '定義不只一種', '連專家的說法都不完全一樣'],
 ['分類牆的四個籃子', '每個功能，放進最像的一個籃子', '四個籃子',
  '固定規則', '照人寫好的步驟', '機器學習', '從例子找規律', '生成式 AI', '做出新的內容', '不是 AI', '沒有程式在判斷',
  '固定規則算不算 AI，專家的分法不一樣'],
 ['固定規則和機器學習', '一個靠人寫好的步驟，一個靠很多例子',
  '固定規則', '人把每一步寫好：如果紅燈，就停', '≠', '機器學習', '給電腦看很多例子，讓它自己找規律',
  '同樣的輸入，固定規則每次結果都一樣',
  '例子不夠或有偏差，機器學習就會判斷錯'],
 ['機器學習：生活裡的例子', '從大量的例子裡找規律，再判斷新的東西',
  '01 臉部解鎖', '比對你的臉', '02 照片整理', '認出人物、寵物、場景', '03 影片推薦', '從觀看紀錄找規律',
  '這些功能都可能認錯，或是推薦錯'],
 ['生成式 AI：會做出新內容', '它也是機器學習，但不只是分類',
  '讀大量資料  →  找出規律  →  預測下一個字',
  '寫文字', '故事、摘要、回答', '畫圖片', '照文字描述畫出來', '接著說', '像在和你聊天',
  '句子通順，不代表內容正確'],
 ['AI 不是什麼？', '知道它的限制，才用得安全',
  '一、不是魔法：是程式、資料和計算\n二、不是人：很會對話，但沒有情緒\n三、不是永遠正確：會說錯還很有把握',
  '所以要記得', '重要的事，一定要再查證', '問爸爸\n或查可靠的來源',
  '暫停影片：說出 AI 不是的三件事'],
 ['分類牆競速：十張功能卡', '先比快，再比誰的理由說得通',
  '第一回合：計時分類', '十張卡貼到四個籃子\n記下花了幾秒',
  '第二回合：說出理由', '每張卡說它怎麼做事\n理由說得通才得分',
  '有些卡不只一個答案，說得出理由就算對'],
 ['換你設計：擴充分類牆', '加一個新功能，再加一條家庭 AI 約定',
  '01', '找一個家裡的新功能', '自己判斷它該放哪個籃子，寫下理由',
  '02', '替它寫一張提醒卡', '它可能在哪裡出錯？',
  '03', '加一條家庭 AI 約定', '例如：不輸入姓名、照片、住址等個資'],
 ['兩小時的 AI 分類課', '影片先引路，接下來用功能卡練習分類',
  '00–25', '開場十分＋概念十五分', '25–65', '功能分類牆競速', '65–75', '休息十分鐘',
  '75–105', '擴充分類牆＋家庭約定', '105–115', '孩子教爸爸分類', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：數位公民，AI 的回答要自己再查證'],
 ['最後一關：教爸爸分類', '暫停影片：不看稿示範一次，再指出一個限制或安全注意',
  '01', '完成 AI 功能分類牆', '十張卡都有籃子和理由',
  '02', '當場分類一個新功能', '說出它是怎麼做事的',
  '03', '指出一個限制或安全注意', '例如：AI 的回答可能是錯的，要再查證',
  '保持好奇，我們下次見！'],
]

BOARD = [
 ('開場：課前教學版揭露、都叫 AI 但做法不同、分類任務與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備功能卡與分類牆；預告競速與作品'),
 ('概念：分類三問（固定步驟？從例子學？做新內容？）', '三步流程卡＋黃字作品', '說出今天要完成的作品'),
 ('概念：AI 是人做的電腦系統，沒有魔法；定義不只一種', '三點條列＋陳犀牛', '用自己的話說「AI 沒有魔法」是什麼意思'),
 ('概念：四個籃子（固定規則、機器學習、生成式 AI、不是 AI）；界線有爭議', '面板四張卡＋黃字說明', '各說一個例子'),
 ('概念：固定規則是人寫步驟；機器學習是從例子找規律，例子有偏差就會錯', '雙框對照（固定規則 ≠ 機器學習）＋白字＋黃字', '說出兩者差在哪裡'),
 ('示範：臉部解鎖、照片整理、影片推薦都用到機器學習，也都會錯', '三張步驟卡＋黃字提醒', '再想一個家裡用到機器學習的功能'),
 ('概念：生成式 AI 預測接下來的內容；通順不代表正確', '路徑一行（讀大量資料→找出規律→預測下一個字）＋三張卡', '說出生成式 AI 和照片整理差在哪裡'),
 ('安全：AI 不是魔法、不是人、不是永遠正確；重要的事要查證', '左側三行；右側「所以要記得」', '暫停影片：說出 AI 不是的三件事'),
 ('活動規則：十張功能卡，先計時分類，再逐張說理由', '左右比較卡（計時分類／說出理由）＋黃字', '兩回合分類；記錄秒數與理由'),
 ('獨立改造與安全：自選新功能、提醒卡、家庭 AI 約定（不輸入個資）', '三點條列＋陳犀牛', '完成自選功能卡與一條家庭 AI 約定'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：當場分類一個新功能，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子教爸爸；錄音回答四個問題；作品命名存檔'),
]

FACT_CHECK = '''# L010 事實查核

查核日：2026-10-07。查核者：製作代理（Claude）與其派出的研究子代理。
方法：子代理下載各來源的原始頁面或 PDF、抽取文字後回報逐字引文（原文見 `source-notes.md`）；主代理再把引文和旁白、投影片、教材逐句比對。
限制：主代理沒有逐頁重讀來源；OpenAI 的條款與說明頁只有擷取工具的摘要，沒有逐字確認，本課只在教材的年齡說明提到並註明；
UNESCO 的生成式 AI 指引全文讀不到，沒有引用；Day of AI 的教材需要登入，沒有取得；來源多為英文，中文是本課轉述。

## 主張與來源

| # | 本課的說法（幕） | 來源依據 | 結論 |
|---|---|---|---|
| 1 | AI 是一種電腦系統，會根據收到的資料，推算出預測、建議或內容（3） | OECD：AI system “infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions”；人工智慧基本法第三條：「透過輸入或感測，經由機器學習及演算法，可為明確或隱含之目標實現預測、內容、建議或決策等…產出」 | 相符（簡化；省略「決策」與「影響環境」） |
| 2 | AI 是人用程式和資料做出來的，背後是電腦在計算，沒有魔法（3、8） | 課表學習目標「理解 AI 沒有魔法」；UNICEF：把 AI 系統看成 “data-driven applications rather than sentient machines” | 相符；「沒有魔法」是課表用語 |
| 3 | 連專家對 AI 的定義都不完全一樣（3） | OECD.AI：“Obtaining consensus on a definition for an AI system … has proven to be a complicated task.”；OECD、NIST、台灣基本法的定義文字各不相同 | 相符 |
| 4 | 固定規則：電腦照人寫好的步驟做，同樣的輸入每次結果都一樣，例如計算機（4、5） | Oak：“A computer can follow fixed rules. For example, a calculator always adds numbers using the same steps.” | 相符 |
| 5 | 規則的例子：如果紅燈，就停下來（5） | OECD：“a driving system might have a rule, ‘If the traffic light is red, stop.’” | 相符；OECD 是把它當成 AI 系統裡的規則 |
| 6 | 固定規則算不算 AI，專家的分法不一樣（4） | Oak：“If it only follows simple fixed steps, it is not AI.”；UNICEF：“AI systems work by either following explicit rules, learning from examples … or improving through trial and error”；OECD 把規則列為 AI 系統的做法 | 相符；本課因此把「固定規則」和「不是 AI」分成兩個籃子，並說明界線有爭議 |
| 7 | 機器學習：沒有人把每一步寫出來，電腦從很多例子找出規律（4、5） | OECD：“…identify patterns and regularities rather than through explicit instructions from a human”；Code.org：“recognize patterns and make decisions without being explicitly programmed” | 相符 |
| 8 | 過濾垃圾郵件用到機器學習（5） | Google（2017）：“Machine learning helps Gmail block sneaky spam and phishing messages” | 相符；沒有引用文中的百分比（2017 年的數字） |
| 9 | 例子不夠或有偏差，就會判斷錯（5） | 教育部注意事項 2.1：「如果這些資料本身具有成見或錯誤，那麼…結果也會存在偏差或錯誤」 | 相符；教育部談的是生成式 AI 工具，本課用在機器學習，屬合理延伸；「例子不夠」是本課補充 |
| 10 | 用臉解鎖手機用到機器學習（6） | Apple：“Face ID uses the TrueDepth camera and machine learning”；Oak：face-unlock 使用 AI | 相符；Apple 的說法只針對 Face ID |
| 11 | 手機把照片依人物、寵物、場景整理，靠機器學習（6） | Apple：“Photos uses on-device machine learning … scene classification, people and pets identification” | 相符；只針對 Apple「照片」 |
| 12 | 影片推薦是從大量紀錄裡找規律（6） | UNICEF：“Most AI applications in use today – from recommendation engines to smart robots – rely on machine learning techniques that recognize patterns in data.” | 相符；「觀看紀錄」是本課的白話說法，沒有針對特定網站查核 |
| 13 | 這些功能都可能認錯或推薦錯（6） | Apple：Face ID 的誤認機率在 13 歲以下兒童較高；其餘為一般常識 | 臉部解鎖有來源；照片整理與推薦「可能出錯」沒有另找來源 |
| 14 | 生成式 AI 是機器學習的一種，會做出新的文字、圖片、聲音；做法是預測接下來最可能出現什麼（7） | UNICEF：“generate new content by using statistical patterns to predict what comes next in language, images and other media”；Microsoft：“uses advanced machine learning techniques … generate new content”；MIT Sloan：“function like advanced autocomplete tools” | 相符；「一個字接一個字」是針對文字的簡化說法 |
| 15 | 通順不代表正確；它可能把錯的事說得很有把握，重要的事要查證（7、8、12） | Google：Gemini “can hallucinate and present inaccurate information as factual”；Anthropic：輸出 “may contain material inaccuracies even if they appear accurate”，“should not rely on any Outputs … without independently confirming their accuracy” | 相符 |
| 16 | Google 給家長的說明提醒：聊天機器人很會對話，但不是人，也沒有情緒（8） | Google：“although Gemini is conversational, it's not a person and cannot think for itself or feel emotions.” | 相符；旁白有標明出處。原文談的是 Gemini，本課說成「聊天機器人」；這是廠商給家長的提醒，不是研究結論 |
| 17 | 語音助理可能同時用到好幾種技術（9） | Apple（2017）：「Hey Siri」偵測器使用深度神經網路；Oak：voice assistant 使用 AI | 部分相符；「好幾種技術」「可能」是本課的說法，沒有查核任何一款助理的內部做法 |
| 18 | 教育部提醒學生：不可以把自己或別人的姓名、照片、住址輸入生成式 AI（10） | 教育部注意事項 2.1 學生版：「不可以將自己或他人的姓名、照片、聯絡方式、住址、學號等個人資料…輸入至『生成式人工智慧』工具。」 | 相符（節錄其中三項） |

## 刻意避免的說法

- 沒有說「固定規則的程式不是 AI」是定論；沒有說鬧鐘、計時器、電燈開關的分類有官方來源（那是本課自己的例子）。
- 沒有說 AI 會理解、思考或有感覺；也沒有不加出處地說「科學已經證明它什麼都不懂」。
- 沒有說 AI 知道自己錯了或會自己查證。
- 沒有說孩子可以自己開 ChatGPT、Gemini 或 Claude 帳號；各平臺的年齡限制寫在教材，本課不需要孩子操作任何生成式 AI 工具。
- 沒有引用「Gmail 擋下 99.9% 垃圾郵件」這個 2017 年的數字，沒有說 Face ID 是生成式 AI 或不會出錯。
- 沒有說「你輸入的每一樣東西都會被拿去訓練」；教育部的說法是「可能」。
- 沒有說 UNESCO 禁止 13 歲以下使用 AI；那份指引的全文這次沒有讀到。

## 課程與素材

- 課程主題、學習目標、120 分鐘流程（10／15／40／10／30／10／5）、動手任務（把家中 10 個功能分類為規則、機器學習、生成式 AI 或非 AI）、
  作品（AI 功能分類牆）與驗收，依 `curriculum/catalog.json` L010 核對。
- 沒有課堂錄音；本集是**依課表製作的課前教學版**，未虛構逐字稿或父子對話，封面、旁白第一句與說明均已揭露。
- 「分類三問」「四個籃子」是本課的教學包裝。課表的好玩機制是競速，本課只在第一回合計時，理由不計時。
- 課表主要參考網址（R07）是 Day of AI。它的課程頁沒有三到六年級的單元，教材需要登入；本課沒有引用它的內容。
- 課表的三組 YouTube 連結是動態搜尋入口；本次沒有挑選、觀看或引用任何影片。
'''

PLAN = '''# L010 AI 是什麼、不是什麼

依課表製作的課前教學版；沒有課堂錄音，不製造逐字稿。
沿用原片頭 v2、陳犀牛、深藍／黃／青、12 頁原生可編輯簡報、36 句旁白、zh-TW-YunJheNeural；
教學段落靜態畫面加 0.55 秒淡化，無背景音樂、無推拉鏡頭。

## 課表核對（curriculum/catalog.json L010）

- 模組：M01 數位探險家；難度 2；主軸：數位素養／AI 素養／網路安全。
- 學習目標：區分規則式程式、機器學習與生成式 AI；理解 AI 沒有魔法。
- 動手任務：把家中 10 個功能分類為規則、ML、生成式 AI 或非 AI。好玩機制：競速。
- 作品：AI 功能分類牆。生活技能支線：數位公民。
- 驗收：完成作品；不看稿說出核心原理；指出至少一個錯誤、限制或安全注意事項。

## 120 分鐘（課堂，與影片片長分開）

| 分鐘 | 內容 | 對應影片頁 |
|---|---|---|
| 00–10 | 任務開場：拿兩張功能卡問孩子「哪一個是 AI？你怎麼知道？」 | 1–2 |
| 10–25 | 概念示範：AI 沒有魔法、四個籃子、固定規則與機器學習、生成式 AI、AI 不是什麼 | 3–8 |
| 25–65 | 共同實作：十張功能卡分類牆競速（計時分類＋說理由） | 9 |
| 65–75 | 休息 | — |
| 75–105 | 孩子獨立改造：自選新功能、提醒卡、一條家庭 AI 約定 | 10 |
| 105–115 | 角色互換：孩子教爸爸分類一個新功能 | 12 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 11–12 |

## 12 頁

1 開場與揭露｜2 分類三問｜3 AI 沒有魔法｜4 四個籃子｜5 固定規則和機器學習｜6 機器學習的例子｜7 生成式 AI｜
8 AI 不是什麼｜9 分類牆競速｜10 擴充分類牆與家庭約定｜11 兩小時安排｜12 驗收與結尾。

## 設計取捨

- 「固定規則」和「不是 AI」分成兩個籃子，並在影片與教材說明：固定規則算不算 AI，各方說法不同（Oak 說不算；UNICEF 與 OECD 把規則列為 AI 系統的做法）。
- 不背定義，改用三個問題看「它怎麼做事」。
- 關於「AI 不是人、沒有情緒」的說法都標明出處（Google 給家長的說明），不當成科學結論。
- 這堂課不需要孩子操作任何生成式 AI 工具；各平臺有年齡限制，要示範時由爸爸用自己的帳號操作，而且不輸入個資。
- 競速只用在第一回合的分類；理由不計時，放錯的卡會加秒，避免只求快。
- 十張功能卡之外另有兩張「不只一個答案」的挑戰卡（語音助理、鍵盤選字）。

## 作品與驗收

- AI 功能分類牆（四個籃子、十張功能卡、每張有理由）。
- 競速紀錄表。
- 自選功能卡、提醒卡、一條家庭 AI 約定。
- 孩子教爸爸：不看稿分類一個新功能，並指出一個限制或安全注意事項。
- 錄音四問（錄音只留私人區）。

## 教材

`classroom/L010_AI是什麼不是什麼/`：爸爸先讀、功能分類牆競速規則、6 頁列印包（分類小抄卡、十六張功能卡、兩頁分類牆底板、
競速紀錄表、提醒卡與家庭 AI 約定卡）、分類紀錄（CSV＋說明）、功能卡解說、自選功能與家庭 AI 約定、驗收與回顧、AI 分類小抄。
由 `authoring/l010/classroom.py` 產生；內容與來源查核見 fact-check.md。
'''

SUMMARY = '''這是依課表製作的課前教學版，不是實際上課錄音，也沒有虛構的課堂對話。

很多東西都說自己有 AI，可是它們做事的方法很不一樣。陳犀牛帶你當分類員：只要問三個問題，就能把家裡的功能分進四個籃子。
看完影片，用十張功能卡玩分類牆競速，最後做出一面自己的 AI 功能分類牆。

這一集會學到
・AI 是人用程式和資料做出來的電腦系統，沒有魔法
・四個籃子：固定規則、機器學習、生成式 AI、不是 AI
・機器學習是從很多例子找規律；生成式 AI 會預測接下來的內容，做出新的文字、圖片和聲音
・AI 不是魔法、不是人、不是永遠正確；重要的事要再查證，不輸入個資

教材用法（classroom.zip）
先讀「00_爸爸先讀」，列印「02_列印包」（A4 共 6 頁），照「01_活動規則」玩功能分類牆競速，用「03_分類紀錄」記錄；
解說在「04_功能卡解說」，下半場完成「05_自選功能與家庭AI約定」，最後用「06_驗收與回顧」讓孩子教爸爸。「07_AI分類小抄」可以貼在電腦旁邊。

注意事項
・課堂是 120 分鐘，影片只是課前引導，片長另計。
・固定規則的程式算不算 AI，各方說法不同；本課把它放在自己的籃子，重點是看它怎麼做事。
・這堂課不需要孩子操作任何生成式 AI 工具。各平臺有年齡限制，要示範時請由爸爸用自己的帳號操作，並且不輸入姓名、照片、住址等個資。
・功能卡的分類沒有唯一答案，說得出理由比較重要。

來源（查核日 2026-10-07）
教育部「中小學使用『生成式人工智慧』注意事項 2.1」（115 年 2 月核定）
人工智慧基本法第三條（總統府公報）：https://www.president.gov.tw/File/Doc/80165b6d-cb49-4b49-952f-56e1e6abe51b
OECD.AI「Updates to the OECD definition of an AI system explained」：https://oecd.ai/en/wonk/ai-system-definition-update
UNICEF「Guidance on AI and Children 3.0」：https://www.unicef.org/innocenti/media/11991/file/UNICEF-Innocenti-Guidance-on-AI-and-Children-3-2025.pdf
Oak National Academy「What is artificial intelligence?」：https://www.thenational.academy/pupils/lessons/what-is-artificial-intelligence/video
Google「Guide your child's Gemini Apps experience」：https://support.google.com/gemini/answer/16109150?hl=en
Apple「About Face ID advanced technology」：https://support.apple.com/en-us/102381
'''

if __name__ == '__main__':
    lesson_builder.build(
        lesson=LESSON, slug=SLUG, ordinal='十', title=TITLE, header_en='AI SORTING WALL', checked=CHECKED,
        src=SRC, scenes=SCENES, visible=VISIBLE, board=BOARD,
        render_options={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        tts_basis="On 2026-10-07 the user asked to produce L007–L010 'following this process' (the L004–L006 process, which "
                  "sends the public narration script to Edge TTS); stated back to the user before synthesis.",
        source_records=SOURCE_RECORDS,
        source_method='A research subagent downloaded each page/PDF on the check date and reported verbatim quotes '
                      '(production/source-notes.md); the producing agent mapped them to claims. Not a human full read.',
        not_verified=['Day of AI 的教材需要登入，沒有取得；其課程頁沒有三到六年級單元，本課沒有引用其內容',
                      'OpenAI 的條款與說明頁只有擷取工具的摘要，沒有逐字確認',
                      'UNESCO 生成式 AI 指引全文無法讀取，未引用',
                      '台灣適用的各平臺最低年齡，以及 Gemini 在台灣對兒童的開放情形，沒有查核',
                      '鬧鐘、電燈開關的分類沒有官方來源，是本課自己的例子',
                      '行政院生成式 AI 參考指引的十點只見於新聞轉載，未引用'],
        documents={'fact-check.md': FACT_CHECK, 'plan.md': PLAN, 'delivery-summary.md': SUMMARY,
                   'source-notes.md': (Path(__file__).resolve().parent / 'source-notes.md').read_text(encoding='utf-8')},
        readme=lesson_builder.readme(LESSON, TITLE))
