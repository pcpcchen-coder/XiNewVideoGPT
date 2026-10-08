# L013 來源查核筆記（研究代理回報）

2026-10-08 由製作代理派出的研究子代理蒐集。子代理下載原始頁面後抽取文字並回報引文；它自己標示了哪些是逐字讀到的、
哪些只是擷取工具的摘要。主代理沒有逐頁重讀，只用這份筆記對照旁白、投影片與教材。以下為回報原文。

---

L013 SOURCE VERIFICATION (checked 2026-10-08)

Nine of the eleven claims are supported; claims 4 and 10 are only partly supported. Four things in the brief need correcting before scripting: the Apple menu names, the FTC "code word", the Personal Voice language, and the YouTube narrator-voice question.

[V] = read in raw HTML/PDF text I downloaded. [T] = WebFetch extraction only, not independently checked.

Could not be read directly:
- openai.com and help.openai.com (403), adobe.com and helpx.adobe.com (403), cib.npa.gov.tw (connection reset): WebFetch only, marked [T].
- isafeevent.moe.edu.tw Deepfake handbooks: 404.
- topic.tipo.gov.tw: 502; I used www.tipo.gov.tw instead.
- 165.npa.gov.tw / 165dashboard.tw: not read.

CORRECTIONS TO THE BRIEF
- Apple's Taiwan pages do not say 「朗讀內容」 or 「個人語音」. They say 「閱讀與朗讀」 (macOS 26/27), 「語音內容」 (macOS 15) and 「個人聲音」.
- The FTC alert does not advise a family code word; that appears only in reader comments on the page. The code-word advice comes from the FBI and Taiwan police.
- Personal Voice does not support Taiwanese Mandarin.
- YouTube's page is now titled "Disclosing use of GenAI content".

1. Generative AI makes text, images, audio — SUPPORTED
- UNICEF, "Guidance on AI and Children 3.0", December 2025, p.6. https://www.unicef.org/innocenti/media/11991/file/UNICEF-Innocenti-Guidance-on-AI-and-Children-3-2025.pdf [V]: "instead of only recognizing and processing data, they can also generate new content by using statistical patterns to predict what comes next in language, images and other media." Also p.5 [V]: "Today, generative AI systems create the videos, news and music."
- Microsoft Learn, "What is generative AI?" (ms.date 2025-03-24). https://learn.microsoft.com/en-us/training/modules/intro-generative-ai-explore-basics/2-what-is-generative-ai [V]: "Generative AI is a term for AI systems that recognize patterns in significant and complex data sets to generate original text, voice, and images based on these patterns."
- Microsoft AI 101, "How Does Generative AI Work" (no date). https://www.microsoft.com/en-us/ai/ai-101/how-does-generative-ai-work [V]: "Image creation. Models such as DALL-E can generate unique images from text prompts"; "They can also generate realistic voiceovers and speech synthesis for use in audiobooks, virtual assistants, and video games."
- Google and OpenAI: no clean one-line definition captured.

2. Image-generation limits in vendors' words — SUPPORTED
- OpenAI API docs, Image generation guide, "Limitations" (no date). https://developers.openai.com/api/docs/guides/image-generation [V]: "Text Rendering: Although significantly improved, the model can still struggle with precise text placement and clarity." / "Consistency: … the model may occasionally struggle to maintain visual consistency for recurring characters or brand elements across multiple generations." / "Composition Control: … the model may have difficulty placing elements precisely in structured or layout-sensitive compositions."
- Google Cloud, "Gemini image generation limitations" (last updated 2026-10-07). https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/gemini-image-generation-limitations [V]: "The model might not create the exact number of images you ask for."
- Google blog, "Gemini image generation got it wrong. We'll do better." (Feb 23, 2024). https://blog.google/products-and-platforms/products/gemini/gemini-image-generation-issue/ [V]: "Some of the images generated are inaccurate or even offensive." / "It will make mistakes."
- Adobe Generative AI User Guidelines (last updated May 15, 2026). https://www.adobe.com/legal/licenses-terms/adobe-gen-ai-user-guidelines.html [T]: "Outputs from generative AI features may be inaccurate, misleading, …" / "Please use your judgment when reviewing and validating generated outputs."
- Canva AI Product Terms (effective 26 June 2026). https://www.canva.com/policies/ai-product-terms/ [T]: "Canva has not verified the accuracy of the Output and it does not represent Canva's views."
- Limit: Google's Gemini help now advertises "Better text rendering", so say text in pictures "can still go wrong", not "always garbled".

