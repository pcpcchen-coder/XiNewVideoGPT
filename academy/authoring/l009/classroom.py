"""Build the L009 classroom pack (real, usable materials; no private data, no real photographs).

    ./portable-runtime.sh python authoring/l009/classroom.py

The three "mock photos" are vector drawings generated here. Every name, school, address, plate,
phone number and ID number in them is invented. After any change: rerun pipeline/delivery.py, then verify.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import classroom_pack  # noqa: E402
import printpack  # noqa: E402

FONT = 'font-family="Noto Sans CJK TC,PingFang TC,Microsoft JhengHei,sans-serif"'
SKIN, LINE = '#f3c9a5', '#0b2540'

# (number, name, situation, file-info line, suggested class, clues, treatment, note)
PHOTOS = [
 ('一', '公園的紙飛機', '小宇在公園拍了自己摺的紙飛機，想放到公開的作品分享網站。',
  '拍攝時間：10 月 3 日 16:12　　位置：有（拍照時相機開著定位）',
  '可公開（分享前先關掉位置）',
  ['看不見的：檔案裡有拍攝位置', '看不見的：檔案裡有拍攝時間'],
  '分享前把位置資訊關掉。畫面上沒有臉、名字、門牌或招牌，其他不用處理。',
  '畫面上找不到線索，寶藏全部藏在檔案裡。判成「需處理（關位置）」也對。'),
 ('二', '放學後的合照', '放學後，小宇和同學在校門口合照，想貼到公開的社群網站。他還沒問同學。',
  '拍攝時間：10 月 5 日 16:00　　位置：有（拍照時相機開著定位）',
  '需處理',
  ['人：兩個人的臉', '人：名牌「三年二班 小宇」', '人：制服上的校徽', '地點：校門招牌「彩虹國小」', '地點：門牌「星星路 12 號」',
   '地點：路牌「星星路」', '文字：車牌', '文字：時鐘指著四點（放學時間）', '同意：同學還沒答應', '看不見的：檔案裡有拍攝位置和時間'],
  '先問同學；他說不要就不發。裁掉或遮住招牌、門牌、路牌、車牌和名牌，用貼圖蓋住校徽，關掉位置；'
  '或是換一個沒有招牌的背景再拍一張，而且只給朋友看。',
  '制服、校名、放學時間合在一起，別人就知道什麼時候在哪裡找得到小宇。判成「不公開」也對。'),
 ('三', '我的新學生證', '小宇拿到新的學生證很開心，想拍給全班同學的群組看。',
  '拍攝時間：10 月 6 日 19:30　　位置：沒有（拍照時相機的定位關著）',
  '不公開',
  ['文字：姓名', '文字：學校', '文字：班級', '文字：學號', '文字：生日', '人：大頭照（臉）', '文字：條碼', '文字：車票上的日期、時間和起訖站',
   '文字：便條紙上的電話', '文字：螢幕上的信箱帳號'],
  '不發。想分享開心的心情，可以只拍學生證的套子或背面，或是當面拿給同學看。',
  '姓名、學校、學號、生日和臉全在同一張照片裡，遮到看不見就沒有東西可看了。位置關著，一樣不適合發。'),
]
assert [len(p[5]) for p in PHOTOS] == [2, 10, 10]
TOTAL = sum(len(p[5]) for p in PHOTOS)


def _t(x, y, text, size, fill=LINE, weight=400, anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" {FONT}>{text}</text>'


def _kid(cx, hair, tag):
    name = ''
    if tag:
        name = (f'<rect x="{cx - 38}" y="166" width="46" height="34" rx="3" fill="#fff" stroke="#c0392b" stroke-width="1.6"/>'
                + _t(cx - 15, 178, '三年二班', 9.5, anchor='middle') + _t(cx - 15, 194, '小宇', 13.5, weight=700, anchor='middle'))
    return (f'<rect x="{cx - 24}" y="258" width="16" height="42" fill="{SKIN}"/><rect x="{cx + 8}" y="258" width="16" height="42" fill="{SKIN}"/>'
            f'<rect x="{cx - 28}" y="296" width="24" height="10" rx="4" fill="#444"/><rect x="{cx + 4}" y="296" width="24" height="10" rx="4" fill="#444"/>'
            f'<rect x="{cx - 56}" y="158" width="16" height="62" rx="7" fill="{SKIN}"/><rect x="{cx + 40}" y="158" width="16" height="62" rx="7" fill="{SKIN}"/>'
            f'<rect x="{cx - 34}" y="228" width="68" height="36" rx="5" fill="#23406b"/>'
            f'<rect x="{cx - 44}" y="150" width="88" height="86" rx="10" fill="#fff" stroke="#7f9bb3" stroke-width="1.5"/>'
            f'<rect x="{cx - 58}" y="152" width="20" height="26" rx="8" fill="#fff" stroke="#7f9bb3" stroke-width="1.5"/>'
            f'<rect x="{cx + 38}" y="152" width="20" height="26" rx="8" fill="#fff" stroke="#7f9bb3" stroke-width="1.5"/>'
            f'<path d="M{cx - 12} 150 L{cx} 166 L{cx + 12} 150 Z" fill="#dbe6ef" stroke="#7f9bb3"/>'
            f'<circle cx="{cx + 24}" cy="182" r="11" fill="#ffd34d" stroke="#b8860b" stroke-width="1.5"/>' + _t(cx + 24, 186.5, '彩', 11, weight=700, anchor='middle')
            + name +
            f'<circle cx="{cx}" cy="112" r="36" fill="{SKIN}"/>'
            f'<path d="M{cx - 36} 112 A36 36 0 0 1 {cx + 36} 112 Q{cx + 18} 86 {cx} 92 Q{cx - 18} 86 {cx - 36} 112 Z" fill="{hair}"/>'
            f'<circle cx="{cx - 12}" cy="116" r="3.6" fill="#222"/><circle cx="{cx + 12}" cy="116" r="3.6" fill="#222"/>'
            f'<path d="M{cx - 12} 128 Q{cx} 140 {cx + 12} 128" fill="none" stroke="#a0522d" stroke-width="2.4" stroke-linecap="round"/>')


def photo1():
    return ('<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg">'
            '<rect width="720" height="320" fill="#cfeafb"/><circle cx="640" cy="56" r="30" fill="#ffd34d"/>'
            '<ellipse cx="250" cy="62" rx="62" ry="17" fill="#fff"/><ellipse cx="292" cy="50" rx="40" ry="15" fill="#fff"/>'
            '<ellipse cx="500" cy="96" rx="48" ry="13" fill="#fff"/>'
            '<ellipse cx="200" cy="246" rx="340" ry="62" fill="#a9dc8f"/><ellipse cx="610" cy="252" rx="290" ry="56" fill="#9bd382"/>'
            '<rect y="238" width="720" height="82" fill="#86c96f"/>'
            '<rect x="88" y="150" width="22" height="100" fill="#8a5a35"/><circle cx="99" cy="118" r="52" fill="#4c9f4a"/>'
            '<circle cx="58" cy="142" r="34" fill="#4c9f4a"/><circle cx="142" cy="142" r="34" fill="#4c9f4a"/>'
            '<rect x="552" y="196" width="120" height="8" fill="#9a6b40"/><rect x="552" y="218" width="120" height="8" fill="#9a6b40"/>'
            '<rect x="562" y="196" width="8" height="52" fill="#7a5230"/><rect x="654" y="196" width="8" height="52" fill="#7a5230"/>'
            '<circle cx="210" cy="268" r="6" fill="#ff9aa8"/><circle cx="238" cy="284" r="6" fill="#fff38a"/><circle cx="478" cy="276" r="6" fill="#ff9aa8"/>'
            '<circle cx="508" cy="296" r="6" fill="#fff"/>'
            f'<path d="M296 320 L322 236 Q346 214 372 232 L402 320 Z" fill="{SKIN}"/><rect x="280" y="296" width="140" height="24" fill="#2f7fbf"/>'
            '<polygon points="236,176 486,92 392,214 356,186" fill="#fff" stroke="#55708a" stroke-width="2"/>'
            '<polygon points="356,186 486,92 344,232" fill="#e3ebf2" stroke="#55708a" stroke-width="2"/>'
            '<line x1="486" y1="92" x2="356" y2="186" stroke="#55708a" stroke-width="2"/>'
            f'<ellipse cx="350" cy="226" rx="30" ry="17" fill="{SKIN}" stroke="#d9a67e" stroke-width="1.5"/>'
            '</svg>')


def photo2():
    return ('<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg">'
            '<rect width="720" height="320" fill="#cfeafb"/><ellipse cx="120" cy="50" rx="56" ry="15" fill="#fff"/>'
            '<rect x="236" y="150" width="186" height="118" fill="#e9f3da"/>'
            '<rect x="0" y="124" width="204" height="144" fill="#f2dfc0" stroke="#b79c72" stroke-width="1.5"/>'
            '<rect x="200" y="112" width="40" height="156" fill="#d8bf95" stroke="#b79c72" stroke-width="1.5"/>'
            '<rect x="418" y="112" width="40" height="156" fill="#d8bf95" stroke="#b79c72" stroke-width="1.5"/>'
            '<circle cx="220" cy="86" r="25" fill="#fff" stroke="#0b2540" stroke-width="3"/>'
            '<line x1="220" y1="86" x2="220" y2="67" stroke="#0b2540" stroke-width="2.6" stroke-linecap="round"/>'
            '<line x1="220" y1="86" x2="231.5" y2="92.6" stroke="#0b2540" stroke-width="3.6" stroke-linecap="round"/>'
            '<rect x="12" y="140" width="180" height="50" rx="5" fill="#0b3a66"/>' + _t(102, 175, '彩虹國小', 30, '#fff', 700, 'middle') +
            '<polygon points="486,100 610,38 734,100" fill="#b5533c"/><rect x="500" y="100" width="220" height="168" fill="#f7c9b0" stroke="#c99a80" stroke-width="1.5"/>'
            '<rect x="606" y="170" width="62" height="98" fill="#7b4a2d"/><circle cx="656" cy="222" r="4" fill="#ffd34d"/>'
            '<rect x="520" y="118" width="60" height="42" fill="#dff1fb" stroke="#7f9bb3" stroke-width="1.5"/>'
            '<rect x="514" y="176" width="78" height="42" rx="4" fill="#1f5fa8"/>' + _t(553, 193, '星星路', 13.5, '#fff', 700, 'middle') + _t(553, 211, '12 號', 13.5, '#fff', 700, 'middle') +
            '<rect x="472" y="40" width="6" height="228" fill="#777"/><rect x="420" y="34" width="110" height="32" rx="4" fill="#1e7d4f"/>' + _t(475, 58, '星星路', 21, '#fff', 700, 'middle') +
            '<rect y="268" width="720" height="52" fill="#c9ccd1"/><line x1="0" y1="268" x2="720" y2="268" stroke="#9aa0a8" stroke-width="2"/>'
            '<rect x="640" y="214" width="96" height="40" rx="12" fill="#e9938f"/><rect x="652" y="222" width="60" height="24" rx="6" fill="#dff1fb"/>'
            '<rect x="604" y="244" width="140" height="48" rx="12" fill="#d9534f"/><circle cx="652" cy="294" r="17" fill="#333"/><circle cx="652" cy="294" r="7" fill="#aaa"/>'
            '<rect x="610" y="258" width="74" height="22" rx="2" fill="#fff" stroke="#333" stroke-width="1.5"/>' + _t(647, 274, '範例-0000', 12, weight=700, anchor='middle')
            + _kid(282, '#3a2a1c', True) + _kid(374, '#6b4423', False) + '</svg>')


def photo3():
    bars = ''.join(f'<rect x="{304 + x}" y="246" width="{w}" height="26" fill="#111"/>'
                   for x, w in zip((0, 6, 10, 18, 23, 31, 36, 44, 50, 57, 66, 71, 80, 86, 94, 101, 108, 116, 121, 130, 137, 144, 152, 158),
                                   (3, 2, 5, 2, 4, 2, 5, 3, 4, 5, 2, 5, 3, 4, 3, 4, 5, 2, 5, 4, 3, 5, 2, 4)))
    return ('<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg">'
            '<rect width="720" height="320" fill="#e9cfa6"/>'
            '<line x1="0" y1="60" x2="720" y2="52" stroke="#dcbd8e" stroke-width="2"/><line x1="0" y1="180" x2="720" y2="188" stroke="#dcbd8e" stroke-width="2"/>'
            '<line x1="0" y1="270" x2="720" y2="262" stroke="#dcbd8e" stroke-width="2"/>'
            '<rect x="18" y="12" width="268" height="124" rx="7" fill="#3b4652"/><rect x="28" y="22" width="248" height="104" fill="#eaf4fb"/>'
            '<rect x="28" y="22" width="248" height="26" fill="#35a9d6"/>' + _t(40, 41, '彩虹信箱', 15, '#fff', 700) + _t(40, 72, '帳號：', 13)
            + _t(40, 92, 'xiaoyu@mail.example', 14.5, weight=700) +
            '<rect x="40" y="102" width="70" height="18" rx="4" fill="#0b3a66"/>' + _t(75, 115, '登入', 11, '#fff', anchor='middle') +
            '<rect x="6" y="136" width="292" height="16" rx="3" fill="#9aa5b1"/>'
            '<g transform="rotate(5 628 62)"><rect x="556" y="18" width="146" height="88" fill="#fff38a" stroke="#d8c84a" stroke-width="1.2"/>'
            + _t(629, 52, '媽媽手機', 17, weight=700, anchor='middle') + _t(629, 80, '00-0000-0000', 16, anchor='middle') + '</g>'
            '<g transform="rotate(7 606 226)"><rect x="508" y="176" width="198" height="100" rx="7" fill="#ffd9b0" stroke="#c98a4b" stroke-width="1.5"/>'
            '<line x1="508" y1="206" x2="706" y2="206" stroke="#c98a4b" stroke-dasharray="4 3"/>' + _t(607, 198, '火車票', 13, '#8a5a2b', 700, 'middle')
            + _t(607, 230, '星星站 → 月亮站', 16.5, weight=700, anchor='middle') + _t(607, 250, '10 月 10 日 08:30 開', 13, anchor='middle')
            + _t(607, 268, '孩童票　3 車 12 號', 12, anchor='middle') + '</g>'
            f'<path d="M150 320 L190 262 Q214 244 240 262 L262 320 Z" fill="{SKIN}"/>'
            '<g transform="rotate(-4 340 190)"><rect x="190" y="94" width="300" height="192" rx="11" fill="#fff" stroke="#0b2540" stroke-width="2"/>'
            '<rect x="190" y="94" width="300" height="42" rx="11" fill="#1f5fa8"/><rect x="190" y="116" width="300" height="20" fill="#1f5fa8"/>'
            + _t(340, 123, '彩虹國小　學生證', 20, '#fff', 700, 'middle') +
            '<rect x="206" y="148" width="84" height="104" fill="#dfeaf2" stroke="#7f9bb3" stroke-width="1.5"/>'
            '<path d="M214 252 Q214 222 248 222 Q282 222 282 252 Z" fill="#fff" stroke="#7f9bb3"/>'
            f'<circle cx="248" cy="192" r="25" fill="{SKIN}"/><path d="M223 192 A25 25 0 0 1 273 192 Q260 174 248 178 Q236 174 223 192 Z" fill="#3a2a1c"/>'
            '<circle cx="240" cy="195" r="2.6" fill="#222"/><circle cx="256" cy="195" r="2.6" fill="#222"/>'
            '<path d="M240 203 Q248 211 256 203" fill="none" stroke="#a0522d" stroke-width="2" stroke-linecap="round"/>'
            + _t(304, 166, '姓名：王小宇', 16, weight=700) + _t(304, 189, '班級：三年二班', 14) + _t(304, 211, '學號：1140302', 14)
            + _t(304, 233, '生日：105 年 5 月 5 日', 14) + bars + '</g>'
            f'<ellipse cx="226" cy="272" rx="36" ry="20" transform="rotate(-28 226 272)" fill="{SKIN}" stroke="#d9a67e" stroke-width="1.5"/>'
            '</svg>')


SVG = {'一': photo1, '二': photo2, '三': photo3}

FILES = {
'00_爸爸先讀.md': f'''# 父子科技學院 L009：個資、照片與數位足跡（爸爸先讀）

這是**依課表製作的課前教材**，沒有真實課堂錄音，也不是實際上課紀錄。
影片先引路；真正的學習發生在孩子自己在照片裡找線索、分類、說出理由，再設計全家人都用得上的檢查表。

## 這堂課要帶走什麼

- 個資：能讓別人認出你是誰、找得到你的資料。單獨看沒什麼的資料，合在一起就更容易認出你。
- 照片裡藏著四種資訊：人、地點、文字，還有存在檔案裡、眼睛看不到的拍攝時間和位置。
- 公開範圍：公開、朋友、只有自己。設成不公開也不是保證，看到的人可以截圖轉傳。
- 數位足跡：貼出去就很難收回來；刪掉也可能還留在別的地方。
- 照片裡有別人，要先問他同不同意；他說不要就不發。
- 至少一個限制或安全注意：關掉位置資訊，別人還是可能從背景認出地點。
- 作品：**家庭發布前檢查表**，另有尋寶紀錄與一條自選家庭規則。

## 課前準備（約 20 分鐘）

1. 列印 `02_列印包_照片尋寶.pdf`（A4，共 5 頁，單面；彩色或黑白都可以）。
   三張「模擬照片」是**畫出來的圖**，人名、校名、門牌、路名、車牌、電話、學號、生日全部虛構。
2. 讀一遍 `04_模擬照片解說.md`，知道每張圖藏了哪些線索（一共 {TOTAL} 個）和建議的分類。
3. 課堂上**不要拿同學、親友或別人的真實照片來討論**。下半場要練習新照片時，請孩子自己畫一張，
   或由爸爸拿一張自己的、已經先看過的照片。
4. 先在自己的手機上找到「照片的拍攝資訊在哪裡看」和「分享時怎麼關掉位置」（見下面一節），上課時示範一次。
5. 準備鉛筆、彩色筆、幾張小貼紙（練習「遮住」），以及一張白紙（練習「裁掉」時當遮板）。
6. 錄音只保存在家裡的私人位置，不直接公開；錄音前先說課次與主題，不要唸出真實的姓名、學校、住址或電話。

## 120 分鐘怎麼走

| 分鐘 | 做什麼 | 爸爸的角色 |
|---|---|---|
| 00–10 | 任務開場：拿模擬照片一問孩子「這張可以貼出去嗎？為什麼？」 | 聽，不糾正 |
| 10–25 | 看影片，認識個資、四種資訊、公開範圍、數位足跡；讀小抄卡 | 在自己的手機上示範看一張照片的拍攝資訊 |
| 25–65 | 三張照片尋寶賽（規則見 `01`） | 當裁判、追問理由、幫忙記錄 |
| 65–75 | 休息、走動、聊天 | — |
| 75–105 | 孩子獨立改造：設計家庭發布前檢查表，加一條自選家庭規則 | 只在孩子開口時協助 |
| 105–115 | 角色互換：孩子帶爸爸檢查一張新的照片 | 當學生，故意問「只給朋友看也不行嗎？」 |
| 115–120 | 錄音總結、作品命名、版本存檔 | 問四個錄音問題，一起決定檢查表貼哪裡 |

## 位置資訊怎麼處理（請對照自己的裝置）

- Apple 的說明：「相機」App 開啟「定位服務」時，拍攝位置的座標會嵌入每個照片和影片檔；分享時，對方可以取得位置。
  也就是說，定位關著拍的照片不會有位置，所以不是每張照片都有。
- **iPhone 分享時關掉位置**：Apple「個人安全使用手冊」（2026 年 9 月版）寫的是，點一下分享按鈕，再點「選項」，關閉「位置」；
  「選項」按鈕上方會顯示「未包含位置」。iOS 18 與 iOS 26 的 iPhone 使用手冊有同樣的步驟。
  **iOS 27 的使用手冊同一頁沒有列出「位置」這一項**，所以請以你手機上實際的畫面為準。
- **讓相機不再記錄位置**：「設定」>「隱私權與安全性」>「定位服務」>「相機」，點「永不」。
- **Mac 的「照片」App**：「照片」>「設定」>「一般」，共享項目下有「包含位置資訊」（Apple 沒有說明預設是開還是關）；
  單張照片可以用「影像」>「位置」>「隱藏位置」。
- **Google 相簿**：說明寫，分享新相簿、連結、對話時，預設不會加入位置詳細資料（透過親友共享功能除外）；
  但下載後用電子郵件寄出的相片，會顯示裝置儲存的原始位置資訊。
- **通訊軟體和社群網站會不會自動移除位置資訊**：這次查不到任何一家的官方說法。教法是「分享之前自己先關掉」，不要假設平台會幫忙。
- 關掉位置也不代表別人不知道在哪裡。Google 提醒，別人仍可能根據相片中出現的地標猜出拍攝地點。
- 「在哪裡看一張照片的拍攝時間和位置」這次沒有對照官方說明，請直接在自己的裝置上找（通常在照片的資訊畫面）。

## 幾個觀念的依據與限制

- **個人資料**：個人資料保護法第 2 條列出姓名、出生年月日、國民身分證統一編號、特徵、教育、聯絡方式等，
  以及「其他得以直接或間接方式識別該個人之資料」。條文沒有逐字寫出「照片」「住址」「學校」，它們屬於能直接或間接識別的資料。
  教育部數位素養教案給孩子的說法是：只要是可以讓別人知道我們身分的資料，都算是個人資料。
- **照片的背景**：澳洲 ThinkUKnow（聯邦警察主導）提醒，穿制服、在學校或家門口拍的照片，都可能含有孩子的個人資訊和位置；
  建議檢查背景的招牌、路牌、門牌，並考慮把校徽模糊或用貼圖蓋住。
  教育部學習單寫：上傳前確認照片背景沒有個人資訊（如地址、學校名稱）。
- **螢幕、車票、證件、車牌**：這是本課自己舉的例子，沒有找到官方的兒童教材逐項列出。
- **收不回來**：美國聯邦貿易委員會（FTC）寫，貼出去的東西收不回來；就算刪掉，也可能已經被存下、分享，並永久留在網路上某處；
  看到的人都可以截圖。它也寫，即使用了隱私設定，也不可能完全控制誰看得到。這些來源用的是「可能」，不是說每一樣東西都會永遠留著。
- **同意**：FTC 寫，先得到照片裡的人同意；他說不要就不要發。教育部教案寫，將他人的照片或影片上傳到網路之前，必須先徵求對方的同意。
- **美國的 COPPA** 把含有兒童影像的照片、住址和地理位置列為個人資訊，但那是規範美國業者的規則，不適用於台灣的孩子，這裡只作對照。

## 需要協助時

- 教育部「中小學數位素養教育資源網」有個資、自拍與分享的教案和學習單：https://eliteracy.edu.tw/
- iWIN 網路內容防護機構（依兒童及少年福利與權益保障法設立）受理兒少網路內容的申訴與諮詢，網站首頁列出的諮詢專線是 02-2577-5118：https://i.win.org.tw/

## 來源（查核日 2026-10-07）

- 個人資料保護法第 2 條（臺北市法規查詢系統）：https://laws.gov.taipei/law/LawSearch/LawArticleContent/FL010627
- 教育部【個人資料正確用】教案：https://eliteracy.edu.tw/Download.ashx?id=1489
- 教育部【安全自拍與分享】學習單：https://eliteracy.edu.tw/Download.ashx?id=1506
- 教育部【躲在角落的眼睛】教案：https://eliteracy.edu.tw/Download.ashx?id=1782
- 教育部【無法鎖碼的網路內容】教案：https://eliteracy.edu.tw/Download.ashx?id=1865
- 教育部【安全自拍，安心上傳】教案：https://eliteracy.edu.tw/Download.ashx?id=1509
- Apple 個人安全使用手冊「管理『照片』中的位置後設資料」：https://support.apple.com/zh-tw/guide/personal-safety/ips0d7a5df82/web
- Apple iPhone 使用手冊「在 iPhone 上分享照片和影片」（iOS 27）：https://support.apple.com/zh-tw/guide/iphone/iphf28f17237/27/ios/27
- Apple「Mac 上的『照片』設定」：https://support.apple.com/zh-tw/guide/photos/pht5156cc968/mac
- Google 相簿說明（相片位置資訊）：https://support.google.com/photos/answer/6153599?hl=zh-Hant
- Google 相簿如何保護你的位置資料：https://support.google.com/photos/answer/11190100?hl=zh-Hant
- FTC「Heads Up: Stop. Think. Connect.」：https://consumer.ftc.gov/articles/heads-up
- FTC「Complying with COPPA: Frequently Asked Questions」：https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions
- ThinkUKnow「Home learning activity: Learning about personal information and image sharing」：https://www.thinkuknow.org.au/sites/default/files/2020-10/Home%20learning%20activity%20Learning%20about%20personal%20information%20and%20image%20sharing.pdf
- ThinkUKnow「Parental advice for posting images」：https://www.thinkuknow.org.au/sites/default/files/2023-01/ThinkUKnow%20parental%20advice%20for%20posting%20images.pdf
- Common Sense Education「Digital Trails」：https://www.commonsense.org/education/digital-citizenship/lesson/digital-trails

全國法規資料庫禁止自動擷取，個資法條文取自臺北市法規查詢系統的官方鏡像。
課表列出的三組 YouTube 連結是動態搜尋入口，不是已核對的固定影片；要用之前請爸爸先看過內容與適齡性。
''',

'01_活動規則_三張照片尋寶賽.md': f'''# 三張照片尋寶賽：規則

課表的好玩機制是「尋寶」。三張模擬照片裡一共藏了 {TOTAL} 個寶藏（藏起來的資訊）。
孩子是**尋寶隊長**，爸爸是**裁判**。不比速度，比誰找得仔細、說得出理由。

## 準備

- 三張模擬照片（列印包第 2、3 頁）。全部是畫出來的圖，內容全部虛構。
- 尋寶紀錄表（列印包第 3 頁，或 `03_尋寶紀錄.csv`）、鉛筆、小貼紙、一張當遮板的白紙。
- 尋寶小抄卡（列印包第 1 頁）放在旁邊。

## 每一張照片怎麼玩（一張約 12 分鐘）

1. **找**：先讀照片上方的「情境」，再把看到的線索一個一個圈出來。別忘了照片下方的「檔案資訊」，那是眼睛看不到的第四種。
2. **想**：回答兩個問題。「照這個情境，誰會看到這張照片？」「以後的小宇，還願意讓大家看到嗎？」
3. **決定**：在紀錄表寫下分類：可公開、需處理、不公開，並說出理由。
4. 判成「需處理」的照片，還要說出處理方法：裁掉、遮住，或是再拍一張；可以直接用貼紙和白紙在圖上試試看。
5. 裁判只問兩個問題：「你怎麼知道的？」「還有誰應該先被問過？」

## 計分

- 每找到一個解說裡有的寶藏：1 分。
- 分類並說得出理由：2 分。分類和解說不同，但理由說得通，一樣給 2 分。
- 需處理的照片，每說出一個做得到的處理方法：1 分（最多 3 分）。
- 主動說出「要先問照片裡的人」：加 2 分。

三張玩完，對照 `04_模擬照片解說.md`。孩子找到解說沒有列的線索，而且說得出道理，也給分。

## 加碼（有時間再玩）

- **藏寶換人當**：孩子在白紙上畫一張自己的「模擬照片」，至少藏五個線索，讓爸爸來找。
  規則：只能畫虛構的人和地方，不可以畫真的同學、真的校名或真的地址。
- **看不見的寶藏**：爸爸拿自己手機裡一張先看過的照片，和孩子一起看它的拍攝時間和位置。

## 結算（約 5 分鐘）

- 哪一種資訊最容易漏掉？
- 有沒有哪一張，一開始覺得可以發，後來改變想法？
- 孩子說出結論，爸爸只追問「你怎麼知道的？」

## 常見卡關

- 孩子只找臉和名字：請他看背景，再看桌上和牆上的字。
- 孩子說「只給同學看沒關係」：問他，群組裡的人可以截圖嗎？截圖以後會到哪裡？
- 孩子把三張都判成不公開：拿照片一討論，沒有人、沒有字、關掉位置之後，還剩什麼風險？
- 孩子問「那我的照片都不能貼嗎？」：可以貼，先找、先想、再決定；很多照片整理一下就可以分享。
''',

'03_尋寶紀錄_填寫說明.md': '''# 尋寶紀錄怎麼寫

`03_尋寶紀錄.csv` 可以用 Numbers 或任何試算表開啟；也可以直接寫在列印包第 3 頁。

每一張照片寫一列：

- **人、地點、文字、看不見的**：各找到什麼，簡單寫下來，例如「名牌」「門牌」「車票」「位置」。
- **誰會看到**：照情境寫：公開、朋友，或只有自己。
- **我的分類**：可公開、需處理、不公開。
- **理由**：為什麼這樣分類。
- **處理方法**：裁掉什麼、遮住什麼、要不要再拍一張、要先問誰。
- **找到幾個寶藏、得分**：照活動規則計分。

紀錄裡只寫模擬照片上的虛構內容，不要寫自己或家人真正的姓名、學校、住址和電話。
''',

'04_模擬照片解說.md': '''# 模擬照片解說（爸爸用，尋寶結束再給孩子看）

三張都是畫出來的圖，人名、校名、門牌、路名、車牌、電話、學號、生日全部虛構。
分類沒有唯一答案；孩子的分類和這裡不同，但理由說得通，就算對。

''' + ''.join(
    f'## 模擬照片{p[0]}：{p[1]}\n\n- 情境：{p[2]}\n- 檔案資訊：{p[3]}\n- 建議分類：**{p[4]}**\n- 藏了 {len(p[5])} 個寶藏：\n'
    + ''.join(f'  {i}. {c}\n' for i, c in enumerate(p[5], 1)) + f'- 建議處理：{p[6]}\n- 說明：{p[7]}\n\n' for p in PHOTOS) + '''## 可以追問的問題

- 照片一：畫面上什麼都沒有，為什麼還要檢查？位置關掉以後，別人還有沒有辦法猜到是哪個公園？
- 照片二：只遮住名牌夠不夠？校名、校徽和時鐘合在一起，說出了什麼？同學說不要的話，怎麼辦？
- 照片三：只傳到班級群組，為什麼還是不建議？如果只是想讓同學知道「我拿到學生證了」，有沒有不拍證件的方法？
- 三張都問：以後的小宇，還願意讓大家看到這張照片嗎？
''',

'05_自選規則卡.md': '''# 孩子獨立改造：加一條自己的家庭規則

選一條，或自己發明。一次只加一條，才知道它有沒有用。

## 靈感

- 穿制服的照片不公開。
- 出門玩的照片，回到家再發。
- 有別人的照片，先問過每一個人。
- 發布之前，把位置資訊關掉。
- 證件、車票、獎狀上有名字的，只給家人看。
- 發之前先放一個晚上，隔天還想發再發。
- 不確定就先存著，問爸爸。

## 我的規則卡

- 規則名稱：＿＿＿＿＿＿＿＿＿＿
- 我的規則（一句話）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 它在保護哪一種資訊？（人／地點／文字／看不見的）＿＿＿＿＿＿＿
- 用模擬照片測試：加規則之前我會怎麼做？＿＿＿＿＿＿＿＿＿＿＿＿
- 加規則之後有什麼不一樣？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 這條規則什麼時候不適用？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 要保留、修改，還是拿掉？為什麼？＿＿＿＿＿＿＿＿＿＿＿＿＿＿

把這條規則也寫到家庭發布前檢查表上，並請家裡每個人簽名。
''',

'06_驗收與回顧.md': '''# 驗收與回顧

## 驗收（孩子說明，爸爸觀察）

- [ ] 完成家庭發布前檢查表（要檢查的問題、「問過了嗎？」、一條自己的家庭規則）
- [ ] 不看稿說出發布前三步：找、想、決定
- [ ] 不看稿說出照片裡的四種資訊：人、地點、文字、看不見的拍攝時間和位置
- [ ] 尋寶紀錄表三張照片都有分類和理由
- [ ] 指出至少一個錯誤、限制或安全注意事項
- [ ] 測試過一條自選家庭規則，並說明要不要保留

## 孩子教爸爸（105–115 分鐘）

請孩子當老師，爸爸當學生。建議順序：

1. 拿出一張新的照片（孩子自己畫的模擬照片，或爸爸一張先看過的照片）。
2. 孩子拿著檢查表，一題一題問爸爸，爸爸照著回答。
3. 孩子說出這張照片的分類和理由，爸爸故意問：「只給朋友看也不行嗎？」
4. 孩子示範一種處理方法：裁掉、遮住，或再拍一張。
5. 孩子出一題考爸爸，例如：「照片刪掉以後，就一定消失了嗎？」

爸爸聽不懂就發問，不要替孩子把話說完。

## 錄音提問（115–120 分鐘，只留在家裡的私人位置）

1. 個資、照片與數位足跡，是在解決什麼？
2. 我怎麼做？
3. 哪裡容易錯？
4. 生活中哪裡會用到？

## 三句學習日誌（課後 15–30 分鐘）

- 我做了什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 哪裡卡住：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
- 下次想加什麼：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

作品命名與存放：檢查表拍照存成 `L009_家庭發布前檢查表_v01`，另存 `L009_尋寶紀錄_v01`、`L009_自選規則卡_v01`，
放進 `文件/Tech Academy/L009_個資照片與數位足跡/`，存好後再打開一次確認。
拍檢查表之前先用它檢查一次：上面有沒有寫到真的姓名或住址？紙本貼在家裡大家都看得到的地方。
''',

'07_發布前尋寶小抄.md': '''# L009 發布前尋寶小抄

## 三個步驟

1. **找**：把照片裡藏著的資訊找出來。
2. **想**：誰會看到？以後還會在網路上嗎？
3. **決定**：可公開、需處理，還是不公開。

## 照片裡的四種資訊

| 種類 | 找什麼 | 問自己 |
|---|---|---|
| 人 | 臉、名牌、制服、校徽 | 照片裡有誰？每個人都同意了嗎？ |
| 地點 | 門牌、路牌、招牌、有名的建築 | 別人看得出這是哪裡嗎？ |
| 文字 | 螢幕、文件、證件、車票 | 有沒有拍到字？放大看得清楚嗎？ |
| 看不見的 | 存在檔案裡的拍攝時間和位置 | 位置資訊關了嗎？ |

## 三種處理方法

- **裁掉**：把門牌、名牌裁到畫面外。
- **遮住**：用貼圖蓋住校徽和文字。
- **再拍一張**：換一個背景。

## 四個提醒

- 設成只給朋友看也不是保證，看到的人可以截圖轉傳。
- 貼出去就很難收回來，刪掉也可能還在別的地方。
- 關掉位置資訊，別人還是可能從背景認出地點。
- 照片裡的人說不要，就不發。

我最容易漏掉的一種資訊：＿＿＿＿＿＿　我們家的規則：＿＿＿＿＿＿＿＿＿＿＿＿
''',
}

SHEET_HEADER = ['模擬照片', '人', '地點', '文字', '看不見的', '誰會看到', '我的分類', '理由', '處理方法', '找到幾個寶藏', '得分']
SHEET_ROWS = [[f'{p[0]} {p[1]}'] for p in PHOTOS] + [['自己畫的模擬照片'], ['自選家庭規則測試']]

EXTRA_CSS = '''.kind{height:38mm;padding:3.5mm 5mm}.kind h3{font-size:16pt;margin:0 0 1mm}.kind p{margin:.8mm 0;font-size:11.5pt}
.kind .ask{font-size:10.5pt;color:#35506b;border-top:.8pt solid #9db7cc;padding-top:1.2mm;margin-top:1.5mm}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:5mm}.steps div{border:1.6pt solid #0b2540;border-radius:3mm;padding:2.5mm 4mm;font-size:11pt}
.steps b{font-size:14pt;display:block}
.act{border:1.3pt solid #35a9d6;border-radius:3mm;padding:2.5mm 5mm;margin-top:4mm;font-size:11.5pt}
.photo{border:1.6pt solid #0b2540;border-radius:3mm;padding:3mm 4mm;margin-bottom:4mm}.photo h3{font-size:13.5pt;margin:0}
.photo .sit{font-size:10.5pt;margin:.8mm 0 2mm;color:#35506b}.photo svg{display:block;width:100%;border:.8pt solid #7f9bb3;border-radius:1.5mm}
.photo .meta{font-size:10pt;margin:2mm 0 0;border:.8pt dashed #7f9bb3;border-radius:2mm;padding:1.2mm 3mm;background:#f6fafd}
.fake{display:inline-block;font-size:9pt;font-weight:400;color:#fff;background:#0b2540;border-radius:1.5mm;padding:.2mm 2mm;margin-left:2mm;vertical-align:middle}
.hunt{table-layout:fixed}.hunt th{font-size:9.5pt;padding:1mm .8mm;text-align:center}.hunt td{height:21mm;font-size:10pt}.hunt td.no{font-weight:700;text-align:center;vertical-align:middle}
.sheet{border:2pt solid #0b2540;border-radius:4mm;padding:5mm 6mm;height:236mm}.sheet h3{font-size:19pt;text-align:center;margin:0 0 1mm}
.sheet .sub{text-align:center;font-size:10.5pt;color:#35506b;margin:0 0 3mm}
.chk{table-layout:fixed}.chk th{font-size:10.5pt}.chk td{height:19.5mm;font-size:11pt}.chk td.k{font-weight:700;vertical-align:middle}.chk td.b{text-align:center;vertical-align:middle;font-size:14pt}
.res{font-size:12.5pt;margin:4mm 0 0}.sign{font-size:11pt;margin:3mm 0 0}
.plan{height:112mm;padding:4mm 6mm}.plan p{margin:1.2mm 0;font-size:11.5pt}.draw{border:1pt dashed #7f9bb3;border-radius:2mm;height:58mm;margin-top:2mm;font-size:9.5pt;color:#7f9bb3;padding:1mm 2mm}
.rule{height:104mm;padding:4mm 6mm;margin-top:6mm}.rule p{margin:1.2mm 0;font-size:11.5pt}'''


def html():
    kind = lambda name, find, ask: f'<div class="cut kind"><h3>{name}</h3><p>{find}</p><p class="ask">問自己：{ask}</p></div>'
    pages = []
    pages.append('<h2>尋寶小抄卡</h2><p class="lead">沿外框剪下，放在電腦旁邊。發布照片之前，先把這四種藏起來的資訊找出來。</p><div class="grid2">'
        + kind('一、人', '臉、名牌、制服、校徽。', '照片裡有誰？每個人都同意了嗎？')
        + kind('二、地點', '門牌、路牌、招牌、有名的建築。', '別人看得出這是哪裡嗎？')
        + kind('三、文字', '螢幕、文件、證件、車票。', '有沒有拍到字？放大看得清楚嗎？')
        + kind('四、看不見的', '存在照片檔案裡的拍攝時間和位置。', '位置資訊關了嗎？')
        + '</div><div class="steps"><div><b>1 找</b>把藏著的資訊找出來</div><div><b>2 想</b>誰會看到？以後還在網路上嗎？</div>'
        '<div><b>3 決定</b>可公開、需處理，還是不公開</div></div>'
        '<div class="act"><b>需處理的照片：</b>裁掉（把門牌、名牌裁到畫面外）・遮住（用貼圖蓋住校徽和文字）・再拍一張（換一個背景）。<br>'
        '<b>照片裡有別人：</b>先問他。只要他說不要，就不發。</div>'
        '<div class="act"><b>記得：</b>只給朋友看也可能被截圖轉傳；貼出去就很難收回來；關掉位置，別人還是可能從背景認出地點。</div>')

    def photo(p):
        return (f'<div class="photo"><h3>模擬照片{p[0]}：{p[1]}<span class="fake">虛構・畫出來的圖</span></h3><p class="sit">情境：{p[2]}</p>'
                f'{SVG[p[0]]()}<p class="meta"><b>檔案資訊（照片上看不到）</b>　{p[3]}</p></div>')
    pages.append('<h2>模擬照片一、二</h2><p class="lead">把找到的線索圈出來。人名、校名、門牌、路名和車牌都是虛構的。</p>' + photo(PHOTOS[0]) + photo(PHOTOS[1]))

    rows = ''.join(f'<tr><td class="no">{n}</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>' for n in ('一', '二', '三'))
    pages.append('<h2>模擬照片三與尋寶紀錄表</h2><p class="lead">學生證、車票、便條紙和螢幕上的內容都是虛構的。</p>' + photo(PHOTOS[2]) +
        '<table class="hunt"><tr><th style="width:7%">照片</th><th>人</th><th>地點</th><th>文字</th><th>看不見的</th>'
        '<th style="width:15%">我的分類</th><th style="width:27%">理由和處理方法</th><th style="width:8%">得分</th></tr>' + rows + '</table>'
        '<p class="note" style="margin:2mm 0 0">分類寫：可公開、需處理、不公開。每找到一個寶藏 1 分；分類並說出理由 2 分。</p>')

    check_rows = ''.join(f'<tr><td class="k">{k}</td><td>{hint}</td><td class="b">□</td></tr>' for k, hint in (
        ('人', ''), ('地點', ''), ('文字', ''), ('看不見的', ''), ('誰看得到', ''), ('問過了嗎？', ''), ('以後的我', ''), ('我們家的規則', '')))
    pages.append('<h2>作品：家庭發布前檢查表</h2><p class="lead">在每一格寫下你們家要問的問題。寫好後，全家人發布照片之前都用這一張。</p>'
        '<div class="sheet"><h3>＿＿＿＿＿家的發布前檢查表</h3><p class="sub">先找　→　再想　→　然後決定</p>'
        '<table class="chk"><tr><th style="width:19%">要檢查什麼</th><th>我們要問的問題（自己寫）</th><th style="width:11%">通過</th></tr>' + check_rows + '</table>'
        '<p class="res"><b>決定：</b>　□ 可公開　　□ 需處理（裁掉・遮住・再拍一張）　　□ 不公開</p>'
        '<p class="sign">全家人簽名：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p class="note" style="margin:3mm 0 0">名稱：L009_家庭發布前檢查表_v＿＿　日期：＿＿＿＿　這張表不要寫真的住址和電話。</p></div>')

    pages.append('<h2>處理計畫與自選家庭規則卡</h2><p class="lead">上半張給「需處理」的照片用；下半張沿外框剪下。</p>'
        '<div class="box plan"><h3>處理計畫（用模擬照片二練習）</h3>'
        '<p>我要<b>裁掉</b>：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>我要<b>遮住</b>：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>要不要<b>再拍一張</b>？換到哪裡拍？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>要先<b>問誰</b>？＿＿＿＿＿＿＿　他說不要的話：＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>位置資訊：□ 已關掉　□ 還沒　　要給誰看：□ 公開　□ 朋友　□ 只有自己</p>'
        '<div class="draw">畫出處理之後的樣子</div></div>'
        '<div class="cut rule"><h3>自選家庭規則卡</h3>'
        '<p>規則名稱：＿＿＿＿＿＿＿＿＿＿＿＿</p><p>我的規則（一句話）：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p>'
        '<p>它在保護哪一種資訊？　□ 人　□ 地點　□ 文字　□ 看不見的</p>'
        '<p>用模擬照片測試，加了規則有什麼不一樣？</p><div class="line"></div><div class="line"></div>'
        '<p>這條規則什麼時候不適用？</p><div class="line"></div>'
        '<p>□ 保留　□ 修改　□ 拿掉　　為什麼？＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿</p></div>')
    return printpack.document('L009 個資、照片與數位足跡 列印包', '父子科技學院 L009｜個資、照片與數位足跡', pages, EXTRA_CSS)


if __name__ == '__main__':
    classroom_pack.build(
        slug='l009-digital-footprint', folder='L009_個資照片與數位足跡', files=FILES,
        sheet=('03_尋寶紀錄.csv', SHEET_HEADER, SHEET_ROWS),
        pack_html=html(), pack_pdf='02_列印包_照片尋寶.pdf', pack_pages=5,
        pack_needles=('尋寶小抄卡', '模擬照片一', '模擬照片三', '虛構', '彩虹國小', '尋寶紀錄表', '家庭發布前檢查表', '自選家庭規則卡'),
        authoring_dir=Path(__file__).resolve().parent,
        extra={'mockPhotos': {'count': 3, 'kind': 'vector drawings generated by this script; no photographs of real people',
                              'allNamesPlacesNumbersInvented': True, 'labelledOnEveryPhoto': True,
                              'hiddenClues': {p[0]: len(p[5]) for p in PHOTOS}, 'totalClues': TOTAL,
                              'suggestedClasses': {p[0]: p[4] for p in PHOTOS}},
               'answersProvided': 'suggested class, clue list and treatment for the three mock photos; other reasoned answers accepted'})
