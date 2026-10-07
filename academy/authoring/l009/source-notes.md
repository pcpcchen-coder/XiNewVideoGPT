# L009 來源查核筆記（研究代理回報）

2026-10-07 由製作代理派出的研究子代理蒐集。子代理下載原始頁面後抽取文字並回報引文；它自己標示了哪些是逐字讀到的、
哪些只是擷取工具的摘要。主代理沒有逐頁重讀，只用這份筆記對照旁白、投影片與教材。以下為回報原文。

---

SOURCE CHECK: personal info / photo metadata / audience / digital footprint (fetched 2026-10-07)

Method note: WebFetch returns a small-model summary, so wherever possible I downloaded the raw HTML/PDF and extracted text myself. [RAW] = verbatim from raw page text. [TOOL] = WebFetch extraction only, not verbatim-guaranteed. law.moj.gov.tw could NOT be fetched (robots.txt disallows all automated access; not bypassed). eteacher.edu.tw could not be fetched (proxy 502).

1. Personal information: SUPPORTED
- 個人資料保護法 第2條, 臺北市法規查詢系統 (official mirror; header 修正日期 民國114年11月11日; Art. 2 is not among the articles amended then). https://laws.gov.taipei/law/LawSearch/LawArticleContent/FL010627 [RAW]
 「一、個人資料：指自然人之姓名、出生年月日、國民身分證統一編號、護照號碼、特徵、指紋、婚姻、家庭、教育、職業、病歷、醫療、基因、性生活、健康檢查、犯罪前科、聯絡方式、財務情況、社會活動及其他得以直接或間接方式識別該個人之資料。」
 Limit: does not literally name 照片, 住址 or 學校; they fall under 「其他得以直接或間接方式識別」.
- FTC, "Complying with COPPA: Frequently Asked Questions", A.3. https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions [RAW]
 "The Rule defines personal information to include: First and last name; A home or other physical address including street name and name of a city or town; Online contact information; A screen or user name that functions as online contact information; A telephone number; A Social Security number; A persistent identifier…; A photograph, video, or audio file, where such file contains a child's image or voice; Geolocation information sufficient to identify street name and name of a city or town; …"
 Limit: page banner says "The COPPA Rule was amended on April 22, 2025. Review the revised Rule…", so the list may be incomplete. It binds US operators, not children.

2. Photos carry hidden metadata: SUPPORTED
- Apple 個人安全使用手冊「管理「照片」中的位置後設資料」, 發佈日期：2026 年 9 月. https://support.apple.com/zh-tw/guide/personal-safety/ips0d7a5df82/web [RAW]
 「已為「相機」App 開啟「定位服務」時，會使用從行動網路、Wi-Fi、GPS 網路和藍牙收集的資訊來判斷照片和影片的拍攝位置座標。此座標會嵌入每個照片和影片檔中」
 「分享包含位置後設資料的照片和影片時，你分享照片和影片的對象可以取用該位置後設資料並得知其拍攝的位置。」
- iPhone 使用手冊 (iOS 27)「在 iPhone 上分享照片和影片」. https://support.apple.com/zh-tw/guide/iphone/iphf28f17237/27/ios/27 [RAW]
 「注意： 分享照片或影片會同時分享其相關聯的後設資料，例如日期與時間、位置、裝置和說明。」
 Limit: location is embedded only when 定位服務 is on for 相機, so not every photo has it.

3. Share without location: SUPPORTED, with a version caveat
- iPhone, same Personal Safety page [RAW]: 「點一下 [分享圖示]，然後點一下「選項」。」「關閉「位置」。」「「未包含位置」會顯示在「選項」按鈕上方。」 To stop collection: 「前往「設定」>「隱私權與安全性」>「定位服務」>「相機」，然後點一下「永不」。」
- iPhone 使用手冊, iOS 18 and iOS 26 pages (…/iphf28f17237/18.0/ios/18.0 and …/26/ios/26) [RAW]: 「打開照片或影片，點一下 [分享圖示]，點一下「選項」，然後執行下列任一項操作：關閉位置資料：關閉「位置」。」
 Caveat: the iOS 27 version of that page lists only 「不分享關鍵字：關閉關鍵字」, 檔案格式 and 「所有照片資料」 under 「選項」; the 位置 line is absent. The September 2026 Personal Safety page still documents it. Check on the actual device before filming.
