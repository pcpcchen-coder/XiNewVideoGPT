"""Build the L013 classroom pack (real, usable materials; no private data, no AI account needed).

    ./portable-runtime.sh python authoring/l013/classroom.py

The warm-up "mock outputs" (one text, one picture) are written and drawn for this lesson with
planted differences; they are not output from any AI tool and are labelled as such on the page.
After any change here: rerun pipeline/delivery.py, then verify.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import classroom_pack  # noqa: E402
import printpack  # noqa: E402

# station, input, output, limits, risks
STATIONS = [
 ('文字站', '一段話（提示詞）', '一段話',
  ['句數、內容可能和你要求的不一樣', '可能加上你沒說的東西', '可能把錯的說得像真的'],
  ['把錯的內容當成真的', '把個資打進去']),
 ('圖片站', '一段描述', '一張圖',
  ['圖裡的字可能寫錯', '數目、顏色、位置可能和描述不一樣', '同一個角色，每次畫出來可能不一樣'],
  ['拿真人的照片去合成', '畫出別人創作的角色']),
 ('聲音站', '一段文字稿', '一段念出來的語音',
  ['有些字可能念錯，停頓可能怪怪的', '不知道哪一句要念得開心、哪一句要小聲'],
  ['模仿別人的聲音', '聽起來像親人的詐騙電話']),
]
PLEDGES = [('不上傳', '自己和別人的照片、聲音，都不放進去'),
           ('要同意', '不可以拿別人的臉和聲音來做東西，就算只是好玩也不行'),
           ('要標示', '哪些是自己做的，哪些是 AI 或電腦做的，都要說清楚')]

# Warm-up mock outputs: (what was asked, what came back, [(difference, kind)])
MOCK_TEXT_IN = '用三句話介紹一隻住在圖書館的小犀牛。牠喜歡看恐龍的書，害怕打雷。'
MOCK_TEXT_OUT = '小犀牛阿寶住在圖書館的二樓。牠最喜歡看太空的書，每天都要看五本。牠什麼都不怕，是圖書館裡最勇敢的動物。牠最好的朋友是一隻貓頭鷹。'
MOCK_TEXT_DIFFS = [('要求三句話，它寫了四句', '和要求不一樣'), ('恐龍的書變成太空的書', '和要求不一樣'), ('害怕打雷變成什麼都不怕', '和要求不一樣'),
                   ('名字阿寶、二樓、每天五本、貓頭鷹朋友', '你沒說，它自己加的')]
MOCK_PIC_IN = '一隻戴紅帽子的小犀牛，手上拿著三顆氣球，旁邊有一塊牌子寫著 HELLO，天上有太陽。'
MOCK_PIC_DIFFS = [('帽子是藍色的，不是紅色', '顏色'), ('氣球有四顆，不是三顆', '數目'), ('牌子寫 HELO，少了一個 L', '圖裡的字'), ('天上是月亮和星星，不是太陽', '細節')]
assert MOCK_TEXT_OUT.count('。') == 4 and '太空' in MOCK_TEXT_OUT and '恐龍' in MOCK_TEXT_IN
SCRIPT_BOXES = (15, 6)   # 90 boxes; the 60th box is marked

MOCK_PIC_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="100%" role="img" aria-label="模擬輸出：戴藍帽子的小犀牛拿著四顆氣球，牌子寫著 HELO，天上有月亮和星星">
<rect x="0" y="0" width="640" height="360" fill="#eef6fb"/>
<rect x="0" y="292" width="640" height="68" fill="#cfe8c6"/>
<circle cx="238" cy="62" r="30" fill="#f2c94c" stroke="#0b2540" stroke-width="2.5"/><circle cx="252" cy="54" r="27" fill="#eef6fb"/>
<polygon points="300,34 305,48 320,48 308,57 313,71 300,62 287,71 292,57 280,48 295,48" fill="#f2c94c" stroke="#0b2540" stroke-width="2"/>
<rect x="76" y="196" width="10" height="112" fill="#8a6b4a" stroke="#0b2540" stroke-width="2.5"/>
<rect x="24" y="140" width="116" height="60" rx="6" fill="#ffffff" stroke="#0b2540" stroke-width="3"/>
<text x="82" y="182" text-anchor="middle" font-family="Noto Sans CJK TC, sans-serif" font-weight="700" font-size="32" fill="#0b2540">HELO</text>
<g stroke="#0b2540" stroke-width="2">
<line x1="428" y1="262" x2="470" y2="118"/><line x1="428" y1="262" x2="520" y2="96"/><line x1="428" y1="262" x2="570" y2="126"/><line x1="428" y1="262" x2="604" y2="186"/></g>
<g stroke="#0b2540" stroke-width="2.5">
<ellipse cx="470" cy="86" rx="25" ry="31" fill="#e4573d"/><ellipse cx="520" cy="64" rx="25" ry="31" fill="#f2b632"/>
<ellipse cx="570" cy="94" rx="25" ry="31" fill="#35a9d6"/><ellipse cx="604" cy="154" rx="25" ry="31" fill="#7ac36a"/></g>
<path d="M162,236 q-26,-4 -30,22" fill="none" stroke="#0b2540" stroke-width="5" stroke-linecap="round"/>
<g fill="#aab3bb" stroke="#0b2540" stroke-width="3">
<rect x="176" y="270" width="34" height="44" rx="10"/><rect x="222" y="274" width="34" height="42" rx="10"/>
<rect x="286" y="274" width="34" height="42" rx="10"/><rect x="330" y="270" width="34" height="44" rx="10"/>
<ellipse cx="262" cy="240" rx="104" ry="64"/>
<ellipse cx="296" cy="166" rx="15" ry="22" transform="rotate(-20 296 166)"/>
<ellipse cx="350" cy="206" rx="64" ry="50"/></g>
<line x1="350" y1="256" x2="424" y2="264" stroke="#0b2540" stroke-width="24" stroke-linecap="round"/>
<line x1="350" y1="256" x2="424" y2="264" stroke="#aab3bb" stroke-width="18" stroke-linecap="round"/>
<polygon points="386,186 404,128 414,196" fill="#f4eedd" stroke="#0b2540" stroke-width="3" stroke-linejoin="round"/>
<polygon points="364,172 373,146 384,176" fill="#f4eedd" stroke="#0b2540" stroke-width="3" stroke-linejoin="round"/>
<path d="M306,166 Q334,104 362,160 Z" fill="#2f6fd0" stroke="#0b2540" stroke-width="3" stroke-linejoin="round"/>
<rect x="298" y="158" width="74" height="10" rx="5" fill="#2f6fd0" stroke="#0b2540" stroke-width="3"/>
<circle cx="352" cy="200" r="6" fill="#0b2540"/><circle cx="398" cy="214" r="3" fill="#0b2540"/>
<path d="M350,232 q22,14 44,2" fill="none" stroke="#0b2540" stroke-width="3" stroke-linecap="round"/>
</svg>'''

FILES = {
'00_爸爸先讀.md': f'''# 父子科技學院 L013：文字、圖片、聲音 AI 體驗站（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在孩子替自己發明的角色做出三樣東西，並且說得出每一站的輸入、輸出、限制和風險。

## 這堂課要帶走什麼

- 多模態：不只一種形式。文字站、圖片站、聲音站，各有自己的輸入和輸出。
- 每一站做三件事：看輸入、看輸出、做檢查。
- 用四個格子比較三站：輸入、輸出、限制、風險。限制是它做不好的地方；風險是可能傷害到人的地方。
- 聲音和影像都能合成：聽到的、看到的，不一定是真的。
- 三個約定：不上傳、要同意、要標示。
- 作品：**多模態角色卡**（文字介紹、概念圖、二十秒旁白，每一樣都標示是誰做的），另有尋寶地圖和三站比較表。

## 三站怎麼設：不需要孩子的帳號

各家 AI 工具都有年齡限制（見最後一節）。這份教材讓每一站都有「不用工具」的做法；要用真的工具，請由你用**自己的帳號**操作，孩子在旁邊說、你來打。

| 體驗站 | 不用工具 | 爸爸用自己的帳號 |
|---|---|---|
| 文字站 | 爸爸當機器人：孩子把提示詞念出來，你照字面回答三句話（玩法同 L011） | 你把孩子的提示詞打進你平常用的 AI 工具 |
| 圖片站 | 爸爸當畫圖機器人：孩子念描述，你照字面畫；或是孩子自己畫 | 你用自己的工具產生圖片；Mac 有「影像樂園」的話也可以用 |
| 聲音站 | 用 Mac 內建的朗讀功能念孩子寫的旁白稿；孩子自己再錄一次 | 同左。這一站不需要另外的工具 |

不管用哪一種：**不上傳任何人的照片和聲音，不輸入姓名、學校、住址等個資，不做真人的臉和聲音。**

### 讓 Mac 朗讀文字（Apple 台灣支援頁面的寫法）

1. 「蘋果」選單 >「系統設定」>「輔助使用」>「閱讀與朗讀」。macOS Sequoia 15 的這一項叫「語音內容」。
2. 開啟「朗讀所選範圍」。
3. 在任何 App 裡選取一段文字，按 **Option + Esc**（預設按鍵組合），Mac 就會念出來；再按一次停止。
4. 也可以在支援的 App 裡選「編輯」>「語音」>「開始朗讀」。

如果念出來的不是中文聲音，請在同一個設定頁更換聲音；這一步的選單名稱本次沒有查核，請以你的 Mac 畫面為準。
Mac 的朗讀和這支影片的旁白一樣，都是**文字轉語音**：電腦照著文字稿念，不是在模仿某一個人。

### 影像樂園（有的話再用）

- Apple 的功能適用範圍頁面列出影像樂園支援「中文（繁體）」，需要配備 M1 或更新晶片的 Mac，並註明部分功能可能未在所有地區提供。
  你的 Mac 上實際能不能用，本次沒有實機查核。
- Apple 的說明寫，可以在「螢幕使用時間」設定中阻擋取用影像製作功能；「寫實影像」的建議使用年齡是 18 歲以上。
- 這堂課只畫孩子**自己發明的角色**，不畫真人，也不畫別人創作的角色。

### 不使用「個人聲音」

Apple 的「個人聲音」可以做出聽起來像本人的合成聲音。Apple 的說明寫：只能用來製作聽起來像你本人的聲音；
只適用於英文（美國）、國語（中國大陸）和西班牙文（墨西哥）。它不支援臺灣華語，這堂課也不教模仿聲音的做法，所以不使用。

## 課前準備（約 15 分鐘）

1. 列印 `02_列印包_AI體驗站.pdf`（A4，共 6 頁，單面；第 2 頁建議彩色列印）。
2. 在 Mac 上照上面的步驟開好「朗讀所選範圍」，自己先試一次。
3. 讀一遍 `04_三站解說.md`，裡面有第 2 頁暖身題的答案。
4. 準備鉛筆、彩色筆、印章或貼紙（尋寶地圖蓋章用）、計時器。
5. 課表的課前準備是「確認兒童帳號、家庭備份與瀏覽器可用；準備不含真實個資的範例」。這堂課用不到兒童帳號；範例已經在列印包裡。
6. 錄音（孩子念旁白、最後的總結）只保存在家裡的私人位置，不上傳、不公開；錄音前先說課次與主題。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：讓 Mac 念一句話給孩子聽，問「這是誰的聲音？是人念的嗎？」 | 先不說答案 |
| 10–25 | 看影片，認識三站、四個比較格子、三個約定；做列印包第 2 頁的暖身題 | 回答問題；不知道的就說「我們等一下試試看」 |
| 25–65 | 父子共同實作：三站尋寶。每一站替角色做一樣東西，找三個寶藏（規則見 `01`） | 當機器人或操作自己的帳號；追問「哪裡和你說的不一樣？」 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：組成多模態角色卡、標示誰做的，增加一個自選規則或功能（見 `05`） | 只在孩子開口時協助 |
| 105–115 | 角色互換：孩子帶爸爸逛一次三個體驗站 | 當遊客，故意問「這是你畫的，還是電腦畫的？」 |
| 115–120 | 錄音總結、作品命名、版本存檔；檢查卡片上沒有真人的照片和個資 | 問四個錄音問題 |

## 家庭密語怎麼約

影片教的是：聽起來像親人、很急、要錢的電話，先掛斷，再打你原本就知道的號碼確認；全家可以先約定一個家庭密語。

- 密語是一個只有家人知道的字或句子。懷疑對方身分的時候才問。
- **密語不寫下來**：不寫在列印包、不打在手機、不放進任何 AI 工具，也不在錄音裡說出來。列印包第 6 頁的卡片只寫「怎麼用」，沒有寫密語的欄位。
- 對方答不出來，或是催你快一點：掛斷，打原本知道的號碼。有疑問可以撥 165 反詐騙專線。
- 依據：美國聯邦調查局（FBI）的公告建議和家人約定祕密的字或句子；台灣警方的宣導列了「設定家庭密語」「先用另一個你確定的聯絡方式去確認」；
  內政部的說法是「先掛斷電話，後查證」。美國聯邦貿易委員會（FTC）的警示寫的是不要相信那個聲音，打你知道是本人的號碼；它沒有提家庭密語。

## 幾個觀念的依據與限制

- **生成式 AI 能做文字、圖片、聲音**：Microsoft Learn 寫，它從資料中的規律產生文字、語音與圖像。UNICEF 的指引寫，它用統計規律預測語言、圖像與其他媒體的下一步來產生新內容。
- **圖片的限制**：OpenAI 的圖像生成指南寫，模型在文字的位置與清晰度上仍可能出問題；同一個角色跨多次生成不一定一致；構圖不一定照指定。
  Google 的技術文件寫，模型不一定產生你要求的確切張數。各家都說文字呈現已經改善，所以教材寫的是「可能」，不是「一定」。
- **圖片的偏向**：OpenAI 的 DALL·E 3 系統卡寫，它可能強化刻板印象，人物的呈現有偏向。教育部的注意事項也提醒留意文化刻板印象或不公平的描述。
  如果你用工具畫了人物，可以和孩子聊：它畫的人，是不是都長得差不多？
- **文字轉語音**：Microsoft Learn 寫，文字轉語音把文字變成像人聲的合成語音，又叫語音合成。
  這個系列的旁白用的是 zh-TW-YunJheNeural，Microsoft 把它列為臺灣華語的標準神經語音，是現成提供的聲音，不是我們拿某個人的聲音去複製的。
  這個聲音當初是怎麼錄製、訓練出來的，本課沒有查核。
- **聲音站的限制**：「有些字可能念錯、停頓怪怪的」是這個系列自己製作旁白時遇到的情形（例如夾在中文裡的英文縮寫念得太短），不是外部來源的說法。
- **模仿聲音要同意**：Microsoft 的 personal voice 要求每個聲音都有本人明確同意並錄下聲明；ElevenLabs 的政策寫，未經同意不得刻意複製他人的聲音。
- **不上傳照片**：教育部注意事項六（三）寫，不可以將自己或他人的姓名、照片、聯絡方式、住址、學號等個人資料輸入生成式人工智慧工具。「聲音」不在原文列舉內，是本課依同一道理延伸。
- **畫自己發明的角色**：智慧財產局 114-05-22 的函釋寫，AI 生成的圖畫與原始著作構成實質近似，可能有侵權問題；有沒有著作權，要看創作過程有沒有人類實際的創意投入。
  是否侵權由法院個案認定。本課給的是保守的建議，不是法律意見。
- **要標示**：教育部注意事項六（四）寫，應依規定註明所使用的工具及用途，不得將生成內容直接當作自己原創作品繳交。
  人工智慧基本法第四條有「產出應做適當資訊揭露或標記」的原則；那是政府推動人工智慧的原則，不是對個人的標示義務。
- **浮水印**：Google 的 SynthID 說明寫，它在 AI 生成的圖像、聲音、文字或影片裡嵌入人察覺不到、但可以偵測的浮水印。這不代表所有假內容都認得出來，影片沒有這樣說。

## 給上傳影片的爸爸：YouTube 的 AI 揭露

YouTube 說明頁「Disclosing use of GenAI content」寫的是（英文原文的整理，查核日 2026-10-08）：

- **需要揭露**：用 AI 大幅變造或生成的**擬真**內容，例如讓真人看起來說了或做了沒做過的事、變造真實事件或地點的影片、生成沒有發生過的擬真場景、以 AI 生成的音樂為影片主體。
- **不需要揭露**：非寫實的內容；用生成式 AI 協助製作（大綱、腳本、縮圖、標題、資訊圖）；產生字幕；複製**自己的**聲音來配音；全動畫影片裡的 AI 動畫。
- 這個系列用的是現成的文字轉語音旁白。頁面的兩份清單都沒有點名這種情形：旁白沒有讓任何真人看起來說了他沒說過的話，所以看起來不屬於第一項；但頁面也沒有寫這種旁白可以免揭露。
- 所以怎麼勾選由你判斷；這份教材沒有替你下結論。影片本身已經在第 6 頁說明旁白是合成的。

## 各家工具的年齡限制（查核日 2026-10-08）

- Google Gemini：產生圖片須年滿 13 歲（或所在國家適用的年齡），編輯圖片須年滿 18 歲。
  另一頁寫，未滿 13 歲的孩子要由家長替受監護的帳號開啟，才能使用 Gemini 應用程式；這一句說的是整個 App，不是產生圖片。
- Microsoft Copilot：說明頁寫至少 13 歲，有些國家更高。那一頁自己註明只適用 2026 年 8 月 18 日以前的 App 版本，現行規定請看最新頁面。
- ElevenLabs：未滿 13 歲不可使用；13 到 18 歲須先取得家長或監護人同意。
- OpenAI、Canva 的條款本次只有擷取工具的摘要，沒有逐字確認，請以官方頁面為準。Adobe Firefly 的年齡沒有查到。
- 教育部注意事項：應遵守各平臺註冊年齡限制及相關規範；非在校使用，請家長陪伴使用。

## 來源（查核日 2026-10-08）

- 教育部「中小學使用『生成式人工智慧』注意事項 2.1」（學生版，115 年 2 月 11 日核定；讀的是師大附中國中部網站轉載的 PDF）
- UNICEF「Guidance on AI and Children 3.0」（2025-12）：https://www.unicef.org/innocenti/media/11991/file/UNICEF-Innocenti-Guidance-on-AI-and-Children-3-2025.pdf
- Microsoft Learn「What is generative AI?」：https://learn.microsoft.com/en-us/training/modules/intro-generative-ai-explore-basics/2-what-is-generative-ai
- Microsoft Learn「What is text to speech?」：https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech
- Microsoft Learn「Language and voice support for the Speech service」：https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts
- Microsoft Learn「What is personal voice for text to speech?」：https://learn.microsoft.com/en-us/azure/ai-services/speech-service/personal-voice-overview
- OpenAI「Image generation guide」（Limitations）：https://developers.openai.com/api/docs/guides/image-generation
- OpenAI「DALL·E 3 System Card」：https://cdn.openai.com/papers/DALL_E_3_System_Card.pdf
- ElevenLabs「Prohibited Use Policy」：https://elevenlabs.io/use-policy
- 美國聯邦貿易委員會（FTC）消費者警示（2023-03-20）：https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes
- FBI IC3 公告 I-120324-PSA（2024-12-03）：https://www.ic3.gov/PSA/2024/PSA241203
- 內政部警政署花蓮港務警察總隊 反詐騙宣導（轉載刑事警察局宣導）：https://www.hlhpd.npa.gov.tw/
- 內政部「通話中直接撥打165？小心詐騙集團假冒警察」：https://www.moi.gov.tw/News_Content.aspx?n=2&s=323333
- 人工智慧基本法（總統府公報，115 年 1 月 14 日）：https://www.president.gov.tw/File/Doc/80165b6d-cb49-4b49-952f-56e1e6abe51b
- 經濟部智慧財產局 函釋（114-05-22）：https://www.tipo.gov.tw/tw/copyright/692-34252.html
- YouTube 說明「Disclosing use of GenAI content」：https://support.google.com/youtube/answer/14328491?hl=en
- Google DeepMind「SynthID」：https://deepmind.google/models/synthid/
- Apple 支援「讓 Mac 朗讀螢幕上的文字」：https://support.apple.com/zh-tw/guide/mac-help/mh27448/mac
- Apple 支援「在 Mac 上製作『個人聲音』」：https://support.apple.com/zh-tw/guide/mac-help/mchldfd72333/mac
- Apple 支援「在 Mac 上使用『影像樂園』製作獨創影像」：https://support.apple.com/zh-tw/guide/mac-help/mchld5412d00/mac
- Apple「macOS 功能特色適用範圍」：https://www.apple.com/tw/macos/feature-availability/
- Google Gemini 說明「Generate & edit images with Gemini Apps」：https://support.google.com/gemini/answer/14286560?hl=en
- Google Gemini 說明「Guide your child's Gemini Apps experience」：https://support.google.com/gemini/answer/16109150?hl=en
- Google Cloud「Gemini image generation limitations」：https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/gemini-image-generation-limitations
- Microsoft 支援「Microsoft Copilot for Young People」：https://support.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-young-people

課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
''',

'01_活動規則_三站尋寶.md': '''# 三站尋寶：規則

課表的好玩機制是「尋寶」。孩子是**尋寶隊長**，爸爸是**站長**。三個體驗站各藏著三個寶藏：輸入、輸出，還有一個限制。

## 準備

- 尋寶地圖（列印包第 3 頁）、角色設定單和旁白稿紙（第 4 頁）、印章或貼紙。
- 三站小抄卡（第 1 頁）放在旁邊。
- 三站怎麼設，見 `00_爸爸先讀.md`。三站都有不用工具的做法。

## 出發前：暖身找不一樣（約 5 分鐘，可以在看完影片後做）

列印包第 2 頁有兩個**模擬輸出**，是這堂課寫的、畫的，不是 AI 生成的，故意和要求不一樣。
請孩子把不一樣的地方圈出來，每一題至少找三個。答案在 `04_三站解說.md`。

## 出發前：發明一個角色（約 5 分鐘）

在第 4 頁的角色設定單寫下：名字、它是誰、喜歡什麼、有什麼本領、長什麼樣子。

- 角色要是**自己發明的**：不是真人，不是家人同學，也不是卡通、遊戲、書裡別人創作的角色。
- 名字不要用真人的名字。

## 第一回合：逛三站（一站約 9 分鐘）

每一站做同樣的四件事：

1. **做一樣東西**
   - 文字站：寫提示詞，請站長（或工具）用三句話介紹角色。
   - 圖片站：寫一段描述，請站長（或工具）畫一張概念圖；也可以自己照著描述畫。
   - 聲音站：寫一段大約二十秒的旁白稿（六十到九十個字），讓電腦念一次。
2. **找輸入**：我給它的是什麼？說得出來就蓋一個章。
3. **找輸出**：它交出來的是什麼？說得出來就蓋一個章。
4. **找一個限制**：它哪裡做不好？說得出一個就蓋第三個章。

三站逛完，地圖上應該有九個章。

## 第二回合：找不一樣（一站約 3 分鐘）

把「我說的」和「它做出來的」放在一起，每一站找出三個不同的地方，寫在地圖右邊。

- 文字站：句數對嗎？有沒有漏掉我說的事？有沒有多出我沒說的事？
- 圖片站：顏色、數目、圖裡的字、位置，和描述一樣嗎？
- 聲音站：孩子自己把旁白念一次，和電腦念的比一比：速度、停頓、哪個字念得不一樣、語氣。

找不到三個也沒關係，寫下「這次都一樣」。**做得和描述一樣，不代表下一次也會一樣。**

## 站長守則（爸爸）

- 當機器人的時候，照字面做，不替孩子把話補完。孩子沒說顏色，你就自己選一個；這正是「它自己加的」。
- 用真的工具時，由你操作自己的帳號，孩子在旁邊說。不上傳照片和聲音，不輸入個資，不做真人。
- 工具做出不適合孩子看的東西，直接關掉，換成不用工具的做法，之後再和孩子聊發生了什麼。
- 每一站問兩個問題：「你給它什麼？」「哪裡和你說的不一樣？」

## 計分（想玩再玩）

- 每蓋一個章：1 分。
- 每找到一個不一樣的地方：1 分。
- 說得出這一站的一個風險：2 分。
- 三站滿分 24 分。分數不是重點，重點是每一站都說得出四個格子。

## 常見卡關

- 孩子的角色是卡通人物：請他改成自己發明的。可以保留「喜歡的特點」（例如會飛、愛吃麵），換掉名字和樣子。
- 孩子想用自己的照片：今天的約定是不上傳。請他用畫的，或是用文字描述。
- 孩子說「電腦念得比我好」：請他說出電腦哪裡念得好、哪裡怪。兩種都可以放進角色卡，只要有標示。
- 二十秒念不完：刪到六十個字再試。旁白稿紙的第六十格有記號。
- 孩子問「那爸爸當機器人算是 AI 嗎？」：不算。這是扮演。角色卡上要寫「爸爸當機器人寫的」。
''',

'03_三站比較_填寫說明.md': '''# 三站比較怎麼寫

`03_三站比較.csv` 可以用 Numbers 或任何試算表開啟；也可以直接寫在列印包第 6 頁。

每一站寫一列：

- **體驗站**：文字站、圖片站、聲音站。
- **我做的東西**：例如「角色的三句介紹」。
- **輸入**：我給它的是什麼。
- **輸出**：它交出來的是什麼。
- **一個限制**：它哪裡做不好。寫自己看到的，不要抄小抄。
- **一個風險**：可能傷害到誰。
- **找到的不一樣**：第二回合找到的，最多寫三個。
- **誰做的**：我、爸爸當機器人、爸爸用工具（寫出工具名稱）、電腦朗讀。

最後一列留給下半場的自選規則或功能：寫下你加了什麼，還有測試的結果。

紀錄裡不需要寫任何人的姓名、帳號或其他個資；**家庭密語不要寫進來**。
''',

'04_三站解說.md': '''# 三站解說（爸爸用）

## 四個格子

| 體驗站 | 輸入 | 輸出 | 限制（它做不好的地方） | 風險（可能傷害到人的地方） |
|---|---|---|---|---|
''' + ''.join(f'| {s[0]} | {s[1]} | {s[2]} | {"；".join(s[3])} | {"；".join(s[4])} |\n' for s in STATIONS) + f'''
孩子說的和表上不一樣沒有關係，只要是他自己看到的、說得出理由，就算找到寶藏。

## 第 2 頁暖身題的答案

兩個模擬輸出都是這堂課寫的、畫的，**不是任何 AI 工具的輸出**，故意和要求不一樣。

### 文字

要求：{MOCK_TEXT_IN}

模擬輸出：{MOCK_TEXT_OUT}

| 哪裡不一樣 | 是哪一種 |
|---|---|
''' + ''.join(f'| {d[0]} | {d[1]} |\n' for d in MOCK_TEXT_DIFFS) + f'''
可以追問：「阿寶」這個名字是誰取的？如果你喜歡，可以留下來嗎？（可以。但要知道那是它加的，不是你說的。）

### 圖片

描述：{MOCK_PIC_IN}

| 哪裡不一樣 | 是哪一種 |
|---|---|
''' + ''.join(f'| {d[0]} | {d[1]} |\n' for d in MOCK_PIC_DIFFS) + '''
黑白列印看不出帽子的顏色。請直接告訴孩子「這頂帽子是藍色的」，或是改找另外三個。

可以追問：氣球多一顆，重要嗎？如果這張圖要用在「三顆氣球」的數學題呢？

## 每一站可以聊的事

### 文字站

- 上一堂（L012）學過：它可能把錯的說得像真的。這一站再加一件事：它可能做得和你要求的不一樣，也可能自己加東西。
- 提示詞寫得越清楚（任務、背景、限制、格式，見 L011），不一樣的地方通常越少；但還是要檢查。

### 圖片站

- 圖裡的字、東西的數目，是最容易檢查的地方。請孩子用手指一個一個數。
- 同一段描述做兩次，結果可能不一樣。有時間可以請孩子自己照同一段描述畫兩次，或是你用工具做兩次，放在一起看。
- 不畫真人，不畫別人創作的角色。孩子問為什麼，可以說：別人花心思創作的角色是別人的作品；真人的臉是那個人自己的。

### 聲音站

- 文字轉語音：電腦照著文字稿念。這支影片裡陳犀牛的聲音就是這樣合成的。
- 模仿聲音是另一種技術，可以做出聽起來很像某個人的聲音。這堂課**不做**，只談規定：只能用內建的聲音，或是你自己的聲音；沒有經過同意，不可以模仿別人。
- 請孩子比較自己念的和電腦念的。常見的不同是速度、停頓和語氣；實際會怎麼不同，要看你的 Mac 用的是哪一種聲音，這份教材沒有辦法替你先聽。

## 聽到、看到，不一定是真的

- 警方的宣導提過：詐騙集團利用 AI 模擬親友的聲音，製造緊急情境，要人匯款。
- 遇到這種電話：先掛斷，再打原本就知道的號碼確認。有疑問可以撥 165。
- 家庭密語怎麼約，見 `00_爸爸先讀.md`。密語不寫下來。
- 和孩子談的時候，重點放在「怎麼做」，不必描述可怕的細節。

## 給爸爸的提醒

- 這堂課沒有附任何 AI 生成的圖片或聲音當範例；第 2 頁的圖是這堂課用簡單的圖形畫的。
- 各家工具的能力和規定變得很快。這份教材的查核日是 2026-10-08；以後再用，請先看一下 `00_爸爸先讀.md` 列的來源有沒有更新。
''',

'05_自選規則與標示.md': '''# 孩子獨立改造：多模態角色卡

下半場做三件事。爸爸只在孩子開口時幫忙。

## 一、組成角色卡

把三站做出來的東西，放到列印包第 5 頁的角色卡上：

- **文字介紹**：三句話。它是誰、喜歡什麼、有什麼本領。可以照抄，也可以自己改寫。
- **概念圖**：貼上或畫上。把和描述不一樣的地方圈出來。
- **二十秒旁白**：把旁白稿抄上去。

## 二、標示每一樣東西是誰做的

每一格下面都有「誰做的」。照實勾選，可以複選：

- 我自己寫的／畫的／錄的
- 爸爸當機器人做的
- 爸爸用工具做的（寫出工具的名稱）
- 電腦朗讀念的

改過的也要說：例如「爸爸當機器人寫的，我改了第二句」。

為什麼要標示？讓看的人知道它是怎麼來的。學校的作業，要照老師的規定註明用了什麼工具、用在哪裡。

## 三、加一個自選的規則或功能

選一個，或自己發明。一次只加一個，才知道它有沒有用。

- **兩種旁白**：自己錄一次，再讓電腦念一次，比一比哪裡不同，在卡片上寫下你比較喜歡哪一種、為什麼。
- **口頭禪**：替角色加一句口頭禪，回到三站各試一次，看它有沒有照做。
- **做兩次**：同一段描述做兩次（或自己畫兩次），圈出兩次不一樣的地方。
- **第四格**：在卡片的每一樣東西旁邊，加寫「這一樣的限制」。
- **我的規定**：訂一條自己的使用規定，例如「圖要先圈出不一樣的地方，才可以貼到卡片上」。
- **換聲音**：把電腦朗讀換一種速度，說說看哪一種比較像你的角色。

我加的是：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

測試：加了以後，角色卡哪裡變了？有沒有哪裡變得更麻煩？要保留、修改，還是拿掉？

## 完成前檢查

- [ ] 卡片上沒有真人的照片
- [ ] 卡片上沒有姓名、學校、住址等個資
- [ ] 角色是我自己發明的
- [ ] 每一樣東西都有標示是誰做的
- [ ] 家庭密語沒有寫在任何地方
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成多模態角色卡：文字介紹、概念圖、二十秒旁白，每一樣都有標示
- [ ] 不看稿說出每一站做的三件事：看輸入、看輸出、做檢查
- [ ] 不看稿比較兩個體驗站：各自的輸入、輸出，還有各一個限制
- [ ] 尋寶地圖三站都有蓋章，每一站寫了找到的不一樣（或寫「這次都一樣」）
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 測試過一個自選的規則或功能，並說明要不要保留

## 孩子帶爸爸逛三站（105–115 分鐘）

請孩子當站長，爸爸當遊客。建議順序：

1. 孩子選兩個體驗站，說出它們的輸入、輸出，還有各一個限制。
2. 爸爸指著角色卡問：「這是你畫的，還是電腦畫的？」孩子指出標示。
3. 爸爸故意說：「我想把你的照片放進去，做一張更像的。」孩子說明為什麼不行。
4. 孩子說出一個限制或安全注意事項，例如：聲音可以被模仿，聽起來像家人，也要先查證。
5. 孩子出一題考爸爸，例如：「接到很急、要錢的電話，第一步做什麼？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

1. 文字、圖片、聲音 AI 體驗站，是在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

錄音裡不要說出家庭密語。

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：角色卡拍照存成 `L013_多模態角色卡_v01`，旁白錄音存成 `L013_角色旁白_v01`，
放進 `文件/Tech Academy/L013_文字圖片聲音AI體驗站/`，存好後再打開一次確認。
存檔前檢查：卡片上沒有真人的照片和個資；錄音只留在這個資料夾，不上傳、不公開。
''',

'07_三站小抄.md': '''# L013 三站小抄

## 每一站做三件事

1. **看輸入**：你給它的是什麼。
2. **看輸出**：它交出來的是什麼。
3. **做檢查**：哪裡和你說的不一樣，還有什麼事不可以做。

## 四個格子

| 體驗站 | 輸入 | 輸出 | 限制 | 風險 |
|---|---|---|---|---|
''' + ''.join(f'| {s[0]} | {s[1]} | {s[2]} | {s[3][0]} | {s[4][0]} |\n' for s in STATIONS) + '''
限制是它做不好的地方；風險是可能傷害到人的地方。

## 三個約定

''' + ''.join(f'{i}. **{p[0]}**：{p[1]}。\n' for i, p in enumerate(PLEDGES, 1)) + '''
## 很急、要錢的電話

1. 先掛斷。
2. 打你原本就知道的號碼確認。
3. 全家先約定家庭密語；密語不寫下來。

## 兩個提醒

- 聽到的、看到的，不一定是真的。
- 做得和描述一樣，不代表下一次也會一樣。

我最想記住的一個限制：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

SHEET_HEADER = ['體驗站', '我做的東西', '輸入', '輸出', '一個限制', '一個風險', '找到的不一樣', '誰做的']
SHEET_ROWS = [[s[0]] for s in STATIONS] + [['自選規則或功能測試']]

EXTRA_CSS = '''.st{padding:3.5mm 6mm;margin-bottom:5mm;height:50mm}.st h3{font-size:16pt;margin:0 0 1.5mm}.st .g{display:grid;grid-template-columns:1fr 1fr;gap:1.5mm 6mm;font-size:11pt}.st .g b{color:#1c6f9a}.st .g p{margin:0 0 .4mm}
.pl{border:1.6pt solid #0b2540;border-radius:3mm;padding:3.5mm 6mm;margin-top:1mm;font-size:11.5pt}.pl h3{font-size:15pt;margin:0 0 1mm}.pl p{margin:1.2mm 0}
.act{border:1.3pt solid #35a9d6;border-radius:3mm;padding:2.5mm 5mm;margin-top:4mm;font-size:11pt}
.mock{border:1.6pt solid #0b2540;border-radius:3mm;padding:3mm 5mm;margin-bottom:4mm}.mock h3{font-size:13pt;margin:0 0 1mm}
.mock .q{font-size:11pt;margin:1mm 0;color:#35506b}.mock .a{font-size:13pt;line-height:1.95;margin:0;border:.8pt solid #9db7cc;border-radius:2mm;padding:1.5mm 4mm;background:#f6fafd}
.fake{display:inline-block;font-size:9pt;font-weight:400;color:#fff;background:#0b2540;border-radius:1.5mm;padding:.2mm 2mm;margin-left:2mm;vertical-align:middle}
.pic{width:168mm;margin:1.5mm auto 0;border:.8pt solid #9db7cc;border-radius:2mm;overflow:hidden;line-height:0}
.found{font-size:11pt;margin:1.5mm 0 0}
.who{font-size:10pt;color:#35506b;margin:1.2mm 0 0}
.stop{border:1.6pt solid #0b2540;border-radius:3mm;padding:3mm 5mm;margin-bottom:4mm;height:68mm;display:grid;grid-template-columns:47% 1fr;gap:5mm}
.stop h3{font-size:15pt;margin:0}.stop p{margin:.8mm 0;font-size:10.5pt}
.stamps{display:flex;gap:4mm;margin-top:2mm}.stamp{width:23mm;text-align:center;font-size:9.5pt;color:#35506b}
.stamp i{display:block;width:21mm;height:21mm;border:1.4pt dashed #35a9d6;border-radius:50%;margin:0 auto 1mm}
.diff p{font-size:10.5pt;margin:0 0 .5mm}.diff .line{height:10.5mm}
.setup{border:1.3pt solid #0b2540;border-radius:3mm;padding:3mm 5mm;margin-bottom:4mm}.setup h3{font-size:14pt;margin:0 0 1mm}.setup p{margin:1.6mm 0;font-size:11.5pt}
.grid{border-collapse:collapse;table-layout:fixed;margin:2mm 0 0}.grid td{height:10.2mm;border:.7pt solid #7f9bb3;padding:0}.grid td.m{background:#fde9a8}
.card{height:240mm;padding:5mm 6mm}.card h3{font-size:16pt;margin:0 0 2mm}.card .top{display:grid;grid-template-columns:92mm 1fr;gap:5mm}
.card .art{height:100mm;border:1.2pt solid #7f9bb3;border-radius:2mm;font-size:9.5pt;color:#7f9bb3;padding:1.5mm 2.5mm}
.card h4{font-size:11.5pt;color:#0b2540;margin:0 0 .5mm}.card .line{height:11mm}
.own{border:1.3pt solid #35a9d6;border-radius:3mm;padding:2mm 4mm;margin-top:3mm;font-size:11pt}.own p{margin:1mm 0}
.cmp{table-layout:fixed}.cmp th{font-size:11pt;text-align:center}.cmp td{height:37mm;font-size:10pt}.cmp td.no{font-weight:700;font-size:12.5pt;vertical-align:middle;text-align:center;background:#f6fafd}
.pw{padding:4mm 6mm 5mm;margin-top:5mm}.pw h3{font-size:15pt;margin:0 0 1.5mm}.pw p{margin:1.8mm 0;font-size:11.5pt}'''


def html():
    pages = []
    st = lambda s: (f'<div class="cut st"><h3>{s[0]}</h3><div class="g"><div><b>輸入</b>　{s[1]}</div><div><b>輸出</b>　{s[2]}</div>'
                    '<div><p><b>限制</b>（它做不好的地方）</p>' + ''.join(f'<p>・{x}</p>' for x in s[3][:2]) + '</div>'
                    '<div><p><b>風險</b>（可能傷害到人的地方）</p>' + ''.join(f'<p>・{x}</p>' for x in s[4][:2]) + '</div></div></div>')
    pages.append('<h2>三站小抄卡</h2><p class="lead">沿外框剪下，逛到哪一站就拿哪一張。每一站做三件事：看輸入、看輸出、做檢查。</p>'
        + ''.join(st(s) for s in STATIONS)
        + '<div class="pl"><h3>三個約定</h3>' + ''.join(f'<p><b>{i}　{p[0]}：</b>{p[1]}。</p>' for i, p in enumerate(PLEDGES, 1)) + '</div>'
        '<div class="act"><b>很急、要錢的電話：</b>先掛斷　→　打你原本就知道的號碼確認　→　全家先約定家庭密語（密語不寫下來）。</div>'
        '<div class="act"><b>記得：</b>聽到的、看到的，不一定是真的。限制是它做不好的地方；風險是可能傷害到人的地方。</div>')

    pages.append('<h2>暖身：找不一樣</h2><p class="lead">下面兩個是這堂課寫的、畫的，不是 AI 生成的，故意和要求不一樣。把不一樣的地方圈出來，每一題至少找三個。</p>'
        '<div class="mock"><h3>文字<span class="fake">模擬輸出・這堂課寫的・故意不一樣</span></h3>'
        f'<p class="q">我的要求：{MOCK_TEXT_IN}</p><p class="a">{MOCK_TEXT_OUT}</p>'
        '<p class="found">我找到＿＿個不一樣。其中＿＿個是「我沒說，它自己加的」。寫下其中三個：</p><div class="line"></div></div>'
        '<div class="mock"><h3>圖片<span class="fake">模擬輸出・這堂課畫的・不是 AI 生成・故意不一樣</span></h3>'
        f'<p class="q">我的描述：{MOCK_PIC_IN}</p><div class="pic">{MOCK_PIC_SVG}</div>'
        '<p class="found">我找到＿＿個不一樣。寫下其中三個：</p><div class="line"></div></div>')

    made = {'文字站': '三句介紹', '圖片站': '一張概念圖', '聲音站': '二十秒旁白'}
    stop = lambda i, s: (f'<div class="stop"><div><h3>第 {i} 站　{s[0]}</h3><p>替角色做：<b>{made[s[0]]}</b></p>'
                         '<div class="stamps"><div class="stamp"><i></i>輸入</div><div class="stamp"><i></i>輸出</div><div class="stamp"><i></i>一個限制</div></div>'
                         '<p style="margin-top:2mm">我找到的限制：</p><div class="line" style="height:7mm"></div></div>'
                         '<div class="diff"><p><b>找不一樣</b>（我說的 和 它做出來的）</p><p>①</p><div class="line"></div><p>②</p><div class="line"></div><p>③</p><div class="line"></div></div></div>')
    pages.append('<h2>尋寶地圖</h2><p class="lead">每一站有三個寶藏：輸入、輸出、一個限制。說得出來就蓋章（或貼貼紙），再找三個不一樣。</p>'
        '<p style="margin:0 0 3mm;font-size:12pt">尋寶隊長的代號：＿＿＿＿＿＿＿＿　我發明的角色：＿＿＿＿＿＿＿＿＿＿＿</p>'
        + ''.join(stop(i, s) for i, s in enumerate(STATIONS, 1))
        + '<p class="note" style="margin:0">找不到三個，就寫「這次都一樣」。做得和描述一樣，不代表下一次也會一樣。</p>')

    cols, rows = SCRIPT_BOXES
    cells = ''.join('<tr>' + ''.join(f'<td{" class=m" if r * cols + c + 1 == 60 else ""}></td>' for c in range(cols)) + '</tr>' for r in range(rows))
    pages.append('<h2>角色設定單和旁白稿紙</h2><p class="lead">角色要是自己發明的：不是真人，也不是別人創作的角色。名字不要用真人的名字。</p>'
        '<div class="setup"><h3>我的角色</h3><p>名字：＿＿＿＿＿＿＿＿＿＿　　它是誰：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>喜歡什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿　有什麼本領：＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>長什麼樣子（顏色、穿戴、手上拿的東西）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p></div>'
        '<div class="setup"><h3>文字站：我的提示詞</h3><p>任務、背景、限制、格式，想到的都寫進去。</p><div class="line"></div><div class="line"></div></div>'
        '<div class="setup"><h3>圖片站：我的描述</h3><p>寫出顏色、數目，還有圖裡要不要有字。</p><div class="line"></div><div class="line"></div></div>'
        f'<div class="setup" style="margin-bottom:0"><h3>聲音站：二十秒旁白稿<small>一格一個字，標點也算；黃色那一格是第六十個字</small></h3>'
        f'<table class="grid">{cells}</table>'
        '<p style="font-size:10.5pt;margin:2mm 0 0">二十秒大約是六十到九十個字。自己念一次：＿＿秒　電腦念一次：＿＿秒</p></div>')

    pages.append('<h2>作品：多模態角色卡</h2><p class="lead">三站做出來的東西放在這裡。每一樣都要標示是誰做的；和描述不一樣的地方，圈出來。</p>'
        '<div class="cut card"><h3>角色名字：＿＿＿＿＿＿＿＿＿＿＿＿</h3>'
        '<div class="top"><div><h4>概念圖</h4><div class="art">貼上或畫在這裡</div></div>'
        '<div><h4>文字介紹（三句話）</h4><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div>'
        '<p class="who" style="margin-top:2.5mm"><b>文字介紹</b>是誰做的：<br>□ 我寫的　□ 爸爸當機器人寫的<br>□ 爸爸用工具：＿＿＿＿＿＿＿</p>'
        '<p class="who" style="margin-top:3mm"><b>概念圖</b>是誰做的：<br>□ 我畫的　□ 爸爸當機器人畫的<br>□ 爸爸用工具：＿＿＿＿＿＿＿</p></div></div>'
        '<h4 style="margin-top:4mm">二十秒旁白稿</h4><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div>'
        '<p class="who">稿子是誰寫的：□ 我　□ 爸爸　　念的人：□ 我自己錄的　□ 電腦朗讀　□ 兩種都有</p>'
        '<div class="own"><p><b>我加的自選規則或功能：</b>＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>測試之後：□ 保留　□ 修改　□ 拿掉　　因為：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p></div>'
        '<p class="who" style="margin-top:3mm">完成前檢查：□ 沒有真人的照片　□ 沒有個資　□ 角色是我發明的　□ 每一樣都有標示</p>'
        '<p class="who">名稱：L013_多模態角色卡_v＿＿　日期：＿＿＿＿＿＿</p></div>')

    cmp_rows = ''.join(f'<tr><td class="no">{s[0]}</td><td></td><td></td><td></td><td></td></tr>' for s in STATIONS)
    pages.append('<h2>三站比較表</h2><p class="lead">用四個格子比較三站。寫你自己看到的，不要抄小抄。</p>'
        '<table class="cmp"><tr><th style="width:14%">體驗站</th><th>輸入<br><small style="margin:0">我給它什麼</small></th><th>輸出<br><small style="margin:0">它交出什麼</small></th>'
        '<th>限制<br><small style="margin:0">它做不好什麼</small></th><th>風險<br><small style="margin:0">可能傷害到誰</small></th></tr>' + cmp_rows + '</table>'
        '<p style="font-size:11.5pt;margin:3mm 0 0">三站最像的地方：＿＿＿＿＿＿＿＿＿＿＿＿＿＿　最不一樣的地方：＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<div class="cut pw"><h3>我們家的密語卡<small>這張卡只寫怎麼用，不寫密語</small></h3>'
        '<p><b>密語放在哪裡：</b>只記在腦袋裡。不寫下來、不打在手機裡、不放進任何 AI 工具、不告訴家人以外的人。</p>'
        '<p><b>什麼時候問：</b>對方聽起來像家人，可是很急、要錢，或是叫你不要告訴別人。</p>'
        '<p><b>答不出來，或是催你快一點：</b>①先掛斷　②打你原本就知道的號碼　③告訴爸爸媽媽。有疑問可以撥 165。</p>'
        '<p>我們約好了：□ 全家都知道密語　□ 沒有寫在任何地方　□ 練習過一次</p><p>約定的日期：＿＿＿＿＿＿</p></div>')
    return printpack.document('L013 文字、圖片、聲音 AI 體驗站 列印包', '父子科技學院 L013｜文字、圖片、聲音 AI 體驗站', pages, EXTRA_CSS)


if __name__ == '__main__':
    classroom_pack.build(
        slug='l013-multimodal-stations', folder='L013_文字圖片聲音AI體驗站', files=FILES,
        sheet=('03_三站比較.csv', SHEET_HEADER, SHEET_ROWS),
        pack_html=html(), pack_pdf='02_列印包_AI體驗站.pdf', pack_pages=6,
        pack_needles=('三站小抄卡', '三個約定', '找不一樣', '這堂課畫的', '尋寶地圖', '旁白稿紙', '多模態角色卡', '三站比較表', '密語卡'),
        authoring_dir=Path(__file__).resolve().parent,
        extra={'mockOutputs': {'text': 1, 'picture': 1, 'writtenOrDrawnForLesson': True, 'notOutputOfAnyAiTool': True, 'labelledOnPage': True,
                               'plantedDifferences': {'text': len(MOCK_TEXT_DIFFS), 'picture': len(MOCK_PIC_DIFFS)},
                               'pictureIs': 'hand-written SVG of simple shapes; hat colour difference needs a colour print'},
               'stationsWithoutTools': {'text': 'father role-plays a literal robot', 'image': 'father or child draws from the description',
                                        'voice': 'macOS built-in Speak Selection plus the child reading aloud'},
               'needsChildAiAccount': False, 'noAiGeneratedSamplesIncluded': True, 'voiceCloningTaught': False,
               'familyCodeWord': 'usage card only; the pack has no field to write the code word',
               'scriptLength': '60–90 characters for about 20 seconds; the 60th box of a 90-box grid is marked'})
