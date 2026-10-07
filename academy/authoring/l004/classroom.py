"""Build the L004 classroom pack (real, usable materials; no private data).

Text files are written directly. The 6-page print pack is authored as HTML
(authoring/l004/print/print-pack.html) and printed to PDF with a headless
Chromium/Chrome when one is available (XINEW_CHROME or a common install path).
Without a browser the existing PDF is kept and reported; a missing PDF is an error.

    ./portable-runtime.sh python authoring/l004/classroom.py

After any change here: rerun pipeline/delivery.py, then verify (classroom is fingerprinted).
"""
from pathlib import Path
import csv
import json
import os
import shutil
import subprocess
import tempfile

R = Path(__file__).resolve().parents[2]
E = R / 'episodes/academy/l004-network-relay'
D = E / 'classroom/L004_封包接力賽'
PRINT = Path(__file__).resolve().parent / 'print'
PDF = D / '02_列印包_封包接力賽.pdf'

DEVICE = '198.51.100.7'
SERVER = '192.0.2.1'
NAME = 'pictures.example.com'

FILES = {
'00_爸爸先讀.md': f'''# 父子科技學院 L004：網路到底是什麼——封包接力賽（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在桌上的接力賽，和孩子自己畫的家庭網路手繪圖。

## 這堂課要帶走什麼

- 六個名詞各做什麼：裝置、路由器、IP 位址、DNS、伺服器、封包。
- 一張圖片的旅程：DNS 查位址 → 資料分成封包 → 路由器一站一站轉送 → 裝置依編號重組。
- 至少一個限制或安全注意：比喻不等於真實；封包可能亂序或遺失；Wi-Fi 密碼不公開。
- 作品：**家庭網路手繪圖**，另有偵探筆記與自選規則卡。

## 課前準備（約 15 分鐘）

1. 列印 `02_列印包_封包接力賽.pdf`（A4，共 6 頁，單面）。沒有印表機也可以照著畫在白紙上。
2. 準備：信封 8–10 個（或把紙對摺代替）、剪刀、筆、膠帶、一枚硬幣、三個小盒子或椅子當路由站、一個「遺失盒」。
3. 圖片：用列印包第 4 頁的範例圖，或請孩子在第 5 頁的空白六格上**自己畫**。不要使用含有人臉、姓名、住址、學校的照片。
4. 排賽道（一直線，彼此相隔幾步）：`裝置 — 路由站 A — 路由站 B — 伺服器`；繞路站 C 放在旁邊，第二案才用。
5. 把轉送表 A、B、C 放在各自的路由站；位址牌放在裝置與伺服器的座位。
6. 錄音只保存在家裡的私人位置，不直接公開；錄音前先說課次與主題，不要唸出帳號、密碼或住址。

本課使用的名稱與位址都是**保留給文件使用的範例**，不是真實服務：
裝置 `{DEVICE}`、伺服器 `{SERVER}`、名稱 `{NAME}`。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：一張圖片怎麼從遠方送到螢幕？先請孩子猜 | 提出案件，不急著給答案 |
| 10–25 | 看影片、認識六個名詞與四個角色；讀角色卡 | 示範一次「查通訊錄 → 寫信封 → 交給路由站」 |
| 25–65 | 三個案件接力賽（規則見 `01_活動規則_三個案件.md`） | 當伺服器與路由器；第三案負責「弄丟」一個信封 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：一條自選規則＋家庭網路手繪圖 | 只在孩子開口時協助；幫忙查看電腦上的線索 |
| 105–115 | 角色互換：孩子教爸爸封包的旅程 | 當學生，照孩子說的做，聽不懂就發問 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 問四個錄音問題，協助存檔 |

## 比喻的限制（請一定和孩子聊）

1. 信封只是比喻。真實的封包是資料，由程式與設備自動處理，沒有人在拆信。
2. 路由器不是丟硬幣選路。它依照自己的轉送資訊與當時的網路狀況，為每個封包選擇下一站；
   同一張圖片的封包**可能**走不同的路，也可能走相同的路，並沒有保證。
3. 網路層（IP）本身**不保證**送達，也不保證順序；封包可能損壞、重複、亂序或沒有到達。
   「確認、重送、排好順序」是 TCP 這類傳送規則加上的；UDP 這類規則比較簡單，不保證送達，也不負責重送。
   （影片旁白只說「某些傳送規則」，TCP、UDP 的名稱留給想多知道一點的孩子。）
4. IP 位址不是住家門牌。裝置連到不同的網路，通常會拿到不同的位址。
5. DNS 通訊錄卡是簡化版。真實的 DNS 由許多名稱伺服器分工，並且會暫存查過的答案。
6. 「路由器不需要讀懂內容」不等於「別人一定看不到內容」。內容能不能保密要看有沒有加密，之後的課再談。
7. 家裡的裝置常使用私人位址（例如 192.168 開頭）；這類位址不會直接在公開的網際網路上轉送，
   對外的連線需要由家裡的閘道（通常就是家用路由器）居中處理。本課不深入這一段。

## 安全與隱私

- 手繪圖、錄音、截圖都**不要**出現：Wi-Fi 密碼、路由器管理密碼、住址、學校、裝置序號。
- 要公開或錄影時，Wi-Fi 名稱與真實位址改用代號，或使用上面的文件範例位址。
- 想順便檢查家裡的 Wi-Fi（爸爸選做，依美國 FTC 的消費者建議）：使用 WPA3 或 WPA2 個人版加密、
  更改預設的管理者帳密與網路名稱、保持路由器更新、設定完成後登出管理者。

## 在 Mac 上找線索（爸爸陪同，選做）

`蘋果選單 → 系統設定 → 側邊欄的 Wi-Fi → 連線中的網路旁按「詳細資訊」`，
可以看到「IP 位址」（Wi-Fi 連線的 IP 位址）與「路由器」（Wi-Fi 連線的路由器位址）。
選單名稱依 macOS 版本可能不同，以自己電腦的畫面為準。看完即可，不必抄到會公開的作品上。

## 來源（查核日 2026-10-07）

- Internet Protocol：https://www.rfc-editor.org/rfc/rfc791
- 主機需求（網路的網路、IP 不保證送達）：https://www.rfc-editor.org/rfc/rfc1122
- 路由器需求（查看 IP 標頭、選擇下一站）：https://www.rfc-editor.org/rfc/rfc1812
- TCP：https://www.rfc-editor.org/rfc/rfc9293 ／ UDP：https://www.rfc-editor.org/rfc/rfc768
- DNS：https://www.rfc-editor.org/rfc/rfc1034 ／ https://www.icann.org/resources/pages/dns-2022-09-13-en
- 文件用範例名稱與位址：https://www.rfc-editor.org/rfc/rfc6761 ／ https://www.rfc-editor.org/rfc/rfc5737
- 私人位址：https://www.rfc-editor.org/rfc/rfc1918
- Mac 上的 Wi-Fi 設定：https://support.apple.com/zh-tw/guide/mac-help/mh11935/mac
- 家用 Wi-Fi 安全：https://consumer.ftc.gov/articles/how-secure-your-home-wi-fi-network

課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
''',

'01_活動規則_三個案件.md': f'''# 封包接力賽：三個案件的規則

## 角色與賽道

賽道排成一直線：`裝置 — 路由站 A — 路由站 B — 伺服器`。繞路站 C 放在 A 與 B 的旁邊。

| 角色 | 誰來當 | 位址（文件範例） |
|---|---|---|
| 裝置 | 孩子 | `{DEVICE}` |
| 伺服器 | 爸爸 | `{SERVER}`，名稱 `{NAME}` |
| 路由站 A、B、C | 放轉送表的椅子或盒子 | 不需要位址牌 |
| DNS | 通訊錄卡（放在裝置旁邊） | — |

**兩個人怎麼玩：** 誰寄出信封，另一個人就先當路由器。寄件人把信封放進第一個路由站就回座位；
另一個人依照每一站的轉送表，把信封一站一站移到終點，再回到自己的座位當收件人。
**三個人以上：** 請家人各顧一個路由站。

**路由器守則：** 只看信封上的「目的地」，查這一站的轉送表，交給下一站。不拆信封、不改標籤、不自己決定終點。

## 第一案：把圖片完整送到（約 15 分鐘）

1. 裝置想要圖片，先查「DNS 通訊錄卡」：`{NAME}` 的位址是多少？把答案唸出來。
2. 裝置填「要求卡」（來源 `{DEVICE}`，目的地 `{SERVER}`，內容：請給我圖片），裝進信封，放到路由站 A。
3. 路由器照轉送表：A → B → 伺服器。
4. 伺服器收到要求，把圖片沿虛線剪成六片，每片裝一個信封，貼上標籤：
   來源 `{SERVER}`、目的地 `{DEVICE}`、第幾片／共 6 片。
5. 伺服器**一次送出一個**信封，放到路由站 B；路由器照轉送表：B → A → 裝置。
6. 裝置收齊後依編號拼回圖片，填「確認卡」（收到 6／6），照原路送回伺服器。
7. 在偵探筆記寫下：到達順序、有沒有缺片、花了多少時間。

過關條件：圖片完整，孩子能指出信封上哪一欄是路由器一定要看的。

## 第二案：順序亂了（約 12 分鐘）

1. 伺服器重新送同一張圖片的六個信封。
2. 這一次路由站 B 每送一個信封就丟一次硬幣：正面交給路由站 A；反面交給繞路站 C。
3. 繞路站 C 的規則：慢慢數到 10，再交給裝置。
4. 裝置**依到達的先後**把信封排成一列，先不要看編號；記下到達順序，再靠編號排回正確順序。
5. 偵探問題：到達順序和送出順序一樣嗎？證據是什麼？沒有編號的話拼得回來嗎？

提醒：真實的路由器不是丟硬幣。硬幣代表「路況會變」，重點是封包不保證照順序到達。

## 第三案：少了一片（約 13 分鐘）

1. 伺服器再送一次六個信封。爸爸趁孩子不注意，把其中一個信封放進「遺失盒」。
2. 裝置收完後清點編號，找出少了哪一片。
3. 裝置填「重送要求卡」：請重送第＿片，照原路送給伺服器。
4. 伺服器從遺失盒取回那一個信封（代表它手上留有原始資料），重新送出。
5. 裝置拼好圖片，再回傳確認卡。

**選做 3B：不重送的規則。** 再玩一次，但規定「不可以要求重送」。圖片缺了一塊就是結果。
討論：什麼情況寧可缺一點也不想等？什麼情況一定要完整？
（這對應兩類傳送規則：有確認與重送的，以及不保證送達、也不負責重送的。）

## 常見卡關

- 信封送錯站：先看標籤上的目的地有沒有寫，再看這一站的轉送表有沒有這個位址。
- 圖片拼不回來：信封有沒有寫第幾片？有沒有把來源和目的地寫反？
- 孩子覺得路由器「應該知道整條路」：請他只照轉送表做一次，體會路由器一次只決定下一站。
''',

'03_偵探筆記_填寫說明.md': '''# 偵探筆記怎麼寫

`03_偵探筆記.csv` 可以用 Numbers 或任何試算表開啟；也可以照欄位抄在紙上。

每個案件寫一列：

- **我的預測**：開始前先猜。例如「六片會照順序到」「會少一片」。
- **實際到達順序**：照信封到達的先後寫編號，例如 `1,3,2,5,4,6`。
- **缺少的編號**：沒有就寫「無」。
- **證據**：你看到什麼才這樣判斷？（到達順序、清點結果、空著的位置）
- **修正方法**：用編號排回去、請伺服器重送、接受缺片……
- **結果**：圖片完整嗎？
- **用時（選填）**：只和自己比，不必比快。

好偵探不只寫答案，還寫**怎麼知道的**。
''',

'04_家庭網路手繪圖_畫法與檢查表.md': '''# 作品：家庭網路手繪圖

用列印包第 6 頁的底稿，或自己拿一張白紙畫。重點是關係畫對，不必畫得漂亮。

## 一定要畫出來

1. **裝置**：至少兩個，用代號，例如「我的筆電」「爸爸的手機」。
2. **路由器**：家裡把裝置連到外面的那一台（有的家庭和數據機是同一台，問爸爸）。
3. **對外連線**：從路由器通往「外面的網路」的一條線。
4. **伺服器**：在外面的網路另一端，保存你想看的資料。
5. **封包方向**：用箭頭畫出「要求」怎麼出去、「回應」怎麼回來。

## 可以加分

- 用實線表示有線、虛線表示無線（Wi-Fi）。
- 在旁邊畫一本通訊錄，標上 DNS：用名稱查位址。
- 畫出一個封包可能遺失或繞路的地方，寫上怎麼補救。

## 不要寫在圖上

Wi-Fi 密碼、路由器管理密碼、住址、學校、裝置序號。
要給別人看或錄影時，Wi-Fi 名稱和真實位址也改成代號。

## 找線索（爸爸陪同，選做）

Mac：`蘋果選單 → 系統設定 → Wi-Fi → 連線中的網路旁按「詳細資訊」`，
看得到「IP 位址」和「路由器」。選單名稱依版本可能不同；看完就好，不必抄到公開的作品上。

## 交件前檢查

- [ ] 至少兩個裝置、一台路由器、一條對外連線、一個伺服器
- [ ] 有箭頭表示封包的去與回
- [ ] 我能指著圖，不看稿說出一張圖片的旅程
- [ ] 圖上沒有密碼、住址或其他不該公開的資訊
- [ ] 寫上作品名稱、版本與日期，例如 `L004_家庭網路手繪圖_v01`
- [ ] 拍照或掃描後存進本課資料夾，並打開確認看得清楚
''',

'05_自選規則卡.md': '''# 孩子獨立改造：增加一條自己的規則

選一條，或自己發明。一次只改一條，才知道是哪一條造成改變。

## 靈感

- 多一個路由站：路變長了，會發生什麼事？
- 多一條可以選的路線：兩條路各送幾個？哪一條比較快？
- 限時送完：趕時間的時候，哪一步最容易出錯？
- 兩張圖片同時送：信封上還需要多寫什麼，才不會拼錯？
- 某個路由站暫停服務：信封要怎麼改道？轉送表要怎麼改？
- 每站一次只能處理一個信封：會不會塞車？

## 我的規則卡

- 規則名稱：＿＿＿＿＿＿＿＿＿＿
- 我改了什麼（只改一條）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 我預測會：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 實際發生：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 證據（到達順序、缺片、時間）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 這條規則像真實網路的哪一件事？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 要保留、修改，還是拿掉？為什麼？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

把結果也記到偵探筆記的「自選規則」那一列。
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成家庭網路手繪圖（裝置、路由器、對外連線、伺服器、封包方向）
- [ ] 不看稿，說出一張圖片的旅程：DNS 查位址 → 分成封包 → 路由器一站一站轉送 → 依編號重組
- [ ] 說出六個名詞各做什麼：裝置、路由器、IP 位址、DNS、伺服器、封包
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 三個案件的偵探筆記有預測、證據與修正方法
- [ ] 測試過一條自選規則，並說明要不要保留

## 孩子教爸爸（105–115 分鐘）

請孩子當老師，爸爸當學生。建議順序：

1. 指著手繪圖，說出要求怎麼出去、回應怎麼回來。
2. 拿一個信封，說明標籤上每一欄給誰看。
3. 示範一次「少了一片」怎麼發現、怎麼補救。
4. 出一題考爸爸，例如：「如果通訊錄卡寫錯位址，會發生什麼事？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

1. 封包接力賽在解決什麼問題？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：`L004_家庭網路手繪圖_v01`、`L004_偵探筆記_v01`、`L004_自選規則卡_v01`，
放進 `文件/Tech Academy/L004_封包接力賽/`，存好後再打開一次確認。
''',

'07_六個名詞小抄.md': '''# L004 六個名詞小抄

| 名詞 | 一句話 | 接力賽裡是什麼 |
|---|---|---|
| 裝置 | 送出要求、收下封包、把資料組回來的電腦或手機 | 孩子的座位 |
| 路由器 | 看封包的目的地位址，決定交給哪個下一站 | 路由站 A、B、C 與轉送表 |
| IP 位址 | 一組編號，標示封包從哪裡來、要送到哪裡 | 地址卡、位址牌 |
| DNS | 網路的通訊錄，用名稱查出位址；不運送資料 | 通訊錄卡 |
| 伺服器 | 保存資料，收到要求後回應 | 爸爸的座位 |
| 封包 | 分成小份的資料，帶著位址與編號等資訊 | 一個個信封 |

## 三個提醒

- 網路本身不保證每個封包都送到，也不保證順序；確認與重送是某些傳送規則加上的。
- 信封、門牌、通訊錄都是比喻，幫忙理解，不等於真實的運作細節。
- Wi-Fi 密碼和住址不寫在作品上，也不在錄影裡唸出來。

我自己的說法（用一句話解釋「網路是什麼」）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

NOTE_ROWS = [
    ['第一案', '正常送達：照轉送表，一次送一個', '', '', '', '', '', '', ''],
    ['第二案', '亂序：路由站 B 丟硬幣，反面走繞路站 C', '', '', '', '', '', '', ''],
    ['第三案', '遺失＋重送：爸爸把一個信封放進遺失盒', '', '', '', '', '', '', ''],
    ['第三案 B（選做）', '遺失但不可以要求重送', '', '', '', '', '', '', ''],
    ['自選規則', '（寫下我的新規則）', '', '', '', '', '', '', ''],
]
NOTE_HEADER = ['案件', '規則', '我的預測', '實際到達順序', '缺少的編號', '證據', '修正方法', '結果（圖片完整嗎）', '用時（選填）']


def label(n):
    return (f'<div class="label"><b>封包標籤</b><span>第 <i>{n}</i> 片／共 6 片</span>'
            f'<p>來源：{SERVER}（伺服器）</p><p>目的地：{DEVICE}（裝置）</p></div>')


def piece_grid(with_picture):
    art = '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg" aria-label="範例圖片：火箭與星球">
 <rect width="600" height="400" fill="#eaf6ff"/>
 <circle cx="470" cy="110" r="62" fill="#ffc531"/><ellipse cx="470" cy="110" rx="98" ry="20" fill="none" stroke="#0b3a66" stroke-width="7"/>
 <circle cx="95" cy="70" r="9" fill="#0b3a66"/><circle cx="210" cy="40" r="6" fill="#0b3a66"/><circle cx="560" cy="250" r="7" fill="#0b3a66"/>
 <circle cx="60" cy="210" r="6" fill="#0b3a66"/><circle cx="330" cy="70" r="5" fill="#0b3a66"/>
 <g transform="rotate(28 270 220)">
  <path d="M270 80 C330 140 330 250 310 300 L230 300 C210 250 210 140 270 80Z" fill="#ffffff" stroke="#0b3a66" stroke-width="7"/>
  <circle cx="270" cy="190" r="26" fill="#35c3ee" stroke="#0b3a66" stroke-width="7"/>
  <path d="M230 250 L185 320 L232 300Z" fill="#ffc531" stroke="#0b3a66" stroke-width="7" stroke-linejoin="round"/>
  <path d="M310 250 L355 320 L308 300Z" fill="#ffc531" stroke="#0b3a66" stroke-width="7" stroke-linejoin="round"/>
  <path d="M245 302 Q270 372 295 302Z" fill="#ff7a3d" stroke="#0b3a66" stroke-width="7" stroke-linejoin="round"/>
 </g>
 <path d="M0 360 Q150 320 300 360 T600 350 L600 400 L0 400Z" fill="#35c3ee"/>
</svg>''' if with_picture else ''
    cells = ''.join(f'<div class="cell"><span>{n}</span></div>' for n in range(1, 7))
    return f'<div class="pic">{art}<div class="cut">{cells}</div></div>'


def html():
    role = lambda t, e, duty, line, limit: (
        f'<div class="card"><h3>{t}<small>{e}</small></h3><h4>職責</h4><ul>{"".join(f"<li>{x}</li>" for x in duty)}</ul>'
        f'<h4>可以這樣說</h4><p class="say">{line}</p><p class="limit">{limit}</p></div>')
    table = lambda title, rows, note: (
        f'<div class="route"><h3>{title}</h3><table><tr><th>信封上的目的地</th><th>交給下一站</th></tr>'
        + ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in rows) + f'</table><p>{note}</p></div>')
    pages = []
    pages.append('<h2>角色卡</h2><p class="lead">沿外框剪下。扮演前先大聲說出自己的職責。</p><div class="grid2">'
        + role('裝置', 'Device', ['送出要求', '收下封包，依編號重組', '全部收到後回傳確認'], f'「我要找 {NAME}，<br>請給我圖片。」', '真實的裝置由程式自動完成這些事。')
        + role('路由器', 'Router', ['只看信封上的目的地位址', '查這一站的轉送表', '交給下一站，不拆信封'], '「目的地是＿＿，下一站是＿＿。」', '一次只決定下一站，不保證送達。')
        + role('DNS', '網路的通訊錄', ['有人問名稱，就回答位址', '不運送圖片'], f'「{NAME}<br>的位址是 {SERVER}。」', '真實的 DNS 由許多名稱伺服器分工。')
        + role('伺服器', 'Server', ['保存圖片等資料', '收到要求後分片、貼標籤、逐一送出', '收到重送要求就補送'], '「收到要求，圖片分成六片送出。」', '回應的是裝置送來的要求。')
        + '</div>')
    pages.append('<h2>DNS 通訊錄卡、位址牌與轉送表</h2><p class="lead">沿外框剪下，放在對應的座位或路由站。</p>'
        '<div class="route"><h3>DNS 通訊錄卡</h3><table><tr><th>名稱</th><th>IP 位址</th></tr>'
        f'<tr><td>{NAME}</td><td>{SERVER}</td></tr><tr><td>games.example.net</td><td>203.0.113.9</td></tr></table>'
        '<p>以上名稱與位址都是保留給文件使用的範例，不是真實服務。</p></div>'
        f'<div class="grid2 tents"><div class="tent">裝置<b>{DEVICE}</b></div><div class="tent">伺服器<b>{SERVER}</b></div></div>'
        + table('路由站 A 轉送表', [(DEVICE, '裝置'), (SERVER, '路由站 B'), ('其他位址', '放進「無法轉送」盒，告訴寄件人')], '位置：裝置與路由站 B 之間。')
        + table('路由站 B 轉送表', [(SERVER, '伺服器'), (DEVICE, '路由站 A（第二案：丟硬幣，正面 A、反面繞路站 C）'), ('其他位址', '放進「無法轉送」盒，告訴寄件人')], '位置：路由站 A 與伺服器之間。')
        + table('繞路站 C 轉送表（第二案才用）', [(DEVICE, '慢慢數到 10，再交給裝置'), ('其他位址', '交回路由站 B')], '硬幣代表路況會變；真實的路由器不是丟硬幣。'))
    pages.append('<h2>信封標籤與訊息卡</h2><p class="lead">剪下後貼在信封上。標籤上的位址是文件範例。</p><div class="grid2">'
        + ''.join(label(n) for n in range(1, 7))
        + f'<div class="label msg"><b>要求卡</b><p>來源：{DEVICE}（裝置）</p><p>目的地：{SERVER}（伺服器）</p><p>內容：請給我圖片</p></div>'
        + f'<div class="label msg"><b>確認卡</b><p>來源：{DEVICE}（裝置）</p><p>目的地：{SERVER}（伺服器）</p><p>內容：收到 ＿＿ 片／共 6 片</p></div>'
        + f'<div class="label msg"><b>重送要求卡</b><p>來源：{DEVICE}（裝置）</p><p>目的地：{SERVER}（伺服器）</p><p>內容：請重送第 ＿＿ 片</p></div>'
        + '<div class="label msg"><b>空白標籤</b><p>來源：＿＿＿＿＿＿＿＿</p><p>目的地：＿＿＿＿＿＿＿</p><p>第 ＿＿ 片／共 ＿＿ 片</p></div>'
        + '</div>')
    pages.append('<h2>範例圖片：沿虛線剪成六片</h2><p class="lead">每一片裝進一個信封。角落的小數字用來檢查有沒有拼對。</p>' + piece_grid(True)
        + '<p class="lead">本圖為本課原創的簡單圖形，可自由列印使用。</p>')
    pages.append('<h2>空白六格：畫自己的圖</h2><p class="lead">畫好再沿虛線剪開。請畫圖，不要貼含有人臉、姓名、住址或學校的照片。</p>' + piece_grid(False))
    pages.append('<h2>家庭網路手繪圖</h2><p class="lead">用代號寫裝置。實線＝有線，虛線＝無線，箭頭＝封包方向。</p>'
        '<div class="draw"><div class="zone z1"><b>家裡的裝置（至少兩個，用代號）</b></div><div class="zone z2"><b>路由器</b></div>'
        '<div class="zone z3"><b>對外連線 → 外面的網路</b></div><div class="zone z4"><b>伺服器（回應要求）</b></div></div>'
        '<div class="grid2 foot"><div><b>不要寫在圖上</b><p>Wi-Fi 密碼、路由器管理密碼、住址、學校、裝置序號。</p></div>'
        '<div><b>作品資訊</b><p>名稱：L004_家庭網路手繪圖_v＿＿</p><p>日期：＿＿＿＿＿＿　代號：＿＿＿＿＿＿</p></div></div>')
    body = ''.join(f'<section><header>父子科技學院 L004｜封包接力賽｜列印包 {i}／{len(pages)}</header>{p}</section>'
                   for i, p in enumerate(pages, 1))
    css = '''@page{size:A4;margin:0}*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:"Noto Sans CJK TC","PingFang TC","Microsoft JhengHei",sans-serif;color:#0b2540;font-size:12.5pt;line-height:1.5}
section{width:210mm;height:297mm;padding:14mm 15mm;page-break-after:always;position:relative;overflow:hidden}
header{font-size:9.5pt;color:#4a6a88;border-bottom:1.2pt solid #35a9d6;padding-bottom:2mm;margin-bottom:5mm}
h2{font-size:21pt;margin:0 0 2mm;color:#0b2540}h3{font-size:15pt;margin:0 0 2mm}h4{font-size:10.5pt;margin:2mm 0 0;color:#4a6a88}
small{font-size:10pt;color:#4a6a88;font-weight:400;margin-left:3mm}.lead{margin:0 0 4mm;color:#35506b}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.card{border:1.6pt dashed #0b2540;border-radius:4mm;padding:6mm;height:112mm}.card ul{margin:1mm 0 0 5mm;padding:0}
.say{font-size:13pt;font-weight:700;margin:1mm 0}.limit{font-size:10.5pt;color:#35506b;border-top:.8pt solid #9db7cc;padding-top:2mm;margin-top:4mm}
.route{border:1.4pt solid #0b2540;border-radius:3mm;padding:2.6mm 4mm;margin-bottom:3mm}.route h3{font-size:13pt;margin:0 0 1.2mm}.route p{margin:1mm 0 0;font-size:10pt;color:#35506b}
table{width:100%;border-collapse:collapse;font-size:11.5pt}th,td{border:.8pt solid #7f9bb3;padding:.9mm 2.5mm;text-align:left}th{background:#e3f3fb}
.tents{margin-bottom:3mm}.tent{border:1.6pt dashed #0b2540;border-radius:3mm;text-align:center;padding:1.8mm;font-size:12.5pt}.tent b{font-size:17pt;margin-left:3mm}
.label{border:1.6pt dashed #0b2540;border-radius:3mm;padding:4mm 5mm;height:38mm}.label b{font-size:14pt;margin-right:4mm}
.label span{font-size:13pt}.label i{font-style:normal;font-weight:700;font-size:19pt}.label p{margin:.6mm 0}.label.msg{background:#fff7dd}
.pic{position:relative;width:180mm;height:120mm;border:1.4pt solid #0b2540;margin:2mm 0 4mm}.pic svg{position:absolute;inset:0;width:100%;height:100%}
.cut{position:absolute;inset:0;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr)}
.cell{border:1.1pt dashed #0b2540;position:relative}.cell span{position:absolute;left:2mm;top:1mm;font-size:11pt;font-weight:700;background:#fff;padding:0 1.5mm;border-radius:1.5mm}
.draw{display:grid;grid-template-columns:1.25fr .8fr 1fr;grid-template-rows:92mm 78mm;gap:5mm;margin-bottom:5mm}
.zone{border:1.3pt dashed #6f8ba3;border-radius:4mm;padding:3mm 4mm;font-size:11pt;color:#35506b}
.z1{grid-row:1/3}.z2{grid-row:1/3}.z3{grid-row:1}.z4{grid-row:2}
.foot>div{border:1.2pt solid #0b2540;border-radius:3mm;padding:3mm 4mm;font-size:10.5pt}.foot p{margin:1mm 0 0}'''
    return f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><title>L004 封包接力賽 列印包</title><style>{css}</style></head><body>{body}</body></html>\n'


