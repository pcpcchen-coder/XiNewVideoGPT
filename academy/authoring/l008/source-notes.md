# L008 來源查核筆記（研究代理回報）

2026-10-07 由製作代理派出的研究子代理蒐集。子代理下載原始頁面後抽取文字並回報引文；它自己標示了哪些是逐字讀到的、
哪些只是擷取工具的摘要。主代理沒有逐頁重讀，只用這份筆記對照旁白、投影片與教材。以下為回報原文。

---

SOURCE CHECK: phishing lesson (8 claims)

How quotes were obtained: raw page HTML/PDF downloaded and converted to text, so quotes are verbatim, EXCEPT CISA (raw fetch returned 403; quotes came from the WebFetch extractor and are marked [tool-extracted, not verified against raw page]).

Sources (URL as fetched; date shown)
A. FTC, "How To Recognize and Avoid Phishing Scams" — https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams — "September 2022"
B. FTC Consumer Alert, "Protect yourself from phishing scams" — https://consumer.ftc.gov/consumer-alerts/2025/04/protect-yourself-phishing-scams — June 4, 2025
C. FTC, "How to Recognize and Report Spam Text Messages" — https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages — "July 2022"
D. FTC Youville handout for kids, "Filling Your Digital Toolbox" (PDF) — https://consumer.ftc.gov/system/files/consumer_ftc_gov/pdf/FillingYourDigitalToolbox-508.pdf — no printed date (PDF metadata 2024-07-16)
E. Apple 支援 (台灣), 「辨識及防範社交工程詐騙，包括網路釣魚訊息、假的支援電話和其他詐騙」 — https://support.apple.com/zh-tw/102568 — 發佈日期：2026 年 06 月 22 日. The current title is 「辨識及防範…」, not 「辨識並避免…」.
F. Gmail說明, 「防範及檢舉網路釣魚電子郵件」 — https://support.google.com/mail/answer/8253?hl=zh-Hant — no date. The page states: 「這個頁面可能含有使用 AI 技術翻譯的內容，也許會有錯誤。」
G. UK NCSC, "How to spot a scam email, text message or call" — https://www.ncsc.gov.uk/collection/phishing-scams/spot-scams — Published 26 November 2021, Reviewed 5 September 2022
H. UK NCSC, "Phishing scams: If you've shared sensitive information" — https://www.ncsc.gov.uk/collection/phishing-scams/what-to-do — same dates
I. Microsoft Support, 「Outlook 中的網路釣魚和可疑行為」 — https://support.microsoft.com/zh-TW/Outlook/mail/phishing-and-suspicious-behavior-in-outlook — no visible date (page metadata ms.date 03/09/2026). The Chinese reads as machine translation.
J. 行政院新聞, 「催繳水電費用是詐騙老梗 慎防「+號境外開頭簡訊」陷阱」 — https://www.ey.gov.tw/Page/9277F759E41CCD91/752cb47e-7aab-478f-87da-2946b0ce3c5b — 日期：112-11-20
K. CISA, "Recognize and Report Phishing" — https://www.cisa.gov/secure-our-world/recognize-and-report-phishing — no date [tool-extracted]

CLAIM 1 — supported (the word "smishing" was not found)
- A: "Scammers use email or text messages to try to steal your passwords, account numbers, or Social Security numbers." / "Attachments and links might install harmful malware."
- F: 「網路釣魚是指企圖竊取個人資訊或駭入線上帳戶的行為，媒介包括電子郵件、訊息、廣告，或是與您使用過的網站類似的網站。」
- G: "Cyber criminals may contact you via email, text, phone call or via social media."
- Limit: no fetched page uses "smishing". Social media is named only by NCSC and Gmail (「社群媒體貼文/訊息和簡訊」).

CLAIM 2 — supported; spelling mistakes are NOT a reliable sign
- Generic greeting, A: "The email has a generic greeting."
- Urgency and prizes, F: 「如果郵件內容的語氣急迫，或是許諾提供有違常理的好處，請特別留意」
- Urgency, G: "Are you told you have a limited time to respond (such as 'within 24 hours' or 'immediately')?"
- Sender, link, personal info and attachment, E: 「寄件人的電子郵件或電話與其所聲稱的公司名稱不符。」「訊息中的連結看似正確，但 URL 與該公司的網站不符。」「訊息內容要求提供個人資訊，例如信用卡號碼或帳號密碼。」「無故寄來的訊息，且包含附件。」
- Gift cards, E: 「請勿使用 Apple Gift Card 支付款項給其他人。」
- Spelling, G: "It used to be easier to spot scams. They might contain bad spelling or grammar… But scams are getting smarter and some even fool the experts."
- Spelling, K [tool-extracted]: "A common sign used to be poor grammar or misspellings although in the era of artificial intelligence (AI) some emails will now have perfect grammar and spelling, so look out for the other signs."
- Limit: Apple's urgency wording (「製造強烈的緊迫感」) sits in its phone/social-engineering section, not its email list. Gift cards appear only as an Apple Gift Card rule.

CLAIM 3 — supported
- B: "Don't click links or download attachments in unexpected messages. If you think the message could be legit, contact the company or bank using a phone number, email, or website you know is real."
- E: 「若有可疑或無故寄來的訊息，切勿點開其中的連結，或是打開或儲存附件。」
- A: "If you see them, report the message and then delete it."
- F: 「切勿回應透過電子郵件、簡訊或通話索取私人資訊的要求。」
- Child, D: "Remember, it's always safer not to respond. If you need more help, ask a parent or trusted adult to look at the message and help you figure out what to do."
- Limit: a flat "never reply" appears only in CISA [tool-extracted]: "Don't reply or click on any attachment or link, including any 'unsubscribe' link."

