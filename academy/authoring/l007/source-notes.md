# L007 來源查核筆記（研究代理回報）

2026-10-07 由製作代理派出的研究子代理蒐集。子代理下載原始頁面後抽取文字；標 [V] 的引文是它在頁面文字中讀到的，
標 [TS] 的是擷取工具的摘要、不是逐字。主代理沒有逐頁重讀，只用這份筆記對照旁白、投影片與教材。以下為回報原文。

---

SOURCE CHECK: passwords / unique passwords / password managers / 2FA (fetched 2026-10-07)

Method note: WebFetch returns only model summaries, so I downloaded the pages directly and extracted the text. Quotes marked [V] were read in the page text. Quotes marked [TS] are "tool summary, not verbatim". cisa.gov returned 403 to direct download, so CISA web pages are [TS]; the CISA tip sheet was read from a mass.gov copy of the PDF.

1. Long beats short-complex; minimum lengths — SUPPORTED (numbers differ)
- CISA "Secure Our World Passwords Tip Sheet", https://www.mass.gov/files/documents/2023/10/06/Secure-Our-World-Passwords-Tip-Sheet.pdf, "As of August 14, 2023" [V]: "Make them long At least 16 characters—longer is stronger!"; "Create a memorable passphrase of 5-7 unrelated words". The live page https://www.cisa.gov/secure-our-world/use-strong-passwords could not be fetched (403).
- NIST "How Do I Create a Good Password?", https://www.nist.gov/cybersecurity-and-privacy/how-do-i-create-good-password, Created April 28, 2025, Updated August 20, 2025 [V]: "NIST guidance recommends that a password should be at least 15 characters long."; "adding these extra complexities will make the password harder to guess, but it's more important for the password to be long, so that should be your main priority."
- FTC "Creating Strong Passwords and Other Ways To Protect Your Accounts", https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts, November 2024 [V]: "Start by making your password long — aim for at least 12 characters."; "make sure that your passphrase consists of random words."
- Limits: NIST does not say symbols are useless. The FTC adds "If the account doesn't allow long passwords, mix uppercase and lowercase letters, numbers, and symbols".

2. Different password per account / 撞庫 — SUPPORTED
- OWASP "Credential stuffing", https://community.owasp.org/attacks/Credential_stuffing (redirected from owasp.org/www-community/attacks/Credential_stuffing), no date [V]: "Since many users will re-use the same password and username/email, when those credentials are exposed (by a database breach or phishing attack, for example) submitting those sets of stolen credentials into dozens or hundreds of other sites can allow an attacker to compromise those accounts too."
- FTC "Use Two-Factor Authentication To Protect Your Accounts", https://consumer.ftc.gov/articles/use-two-factor-authentication-protect-your-accounts, September 2022 [V]: "This works only if you use the same username and password in more than one place — and is a reason to never reuse the same username and password."
- 資安署 slides (see 8) [V, PDF layout text]: "駭客購買大量外洩帳密後，採撞庫攻擊登入".
- Limit: none of these gives a figure for how often it happens.

3. Password manager; Apple built-in — SUPPORTED
- CISA tip sheet (as 1) [V]: "A password manager creates, stores and fills passwords for us automatically. Then we each only have to remember one strong password—for the password manager itself."
- NIST page (as 1) [V]: "NIST experts highly recommend that you use a password manager."
- Apple 「使用『密碼』App 在 Apple 裝置間製作、管理及共享密碼和通行密鑰」, https://support.apple.com/zh-tw/120758 [V]: 「自 iOS 18、iPadOS 18、macOS Sequoia 和 visionOS 2 起，『密碼』App 能協助管理密碼、通行密鑰和驗證碼。你可以產生、製作並儲存高強度密碼」; 「如此一來，你就能讓所有帳號都使用獨有且複雜的密碼，而不必記住密碼。」
- Apple 「在 Mac 上的 Safari 中自動填寫使用者名稱與密碼」, https://support.apple.com/zh-tw/guide/safari/ibrwf71ba236/mac [V]: 「如果你已在 Mac 上設定 iCloud 鑰匙圈，第一次按一下密碼欄位時，系統會自動建議一個獨有且難以猜測的密碼。」 The same page warns: 「Safari 會以你的使用者登入資訊為任何使用 Mac 的使用者自動填寫你的資訊。」
- Limits: the Apple pages do not mention a "main password". The "one password to remember" wording is CISA's, about password managers in general.

