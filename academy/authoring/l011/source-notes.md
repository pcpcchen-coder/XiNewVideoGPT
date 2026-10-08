# L011 來源查核筆記（研究代理回報）

2026-10-08 由製作代理派出的研究子代理蒐集。子代理下載原始頁面後抽取文字並回報引文；它自己標示了哪些是逐字讀到的、
哪些只是擷取工具的摘要。主代理沒有逐頁重讀，只用這份筆記對照旁白、投影片與教材。以下為回報原文。

---

L011 SOURCE VERIFICATION (checked 2026-10-08)
[V] = read in raw HTML/PDF text I downloaded; [V-img] = image-only PDF, pages rendered and read by eye; [T] = WebFetch extraction only.

Could not fetch raw:
- help.openai.com and openai.com: HTTP 403 to curl, so all OpenAI help/terms quotes are [T].
- pads.moe.edu.tw (official download page for 數位教學指引): TLS certificate failure in curl and WebFetch; not bypassed.
- services.google.com/.../gemini-for-google-workspace-prompting-guide-101.pdf: 404.

1. INGREDIENTS OF A GOOD PROMPT: PARTLY. No vendor uses your exact four; every element is supported somewhere.

(a) OpenAI Academy, "Prompting", https://academy.openai.com/public/clubs/work-users-ynjqu/resources/prompting. Exists, public, "August 6, 2025 · Last updated on September 4, 2026". Workplace-oriented. It lists three steps [V]:
- "Outline the task": "Be clear about what you need ChatGPT to do. Outline what you want, who it’s for, and why it matters."
- "Give helpful context": "Add any background (or documentation) that will help."
- "Describe your ideal output": "specifying role, audience, or format produces the most accurate and relevant results."
- Tip, "Guide the tone and format": "Tell ChatGPT how you want the response to sound and look."

(a2) OpenAI, "ChatGPT at home" parent guide, https://cdn.openai.com/pdf/chatgpt-at-home.pdf (PDF metadata May 2026; framed for parents of teens) [V-img]:
- "A strong prompt usually includes three parts:" Task "What do you want ChatGPT to do?" / Context "What should it know about your child, schedule, audience, or constraints?" / Output "What should the answer look like: a list, table, text message, plan, script, or checklist?"

(b) OpenAI Help Center, "Prompt engineering best practices for ChatGPT", https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt ("Updated: 2 months ago") [T]:
- Sub-headings: "Be clear and specific", "Iterative refinement", "Requesting a different tone".
- "Ensure your prompts are clear, specific, and provide enough context for the model to understand what you are asking."

(c) Anthropic, "Prompting best practices", https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (docs.anthropic.com/en/docs/be-clear-direct redirects here; no date; developer docs) [V]:
- Headings: "Be clear and direct", "Add context to improve performance", "Use examples effectively", "Structure prompts with XML tags", "Give Claude a role".
- "Be specific about the desired output format and constraints."
- "The more precisely you explain what you want, the better the result."

(d) Google Workspace, "How to write effective prompts", https://workspace.google.com/resources/ai/writing-effective-prompts/ (no date) [V]:
- "The four main areas to consider when writing an effective prompt are: Persona / Task / Context / Format"
- "You don’t need to use all four in every prompt, but using a few will help!"
- Google's "Tips to write prompts for Gemini", https://support.google.com/a/users/answer/14200040?hl=en (no date) [V], lists: "Use natural language", "Be clear and concise", "Provide context", "Use specific and relevant keywords", "Break down complex tasks into separate prompts".

(e) Microsoft Support, "Get started writing prompts in Microsoft Copilot", https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-writing-prompts-in-microsoft-365-copilot (the older "Learn about Copilot prompts" URL redirects here; "Last updated: September 2026") [V]:
- "Prompts can include four parts: Goal: What do you want Copilot to do? Context: Why do you need it, and who is involved? Source: What information or samples should Copilot use? … Expectations: How should Copilot respond?"
- "all that's required is a clear goal."

Mapping:
- 任務 = Task (OpenAI, Google) / Goal (Microsoft).
- 背景 = Context (all).
- 格式 = Output (OpenAI) / Format (Google) / Expectations (Microsoft).
- 限制 is not a separate named part in any vendor list. It appears only inside Anthropic's "format and constraints" and OpenAI's Context row ("audience, or constraints").
- Persona/role (Google, Anthropic) and Source (Microsoft) are left out of your four.

2. ITERATE: SUPPORTED.
- OpenAI Academy [V]: "if the first answer isn’t quite right, clarify or adjust mid-conversation rather than starting over."
- Google [V]: "Use follow-up prompts and an iterative process of review and refinement to yield better results."
- Microsoft [V]: "Expect some back-and-forth conversation to get the results you're looking for."
- ChatGPT at home [V-img]: "Ask ChatGPT for a first draft, then improve it with one follow-up question."

3. EXAMPLES HELP: SUPPORTED, mainly by Anthropic.
- Anthropic [V]: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure."
- Microsoft's "Source" part mentions "samples" [V].
- Not found on the OpenAI Academy page or [T] the OpenAI Help article.