def find_browser():
    candidates = [os.environ.get('XINEW_CHROME'), '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                  shutil.which('chromium'), shutil.which('chromium-browser'), shutil.which('google-chrome'),
                  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                  '/Applications/Chromium.app/Contents/MacOS/Chromium',
                  '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge']
    return next((c for c in candidates if c and Path(c).is_file()), None)


def main():
    D.mkdir(parents=True, exist_ok=True)
    PRINT.mkdir(parents=True, exist_ok=True)
    for name, text in FILES.items():
        assert '待編寫' not in text
        (D / name).write_text(text, encoding='utf-8')
    with (D / '03_偵探筆記.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f); w.writerow(NOTE_HEADER); w.writerows(NOTE_ROWS)
    source = PRINT / 'print-pack.html'
    source.write_text(html(), encoding='utf-8')
    browser = find_browser()
    rendered = False
    if browser:
        with tempfile.TemporaryDirectory(prefix='xinew-print-') as t:
            out = Path(t) / 'pack.pdf'
            subprocess.run([browser, '--headless', '--no-sandbox', '--disable-gpu', f'--user-data-dir={t}/profile',
                            '--no-pdf-header-footer', f'--print-to-pdf={out}', source.as_uri()],
                           check=True, capture_output=True, timeout=180)
            shutil.copyfile(out, PDF)
        rendered = True
    elif not PDF.is_file():
        raise SystemExit('No Chromium/Chrome found and no existing print pack PDF. Set XINEW_CHROME.')
    else:
        print('No browser found: kept the existing print pack PDF unchanged')

    # Validation of what is actually on disk.
    names = sorted(p.name for p in D.iterdir() if p.is_file())
    for name in FILES:
        assert (D / name).read_text(encoding='utf-8').strip()
    with (D / '03_偵探筆記.csv').open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    assert len(rows) == 6 and all(len(r) == 9 for r in rows)
    info = subprocess.run(['pdfinfo', str(PDF)], capture_output=True, text=True, check=True).stdout
    pages = int(next(x for x in info.splitlines() if x.startswith('Pages:')).split()[1])
    assert pages == 6, pages
    fonts = subprocess.run(['pdffonts', str(PDF)], capture_output=True, text=True, check=True).stdout.splitlines()[2:]
    assert fonts and all(x.split()[-5] == 'yes' for x in fonts), fonts  # every font embedded
    text = subprocess.run(['pdftotext', str(PDF), '-'], capture_output=True, text=True, check=True).stdout
    for needle in ('角色卡', '路由站 A 轉送表', '封包標籤', '家庭網路手繪圖', DEVICE, SERVER, NAME):
        assert needle in text, needle
    (E / 'qc').mkdir(exist_ok=True)
    (E / 'qc/classroom-validation.json').write_text(json.dumps({
        'folder': D.relative_to(E).as_posix(), 'files': names, 'fileCount': len(names),
        'utf8TextReadable': True, 'detectiveNotesRows': len(rows) - 1, 'detectiveNotesColumns': 9,
        'printPack': {'file': PDF.name, 'pages': pages, 'allFontsEmbedded': True, 'renderedThisRun': rendered,
                      'source': 'authoring/l004/print/print-pack.html'},
        'exampleValuesAreDocumentationReserved': [DEVICE, SERVER, '203.0.113.9', NAME, 'games.example.net'],
        'privateData': 'none', 'status': 'PASS (structure); page-by-page visual review recorded separately'},
        ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Classroom pack: {len(names)} files, print pack {pages} pages')


if __name__ == '__main__':
    main()
