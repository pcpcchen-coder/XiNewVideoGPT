# L011 事實查核

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