CLAIM 4 — supported
- E (footnote to the URL bullet): 「若要在 Mac 上確認連結導向的網站，請將指標停留在連結上方，即可查看 URL。如果 Safari 的狀態列未顯示 URL，請依序選擇「顯示方式」和「顯示狀態列」。在 iOS 裝置上，你可以按住連結。」
- F: 「在電腦上點選連結前，建議您先將滑鼠游標懸停在連結上。如果顯示的網址與說明不相符，就表示該連結可能會將您導向網路釣魚網站。」
- Look-alike sites, C: "Some links might take you to a spoofed website that looks real but isn't."
- Look-alike domain, K [tool-extracted]: "Incorrect email addresses or links, like amazan.com"
- Limit: no verbatim-checked page explains how to read a domain name. The misspelled-domain example is CISA only.

CLAIM 5 — partly supported (FTC does not say "change password / turn on 2FA" in that section)
- A: "If you think a scammer has your information, like your Social Security, credit card, or bank account number, go to IdentityTheft.gov." / "If you think you clicked on a link or opened an attachment that downloaded harmful software, update your computer's security software. Then run a scan and remove anything it identifies as a problem."
- E: 「…可能已在詐騙網站上輸入密碼或其他個人資訊，請立即更改 Apple 帳號密碼，並確認已啟用雙重認證。」
- H: "You should change the passwords on any of your accounts which use the same password."
- Limit: the password and 2FA wording is Apple's (about the Apple account) and NCSC's. IdentityTheft.gov is US-only.

CLAIM 6 — supported for Apple, Gmail and 165 (via 行政院); 165's own site could not be read
- E: 「如果收到看似由 Apple 寄發的可疑電子郵件，請將其轉寄至 reportphishing@apple.com。」 For SMS: 「請拍攝訊息的截圖，然後將截圖寄送到 reportphishing@apple.com。」 In Messages: 「請點一下訊息底下的「回報垃圾訊息」。」
- F: 「在電腦上前往 Gmail。」「開啟郵件。」「按一下「回覆」圖示 旁邊的「更多」圖示 。」「按一下「回報為網路釣魚郵件」。」
- J: 「民眾如有詐騙疑義也可撥打「165」反詐騙專線、或是上「內政部警政署165全民防騙網站（ https://165.npa.gov.tw/ ）」，檢舉詐騙簡訊。」 Also: 「切勿點擊連結，務必小心查證」
- Limit: 165.npa.gov.tw is a JavaScript app and returned no readable text, so there is no first-hand 165 wording and its current menu labels are unverified. J is from 2023 and concerns SMS. FTC's channels (reportphishing@apwg.org, 7726, ReportFraud.ftc.gov) are US channels.

CLAIM 7 — partly supported (each source speaks for itself or one channel; no Taiwan bank-regulator source was found)
- E: 「切勿將你的 Apple 帳號密碼或驗證碼與任何人分享。Apple 絕不會為了提供支援而要求提供這類資訊。」
- F: 「注意：Gmail 絕不會透過電子郵件詢問您的密碼等個人資訊。」
- A: "legitimate companies won't email or text with a link to update your payment information."
- C: "Legitimate companies won't ask for information about your account by text."
- G: "your bank (or any other official source) will never ask you to supply personal information via email"

CLAIM 8 — supported
- I: 「一些欺騙性電子郵件看似來自安全的發件人，但實際上有一個「欺騙」的來源地址來欺騙您。」 / 「您在郵件中看到的電子郵件地址可能與您在 [寄件者] 電子郵件地址中看到的不同。」
- F: 「檢查電子郵件地址與寄件者名稱是否相符。」「檢查郵件標頭，確保「寄件者」標頭並未顯示不正確的名稱。」
- Limit: no fetched page says in plain words "anyone can type any display name". Microsoft's Chinese is awkward, so paraphrase it. Apple's spoofing sentence is about phone numbers.

DO NOT SAY
- "Phishing messages always have spelling mistakes" or "good spelling means it is real" — contradicted by NCSC and CISA.
- "If the sender address looks right, it is safe" — contradicted by Microsoft.
- "FTC says to change your password and turn on 2FA after clicking" — that wording is Apple's and NCSC's.
- "Forward it to 7726 / reportphishing@apwg.org / ReportFraud.ftc.gov" as steps for Taiwan.
- "Forward any phishing email to reportphishing@apple.com" — Apple says only mail that looks like it is from Apple.
- "Real companies never send links or emails" — FTC: "real companies might communicate with you by email".
- "It's called smishing" as a sourced term, or exact 165 website button names — neither was found.
- "Hovering proves a link is safe" — sources say only that a mismatch signals danger.
- Gmail's report steps as phone steps — the page says 「在電腦上」.

Not usable: the TWCERT/CC results were enterprise threat newsletters, and no usable 數位發展部 or 教育部 page turned up. The 新北市警察局 page had only the phone-scam slogan 「1聽2掛3撥打165查證」.

Housekeeping: no repo or project files were written. Downloads are in the scratchpad under phish_dl_k7q/. Another concurrent process overwrote scratchpad tools/h2t.py, so the shared tools/ and dl/ folder names collide — use unique folder names there.