- Mac,「Mac 上的「照片」設定」(macOS 27; same wording for 26 and 15). https://support.apple.com/zh-tw/guide/photos/pht5156cc968/mac [RAW]
 「請選擇「照片」>「設定」，然後按一下設定視窗最上方的「一般」」; under 共享: 「包含位置資訊：分享或輸出照片時包含由具備 GPS 功能的相機（如 iPhone）拍攝之照片中內嵌的位置資訊。」
 Per-photo removal (Personal Safety page): 「選擇「影像」>「位置」，然後選擇「隱藏位置」」.
 Limit: Apple does not state the default on/off state, and the Mac export page mentions no location checkbox.

4. Background reveals information: PARTLY SUPPORTED
- ThinkUKnow (AFP-led), "Home learning activity: Learning about personal information and image sharing", ages 8–12, PDF undated (2020-10 in URL). https://www.thinkuknow.org.au/sites/default/files/2020-10/Home%20learning%20activity%20Learning%20about%20personal%20information%20and%20image%20sharing.pdf [RAW]
 "Images in school uniform, at school, or even out the front of a home can all contain personal information about a child and their location." Activity answers: "The logo on his school uniform, his first name written on the soccer ball, a sign in the background which says where he is."
- ThinkUKnow, "Parental advice for posting images" (2023-01 in URL). https://www.thinkuknow.org.au/sites/default/files/2023-01/ThinkUKnow%20parental%20advice%20for%20posting%20images.pdf [RAW]
 "Check the background for identifying information (like public signs, street signs, house numbers)"; "If your child is wearing a uniform; consider blurring the school logo or covering with an emoji".
- 教育部 中小學數位素養教育資源網,【安全自拍與分享】學習單 (lesson plan is 國中). https://eliteracy.edu.tw/Download.ashx?id=1506 [RAW]
 「上傳前確認照片背景沒有個人資訊（如地址、學校名稱）」; listed as 危險行為: 「上傳穿著校服或制服的清晰個人照」.
- Same site,【躲在角落的眼睛】教案 (國小三至四年級). https://eliteracy.edu.tw/Download.ashx?id=1782 [RAW]
 「❌「今天我們去美美公園校外教學，我們全班穿著學校運動服，老師還說下週五也要去！」（附上班上同學合照、並有名牌─個資外洩）」
