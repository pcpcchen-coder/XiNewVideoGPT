"""Build the L014 classroom pack (real, usable materials; no private data, no account or AI tool needed).

    ./portable-runtime.sh python authoring/l014/classroom.py

The warm-up vague rules and the example rules are written for this lesson; the minutes in the
examples are placeholders for the family to negotiate, not health advice.
After any change here: rerun pipeline/delivery.py, then verify.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import classroom_pack  # noqa: E402
import printpack  # noqa: E402

TOPICS = ['使用時間', '花錢', '隱私', '作業和 AI', '求助']
CONDITIONS = [('說得清楚', '寫出誰、什麼時候、做什麼'), ('做得到', '兩個人都同意，也真的做得到'), ('檢查得到', '一看就知道有沒有做到')]

# Warm-up: (vague rule, which condition it fails, one executable rewrite)
WARMUP = [
    ('不要玩太久', '說不清楚：多久算太久？', '寫完功課後，在客廳用三十分鐘；鬧鐘響了就存檔關機'),
    ('不可以亂買', '說不清楚：什麼叫亂買？', '要付錢的東西，都先問爸爸，爸爸同意了才買'),
    ('永遠不碰手機', '做不到：查功課、打電話也要用', '吃飯的時候，全家的手機都放進客廳的籃子'),
    ('要乖乖的', '檢查不到：怎麼看出有沒有做到？', '在網路上看到害怕的東西，當天就告訴爸爸媽媽'),
]
assert len(WARMUP) == 4

# Example rules, one per topic (used in 04 as a reference after the race, never handed out before it)
EXAMPLES = {
    '使用時間': ('平日寫完功課後，可以在客廳用平板三十分鐘；鬧鐘響了就存檔關機', '眼睛和睡覺都需要休息；在客廳比較容易互相提醒', '隔天少用十分鐘，自己設鬧鐘'),
    '花錢': ('遊戲裡的點數、寶石、會員，和下載新遊戲，都先問爸爸，同意了才買', '那些都是真的錢；免費遊戲裡也可能有要付錢的東西', '一起看帳單，想辦法退款或補回來，下次先問'),
    '隱私': ('姓名、學校、住址、電話、照片和密碼，不在網路上給別人，也不打進 AI 工具', '這些資料能讓陌生人找到你，或登入你的帳號', '馬上告訴爸爸，一起改密碼或刪除'),
    '作業和 AI': ('作業先自己想、自己寫；老師允許才問 AI，答案自己查證，並寫出用了什麼工具、用在哪裡', '作業是為了自己學會；它會說錯；老師要知道哪些是你做的', '重寫自己沒想過的那一段，再跟老師說明'),
    '求助': ('看到害怕、不舒服的東西，或有人要錢、要照片、叫你保密，當天就告訴爸爸媽媽', '越早說，越容易處理；叫你保密的人，常常就是有問題的人', '（給爸爸）孩子來說，先謝謝他，先一起處理，不先罵人'),
}
assert list(EXAMPLES) == TOPICS

HELP = [('爸爸媽媽', '第一個找的人；在家裡、在外面都一樣'),
        ('老師、學校輔導老師', '在學校遇到的事'),
        ('iWIN 網路內容防護機構', '諮詢專線 02-2577-5118（看到不當的網路內容）'),
        ('165 反詐騙專線', '有人要錢、說你中獎、要你匯款')]

FILES = {
'00_爸爸先讀.md': '''# 父子科技學院 L014：我們家的科技公約（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在你和孩子各寫五條規則、一條一條協商，最後一起簽下「家庭科技公約 v1.0」。

## 這堂課要帶走什麼

- 公約：全家人一起討論、一起答應、一起遵守的約定。**爸爸也要寫五條、也要遵守。**
- 好規則的三個條件：**說得清楚**（誰、什麼時候、做什麼）、**做得到**（兩個人都同意，也真的做得到）、**檢查得到**（一看就知道有沒有做到）。
  每一條還要寫**理由**，和**沒做到的時候怎麼補救**。
- 五個主題：使用時間、花錢、隱私、作業和 AI、求助。
- 作品：**家庭科技公約 v1.0**（列印包第 5 頁），加上十張規則卡和協商紀錄。

## 課前準備（約 15 分鐘）

1. 列印 `02_列印包_科技公約.pdf`（A4，共 6 頁，單面）。第 2、3 頁的規則卡沿虛線剪開。
2. 讀一遍 `04_五個主題解說.md`：裡面有第 1 頁暖身題的參考答案，以及每個主題的範例規則。**範例請在競速之後才拿出來**，先讓孩子自己想。
3. 準備計時器（八分鐘）、鉛筆、彩色筆、膠帶或磁鐵（把公約貼起來）。
4. 先想好你自己的五條規則裡，至少有一條是**管你自己的**（例如吃飯時你的手機也放進籃子）。孩子看到爸爸也被規則管，協商才公平。
5. 課表的課前準備是「確認兒童帳號、家庭備份與瀏覽器可用；準備不含真實個資的範例」。這堂課用不到兒童帳號、瀏覽器或任何 AI 工具；
   範例已經在列印包裡，都不含真實個資。
6. 錄音（最後的總結）只保存在家裡的私人位置，不上傳、不公開；錄音前先說課次與主題。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：問孩子「我們家現在有哪些沒寫下來的規則？」說出三條 | 只聽、不辯解 |
| 10–25 | 看影片：三個條件、五個主題；做列印包第 1 頁的暖身題（把模糊規則改成做得到） | 回答問題，說說你自己的理由 |
| 25–65 | 父子共同實作：規則競速（八分鐘各寫五條）＋一條一條協商（規則見 `01`） | 也寫五條；協商時先說理由，再聽孩子的理由 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：把協商好的規則抄進公約 v1.0，增加一個自選規則或功能，請爸爸試一次（見 `05`） | 只在孩子開口時協助；照著孩子的規則做一次 |
| 105–115 | 角色互換：孩子教爸爸好規則的三個條件，並挑一條說明為什麼做得到 | 當學生，故意拿一條模糊的規則問他 |
| 115–120 | 錄音總結、作品命名、版本存檔、全家簽名 | 錄音、簽名、把公約貼在看得到的地方 |

## 協商時的三個提醒

- **不靠大聲贏。** 每一條都要說得出理由；說不出理由的，先放進「下一版再談」。
- **做不到的改小一點，不是刪掉。** 例如「永遠不碰手機」改成「吃飯的時候全家手機放進籃子」。
- **補救不是處罰。** 「沒做到怎麼辦」寫的是怎麼補回來（隔天少用十分鐘、一起退款、一起改密碼），不是罵人或沒收。

## 分鐘數是你們自己訂的

影片和範例裡的「三十分鐘」只是寫規則的**例子**，不是建議的螢幕時間；本課沒有引用任何每日分鐘數的建議。
時間多長、在哪裡用，由你們依孩子的年紀、作業與睡眠一起協商。

## 家長控制功能只是幫手

Mac、iPhone、iPad 有「螢幕使用時間」，可以設定使用時段、App 使用限額，替孩子管理通常需要先設定「家人共享」；
「家人共享」的組織者也可以管理「購買前詢問」。本次製作環境連不上 Apple 支援網站，**這些名稱只有搜尋摘要，選單與步驟沒有逐字查核，請以你的畫面為準**。
參考：https://support.apple.com/zh-hk/108784 。

規則先由全家說好，設定只是幫忙提醒；設定不能取代「為什麼要這樣做」的對話。

## 求助管道（寫進公約第五條）

| 找誰 | 什麼時候 |
|---|---|
| 爸爸媽媽 | 第一個找的人 |
| 老師、學校輔導老師 | 在學校遇到的事 |
| iWIN 網路內容防護機構 02-2577-5118 | 看到不當的網路內容 |
| 165 反詐騙專線 | 有人要錢、說你中獎、要你匯款 |

iWIN 專線與 165 來自本系列先前課次（2026-10-07／08）的查核，本次沒有重讀官方網站；撥打前可先上網確認。

## 隱私

這堂課不需要任何帳號、照片、真實姓名或地址。公約上可以寫「爸爸」「我」，不必寫全名；公約貼在家裡，不拍照上傳。
''',

'01_規則競速與協商.md': '''# 規則競速與協商：規則

## 第一回合：規則競速（八分鐘）

1. 拿出列印包第 2 頁（孩子）和第 3 頁（爸爸）的規則卡，沿虛線剪開，各五張。
2. 每張卡已經印好一個主題：使用時間、花錢、隱私、作業和 AI、求助。**每個主題寫一條。**
3. 計時八分鐘。兩個人同時寫，每張卡寫「規則」和「理由」兩行。
4. 先寫完五張的人喊「完成」，可以先念第一張；時間到還沒寫完的卡，空著也沒關係，第二回合一起想。
5. 競速只比寫的速度，**不比誰的規則比較多被採用**。

## 第二回合：一條一條協商（不計時）

依主題順序，一次拿出同一個主題的兩張卡（你的和爸爸的）：

1. 兩個人各念一次自己的卡，說出理由。
2. 用三個條件檢查，在 `03_規則協商表` 打勾：
   - 說得清楚：寫出誰、什麼時候、做什麼了嗎？
   - 做得到：兩個人都同意嗎？真的做得到嗎？
   - 檢查得到：一看就知道有沒有做到嗎？
3. 沒過的地方一起改：說不清楚的改清楚，做不到的改小一點，檢查不到的加上看得到的動作（例如「鬧鐘響了就存檔關機」）。
4. 兩個人都同意，才寫進「改成（協商後）」；再一起寫「沒做到時怎麼補救」。
5. 吵不出結果的，寫進協商表最下面的「下一版再談」，不要硬寫進 v1.0。

## 加分（不是必須）

- 有一條規則是管爸爸的。
- 有一條規則寫的是「要做什麼」，不只是「不可以」。
- 每一條都有補救方法，而且補救不是處罰。
''',

'03_規則協商表_填寫說明.md': '''# 規則協商表怎麼寫

`03_規則協商表.csv` 可以用 Numbers 或試算表打開，也可以照列印包第 4 頁手寫。

| 欄位 | 寫什麼 |
|---|---|
| 編號、誰提的、主題 | 已經填好：孩子五條、爸爸五條，每個主題各一條 |
| 原本的規則 | 照規則卡抄，不要先改 |
| 說得清楚／做得到／檢查得到 | 過了寫 ✓，沒過寫 ✗ |
| 理由 | 為什麼要這條規則 |
| 沒做到時怎麼補救 | 怎麼補回來，不是處罰 |
| 改成（協商後） | 兩個人都同意的版本 |
| 兩人都同意 | 都同意寫 ✓；沒談好寫「下一版再談」 |

最後一列「自選規則或功能」留給下半場：寫你加了什麼、請爸爸試一次之後保留、修改還是拿掉。
''',

'04_五個主題解說.md': '''# 五個主題解說（爸爸用）

**請在競速之後再看「範例規則」。**先讓孩子自己寫，範例只拿來比較，不拿來抄。

## 暖身題參考答案（列印包第 1 頁）

| 模糊的規則 | 哪個條件沒過 | 一種改法 |
|---|---|---|
''' + ''.join(f'| {a} | {b} | {c} |\n' for a, b, c in WARMUP) + '''
改法不只一種；孩子的版本只要三個條件都過，就是對的。

## 好規則的三個條件

''' + ''.join(f'- **{n}**：{d}\n' for n, d in CONDITIONS) + '''- 每一條另外寫**理由**和**沒做到時怎麼補救**。

## 五個主題與範例規則

''' + ''.join(f'''### {t}

- 範例規則：{EXAMPLES[t][0]}
- 理由：{EXAMPLES[t][1]}
- 沒做到時：{EXAMPLES[t][2]}

''' for t in TOPICS) + '''## 每個主題容易錯的地方

- **使用時間**：只寫「不要太久」，沒有寫幾分鐘、在哪裡、時間到怎麼停。分鐘數由家裡協商，本課不提供建議值。
- **花錢**：以為免費的遊戲就不會花錢。遊戲裡的點數、寶石、會員常常要用真的錢買，下載新遊戲前也先問。
- **隱私**：只想到自己的資料，忘了別人的照片也不能亂傳；密碼連好朋友也不告訴。
- **作業和 AI**：把它寫的內容直接當成自己的作業交出去；忘了它會說錯；沒有照老師規定註明用了什麼工具、用在哪裡。
  老師說不能用，就不用。依據：教育部「中小學使用『生成式人工智慧』注意事項 2.1」學生版六（三）、六（四）。
- **求助**：怕被罵所以不說。公約第五條也要寫給爸爸：孩子來求助，先一起處理，不先罵人。
''',

'05_自選規則與功能.md': '''# 孩子獨立改造：家庭科技公約 v1.0

## 1. 整理成公約（列印包第 5 頁）

把協商表裡「兩人都同意」的規則，依五個主題抄進公約。每一條旁邊寫理由和沒做到時怎麼補救。
寫不下就寫重點；字要讓全家都看得懂。

## 2. 加一個自選規則或功能

選一個，或自己想：

- **每週檢查表**（列印包第 6 頁）：每天晚上替五個主題打勾，週末一起看哪一條最難做到。
- **修改規則的方法**：寫一條「規則做不到的時候，全家怎麼一起修改」，例如每個月第一個星期六開會、改了就把版本號加一（v1.1）。
- **新的主題**：例如「睡前」「出門在外」「玩線上遊戲時跟誰說話」。
- **好行為的獎勵**：例如一週都做到，週末選一部全家一起看的影片。

## 3. 請爸爸試一次

請爸爸照著你的自選規則或功能做一次（例如真的打一天的勾）。做完之後問自己：

- 爸爸看得懂嗎？
- 做得到嗎？
- 看得出有沒有做到嗎？

三題都是「是」就保留；有一題不是，就改一改再試一次。把結果寫在協商表最後一列。

## 4. 命名與存檔

- 名稱：`L014_家庭科技公約_v1.0`，寫上日期。
- 全家簽名，貼在看得到的地方。不拍照上傳、不寫全名和住址。
- 過一陣子（例如一個月後、寒暑假前）再一起檢查，改好的版本叫 v1.1。
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（依課表）

- [ ] 完成「家庭科技公約 v1.0」：五個主題、每條的理由、沒做到時的補救、全家簽名、日期。
- [ ] 能不用看稿說出核心原理：好規則的三個條件（說得清楚、做得到、檢查得到），並挑一條公約說明它為什麼做得到。
- [ ] 能指出至少一個錯誤、限制或安全注意事項，例如：
  - 規則太模糊，像「不要玩太久」，就沒辦法檢查。
  - 規則做不到，像「永遠不碰手機」，很快就沒人遵守。
  - 家長控制功能只是幫手，不能取代全家說好的約定。
  - 看起來免費的遊戲，裡面也可能要付錢。
  - 遇到有人要錢、要照片、叫你保密，馬上告訴爸爸媽媽。

## 角色互換（105–115）

孩子當老師，爸爸當學生：

1. 孩子說出三個條件。
2. 爸爸拿一條模糊的規則（例如「要乖乖的」）請孩子改，孩子說出哪個條件沒過、怎麼改。
3. 孩子挑公約裡一條，說明它為什麼做得到、怎麼檢查。

## 錄音四問（115–120，錄音只留在家裡）

1. 我們家的科技公約在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 課後延伸（15–30 分鐘）

自由改造公約，或做一週的檢查表；寫三句學習日誌：我做了什麼、哪裡卡住、下次想加什麼（列印包第 6 頁）。
''',

'07_公約小抄.md': '''# L014 公約小抄

## 好規則的三個條件

''' + ''.join(f'{i}. **{n}**：{d}\n' for i, (n, d) in enumerate(CONDITIONS, 1)) + '''
每一條都寫：**理由**、**沒做到時怎麼補救**。

## 五個主題

''' + ''.join(f'- {t}\n' for t in TOPICS) + '''
## 三句話記住

- 先各自提出，再一起協商，最後寫下來。
- 爸爸的規則也算數，大人也要遵守。
- 越早說，越容易處理。
''',
}

SHEET_HEADER = ['編號', '誰提的', '主題', '原本的規則', '說得清楚', '做得到', '檢查得到', '理由', '沒做到時怎麼補救', '改成（協商後）', '兩人都同意']
SHEET_ROWS = ([[f'孩子{i}', '孩子', t] for i, t in enumerate(TOPICS, 1)] + [[f'爸爸{i}', '爸爸', t] for i, t in enumerate(TOPICS, 1)]
              + [['自選', '孩子', '自選規則或功能'], ['下一版再談', '', '']])

EXTRA_CSS = '''.cond{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-bottom:5mm}.cond div{border:1.4pt solid #0b2540;border-radius:3mm;padding:3mm 4mm}
.cond b{display:block;font-size:15pt;color:#1c6f9a}.cond span{font-size:10pt}
.warm{table-layout:fixed}.warm td{height:21mm;font-size:11.5pt}.warm td.v{font-weight:700;font-size:13pt;vertical-align:middle;background:#f6fafd}
.rc{border:1.5pt dashed #0b2540;border-radius:3mm;padding:2.5mm 5mm;margin-bottom:3.5mm}
.rc h3{font-size:14pt;margin:0 0 1mm}.rc h3 span{font-size:10pt;color:#4a6a88;font-weight:400;margin-left:3mm}.rc p{margin:.5mm 0 0;font-size:11pt}.rc .line{height:8.5mm}
.neg{table-layout:fixed}.neg th{font-size:9.5pt;text-align:center;padding:1mm}.neg td{height:16.5mm;font-size:9.5pt;padding:1mm}.neg td.c{text-align:center}
.pact{border:2pt solid #0b2540;border-radius:4mm;padding:4mm 6mm;height:248mm}.pact h3{font-size:18pt;text-align:center;margin:0 0 1mm}
.pact .t{border-top:1pt solid #9db7cc;padding-top:1.5mm;margin-top:1.8mm}.pact .t b{font-size:12pt;color:#1c6f9a}.pact .t .line{height:7.5mm}.pact .t p{margin:.5mm 0 0;font-size:9.5pt;color:#35506b}
.sign{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm;margin-top:3mm;font-size:11pt}.sign div{border-bottom:1pt solid #0b2540;height:11mm}
.week{table-layout:fixed}.week th{text-align:center;font-size:10.5pt}.week td{height:11mm}.week td.n{font-size:10.5pt;font-weight:700}
.help{margin-top:4mm}.help td{font-size:10.5pt}
.log .line{height:9mm}'''


def html():
    pages = []
    cond = '<div class="cond">' + ''.join(f'<div><b>{i}. {n}</b><span>{d}</span></div>' for i, (n, d) in enumerate(CONDITIONS, 1)) + '</div>'
    warm = ''.join(f'<tr><td class="v">{a}</td><td></td><td></td></tr>' for a, _, _ in WARMUP)
    pages.append('<h2>好規則的三個條件</h2><p class="lead">每一條規則都要過三關；另外寫上理由，和沒做到的時候怎麼補救。</p>' + cond
        + '<h3>暖身題：把模糊的規則改成做得到</h3><p class="note" style="margin:0 0 2mm">說出哪一個條件沒過，再寫一種改法。改法不只一種。</p>'
        '<table class="warm"><tr><th style="width:24%">模糊的規則</th><th style="width:30%">哪個條件沒過？</th><th>我的改法</th></tr>' + warm + '</table>'
        '<div class="box" style="margin-top:5mm"><h3 style="font-size:13pt">五個主題</h3><p style="margin:0;font-size:12pt">'
        + '　・　'.join(TOPICS) + '</p><p class="note" style="margin:1.5mm 0 0">公約三步驟：各自提出 → 一起協商 → 寫下來、全家簽名。</p></div>')

    def cards(who):
        return (f'<h2>規則卡：{who}的五條</h2><p class="lead">沿虛線剪開。規則競速：計時八分鐘，每個主題寫一條。</p>'
                + ''.join(f'<div class="rc"><h3>{t}<span>{who}寫的</span></h3><p>規則：</p><div class="line"></div><div class="line"></div>'
                          f'<p style="margin-top:2.5mm">理由：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p></div>' for t in TOPICS))
    pages.append(cards('孩子'))
    pages.append(cards('爸爸'))

    neg = ''.join(f'<tr><td class="c">{r[0]}</td><td class="c">{r[2]}</td><td></td><td class="c">□</td><td class="c">□</td><td class="c">□</td><td></td><td class="c">□</td></tr>'
                  for r in SHEET_ROWS[:10])
    pages.append('<h2>協商紀錄</h2><p class="lead">一次拿出同一個主題的兩張卡，說出理由，用三個條件檢查；兩個人都同意才寫進去。</p>'
        '<table class="neg"><tr><th style="width:9%">編號</th><th style="width:12%">主題</th><th style="width:20%">原本的規則</th><th style="width:7%">說得<br>清楚</th>'
        '<th style="width:7%">做得到</th><th style="width:7%">檢查<br>得到</th><th>改成（協商後）</th><th style="width:7%">都<br>同意</th></tr>' + neg + '</table>'
        '<p style="margin:3mm 0 1mm;font-size:11pt"><b>下一版再談：</b></p><div class="line"></div>')

    sections = ''.join(f'<div class="t"><b>{i}. {t}</b><div class="line"></div><div class="line"></div>'
                       f'<p>理由：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿　沒做到時：＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p></div>' for i, t in enumerate(TOPICS, 1))
    pages.append('<div class="pact"><h3>我們家的科技公約 v1.0</h3><p class="note" style="text-align:center;margin:0">全家一起討論、一起答應、一起遵守。大人也要遵守。</p>'
        + sections + '<div class="t"><b>6. 我加的自選規則或功能</b><div class="line"></div></div>'
        '<p style="font-size:10.5pt;margin:2.5mm 0 0">下次一起檢查的日期：＿＿＿＿＿＿　改好的版本叫 v1.1　　訂立日期：＿＿＿＿＿＿</p>'
        '<div class="sign"><span>孩子簽名</span><span>爸爸簽名</span><span>其他家人簽名</span><div></div><div></div><div></div></div>'
        '<p class="note" style="margin:2mm 0 0">名稱：L014_家庭科技公約_v1.0　不寫全名、住址，不拍照上傳。</p></div>')

    days = ['一', '二', '三', '四', '五', '六', '日']
    week = ''.join(f'<tr><td class="n">{t}</td>' + '<td></td>' * 7 + '</tr>' for t in TOPICS)
    helps = ''.join(f'<tr><td style="width:38%"><b>{a}</b></td><td>{b}</td></tr>' for a, b in HELP)
    pages.append('<h2>每週檢查表和求助卡</h2><p class="lead">自選功能範例：每天晚上替五個主題打勾，週末一起看哪一條最難做到。</p>'
        '<table class="week"><tr><th style="width:22%">主題</th>' + ''.join(f'<th>{d}</th>' for d in days) + '</tr>' + week + '</table>'
        '<p style="font-size:11pt;margin:2mm 0 0">這週最難做到的是：＿＿＿＿＿＿　要不要改？□ 不用　□ 下一版改成：＿＿＿＿＿＿＿＿＿＿</p>'
        '<div class="cut help"><h3>求助卡<small>看到害怕、不舒服的東西，或有人要錢、要照片、叫你保密</small></h3>'
        '<table>' + helps + '</table>'
        '<p class="note" style="margin:2mm 0 0">越早說，越容易處理。爸爸答應：先一起處理，不先罵人。　爸爸簽名：＿＿＿＿＿＿</p>'
        '<p class="note" style="margin:1mm 0 0">專線號碼來自本系列先前的查核；撥打前可以先上網確認。</p></div>'
        '<div class="log" style="margin-top:4mm"><h3>學習日誌</h3><p style="margin:0">我做了什麼：</p><div class="line"></div>'
        '<p style="margin:1mm 0 0">哪裡卡住：</p><div class="line"></div><p style="margin:1mm 0 0">下次想加什麼：</p><div class="line"></div></div>')
    return printpack.document('L014 我們家的科技公約 列印包', '父子科技學院 L014｜我們家的科技公約', pages, EXTRA_CSS)


if __name__ == '__main__':
    classroom_pack.build(
        slug='l014-family-tech-pact', folder='L014_我們家的科技公約', files=FILES,
        sheet=('03_規則協商表.csv', SHEET_HEADER, SHEET_ROWS),
        pack_html=html(), pack_pdf='02_列印包_科技公約.pdf', pack_pages=6,
        pack_needles=('好規則的三個條件', '暖身題', '規則卡：孩子的五條', '規則卡：爸爸的五條', '協商紀錄', '我們家的科技公約 v1.0', '每週檢查表', '求助卡', '學習日誌'),
        authoring_dir=Path(__file__).resolve().parent,
        extra={'ruleCards': {'child': 5, 'father': 5, 'onePerTopic': True}, 'topics': TOPICS,
               'warmUpVagueRules': len(WARMUP), 'exampleRulesPerTopic': 1,
               'minutesInExamplesAreNotAdvice': True, 'needsChildAccount': False, 'needsAiTool': False,
               'helpLines': 'iWIN 02-2577-5118 and 165, from earlier lessons\' source checks (not re-read 2026-10-19)',
               'parentalControlNames': 'Screen Time / Family Sharing / Ask to Buy from web-search summaries only; parent told to follow own screen'})