3. Text-to-speech and the narrator voice — SUPPORTED
- Microsoft Learn, "What is text to speech?" (ms.date 2026-01-30). https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech [V]: "Text to speech enables your applications, tools, or devices to convert text into human like synthesized speech. The text to speech capability is also known as speech synthesis." / "Text to speech uses deep neural networks to make computer voices nearly indistinguishable from human recordings."
- Microsoft Learn, "Language and voice support for the Speech service" (ms.date 2026-09-09), table "Text to speech voices". https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts [V]. Row: zh-TW | Chinese (Taiwanese Mandarin, Traditional) | Standard | zh-TW-YunJheNeural (Male) | (Style/Roles blank) | Voice conversion ❌. Same page: "Standard voices: High-quality neural voices available out of the box".
- So YunJhe is a prebuilt standard neural voice, not a clone of a specific person the user supplied.
- Not verified: that Edge TTS serves this voice. The page documents Azure Speech only.
- Cloning contrast, Microsoft Learn "personal voice" overview (ms.date 2026-09-09). https://learn.microsoft.com/en-us/azure/ai-services/speech-service/personal-voice-overview [V]: "With personal voice, you can enable your users to get AI generated replication of their own voices in a few seconds."

4. Voice-clone scams — PARTLY
- FTC Consumer Alert, "Scammers use AI to enhance their family emergency schemes", Alvaro Puig, March 20, 2023. https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes [V]: "A scammer could use AI to clone the voice of your loved one. All he needs is a short audio clip of your family member's voice — which he could get from content posted online — and a voice-cloning program." / "Don’t trust the voice. Call the person who supposedly contacted you and verify the story. Use a phone number you know is theirs."
- FBI IC3 PSA I-120324-PSA, December 3, 2024. https://www.ic3.gov/PSA/2024/PSA241203 [V]: "Criminals generate short audio clips containing a loved one's voice to impersonate a close relative in a crisis situation, asking for immediate financial assistance or demanding a ransom." / "Create a secret word or phrase with your family to verify their identity." / "Verify the identity of the person calling you by hanging up the phone, researching the contact of the bank or organization purporting to call you, and call the phone number directly."
- Taiwan, 內政部警政署花蓮港務警察總隊 反詐騙宣導 open data, reposting CIB 刑事警察局 videos. https://www.hlhpd.npa.gov.tw/ch/app/openData/data/list?module=publicizearea&mserno=105480c9-65f8-41bd-ae8d-17f9507da67f&type=xml [V]
  - 114-07-02 item: 「近期，詐騙集團利用人工智慧AI技術，模擬親友的聲音，製造緊急情境，誘使受害者匯款。」「如何防範AI語音詐騙 1.設定家庭密語 2.保持冷靜，勿急於匯款 3.避免公開分享聲音資料」
  - 114-12-10 item: 「聲音、影像都能被偽造，大家一定要提高警覺！」「先用另一個你確定的聯絡方式（電話、面對面）去確認，不要只信影片或語音，可撥打165反詐騙專線求證。」
- 刑事警察局, 常見詐騙手法話術解析—第五章 猜猜我是誰 (meta 2023-03-09). https://www.cib.npa.gov.tw/ch/app/data/view?module=wg116&id=1909&serno=4f04dab6-3ca5-4139-a94e-66be03b62ba3 [T]: 「可與親友約定專屬密語，做為懷疑對方身分時的確認。」 The page does not mention AI.
- 內政部, 「通話中直接撥打165?小心詐騙集團假冒警察」. https://www.moi.gov.tw/News_Content.aspx?n=2&s=323333 [V]: 「遵循「一聽、二掛、三查證」原則，必「先掛斷電話，後查證」」. This is general advice, not AI-specific.
- Limit: no CIB or 165 press release stating a clip length was read. The "short clip" claim rests on the FTC and FBI only.

