# 192 堂製作與發布進度

由 `pipeline/status.py --write` 依 production-status.json 產生。製作與發布是兩個獨立狀態。

- `completed_historical`／`published_historical`：使用者移交紀錄，本次未重驗。
- `verified`：有本集驗收證據；不表示已上傳。
- `awaiting_user_upload`：交給使用者上傳。
- `published_user_reported`：使用者回報；`published_verified`：另有實際觀察證據。
- `planned`：只規劃，尚未製作。下列課表不會觸發背景執行。

| 課號 | 主題 | 製作 | 發布 | 影片 |
|---|---|---|---|---|
| L001 | 開學任務：把 MacBook 變成我的工作站 | completed_historical | published_historical | [YouTube](https://youtu.be/JrYLz3D-7p4) |
| L002 | 檔案與資料夾尋寶 | completed_historical | published_historical | [YouTube](https://youtu.be/soztdVd9Xys) |
| L003 | 鍵盤忍者：快捷鍵競速 | verified | published_verified | [YouTube](https://youtu.be/nhWH6BQna5A) |
| L004 | 網路到底是什麼：封包接力賽 | verified | awaiting_user_upload | — |
| L005 | 搜尋高手：把大問題拆成好問題 | verified | published_verified | [YouTube](https://youtu.be/_vZlGoif3vs) |
| L006 | 真真假假：來源與證據偵探 | verified | published_verified | [YouTube](https://youtu.be/C5Aw2U88q10) |
| L007 | 密碼城堡與雙重驗證 | verified | published_verified | [YouTube](https://youtu.be/5S83wW8ojAk) |
| L008 | 釣魚郵件偵探社 | verified | published_verified | [YouTube](https://youtu.be/tZOsZSzrc34) |
| L009 | 個資、照片與數位足跡 | verified | published_verified | [YouTube](https://youtu.be/YxGX5Ax6YVs) |
| L010 | AI 是什麼、不是什麼 | verified | published_verified | [YouTube](https://youtu.be/Y5lDAh-5eFE) |
| L011 | 第一個好提示詞：任務、背景、限制、格式 | verified | awaiting_user_upload | — |
| L012 | AI 會亂講：幻覺抓錯賽 | verified | awaiting_user_upload | — |
| L013 | 文字、圖片、聲音 AI 體驗站 | verified | awaiting_user_upload | — |
| L014 | 我們家的科技公約 | planned | not_uploaded | — |
| L015 | 迷你專案：數位安全逃脫室 | planned | not_uploaded | — |
| L016 | 成果發表：我的數位公民手冊 | planned | not_uploaded | — |
| L017 | 角色真的動起來了 | planned | not_uploaded | — |
| L018 | 事件：誰先按下開始鍵 | planned | not_uploaded | — |
| L019 | 迴圈舞蹈機器人 | planned | not_uploaded | — |
| L020 | 條件判斷迷宮 | planned | not_uploaded | — |
| L021 | 變數：分數、血量與時間 | planned | not_uploaded | — |
| L022 | 隨機數與機率怪獸 | planned | not_uploaded | — |
| L023 | 廣播訊息：角色怎麼合作 | planned | not_uploaded | — |
| L024 | 分身軍團 | planned | not_uploaded | — |
| L025 | 座標、方向與碰撞 | planned | not_uploaded | — |
| L026 | 音效與節奏：用程式作曲 | planned | not_uploaded | — |
| L027 | 互動故事與分鏡 | planned | not_uploaded | — |
| L028 | 除錯偵探：找出五隻 Bug | planned | not_uploaded | — |
| L029 | 遊戲設計：先用紙玩 | planned | not_uploaded | — |
| L030 | 原創遊戲 Alpha：核心玩法 | planned | not_uploaded | — |
| L031 | 玩家測試與改版 | planned | not_uploaded | — |
| L032 | Scratch 遊戲展 | planned | not_uploaded | — |
| L033 | AI 圖像提示詞：主角、場景、動作與構圖 | planned | not_uploaded | — |
| L034 | 著作權、引用與『我真的能用嗎』 | planned | not_uploaded | — |
| L035 | AI 幫忙想故事，但人類當導演 | planned | not_uploaded | — |
| L036 | 角色設定與世界觀聖經 | planned | not_uploaded | — |
| L037 | 好聲音：距離、噪音、情緒與停頓 | planned | not_uploaded | — |
| L038 | 錄音轉文字：機器聽懂了多少 | planned | not_uploaded | — |
| L039 | 把口語整理成能讀的文字稿 | planned | not_uploaded | — |
| L040 | 簡報不是逐字稿：一頁只講一件事 | planned | not_uploaded | — |
| L041 | PPT 視覺：字體、對齊、留白與圖解 | planned | not_uploaded | — |
| L042 | TTS 配音：自然、停頓、專有名詞 | planned | not_uploaded | — |
| L043 | 剪輯節奏：畫面為什麼要換 | planned | not_uploaded | — |
| L044 | 縮圖與標題：吸引但不欺騙 | planned | not_uploaded | — |
| L045 | 兒童頻道的安全與隱私 | planned | not_uploaded | — |
| L046 | 一分鐘科普片：為什麼電池會沒電 | planned | not_uploaded | — |
| L047 | 試播會：觀眾到底聽懂了嗎 | planned | not_uploaded | — |
| L048 | 第一季首映與內容資產歸檔 | planned | not_uploaded | — |
| L049 | Python 第一行：讓電腦說話 | planned | not_uploaded | — |
| L050 | 變數：替資料貼標籤 | planned | not_uploaded | — |
| L051 | input/output：會問問題的程式 | planned | not_uploaded | — |
| L052 | if/else：猜數字對決 | planned | not_uploaded | — |
| L053 | while：直到任務完成 | planned | not_uploaded | — |
| L054 | for/range：巡邏與計數 | planned | not_uploaded | — |
| L055 | list：冒險者的背包 | planned | not_uploaded | — |
| L056 | dict：怪物圖鑑 | planned | not_uploaded | — |
| L057 | function：自訂技能卡 | planned | not_uploaded | — |
| L058 | random：命運骰子 | planned | not_uploaded | — |
| L059 | 例外處理：程式也要有安全網 | planned | not_uploaded | — |
| L060 | 檔案：讓遊戲記得你 | planned | not_uploaded | — |
| L061 | 文字 RPG 設計：地圖、事件與狀態 | planned | not_uploaded | — |
| L062 | 文字 RPG Alpha | planned | not_uploaded | — |
| L063 | 測試與除錯：找出最短破關路線 | planned | not_uploaded | — |
| L064 | 發布 v1.0：寫給玩家的說明 | planned | not_uploaded | — |
| L065 | 網頁、網站、瀏覽器與伺服器 | planned | not_uploaded | — |
| L066 | HTML 骨架：內容的房子 | planned | not_uploaded | — |
| L067 | 連結、圖片與清單 | planned | not_uploaded | — |
| L068 | CSS 上色但不失控 | planned | not_uploaded | — |
| L069 | Box Model：每個元素都有盒子 | planned | not_uploaded | — |
| L070 | Flexbox 排版挑戰 | planned | not_uploaded | — |
| L071 | 手機也要好看：Responsive | planned | not_uploaded | — |
| L072 | 可及性：不是每個人都一樣使用網頁 | planned | not_uploaded | — |
| L073 | JavaScript 第一個互動 | planned | not_uploaded | — |
| L074 | DOM：程式如何改網頁 | planned | not_uploaded | — |
| L075 | 表單與輸入驗證 | planned | not_uploaded | — |
| L076 | Local Storage：讓瀏覽器記得 | planned | not_uploaded | — |
| L077 | 網站企劃：個人科技博物館 | planned | not_uploaded | — |
| L078 | 建置 Sprint：從首頁到作品頁 | planned | not_uploaded | — |
| L079 | GitHub Pages 發布與測試 | planned | not_uploaded | — |
| L080 | 線上導覽員發表會 | planned | not_uploaded | — |
| L081 | 電、電子與安全規則 | planned | not_uploaded | — |
| L082 | Hello micro:bit：LED 與按鈕 | planned | not_uploaded | — |
| L083 | 感測器就是機器的感官 | planned | not_uploaded | — |
| L084 | 加速度計：步數與動作偵測 | planned | not_uploaded | — |
| L085 | 電子羅盤尋寶 | planned | not_uploaded | — |
| L086 | 溫度警報與舒適區 | planned | not_uploaded | — |
| L087 | Radio：兩台裝置秘密通訊 | planned | not_uploaded | — |
| L088 | 音樂、節拍與蜂鳴器 | planned | not_uploaded | — |
| L089 | 伺服馬達：讓程式真的動 | planned | not_uploaded | — |
| L090 | 資料記錄：環境偵探 | planned | not_uploaded | — |
| L091 | 從積木切換到 Python | planned | not_uploaded | — |
| L092 | 狀態機：裝置現在在做什麼 | planned | not_uploaded | — |
| L093 | 可穿戴裝置企劃 | planned | not_uploaded | — |
| L094 | 智慧房間原型 | planned | not_uploaded | — |
| L095 | 壓力測試與故障排除 | planned | not_uploaded | — |
| L096 | 家庭 Maker Faire | planned | not_uploaded | — |
| L097 | Terminal 不可怕：檔案系統指令 | planned | not_uploaded | — |
| L098 | Git 的時間機器模型 | planned | not_uploaded | — |
| L099 | GitHub Repository 與 README | planned | not_uploaded | — |
| L100 | Commit：一次只說清楚一件事 | planned | not_uploaded | — |
| L101 | Branch：安全地試新點子 | planned | not_uploaded | — |
| L102 | Issue、任務與完成定義 | planned | not_uploaded | — |
| L103 | Python Modules 與專案結構 | planned | not_uploaded | — |
| L104 | Class 與物件：會保存狀態的角色 | planned | not_uploaded | — |
| L105 | 測試：程式如何證明自己沒壞 | planned | not_uploaded | — |
| L106 | Debug 與 Logging：留下線索 | planned | not_uploaded | — |
| L107 | 演算法競賽：更快不一定更好 | planned | not_uploaded | — |
| L108 | 資料結構選擇：list、dict、set、queue | planned | not_uploaded | — |
| L109 | 和 AI Pair Programming | planned | not_uploaded | — |
| L110 | CLI 工具企劃：解決一個真問題 | planned | not_uploaded | — |
| L111 | Code Review 與 Release Candidate | planned | not_uploaded | — |
| L112 | 發布 v1.0 與回顧 | planned | not_uploaded | — |
| L113 | 資料從哪裡來：量測就是提問 | planned | not_uploaded | — |
| L114 | CSV 與表格：機器喜歡整齊 | planned | not_uploaded | — |
| L115 | 試算表公式：讓資料自己算 | planned | not_uploaded | — |
| L116 | 平均數不是唯一答案 | planned | not_uploaded | — |
| L117 | 圖表會說話，也會騙人 | planned | not_uploaded | — |
| L118 | 相關不等於因果 | planned | not_uploaded | — |
| L119 | 感測雜訊與移動平均 | planned | not_uploaded | — |
| L120 | 電池的三個基本訊號：V、I、T | planned | not_uploaded | — |
| L121 | SOC：還剩多少能量 | planned | not_uploaded | — |
| L122 | SOH 與老化：新舊電池差在哪 | planned | not_uploaded | — |
| L123 | 充電曲線與功率限制 | planned | not_uploaded | — |
| L124 | 能量、功率與電費 | planned | not_uploaded | — |
| L125 | Python 資料分析：讀檔、計算、畫圖 | planned | not_uploaded | — |
| L126 | 規則式異常偵測 | planned | not_uploaded | — |
| L127 | 資料儀表板：先回答問題再畫圖 | planned | not_uploaded | — |
| L128 | 能源科學展：結論有證據嗎 | planned | not_uploaded | — |
| L129 | 規則還是學習：怎麼讓機器做判斷 | planned | not_uploaded | — |
| L130 | 標籤與訓練資料：老師教錯會怎樣 | planned | not_uploaded | — |
| L131 | 影像分類：教電腦認爸爸和物品 | planned | not_uploaded | — |
| L132 | 聲音模型：掌聲、口令與背景噪音 | planned | not_uploaded | — |
| L133 | 姿勢模型：人體就是控制器 | planned | not_uploaded | — |
| L134 | Train／Validation／Test 三種考卷 | planned | not_uploaded | — |
| L135 | 混淆矩陣：錯在哪一類 | planned | not_uploaded | — |
| L136 | 偏差與公平：誰被資料漏掉了 | planned | not_uploaded | — |
| L137 | 神經網路直覺：很多小判斷接起來 | planned | not_uploaded | — |
| L138 | 向量與 Embedding：把意思放進地圖 | planned | not_uploaded | — |
| L139 | LLM：下一個 Token 預測機 | planned | not_uploaded | — |
| L140 | RAG：先找資料再回答 | planned | not_uploaded | — |
| L141 | Prompt 與 Evals：答案好不好要先定義 | planned | not_uploaded | — |
| L142 | AI 倫理、隱私與責任邊界 | planned | not_uploaded | — |
| L143 | AI 小幫手 Alpha | planned | not_uploaded | — |
| L144 | Model Card 與 Demo Day | planned | not_uploaded | — |
| L145 | 機器人的三段式：感知—思考—行動 | planned | not_uploaded | — |
| L146 | 馬達與機構：轉動如何變成動作 | planned | not_uploaded | — |
| L147 | 距離、光線、碰撞：機器人的感官 | planned | not_uploaded | — |
| L148 | 控制迴路：不是開了就不管 | planned | not_uploaded | — |
| L149 | 循線車模擬：規則控制 | planned | not_uploaded | — |
| L150 | 狀態機任務：巡邏、發現、追蹤、返回 | planned | not_uploaded | — |
| L151 | 藍牙與 Wi‑Fi：遙控不是魔法 | planned | not_uploaded | — |
| L152 | MQTT 與訊息主題 | planned | not_uploaded | — |
| L153 | 智慧家庭與 Home Automation 思維 | planned | not_uploaded | — |
| L154 | 機器視覺：看見不等於理解 | planned | not_uploaded | — |
| L155 | 語音介面：聽錯時怎麼辦 | planned | not_uploaded | — |
| L156 | Fail-safe：機器人首先不能傷人 | planned | not_uploaded | — |
| L157 | Robot Mission 企劃 | planned | not_uploaded | — |
| L158 | 原型整合 Sprint | planned | not_uploaded | — |
| L159 | 整合測試與故障注入 | planned | not_uploaded | — |
| L160 | Robot Challenge Day | planned | not_uploaded | — |
| L161 | 自動化、工作流與 Agent 差在哪 | planned | not_uploaded | — |
| L162 | 先畫流程再寫程式 | planned | not_uploaded | — |
| L163 | 工具就是 Agent 的手腳 | planned | not_uploaded | — |
| L164 | JSON：系統之間的共同語言 | planned | not_uploaded | — |
| L165 | HTTP 與 API：向另一個系統借能力 | planned | not_uploaded | — |
| L166 | API Key 與秘密管理 | planned | not_uploaded | — |
| L167 | Prompt Template：可重複的工作指令 | planned | not_uploaded | — |
| L168 | Context 與 Memory：記住什麼、忘掉什麼 | planned | not_uploaded | — |
| L169 | Planner／Executor／Reviewer | planned | not_uploaded | — |
| L170 | Evals：Agent 做完不代表做對 | planned | not_uploaded | — |
| L171 | 檔案自動化：整理錄音與專案 | planned | not_uploaded | — |
| L172 | 有來源的研究 Agent | planned | not_uploaded | — |
| L173 | Coding Agent 的 Repo 規則 | planned | not_uploaded | — |
| L174 | 個人學習 Agent Alpha | planned | not_uploaded | — |
| L175 | Red Team：讓 Agent 失敗給你看 | planned | not_uploaded | — |
| L176 | Agent Demo Day 與運維手冊 | planned | not_uploaded | — |
| L177 | 問題獵人：先找痛點，不急著想 App | planned | not_uploaded | — |
| L178 | 使用者訪談：問經驗，不問幻想 | planned | not_uploaded | — |
| L179 | 產品需求：要做什麼，也要說不做什麼 | planned | not_uploaded | — |
| L180 | 優先順序：時間永遠不夠 | planned | not_uploaded | — |
| L181 | 估算與拆工：大象一口一口吃 | planned | not_uploaded | — |
| L182 | 預算與金錢：每個選擇都有機會成本 | planned | not_uploaded | — |
| L183 | 時間管理：能量比行事曆更重要 | planned | not_uploaded | — |
| L184 | 溝通與衝突：批評作品，不攻擊人 | planned | not_uploaded | — |
| L185 | 急救與緊急思維 | planned | not_uploaded | — |
| L186 | 料理也是工程：量測、流程與衛生 | planned | not_uploaded | — |
| L187 | 維修思維：先診斷，不要亂拆 | planned | not_uploaded | — |
| L188 | 研究方法：主張、證據、反例與限制 | planned | not_uploaded | — |
| L189 | 畢業專題提案 | planned | not_uploaded | — |
| L190 | 畢業專題 Build Sprint | planned | not_uploaded | — |
| L191 | 正式製作：文件、影片、來源與發布 | planned | not_uploaded | — |
| L192 | 畢業與 Teach-back：換孩子教爸爸 | planned | not_uploaded | — |
