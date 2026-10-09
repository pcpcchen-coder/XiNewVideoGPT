# 父子科技學院代理接續規則

## 先讀與決策順序

1. 本次使用者指令。
2. `series-policy.json` 及其中 `episodeOverrides`：系列預設雲端製作、使用者上傳；L003 已有新指令改由本機代理接手，先讀 `docs/LOCAL_UPLOAD_L003.md`。
3. `CLOUD_START_HERE.md`、`docs/CLOUD_PRODUCTION_GUIDE.md`。
4. `curriculum/catalog.json`、`curriculum/production-status.json` 與本課 `lesson.json`。
5. 歷史文件及 L003 範例僅作證據與參考；有衝突時依上述順序。

## 執行邊界

- 每次只做指定課次；使用者明確指定起訖範圍時，允許依序逐集完成，每集保存及 commit 後再進下一集。要求「下一集」時用 `pipeline/status.py --next` 找尚未製作的課，先核對課表。<!-- academy-status:sentence -->L004、L011–L013 已由 Claude 製作並交付（verified／awaiting_user_upload，尚未上傳），不重製；下一堂是 L014「我們家的科技公約」，接手仍讀狀態表。 L005–L010 已發布，影片網址及觀察證據見狀態表，不重複上傳。<!-- /academy-status:sentence -->
- 系列預設不登入／上傳／公開 YouTube、不建立 OAuth、不安排背景批次。L003 最新明確例外是本機瀏覽器上傳並完成公開；先核對實際本機連線、頻道及既有影片。其他課次仍依原分工。
- 沒有錄音就做課前教學版並明說；不可虛構逐字稿。私人錄音只放 `lessons/Lxxx/private/`，不得進公開 Git 或交付 ZIP。
- 192 堂主題／目標以課表為準。576 組是 YouTube 搜尋入口，不是已核驗的固定影片；若選影片須逐支核對標題、網址、內容及適齡性。

## 固定系列規格

- 陳犀牛 Chen XiNew、深藍／黃／青、原片頭 v2、`zh-TW-YunJheNeural`。
- 12 頁可編輯簡報、36 句旁白、靜態畫面＋平滑淡化；教學段落無背景音樂、無推拉鏡頭。
- 120 分鐘課堂為 10／15／40／10／30／10／5 分鐘；影片長度另依實測旁白，不把兩小時寫成片長。
- 做簡報時若有當次 Presentations skill，先讀並遵循。Claude 等無 artifact-tool／skill 的環境，使用本 repo 明確提供的 `ooxml-template` 保留原可編輯版型，流程見 `docs/CLAUDE_HANDOFF.md`；不得把截圖當可編輯簡報或略過逐頁 QA。
- 新內容可調整教學圖解與版面，但需保留品牌、可編輯性與驗收；L001 版型只提供起點，不能強塞不適合的主題。

## 收尾

- 每階段記錄進度；生成依賴變動時重建下游。production/audio/subtitles/output/assets/slides/classroom 變動後重跑 verify。
- 不複製前集音檔、字幕時間、QC PASS 或發布 URL 到新課次。
- 通過技術檢查後仍需逐頁、字幕與音訊內容檢視，寫明檢查者、方法、限制；不可把機器檢查寫成人類聽審或版權通過。
- 用 `package` 產出白名單交付包，更新進度為 `verified` / `awaiting_user_upload`；已上傳與已公開分開記錄。
- 交付保存成功後才提供可下載檔案；影片 URL 由使用者回傳後記錄為使用者回報，能實際觀察才升級為已驗證。
- 修改程式與文件要回寫此 repo；大型每集成品保存在交付儲存位置並記錄完整檔名、SHA-256、大小與取得方法。