5. "Seeing is not believing", child-oriented — SUPPORTED
- 教育部 注意事項2.1 學生版 第三點 (source in 6c) [V]: 「這項技術能利用既有的圖片、影像或聲音素材，製造出看似真實的影片和圖像，甚至假新聞。」「不要輕易相信未經審核的影片或照片」
- Same document, 示例 [V]: 「被深偽技術整合他們的臉（聲音）到假圖片或假影片中」
- UNICEF 3.0 p.17 [V]: "AI can be used to instantly and at low cost create content that can be indistinguishable from human-generated content" / "a range of scams, such as synthetic voice scams that impersonate relatives requesting money."

6. Labelling
(a) YouTube Help, "Disclosing use of GenAI content" (no date; ©2026). https://support.google.com/youtube/answer/14328491?hl=en [V] — SUPPORTED
- Must disclose: "we require creators to disclose when they use AI to meaningfully alter or generate photorealistic content." It lists content that "Makes a real person appear to say or do something they didn’t do. / Alters footage of a real event or place. / Generates a realistic scene that didn’t actually occur. / Creates music that’s the main focus of the video."
- Need not disclose: "Creators don’t need to disclose non-realistic content that’s made with AI, or edits to realistic content that are minor." Examples: "Production assistance, like using generative AI tools to create or improve a video outline, script, thumbnail, title, or infographic", "Caption creation", "Cloning one’s own voice to create voice overs or dubs", "Using an AI-generated or altered animation … in a fully animated video".
- Synthetic narrator voice: a stock TTS narrator is not named in either list. It is not a real person's voice, so it does not fall under the first trigger. Say "the page does not list it as requiring disclosure", not "YouTube exempts it".
- Also: "YouTube may automatically apply an AI label…" for "Content that contains C2PA metadata".
(b) SynthID and C2PA — SUPPORTED
- Google DeepMind, "Google SynthID" (no date). https://deepmind.google/models/synthid/ [V]: "SynthID embeds digital watermarks directly into AI-generated images, audio, text or video. The watermarks are … imperceptible to humans – but can be detected by SynthID's technology."
- C2PA (no date). https://c2pa.org/ [V]: "Content Credentials function like a nutrition label for digital content, giving a peek at the content’s history".
(c) 教育部「中小學使用「生成式人工智慧」注意事項2.1」 — SUPPORTED
- Header [V]: 「中華民國115年2月11日臺教資（一）字第1152700391號函核定」.
- 學生版 was read from a school mirror: https://jr.hs.ntnu.edu.tw/wp-content/uploads/2026/02/中小學使用「生成式人工智慧」注意事項2.1.pdf. The official host has the 教師、行政人員及家長版, which matches the mirror: https://eliteracy.edu.tw/Upload/pdfs/附件1-中小學使用生成式人工智慧注意事項2.1_教師_行政人員及家長版_F1150211-.pdf. I did not find the 學生版 on an official host.
- 學生版 六（三）[V]: 「不可以將自己或他人的姓名、照片、聯絡方式、住址、學號等個人資料，或家庭、學校的機密資訊輸入至「生成式人工智慧」工具。」
- 六（四）[V]: 「應依規定註明所使用的工具及用途，不得將生成內容直接當作自己原創作品繳交。」
- 第五點 [V]: 「應遵守各平臺註冊年齡限制及相關規範。」「若為非在校使用，亦請家長陪伴使用。」
- 教師家長版 六 [V]: 「正確標示生成內容的來源」
(d) 人工智慧基本法, 115年1月14日 華總一義字第11500001671號. https://www.president.gov.tw/File/Doc/80165b6d-cb49-4b49-952f-56e1e6abe51b [V] — SUPPORTED as a principle only
- 第4條第5款: 「透明與可解釋：人工智慧之產出應做適當資訊揭露或標記，以利評估可能風險」
- 第5條第2項: 「政府應以兒少最佳利益為原則，人工智慧產品或系統經…認定為高風險應用者，應明確標示注意事項或警語。」
- Limit: these are principles the government follows when promoting AI. They are not a labelling duty on individuals and carry no penalty.

