# L010 事實查核

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
