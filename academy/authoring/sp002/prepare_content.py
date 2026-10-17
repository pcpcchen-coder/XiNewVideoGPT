"""SP002 番外篇：FamilyRecorder — production sources (12 scenes / 36 sentences).

    ./portable-runtime.sh python authoring/sp002/prepare_content.py

Everything said here comes from the public repo pcpcchen-coder/FamilyRecorder at commit ff76063
(see source-notes.md). No real recording, transcript or family data is shown or quoted.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import special_builder  # noqa: E402

SPECIAL, SLUG, CHECKED = 'SP002', 'sp002-familyrecorder', '2026-10-17'
TITLE = 'FamilyRecorder：家裡的當下記錄器'
REPO = 'https://github.com/pcpcchen-coder/FamilyRecorder'
AT = REPO + '/blob/ff76063ab82fc3884bfe898f45a010372d97607d/'
SRC = {
    'readme': AT + 'README.md',
    'use_cases': AT + 'docs/use-cases.md',
    'privacy': AT + 'docs/privacy.md',
    'speakers': AT + 'docs/speakers.md',
    'getting_started': AT + 'docs/getting-started.md',
    'daily_summary': AT + 'docs/daily-summary.md',
    'menu_bar': AT + 'docs/menu-bar.md',
    'config': AT + 'config.example.yaml',
    'summary_py': AT + 'src/family_recorder/summary.py',
    'next_lesson': 'lessons/L014/lesson.json',
}
SOURCE_RECORDS = [
    {'id': 'readme', 'title': 'FamilyRecorder README（繁體中文）', 'publisher': 'pcpcchen-coder/FamilyRecorder', 'url': SRC['readme'],
     'usedFor': '定位、標語、需求、三步驟、核心功能、隱私承諾表、逐字稿與摘要範例、同意提醒'},
    {'id': 'use_cases', 'title': '應用場景指南', 'publisher': 'pcpcchen-coder/FamilyRecorder', 'url': SRC['use_cases'],
     'usedFor': '當下記錄器；家庭日誌已完整實作；家教複習與夢境記錄換 prompt 即可；倫理檢查'},
    {'id': 'privacy', 'title': '隱私與信任邊界', 'publisher': 'pcpcchen-coder/FamilyRecorder', 'url': SRC['privacy'],
     'usedFor': '什麼資料去哪裡；安靜時不存 WAV；「能被驗證，而不是被承諾」；自我驗證指令；明確禁止的用途'},
    {'id': 'speakers', 'title': '家庭成員與方向', 'publisher': 'pcpcchen-coder/FamilyRecorder', 'url': SRC['speakers'],
     'usedFor': '15 秒樣本；音色與方向是兩份獨立證據；不是身分驗證'},
    {'id': 'getting_started', 'title': '安裝與上手', 'publisher': 'pcpcchen-coder/FamilyRecorder', 'url': SRC['getting_started'],
     'usedFor': 'Apple Silicon Mac、macOS 13 以上、reSpeaker XVF3800 USB 4-Mic Array'},
    {'id': 'daily_summary', 'title': '每日摘要與行事曆', 'publisher': 'pcpcchen-coder/FamilyRecorder', 'url': SRC['daily_summary'],
     'usedFor': '摘要內容；行事曆候選事件預設逐筆確認'},
    {'id': 'menu_bar', 'title': '選單列與服務管理', 'publisher': 'pcpcchen-coder/FamilyRecorder', 'url': SRC['menu_bar'],
     'usedFor': '暫停 15 分鐘、1 小時或直到手動恢復'},
    {'id': 'config', 'title': 'config.example.yaml', 'publisher': 'pcpcchen-coder/FamilyRecorder', 'url': SRC['config'],
     'usedFor': '30 秒一段；摘要 00:10；防幻覺各層與「不封鎖特定句子」；註冊樣本丟棄只留特徵'},
    {'id': 'summary_py', 'title': 'src/family_recorder/summary.py', 'publisher': 'pcpcchen-coder/FamilyRecorder', 'url': SRC['summary_py'],
     'usedFor': 'Codex 以 --ephemeral、--sandbox read-only、暫存目錄執行；摘要程式沒有讀取音訊的實作'},
    {'id': 'next_lesson', 'title': 'L014 我們家的科技公約（課表）', 'publisher': '父子科技學院課表', 'url': SRC['next_lesson'],
     'usedFor': '結尾預告下一堂正課'},
]

SCENES = [
 ('FamilyRecorder：家裡的當下記錄器', [
  '歡迎回到父子科技學院，我是陳犀牛，今天是番外篇，要介紹爸爸放在網路上的開源專案；這是依專案公開的程式和文件製作的介紹，並非實際使用錄音。',
  '它的名字叫 Family Recorder，翻成中文，就是家庭記錄器。',
  '家裡的一句叮嚀、半夜想到的點子，常常說完幾秒就忘了；它想做的，就是把這些話留下來，而且把隱私放在第一位。'],
  ['readme']),
 ('聽、寫、整理', [
  '它做事只有三個步驟。第一步是聽：桌上的麥克風一直聽，每三十秒切成一小段。',
  '第二步是寫：電腦自己把有人說話的片段變成文字，不用上網。',
  '第三步是整理：每天半夜十二點十分，把前一天的逐字稿整理成摘要，早上起床就能看。'],
  ['readme', 'config']),
 ('需要準備的三樣東西', [
  '要讓它上班，需要準備三樣東西。第一，一支有四個麥克風的陣列，可以聽出聲音從哪個方向來。',
  '第二，一台使用蘋果晶片的 Mac，負責辨識和存檔。',
  '第三，想要每天的摘要，就用官方工具 Codex，登入自己的 ChatGPT 帳號；不需要另外申請程式用的金鑰。'],
  ['getting_started', 'readme']),
 ('四個本事', [
  '它有四個本事。第一是守門：先判斷這三十秒有沒有人在說話；安靜的時候，不存聲音，也不送去辨識。',
  '第二是聽寫：語音辨識程式 Whisper，直接在這台電腦裡，把話變成文字。',
  '第三是防幻覺，第四是認聲音：猜猜看，這段話可能是誰說的、從哪個方向傳來。'],
  ['readme', 'privacy']),
 ('聲音留在家，文字才出門', [
  '一般的雲端錄音服務，會把聲音檔上傳到別人的伺服器去辨識。',
  '這個專案剛好相反：原始聲音、聲音特徵和資料庫，通通留在這台電腦裡。',
  '每天只有一份逐字稿的文字，會送到你自己的帳號去整理；連這個都不想要，也可以關掉摘要，整套變成完全離線。'],
  ['readme', 'privacy']),
 ('防幻覺：還記得第十二堂嗎', [
  '還記得第十二堂的幻覺嗎？語音辨識也會幻覺：房間很安靜，或是只有冷氣在響，它卻可能寫出一句根本沒人說過的話。',
  '所以它設了好幾道關卡：看麥克風硬體有沒有聽到人聲、看背景噪音、看辨識的信心分數，一模一樣的句子一再冒出來也要攔。',
  '被攔下來的句子不會丟掉，而是寫進一份檢查紀錄，事後可以查；而且它不封鎖任何特定的句子。'],
  ['config', 'readme', 'privacy']),
 ('可能是誰？從哪裡來？', [
  '再來是認聲音。每位家人先錄十五秒的聲音樣本，電腦只留下聲音的特徵，那段錄音不保留。',
  '麥克風陣列還會回報，聲音是從哪個角度傳來；音色和方向，是兩份獨立的線索，一起寫在逐字稿上。',
  '所以逐字稿上寫的是可能說話者，而不是確認身分；它不能拿來開門、付款，也不能當成證據。'],
  ['speakers', 'config', 'privacy']),
 ('隱私承諾：能檢查，才可信', [
  '一台一直開著麥克風的電腦，值得相信嗎？這個專案的答案是：要能自己檢查，而不是只聽承諾。',
  '負責摘要的程式裡，根本沒有讀取聲音檔的功能；每次請 Codex 整理，都在唯讀、用完就丟的暫時環境裡進行。',
  '文件裡還附了指令，讓你自己確認，安靜的時候，真的沒有存下任何聲音檔。'],
  ['privacy', 'summary_py']),
 ('換提示詞，換用途', [
  '它的核心，其實是一台當下記錄器；換掉整理用的提示詞，它就能做不同的事。',
  '家庭聲音日誌已經完整做好；家教的課後複習、夢境和半夜靈感的記錄，換一份提示詞，今天就能試。',
  '不過有一件事絕對不行：不能拿它來監控任何人，它也不提供偷偷錄音的功能。'],
  ['use_cases', 'readme', 'privacy']),
 ('早上會看到什麼', [
  '早上起床，你會看到三樣東西。第一是逐字稿，每一段都有時間、可能的說話者和聲音的方向。',
  '第二是每日摘要：事件時間軸、待辦事項，還有一段一百字以內的重點。',
  '第三是行事曆的候選事件，例如下週三的親師座談會；預設要你一筆一筆確認，才會真的加進行事曆。'],
  ['readme', 'daily_summary', 'config']),
 ('一句話的旅程', [
  '我們跟著一句話走一趟。假設晚上七點四十分，有人在客廳說：明天記得去拿包裹。',
  '這三十秒有人說話，所以通過守門，在電腦裡變成文字，寫進當天的逐字稿，標上可能的說話者和方向。',
  '半夜十二點十分，整理程式把它放進前一天的摘要；早上你一打開，就會在待辦事項裡看到它。'],
  ['readme', 'config']),
 ('帶回家的三個問題', [
  '最後，留三個問題給你和家人。第一，哪些話值得被記住？哪些話，你希望它不要記？',
  '第二，要在家裡收音，每個人都同意了嗎？客人來的時候怎麼辦？第三，大家都知道怎麼按暫停嗎？',
  '這些問題，正好是下一堂正課的主題：我們家的科技公約；我是陳犀牛，保持好奇，我們下次見！'],
  ['use_cases', 'menu_bar', 'next_lesson']),
]

VISIBLE = [
 ['番外篇 SP002', 'FamilyRecorder\n家裡的當下記錄器', '聲音留在家，每天只有文字出門一次', '番外篇  ·  依公開專案製作的介紹'],
 ['聽、寫、整理', '每天自動跑一圈',
  '01 聽', '麥克風一直聽\n每 30 秒一段', '→',
  '02 寫', '電腦自己把話\n變成文字', '→',
  '03 整理', '每天 00:10\n整理成摘要',
  '今天的主角：FamilyRecorder'],
 ['需要準備的三樣東西', '麥克風、電腦、帳號',
  '01', '四麥克風陣列', 'XVF3800：聽得出聲音的方向',
  '02', 'Apple 晶片的 Mac', 'macOS 13 以上，負責辨識和存檔',
  '03', 'ChatGPT 帳號', '要每日摘要才需要；不需要 API 金鑰'],
 ['四個本事', '每一段聲音都要過這四關', '四個本事',
  '守門', '有人說話才存', '聽寫', '在本機變成文字', '防幻覺', '攔下沒人說的話', '認聲音', '可能是誰、從哪來',
  '安靜的時候：不存聲音，也不辨識'],
 ['聲音留在家，文字才出門', '和一般雲端錄音服務比一比',
  '一般雲端錄音', '把聲音檔上傳去辨識', '≠', 'FamilyRecorder', '聲音留在 Mac，只送文字',
  '原始聲音、聲音特徵、資料庫：不出門',
  '逐字稿文字每天一次，送到自己的帳號'],
 ['防幻覺：還記得第十二堂嗎？', '安靜的房間，也可能被寫出一句話',
  '01 硬體把關', '麥克風有沒有聽到人聲', '02 看信心分數', '辨識得有沒有把握', '03 攔重複句', '一樣的話一直冒出來',
  '攔下的句子寫進檢查紀錄，不丟掉'],
 ['可能是誰？從哪裡來？', '音色和方向，兩份獨立的線索',
  '15 秒樣本  →  音色特徵  +  方向角度',
  '音色', '像不像已註冊的家人', '方向', '聲音從幾度傳來', '逐字稿', '寫可能說話者',
  '不是確認身分：不能拿來開門、付款或當證據'],
 ['隱私承諾：能檢查，才可信', '一台一直開著麥克風的電腦',
  '一、原始聲音：永遠留在 Mac\n二、聲音特徵：只存在本機\n三、逐字稿文字：每天出門一次',
  '為什麼可以相信？', '摘要程式沒有讀聲音檔的功能', '文件附了指令\n可以自己檢查',
  '先取得每個人的同意，再開始收音'],
 ['換提示詞，換用途', '核心是一台當下記錄器',
  '已完成：家庭聲音日誌', '事件時間軸、待辦\n行事曆候選事件',
  '換提示詞就能試', '家教課後複習\n夢境與半夜靈感',
  '不能用來監控任何人，也不偷偷錄音'],
 ['早上會看到什麼？', '三份產出，存在你的 Mac 裡',
  '01', '逐字稿', '時間、可能說話者、聲音方向',
  '02', '每日摘要', '事件時間軸、待辦、一百字重點',
  '03', '行事曆候選', '一筆一筆確認，才會加進去'],
 ['一句話的旅程', '假設有人說：明天記得去拿包裹',
  '19:40', '客廳說一句話', '30 秒', '守門：有人在說話', '本機', 'Whisper 變成文字',
  '逐字稿', '時間、可能是誰、方向', '00:10', '整理前一天的摘要', '早上', '在待辦事項看到它',
  '番外篇重點：先取得同意，再開始收音'],
 ['帶回家的三個問題', '暫停影片，和家人一起想一想',
  '01', '哪些話值得記住？', '哪些話希望它不要記',
  '02', '每個人都同意了嗎？', '客人來的時候怎麼辦',
  '03', '誰知道怎麼按暫停？', '選單列就能暫停錄音',
  '保持好奇，我們下次見！'],
]

BOARD = [
 ('開場：番外篇揭露、專案名稱與它要解決的問題', '封面版型：標籤、兩行主題、一句說明、番外篇揭露；原陳犀牛角色', '猜猜看：家裡哪些話最容易說完就忘'),
 ('概念：聽、寫、整理三步驟', '三步流程卡＋黃字', '說出三個步驟'),
 ('準備：麥克風陣列、Apple 晶片 Mac、ChatGPT 帳號', '三點條列＋陳犀牛', '找出哪一樣只有要摘要時才需要'),
 ('概念：守門、聽寫、防幻覺、認聲音', '面板四張卡＋黃字', '說出安靜的時候會發生什麼'),
 ('對比：一般雲端錄音 vs 本機辨識、只送文字', '雙框對照＋白字＋黃字', '說出哪些資料不出門'),
 ('連結第十二堂：語音辨識的幻覺與攔截關卡', '三張步驟卡＋黃字', '想一想：為什麼不直接封鎖某些句子'),
 ('認聲音：音色樣本與方向角度，可能說話者不是確認身分', '路徑一行＋三張卡＋黃字', '說出它不能拿來做哪些事'),
 ('隱私：能檢查才可信；摘要程式沒有讀聲音檔的功能', '左三行＋右側「為什麼可以相信？」＋黃字', '說出每天出門的是哪一種資料'),
 ('用途：換提示詞換用途；不能監控、不偷錄', '左右比較卡＋黃字', '想一個你想試的用途'),
 ('產出：逐字稿、每日摘要、行事曆候選', '三點條列＋陳犀牛', '說出行事曆事件怎麼加進去'),
 ('流程：一句話從客廳到早上的待辦事項', '六列時間軸＋黃字', '把六個步驟按順序說一遍'),
 ('討論：三個問題；預告 L014 我們家的科技公約；固定結尾', '三點條列＋陳犀牛＋結尾語', '和家人討論三個問題'),
]

FACT_CHECK = '''# SP002 事實查核

查核日：2026-10-17。查核者：製作代理（Claude）。
方法：clone 公開 repo `pcpcchen-coder/FamilyRecorder`（main，commit `ff76063`，2026-10-03），逐檔閱讀 README、docs 與相關原始碼，
把旁白、投影片與教材逐句對照（筆記見 `source-notes.md`）。
限制：沒有安裝或執行這個專案，沒有接麥克風實測；以下都是「文件與程式寫了什麼」。文件與程式有兩處小出入（版本號、summary.py 的 import 與行數），影片都沒有引用。

## 主張與來源

| # | 本片的說法（幕） | 來源依據 | 結論 |
|---|---|---|---|
| 1 | 爸爸放在網路上的開源專案（1） | repo 擁有者 pcpcchen-coder；LICENSE 為 MIT | 相符；沒有說每一行程式是誰寫的 |
| 2 | 家裡的一句叮嚀、半夜想到的點子，說完幾秒就忘；想把它們留下來，隱私優先（1） | README 開頭標語與副標「隱私優先的當下記錄器」 | 相符（轉述） |
| 3 | 三步驟：聽、寫、整理；每三十秒一段（2） | README 系統總覽；config `audio.chunk_seconds: 30` | 相符；「三步驟」是本片的歸納 |
| 4 | 有人說話的片段在電腦上變成文字，不用上網（2、4） | README：「語音辨識 100% 在你的 Mac 上（whisper.cpp + Metal）」「這一整層完全離線，不需要網路」 | 相符 |
| 5 | 每天半夜十二點十分整理前一天（2、11） | config `summary.hour: 0`、`minute: 10`；docs/use-cases.md「00:10 整理昨天（預設）」 | 相符（預設值，可改） |
| 6 | 需要四麥克風陣列、蘋果晶片的 Mac（macOS 13 以上）（3） | docs/getting-started.md；README「你需要準備」 | 相符 |
| 7 | 每日摘要用官方 Codex 登入自己的 ChatGPT 帳號，不需要 API 金鑰（3） | README：「不需要 API key」「一個可使用 Codex 的 ChatGPT 帳號」 | 相符 |
| 8 | 守門：安靜時不存聲音、也不送去辨識（4） | docs/privacy.md「不建立 WAV」「不呼叫 Whisper」 | 相符；仍會留低容量數值遙測，教材有寫 |
| 9 | 一般雲端錄音服務會上傳聲音檔辨識（5） | README 比較表「上傳音訊到雲端」 | 相符（README 的一般性比較，不指特定產品） |
| 10 | 原始聲音、聲音特徵、資料庫留在這台電腦（5、8） | README 隱私承諾表；docs/privacy.md | 相符 |
| 11 | 每天只有逐字稿文字送到自己的帳號；可以關掉摘要，完全離線（5） | docs/privacy.md「一句話總結」與 `summary.enabled: false` | 相符；啟用行事曆時，候選標題與時間也會經由行事曆 App 寫入，教材有寫 |
| 12 | 語音辨識在安靜或只有固定噪音時，可能寫出沒人說過的話（6） | config 註解「deterministic Whisper text on silence or steady noise」；README 多層防幻覺 | 相符；「冷氣在響」是本片舉的固定噪音例子 |
| 13 | 關卡：硬體人聲、背景噪音、信心分數、重複句（6） | README 多層防幻覺；config `hallucination_filter` | 相符（舉其中幾層） |
| 14 | 攔下的句子寫進檢查紀錄；不封鎖任何特定句子（6） | README「攔截決策全部寫入稽核表」「不封鎖任何特定句子」；docs/privacy.md `transcription_audits` | 相符 |
| 15 | 每位家人錄十五秒樣本，只留聲音特徵，錄音不保留（7） | docs/speakers.md；config 註解「The enrollment WAV is discarded」 | 相符 |
| 16 | 麥克風陣列回報聲音角度；音色和方向是兩份獨立線索（7） | docs/speakers.md | 相符 |
| 17 | 寫的是可能說話者，不是確認身分；不能開門、付款、當證據（7） | README；docs/privacy.md 明確禁止的用途 | 相符 |
| 18 | 要能自己檢查，而不是只聽承諾（8） | docs/privacy.md 開頭 | 相符（轉述） |
| 19 | 摘要程式沒有讀取聲音檔的功能；每次在唯讀、用完就丟的暫時環境進行（8） | summary.py：Codex 參數 `--ephemeral`、`--sandbox read-only`、暫存工作目錄；import 只有設定、歷史與儲存模組 | 相符 |
| 20 | 文件附了指令，可確認安靜時沒有存聲音檔（8） | docs/privacy.md「如何自己驗證」第 4 項 | 相符 |
| 21 | 換提示詞換用途；家庭日誌已完整；家教、夢境換提示詞今天就能試（9） | README；docs/use-cases.md | 相符 |
| 22 | 不能拿來監控任何人；不提供偷偷錄音的功能（9） | README IMPORTANT；docs/privacy.md | 相符 |
| 23 | 早上看到逐字稿、每日摘要（時間軸、待辦、一百字重點）、行事曆候選（10） | README 產出範例；config 摘要 prompt；docs/daily-summary.md | 相符；行事曆功能預設關閉，要先開啟 |
| 24 | 行事曆候選預設逐筆確認（10） | docs/daily-summary.md 第 224 行；可改成自動加入（第 239 行） | 相符 |
| 25 | 「明天記得去拿包裹」的旅程（11） | README 逐字稿與摘要範例（19:40、待辦事項） | 相符；是 README 的範例，不是真實紀錄 |
| 26 | 選單列能暫停錄音（12 投影片） | docs/menu-bar.md：暫停 15 分鐘、1 小時或直到手動恢復 | 相符 |
| 27 | 下一堂正課是 L014 我們家的科技公約（12） | 課表 L014 | 相符 |

## 刻意避免的說法

- 沒有說它保證資料不會外洩；文件自己列出不防護的情形（能存取這台 Mac 的人、備份、送到 ChatGPT 之後的文字）。
- 沒有給辨識或人別的準確率；文件沒有數字，也寫明錯認仍可能發生。
- 沒有提版本號（pyproject 是 0.16.0，README 仍寫 0.14.4）。
- 沒有示範任何真實錄音、逐字稿或家人資料。
- 沒有說它是家長監控工具；文件明確禁止這種用途。
'''

PLAN = '''# SP002 番外篇：FamilyRecorder

依公開 repo 製作的專案介紹；沒有實際使用錄音，沒有真實逐字稿或家人資料。
沿用原片頭 v2、陳犀牛、深藍／黃／青、12 頁原生可編輯簡報、36 句旁白、zh-TW-YunJheNeural；
教學段落靜態畫面加 0.55 秒淡化，無背景音樂、無推拉鏡頭。不佔課號，不更動課表。

## 為什麼這樣排

- 觀眾是一起看片的孩子和爸爸，所以先講「它解決什麼問題」，再講「怎麼運作」，最後講「隱私與同意」。
- 和正課接得起來：第 6 頁接第十二堂的幻覺；第 9 頁接第十一堂的提示詞；結尾三個問題接到下一堂 L014「我們家的科技公約」。
- 語氣比正課活潑：用「要讓它上班」「四個本事」「一句話的旅程」來講，但每一句都對得回文件或程式。

## 12 頁

1 開場與揭露｜2 聽、寫、整理｜3 需要準備的三樣東西｜4 四個本事｜5 聲音留在家，文字才出門｜6 防幻覺｜
7 可能是誰、從哪裡來｜8 隱私承諾｜9 換提示詞，換用途｜10 早上會看到什麼｜11 一句話的旅程｜12 帶回家的三個問題。

## 家庭討論包

`classroom/SP002_FamilyRecorder家庭討論包/`：爸爸先讀、家庭討論卡、3 頁列印包（一句話的旅程排序卡、資料去哪裡分類遊戲、我們家的收音約定）、
資料去哪裡（CSV＋說明）、解答與解說、和孩子一起讀專案。約 30–45 分鐘，不需要任何帳號，也不需要真的安裝。
由 `authoring/sp002/classroom.py` 產生。
'''

SUMMARY = '''這是番外篇，依 FamilyRecorder 公開的程式與文件製作的介紹，不是實際使用錄音，也沒有任何真實逐字稿或家人資料。

家裡的一句叮嚀、半夜想到的點子，常常說完幾秒就忘了。FamilyRecorder 是爸爸在 GitHub 上公開的開源專案：
桌上的四麥克風陣列一直聽，Mac 在本機把有人說話的片段變成文字，每天整理成一份摘要。陳犀牛帶你看它怎麼運作，以及它怎麼保護隱私。

這一集會看到
・聽、寫、整理三步驟；安靜的時候不存聲音，也不送去辨識
・四個本事：守門、聽寫、防幻覺、認聲音（可能說話者不是確認身分）
・聲音留在家：原始聲音、聲音特徵、資料庫都不出門，每天只有逐字稿文字出門一次，也可以完全離線
・換提示詞就換用途；不能拿來監控任何人，也不提供偷偷錄音
・一句「明天記得去拿包裹」從客廳走到早上的待辦事項

家庭討論包（classroom.zip）
先讀「00_爸爸先讀」，列印「02_列印包」（A4 共 3 頁），玩「一句話的旅程」排序和「資料去哪裡」分類，最後用「01_家庭討論卡」討論三個問題。
約 30–45 分鐘，不需要任何帳號，也不需要真的安裝。

注意事項
・這一集的旁白是文字轉語音合成的，不是真人錄音。
・在家裡收音之前，要先取得每一位可能被錄到的人的同意，並清楚標示正在收音。

來源（查核日 2026-10-17）
FamilyRecorder（MIT 授權）：https://github.com/pcpcchen-coder/FamilyRecorder
README、應用場景、隱私與信任邊界、家庭成員與方向、每日摘要與行事曆等文件，以及 config.example.yaml 與 summary.py（commit ff76063）
'''

README = ('# 父子科技學院 SP002 番外篇：FamilyRecorder\n\n'
          '依公開 repo `pcpcchen-coder/FamilyRecorder` 製作的專案介紹，不佔課號、不更動課表。沒有實際使用錄音，沒有真實逐字稿或家人資料。\n'
          '製作來源、旁白、PPTX、家庭討論包與 QC 都在這個資料夾；先讀 `production/START_HERE.md`。\n'
          '交付版本、檔案雜湊、大型檔取得方式與重建命令見 `delivery.json`；檢視方法與限制見 `qc/manual-review.md`。\n'
          'YouTube 由使用者自行上傳。內容由 `authoring/sp002/prepare_content.py` 與 `authoring/sp002/classroom.py` 產生。\n')

if __name__ == '__main__':
    special_builder.build(
        special=SPECIAL, slug=SLUG, title=TITLE, header_en='FAMILY RECORDER', cover_disclosure='依公開專案製作的介紹',
        first_sentence_needles=('番外篇', '並非實際使用錄音'), summary_prefix='這是番外篇，依 FamilyRecorder 公開的程式與文件製作的介紹',
        checked=CHECKED, src=SRC, scenes=SCENES, visible=VISIBLE, board=BOARD,
        render_options={'asianLatinAutoSpace': False, 'captionLineBreak': 'kinsoku'},
        tts_basis='On 2026-10-17 the user asked for SP002; the producing agent stated before synthesis that the public script '
                  'would go to Edge TTS on the same basis as L004–L013.',
        source_records=SOURCE_RECORDS,
        source_method='The producing agent cloned the public repo (commit ff76063) and read the README, docs and relevant source '
                      'files itself; claims were mapped line by line (production/source-notes.md). The project was not installed or run.',
        not_verified=['沒有安裝或執行 FamilyRecorder，沒有接 XVF3800 實測；所有說法是文件與程式碼寫了什麼',
                      '辨識與人別的準確率文件沒有給數字，本片也不提',
                      '文件與程式有小出入：pyproject 版本 0.16.0、README 仍寫 0.14.4；docs/privacy.md 寫 summary.py 只 import config 與 storage、515 行，'
                      '目前程式多 import history、522 行。本片不引用這些細節'],
        documents={'fact-check.md': FACT_CHECK, 'plan.md': PLAN, 'delivery-summary.md': SUMMARY,
                   'source-notes.md': (Path(__file__).resolve().parent / 'source-notes.md').read_text(encoding='utf-8')},
        readme=README, content_mode='special-project-introduction', delivery_label='番外篇・依公開專案製作的介紹（無實際使用錄音）',
        classroom_note='classroom.zip 是家庭討論包，約 30–45 分鐘；這集是番外篇，沒有 120 分鐘的課堂流程。')