7. Consent and real people — SUPPORTED
- OpenAI Usage policies (effective October 29, 2025). https://openai.com/policies/usage-policies/ [T]: "use of someone's likeness, including their photorealistic image or voice, without their consent".
- Google Generative AI Prohibited Use Policy (last modified December 17, 2024). https://policies.google.com/terms/generative-ai/use-policy [V]: "Impersonating an individual (living or dead) without explicit disclosure, in order to deceive."
- ElevenLabs Prohibited Use Policy (last updated 17 August 2026). https://elevenlabs.io/use-policy [V]: "creating or using ElevenLabs audio output to intentionally replicate the voice of another person: a) without consent or legal right…; c) in a manner intended to deceive others about whether the voice was generated by artificial intelligence."
- Microsoft personal voice (URL in 3) [V]: "it's required that every voice be created with explicit consent from the user. A recorded statement from the user is required".

8. Copyright (TIPO primary) — SUPPORTED
- 智慧財產局 電子郵件1140522c, 令函日期 114-05-22. https://www.tipo.gov.tw/tw/copyright/692-34252.html [V]: 「故AI生成之圖畫是否享有著作權，應視創作過程中有無人類實際的創意投入而定」「若創作過程中完全是由AI的演算功能獨立進行完成，並無人類精神文明之投入，則該AI生成的圖畫無法享有著作權。」「如AI生成圖畫與用於AI訓練資料中之原始著作有構成實質近似之情境…可能會…有侵權之問題。」
- 智著字第11460005900號, 114-04-01. https://www.tipo.gov.tw/tw/copyright/692-33518.html [V]: 「人工智慧獨立創作」…「原則上無法享有著作權。」
- Using others' works: 電子郵件1150624, 115-06-24. https://www.tipo.gov.tw/tw/copyright/692-87797.html [V]: 「復刻、微調或致敬…可能構成重製、改作等著作利用行為…原則上應取得著作財產權人之同意或授權」. That case concerns a workbook design, not AI.
- Every letter ends by saying disputes are decided case by case by the courts.

9. Apple, support.apple.com/zh-tw (no dates shown; default version now "macOS 27 Golden Gate") — SUPPORTED with wording corrections
(a) 「讓 Mac 朗讀螢幕上的文字」. https://support.apple.com/zh-tw/guide/mac-help/mh27448/mac [V]
- macOS 26 and 27: 「選擇「蘋果」選單 >「系統設定」，然後按一下側邊欄中的「輔助使用」。」→「按一下「閱讀與朗讀」。」→「開啟「朗讀所選範圍」。」「預設按鍵組合是 Option + Esc」
- macOS Sequoia 15 (…/mh27448/15.0/mac/15.0) [V]: the middle step is 「按一下「語音內容」。」
- All versions: 「選擇「編輯」>「語音」>「開始朗讀」。」
(b) 「在 Mac 上製作「個人聲音」」. https://support.apple.com/zh-tw/guide/mac-help/mchldfd72333/mac [V]
- 「若你有失去說話能力的風險，可以使用 Mac 上的「個人聲音」來製作聽起來像你的合成聲音」
- 「「個人聲音」只適用於配備 Apple 晶片的 Mac 電腦，而且只適用於英文（美國）、國語（中國大陸）和西班牙文（墨西哥）。」
- 「你只能使用「個人聲音」來在裝置上製作聽起來像你本人的聲音、使用你本人的聲音，且只能由本人用於非商業用途。」
- 「你必須設定登入密碼」
(c) Image Playground
- Apple 台灣 Newsroom, 2025年11月4日. https://www.apple.com/tw/newsroom/2025/11/apple-intelligence-features-are-now-available-in-traditional-chinese/ [V]: 「Apple Intelligence 現已支援繁體中文等八種新語言」
- 「macOS Golden Gate – 功能特色適用範圍」. https://www.apple.com/tw/macos/feature-availability/ [V]: 影像樂園 lists 「中文 (繁體)」. Requirement: 「配備 M1 與更新的晶片的 Mac 機型」, 「部分功能可能未在所有地區提供」.
- 「在 Mac 上使用「影像樂園」製作獨創影像」. https://support.apple.com/zh-tw/guide/mac-help/mchld5412d00/mac [V]: 「你可以在「螢幕使用時間」設定中阻擋取用「影像樂園」等影像製作功能。…「寫實影像」的建議使用年齡為 18 歲以上。」
- Limit: the pages list the language "繁體中文"; none says "available in Taiwan" in those words.

