"""Author L012 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable. Holds only this lesson's text; authoring/lesson_builder.py writes the files.
After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l012/prepare_content.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lesson_builder  # noqa: E402

LESSON, SLUG, TITLE = 'L012', 'l012-ai-hallucination', 'AI 會亂講：幻覺抓錯賽'
CHECKED = '2026-10-08'

SRC = {
    'curriculum': 'curriculum/catalog.json：L012；來源 V2 Excel 逐堂課程第 12 堂',
    'nist_genai': 'https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf',
    'ibm_hallucination': 'https://www.ibm.com/think/topics/ai-hallucinations',
    'mit_sloan': 'https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/',
    'gemini_responses': 'https://support.google.com/gemini/answer/16279220?hl=zh-Hant',
    'eliteracy_ai': 'https://eliteracy.edu.tw/Download.ashx?id=1817',
    'openai_truth': 'https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth',
    'openai_search': 'https://help.openai.com/en/articles/9237897-chatgpt-search',
    'google_ai_overviews': 'https://support.google.com/websearch/answer/14901683?hl=zh-Hant',
    'mata_order': 'https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_3.pdf',
    'moe_genai': 'https://jr.hs.ntnu.edu.tw/wp-content/uploads/2026/02/中小學使用「生成式人工智慧」注意事項2.1.pdf',
    'anthropic_terms': 'https://www.anthropic.com/legal/consumer-terms',
    'irf_rhino': 'https://rhinos.org/about-rhinos/state-of-the-rhino/',
    'irf_species': 'https://rhinos.org/about-rhinos/rhino-species/',
    'save_the_rhino': 'https://www.savetherhino.org/rhino-info/population-figures/',
    'ysnp_terrain': 'https://www.ysnp.gov.tw/StaticPage/Terrain',
    'ysnp_vision': 'https://www.ysnp.gov.tw/StaticPage/Vision',
    'ey_parks': 'https://www.ey.gov.tw/state/4447F4A951A1EC45/dc08391a-c57c-4cf7-af9a-cc0d9e4ebb1c',
    'ysnp_bear': 'https://www.ysnp.gov.tw/StaticPage/Science',
    'forest_bear': 'https://www.forest.gov.tw/MagazineFile/6855',
    'nasa_moon': 'https://science.nasa.gov/moon/facts/',
    'nasa_apollo11': 'https://www.nasa.gov/centers-and-facilities/kennedy/50-years-ago-apollo-astronauts-land-take-first-steps-on-moon/',
    'nasa_apollo11_history': 'https://www.nasa.gov/wp-content/uploads/static/history/ap11ann/FirstLunarLanding/ch-1.html',
    'nasa_moonwalkers': 'https://science.nasa.gov/moon/moon-walkers/',
    'nasa_sunlight': 'https://astrobiology.nasa.gov/quick-facts/more-quick-facts/',
    'catalog_reference': 'https://academy.openai.com/',
}

SOURCE_RECORDS = [
    {'id': 'nist_genai', 'title': 'NIST AI 600-1：Generative Artificial Intelligence Profile（2024-07）', 'publisher': 'U.S. National Institute of Standards and Technology', 'url': SRC['nist_genai'], 'usedFor': '生成式 AI 會產生並有自信地呈現錯誤或虛假的內容（confabulation，俗稱 hallucination）；這是預測下一個字的設計造成的；連用來支持答案的引用也可能是編的'},
    {'id': 'ibm_hallucination', 'title': 'What Are AI Hallucinations?（2023-09-01；2026-07-31 更新）', 'publisher': 'IBM', 'url': SRC['ibm_hallucination'], 'usedFor': '聽起來合理、實際上錯誤或完全捏造的輸出；假事實、編造的研究、不存在的網址、關於真實對象的錯誤細節'},
    {'id': 'mit_sloan', 'title': 'When AI Gets It Wrong: Addressing AI Hallucinations and Bias', 'publisher': 'MIT Sloan Teaching & Learning Technologies', 'url': SRC['mit_sloan'], 'usedFor': '生成式 AI 像進階的自動完成，依規律預測下一個字；目標是產生看似合理的內容，不是驗證真假'},
    {'id': 'gemini_responses', 'title': '瞭解 Gemini 應用程式的回覆', 'publisher': 'Google Gemini 應用程式說明', 'url': SRC['gemini_responses'], 'usedFor': '中文用詞：「Gemini 可能會產生幻覺，將不準確的資訊當做事實」'},
    {'id': 'eliteracy_ai', 'title': '教案【AI的練習曲】（高中；設計者 國立陽明交通大學）', 'publisher': '教育部 中小學數位素養教育資源網', 'url': SRC['eliteracy_ai'], 'usedFor': '「AI可能會有幻覺」；統計數據、名言、法條、專有名詞應至原始文件或官方網站核實；交叉比對搜尋、追溯原始資料'},
    {'id': 'openai_truth', 'title': 'Does ChatGPT tell the truth?', 'publisher': 'OpenAI Help Center（只有擷取工具的摘要，沒有逐字確認）', 'url': SRC['openai_truth'], 'usedFor': '錯誤的日期或事實；編造的引言、研究、引用或不存在的來源；過度自信的回答；請自行查證引言、數據與引用'},
    {'id': 'openai_search', 'title': 'Searching the web with ChatGPT', 'publisher': 'OpenAI Help Center（只有擷取工具的摘要，沒有逐字確認）', 'url': SRC['openai_search'], 'usedFor': '搜尋結果與引用可能不完整、過時或不正確；打開引用的來源確認它支持答案'},
    {'id': 'google_ai_overviews', 'title': 'Google 搜尋的 AI 摘要說明', 'publisher': 'Google 搜尋說明', 'url': SRC['google_ai_overviews'], 'usedFor': '「務必多方查證重要資訊。點按連結，參閱網路上的佐證資訊和其他 Google 搜尋結果。」；無法確保 AI 摘要內容皆正確無誤'},
    {'id': 'mata_order', 'title': 'Mata v. Avianca, Inc.，Opinion and Order on Sanctions（No. 22-cv-1461，2023-06-22）', 'publisher': '美國紐約南區聯邦地方法院（CourtListener 的 RECAP 存檔）', 'url': SRC['mata_order'], 'usedFor': '兩位律師與事務所提交了由 ChatGPT 產生、並不存在的六個判決與假引文，共同被處以 5,000 美元罰款；律師回頭問它案例是不是真的，它回答是真的'},
    {'id': 'moe_genai', 'title': '中小學使用「生成式人工智慧」注意事項 2.1（學生版；115 年 2 月 11 日核定）', 'publisher': '教育部（師大附中國中部網站轉載的 PDF）', 'url': SRC['moe_genai'], 'usedFor': '不能全盤接受生成的內容，需結合其他可靠來源查證；有疑慮向老師或家長請教；不可以直接將生成內容作為作業或報告的原始答案'},
    {'id': 'anthropic_terms', 'title': 'Consumer Terms of Service（2025-10-08 生效）', 'publisher': 'Anthropic', 'url': SRC['anthropic_terms'], 'usedFor': '輸出即使看起來很詳細也可能不正確；不應在沒有自行確認的情況下依賴輸出'},
    {'id': 'irf_rhino', 'title': '2026 State of the Rhino（2026-09）', 'publisher': 'International Rhino Foundation', 'url': SRC['irf_rhino'], 'usedFor': '教材資料卡：現存五種犀牛；全球約 26,700 隻；爪哇犀牛約 50 隻'},
    {'id': 'irf_species', 'title': 'Rhino Species（各物種頁面）', 'publisher': 'International Rhino Foundation', 'url': SRC['irf_species'], 'usedFor': '教材資料卡：白犀牛、黑犀牛、蘇門答臘犀牛有兩支角，大獨角犀與爪哇犀牛一支；角是角蛋白，和指甲、頭髮同樣的材料；嗅覺與聽覺靈敏、視力不好'},
    {'id': 'save_the_rhino', 'title': 'Rhino population figures', 'publisher': 'Save the Rhino International', 'url': SRC['save_the_rhino'], 'usedFor': '教材資料卡：與 IRF 相同的族群數字（2025 年由 IUCN 專家小組回報）'},
    {'id': 'ysnp_terrain', 'title': '地形地質（更新日期 115-10-08）', 'publisher': '玉山國家公園管理處', 'url': SRC['ysnp_terrain'], 'usedFor': '教材資料卡：玉山主峰海拔 3,952 公尺'},
    {'id': 'ysnp_vision', 'title': '願景與沿革', 'publisher': '玉山國家公園管理處', 'url': SRC['ysnp_vision'], 'usedFor': '教材資料卡：臺灣第一高峰；玉山國家公園為我國第 2 座國家公園'},
    {'id': 'ey_parks', 'title': '國情簡介：國家公園簡介（114-04-21，資料來源：內政部）', 'publisher': '行政院', 'url': SRC['ey_parks'], 'usedFor': '教材資料卡：玉山國家公園成立時間 74 年 4 月'},
    {'id': 'ysnp_bear', 'title': '臺灣黑熊科普（更新日期 115-10-08）', 'publisher': '玉山國家公園管理處', 'url': SRC['ysnp_bear'], 'usedFor': '教材資料卡：瀕臨絕種野生動物；胸前黃白色 V 字形或新月形斑紋；族群約 200~600 隻'},
    {'id': 'forest_bear', 'title': '臺灣黑熊救援案件紀實（林業期刊）', 'publisher': '農業部林業及自然保育署', 'url': SRC['forest_bear'], 'usedFor': '教材資料卡：全島族群數量推估約有數百隻（與上一個來源的數字不同，用來說明估計值）'},
    {'id': 'nasa_moon', 'title': 'Moon Facts', 'publisher': 'NASA Science', 'url': SRC['nasa_moon'], 'usedFor': '教材資料卡：月球與地球平均距離 384,400 公里'},
    {'id': 'nasa_apollo11', 'title': '50 Years Ago: Apollo Astronauts Land, Take First Steps on Moon（2019-07-20）', 'publisher': 'NASA', 'url': SRC['nasa_apollo11'], 'usedFor': '教材資料卡：阿姆斯壯、艾德林登月，柯林斯留在指揮艙繞月'},
    {'id': 'nasa_apollo11_history', 'title': 'The First Lunar Landing', 'publisher': 'NASA History', 'url': SRC['nasa_apollo11_history'], 'usedFor': '教材資料卡：1969 年 7 月 20 日（美國東部時間）登月艙降落月球'},
    {'id': 'nasa_moonwalkers', 'title': 'Moon Walkers', 'publisher': 'NASA Science', 'url': SRC['nasa_moonwalkers'], 'usedFor': '教材資料卡：一共 12 個人在月球上走過'},
    {'id': 'nasa_sunlight', 'title': 'More Quick Facts', 'publisher': 'NASA Astrobiology', 'url': SRC['nasa_sunlight'], 'usedFor': '教材資料卡：陽光從太陽到地球需要 8 分 20 秒'},
    {'id': 'catalog_reference', 'title': 'OpenAI Academy', 'publisher': 'OpenAI（課表 R20 的主要參考網址）', 'url': SRC['catalog_reference'], 'usedFor': '課表列出的參考入口；本課沒有引用其中任何一頁'},
]

SCENES = [
 ('AI 會亂講：幻覺抓錯賽', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第十二堂，幻覺抓錯賽，這是依課表製作的課前教學版，並非實際上課錄音。',
  '生成式 AI，有時候會把錯的事情說得跟真的一樣，這種情形常被叫做幻覺。',
  '今天你要當偵探，從回答裡找出需要查證的地方，最後完成一張回答查核表。'],
  ['curriculum', 'nist_genai', 'gemini_responses']),
 ('抓錯的三個步驟', [
  '抓錯有三個步驟。第一步是標記，把回答裡的名稱、數字、日期和引用圈起來。',
  '第二步是查證，到可靠的來源去找，看看它說得對不對。',
  '第三步是判定，寫下結果：正確、錯誤，或是查不到；查不到的，就不能當成真的。'],
  ['curriculum', 'moe_genai']),
 ('AI 幻覺：說得很順，卻是錯的', [
  '有時候，回答讀起來很通順、很有把握，內容卻是錯的，甚至是編出來的；這種情形，大家叫它幻覺。',
  '會這樣，是因為它的做法是預測接下來最可能出現的字，目標是寫得通順，而不是確認真假。',
  '就算回答後面附了來源連結，也還是可能出錯，所以一樣要查。'],
  ['nist_genai', 'ibm_hallucination', 'mit_sloan', 'openai_search', 'google_ai_overviews']),
 ('最需要查的四種東西', [
  '回答裡有四種東西最需要查。第一種是名稱，像是人名、地名和書名；第二種是數字，例如多高、多少隻。',
  '第三種是日期，哪一年、哪一天；第四種是引用，也就是它說資料來自哪一本書、哪一個網站。',
  '還有第五種要留意：說得太肯定的話，例如一定、剛好、所有；真實世界的數字，常常只是估計。'],
  ['curriculum', 'openai_truth', 'ibm_hallucination', 'eliteracy_ai', 'ysnp_bear', 'forest_bear']),
 ('引用也可能是編的', [
  '引用特別要小心，因為連書名、網址和案例，都可能是編出來的。',
  '二零二三年，美國有兩位律師請聊天機器人找判決，它編出了六個根本不存在的案例；律師交給法院之後，和事務所一起被罰了五千美元。',
  '所以看到引用，要自己去確認兩件事：它真的存在嗎？裡面真的這樣寫嗎？'],
  ['nist_genai', 'ibm_hallucination', 'mata_order', 'openai_search']),
 ('怎麼查證？', [
  '怎麼查呢？第一，找原始的來源，例如官方網站，或是它說的那本書。',
  '第二，再找第二個可靠的來源，看看兩邊說的一不一樣；重要的事，多查一個地方比較保險。',
  '第三，查不到，或是看不懂，就問爸爸或老師；只是回頭再問它一次你確定嗎，不算查證。'],
  ['eliteracy_ai', 'google_ai_overviews', 'moe_genai', 'mata_order']),
 ('判定：正確、錯誤、查不到', [
  '查完之後要判定。可靠的來源也這樣說，就是正確；和可靠的來源不一樣，就是錯誤。',
  '如果怎麼查都查不到，就寫查不到，而且先不要把它當成真的。',
  '還要記得，一個回答裡，對的和錯的可能混在一起，所以要一句一句看。'],
  ['curriculum', 'ibm_hallucination']),
 ('三種特別要小心的時候', [
  '有三種時候特別要小心。第一，要用在作業和報告的內容，一定先查證，再使用。',
  '第二，和健康、金錢、安全有關的事，不要只聽它的，一定要問大人。',
  '第三，查證的人也會出錯，所以重要的事要找第二個來源；發現錯誤就告訴爸爸，不要直接轉傳出去。'],
  ['moe_genai', 'anthropic_terms', 'google_ai_overviews']),
 ('幻覺抓錯賽：三則模擬回答', [
  '現在開始抓錯賽。教材裡有三則模擬回答，是這堂課特地編寫的，裡面故意藏了錯誤；請在每一則至少圈出三個需要查證的地方。',
  '接著拿出資料卡，或是和爸爸一起上官方網站查，把每個地方判定成正確、錯誤，或是查不到。',
  '找到錯誤之後，還要說出它是哪一種：名稱、數字、日期、引用，還是說得太肯定。'],
  ['curriculum']),
 ('換你設計：AI 回答查核表', [
  '下半場換你設計自己的回答查核表，欄位由你決定，至少要有：哪一句話、是哪一種、去哪裡查，還有查到的結果。',
  '再加一條你自己的偵探規則，例如只要是數字，就一定查兩個地方。',
  '如果爸爸願意，可以請他用自己的帳號問一題冷門的問題，你來找出至少三個需要查證的地方。'],
  ['curriculum']),
 ('兩小時的抓錯偵探課', [
  '兩小時的安排如下：開場十分鐘，認識幻覺和查核重點十五分鐘，接著四十分鐘舉行抓錯賽，再休息十分鐘。',
  '然後用三十分鐘完成自己的查核表和偵探規則，再用十分鐘交換角色，由你帶著爸爸查證一則新的回答。',
  '最後五分鐘錄音總結，替查核表取名字、存檔，以後看到任何回答，都可以拿出來用。'],
  ['curriculum']),
 ('最後一關：教爸爸查證', [
  '最後一關，請不看稿，拿一則新的回答，當場示範一次：標記、查證、判定。',
  '再指出一個限制或安全注意事項，例如有附來源連結的回答，也可能是錯的。',
  '今天的作品是回答查核表，下次我們要去逛文字、圖片和聲音的體驗站；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum', 'openai_search', 'google_ai_overviews']),
]

VISIBLE = [
 ['第十二堂任務', 'AI 會亂講：\n幻覺抓錯賽', '先標記、再查證、後判定，把錯誤抓出來', '第十二堂  ·  依課表製作的課前教學版'],
 ['抓錯的三個步驟', '先標記、再查證、後判定',
  '01 標記', '圈出名稱、數字\n日期和引用', '→',
  '02 查證', '到可靠的來源\n看它說得對不對', '→',
  '03 判定', '正確、錯誤\n或是查不到',
  '今天的作品：AI 回答查核表'],
 ['AI 幻覺：說得很順，卻是錯的', '「幻覺」是大家常用的說法',
  '01', '它是什麼', '讀起來通順又有把握，內容卻是錯的或編的',
  '02', '為什麼會這樣', '它在預測最可能的字，不是在確認真假',
  '03', '有附來源也要查', '來源連結和引用，也可能出錯'],
 ['最需要查的四種東西', '看到這四種，就先圈起來', '回答裡的',
  '名稱', '人名、地名、書名', '數字', '多高、多少、第幾', '日期', '哪一年、哪一天', '引用', '哪本書、哪個網站',
  '第五種：說得太肯定，例如「一定」「剛好」「所有」'],
 ['引用也可能是編的', '書名、網址、案例，都要自己確認',
  '回答裡寫著', '資料來源：某本書、某個網站', '？', '你要確認兩件事', '它真的存在嗎？裡面真的這樣寫嗎？',
  '2023 年，美國有律師交出聊天機器人編的判決',
  '那些判決並不存在；律師和事務所被罰五千美元'],
 ['怎麼查證？', '重要的事，多查一個地方',
  '01 找原始來源', '官方網站、原本的書', '02 找第二個來源', '兩邊說的一樣嗎？', '03 問大人', '查不到就問爸爸、老師',
  '回頭問它「你確定嗎」不算查證'],
 ['判定：正確、錯誤、查不到', '每一個圈起來的地方，都要有結果',
  '標記  →  查證  →  判定',
  '正確', '可靠來源也這樣說', '錯誤', '和可靠來源不一樣', '查不到', '先不要當成真的',
  '對的和錯的可能混在一起，要一句一句看'],
 ['三種特別要小心的時候', '查證不是找麻煩，是保護自己',
  '一、作業和報告：先查證，再使用\n二、健康、金錢、安全：一定問大人\n三、發現錯誤：告訴爸爸，不要轉傳',
  '還要記得', '查證的人也會出錯', '重要的事\n要找第二個來源',
  '暫停影片：說出最需要查的四種東西'],
 ['幻覺抓錯賽：三則模擬回答', '回答是這堂課編寫的，裡面故意藏了錯誤',
  '第一回合：標記', '每一則至少圈出三個地方\n寫下它是哪一種',
  '第二回合：查證和判定', '對照資料卡或官方網站\n寫下正確、錯誤、查不到',
  '找到錯，還要說出它是哪一種'],
 ['換你設計：AI 回答查核表', '做一張以後都用得上的表，再加一條偵探規則',
  '01', '設計查核表的欄位', '哪一句、哪一種、去哪裡查、查到什麼',
  '02', '加一條偵探規則', '例如：只要是數字，就查兩個地方',
  '03', '請爸爸問一題冷門題', '用爸爸的帳號；你來找出三個要查的地方'],
 ['兩小時的抓錯偵探課', '影片先引路，接下來用查核表練習抓錯',
  '00–25', '開場十分＋概念十五分', '25–65', '三則回答抓錯賽', '65–75', '休息十分鐘',
  '75–105', '我的查核表＋偵探規則', '105–115', '孩子教爸爸查證', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：資訊判讀，先標記、再查證、後判定'],
 ['最後一關：教爸爸查證', '暫停影片：不看稿示範一次，再指出一個限制或安全注意',
  '01', '完成 AI 回答查核表', '三則回答都查完，欄位自己設計',
  '02', '當場查一個地方', '標記、查證、判定，說出它是哪一種',
  '03', '指出一個限制或安全注意', '例如：有附來源的回答，也可能是錯的',
  '保持好奇，我們下次見！'],
]

BOARD = [
 ('開場：課前教學版揭露、生成式 AI 會把錯的說得像真的、偵探任務與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備模擬回答與查核表；預告抓錯賽'),
 ('概念：標記、查證、判定三個步驟', '三步流程卡：標記 → 查證 → 判定', '說出今天要完成的作品'),
 ('概念：幻覺是什麼、為什麼會發生、有附來源也要查', '三點條列＋陳犀牛', '用自己的話說什麼是幻覺'),
 ('概念：最需要查的四種（名稱、數字、日期、引用）與第五種（說得太肯定）', '面板四張卡＋黃字說明', '各舉一個例子'),
 ('示範：引用也可能是編的；律師交出不存在的判決被罰款', '雙框（回答裡寫著 ？ 你要確認兩件事）＋白字＋黃字', '說出看到引用要確認哪兩件事'),
 ('示範：找原始來源、找第二個來源、問大人；再問一次不算查證', '三張步驟卡＋黃字提醒', '說出三個查證的方法'),
 ('概念：判定成正確、錯誤、查不到；對錯可能混在一起', '路徑一行＋三張卡＋黃字', '說出查不到的時候怎麼辦'),
 ('安全：作業報告先查證；健康金錢安全問大人；發現錯誤不轉傳', '左側三行；右側「還要記得」', '暫停影片：說出最需要查的四種東西'),
 ('活動規則：三則模擬回答，先標記，再查證和判定', '左右比較卡（標記／查證和判定）＋黃字', '每則至少圈三處並判定'),
 ('獨立改造：自己的查核表、偵探規則、請爸爸問冷門題', '三點條列＋陳犀牛', '完成查核表；加一條偵探規則'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：當場查一個地方，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子教爸爸；錄音回答四個問題；作品命名存檔'),
]

FACT_CHECK = '''# L012 事實查核

查核日：2026-10-08。查核者：製作代理（Claude）與其派出的研究子代理。
方法：子代理下載各來源的原始頁面或 PDF、抽取文字後回報逐字引文（原文見 `source-notes.md`）；主代理再把引文和旁白、投影片、教材逐句比對。
限制：主代理沒有逐頁重讀來源；OpenAI 說明中心只有擷取工具的摘要，沒有逐字確認；法院命令讀的是 CourtListener 的 RECAP 存檔（法院自己的檔案），沒有找到法院網站上的網址；
來源多為英文，中文是本課轉述。

## 主張與來源（影片）

| # | 本課的說法（幕） | 來源依據 | 結論 |
|---|---|---|---|
| 1 | 生成式 AI 有時會把錯的事情說得跟真的一樣，常被叫做幻覺（1、3） | NIST：“generate and confidently present erroneous or false content … colloquially also referred to as ‘hallucinations’”；Google 中文說明：「Gemini 可能會產生幻覺，將不準確的資訊當做事實」 | 相符。「幻覺」是俗稱；教育部注意事項 2.1 沒有用這個詞，教材有註明 |
| 2 | 回答讀起來通順、有把握，內容卻是錯的或編的（3） | IBM：“outputs that sound plausible but are factually wrong, irrelevant or entirely fabricated”；NIST：風險來自 “the confident nature of the response” | 相符 |
| 3 | 原因：它預測接下來最可能出現的字，目標是通順，不是確認真假（3） | NIST：“LLMs predict the next token or word”；MIT Sloan：“Their goal is to generate plausible content, not to verify its truth.” | 相符（簡化） |
| 4 | 就算附了來源連結，也可能出錯（3、12） | OpenAI 說明（摘要）：“Search results and citations can be incomplete, outdated, or incorrect.”；Google：「因此，我們無法確保 AI 摘要內容皆正確無誤。」 | 相符；OpenAI 那一句沒有逐字確認 |
| 5 | 最需要查：名稱、數字、日期、引用（2、4） | 課表學習目標；OpenAI 說明（摘要）：“Incorrect definitions, dates, or facts”、“Fabricated quotes, studies, citations or references to non-existent sources”；IBM：“nonexistent URLs or incorrect details about real entities”；教育部數位素養教案：「統計數據、名言、法條、專有名詞，應至原始文件或官方網站核實」 | 相符；沒有單一來源同時列出這四項，四項的組合來自課表 |
| 6 | 第五種：說得太肯定；真實世界的數字常常只是估計（4） | OpenAI 說明（摘要）：“Overconfident answers to ambiguous or complex questions”；臺灣黑熊的族群數字，玉山國家公園管理處寫「約200~600隻」、林業期刊寫「數百隻」 | 相符；「常常只是估計」是本課的概括，教材用臺灣黑熊當例子 |
| 7 | 連書名、網址和案例都可能是編的（5） | IBM：“invented studies, nonexistent URLs”；NIST：“confabulated logic or citations” | 相符 |
| 8 | 2023 年，美國兩位律師請聊天機器人找判決，它編出六個不存在的案例；律師交給法院後，和事務所一起被罰五千美元（5） | 紐約南區聯邦地方法院 2023-06-22 制裁命令：“submitted non-existent judicial opinions with fake quotes and citations created by the artificial intelligence tool ChatGPT”；六個判決 “were generated by ChatGPT and do not exist”；“A penalty of $5,000 is jointly and severally imposed on Respondents” | 相符。罰款是兩位律師與事務所共同負擔一筆 5,000 美元，不是每人 5,000；法院也寫，使用可靠的 AI 工具協助本身沒有不當。旁白說「聊天機器人」，命令寫的是 ChatGPT |
| 9 | 查證：找原始來源、找第二個可靠來源（6） | 教育部數位素養教案：「追溯原始資料」「交叉比對搜尋」；Google：「務必多方查證重要資訊。」 | 相符 |
| 10 | 查不到或看不懂就問爸爸或老師（6） | 教育部注意事項：「如對內容仍有疑慮，應向老師或家長請教」 | 相符 |
| 11 | 只是回頭再問它一次「你確定嗎」，不算查證（6） | 沒有廠商說再問一次就會更正。法院命令第 45 段：律師問 ChatGPT 那個案例是不是真的，它回答是真的 | 這是本課的建議；依據只有一個 2023 年的案例，不是通則。旁白沒有說「再問一次一定沒用」 |
| 12 | 查不到的，先不要當成真的（2、7） | 教育部注意事項結語：「不要輕易相信未經證實的訊息。」 | 相符 |
| 13 | 一個回答裡，對的和錯的可能混在一起（7） | IBM：“incorrect details about real entities” | 相符（旁白用「可能」） |
| 14 | 作業和報告的內容先查證再使用（8） | 教育部注意事項：「不可以直接將生成內容作為作業或報告的原始答案。」 | 相符 |
| 15 | 健康、金錢、安全的事不要只聽它的，要問大人（8） | 沒有逐字來源；Anthropic 條款：不應在沒有自行確認的情況下依賴輸出 | 本課的建議 |
| 16 | 發現錯誤告訴爸爸，不要直接轉傳（8） | 教育部注意事項結語：「不要輕易相信未經證實的訊息」；本課延伸 | 本課的建議 |

## 教材三則模擬回答裡的參考事實

三則「模擬回答」是本課編寫的，不是任何 AI 工具的輸出；裡面的錯誤是故意放的。用來判定對錯的參考事實如下。

| 主題 | 參考事實 | 來源 |
|---|---|---|
| 犀牛 | 現存五種：白犀牛、黑犀牛、大獨角犀、爪哇犀牛、蘇門答臘犀牛 | International Rhino Foundation（IRF）：“the five surviving rhino species in Africa and Asia” |
| 犀牛 | 角是角蛋白，和指甲、頭髮同樣的材料 | IRF：“Rhino horn is made of compressed keratin fibers, the same material that is found in fingernails and hair.” |
| 犀牛 | 白犀牛、黑犀牛、蘇門答臘犀牛兩支角；大獨角犀、爪哇犀牛一支 | IRF 各物種頁面 |
| 犀牛 | 嗅覺與聽覺靈敏，視力不好 | IRF：“keen sense of smell and hearing, but they have poor vision”；Save the Rhino 同 |
| 犀牛 | 全球約 26,700 隻 | IRF《2026 State of the Rhino》；Save the Rhino 數字相同 |
| 玉山 | 主峰海拔 3,952 公尺，臺灣第一高峰 | 玉山國家公園管理處；行政院國情簡介 |
| 玉山 | 玉山國家公園是我國第 2 座國家公園，成立時間民國 74 年 4 月 | 玉山國家公園管理處；行政院國情簡介（資料來源：內政部） |
| 臺灣黑熊 | 瀕臨絕種野生動物；胸前黃白色 V 字形或新月形斑紋 | 玉山國家公園管理處「臺灣黑熊科普」 |
| 臺灣黑熊 | 族群數量是估計值：「約200~600隻」「數百隻」，各來源不同 | 玉山國家公園管理處；林業及自然保育署期刊 |
| 月球 | 與地球平均距離 384,400 公里 | NASA Science “Moon Facts” |
| 月球 | 阿波羅 11 號，1969 年 7 月 20 日（美國東部時間）降落 | NASA History |
| 月球 | 阿姆斯壯與艾德林踏上月面，柯林斯留在指揮艙繞月 | NASA（2019-07-20 專文） |
| 月球 | 一共 12 個人在月球上走過 | NASA Science “Moon Walkers” |
| 太陽 | 陽光到地球約 8 分 20 秒 | NASA Astrobiology |

模擬回答裡的「《犀牛全知道》（星星出版社，2031 年）」和「www.nasa.example/moon-walkers」是本課編的假引用：出版年份是未來，網址用的是保留給範例的 `.example`。

## 刻意避免的說法

- 沒有說「再問一次『你確定嗎』AI 就會自己更正」，也沒有說「再問一次一定沒用」。
- 沒有說連上網路或有附連結的 AI 不會出錯。
- 沒有說教育部注意事項用了「幻覺」這個詞。
- 沒有說每位律師各罰五千美元，也沒有說法院禁止使用 AI。
- 沒有引用任何幻覺發生的百分比。
- 參考事實避開了各來源不一致的數字：白犀牛體重、犀牛最高時速、爪哇犀牛的舊數字、臺灣黑熊的單一數字、登月的分鐘數。
- 沒有說白犀牛是最大的犀牛；沒有說玉山是「東北亞第一高峰」；臺灣黑熊胸前斑紋照官方寫「黃白色」。

## 課程與素材

- 課程主題、學習目標、120 分鐘流程（10／15／40／10／30／10／5）、動手任務（請 AI 回答冷門題，孩子找出至少 3 個需驗證點）、
  作品（AI 回答查核表）與驗收，依 `curriculum/catalog.json` L012 核對。
- 沒有課堂錄音；本集是**依課表製作的課前教學版**，未虛構逐字稿或父子對話，封面、旁白第一句與說明均已揭露。
- 課表的任務是「請 AI 回答冷門題」。各家工具有年齡限制，所以本課提供三則編寫好的模擬回答讓孩子練習；真的要問 AI，由爸爸用自己的帳號操作（影片第 10 頁）。
- 課表的好玩機制是偵探辦案：標記、查證、判定。
- 片名是「AI 會亂講：幻覺抓錯賽」；旁白第一句念的是「幻覺抓錯賽」，作品「AI 回答查核表」念作「回答查核表」，避免英文縮寫夾在中文裡念得太短。
- 課表主要參考網址（R20）是 OpenAI Academy 首頁；本課沒有引用其中任何一頁。
- 課表的三組 YouTube 連結是動態搜尋入口；本次沒有挑選、觀看或引用任何影片。
'''

PLAN = '''# L012 AI 會亂講：幻覺抓錯賽

依課表製作的課前教學版；沒有課堂錄音，不製造逐字稿。
沿用原片頭 v2、陳犀牛、深藍／黃／青、12 頁原生可編輯簡報、36 句旁白、zh-TW-YunJheNeural；
教學段落靜態畫面加 0.55 秒淡化，無背景音樂、無推拉鏡頭。

## 課表核對（curriculum/catalog.json L012）

- 模組：M01 數位探險家；難度 2；主軸：數位素養／AI 素養／網路安全。
- 學習目標：養成查核名稱、數字、日期、引用與不確定性的習慣。
- 動手任務：請 AI 回答冷門題，孩子找出至少 3 個需驗證點。好玩機制：偵探辦案。
- 作品：AI 回答查核表。生活技能支線：資訊判讀。
- 驗收：完成作品；不看稿說出核心原理；指出至少一個錯誤、限制或安全注意事項。

## 120 分鐘（課堂，與影片片長分開）

| 分鐘 | 內容 | 對應影片頁 |
|---|---|---|
| 00–10 | 任務開場：爸爸念模擬回答一，問孩子「你覺得哪裡怪怪的？」 | 1–2 |
| 10–25 | 概念示範：幻覺是什麼、最需要查的四種、引用也可能是編的、怎麼查證、怎麼判定 | 3–8 |
| 25–65 | 共同實作：三則模擬回答抓錯賽（標記、查證、判定） | 9 |
| 65–75 | 休息 | — |
| 75–105 | 孩子獨立改造：自己的 AI 回答查核表、一條偵探規則；爸爸用自己的帳號問一題冷門題（可不做） | 10 |
| 105–115 | 角色互換：孩子帶爸爸查證一則新的回答 | 12 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 11–12 |

## 12 頁

1 開場與揭露｜2 標記、查證、判定｜3 幻覺是什麼｜4 最需要查的四種｜5 引用也可能是編的｜6 怎麼查證｜7 怎麼判定｜
8 三種特別要小心的時候｜9 抓錯賽規則｜10 我的查核表｜11 兩小時安排｜12 驗收與結尾。

## 設計取捨

- 三則「模擬回答」是本課編寫的，逐則標示不是真的 AI 輸出；裡面的錯誤是故意放的，判定用的參考事實都有官方來源（IRF、玉山國家公園管理處、行政院、NASA）。
- 課表要孩子找「需驗證點」，不是只找錯。所以圈出來的地方有對有錯，孩子要查過才知道。
- 「不確定性」用臺灣黑熊的族群數字來教：官方來源給的是範圍，而且彼此不同；模擬回答卻寫「剛好 1,000 隻，非常確定」。
- 假引用做得查得出來：書的出版年份是未來的 2031 年，網址用保留給範例的 `.example`。
- 真實案例只用有法院文件的一件（Mata v. Avianca），並照命令的寫法說是一筆共同負擔的罰款。
- 孩子不需要 AI 帳號；真的要問冷門題，由爸爸用自己的帳號操作。

## 作品與驗收

- AI 回答查核表（欄位由孩子設計）。
- 三則模擬回答的抓錯紀錄。
- 一條自選偵探規則。
- 孩子教爸爸：不看稿當場標記、查證、判定一個地方，並指出一個限制或安全注意事項。
- 錄音四問（錄音只留私人區）。

## 教材

`classroom/L012_AI會亂講_幻覺抓錯賽/`：爸爸先讀、抓錯賽規則、5 頁列印包（查核小抄卡、三則模擬回答、查證資料卡、
抓錯紀錄表、AI 回答查核表與偵探規則卡）、抓錯紀錄（CSV＋說明）、模擬回答解說、自選偵探規則、驗收與回顧、查核小抄。
由 `authoring/l012/classroom.py` 產生；內容與來源查核見 fact-check.md。
'''

SUMMARY = '''這是依課表製作的課前教學版，不是實際上課錄音，也沒有虛構的課堂對話。

生成式 AI 有時候會把錯的事情說得跟真的一樣，大家常把這種情形叫做幻覺。陳犀牛帶你當偵探：先標記、再查證、後判定。
看完影片，用三則特地編寫、故意藏了錯誤的模擬回答舉辦抓錯賽，最後完成一張以後都用得上的 AI 回答查核表。

這一集會學到
・幻覺是什麼：說得通順又有把握，內容卻是錯的或編的
・最需要查的四種東西：名稱、數字、日期、引用；還有第五種，說得太肯定的話
・引用也可能是編的：要確認它真的存在、裡面真的這樣寫
・怎麼查證：找原始來源、找第二個可靠來源、查不到就問大人

教材用法（classroom.zip）
先讀「00_爸爸先讀」，列印「02_列印包」（A4 共 5 頁），照「01_活動規則」舉辦抓錯賽，用「03_抓錯紀錄」記錄；
答案與依據在「04_模擬回答解說」，下半場完成 AI 回答查核表和「05_自選偵探規則」，最後用「06_驗收與回顧」讓孩子教爸爸。「07_查核小抄」可以貼在電腦旁邊。

注意事項
・課堂是 120 分鐘，影片只是課前引導，片長另計。
・教材的三則模擬回答是這堂課編寫的，不是真的 AI 輸出；裡面的錯誤是故意放的，請不要把它當成資料引用。
・有附來源連結的回答也可能出錯；只是再問它一次「你確定嗎」不算查證。
・各家 AI 工具都有年齡限制。想問真的 AI 一題冷門題，請由爸爸用自己的帳號操作，並且不輸入個資。

來源（查核日 2026-10-08）
教育部「中小學使用『生成式人工智慧』注意事項 2.1」（115 年 2 月核定）
NIST AI 600-1「Generative Artificial Intelligence Profile」：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
IBM「What Are AI Hallucinations?」：https://www.ibm.com/think/topics/ai-hallucinations
Google 搜尋說明（AI 摘要）：https://support.google.com/websearch/answer/14901683?hl=zh-Hant
Mata v. Avianca 制裁命令（2023-06-22）：https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_3.pdf
International Rhino Foundation「State of the Rhino」：https://rhinos.org/about-rhinos/state-of-the-rhino/
玉山國家公園管理處：https://www.ysnp.gov.tw/
NASA Science「Moon Facts」：https://science.nasa.gov/moon/facts/
'''

if __name__ == '__main__':
    lesson_builder.build(
        lesson=LESSON, slug=SLUG, ordinal='十二', title=TITLE, header_en='HALLUCINATION HUNT', checked=CHECKED,
        src=SRC, scenes=SCENES, visible=VISIBLE, board=BOARD,
        render_options={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        tts_basis="On 2026-10-08 the user asked to start producing L011–L013 after receiving L007–L010, whose hand-over stated that "
                  "the public narration is sent to Edge TTS on the same basis; restated to the user before synthesis.",
        source_records=SOURCE_RECORDS,
        source_method='A research subagent downloaded each page/PDF on the check date and reported verbatim quotes '
                      '(production/source-notes.md); the producing agent mapped them to claims. Not a human full read.',
        not_verified=['OpenAI 說明中心兩頁只有擷取工具的摘要，沒有逐字確認',
                      '法院制裁命令讀的是 CourtListener 的 RECAP 存檔，沒有找到法院網站上的網址',
                      'Google Bard 與加拿大航空兩個案例沒有取得足夠的第一手來源，沒有使用',
                      '林業及自然保育署《臺灣黑熊保育行動計畫》只有擷取工具的摘要，沒有使用其中的數字',
                      '世界自然基金會（WWF）的犀牛頁面只有擷取工具的摘要，且數字與 IRF 不同，沒有使用',
                      '沒有用任何真實 AI 工具產生回答；三則模擬回答是本課編寫的'],
        documents={'fact-check.md': FACT_CHECK, 'plan.md': PLAN, 'delivery-summary.md': SUMMARY,
                   'source-notes.md': (Path(__file__).resolve().parent / 'source-notes.md').read_text(encoding='utf-8')},
        readme=lesson_builder.readme(LESSON, TITLE))