4. AUDIENCE / READING LEVEL: SUPPORTED.
- ChatGPT at home [V-img]: "Write this in a way a 10-year-old can understand."; "Help me explain fractions to my 8-year-old, with 3 simple examples."; "Adding detail, like your children’s ages or grade level, food preferences, interests, or daily schedule, can help you get more useful, relevant answers."
- OpenAI Academy [V]: "who it’s for"; "role, audience, or format".
- Microsoft example [V]: "Our audience is professionals who work in a hybrid environment…"
- No vendor page says "9-year-old"; use 8 or 10, or your own wording.

5. 教育部「中小學使用『生成式人工智慧』注意事項2.1（學生版）」: SUPPORTED [V].
Header: 「中華民國115年2月11日臺教資（一）字第1152700391號函核定」. Source: https://jr.hs.ntnu.edu.tw/wp-content/uploads/2026/02/中小學使用「生成式人工智慧」注意事項2.1.pdf (14 pages, both versions). I found no MOE-hosted student copy. Authenticity checks: the teacher half is text-identical to the MOE-site copy (https://eliteracy.edu.tw/Upload/pdfs/附件1-中小學使用生成式人工智慧注意事項2.1_教師_行政人員及家長版_F1150211-.pdf), and the student half is text-identical to https://www.mqjh.tp.edu.tw/uploads/1772592666207cLTEZbtn.pdf.

(i) 六（三）「不可以將自己或他人的姓名、照片、聯絡方式、住址、學號等個人資料，或家庭、學校的機密資訊輸入至「生成式人工智慧」工具。」
(ii) 二「不能全盤接受生成的內容，而需結合其他可靠來源的知識和批判性思維進行查證」; 一「遇有疑慮應向老師或家長詢問，不宜直接採信或用於作業、報告或公開發表的內容。」
(iii) 六（四）「完成作業或報告時，如依老師或學校規定使用「生成式人工智慧」工具協助構思或潤飾，應依規定註明所使用的工具及用途，不得將生成內容直接當作自己原創作品繳交。」
(iv) 五「中小學學生使用「生成式人工智慧」工具應遵守各平臺註冊年齡限制及相關規範。」「在校應於教師引導或指導下使用，若為非在校使用，亦請家長陪伴使用。」 Appendix 五:「若需使用其他商用版的「生成式人工智慧」工具（如ChatGPT、Gemini等），應經由學校評估資安風險，並在師長指導下審慎使用。」 It states no age number.
(v) Nothing on how to ask. 六（一）「應先自行閱讀與思考，再視需要使用工具輔助。」 is the nearest.