10. Ages — PARTLY
- OpenAI Terms of Use (effective January 1, 2026). https://openai.com/policies/terms-of-use/ [T]: "You must be at least 13 years old or the minimum age required in your country to consent to use the Services." / "If you are under 18 you must have your parent or legal guardian’s permission to use the Services."
- Gemini Apps Help, "Generate & edit images with Gemini Apps". https://support.google.com/gemini/answer/14286560?hl=en [V]: "To generate and edit images, you must be 18 or over" / "To generate images, you must be 13 (or the applicable age in your country) or over." / "Editing images isn't available to users under 18."
- Gemini Apps Help, "Guide your child's Gemini Apps experience". https://support.google.com/gemini/answer/16109150?hl=en [V]: "A parent must enable access before their child under 13 (or the applicable age in your country) can use Gemini Apps with a supervised account."
- Microsoft Support, "Microsoft Copilot for Young People". https://support.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-young-people [V]: "You must be at least 13 years old to use Copilot, and in some countries, the minimum age may be higher". The page itself warns it applies only to the app version before August 18, 2026.
- Canva Terms of Use (effective 19 August 2026). https://www.canva.com/policies/terms-of-use/ [T]: "Children may not access or use the Service, other than through Canva Education." / "a child is a person under the age of 13".
- Adobe Firefly: age not verified. Only the 2023 Generative AI Additional Terms were read [V]; they set 18+ for Acrobat text-to-text only.
- ElevenLabs (URL in 7) [V]: no one under 13, and no one aged 13–18 "without first obtaining parental or guardian consent".

11. Bias — SUPPORTED
- OpenAI, "DALL·E 3 System Card", October 3, 2023. https://cdn.openai.com/papers/DALL_E_3_System_Card.pdf [V]: "DALL·E 3 has the potential to reinforce stereotypes" / "By default, DALL·E 3 produces images that tend to disproportionately represent individuals who appear White, female, and youthful… We additionally see a tendency toward taking a Western point-of-view more generally."
- UNICEF 3.0 [V]: "While many AI systems indicate that their outputs may be inaccurate or biased, such systems need to be more explicit and transparent about this risk".
- 教育部 2.1 學生版 第二點 [V]: 「留意其中是否涉及文化刻板印象或不公平的描述」

DO NOT SAY
- That the FTC recommends a family code word (FBI and Taiwan police do).
- That a few seconds of audio is enough to clone a voice, stated as official Taiwan police fact.
- That watermarks, SynthID or Content Credentials make fakes always detectable. Canva's terms even prohibit stripping the tags, which implies they can be removed.
- That YouTube exempts TTS narration, or that the series must tick "AI use: Yes". Neither is stated.
- That 人工智慧基本法 requires individuals to label AI content.
- 「朗讀內容」 or 「個人語音」 as Mac menu names.
- That the child can make a Personal Voice in Taiwanese Mandarin; it also must be the user's own voice.
- That Image Playground is "available in Taiwan"; say it supports Traditional Chinese on M1-or-later Macs, with some features region-limited.
- That children may open their own accounts (13+ floors, Gemini image editing 18+, under-13 only through parent-enabled supervision), or any Adobe Firefly age.
- That AI pictures always get text wrong, or that AI-made work is never copyrightable. TIPO says it depends on human creative input, decided case by case.
- That zh-TW-YunJheNeural is a real person's cloned voice, or that Microsoft documents Edge TTS serving it.
