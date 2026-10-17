"""Build the SP002 family discussion pack (no account, no install, no private data).

    ./portable-runtime.sh python authoring/sp002/classroom.py

Facts come from the public FamilyRecorder repo (commit ff76063), see source-notes.md.
After any change here: rerun pipeline/delivery.py, then verify.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import classroom_pack  # noqa: E402
import printpack  # noqa: E402

REPO = 'https://github.com/pcpcchen-coder/FamilyRecorder'

# One sentence's journey, in the correct order (letters are printed shuffled on the card sheet).
JOURNEY = [
 ('有人在客廳說：明天記得去拿包裹。', '晚上 7:40'),
 ('守門：這 30 秒有人在說話嗎？有，所以留下來。', '馬上'),
 ('Mac 用 Whisper 在本機把話變成文字，不用上網。', '幾分鐘內'),
 ('寫進當天的逐字稿：時間、可能是誰、聲音方向。', '幾分鐘內'),
 ('整理程式把前一天的逐字稿文字送去整理成摘要。', '半夜 00:10'),
 ('打開摘要，在待辦事項看到：明天拿包裹。', '早上'),
]
SHUFFLE = [3, 0, 5, 2, 4, 1]          # printed order of the cards (index into JOURNEY)
LETTERS = 'ABCDEF'
assert sorted(SHUFFLE) == list(range(6)) and SHUFFLE != list(range(6))
ANSWER = ''.join(LETTERS[SHUFFLE.index(i)] for i in range(6))
DETOUR = '岔路卡：如果這 30 秒很安靜呢？→ 不存聲音檔、不送去辨識，只留下幾個數字紀錄。'

# Where each kind of data goes (docs/privacy.md, README privacy table).
DATA = [
 ('原始聲音檔', '留在家', 'audio/ 資料夾，預設保留 7 天', '從不上傳'),
 ('聲音特徵', '留在家', 'speaker-profiles/，權限只有自己能讀', '用 15 秒樣本算出來；樣本錄音會丟掉，只留特徵，而且不能還原成聲音'),
 ('聲音方向的角度', '留在家', '資料庫的 acoustic_samples 表', '從不上傳'),
 ('資料庫', '留在家', 'listener.sqlite3', '從不上傳'),
 ('被攔下的句子', '留在家', '資料庫的 transcription_audits 表', '不進逐字稿，所以也不會送去整理'),
 ('每日摘要', '留在家', 'summaries/ 資料夾', '在雲端整理好、存回 Mac；這是產出'),
 ('逐字稿文字', '會出門', 'transcripts/ 資料夾', '每天一次，送到自己的 ChatGPT 帳號；可以關掉'),
 ('行事曆候選事件', '會出門（有開才會）', '資料庫的 calendar_candidates 表', '只在開啟行事曆功能時，候選的標題、時間和成員名，經由行事曆 App 寫進自己的 Google 帳號'),
]
OUT = [d[0] for d in DATA if d[1].startswith('會出門')]
assert OUT == ['逐字稿文字', '行事曆候選事件']

AGREEMENT = [
 '所有可能被錄到的人都知道，而且同意（訪客、家教老師、維修人員也算）。',
 '收音是看得見的：麥克風放在看得到的地方，必要時貼上「正在收音」。',
 '每個人都知道怎麼暫停（選單列可以暫停 15 分鐘、1 小時，或直到手動恢復）。',
 '開啟每天的雲端摘要之前，全家再確認一次：逐字稿文字會離開這台 Mac。',
 '小孩由爸媽同意，而且小孩自己也知道。',
 '不拿來監控任何人，也不拿逐字稿當吵架的證據。',
 '臥室、浴室、客人來訪的時候，先暫停或不收。',
]

FILES = {
'00_爸爸先讀.md': f'''# 父子科技學院 SP002 番外篇：FamilyRecorder（爸爸先讀）

這是番外篇，依 FamilyRecorder 公開的程式與文件製作的介紹，**不是實際使用錄音**，影片和這份討論包裡沒有任何真實逐字稿或家人資料。
例句「明天記得去拿包裹」是專案 README 裡的範例。

## 這份討論包在做什麼

看完影片，用兩個小遊戲把「它怎麼運作」「資料去哪裡」弄清楚，最後全家一起討論：如果我們家要裝，要先約好什麼。
不需要任何帳號，也不需要真的安裝。全程約 30–45 分鐘。

| 分鐘 | 做什麼 |
|---|---|
| 0–7 | 一起看影片（約 6 分鐘） |
| 7–17 | 遊戲一：一句話的旅程（列印包第 1 頁，排序卡） |
| 17–27 | 遊戲二：資料去哪裡？（列印包第 2 頁，分類卡） |
| 27–45 | 討論三個問題，寫下我們家的收音約定（列印包第 3 頁、`01_家庭討論卡.md`） |

## 課前準備（約 5 分鐘）

1. 列印 `02_列印包_家庭討論包.pdf`（A4，共 3 頁，單面）。第 1、2 頁的卡片沿虛線剪下。
2. 讀一遍 `04_解答與解說.md`。
3. 想展示你自己的安裝畫面也可以；但逐字稿裡可能有其他家人的話，**給孩子看之前，先問過被錄到的人**。

## 幾個重點的出處

- 定位、需求、隱私承諾表、產出範例：README.md
- 什麼資料去哪裡、安靜時不存聲音、自我驗證指令、明確禁止的用途：docs/privacy.md
- 15 秒樣本、音色與方向是兩份獨立證據、不是身分驗證：docs/speakers.md
- 家教複習、夢境記錄等用途與倫理檢查：docs/use-cases.md
- 每天 00:10 整理前一天、30 秒一段：config.example.yaml
- 摘要用唯讀、用完就丟的暫時環境：src/family_recorder/summary.py

以上都在 {REPO}（查核日 2026-10-17，commit ff76063）。

## 誠實說明

- 這份教材只根據文件與程式碼；製作時沒有安裝或執行，也沒有實測辨識準確度。
- 文件自己寫明「不防護」的情形：能用這台 Mac 的人、Time Machine 或 iCloud 備份、送到 ChatGPT 之後的逐字稿文字。
- 文件與程式有兩處小出入：pyproject 版本是 0.16.0，README 仍寫 0.14.4；docs/privacy.md 說 summary.py 只 import config 與 storage、515 行，
  目前程式多 import 了 history（自述沒有音訊、網路或摘要用戶端存取）、共 522 行。影片沒有引用這些細節。
''',

'01_家庭討論卡.md': '''# 家庭討論卡：帶回家的三個問題

影片最後留了三個問題。每個人都說一次，爸爸最後說。沒有標準答案。

## 一、哪些話值得被記住？哪些話，你希望它不要記？

- 想想看：家裡最常忘記的是哪一種話？（約定、待辦、靈感、叮嚀……）
- 有沒有哪些時候，你一點都不想被記下來？
- 如果一句話被記下來，但寫錯了字，會發生什麼事？（想想第十二堂的幻覺）

## 二、要在家裡收音，每個人都同意了嗎？客人來的時候怎麼辦？

- 「同意」要怎麼問，才算真的同意？可以說不嗎？
- 爺爺奶奶、同學、家教老師來家裡，要怎麼讓他們知道？
- 夢話、睡覺時說的話算不算本人想說的話？

## 三、大家都知道怎麼按暫停嗎？

- 誰負責教其他人暫停？
- 哪些時間或房間，一定要先暫停？
- 如果有人忘了暫停，要怎麼處理錄到的東西？

## 記下我們的決定

把討論的結果寫在列印包第 3 頁「我們家的收音約定」。下一堂正課 L014「我們家的科技公約」，可以把它放進公約裡。
''',

'03_資料去哪裡_說明.md': '''# 資料去哪裡（表格說明）

`03_資料去哪裡.csv` 可以用 Numbers 或任何試算表開啟。它是遊戲二的完整答案表，整理自專案文件 docs/privacy.md 和 README 的隱私承諾表。

- **資料**：系統會產生或保存的東西。
- **去哪裡**：留在家（這台 Mac）或會出門。
- **存在哪裡**：資料夾或資料庫的表名。
- **說明**：保留多久、什麼條件下才會出門。

重點只有一句：**聲音不出門；每天只有逐字稿的文字出門一次，而且可以關掉。** 行事曆功能預設是關的，開了才會把候選事件寫進自己的行事曆。
''',

'04_解答與解說.md': f'''# 解答與解說（爸爸用）

## 遊戲一：一句話的旅程

卡片印出來的順序是打亂的。正確順序是：**{' → '.join(ANSWER)}**

''' + ''.join(f'{i}. （{LETTERS[SHUFFLE.index(i - 1)]}）{JOURNEY[i - 1][0]}　{JOURNEY[i - 1][1]}\n' for i in range(1, 7)) + f'''
{DETOUR}

可以追問：

- 哪一步之後，資料第一次離開這台 Mac？（第 5 步；而且只有文字）
- 「幾分鐘內」是本教材的說法，文件沒有給精確時間；辨識要花多久，要看電腦和模型。
- 如果第 2 步的守門判斷錯了，把冷氣聲當成人在說話，後面會發生什麼？（防幻覺的關卡會再擋一次；擋下來的寫進檢查紀錄）

## 遊戲二：資料去哪裡？

| 資料 | 去哪裡 | 說明 |
|---|---|---|
''' + ''.join(f'| {d[0]} | {d[1]} | {d[3]} |\n' for d in DATA) + '''
可以追問：

- 為什麼聲音特徵不出門也很重要？（它是你的聲音的「指紋」，文件寫明不上傳，而且不能還原成聲音）
- 每日摘要是在雲端整理的，為什麼還算「留在家」？（整理好的結果存回這台 Mac；文件把它列為產出）
- 有沒有辦法讓逐字稿文字也不出門？（可以，把每天的雲端摘要關掉，整套就完全離線，只是沒有摘要）

## 討論時可以補充的事實

- 逐字稿寫的是「可能說話者」，不是確認身分；不能拿來開門、付款，也不能當證據。
- 專案不提供偷偷錄音的功能，也明確寫著不能用來監控任何人。
- 文件附了指令，讓人自己檢查安靜時是不是真的沒存聲音檔：這叫「能檢查，才可信」。
''',

'05_和孩子一起讀專案.md': f'''# 和孩子一起讀專案（延伸，15–20 分鐘）

打開 {REPO}，一起找下面這些東西。找到一個就打勾。

- [ ] README 最上面的一句話：它想把什麼留下來？
- [ ] 「一般雲端錄音服務」和 FamilyRecorder 的比較表：找出「雲端拿到什麼」那一列。
- [ ] 黃色或紅色框的 IMPORTANT 提醒：使用前要先做什麼？
- [ ] 系統總覽的圖：找出寫著「這一整層完全離線」的那一塊。
- [ ] 「產出長什麼樣」：逐字稿範例裡，說話者前面寫的是哪兩個字？（可能）
- [ ] docs/privacy.md 的「明確非目標」：找出一項它刻意不做的事。
- [ ] docs/use-cases.md：除了家庭日誌，還有哪兩個場景？

讀完問孩子：

1. 你覺得這個專案最聰明的設計是哪一個？
2. 如果你來寫，你會加什麼功能？那個功能會不會讓別人不舒服？
3. 為什麼文件要寫「刻意不做」的事？

提醒：GitHub 上的程式和文件是公開的，但**不要**在 issue 或任何公開地方貼家裡的逐字稿。
''',
}

SHEET_HEADER = ['資料', '去哪裡', '存在哪裡', '說明']
SHEET_ROWS = [[d[0], d[1], d[2], d[3]] for d in DATA]

EXTRA_CSS = '''.cards{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:3mm}.jc{height:46mm;padding:5mm 6mm;position:relative}
.jc b{position:absolute;top:2.5mm;right:4mm;font-size:20pt;color:#35a9d6}.jc p{margin:7mm 10mm 0 0;font-size:15pt;line-height:1.6}
.detour{height:auto;margin-top:5mm;padding:4mm 6mm;font-size:12pt;border-color:#f0a020}
.order{margin-top:7mm;font-size:14pt}.order span{display:inline-block;width:13mm;height:13mm;border:1.2pt solid #7f9bb3;border-radius:2mm;margin-right:3mm;vertical-align:middle}
.dc{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:3mm;margin-top:2mm}.dc div{height:24mm;padding:2.5mm 3mm;font-size:13pt;font-weight:700;display:flex;align-items:center;justify-content:center;text-align:center}
.zones{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:6mm}.zone{height:150mm;border:2pt solid #0b2540;border-radius:4mm;padding:4mm 5mm}
.zone h3{font-size:16pt;margin:0}.zone p{font-size:10.5pt;color:#35506b;margin:1mm 0 0}.zone.out{border-color:#f0a020}
.ag li{margin:3.2mm 0;font-size:13pt;list-style:none}.ag li:before{content:"□ ";font-size:13pt}.ag{padding-left:2mm;margin:2mm 0 4mm}
.dec{border:1.6pt solid #0b2540;border-radius:3mm;padding:4mm 6mm;margin-top:3mm}.dec p{margin:3.4mm 0;font-size:13pt}'''


def html():
    pages = []
    card = lambda k: (f'<div class="cut jc"><b>{LETTERS[k]}</b><p>{JOURNEY[SHUFFLE[k]][0]}</p></div>')
    pages.append('<h2>遊戲一：一句話的旅程</h2><p class="lead">沿虛線剪下六張卡，排出這句話從客廳走到早上的順序。卡片上的英文字母是打亂的。</p>'
        '<div class="cards">' + ''.join(card(k) for k in range(6)) + '</div>'
        f'<div class="cut detour">{DETOUR}</div>'
        '<p class="order">我排的順序：' + '<span></span>' * 6 + '</p>'
        '<p class="note">想一想：排到第幾張卡的時候，資料第一次離開這台 Mac？離開的是聲音，還是文字？</p>')

    pages.append('<h2>遊戲二：資料去哪裡？</h2><p class="lead">剪下八張資料卡，放進下面兩個框：留在家裡的 Mac，或是會出門。放好再對答案。</p>'
        '<div class="dc">' + ''.join(f'<div class="cut">{d[0]}</div>' for d in DATA) + '</div>'
        '<div class="zones"><div class="zone"><h3>留在家裡的 Mac</h3><p>從不上傳</p></div>'
        '<div class="zone out"><h3>會出門</h3><p>什麼時候出門？出門去哪裡？寫在卡片旁邊</p></div></div>'
        '<p class="note" style="margin-top:3mm">提示：聲音從頭到尾都不出門。</p>')

    pages.append('<h2>我們家的收音約定</h2><p class="lead">如果我們家要裝這樣的東西，先一起確認下面每一項。這張紙只留在家裡。</p>'
        '<ul class="ag">' + ''.join(f'<li>{x}</li>' for x in AGREEMENT) + '</ul>'
        '<div class="dec"><h3 style="margin:0 0 1mm">我們的決定</h3>'
        '<p>□ 先不裝　　□ 先試一週再說　　□ 只在＿＿＿＿＿＿＿＿裡收音</p>'
        '<p>一定要先暫停的時間或地方：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>每天的雲端摘要：□ 開　□ 關　　負責教大家按暫停的人：＿＿＿＿＿＿</p>'
        '<p>我們最想記住的一種話：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>討論日期：＿＿＿＿＿＿　　全家都同意了：□</p></div>'
        '<div class="dec"><h3 style="margin:0 0 1mm">換你當設計師</h3><p>如果由你來寫這個專案，你會再加一個什麼保護？</p>'
        '<div class="line"></div><div class="line"></div></div>'
        '<p class="note" style="margin-top:3mm">下一堂正課 L014「我們家的科技公約」，可以把這張約定放進公約裡。</p>')
    return printpack.document('SP002 FamilyRecorder 家庭討論包 列印包', '父子科技學院 SP002 番外篇｜FamilyRecorder 家庭討論包', pages, EXTRA_CSS)


if __name__ == '__main__':
    classroom_pack.build(
        slug='sp002-familyrecorder', folder='SP002_FamilyRecorder家庭討論包', files=FILES,
        sheet=('03_資料去哪裡.csv', SHEET_HEADER, SHEET_ROWS),
        pack_html=html(), pack_pdf='02_列印包_家庭討論包.pdf', pack_pages=3,
        pack_needles=('一句話的旅程', '岔路卡', '資料去哪裡', '留在家裡的 Mac', '會出門', '我們家的收音約定', '我們的決定'),
        authoring_dir=Path(__file__).resolve().parent, episode_dir='specials/sp002-familyrecorder',
        extra={'activityMinutes': '30-45', 'needsAccount': False, 'needsInstall': False,
               'journeyCards': 6, 'journeyAnswer': ANSWER, 'dataCards': len(DATA), 'dataThatLeaves': OUT,
               'factsFrom': 'FamilyRecorder README, docs/privacy.md, docs/speakers.md, docs/use-cases.md, config.example.yaml (commit ff76063)'})