- Google 相簿說明. https://support.google.com/photos/answer/6153599?hl=zh-Hant [RAW]
 「即使你隱藏相片的位置資訊，其他人仍有可能根據相片中出現的地標猜中相片的拍攝地點。」
 Limit: licence plates, screens and documents appear only in a UNICEF Montenegro Young Reporter opinion blog, 28 July 2026 (https://www.unicef.org/montenegro/en/blog/you-post-look-again) [RAW]: "capture random people and license plates in the background"; "my laptop screen reflected part of a document". Passports and boarding passes: Australian Passport Office, "Take care what you share!", 04 March 2025 (https://passports.gov.au/node/446) [TOOL]: "Don't share photos of your passport or boarding pass". No official children's source was found for plates, screens or tickets.

5. Permanence: SUPPORTED
- FTC, "Heads Up: Stop. Think. Connect.", August 2023. https://consumer.ftc.gov/articles/heads-up [RAW]
 "Once you post something online, you can't take it back"; "Even if you delete something you've posted — or the post expires — that photo or comment you don't want people to see anymore could be saved, shared, and live somewhere online — permanently."; "Anybody who sees your post can take a screenshot or recording."
- Common Sense Education, "Digital Trails" (Grade 2). https://www.commonsense.org/education/digital-citizenship/lesson/digital-trails [RAW]
 "digital footprint – a record of what you do online, including the sites you visit and the things you share"
- Chinese definition, eliteracy【無法鎖碼的網路內容】教案 (國中). https://eliteracy.edu.tw/Download.ashx?id=1865 [RAW]
 「數位足跡是指個人在網路上活動時，留下的各類數據與紀錄。」
 Limit: the sources say "could be" and "may", not that everything stays forever.

6. Audience settings: SUPPORTED
- FTC, same page [RAW]: "Use privacy settings. Find out how to turn on privacy settings for devices, apps, and social media accounts — then do it. This helps you limit who can see where you are, what you post, and who can connect with you." and "It's impossible to completely control who sees your profile, pictures, videos, or texts — even if you use privacy settings or apps that delete your content after it's viewed or within 24 hours."
- eSafety Commissioner, "Privacy and your child". https://esafety.gov.au/parents/skills-advice/privacy-child [TOOL]: "Even if their profile is set to private, they can't control what their friends will do with the content they post…"
- eliteracy 1506 [RAW]: 「分享對象：（ ） 公開 （ ） 朋友 （ ） 僅限自己」
 Limit: no platform-specific menu names were verified.

7. Ask permission: SUPPORTED
- FTC, same page [RAW]: "It can be embarrassing, unfair, and even unsafe to send or post photos and videos without getting permission from the people in them. Get someone's OK first. Before you post, ask them: 'Are you okay if I post this on social?' If they say no, don't post it."
- eliteracy【安全自拍，安心上傳】教案 (國中). https://eliteracy.edu.tw/Download.ashx?id=1509 [RAW]: 「將他人的照片或影片上傳到網路之前，必須先徵求對方的同意。」
- eliteracy【為什麼我的照片被公開在網路上？】教案 (國小三至四年級). https://eliteracy.edu.tw/Download.ashx?id=1484 [RAW]: 「在網路上發文或是上傳照片之前，要先想一想會不會對自己或別人造成傷害。」

8. Taiwan resources: PARTLY SUPPORTED
- 中小學數位素養教育資源網, https://eliteracy.edu.tw/ (footer: eliteracy(at)mail.moe.gov.tw; 網站維運：國立陽明交通大學; 最後更新 2026/9/29) [RAW]. Quotes as above, plus【個人資料正確用】教案 (id=1489): 「只要是可以讓別人知道我們身分的資料，都算是「個人資料」。」 I did not verify that this site is the successor to eteacher.edu.tw.
- iWIN, https://i.win.org.tw/about.php [RAW]: 「iWIN網路內容防護機構，是依照兒少法第46條授權，由國家通訊傳播委員會邀請各目的事業主管機關，如衛生福利部、教育部、文化部、內政部警政署及數發部等共同籌設。」 Home page: 「諮詢專線：02-2577-5118」.
 Limit: no iWIN page specifically on photo privacy was found. 數位發展部 was not checked.

9. Do apps strip location metadata? NOT ESTABLISHED for LINE, Instagram, Facebook, WhatsApp, Signal and X
- No official statement was found for any of them. X's help page lists the question "What happens to the Exif data for my photo?" but the answer text was not retrievable.
- What official sources do say:
 - Apple (claim 2): sharing includes location metadata unless it is turned off.
 - Google 相簿說明「Google 相簿如何保你的位置資料」[page's own title]. https://support.google.com/photos/answer/11190100?hl=zh-Hant [RAW]: 「分享新相簿、連結、對話和其他項目時，系統預設不會加入位置詳細資料 (除非是透過親友共享功能分享)。」 Answer 6153599 adds that for photos downloaded and emailed, 「系統會顯示裝置儲存的原始位置資訊」.
 - UK Safer Internet Centre, "Guide to removing EXIF metadata". https://saferinternet.org.uk/guide-to-removing-exif-metadata [RAW]: "whilst some platforms may automatically do this, the following steps are provided as a means to check and remove EXIF data".

Do NOT say
- 「傳到 LINE/IG/FB 會自動移除位置」, or that they keep it. Neither is established.
- 「設成不公開/只限朋友就安全」 or 「刪掉就消失」. FTC contradicts both.
- 「關掉位置別人就不知道在哪」. Google says landmarks can still give it away.
- 「每張手機照片都有定位」. Apple says only when 定位服務 is on for 相機.
- That 「選項」→「位置」 is documented for every iOS version (see the iOS 27 caveat), or what the Mac default for 「包含位置資訊」 is.
- 「個資法明文列出照片/住址/學校」, or that COPPA applies to Taiwanese children.
- That official guidance lists 車牌, 螢幕 or 票券. Present those as the lesson's own examples.

Possibly worth saving to memory: law.moj.gov.tw blocks automated fetching, so statutes need an official mirror (laws.gov.taipei LawArticleContent pages work). Apple Support guide pages can be downloaded raw per OS version, which is how the iOS 27 discrepancy surfaced.
