# SP002 事實查核

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
