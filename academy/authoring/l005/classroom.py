"""Build the L005 classroom pack (real, usable materials; no private data).

    ./portable-runtime.sh python authoring/l005/classroom.py

After any change here: rerun pipeline/delivery.py, then verify (classroom is fingerprinted).
"""
from pathlib import Path
import csv
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import printpack  # noqa: E402

R = Path(__file__).resolve().parents[2]
E = R / 'episodes/academy/l005-search-master'
D = E / 'classroom/L005_搜尋高手'
PRINT = Path(__file__).resolve().parent / 'print'
PDF = D / '02_列印包_搜尋尋寶.pdf'

FILES = {
'00_爸爸先讀.md': '''# 父子科技學院 L005：搜尋高手——把大問題拆成好問題（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在孩子自己動手搜尋、比較，並寫出一張搜尋策略卡。

## 這堂課要帶走什麼

- 搜尋三步：拆問題 → 選關鍵字 → 比結果。
- 四把鑰匙：關鍵字、引號（完全相符）、減號（排除字詞）、時間條件。
- 同一題用模糊、精準、分段三種方法搜尋，比較答案品質。
- 至少一個限制或安全注意：排在前面不一定最正確、廣告有標示、AI 摘要可能出錯、不輸入個資。
- 作品：**搜尋策略卡**，另有三種搜法比較紀錄與自選規則卡。

## 課前準備（約 15 分鐘）

1. 列印 `02_列印包_搜尋尋寶.pdf`（A4，共 5 頁，單面）。沒有印表機也可以照著畫在白紙上。
2. 確認孩子的電腦可以上網、瀏覽器可用。在 Mac 的 Safari，直接在最上方的「智慧型搜尋」欄位輸入字詞就能搜尋；
   搜尋相關設定在 `Safari > 設定 > 搜尋`。
3. 先看一下搜尋引擎的安全設定。以 Google 為例，「安全搜尋」會嘗試過濾情色露骨與暴力血腥內容，
   但它只適用於 Google 搜尋，其他搜尋引擎或網站不受影響。爸爸請先確認目前的設定，課堂中也坐在旁邊。
4. 從列印包第 5 頁的寶藏題選一題，或和孩子一起想一題。題目不要包含姓名、住址、學校、帳號等個人資料。
5. 爸爸自己先用三種方法各搜一次，心裡有個底，但**不要準備標準答案**。
6. 錄音只保存在家裡的私人位置，不直接公開；錄音前先說課次與主題，不要唸出帳號、密碼或住址。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：出一個大問題，請孩子先用自己的方法搜尋 | 觀察，不糾正 |
| 10–25 | 看影片、認識四把鑰匙與拆問題；讀小抄卡 | 示範一次「口語問題 → 關鍵字」 |
| 25–65 | 三種搜法尋寶賽（規則見 `01_活動規則_三種搜法尋寶賽.md`） | 計時、幫忙記錄，不代打字 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：完成搜尋策略卡，加一條自選規則並測試 | 只在孩子開口時協助 |
| 105–115 | 角色互換：孩子教爸爸搜尋一個新問題 | 當學生，照孩子說的做，聽不懂就發問 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 問四個錄音問題，協助存檔 |

## 四把鑰匙的依據與限制（以 Google 搜尋為例）

- **關鍵字**：官方的搜尋提示建議從簡單字詞開始，並選用網頁上常出現的字詞，例如把「我的頭很痛」改成「頭痛」。
- **引號**：在字詞或詞組前後加上引號，搜尋完全相符的內容，例如 `"最高的建築物"`。
- **減號**：輸入 `-` 加上要排除的字詞，例如 `豹的速度 -汽車`。
- **時間**：搜尋後點選搜尋框下方的「工具」可依發布時間篩選；也可以用 `before:`、`after:` 加上年份或日期。
- **不要加空格**：運算子與字詞之間不可以有空格。`site:nytimes.com` 有效，`site: nytimes.com` 無效。
- **工具不一定都看得到**：顯示哪些搜尋工具，會因搜尋內容、結果類型和瀏覽器而不同。
- **別的搜尋引擎不一樣**：引號、減號在其他搜尋引擎多半也有，但寫法與效果可能不同，有的官方說明也承認部分語法並非每次都完全正確。
- 影片和教材的例子只示範寫法，**不保證你會看到一樣的結果**；每個人、每個時間看到的結果都可能不同。

## 資訊判讀與安全（請一定和孩子聊）

1. 排在最前面的結果不一定最正確。搜尋結果的排序和關聯程度、熱門程度等條件有關，不是正確性的保證。
2. 有些結果是廣告，會有「廣告」或「贊助」之類的標示（實際字樣以畫面為準）。先看標示，再決定要不要點。
3. 搜尋結果上方的 AI 摘要可能有誤。重要的事情要點進來源，並多方查證。
4. 找到答案後問三件事：相關嗎？誰寫的？資料多新？下一堂課會專門練習來源與證據。
5. 不要把密碼、住址、身分證字號、學校加姓名這類個人資料打進搜尋框。
6. 遇到讓人不舒服的內容，先關掉分頁，告訴爸爸，不必自己處理。

## 來源（查核日 2026-10-07）

- Google 搜尋說明「修正 Google 搜尋結果範圍」：https://support.google.com/websearch/answer/2466433?hl=zh-Hant
- Google 搜尋說明「瞭解搜尋提示…」：https://support.google.com/websearch/answer/134479?hl=zh-Hant
- Google 搜尋說明「利用篩選器縮小搜尋結果範圍」：https://support.google.com/websearch/answer/142143?hl=zh-Hant
- Google 搜尋說明「AI 摘要」：https://support.google.com/websearch/answer/14901683?hl=zh-Hant
- Google 搜尋說明「安全搜尋」：https://support.google.com/websearch/answer/510?hl=zh-Hant
- Google Ads 說明「Google 搜尋結果與廣告的差別」：https://support.google.com/google-ads/answer/1722080?hl=zh-Hant
- DuckDuckGo 進階語法說明：https://duckduckgo.com/duckduckgo-help-pages/results/syntax/
- Apple 支援「在 Mac 上使用 Safari 搜尋網際網路」：https://support.apple.com/zh-tw/guide/safari/sfrid73436cb/mac
- Apple 支援「在 Mac 上的 Safari 中進行自訂搜尋」：https://support.apple.com/zh-tw/guide/safari/ibrwe75c2a3c/mac
- 交通部中央氣象署「颱風消息」（寶藏題 A 可用的官方來源範例）：https://www.cwa.gov.tw/V8/C/P/Typhoon/TY_NEWS.html

課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
課表的主要參考網址（OpenAI Academy）談的是生成式 AI，本課沒有引用；拆問題的方法之後向 AI 提問時也用得到。
''',

'01_活動規則_三種搜法尋寶賽.md': '''# 三種搜法尋寶賽：規則

目標不是比誰快，而是比**哪一種搜法找到的答案比較好**。

## 準備

- 一個大問題（寶藏題）。可從列印包第 5 頁選，或自己出題，不含個人資料。
- 列印包第 2 頁「藏寶圖」、第 3 頁「三種搜法比較表」，或用 `03_比較紀錄.csv`。
- 同一台電腦、同一個瀏覽器、同一個搜尋引擎，三種方法才好比較。

## 評分標準（每一次搜尋都用同一套）

看前五筆結果，回答三個問題，各 0–2 分：

| 問題 | 0 分 | 1 分 | 2 分 |
|---|---|---|---|
| 相關嗎？ | 沒有回答問題 | 回答了一部分 | 直接回答問題 |
| 誰寫的？ | 看不出來 | 看得出是誰，但不確定可不可靠 | 是負責這件事的機關、學校或專業機構 |
| 資料多新？ | 沒有日期 | 有日期但很舊，或不確定還適不適用 | 有日期，而且對這個問題來說夠新 |

廣告和 AI 摘要不算在前五筆裡，但可以記下有沒有看到。

## 第一回合：模糊搜尋（約 8 分鐘）

1. 只輸入一到兩個字，例如寶藏題 A 只輸入：`颱風`。
2. 先預測：前五筆裡有幾筆能回答大問題？
3. 數一數並評分，寫進比較表。

## 第二回合：精準搜尋（約 12 分鐘）

1. 圈出大問題裡的二到四個關鍵詞，例如：`颱風 防災 準備 清單`。
2. 視需要加一把鑰匙：引號、減號或時間條件。每次只加一把，才知道是誰起作用。
3. 再數一次並評分。和第一回合比，差在哪裡？

## 第三回合：分段搜尋（約 20 分鐘）

1. 在「藏寶圖」把大問題拆成三個小問題。每個小問題都要能找到一個可以檢查的答案。
2. 三個小問題各搜尋一次，各自評分。
3. 每找到一個小問題的答案，並寫下來源是誰、日期是什麼時候，就得到一顆寶石。

## 結算（約 5 分鐘）

- 三種搜法各得幾分？哪一種最省力？哪一種答案最完整？
- 有沒有哪一次是關鍵字換個說法就變好的？
- 孩子說出結論，爸爸只追問「你怎麼知道的？」

## 常見卡關

- 結果太多太雜：關鍵字太少，或大問題還沒拆開。
- 完全找不到：關鍵字太口語，換成網頁上可能出現的說法；或引號裡的字太長。
- 減號沒效果：檢查減號和字詞中間是不是多了空格。
- 找不到時間篩選：工具會因搜尋內容和瀏覽器而不同，改用 `after:` 加日期，或換一種搜尋類型再試。
''',

'03_比較紀錄_填寫說明.md': '''# 比較紀錄怎麼寫

`03_比較紀錄.csv` 可以用 Numbers 或任何試算表開啟；也可以直接寫在列印包第 3 頁。

每一次搜尋寫一列：

- **我輸入的字詞**：照實寫，連引號、減號都寫出來。
- **用到的鑰匙**：關鍵字、引號、減號、時間條件，沒有就寫「無」。
- **前五筆有用幾筆**：0 到 5。廣告和 AI 摘要不算。
- **最好的來源是誰**：寫出機關、學校、媒體或網站名稱，看不出來就寫「不確定」。
- **資料日期**：網頁上寫的日期，沒有就寫「無」。
- **相關／來源／新舊**：照規則各給 0–2 分。
- **備註**：換了什麼說法、哪裡卡住、有沒有看到廣告或 AI 摘要。

三種搜法用的是同一個大問題、同一台電腦、同一個搜尋引擎，這樣比較才公平。
你看到的結果可能和別人不一樣，這很正常，照你自己看到的記錄就好。
''',

'04_搜尋策略卡_寫法與檢查表.md': '''# 作品：搜尋策略卡

用列印包第 4 頁的卡片，或自己拿一張紙寫。這張卡以後查資料都可以拿出來用。

## 卡上要有

1. **我的大問題**：一句話。
2. **三個小問題**：每個都能找到一個可以檢查的答案。
3. **關鍵字與鑰匙**：每個小問題用了哪些詞、哪一把鑰匙。
4. **我的搜尋規則**：至少一條自己訂的規則（見 `05_自選規則卡.md`）。
5. **一個限制或安全提醒**：用自己的話寫。

## 交件前檢查

- [ ] 大問題和小問題都沒有個人資料
- [ ] 三個小問題都實際搜尋過，並寫下答案的來源與日期
- [ ] 至少用過引號、減號、時間條件其中兩把鑰匙
- [ ] 寫了一條自己的搜尋規則，而且真的測試過
- [ ] 能不看稿說出：為什麼要先拆問題
- [ ] 寫上作品名稱、版本與日期，例如 `L005_搜尋策略卡_v01`
- [ ] 拍照或掃描後存進本課資料夾，並打開確認看得清楚
''',

'05_自選規則卡.md': '''# 孩子獨立改造：加一條自己的搜尋規則

選一條，或自己發明。一次只加一條，才知道它有沒有用。

## 靈感

- 每個小問題至少換兩種說法再決定。
- 重要的答案，一定要在第二個來源也找到。
- 先看是誰寫的，再看內容。
- 需要最新資料的問題，一定加上時間條件。
- 只在某一個網站裡找：`site:` 加網站，例如 `site:cwa.gov.tw 颱風`。
- 只找某一種檔案：`filetype:` 加檔案類型，例如 `filetype:pdf`。
- 看到廣告標示先跳過，從沒有標示的結果看起。

## 我的規則卡

- 規則名稱：＿＿＿＿＿＿＿＿＿＿
- 我的規則（一句話）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 我預測它會讓搜尋：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 用同一個小問題測試，加規則前：＿＿＿ 分　加規則後：＿＿＿ 分
- 我看到的證據：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 這條規則什麼時候不適用？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 要保留、修改，還是拿掉？為什麼？＿＿＿＿＿＿＿＿＿＿＿＿＿＿

把結果也記到比較紀錄的「自選規則」那一列。
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成搜尋策略卡（大問題、三個小問題、關鍵字與鑰匙、自己的規則、一個限制）
- [ ] 不看稿說出搜尋三步：拆問題 → 選關鍵字 → 比結果
- [ ] 示範四把鑰匙各一次：關鍵字、引號、減號、時間條件
- [ ] 三種搜法的比較紀錄有分數，也有「怎麼知道的」
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 測試過一條自選規則，並說明要不要保留

## 孩子教爸爸（105–115 分鐘）

請孩子當老師，爸爸當學生。建議順序：

1. 爸爸出一個新的大問題（不含個資）。
2. 孩子示範怎麼拆成小問題，爸爸照著寫。
3. 孩子選關鍵字，並決定要不要加一把鑰匙，說出理由。
4. 一起看結果，孩子說出哪一筆比較可信、為什麼。
5. 孩子出一題考爸爸，例如：「減號後面多一個空格會怎樣？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

1. 把大問題拆成好問題，是在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：`L005_搜尋策略卡_v01`、`L005_比較紀錄_v01`、`L005_自選規則卡_v01`，
放進 `文件/Tech Academy/L005_搜尋高手/`，存好後再打開一次確認。
''',

'07_四把鑰匙小抄.md': '''# L005 四把鑰匙小抄（以 Google 搜尋為例）

| 鑰匙 | 做什麼 | 寫法 | 例子 |
|---|---|---|---|
| 關鍵字 | 說清楚要找什麼 | 挑二到四個重要的詞 | `貓 抓沙發 原因` |
| 引號 | 找完全相符的字詞或句子 | 前後加半形雙引號 | `"床前明月光"` |
| 減號 | 排除含有某個字詞的結果 | `-` 緊貼著字詞 | `蘋果 -手機` |
| 時間條件 | 找夠新（或某段時間）的資料 | 搜尋後按「工具」；或 `after:`、`before:` 加日期 | `太空 新發現 after:2026/01/01` |

## 進階鑰匙（自選規則可以用）

| 鑰匙 | 做什麼 | 例子 |
|---|---|---|
| `site:` | 只在某個網站裡找 | `site:cwa.gov.tw 颱風` |
| `filetype:` | 只找某種檔案 | `防災手冊 filetype:pdf` |

## 四個提醒

- 運算子和字詞之間不要有空格：`-手機` 可以，`- 手機` 不行。
- 看得到哪些工具，會因搜尋內容和瀏覽器而不同；別的搜尋引擎寫法也可能不同。
- 排在最前面不一定最正確；廣告有標示；AI 摘要可能出錯，重要的事多方查證。
- 不把密碼、住址這類個人資料打進搜尋框。

我最常用的鑰匙：＿＿＿＿＿＿　我最容易忘記的事：＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

NOTE_HEADER = ['搜法', '問題', '我輸入的字詞', '用到的鑰匙', '前五筆有用幾筆', '最好的來源是誰', '資料日期',
               '相關(0-2)', '來源(0-2)', '新舊(0-2)', '備註']
NOTE_ROWS = [['第一回合 模糊', '大問題'], ['第二回合 精準', '大問題'], ['第三回合 分段', '小問題一'],
             ['第三回合 分段', '小問題二'], ['第三回合 分段', '小問題三'], ['自選規則', '（寫下測試的小問題）']]

EXTRA_CSS = '''.key{height:118mm}.key h3{font-size:19pt}.key code{font-size:13pt}.key p{margin:1.5mm 0}
.key .warn{font-size:10.5pt;color:#35506b;border-top:.8pt solid #9db7cc;padding-top:2mm;margin-top:3mm}
.strip{margin-top:5mm;font-size:11pt}.big{min-height:22mm}.q{margin-bottom:4mm}.q h3{font-size:13.5pt;margin-bottom:1mm}
.q table td{height:11mm}.cmp td{height:17mm}.cmp th{font-size:10pt;padding:1mm 1.2mm}.cmp{table-layout:fixed}.card{height:108mm;padding:4mm 6mm}.card h3{font-size:16pt;margin:0}
.card p{margin:.8mm 0 0;font-size:11pt}.card .line{height:6.4mm}.quest{height:58mm}.quest h3{font-size:14pt}.quest p{margin:1mm 0;font-size:11.5pt}
.rubric td,.rubric th{font-size:10.5pt;padding:1mm 2mm}'''


def html():
    key = lambda name, what, how, example, warn: (
        f'<div class="cut key"><h3>{name}</h3><h4>做什麼</h4><p>{what}</p><h4>怎麼寫</h4><p>{how}</p>'
        f'<h4>例子</h4><p><code>{example}</code></p><p class="warn">{warn}</p></div>')
    pages = []
    pages.append('<h2>四把鑰匙小抄卡</h2><p class="lead">沿外框剪下，搜尋時放在鍵盤旁邊。以 Google 搜尋為例。</p><div class="grid2">'
        + key('關鍵字', '說清楚要找什麼', '挑出二到四個最重要的詞，用網頁上可能出現的說法', '貓 抓沙發 原因', '結果不好，就換個說法再試一次。')
        + key('引號', '找完全相符的字詞或句子', '在前後加上半形的雙引號', '&quot;床前明月光&quot;', '適合找一句話的出處、歌名、錯誤訊息。')
        + key('減號', '排除含有某個字詞的結果', '減號緊貼著要排除的字詞', '蘋果 -手機', '減號和字詞之間不要有空格。')
        + key('時間條件', '找夠新，或某段時間的資料', '搜尋後按「工具」依時間篩選；或直接輸入日期條件', '太空 新發現 after:2026/01/01', '看得到哪些工具，會因搜尋內容和瀏覽器而不同。')
        + '</div><p class="strip">進階鑰匙：<code>site:cwa.gov.tw 颱風</code> 只在某個網站裡找；<code>防災手冊 filetype:pdf</code> 只找某種檔案。</p>')
    small = lambda n: (f'<div class="box q"><h3>小問題{n}：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</h3>'
        '<table><tr><th style="width:26%">我輸入的字詞</th><td></td></tr><tr><th>用了哪把鑰匙</th><td></td></tr>'
        '<tr><th>找到的答案</th><td></td></tr><tr><th>來源是誰、日期</th><td></td></tr></table></div>')
    pages.append('<h2>藏寶圖：把大問題拆成小問題</h2><p class="lead">每個小問題，都要能找到一個可以檢查的答案。一次只搜尋一個。</p>'
        '<div class="box q big"><h3>我的大問題（不含個人資料）</h3><div class="line"></div></div>'
        + small('一') + small('二') + small('三')
        + '<p class="note">每找到一個小問題的答案，並寫下來源與日期，就得到一顆寶石。我得到 ＿＿ 顆。</p>')
    row = lambda a, b: f'<tr><td>{a}<br><span class="note">{b}</span></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>'
    pages.append('<h2>三種搜法比較表</h2><p class="lead">同一個大問題、同一台電腦、同一個搜尋引擎。看前五筆，廣告和 AI 摘要不算。</p>'
        '<table class="cmp"><tr><th style="width:14%">搜法</th><th style="width:24%">我輸入的字詞</th><th style="width:11%">前五筆<br>有用幾筆</th>'
        '<th style="width:17%">最好的<br>來源是誰</th><th style="width:11%">資料<br>日期</th><th>相關<br>0–2</th><th>來源<br>0–2</th><th>新舊<br>0–2</th></tr>'
        + row('第一回合', '模糊搜尋') + row('第二回合', '精準搜尋') + row('第三回合', '小問題一') + row('第三回合', '小問題二')
        + row('第三回合', '小問題三') + row('自選規則', '我的新規則') + '</table>'
        '<div class="box" style="margin-top:5mm"><b>我的結論</b><p class="note">哪一種搜法的答案最好？我怎麼知道的？</p><div class="line"></div><div class="line"></div></div>')
    card = ('<div class="cut card"><h3>搜尋策略卡</h3><p>我的大問題</p><div class="line"></div>'
        '<p>三個小問題</p><div class="line"></div><div class="line"></div><div class="line"></div>'
        '<p>我最常用的鑰匙</p><div class="line"></div><p>我的搜尋規則</p><div class="line"></div>'
        '<p>一個限制或安全提醒</p><div class="line"></div>'
        '<p class="note">名稱：L005_搜尋策略卡_v＿＿　日期：＿＿＿＿　代號：＿＿＿＿</p></div>')
    pages.append('<h2>作品：搜尋策略卡</h2><p class="lead">一人一張。寫好後剪下，以後查資料都可以拿出來用。</p>' + card + '<div style="height:6mm"></div>' + card)
    quest = lambda tag, q, hint: f'<div class="cut quest"><h3>寶藏題 {tag}</h3><p><b>{q}</b></p><p class="note">{hint}</p></div>'
    pages.append('<h2>寶藏題卡與評分標準</h2><p class="lead">選一題當大問題。本教材不提供標準答案，重點是比較搜法。</p><div class="grid2">'
        + quest('A', '颱風來之前，我們家要準備什麼？', '可以拆成：警報在哪裡看？要準備哪些東西？停電停水時怎麼辦？')
        + quest('B', '想養一隻倉鼠，要先知道什麼？', '可以拆成：吃什麼？需要什麼樣的環境？每個月大概要花多少？')
        + quest('C', '想在陽台種一種香草植物，該選哪一種？', '可以拆成：需要多少日照？多久澆一次水？什麼季節適合種？')
        + quest('D', '自己出題：＿＿＿＿＿＿＿＿＿', '不要包含姓名、住址、學校、帳號等個人資料。')
        + '</div><table class="rubric" style="margin-top:6mm"><tr><th>評分</th><th>0 分</th><th>1 分</th><th>2 分</th></tr>'
        '<tr><th>相關嗎？</th><td>沒有回答問題</td><td>回答了一部分</td><td>直接回答問題</td></tr>'
        '<tr><th>誰寫的？</th><td>看不出來</td><td>看得出是誰，但不確定可不可靠</td><td>負責這件事的機關、學校或專業機構</td></tr>'
        '<tr><th>資料多新？</th><td>沒有日期</td><td>有日期但很舊，或不確定還適不適用</td><td>有日期，而且對這個問題來說夠新</td></tr></table>'
        '<p class="note" style="margin-top:4mm">排在最前面不一定最正確；廣告有標示；AI 摘要可能出錯，重要的事多方查證。不把個人資料打進搜尋框。</p>')
    return printpack.document('L005 搜尋高手 列印包', '父子科技學院 L005｜搜尋高手', pages, EXTRA_CSS)


def main():
    D.mkdir(parents=True, exist_ok=True)
    PRINT.mkdir(parents=True, exist_ok=True)
    for name, text in FILES.items():
        assert '待編寫' not in text
        (D / name).write_text(text, encoding='utf-8')
    with (D / '03_比較紀錄.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f); w.writerow(NOTE_HEADER)
        w.writerows([r + [''] * (len(NOTE_HEADER) - len(r)) for r in NOTE_ROWS])
    source = PRINT / 'print-pack.html'
    source.write_text(html(), encoding='utf-8')
    rendered = printpack.render(source, PDF)

    names = sorted(p.name for p in D.iterdir() if p.is_file())
    for name in FILES:
        assert (D / name).read_text(encoding='utf-8').strip()
    with (D / '03_比較紀錄.csv').open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    assert len(rows) == 7 and all(len(r) == len(NOTE_HEADER) for r in rows)
    pages = printpack.check(PDF, 5, ('四把鑰匙小抄卡', '藏寶圖', '三種搜法比較表', '搜尋策略卡', '寶藏題', '蘋果 -手機', 'after:2026/01/01'))
    (E / 'qc').mkdir(exist_ok=True)
    (E / 'qc/classroom-validation.json').write_text(json.dumps({
        'folder': D.relative_to(E).as_posix(), 'files': names, 'fileCount': len(names),
        'utf8TextReadable': True, 'comparisonRows': len(rows) - 1, 'comparisonColumns': len(NOTE_HEADER),
        'printPack': {'file': PDF.name, 'pages': pages, 'allFontsEmbedded': True, 'renderedThisRun': rendered,
                      'source': 'authoring/l005/print/print-pack.html'},
        'answersProvided': False, 'privateData': 'none',
        'status': 'PASS (structure); page-by-page visual review recorded separately'},
        ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Classroom pack: {len(names)} files, print pack {pages} pages')


if __name__ == '__main__':
    main()
