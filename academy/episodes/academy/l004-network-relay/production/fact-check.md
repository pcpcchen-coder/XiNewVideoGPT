# L004 事實查核

查核日：2026-10-07。查核者：製作代理（Claude）。
方法：當日以網頁擷取工具讀取下列官方／原始來源，逐項抽出對應段落，再和旁白、投影片、教材逐句比對。
限制：引文由工具擷取後節錄，不是人工逐頁通讀全文；RFC 以英文原文為準，中文為本課轉述；未做任何網路實測或 macOS 實機操作。

## 主張與來源

| # | 本課的說法（幕） | 來源依據 | 結論 |
|---|---|---|---|
| 1 | 網際網路是許多網路互相連接而成的大網路（2） | RFC 1122 §1.1.2：“The Internet is a network of networks.” | 相符 |
| 2 | 網路之間由路由器互連；路由器一站一站轉送（2、4） | RFC 1122 §1.1.1：networks are interconnected using packet-switching computers called "gateways" or "IP routers"；RFC 791 §1.4：internet modules use the addresses carried in the internet header to transmit datagrams toward their destinations | 相符 |
| 3 | 資料分成許多小份，每份叫封包（2、6） | RFC 9293 §3.7：TCP packetizes a stream of bytes into TCP segments；§2.2：each TCP segment sent as an IP datagram | 相符；「封包」是通稱，嚴格名稱依層次為 segment／datagram |
| 4 | 連上網路的裝置會有 IP 位址，是一組編號（3） | Apple「在 Mac 上使用 DHCP 或手動 IP 位址」：IP 位址是在網際網路或網路上用於識別每部電腦的數字，系統會用 DHCP 指定；RFC 791 §1.1：hosts identified by fixed length addresses | 相符 |
| 5 | 每個封包帶著來源與目的地位址（3） | RFC 791 §3.1：Source Address、Destination Address 欄位 | 相符 |
| 6 | 路由器查看目的地位址決定下一站，不需要讀懂內容（3、7） | RFC 1812 §1：a router examines the IP protocol header as part of the switching process；§2.2.3：choose the address and relevant interface of the next-hop router or the destination host | 相符；「不需要讀懂內容」指轉送所需資訊在標頭，不代表內容保密（教材已說明） |
| 7 | IP 位址不是住家門牌；連到不同網路，位址通常不同（3） | RFC 791 §2.3：“An address indicates where it is.”；Apple DHCP 文件：位址由所連網路指定 | 合理推論；用「通常」，未宣稱一定改變 |
| 8 | DNS 像通訊錄，用名稱查出位址；裝置先查再送（4、5） | ICANN：“The DNS is the address book of the Internet.”“Your device uses the DNS to look up the domain name and find its associated IP address.”；Apple：DNS 伺服器會對應網域名稱至 IP 位址；RFC 1034 §2.4、§3.6 | 相符 |
| 9 | DNS 只查位址，不運送圖片（5） | RFC 1034 §2.4：name servers hold information；resolvers extract information from name servers | 相符（職責區分） |
| 10 | example.com 與 192.0.2.1 是保留給文件的範例，不是真實對應（5） | RFC 6761 §6.5：example names are reserved for use in documentation；RFC 5737 §3：192.0.2.0/24 等區塊 provided for use in documentation | 相符；教材另用 198.51.100.7、203.0.113.9、example.net，同屬保留範圍 |
| 11 | 伺服器保存資料並回應裝置的要求（2、4） | RFC 9110 §3.3：server accepts connections in order to service HTTP requests by sending HTTP responses | 相符（以網頁為例） |
| 12 | 封包帶編號，接收端依編號排回順序（6、8、9） | RFC 9293 §3.4：every octet of data has a sequence number；RFC 1122 §1.1.3：TCP provides end-to-end reliability, resequencing | 相符（指 TCP 這類規則） |
| 13 | 路由器分別處理每個封包；同一張圖的封包不一定走同一條路，可能亂序（9） | RFC 1122 §1.1.2：gateways … forwarding each IP datagram independently of other datagrams；§1.1.3：may arrive … out of order | 相符；用「不一定」，未宣稱一定走不同路 |
| 14 | 封包可能遺失；網路本身不保證送到（9） | RFC 1122 §1.1.3：no end-to-end delivery guarantees … damaged, duplicated, out of order, or not at all；RFC 791 §1.4：no acknowledgments … no retransmissions | 相符 |
| 15 | 某些傳送規則加上確認與重送；有些規則較簡單、不負責重送（9） | RFC 9293 §2.2、§3.8（TCP 重送）；RFC 768：delivery and duplicate protection are not guaranteed | 相符；旁白不點名 TCP／UDP，教材才列名稱 |
| 16 | 系統設定 → Wi-Fi →「詳細資訊」可看到 IP 位址與路由器位址（10） | Apple「Mac 上的 Wi-Fi 設定」：「詳細資訊」按鈕—檢視 IP 和路由器位址；「IP 位址」「路由器」項目 | 相符；選單依 macOS 版本可能不同，教材已註明 |
| 17 | Wi-Fi 密碼與住址不寫在作品上、不公開（10、12） | FTC：加密網路、更改預設帳密等家用 Wi-Fi 保護建議 | 屬本課的數位公民提醒，方向與 FTC 建議一致；非逐字引用 |
| 18 | 名稱打錯可能查不到，或被帶到不是想去的地方（5） | 由 #8 推得：不同名稱對應不同位址 | 推論與安全提醒，非引用 |

## 刻意避免的錯誤說法

- 沒有說「所有封包必走同一路線」，也沒有說「一定走不同路線」。
- 沒有說「所有網路協定都保證送達」；明說網路本身不保證，確認與重送是部分規則加上的。
- 沒有把 IP 位址說成住家地址或固定不變。
- 沒有把範例名稱與範例位址說成真實服務。

## 課程與素材

- 課程主題、學習目標、120 分鐘流程（10／15／40／10／30／10／5）、動手任務、作品與驗收，依 `curriculum/catalog.json` L004 核對。
- 沒有課堂錄音；本集是**依課表製作的課前教學版**，未虛構逐字稿或父子對話，封面、旁白第一句與說明均已揭露。
- 接力賽三個案件、轉送表與硬幣繞路是本課原創的教學設計，不是任何官方活動的轉載；硬幣只代表路況變化，教材已說明。
- 課表的三組 YouTube 連結是動態搜尋入口；本次沒有挑選、觀看或引用任何影片。
- 列印包範例圖為本課原創簡單圖形；角色與版型沿用系列既有素材。