4. 2FA adds a second step — SUPPORTED (the "cannot" wording is the FTC's)
- Apple 「『Apple 帳號』的雙重認證」, https://support.apple.com/zh-tw/102660, 發佈日期 2026 年 08 月 13 日 [V]: 「雙重認證能為『Apple 帳號』提供多一層安全保護，確保即使有人知道你的密碼，仍然只有你可以存取帳號。」; needs 「六位數驗證碼，此驗證碼會自動顯示在受信任裝置上，或傳送至受信任的電話號碼。」
- FTC 2FA page (as 2) [V]: "Even if a hacker knows your username and password, they can't log in to your account without the second credential or authentication factor."
- Google 「開啟兩步驟驗證功能」, https://support.google.com/accounts/answer/185839?hl=zh-Hant&co=GENIE.Platform%3DDesktop, no date [V]: 「您可以開啟兩步驟驗證 (又稱為「雙重驗證」)，在密碼遭竊時為帳戶多添一層保護。」
- Limit: NIST is weaker: MFA "can help protect a user's account even if their password is compromised" [V]. See 6: codes can be phished.

5. Never share a verification code — SUPPORTED (scope differs by source)
- Apple 「安全性與『Apple 帳號』」, https://support.apple.com/zh-tw/102614, 2024 年 09 月 24 日 [V]: 「切勿將你的『Apple 帳號』密碼、驗證碼、裝置密碼、復原密鑰或任何帳號安全性詳細資訊提供給任何人。Apple 絕對不會要求你提供這些資訊。」
- Google (as 4) [V]: 「請勿將驗證碼提供給任何人，以免帳戶遭詐騙者盜用。Google 不會透過通話要求您提供驗證碼。」
- FTC 2FA page [V]: "No matter what the story is, don't share your verification code with someone if you didn't contact them first."
- Limits: Google's "will not ask" covers phone calls only. The FTC's rule is conditional. No source says "all legitimate companies never ask".

6. Second factors are not equally strong — SUPPORTED
- FTC password page (as 1) [V], on text/email passcodes: "this is the least secure type of two-factor authentication, so choose a more secure method like an authenticator app or a security key".
- FTC 2FA page [V]: "Security keys are the strongest method of two-factor authentication because they don't use credentials that hackers can steal."; text/email codes are "better than nothing".
- NIST SP 800-63B-4, https://pages.nist.gov/800-63-4/sp800-63b.html, page stamp Tue, 26 Aug 2025 [V]: "Authenticators that involve the manual entry of an authenticator output (e.g., out-of-band and OTP authenticators) SHALL NOT be considered phishing-resistant".
- NIST consumer page [V]: "Some MFA methods are more secure than others (text codes are particularly vulnerable), but in general, having more than one factor for authentication makes your accounts more secure."
- CISA https://www.cisa.gov/MFA [TS]: "Some MFA types are better than others—phishing-resistant MFA is the standard all industry leaders should strive for, but any MFA is better than no MFA."
- Limit: by NIST's wording authenticator-app codes are also not phishing-resistant; only FIDO/WebAuthn-type methods are.

7. No personal info or common passwords; forced periodic change is outdated — SUPPORTED, with a scope limit
- NIST SP 800-63B-4 (as 6) [V]: "Verifiers and CSPs SHALL NOT impose other composition rules (e.g., requiring mixtures of different character types) for passwords."; "Verifiers and CSPs SHALL NOT require subscribers to change passwords periodically. However, verifiers SHALL force a change if there is evidence that the authenticator has been compromised."
- FTC password page [V]: "If a company or website tells you it lost your password in a data breach, change your password right away."
- Personal info: 資安署 (see 8) [V]: 「避免使用個人生日、電話等易被猜測資訊」.
- Limits: the NIST rules bind service providers, not users, and NIST's consumer page does not mention periodic changes. In practice Apple still requires 「至少八個字元，包含大寫和小寫字母，以及至少一個數字」 (102614) [V].

8. Taiwan official guidance — SUPPORTED
- 數位發展部資通安全署 新聞稿「強化帳密安全，落實三大防護原則」, https://moda.gov.tw/ACS/press/news/press/18660, 發稿日期 115年1月12日 [V]: 「強化密碼複雜度：密碼長度至少15個字元，並混合大小寫英文、數字及特殊符號，或使用密碼管理工具生成及管理密碼，避免使用個人生日、電話等易被猜測資訊。」; 「啟用兩步驟驗證：以使用密碼登入外增設第二個驗證步驟，如開啟簡訊驗證碼、臉部或指紋驗證，使用身分驗證器等」; 「常見之弱密碼 如「 123456 」、「 admin 」或以鍵盤排列順序設定之「QWERTY」」.
- The attached slides, https://www-api.moda.gov.tw/File/Get/acs/zh-tw/5HycTUokNYjQYJq, add 「至少包含15個字元(越長越好)」 and 「運用4到7個無關聯的單字組成」, credited 「來源：美國網路安全暨基礎設施安全局 CISA」.
- TWCERT/CC 「常見的OTP驗證」, https://www.twcert.org.tw/newepaper/cp-92-8285-1c028-3.html, 2024-12-04 [V]: 「也呼籲使用者切勿隨意將OTP資訊提供給他人」.
- Limits: 資安署 still advises mixing character types and does not rank second factors. 165 全民防騙網 and 教育部: not found (searched; no relevant page fetched).

9. Children's Apple accounts — SUPPORTED
- Apple 「為小孩建立『Apple 帳號』」, https://support.apple.com/zh-tw/102617, 2026 年 09 月 21 日 [V]: 「家長或監護人必須為未滿 13 歲的兒童建立『Apple 帳號』（年齡要求依國家或地區而異）。」
- Limit: Taiwan's exact age threshold was not checked.

Terminology: Apple zh-tw uses 雙重認證 and 通行密鑰; Google zh-Hant uses 兩步驟驗證 and 密碼金鑰; 資安署 uses 兩步驟驗證.

DO NOT SAY
- "Change your password every three months." NIST forbids providers from requiring it; change when there is a leak or unknown login.
- "A strong password must contain symbols and numbers." NIST puts length first; say some sites still require them.
- A single "official" minimum. It is CISA 16, NIST 15, 資安署 15, FTC 12; Apple accepts 8.
- "With 2FA nobody can ever get in." Codes can be phished; say "much harder".
- "SMS codes are useless." They are the weakest option but better than nothing.
- "Real companies never ask for a code" as a universal fact. Attribute it to Apple, or to Google for phone calls.
- "Authenticator apps are phishing-proof."
- That Apple's Passwords app has a "master password".
- Any CISA web-page sentence in quotation marks, until re-read in a browser.
