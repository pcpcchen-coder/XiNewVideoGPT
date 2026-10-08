# L012 來源查核筆記（研究代理回報）

2026-10-08 由製作代理派出的研究子代理蒐集。子代理下載原始頁面後抽取文字並回報引文；它自己標示了哪些是逐字讀到的、
哪些只是擷取工具的摘要。主代理沒有逐頁重讀，只用這份筆記對照旁白、投影片與教材。以下為回報原文。

---

L012 SOURCE VERIFICATION (fetched 2026-10-08)

Marks: [V] = read in raw HTML/PDF text I downloaded; [T] = WebFetch extraction only.
Could not download directly (the sites' own bot walls, not the proxy): help.openai.com, openai.com, worldwildlife.org, CRT decisions site (captcha), conservation.forest.gov.tw (empty reply) -> [T]. Not obtained at all: Reuters (blocked) and CanLII (robots).

PART A

A1 Definition - SUPPORTED
- NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile", July 2024, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf §2.2 [V]: "“Confabulation” refers to a phenomenon in which GAI systems generate and confidently present erroneous or false content in response to prompts. ... These phenomena are colloquially also referred to as “hallucinations” or “fabrications.”"
- IBM, "What Are AI Hallucinations?", published 01 September 2023, updated 31 July 2026, https://www.ibm.com/think/topics/ai-hallucinations [V]: "AI hallucinations are instances where an AI system produces outputs that sound plausible but are factually wrong, irrelevant or entirely fabricated."
- Anthropic, "Reduce hallucinations" (Claude Platform Docs), no date, https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations [V]: "Even the most advanced language models, like Claude, can sometimes generate text that is factually incorrect or inconsistent with the given context. This phenomenon, known as "hallucination," ..."
- Google, "Learn about responses from Gemini Apps", no date, https://support.google.com/gemini/answer/16279220?hl=en [V]: "Gemini can hallucinate and present inaccurate information as factual."
- MIT Sloan Teaching & Learning Technologies, "When AI Gets It Wrong: Addressing AI Hallucinations and Bias", no date, https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/ [V]: "Generative AI tools can produce fabricated information that appears authentic—a problem widely known as “hallucination”"
- Chinese term:
  - Google, same page ?hl=zh-Hant [V]: 「Gemini 可能會產生幻覺，將不準確的資訊當做事實」
  - 教育部中小學數位素養教育資源網, 教案【AI的練習曲】(高中；設計者 國立陽明交通大學), no date, https://eliteracy.edu.tw/Download.ashx?id=1817 [V]: 「AI可能會有幻覺，或者對自己處理的文獻內容有不精確、甚至是錯誤的理解」
  - LIMIT: 教育部「注意事項2.1」(both versions) contains zero 「幻覺」 [V]; it says 偏誤／錯誤／虛構景點. 數位發展部 use of the term: NOT FOUND.

A2 What gets made up - SUPPORTED (no single source lists all five)
- OpenAI Help Center, "Does ChatGPT tell the truth?", "Updated: 2 months ago", https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth [T]: "Incorrect definitions, dates, or facts"; "Fabricated quotes, studies, citations or references to non-existent sources"; "Overconfident answers to ambiguous or complex questions"
- IBM [V]: "presents fake facts, invented studies, nonexistent URLs or incorrect details about real entities as factual outputs."
- NIST [V]: "GAI outputs may also include confabulated logic or citations that purport to justify or explain the system’s answer"
- Google Gemini help [V]: "Gemini Apps may provide inaccurate or inappropriate responses about people, so double-check its responses."
- eliteracy 教案 [V]: 「若AI有提供統計數據、名言、法條、專有名詞，應至原始文件或官方網站核實。」

A3 Why - SUPPORTED
- NIST [V]: "Confabulations are a natural result of the way generative models are designed: they generate outputs that approximate the statistical distribution of their training data; for example, LLMs predict the next token or word in a sentence or phrase."
- MIT Sloan [V]: "Generative AI models function like advanced autocomplete tools: They’re designed to predict the next word or sequence based on observed patterns. Their goal is to generate plausible content, not to verify its truth."
- arXiv 2509.04664 abstract, "Why Language Models Hallucinate", https://arxiv.org/abs/2509.04664 [V]: "large language models sometimes guess when uncertain, producing plausible yet incorrect statements instead of admitting uncertainty."
- 教育部 2.1 學生版 第一點 [V]: 「…如果這些資料本身具有成見或錯誤，那麼使用「生成式人工智慧」工具的結果也會存在偏差或錯誤，因為這些工具無法自行判斷結果的正確性和合理性。」

A4 Cases
(i) Mata v. Avianca - SUPPORTED [V]. Source is the RECAP copy of the court's own filing, not a court-hosted URL (none found): https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_3.pdf
- Header: "Case 1:22-cv-01461-PKC Document 54 Filed 06/22/23", "OPINION AND ORDER ON SANCTIONS", Castel, U.S.D.J.; "Dated: New York, New York June 22, 2023".
- "Peter LoDuca, Steven A. Schwartz and the law firm of Levidow, Levidow & Oberman P.C. ... abandoned their responsibilities when they submitted non-existent judicial opinions with fake quotes and citations created by the artificial intelligence tool ChatGPT"
- "A penalty of $5,000 is jointly and severally imposed on Respondents" - one $5,000 total for two lawyers plus the firm, not $5,000 each.
- Six fake decisions: "the “Varghese”, “Miller”, “Petersen”, “Shaboon”, “Martinez” and “Durden” decisions were generated by ChatGPT and do not exist."
- Balance: "there is nothing inherently improper about using a reliable artificial intelligence tool for assistance."
(ii) Bard - PARTLY
- NPR, "Google's AI chatbot, Bard, sparks a $100 billion loss in Alphabet shares", February 9, 2023, https://www.npr.org/2023/02/09/1155650909/google-chatbot--error-bard-shares [V]: the prompt was "What new discoveries from the James Webb Space Telescope can I tell my 9 year old about?"; Bard's reply included "the claim that the telescope took the very first pictures of "exoplanets,""; "The European Southern Observatory's very large telescope took the first pictures of those special celestial bodies in 2004, a fact that NASA confirms."; shares "dropped 9% Wednesday". The ad tweet is dated February 6, 2023.
- NASA Science, "2M1207 b – First image of an exoplanet", April 26, 2010, https://science.nasa.gov/resource/2m1207-b-first-image-of-an-exoplanet [V]: "2M1207 b is the first exoplanet directly imaged ... It was imaged for the first time in 2004 by the Very Large Telescope (VLT), operated by the European Southern Observatory".
- ESO, https://www.eso.org/public/images/26a_big-vlt/ [V]: "It was imaged the first time by the VLT in 2004."
- Google's own statement and Reuters: NOT OBTAINED. "$100 billion" appears only in NPR's headline.
(iii) Moffatt v. Air Canada, 2024 BCCRT 149 - [T] only, https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do: issued February 14, 2024, member Christopher C. Rivers; "I find Air Canada did not take reasonable care to ensure its chatbot was accurate."; "It should be obvious to Air Canada that it is responsible for all the information on its website."; ordered $812.02 total ("$650.88 in damages", "$36.14 in pre-judgment interest", "$125 in CRT fees"). No second source checked; I would not use it on screen.

A5 How to check - SUPPORTED
- 教育部「中小學使用『生成式人工智慧』注意事項2.1」學生版 (115年2月11日臺教資（一）字第1152700391號函核定), https://jr.hs.ntnu.edu.tw/wp-content/uploads/2026/02/中小學使用「生成式人工智慧」注意事項2.1.pdf - re-opened, HTTP 200 [V]. An MOE-hosted copy was found only for the teacher version: https://eliteracy.edu.tw/Upload/pdfs/附件1-中小學使用生成式人工智慧注意事項2.1_教師_行政人員及家長版_F1150211-.pdf [V]. No newer version found.
  - 二、檢核內容並結合多元管道查證: 「所以當我們在使用「生成式人工智慧」工具時，不能全盤接受生成的內容，而需結合其他可靠來源的知識和批判性思維進行查證，並留意其中是否涉及文化刻板印象或不公平的描述，如對內容仍有疑慮，應向老師或家長請教，不可以直接將生成內容作為作業或報告的原始答案。」
  - 結語: 「1. 保持對資訊來源保持的高度警覺。 2. 不要輕易相信未經證實的訊息。 3. 學會如何辨別虛假資訊。」 (the doubled 保持 is in the original)
  - 示例一: 「…甚至還可能是虛構景點的行程。因此，當AI給出的資訊看起來奇怪、不合常理或與課本不同時，我們要停下來檢查內容，不要直接用在作業或報告上，並主動向老師或家長確認資訊是否正確。」
- Google Search Help, "Find information in faster & easier ways with AI Overviews in Google Search", no date, https://support.google.com/websearch/answer/14901683?hl=en [V]: "How to double-check responses: Always check important info in more than one place. Click the links to supporting information from the web and try other Google Search results too." zh-Hant [V]: 「務必多方查證重要資訊。點按連結，參閱網路上的佐證資訊和其他 Google 搜尋結果。」
- OpenAI help [T]: "Always verify quotes, data, technical information or references to external documents."; "...check sources when accuracy matters by visiting links directly."
- Anthropic Consumer Terms of Service, "Effective October 8, 2025", https://www.anthropic.com/legal/consumer-terms [V]: "You should not rely on any Outputs or Actions without independently confirming their accuracy."
- Lateral reading: Digital Inquiry Group, Civic Online Reasoning, "Teaching Lateral Reading", no date, https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading [V]: "the best way to learn about a website is lateral reading—leaving a site to see what other digital sources say about it."
- eliteracy 教案 [V]: 「交叉比對搜尋：使用鎖定的關鍵字在不同來源搜尋…」「追溯原始資料：檢查原始報告中的內容是否與AI的描述一致。」
- CHANGED: Google's page https://support.google.com/gemini/answer/14143489 is now titled "View related sources from Gemini Apps" and no longer describes a "double-check response" button [V]. It also says "Not all responses include related links or sources."

A6 Confident when wrong - SUPPORTED. "Won't tell you when unsure" - PARTLY (sources say it guesses; none says it never flags uncertainty).
- NIST [V]: "Risks from confabulations may arise when users believe false content – often due to the confident nature of the response"
- OpenAI help [T]: "Sometimes, it might sound confident—even when it’s wrong."
- Anthropic terms [V]: "Outputs may not always be accurate and may contain material inaccuracies even if they appear accurate because of their level of detail or specificity."
- Google, "AI Overviews and AI Mode in Search", May 2025, https://search.google/pdf/google-about-AI-overviews-AI-Mode.pdf [V]: "it may sometimes confidently present information that is inaccurate, which is commonly known as “hallucination.”"
- "Are you sure?": no vendor says re-asking fixes it. Evidence against, Mata order ¶45 [V]: Schwartz asked ChatGPT "“Is Varghese a real case” and “Are the other cases you provided fake”" and "ChatGPT responded that it had supplied “real” authorities that could be found through Westlaw, LexisNexis and the Federal Reporter." One 2023 case, not a general rule.
- Anthropic docs [V] (developer prompting advice, not a user fix): "Allow Claude to say "I don't know" ..."; "while these techniques significantly reduce hallucinations, they don't eliminate them entirely."

A7 Search-connected tools - SUPPORTED
- OpenAI Help Center, "Searching the web with ChatGPT", "Updated: 2 months ago", https://help.openai.com/en/articles/9237897-chatgpt-search [T]: "Search results and citations can be incomplete, outdated, or incorrect."; "Open a cited source to check that it supports the answer"
- Google AI Overviews help [V]: "AI Overviews can and will make mistakes." zh-Hant [V]: 「因此，我們無法確保 AI 摘要內容皆正確無誤。」
- Google PDF [V]: "in some cases this experiment may misinterpret web content or miss context"
- Gemini help [V]: "Gemini can misrepresent how it works, including ... (like citing sources, or providing fresh information)."
- NOT FOUND: a vendor sentence saying outright that a cited page may not contain the claim.

PART B

B1 Rhinos. Sources: International Rhino Foundation "2026 State of the Rhino" (September 2026), https://rhinos.org/about-rhinos/state-of-the-rhino/ and its PDF https://rhinos.org/wp-content/uploads/2026/09/State-of-the-Rhino-2026_FINAL.pdf; IRF species pages under https://rhinos.org/about-rhinos/rhino-species/; Save the Rhino https://www.savetherhino.org/rhino-info/population-figures/ and species pages. All [V].
- Five species: IRF "the five surviving rhino species in Africa and Asia" - white, black, greater one-horned, Javan, Sumatran.
- Horns (IRF): "White rhinos have two horns."; "Black rhinos have two horns."; "Sumatran rhinos have two horns."; "Greater one-horned rhinos have a single horn"; "Javan rhinos possess a single horn 10 in (25 cm) long, at least in males; females have a smaller or no horn."
- Keratin (IRF): "Rhino horn is made of compressed keratin fibers, the same material that is found in fingernails and hair."
- Largest: PARTLY. Save the Rhino says only "the white rhino is the larger of the two African species"; IRF gives white and greater one-horned the same weight. Avoid "largest of all rhinos".
- White rhino weight: DISAGREE - IRF "1,800 – 2,700 kg"; Save the Rhino "1,800 - 2,500 kg". Avoid, or say 約2公噸.
- Diet (IRF): "White rhinos are grazers."; "Black rhinos are browsers." WWF [T]: "megaherbivores—plant-eaters". 吃植物 is safe.
- Gestation (IRF): white "approximately 16 months"; black, greater one-horned and Sumatran "approximately 15 – 16 months"; Javan "Gestation is unknown".
- Populations, agreeing between IRF 2026 and Save the Rhino ("as reported in 2025 by the IUCN SSC African and Asian Rhino Specialist Groups"): white 15,752 (2024 count); black 6,788 (end of 2024); greater one-horned 4,075; Javan about 50; Sumatran 34–47; "The total global population of rhinos is approximately 26,700."
  - DISAGREE: WWF [T] still says "around 76 Javan rhinos"; IRF's Sumatran page says both "Fewer than 80" and "34-47"; the earlier white count is 17,464 (2023) in IRF 2026 but 15,942 (end of 2021) in IRF's 7 August 2025 release; black rhino 1970 figure is 65,000 (IRF) vs 70,000 (Save the Rhino).
- IUCN status (IRF): Javan and Sumatran "Critically Endangered"; black Critically Endangered; greater one-horned Vulnerable; white Near Threatened.
- Speed (Save the Rhino only): white "up to 40 km/h for short periods"; greater one-horned "up to 40 km/h"; black "recorded at highs of 55 km/h". Single source, differs by species.
- Senses: IRF "keen sense of smell and hearing, but they have poor vision"; Save the Rhino "poor eyesight, but acute senses of hearing and smell".

B2 Yushan [V]
- 玉山國家公園管理處, https://www.ysnp.gov.tw/StaticPage/Terrain (更新日期：115-10-08): 「十字之交點即為玉山主峰，海拔3,952公尺。」
- 同站 https://www.ysnp.gov.tw/StaticPage/Vision: 「其間有臺灣第一高峰，海拔3,952公尺之玉山主峰」；「玉山國家公園為我國第2座國家公園」
- 行政院國情簡介「國家公園簡介」(日期：114/04/21，資料來源：內政部), https://www.ey.gov.tw/state/4447F4A951A1EC45/dc08391a-c57c-4cf7-af9a-cc0d9e4ebb1c: 「玉山國家公園 成立時間：74年4月」；「臺灣最高峰，海拔3,952公尺的玉山主峰」 (民國74年 = 1985). Day of month not on an official page I fetched.
- The three official pages agree on 3,952. 中央氣象署 additionally calls it 「東北亞第一高峰」 - avoid.

B3 Moon / Apollo 11 [V]
- Distance: NASA, https://science.nasa.gov/moon/facts/: "The Moon is an average of 238,855 miles (384,400 kilometers) away." The same page also rounds to 385,000 and 384,000 km; use 平均約38萬4千公里.
- Landing: NASA history, https://www.nasa.gov/wp-content/uploads/static/history/ap11ann/FirstLunarLanding/ch-1.html: "On July 20 at 4:18 p.m. EDT, the Lunar Module touched down on the Moon ... And at 10:56 p.m., Armstrong ... touching one foot to the Moon's surface". NASA gives EDT only; no UTC note found. My own conversion: the first step falls on July 21 in UTC and in Taiwan time. Use 1969年7月20日（美國時間） and avoid the minute.
- Crew: NASA, Jul 20, 2019, https://www.nasa.gov/centers-and-facilities/kennedy/50-years-ago-apollo-astronauts-land-take-first-steps-on-moon/: "Commander Neil A. Armstrong ... Lunar Module Pilot Edwin “Buzz” Aldrin ... Command Module Pilot Michael Collins remained in the command and service module (CSM), called Columbia, orbiting above."
- Twelve walkers: NASA, https://science.nasa.gov/moon/moon-walkers/: "Neil Armstrong and Edwin "Buzz" Aldrin were the first of 12 human beings to walk on the Moon." Still current: "Four more humans, the Artemis II crew, traveled around the Moon in 2026" (no landing).
- Sunlight: NASA Astrobiology, https://astrobiology.nasa.gov/quick-facts/more-quick-facts/: "Light from the Sun takes 8 minutes and 20 seconds to reach Earth." NASA SVS, https://svs.gsfc.nasa.gov/11084: "Light takes eight minutes". NASA StarChild says "8.5 minutes" (of heat). Use 大約8分鐘.

B4 Formosan black bear
- 玉山國家公園管理處「臺灣黑熊科普」(更新日期：115-10-08), https://www.ysnp.gov.tw/StaticPage/Science [V]: 「臺灣黑熊為瀕臨絕種野生動物。目前族群在臺灣僅剩下約200~600隻。」；「最大的特徵便是胸前的黃白色V字形或新月形斑紋，故又名"月熊"。」 Note 黃白色, not pure white, and "V字形或新月形".
- 農業部林業及自然保育署《臺灣黑熊保育行動計畫》, 2025年9月, https://conservation.forest.gov.tw/File.aspx?fno=91564 [T]: 「胸前黃白色 V 字形斑紋」；「臺灣黑熊為野生動物保育法公告的瀕臨絕種保育類野生動物」；「現今臺灣黑熊族群量為 139-621 隻不等（林容安 2013）」
- 林務局期刊〈臺灣黑熊救援案件紀實〉, https://www.forest.gov.tw/MagazineFile/6855 [V]: 「全島族群數量推估約有數百隻」; IUCN「易危物種」 but 我國「瀕臨絕種野生動物」.
- Population: DISAGREE (200~600 / 139-621 / 數百隻). Use no number, or 數百隻.

DO NOT SAY
- "Asking 'are you sure?' makes the AI correct itself" - unsupported; Mata shows the opposite once.
- "AI with search or links doesn't hallucinate" - contradicted by OpenAI and Google.
- "Press Google's double-check button" - no longer on Google's help page.
- "教育部注意事項說 AI 有『幻覺』" - the word is not in it.
- "Each lawyer was fined $5,000", or that the court banned AI.
- "Webb has never photographed an exoplanet", "Bard cost Google $100 billion" as fact, or any Google statement.
- Any hallucination percentage. MIT Sloan's legal-research figures are secondary and dated.
- "White rhino is the largest rhino", exact white rhino weight, one "rhino top speed", "76 Javan rhinos", 1970 black rhino totals.
- A specific 臺灣黑熊 count; 「白色V字」 (official wording is 黃白色); 玉山「東北亞第一高峰」; the Apollo landing minute; how many moonwalkers are still alive.
- Moffatt details on screen (single [T] source).