MOE's word for "prompt": 「提示詞」 appears zero times in all four MOE documents I searched.
- 注意事項 2.1 has no term for it (it uses 輸入, 詢問).
- 教育部《中小學數位教學指引3.0版》(cover 2025年1月; school-hosted copy https://www2.chjhs.tyc.edu.tw/gov/教育部中小學數位教學指引3.0版1140113.pdf) uses 「提示 (Prompt)」 and 「提問」. Its 7-2(4) [V]: 「練習提問：要知道生成式 AI 產生的內容是無法預測的，同樣的提示（Prompt）可能會有不同的結果，因此要學習將問題切分為一系列的小問題，一步步提問與解決問題，並辨認提供內容的正確與適切性，直到獲得最後的結果。」 and (5) 「靈活調整：…如果生成的答案或方向不如預期，要保持彈性思維並能夠調整方向。」
- So 「提示詞」 is common usage, not MOE's term; consider "提示詞（教育部文件寫作「提示（Prompt）」或「提問」）".

6. CHILD-ORIENTED RESOURCES: PARTLY.
- 教育部 eliteracy 手冊《你不可不知的生成式AI 國小高年級學生版》, listed at https://eliteracy.edu.tw/Handbooks.aspx (PDF metadata Sept 2024; old isafeevent.moe.edu.tw URL is 404) [V]: 「生成式AI生成文章時，通常都是從「提問(prompt)」開始，而問對問題就是成功的一半，生成式AI的產出的品質有賴於正確的提問。」 It repeats the 練習提問 / 靈活調整 / 保護隱私 items.
- 《AI與我們的生活 國小中年級學生版》, same listing page [V]: 「如果人類給予錯誤的要求，那麼生成式AI工具也無法生成出人類想要的內容。…所以生成式AI所生成的內容也無法確保正確性。」
- Google Be Internet Awesome, "Understanding AI: Foundational AI literacy for Grades 2nd-8th", June 2025, https://services.google.com/fh/files/misc/bia_ai-literacy-guide_en.pdf [V]: "When you order a cake, a baker needs to know what kind of cake you want, right? … Prompts are the words you type or say to tell AI what to do." It also says the lessons prioritise understanding "rather than instructing elementary and middle school students on how to use AI tools directly", and "Always use AI with a trusted grown-up".
- Google "Family Guide to AI" (© 2025), https://services.google.com/fh/files/misc/family-guide-to-ai.pdf [V]: "You should always double-check if what AI tells you is right."; "Never enter private information, such as your phone number or home address, into AI." No prompt-writing content.
- Computing at School, "Prompt Engineering for Young Learners: The CRAFT Framework" (ages 8-13; last edit 05 June 2026), https://www.computingatschool.org.uk/resources/2026/may/prompt-engineering-for-young-learners-the-craft-framework/ [V, description only]: "The CRAFT framework (Context, Role, Action, Format, Tone)". Download is behind login, and it is a community upload by "ForeShiloh Education", not an official standard.
- Common Sense "AI Literacy Lessons for Grades K–12" (https://www.commonsense.org/education/collections/ai-literacy-lessons-for-grades-k-12) [V]: K–5 titles are media literacy; no prompt-writing lesson.
- Code.org "Exploring Generative AI" mentions "prompt engineering" [V]; grade band not confirmed.
- Day of AI, Oak (only KS4 hits), UNICEF: nothing usable found.

7. AGES (father operates his own account): SUPPORTED.
- OpenAI Terms of Use, "Effective: January 1, 2026", https://openai.com/policies/row-terms-of-use/ (same text at /policies/terms-of-use/) [T]: "You must be at least 13 years old or the minimum age required in your country to consent to use the Services." "If you are under 18 you must have your parent or legal guardian’s permission to use the Services."
- OpenAI Help, "Is ChatGPT safe for all ages?", https://help.openai.com/en/articles/8313401-is-chatgpt-safe-for-all-ages ("Updated: last month") [T, fragments]: "ChatGPT is not meant for children under 13"; for under-13s in education "the actual interaction with ChatGPT must be conducted by an adult."
- Anthropic Consumer Terms, "Effective October 8, 2025", https://www.anthropic.com/legal/consumer-terms [V]: "You must be at least 18 years old or the minimum age required to consent to use the Services in your location, whichever is higher."
- Claude Help, "Age assurance on Claude", May 18, 2026, https://support.claude.com/en/articles/15171100-age-assurance-on-claude [V]: "Claude, our consumer product, is only available to people over 18 years." zh-TW page: 「我們的消費者產品 Claude 僅供 18 歲及以上的人士使用。」
- Google, "What you need to sign in to Gemini Apps", https://support.google.com/gemini/answer/13278668?hl=en (no date) [V]: "You must be 13 (or the applicable age in your country) or over to use Gemini with a personal or school Google Account and 18 or over to use Gemini with a work account."
- Google account ages, https://support.google.com/accounts/answer/1350409?hl=en [V]: "For all countries not listed below, 13 is the minimum age". Taiwan is not listed (Asia: South Korea 14+, Vietnam 15+), so 13 for Taiwan is my inference from the list.
- Google Family Link, https://support.google.com/gemini/answer/16109150?hl=en [V]: "A parent must enable access before their child under 13 … can use Gemini Apps with a supervised account." The sign-in page above contradicts this for the web app: "You still can’t access the Gemini web app with a Google Account managed by Family Link." Avoid specifics about child accounts.
- Microsoft Copilot Terms of Use, "Effective: August 18, 2026", https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse [V]: "you need to be old enough at least 13, but sometimes older, depending on your country’s laws."
- Taiwan-specific: no vendor page mentions Taiwan; only the MOE text in 5(iv).

8. OUTPUTS CAN BE WRONG: SUPPORTED.
- Anthropic terms [V]: "Outputs may not always be accurate and may contain material inaccuracies even if they appear accurate because of their level of detail or specificity."
- Microsoft terms [V]: "Copilot tries to give you good answers, but it can make mistakes."
- Google, https://support.google.com/gemini/answer/13954172 [V]: "Because generative AI is experimental and a work in progress, it can and will make mistakes".
- OpenAI terms [T]: "Output may not always be accurate."

9. "BETTER PROMPT GUARANTEES A CORRECT ANSWER": NOT FOUND anywhere. The guidance says the opposite.
- OpenAI Academy [V]: "There’s no single “perfect” way to prompt." The strongest positive wording is "A good prompt helps the model understand what you need" (helps, not guarantees).
- Google [V]: "prompts can sometimes have unpredictable responses."
- Microsoft [V]: "Using the same prompt multiple times can result in different responses."
- Anthropic, "Reduce hallucinations", https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations [V]: "while these techniques significantly reduce hallucinations, they don't eliminate them entirely."
- MOE: see the 練習提問 quote in 5.

DO NOT SAY
- That 任務／背景／限制／格式 is an official or standard formula of OpenAI, Google, Microsoft, Anthropic or 教育部. Say it is this lesson's simplification.
- That 「提示詞」 is the 教育部 term.
- That a good prompt makes the answer correct, or that vendors promise accuracy.
- That the child may open an account. Claude is 18+; ChatGPT, Gemini and Copilot are 13+ with conditions.
- That Family Link lets a Taiwanese child use Gemini (Google's pages conflict; Taiwan availability unverified).
- That MOE 2.1 gives an age number, or teaches how to write prompts.
- "Explain to a 9-year-old" as a vendor quote.
- CRAFT or any other acronym framework as authoritative.
- Exact wording from OpenAI Help Center or Terms as checked verbatim; those are [T] only.
