"""Author L013 production sources (curriculum-based pre-class edition; no recording implied).

Rerunnable. Holds only this lesson's text; authoring/lesson_builder.py writes the files.
After any change here, rebuild downstream stages.

    ./portable-runtime.sh python authoring/l013/prepare_content.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lesson_builder  # noqa: E402

LESSON, SLUG, TITLE = 'L013', 'l013-multimodal-stations', '文字、圖片、聲音 AI 體驗站'
CHECKED = '2026-10-08'

SRC = {
    'curriculum': 'curriculum/catalog.json：L013；來源 V2 Excel 逐堂課程第 13 堂',
    'unicef3': 'https://www.unicef.org/innocenti/media/11991/file/UNICEF-Innocenti-Guidance-on-AI-and-Children-3-2025.pdf',
    'ms_learn_genai': 'https://learn.microsoft.com/en-us/training/modules/intro-generative-ai-explore-basics/2-what-is-generative-ai',
    'ms_ai101': 'https://www.microsoft.com/en-us/ai/ai-101/how-does-generative-ai-work',
    'openai_image_limits': 'https://developers.openai.com/api/docs/guides/image-generation',
    'google_image_blog': 'https://blog.google/products-and-platforms/products/gemini/gemini-image-generation-issue/',
    'openai_dalle_card': 'https://cdn.openai.com/papers/DALL_E_3_System_Card.pdf',
    'ms_tts': 'https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech',
    'ms_voices': 'https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts',
    'ms_personal_voice': 'https://learn.microsoft.com/en-us/azure/ai-services/speech-service/personal-voice-overview',
    'elevenlabs_policy': 'https://elevenlabs.io/use-policy',
    'google_policy': 'https://policies.google.com/terms/generative-ai/use-policy',
    'ftc_voice': 'https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes',
    'fbi_psa': 'https://www.ic3.gov/PSA/2024/PSA241203',
    'npa_hualien': 'https://www.hlhpd.npa.gov.tw/ch/app/openData/data/list?module=publicizearea&mserno=105480c9-65f8-41bd-ae8d-17f9507da67f&type=xml',
    'moi_165': 'https://www.moi.gov.tw/News_Content.aspx?n=2&s=323333',
    'moe_genai': 'https://jr.hs.ntnu.edu.tw/wp-content/uploads/2026/02/中小學使用「生成式人工智慧」注意事項2.1.pdf',
    'tw_ai_act': 'https://www.president.gov.tw/File/Doc/80165b6d-cb49-4b49-952f-56e1e6abe51b',
    'tipo_ai': 'https://www.tipo.gov.tw/tw/copyright/692-34252.html',
    'tipo_reuse': 'https://www.tipo.gov.tw/tw/copyright/692-87797.html',
    'youtube_disclosure': 'https://support.google.com/youtube/answer/14328491?hl=en',
    'synthid': 'https://deepmind.google/models/synthid/',
    'apple_speak': 'https://support.apple.com/zh-tw/guide/mac-help/mh27448/mac',
    'apple_personal_voice': 'https://support.apple.com/zh-tw/guide/mac-help/mchldfd72333/mac',
    'apple_image_playground': 'https://support.apple.com/zh-tw/guide/mac-help/mchld5412d00/mac',
    'apple_availability': 'https://www.apple.com/tw/macos/feature-availability/',
    'gemini_images': 'https://support.google.com/gemini/answer/14286560?hl=en',
    'catalog_reference': 'https://academy.openai.com/',
}

SOURCE_RECORDS = [
    {'id': 'unicef3', 'title': 'Guidance on AI and Children 3.0（2025-12）', 'publisher': 'UNICEF Innocenti', 'url': SRC['unicef3'], 'usedFor': '生成式 AI 用統計規律預測語言、圖像與其他媒體的下一步來產生新內容；AI 生成內容可能與人做的難以分辨；模仿親人聲音要錢的合成語音詐騙'},
    {'id': 'ms_learn_genai', 'title': 'What is generative AI?（2025-03-24）', 'publisher': 'Microsoft Learn', 'url': SRC['ms_learn_genai'], 'usedFor': '生成式 AI 從資料中的規律產生文字、語音與圖像'},
    {'id': 'ms_ai101', 'title': 'How Does Generative AI Work', 'publisher': 'Microsoft', 'url': SRC['ms_ai101'], 'usedFor': '從文字提示產生圖像；產生擬真的旁白與語音合成'},
    {'id': 'openai_image_limits', 'title': 'Image generation guide：Limitations', 'publisher': 'OpenAI API docs', 'url': SRC['openai_image_limits'], 'usedFor': '圖片裡的文字位置與清晰度仍可能出問題；同一角色跨多次生成不一定一致；構圖不一定照指定'},
    {'id': 'google_image_blog', 'title': "Gemini image generation got it wrong. We'll do better.（2024-02-23）", 'publisher': 'Google', 'url': SRC['google_image_blog'], 'usedFor': '生成的圖像有些不正確，甚至冒犯人；它會出錯'},
    {'id': 'openai_dalle_card', 'title': 'DALL·E 3 System Card（2023-10-03）', 'publisher': 'OpenAI', 'url': SRC['openai_dalle_card'], 'usedFor': '教材：圖像生成可能強化刻板印象，人物呈現有偏向'},
    {'id': 'ms_tts', 'title': 'What is text to speech?（2026-01-30）', 'publisher': 'Microsoft Learn（Azure AI Speech）', 'url': SRC['ms_tts'], 'usedFor': '文字轉語音把文字變成像人聲的合成語音，又叫語音合成；用深度神經網路讓電腦聲音接近真人錄音'},
    {'id': 'ms_voices', 'title': 'Language and voice support for the Speech service（2026-09-09）', 'publisher': 'Microsoft Learn（Azure AI Speech）', 'url': SRC['ms_voices'], 'usedFor': 'zh-TW-YunJheNeural 列在臺灣華語的標準（Standard）神經語音；標準語音是現成可用的聲音，不是某位使用者的複製聲音'},
    {'id': 'ms_personal_voice', 'title': 'What is personal voice for text to speech?（2026-09-09）', 'publisher': 'Microsoft Learn（Azure AI Speech）', 'url': SRC['ms_personal_voice'], 'usedFor': '有技術能在幾秒內做出使用者自己聲音的 AI 複製；每個聲音都必須有本人明確同意並錄下聲明'},
    {'id': 'elevenlabs_policy', 'title': 'Prohibited Use Policy（2026-08-17 更新）', 'publisher': 'ElevenLabs', 'url': SRC['elevenlabs_policy'], 'usedFor': '未經同意不得刻意複製他人的聲音；不得讓人誤以為聲音不是 AI 產生的；13 歲以下不得使用'},
    {'id': 'google_policy', 'title': 'Generative AI Prohibited Use Policy（2024-12-17）', 'publisher': 'Google', 'url': SRC['google_policy'], 'usedFor': '禁止在沒有明確揭露的情況下冒充他人以欺騙'},
    {'id': 'ftc_voice', 'title': 'Scammers use AI to enhance their family emergency schemes（2023-03-20）', 'publisher': 'U.S. Federal Trade Commission', 'url': SRC['ftc_voice'], 'usedFor': '詐騙者可以用一小段聲音複製親人的聲音；不要相信那個聲音，用你知道的號碼打給本人確認'},
    {'id': 'fbi_psa', 'title': 'Public Service Announcement I-120324-PSA（2024-12-03）', 'publisher': 'FBI Internet Crime Complaint Center', 'url': SRC['fbi_psa'], 'usedFor': '和家人約定一個祕密的字或句子來確認身分；掛斷電話後自己查號碼再回撥'},
    {'id': 'npa_hualien', 'title': '反詐騙宣導（轉載刑事警察局宣導；114-07-02、114-12-10）', 'publisher': '內政部警政署花蓮港務警察總隊 開放資料', 'url': SRC['npa_hualien'], 'usedFor': '「詐騙集團利用人工智慧AI技術，模擬親友的聲音，製造緊急情境，誘使受害者匯款」；設定家庭密語；聲音、影像都能被偽造，先用另一個確定的聯絡方式確認，可撥打 165'},
    {'id': 'moi_165', 'title': '通話中直接撥打165？小心詐騙集團假冒警察', 'publisher': '內政部', 'url': SRC['moi_165'], 'usedFor': '「一聽、二掛、三查證」；先掛斷電話，後查證（一般防詐原則，不是專講 AI）'},
    {'id': 'moe_genai', 'title': '中小學使用「生成式人工智慧」注意事項 2.1（學生版；115 年 2 月 11 日核定）', 'publisher': '教育部（師大附中國中部網站轉載的 PDF）', 'url': SRC['moe_genai'], 'usedFor': '深偽技術能用既有的圖片、影像或聲音製造看似真實的影片和圖像；不可輸入自己或他人的姓名、照片等個資；依規定註明所使用的工具及用途；遵守各平臺年齡限制，非在校使用請家長陪伴'},
    {'id': 'tw_ai_act', 'title': '人工智慧基本法 第四條（總統府公報第 7837 號，115 年 1 月 14 日）', 'publisher': '總統府', 'url': SRC['tw_ai_act'], 'usedFor': '教材：透明與可解釋原則，人工智慧之產出應做適當資訊揭露或標記（政府推動 AI 的原則，不是對個人的標示義務）'},
    {'id': 'tipo_ai', 'title': '電子郵件 1140522c 函釋（114-05-22）', 'publisher': '經濟部智慧財產局', 'url': SRC['tipo_ai'], 'usedFor': 'AI 生成的圖畫是否享有著作權，視有無人類實際的創意投入；與原始著作實質近似可能有侵權問題；個案由法院認定'},
    {'id': 'tipo_reuse', 'title': '電子郵件 1150624 函釋（115-06-24）', 'publisher': '經濟部智慧財產局', 'url': SRC['tipo_reuse'], 'usedFor': '教材：復刻、微調或致敬他人著作可能構成重製、改作，原則上應取得授權（該函釋談的不是 AI）'},
    {'id': 'youtube_disclosure', 'title': 'Disclosing use of GenAI content', 'publisher': 'YouTube Help', 'url': SRC['youtube_disclosure'], 'usedFor': '教材（給爸爸）：創作者須揭露以 AI 大幅變造或生成的擬真內容；非寫實內容、腳本與字幕等製作協助不需揭露'},
    {'id': 'synthid', 'title': 'Google SynthID', 'publisher': 'Google DeepMind', 'url': SRC['synthid'], 'usedFor': '教材：在 AI 生成的圖像、聲音、文字或影片裡嵌入人察覺不到、但可被偵測的數位浮水印'},
    {'id': 'apple_speak', 'title': '讓 Mac 朗讀螢幕上的文字', 'publisher': 'Apple 支援（台灣）', 'url': SRC['apple_speak'], 'usedFor': '教材：「系統設定」>「輔助使用」>「閱讀與朗讀」（macOS 15 是「語音內容」）>「朗讀所選範圍」，預設按鍵 Option + Esc；「編輯」>「語音」>「開始朗讀」'},
    {'id': 'apple_personal_voice', 'title': '在 Mac 上製作「個人聲音」', 'publisher': 'Apple 支援（台灣）', 'url': SRC['apple_personal_voice'], 'usedFor': '教材：「個人聲音」只能用本人的聲音、只適用英文（美國）、國語（中國大陸）、西班牙文（墨西哥），本課不使用'},
    {'id': 'apple_image_playground', 'title': '在 Mac 上使用「影像樂園」製作獨創影像', 'publisher': 'Apple 支援（台灣）', 'url': SRC['apple_image_playground'], 'usedFor': '教材：可在「螢幕使用時間」阻擋影像製作功能；「寫實影像」建議使用年齡 18 歲以上'},
    {'id': 'apple_availability', 'title': 'macOS 功能特色適用範圍', 'publisher': 'Apple（台灣）', 'url': SRC['apple_availability'], 'usedFor': '教材：影像樂園支援繁體中文，需要 M1 或更新晶片的 Mac，部分功能未在所有地區提供'},
    {'id': 'gemini_images', 'title': 'Generate & edit images with Gemini Apps', 'publisher': 'Google Gemini Apps Help', 'url': SRC['gemini_images'], 'usedFor': '教材：產生圖片須年滿 13 歲（或所在國家適用年齡），編輯圖片須年滿 18 歲'},
    {'id': 'catalog_reference', 'title': 'OpenAI Academy', 'publisher': 'OpenAI（課表 R20 的主要參考網址）', 'url': SRC['catalog_reference'], 'usedFor': '課表列出的參考入口；本課沒有引用其中任何一頁'},
]

SCENES = [
 ('文字、圖片、聲音 AI 體驗站', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是第十三堂，我們要逛三個體驗站：文字、圖片和聲音，這是依課表製作的課前教學版，並非實際上課錄音。',
  '生成式 AI，不只會寫字，還能照著你的描述，做出圖片和聲音。',
  '今天你要替一個自己發明的角色，完成一張多模態角色卡。'],
  ['curriculum', 'ms_learn_genai']),
 ('每一站做三件事', [
  '每一站都做三件事。第一，看輸入：你給它的是什麼。',
  '第二，看輸出：它交出來的是什麼。',
  '第三，做檢查：哪裡和你說的不一樣，還有什麼事不可以做。'],
  ['curriculum']),
 ('多模態：不只一種形式', [
  '多模態的意思，是不只一種形式。文字站，輸入一段話，輸出也是一段話。',
  '圖片站，輸入一段描述，輸出是一張圖；聲音站，輸入一段文字稿，輸出是一段念出來的語音。',
  '三站的做法很像，都是從大量的資料裡學到規律，再做出新的內容，所以也都可能出錯。'],
  ['ms_learn_genai', 'ms_ai101', 'unicef3']),
 ('用四個格子比較三站', [
  '每一站都用四個格子來比較。輸入，是你給它的東西；輸出，是它交出來的東西。',
  '限制，是它做不好的地方，例如圖片裡的字可能寫錯，細節可能和你說的不一樣。',
  '風險，是可能傷害到人的地方，例如有人拿它來模仿別人的臉和聲音。'],
  ['curriculum', 'openai_image_limits', 'google_image_blog', 'moe_genai']),
 ('圖片站：描述變成一張圖', [
  '來看圖片站。你描述一隻戴紅帽子的小犀牛，手上拿著三顆氣球，它就照著畫出一張圖。',
  '可是圖片可能和你說的不一樣：帽子的顏色、氣球的數目，還有畫面裡的字，都要一樣一樣檢查。',
  '還有兩件事不能做：不要上傳自己或別人的照片，也不要叫它畫別人創作的角色，請畫你自己發明的。'],
  ['ms_ai101', 'openai_image_limits', 'moe_genai', 'tipo_ai']),
 ('聲音站：文字變成語音', [
  '再來看聲音站。文字轉語音，是電腦照著文字稿念出聲音；像我陳犀牛的聲音，就是這樣合成出來的，不是真人錄的。',
  '還有一種技術，可以模仿某一個人的聲音，聽起來很像本人。',
  '所以聲音站的規定是：只能用電腦內建的聲音，或是你自己的聲音；沒有經過同意，不可以模仿別人。'],
  ['ms_tts', 'ms_voices', 'ms_personal_voice', 'elevenlabs_policy']),
 ('聽到、看到，不一定是真的', [
  '因為聲音和影像都能合成，所以聽到的、看到的，不一定是真的。',
  '警察提醒過，有詐騙集團利用 AI，模仿親友的聲音，假裝有急事，要你匯錢。',
  '遇到這種電話，先掛斷，再打你原本就知道的號碼確認；全家人也可以先約定一個家庭密語。'],
  ['moe_genai', 'npa_hualien', 'ftc_voice', 'fbi_psa', 'moi_165']),
 ('三個約定', [
  '用這些工具，有三個約定。第一，不上傳：自己和別人的照片、聲音，都不放進去。',
  '第二，要同意：不可以拿別人的臉和聲音來做東西，就算只是好玩也不行。',
  '第三，要標示：哪些是你自己做的，哪些是 AI，都要說清楚；作業也要照老師的規定，註明使用的工具。'],
  ['moe_genai', 'google_policy', 'elevenlabs_policy', 'tw_ai_act']),
 ('三站尋寶', [
  '現在開始尋寶。先發明一個角色，再和爸爸一起逛三站：文字站寫三句介紹，圖片站做一張概念圖，聲音站做一段大約二十秒的旁白。',
  '每一站都藏著三個寶藏：輸入、輸出，還有一個限制，找到就在尋寶地圖上蓋章；再把描述和結果放在一起，找出三個不同的地方。',
  '這三站都不需要你自己的帳號：文字可以請爸爸當機器人，圖片可以自己畫，聲音可以用電腦內建的朗讀功能。'],
  ['curriculum', 'apple_speak']),
 ('換你設計：多模態角色卡', [
  '下半場換你自己來，把三站做出來的東西，組成一張多模態角色卡：文字介紹、概念圖，還有二十秒旁白。',
  '在卡片上標示，每一樣東西是誰做的：是你、是爸爸，還是電腦；和描述不一樣的地方，也要圈出來。',
  '再加一個你自選的規則或功能，例如旁白自己錄一次，再讓電腦念一次，比一比哪裡不同。'],
  ['curriculum', 'moe_genai']),
 ('兩小時的體驗站', [
  '這兩個小時的安排是：開場十分鐘，認識三個體驗站十五分鐘，接著四十分鐘，和爸爸逛三站尋寶，然後休息十分鐘。',
  '下半場三十分鐘，自己完成角色卡，再加一個自選的規則或功能；接著十分鐘交換角色，由你帶爸爸逛一次三個體驗站。',
  '最後五分鐘錄音總結，替角色卡取名字、存檔，並且檢查卡片上沒有真人的照片和個資。'],
  ['curriculum']),
 ('最後一關：帶爸爸逛體驗站', [
  '最後一關，請不看稿，挑兩個體驗站，說出它們的輸入、輸出，還有各一個限制。',
  '再指出一個限制或安全注意事項，例如聲音可以被模仿，聽起來像家人，也要先查證。',
  '今天的作品是多模態角色卡，下次我們要一起訂出我們家的科技公約；我是陳犀牛，保持好奇，我們下次見！'],
  ['curriculum', 'npa_hualien']),
]

VISIBLE = [
 ['第十三堂任務', '文字、圖片、聲音\nAI 體驗站', '比較三站的輸入、輸出、限制和風險', '第十三堂  ·  依課表製作的課前教學版'],
 ['每一站做三件事', '先看輸入、再看輸出、最後檢查',
  '01 輸入', '你給它的\n是什麼', '→',
  '02 輸出', '它交出來的\n是什麼', '→',
  '03 檢查', '哪裡不一樣\n什麼不可以做',
  '今天的作品：多模態角色卡'],
 ['多模態：不只一種形式', '三站的做法很像：學到規律，再做出新的內容',
  '01', '文字站', '輸入一段話，輸出一段話',
  '02', '圖片站', '輸入一段描述，輸出一張圖',
  '03', '聲音站', '輸入一段文字稿，輸出一段語音'],
 ['用四個格子比較三站', '每一站都問同樣的四個問題', '四個格子',
  '輸入', '你給它什麼', '輸出', '它交出什麼', '限制', '它做不好什麼', '風險', '可能傷害到誰',
  '限制是它的問題；風險是用的人可能造成的問題'],
 ['圖片站：描述變成一張圖', '圖片可能和描述不一樣，要一樣一樣檢查',
  '你的描述', '戴紅帽子的小犀牛，拿著三顆氣球', '→', '要檢查的地方', '帽子顏色、氣球數目、畫面裡的字',
  '不上傳自己或別人的照片',
  '不畫別人創作的角色，畫你自己發明的'],
 ['聲音站：文字變成語音', '電腦可以照稿子念，也有技術能模仿人的聲音',
  '01 文字轉語音', '電腦照著文字稿念', '02 模仿聲音', '聽起來很像某個人', '03 要先同意', '只用內建的或自己的聲音',
  '陳犀牛的聲音是文字轉語音合成的，不是真人錄的'],
 ['聽到、看到，不一定是真的', '聲音和影像都能合成',
  '聲音很像  →  先掛斷  →  打原本知道的號碼',
  '聲音可以模仿', '像親人也可能是假的', '影像可以合成', '看到也不一定是真的', '家庭密語', '全家先約定一個暗號',
  '很急、要錢的電話：先掛斷，再查證'],
 ['三個約定', '用得安心，也不傷害別人',
  '一、不上傳：自己和別人的照片、聲音\n二、要同意：不模仿別人的臉和聲音\n三、要標示：哪些是 AI 做的要說清楚',
  '為什麼要標示？', '讓看的人知道它是怎麼來的', '作業照老師的規定\n註明工具和用途',
  '暫停影片：說出這三個約定'],
 ['三站尋寶', '每一站替角色做一樣東西，找三個寶藏',
  '第一回合：逛三站', '介紹、概念圖、二十秒旁白\n找到輸入、輸出、限制就蓋章',
  '第二回合：找不一樣', '描述和結果放在一起\n找出三個不同的地方',
  '不用自己的帳號：爸爸當機器人、自己畫、電腦朗讀'],
 ['換你設計：多模態角色卡', '一個自己發明的角色，三種形式',
  '01', '組成角色卡', '文字介紹、概念圖、二十秒旁白',
  '02', '標示誰做的', '你、爸爸，還是電腦；圈出不一樣的地方',
  '03', '加一個自選規則或功能', '例如：旁白自己錄一次，電腦念一次，比比看'],
 ['兩小時的體驗站', '影片先引路，接下來逛三站、做角色卡',
  '00–25', '開場十分＋概念十五分', '25–65', '三站尋寶：做三樣東西', '65–75', '休息十分鐘',
  '75–105', '角色卡＋自選規則', '105–115', '孩子帶爸爸逛三站', '115–120', '錄音總結＋作品存檔',
  '今日生活技能：數位公民，不上傳、要同意、要標示'],
 ['最後一關：帶爸爸逛體驗站', '暫停影片：不看稿示範一次，再指出一個限制或安全注意',
  '01', '完成多模態角色卡', '文字、概念圖、二十秒旁白，都有標示',
  '02', '當場比較兩個體驗站', '說出輸入、輸出和各一個限制',
  '03', '指出一個限制或安全注意', '例如：聲音可以被模仿，要先查證',
  '保持好奇，我們下次見！'],
]

BOARD = [
 ('開場：課前教學版揭露、生成式 AI 能做文字圖片聲音、今天的三站與作品', '封面版型：任務標籤、兩行主題、一句任務說明；原陳犀牛角色', '準備尋寶地圖與角色卡；預告三個體驗站'),
 ('概念：每站看輸入、看輸出、做檢查', '三步流程卡：輸入 → 輸出 → 檢查', '說出今天要完成的作品'),
 ('概念：多模態；三站的輸入與輸出', '三點條列＋陳犀牛', '各說一個例子'),
 ('概念：用輸入、輸出、限制、風險四格比較', '面板四張卡＋黃字說明', '說出限制和風險差在哪裡'),
 ('示範：圖片站，描述與要檢查的地方；不上傳照片、不畫別人的角色', '雙框（你的描述 → 要檢查的地方）＋白字＋黃字', '說出圖片站要檢查哪三樣'),
 ('示範：聲音站，文字轉語音與模仿聲音；陳犀牛的聲音是合成的', '三張步驟卡＋黃字說明', '說出聲音站的規定'),
 ('安全：聲音和影像能合成；詐騙模仿親友聲音；先掛斷再確認、家庭密語', '路徑一行＋三張卡＋黃字', '和爸爸約定遇到這種電話怎麼做'),
 ('數位公民：不上傳、要同意、要標示', '左側三行；右側「為什麼要標示？」', '暫停影片：說出這三個約定'),
 ('共同實作：逛三站，替角色做文字介紹、概念圖、二十秒旁白；每站找三個寶藏，再找三個不一樣的地方', '左右比較卡（逛三站／找不一樣）＋黃字', '完成尋寶地圖和三樣東西'),
 ('獨立改造：組成多模態角色卡、標示誰做的、加一個自選規則或功能', '三點條列＋陳犀牛', '完成角色卡'),
 ('120 分鐘安排：10／15／40／10／30／10／5', '六列時間表與今日生活技能', '依時間表進行；休息十分鐘'),
 ('作品驗收與回顧：當場比較兩站，指出一個限制或安全注意；固定結尾', '三點驗收條列＋陳犀牛＋結尾語', '孩子帶爸爸逛三站；錄音回答四個問題；作品命名存檔'),
]

FACT_CHECK = '''# L013 事實查核

查核日：2026-10-08。查核者：製作代理（Claude）與其派出的研究子代理。
方法：子代理下載各來源的原始頁面或 PDF、抽取文字後回報逐字引文（原文見 `source-notes.md`）；主代理再把引文和旁白、投影片、教材逐句比對。
限制：主代理沒有逐頁重讀來源；OpenAI 的條款與使用政策、Adobe 與 Canva 的條款只有擷取工具的摘要，沒有逐字確認，本課沒有依賴它們；
刑事警察局與 165 全民防騙網的網頁讀不到，台灣警方的說法取自花蓮港務警察總隊轉載的宣導資料與內政部新聞；來源多為英文，中文是本課轉述。

## 主張與來源

| # | 本課的說法（幕） | 來源依據 | 結論 |
|---|---|---|---|
| 1 | 生成式 AI 不只會寫字，還能照描述做出圖片和聲音（1、3） | Microsoft Learn：“generate original text, voice, and images based on these patterns”；Microsoft AI 101：從文字提示產生圖像、產生旁白與語音合成 | 相符 |
| 2 | 三站都是從大量資料學到規律，再做出新內容，所以都可能出錯（3） | UNICEF：“generate new content by using statistical patterns to predict what comes next in language, images and other media”；Google：“It will make mistakes.” | 相符（簡化） |
| 3 | 圖片裡的字可能寫錯，細節可能和你說的不一樣（4、5） | OpenAI 圖像生成指南：“the model can still struggle with precise text placement and clarity”、構圖不一定照指定；Google：“Some of the images generated are inaccurate” | 相符。旁白用「可能」；各家都說文字呈現已有改善，沒有說一定寫錯。「氣球的數目」是本課舉的檢查項目，不是引用 |
| 4 | 風險：有人拿它來模仿別人的臉和聲音（4、7） | 教育部注意事項第三點：深偽技術「能利用既有的圖片、影像或聲音素材，製造出看似真實的影片和圖像」；示例：「整合他們的臉（聲音）到假圖片或假影片中」 | 相符 |
| 5 | 不要上傳自己或別人的照片（5、8） | 教育部注意事項六（三）：「不可以將自己或他人的姓名、照片…輸入至『生成式人工智慧』工具。」 | 相符；「聲音」不在原文列舉內，是本課依同一道理延伸 |
| 6 | 不要叫它畫別人創作的角色，畫自己發明的（5） | 智慧財產局 114-05-22 函釋：AI 生成圖畫與原始著作「構成實質近似」可能有侵權問題；115-06-24 函釋：復刻、致敬他人著作原則上應取得授權（後者談的不是 AI） | 這是本課依函釋給的保守建議；是否侵權由法院個案認定，影片沒有說「一定違法」 |
| 7 | 文字轉語音：電腦照著文字稿念出聲音（6） | Microsoft Learn：“convert text into human like synthesized speech … also known as speech synthesis” | 相符 |
| 8 | 陳犀牛的聲音是這樣合成出來的，不是真人錄的（6） | 本系列的製作流程：旁白由 Edge TTS 以 zh-TW-YunJheNeural 合成（各集 `production/tts-manifest.json`）；Microsoft 把這個聲音列為臺灣華語的標準神經語音 | 相符。Microsoft 的文件記載的是 Azure 語音服務；Edge TTS 提供同名聲音這一點，文件沒有寫 |
| 9 | 有技術可以模仿某個人的聲音，聽起來很像本人（6） | Microsoft：personal voice 可 “get AI generated replication of their own voices in a few seconds”；美國聯邦貿易委員會（FTC）：“A scammer could use AI to clone the voice of your loved one.” | 相符 |
| 10 | 只能用內建的聲音或自己的聲音；沒有同意不可以模仿別人（6、8） | Microsoft：每個聲音都必須有本人明確同意並錄下聲明；ElevenLabs：未經同意不得刻意複製他人的聲音；Apple「個人聲音」：只能使用你本人的聲音 | 相符（這是廠商的使用規定，加上本課的課堂規定） |
| 11 | 聲音和影像都能合成，聽到看到不一定是真的（7） | 教育部注意事項：「不要輕易相信未經審核的影片或照片」；台灣警方宣導：「聲音、影像都能被偽造」 | 相符 |
| 12 | 警察提醒：詐騙集團利用 AI 模仿親友的聲音，假裝有急事要你匯錢（7） | 花蓮港務警察總隊轉載的宣導（114-07-02）：「詐騙集團利用人工智慧AI技術，模擬親友的聲音，製造緊急情境，誘使受害者匯款。」 | 相符；來源是警政署所屬單位轉載的宣導，不是刑事警察局本站 |
| 13 | 先掛斷，再打原本知道的號碼確認；全家約定家庭密語（7） | FTC：“Call the person … Use a phone number you know is theirs.”；FBI：“Create a secret word or phrase with your family”；台灣警方宣導：「設定家庭密語」「先用另一個你確定的聯絡方式…確認」；內政部：「先掛斷電話，後查證」 | 相符。FTC 的警示沒有提家庭密語，那是 FBI 與台灣警方的建議 |
| 14 | 不可以拿別人的臉和聲音來做東西（8） | Google 政策：禁止未明確揭露就冒充他人以欺騙；ElevenLabs 政策；Microsoft 的同意要求 | 相符；「就算只是好玩也不行」是本課的課堂規定，比廠商政策嚴 |
| 15 | 要標示哪些是自己做的、哪些是 AI；作業照老師規定註明工具（8、10） | 教育部注意事項六（四）：「應依規定註明所使用的工具及用途，不得將生成內容直接當作自己原創作品繳交。」；人工智慧基本法第四條：產出應做適當資訊揭露或標記（政府推動的原則） | 相符。基本法那一條不是對個人的標示義務，教材有說明 |
| 16 | 三站都不需要孩子的帳號：爸爸當機器人、自己畫、電腦內建朗讀（9） | Apple 支援（台灣）：「朗讀所選範圍」在「系統設定」>「輔助使用」>「閱讀與朗讀」（macOS 15 為「語音內容」） | 相符；影片沒有念出選單名稱，選單與版本寫在教材 |
| 17 | 二十秒旁白（9、10） | 課表任務；本系列自己的旁白語速約每秒 3.3–5 字，二十秒約 66–100 字 | 照這個語速，二十秒約 66–100 字；孩子自己念通常比較慢，教材建議 60–90 字。這是參考值，來自本系列的量測，不是外部來源 |

## 刻意避免的說法

- 沒有說 FTC 建議家庭密語（那是 FBI 與台灣警方的建議）。
- 沒有說「幾秒鐘的聲音就能複製」是台灣警方的說法；影片沒有提到需要多長的聲音。
- 沒有說浮水印或內容憑證能讓假內容一定被認出來。
- 沒有說 YouTube 豁免文字轉語音旁白，也沒有說本系列一定要勾選 AI 揭露；教材只把頁面的原文整理給爸爸判斷。
- 沒有說人工智慧基本法要求個人標示 AI 內容。
- 沒有使用「朗讀內容」「個人語音」這些不是 Apple 台灣用語的選單名稱；沒有說孩子可以用臺灣華語製作「個人聲音」。
- 沒有說影像樂園「在台灣可用」；教材寫的是支援繁體中文、需要 M1 以上的 Mac、部分功能未在所有地區提供。
- 沒有說 AI 畫的圖裡的字一定是錯的，也沒有說 AI 做的東西一定沒有著作權。
- 沒有說陳犀牛的聲音是某位真人的複製聲音；沒有對陳犀牛的圖像來源做任何說明（本次沒有查核）。
- 影片沒有示範任何真實 AI 工具的畫面或輸出。

## 課程與素材

- 課程主題、學習目標、120 分鐘流程（10／15／40／10／30／10／5）、動手任務（完成一個角色的文字介紹、概念圖與 20 秒旁白）、
  作品（多模態角色卡）與驗收，依 `curriculum/catalog.json` L013 核對。
- 沒有課堂錄音；本集是**依課表製作的課前教學版**，未虛構逐字稿或父子對話，封面、旁白第一句與說明均已揭露。
- 課表的好玩機制是尋寶：每站替角色做一樣東西，找出輸入、輸出和一個限制，再找出三個和描述不一樣的地方。
- 課表 25–65 的共同實作是三樣東西，75–105 是「增加一個自選規則或功能」；影片第 9、10、11 頁照這個順序。
- 片名是「文字、圖片、聲音 AI 體驗站」；旁白第一句念的是「我們要逛三個體驗站：文字、圖片和聲音」，避免英文縮寫夾在中文裡念得太短。
- 課表主要參考網址（R20）是 OpenAI Academy 首頁；本課沒有引用其中任何一頁。
- 課表的三組 YouTube 連結是動態搜尋入口；本次沒有挑選、觀看或引用任何影片。
'''

PLAN = '''# L013 文字、圖片、聲音 AI 體驗站

依課表製作的課前教學版；沒有課堂錄音，不製造逐字稿。
沿用原片頭 v2、陳犀牛、深藍／黃／青、12 頁原生可編輯簡報、36 句旁白、zh-TW-YunJheNeural；
教學段落靜態畫面加 0.55 秒淡化，無背景音樂、無推拉鏡頭。

## 課表核對（curriculum/catalog.json L013）

- 模組：M01 數位探險家；難度 2；主軸：數位素養／AI 素養／網路安全。
- 學習目標：比較不同生成媒介的輸入、輸出、限制與風險。
- 動手任務：完成一個角色的文字介紹、概念圖與 20 秒旁白。好玩機制：尋寶。
- 作品：多模態角色卡。生活技能支線：數位公民。
- 驗收：完成作品；不看稿說出核心原理；指出至少一個錯誤、限制或安全注意事項。

## 120 分鐘（課堂，與影片片長分開）

| 分鐘 | 內容 | 對應影片頁 |
|---|---|---|
| 00–10 | 任務開場：讓電腦念一句話給孩子聽，問「這是誰的聲音？」 | 1–2 |
| 10–25 | 概念示範：多模態、四個比較格子、圖片站、聲音站、聽到看到不一定是真的、三個約定 | 3–8 |
| 25–65 | 共同實作：三站尋寶，替角色完成文字介紹、概念圖與二十秒旁白；每站找輸入、輸出、限制，再找不一樣 | 9 |
| 65–75 | 休息 | — |
| 75–105 | 孩子獨立改造：組成多模態角色卡、標示誰做的，增加一個自選規則或功能 | 10 |
| 105–115 | 角色互換：孩子帶爸爸逛三站 | 12 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 11–12 |

## 12 頁

1 開場與揭露｜2 每站三件事｜3 多模態｜4 四個比較格子｜5 圖片站｜6 聲音站｜7 聽到看到不一定是真的｜
8 三個約定｜9 三站尋寶｜10 多模態角色卡｜11 兩小時安排｜12 驗收與結尾。

## 設計取捨

- 三站都有「不需要孩子帳號」的做法：文字站請爸爸當機器人（沿用 L011），圖片站自己畫，聲音站用 Mac 內建的朗讀功能。
  爸爸想用真的工具，由他用自己的帳號操作，不上傳任何人的照片和聲音。
- 影片坦白說陳犀牛的聲音是文字轉語音合成的；這是事實，也是聲音站最貼近的例子。
- 聲音模仿只教風險與規定，不教做法；Apple 的「個人聲音」不支援臺灣華語，而且只能用本人的聲音，本課不使用。
- 詐騙的應對照 FTC、FBI 與台灣警方共同的建議：先掛斷、打原本知道的號碼、約定家庭密語。
- 著作權只給保守建議（畫自己發明的角色），不替法院下結論。
- 作品上要標示每一樣東西是誰做的：自己、爸爸機器人、哪一個工具、電腦朗讀。

## 作品與驗收

- 多模態角色卡（文字介紹、概念圖、二十秒旁白稿，以及每一項是誰做的標示）。
- 尋寶地圖與三站比較表。
- 家庭密語卡（密語本身不寫在任何會存檔或上傳的地方）。
- 孩子帶爸爸逛三站：不看稿說出兩站的輸入、輸出和各一個限制，並指出一個限制或安全注意事項。
- 錄音四問（錄音只留私人區）。

## 教材

`classroom/L013_文字圖片聲音AI體驗站/`：爸爸先讀、三站尋寶規則、6 頁列印包（三站小抄卡、暖身找不一樣、尋寶地圖、角色設定與旁白稿紙、
多模態角色卡、三站比較表與家庭密語卡）、三站比較（CSV＋說明）、三站解說、自選規則與標示、驗收與回顧、三站小抄。
由 `authoring/l013/classroom.py` 產生；內容與來源查核見 fact-check.md。
'''

SUMMARY = '''這是依課表製作的課前教學版，不是實際上課錄音，也沒有虛構的課堂對話。

生成式 AI 不只會寫字，還能照著描述做出圖片和聲音。陳犀牛帶你逛三個體驗站：文字、圖片、聲音，每一站都看輸入、看輸出、做檢查。
看完影片，和爸爸逛三站尋寶，替一個自己發明的角色做出文字介紹、概念圖和二十秒旁白，最後組成一張多模態角色卡。

這一集會學到
・多模態：文字、圖片、聲音三種形式，各自的輸入和輸出
・用四個格子比較：輸入、輸出、限制、風險
・聲音和影像都能合成：遇到很急、要錢的電話，先掛斷，再打原本知道的號碼；全家可以約定家庭密語
・三個約定：不上傳自己和別人的照片、聲音；不模仿別人；用了要標示

教材用法（classroom.zip）
先讀「00_爸爸先讀」，列印「02_列印包」（A4 共 6 頁），照「01_活動規則」逛三站尋寶，用「03_三站比較」記錄；
各站的重點和暖身題的答案在「04_三站解說」，下半場照「05_自選規則與標示」組成多模態角色卡，最後用「06_驗收與回顧」讓孩子帶爸爸逛三站。「07_三站小抄」可以貼在電腦旁邊。

注意事項
・課堂是 120 分鐘，影片只是課前引導，片長另計。
・這一集的旁白是文字轉語音合成的，不是真人錄音。
・三站都有不需要孩子帳號的做法：爸爸當機器人、自己畫、用電腦內建的朗讀功能。各家 AI 工具都有年齡限制，要用請由爸爸用自己的帳號操作。
・不上傳自己或別人的照片和聲音；不模仿別人的臉和聲音；角色請畫自己發明的。

來源（查核日 2026-10-08）
教育部「中小學使用『生成式人工智慧』注意事項 2.1」（115 年 2 月核定）
Microsoft Learn「What is text to speech?」：https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech
OpenAI「Image generation guide」：https://developers.openai.com/api/docs/guides/image-generation
美國聯邦貿易委員會（FTC）消費者警示：https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes
FBI IC3 公告：https://www.ic3.gov/PSA/2024/PSA241203
內政部「先掛斷電話，後查證」：https://www.moi.gov.tw/News_Content.aspx?n=2&s=323333
經濟部智慧財產局函釋（114-05-22）：https://www.tipo.gov.tw/tw/copyright/692-34252.html
Apple 支援「讓 Mac 朗讀螢幕上的文字」：https://support.apple.com/zh-tw/guide/mac-help/mh27448/mac
'''

if __name__ == '__main__':
    lesson_builder.build(
        lesson=LESSON, slug=SLUG, ordinal='十三', title=TITLE, header_en='AI MEDIA STATIONS', checked=CHECKED,
        src=SRC, scenes=SCENES, visible=VISIBLE, board=BOARD,
        render_options={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        tts_basis="On 2026-10-08 the user asked to start producing L011–L013 after receiving L007–L010, whose hand-over stated that "
                  "the public narration is sent to Edge TTS on the same basis; restated to the user before synthesis.",
        source_records=SOURCE_RECORDS,
        source_method='A research subagent downloaded each page/PDF on the check date and reported verbatim quotes '
                      '(production/source-notes.md); the producing agent mapped them to claims. Not a human full read.',
        not_verified=['OpenAI 的條款與使用政策、Adobe 與 Canva 的條款只有擷取工具的摘要，沒有逐字確認，未依賴',
                      '刑事警察局（cib.npa.gov.tw）與 165 全民防騙網讀不到；台灣警方的說法取自花蓮港務警察總隊轉載的宣導資料',
                      'Microsoft 的文件記載 Azure 語音服務有 zh-TW-YunJheNeural；Edge TTS 提供同名聲音這一點沒有官方文件',
                      '影像樂園在台灣的實際可用情形沒有實機查核；Apple 的頁面只列出支援繁體中文',
                      '陳犀牛角色圖像的來源本次沒有查核，影片沒有對它做任何說明',
                      '沒有用任何真實 AI 工具產生圖片或聲音；教材沒有附 AI 生成的範例，暖身題的文字與圖是本課自己寫、自己用簡單圖形畫的',
                      'Mac 更換朗讀聲音的選單名稱沒有查核；教材請爸爸以自己的畫面為準'],
        documents={'fact-check.md': FACT_CHECK, 'plan.md': PLAN, 'delivery-summary.md': SUMMARY,
                   'source-notes.md': (Path(__file__).resolve().parent / 'source-notes.md').read_text(encoding='utf-8')},
        readme=lesson_builder.readme(LESSON, TITLE))
