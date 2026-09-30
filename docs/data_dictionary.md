# TÀI LIỆU DATA DICTIONARY & DANH MỤC NGUỒN DỮ LIỆU ĐẦY ĐỦ
## HỆ THỐNG DỮ LIỆU NGÀNH CÔNG NGHIỆP GAME TOÀN CẦU (GLOBAL GAMING INDUSTRY ANALYTICS)

> **Đồ án:** Phân Tích Doanh Số & Cạnh Tranh Nền Tảng Ngành Công Nghiệp Game Toàn Cầu (PC vs Console vs Mobile)  
> **Môn học:** Tương tác Dữ liệu Trực quan (Interactive Data Visualization)  
> **Tổng quy mô hệ thống:** **10.757 bản ghi** qua 5 tập dữ liệu bổ trợ lẫn nhau, bao quát toàn diện 3 trụ cột nền tảng và 2 nguồn chuẩn vĩ mô toàn cầu.

---

## 🌐 1. DANH MỤC NGUỒN THU THẬP DỮ LIỆU ĐẦY ĐỦ (DATA SOURCES & CITATIONS)

Hệ thống dữ liệu của dự án được thu thập, trích xuất và đối chiếu từ các nguồn dữ liệu chính thống và uy tín nhất của ngành công nghiệp game:

### 1.1. Nguồn Dữ Liệu Console Gaming & Lịch Sử (VGChartz & IGN)
*   **Trang web thu thập:** [VGChartz Global Video Game Database](https://www.vgchartz.com/)
*   **Truy vấn trích xuất dữ liệu gốc (Endpoint Query):**  
    `https://www.vgchartz.com/games/games.php?page=1&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=1`
*   **Script cào dữ liệu:** `crawl_vgchartz.py` (Cào tự động 4.000 tựa game có lượng xuất xưởng cao nhất mọi thời đại).
*   **Nguồn tham chiếu giá bán game & Lạm phát theo thế hệ máy (MSRP Reference):**
    *   *IGN Research:* [The Real Cost of Gaming: Inflation, Time, and Purchasing Power](https://www.ign.com/articles/2013/10/15/the-real-cost-of-gaming-inflation-time-and-purchasing-power) (Giá chuẩn: Era $\le 2005 = \$50$, Era $2006-2020 = \$60$).
    *   *IGN Analysis:* [Why $70 PS5 and Xbox Series X Games Make Sense - But the Timing Couldn't Be Worse](https://www.ign.com/articles/why-70-ps5-and-xbox-series-x-games-make-sensebut-the-timing-couldnt-be-worse) (Giá chuẩn Next-Gen $\ge 2021 = \$70$).

### 1.2. Nguồn Dữ Liệu PC Gaming (Steam & SteamSpy API)
*   **Nền tảng phân phối số:** [Steam Store (Valve Corporation)](https://store.steampowered.com/)
*   **API trích xuất dữ liệu thị trường:** [SteamSpy REST API](https://steamspy.com/api.php)
*   **API Endpoints sử dụng:**
    *   `https://steamspy.com/api.php?request=all&page=1`
    *   `https://steamspy.com/api.php?request=appdetails&appid={appid}`
*   **Script cào dữ liệu:** `crawl_steamspy.py` (Trích xuất 4.000 tựa game PC có lượng người sở hữu và tương tác CCU cao nhất).

### 1.3. Nguồn Dữ Liệu Mobile Gaming (Google Play & Sensor Tower)
*   **Thư viện trích xuất API:** [Google Play Scraper API for Python (JoMingyu)](https://github.com/JoMingyu/google-play-scraper)
*   **Cửa hàng ứng dụng:** [Google Play Store Android Ecosystem](https://play.google.com/store/apps)
*   **Script cào dữ liệu:** `crawl_mobile.py` (Cào 2.720 tựa game di động phổ biến thuộc các danh mục trò chơi).
*   **Báo cáo chuẩn thể loại & Doanh thu di động toàn cầu:** [Sensor Tower - State of Gaming Market Report 2024–2026](https://sensortower.com/report/state-of-gaming-2026/download)

### 1.4. Nguồn Báo Cáo Nghiên Cứu Thị Trường Vĩ Mô (Newzoo Global Games Market Reports)
Dữ liệu thị phần (%) và tốc độ tăng trưởng (% YoY) theo 5 khu vực địa lý lớn được đối chiếu từ chuỗi báo cáo thường niên chính thức của Newzoo:
*   **Newzoo 2026 Report:** *2026 Newzoo Global Games Market Report Free Edition* (Bản PDF nội bộ).
*   **Newzoo 2025 Report:** [2025 Newzoo Free Global Games Market Report (Scribd Document 934327627)](https://www.scribd.com/document/934327627/2025-Newzoo-Free-Global-Games-Market-Report)
*   **Newzoo 2024 Report:** [2024 Newzoo Free Global Games Market Report (Scribd Document 759739689)](https://www.scribd.com/document/759739689/2024-Newzoo-Free-Global-Games-Market-Report)
*   **Newzoo 2023 Report:** [2023 Newzoo Free Global Games Market Report (Scribd Document 693940834)](https://www.scribd.com/document/693940834/2023-Newzoo-Free-Global-Games-Market-Report)
*   **Newzoo 2022 Update:** [Newzoo Global Games Market Report November 2022 Update (Scribd Document 833850227)](https://www.scribd.com/document/833850227/Newzoo-Global-Games-Market-Report-November-2022-Update)

---

## 📊 2. TỔNG QUAN DANH MỤC 5 TẬP DỮ LIỆU ĐANG SỞ HỮU

| STT | Tên File Dữ Liệu | Vị trí lưu trữ | Phân khúc / Nền tảng | Số dòng | Số cột | Vai trò trong Phân tích |
|:---:|:---|:---|:---|:---:|:---:|:---|
| **1** | **`vgchartz_games.csv`** | `data/raw/` | **Console & History** (PlayStation, Xbox, Nintendo) | **4.000** | **19** | Dữ liệu vi mô lịch sử máy chơi game Console (bản đĩa xuất xưởng, điểm số, hãng sản xuất). |
| **2** | **`steamspy_games_4000.csv`** | `data/raw/` | **PC Gaming** (Steam Ecosystem) | **4.000** | **23** | Dữ liệu vi mô nền tảng PC (lượng sở hữu, giá bán, tương tác CCU, tỷ lệ đánh giá tích cực). |
| **3** | **`mobile_playstore_games_2000+.csv`** | `data/raw/` | **Mobile Gaming** (Android Ecosystem) | **2.720** | **23** | Dữ liệu vi mô game di động (lượt tải thực tế, cờ IAP, đánh giá sao, nhà phát triển). |
| **4** | **`genre_revenue_2024_2025.csv`** | `data/external/` | **Macro Genre Benchmark** (Mobile & Steam) | **12** | **5** | Khung tham chiếu vĩ mô doanh thu theo 12 thể loại chính (Tỷ USD) dùng chuẩn hóa ARPU Mobile. |
| **5** | **`revenue_by_region(2021 - 2025).csv`** | `data/external/` | **Geographic Market Share** (Global Regions) | **25** | **5** | Dữ liệu thị phần (%) và tốc độ tăng trưởng (% YoY) của 5 khu vực địa lý phục vụ **Bản đồ Choropleth Map**. |

---

## 📖 3. DATA DICTIONARY CHI TIẾT TỪNG TẬP DỮ LIỆU

---

### 3.1. File `vgchartz_games.csv` (Console & Multiplatform History)
*Tập dữ liệu vi mô đại diện cho hệ sinh thái Console, phản ánh lịch sử hơn 4 thập kỷ phát hành game đóng hộp (Boxed/Physical copies).*

| STT | Tên Cột (`Field Name`) | Kiểu Dữ Liệu | Tỷ lệ Null thực tế | Ví dụ / Mẫu | Mô tả chi tiết & Ý nghĩa phân tích |
|:---:|:---|:---|:---:|:---|:---|
| 1 | `Pos` | Integer | 0 (0.0%) | `1`, `10`, `100` | Thứ hạng của tựa game trên bảng xếp hạng phân phối của VGChartz. |
| 2 | `Game` | String (Text) | 0 (0.0%) | `Grand Theft Auto V`, `Tetris` | Tên tựa game hoặc tên toàn bộ franchise/series. |
| 3 | `Platform` | String (Categorical) | 0 (0.0%) | `PS2`, `PS4`, `X360`, `NS`, `PC` | Hệ máy phát hành (37 hệ máy: PlayStation, Xbox, Nintendo, Sega, Atari...). |
| 4 | `Genre` | String (Categorical) | 0 (0.0%) | `Action`, `Shooter`, `Role-Playing` | Thể loại trò chơi theo hệ thống phân loại của VGChartz. |
| 5 | `Publisher` | String (Text) | 0 (0.0%) | `Nintendo`, `Electronic Arts` | Đơn vị phát hành thương mại chịu trách nhiệm đưa game ra thị trường. |
| 6 | `Developer` | String (Text) | 0 (0.0%) | `Rockstar North`, `Game Freak` | Studio trực tiếp lập trình và phát triển sản phẩm. |
| 7 | `Critic Score` | Float | 1.530 nulls (38.2%) | `9.7`, `8.4` | Điểm đánh giá bình quân từ giới phê bình chuyên nghiệp (thang điểm 10). |
| 8 | `User Score` | Float | 565 nulls (14.1%) | `8.5`, `9.2` | Điểm đánh giá bình quân từ cộng đồng game thủ (thang điểm 10). |
| 9 | `Metacritic (RAWG)` | Float | 1.797 nulls (44.9%) | `97.0`, `85.0` | Điểm Metascore chuẩn hóa từ cơ sở dữ liệu RAWG (thang điểm 100). |
| 10 | `VGChartz Score` | Float | 3.690 nulls (92.2%) | `9.0` | Điểm số độc quyền của ban biên tập VGChartz (phần lớn khuyết, ít dùng). |
| 11 | `Total Shipped` | String (Text + `m`) | **0 (0.0%)** | `"520.00m"`, `"230.00m"` | **Chỉ số Lượng cốt lõi**: Tổng số lượng bản game đã xuất xưởng toàn cầu (triệu bản). |
| 12 | `Total Sales` | Float | 4.000 nulls (100.0%) | `NaN` | *(Cột khuyết 100% trong bản cào All-time Shipped, dùng `Total Shipped` thay thế).* |
| 13 | `NA Sales` | Float | 4.000 nulls (100.0%) | `NaN` | Doanh số Bắc Mỹ *(Được bổ trợ bởi `revenue_by_region(2021 - 2025).csv`)*. |
| 14 | `PAL Sales` | Float | 4.000 nulls (100.0%) | `NaN` | Doanh số Châu Âu *(Được bổ trợ bởi `revenue_by_region(2021 - 2025).csv`)*. |
| 15 | `Japan Sales` | Float | 4.000 nulls (100.0%) | `NaN` | Doanh số Nhật Bản *(Được bổ trợ bởi `revenue_by_region(2021 - 2025).csv`)*. |
| 16 | `Other Sales` | Float | 4.000 nulls (100.0%) | `NaN` | Doanh số các vùng khác *(Được bổ trợ bởi `revenue_by_region(2021 - 2025).csv`)*. |
| 17 | `Release Date` | String (Date Text) | 417 nulls (10.4%) | `17th Sep 13`, `18th Nov 11` | Ngày phát hành ban đầu của game dạng chuỗi ngày tháng. |
| 18 | `Release Year` | Float | 417 nulls (10.4%) | `2013.0`, `2011.0` | Năm phát hành (1971 – 2025), phục vụ phân tích chuỗi thời gian. |
| 19 | `Last Update` | String (Date Text) | 1.223 nulls (30.6%) | `27th Feb 20` | Ngày hệ thống VGChartz cập nhật lại số liệu xuất xưởng gần nhất. |

---

### 3.2. File `steamspy_games_4000.csv` (PC Platform - Steam Ecosystem)
*Tập dữ liệu vi mô đại diện cho phân khúc máy tính cá nhân (PC Gaming) thông qua nền tảng phân phối số Steam lớn nhất hành tinh.*

| STT | Tên Cột (`Field Name`) | Kiểu Dữ Liệu | Tỷ lệ Null thực tế | Ví dụ / Mẫu | Mô tả chi tiết & Ý nghĩa phân tích |
|:---:|:---|:---|:---:|:---|:---|
| 1 | `appid` | Integer | 0 (0.0%) | `730`, `1172470` | Mã định danh duy nhất (Steam AppID) của tựa game trên Steam Store. |
| 2 | `name` | String (Text) | 0 (0.0%) | `Counter-Strike: Global Offensive` | Tên thương mại chính thức của trò chơi trên Steam. |
| 3 | `genre` | String (Categorical) | 0 (0.0%) | `Action`, `Strategy`, `RPG` | Thể loại chính của game do nhà phát hành khai báo. |
| 4 | `tags` | String (JSON/Text) | 251 nulls (6.3%) | `{'FPS': 92348, 'Action': 89201}` | Chuỗi từ khóa/thẻ tag do cộng đồng người chơi bình chọn. |
| 5 | `game_mode` | String (Text) | 236 nulls (5.9%) | `Single-player`, `Multi-player` | Chế độ chơi: Chơi đơn, Chơi mạng, Co-op. |
| 6 | `developer` | String (Text) | 13 nulls (0.3%) | `Valve`, `Respawn Entertainment` | Studio lập trình và phát triển trò chơi. |
| 7 | `publisher` | String (Text) | 20 nulls (0.5%) | `Valve`, `Electronic Arts` | Công ty phát hành thương mại. |
| 8 | `release_date` | String (Date) | 0 (0.0%) | `Aug 21, 2012` | Ngày phát hành chính thức trên Steam. |
| 9 | `release_year` | Integer | 0 (0.0%) | `2012` | Năm phát hành của game trên Steam (1997 – 2025). |
| 10 | `owners` | String (Range) | **0 (0.0%)** | `"100,000,000 .. 200,000,000"` | **Chỉ số Lượng cốt lõi**: Khoảng ước tính số tài khoản sở hữu game. |
| 11 | `price` | Integer | 0 (0.0%) | `2999` (\$29.99), `0` (Free) | Giá bán thực tế hiện tại tính bằng **cents USD** (cần chia 100). |
| 12 | `initialprice` | Integer | 0 (0.0%) | `3999` (\$39.99) | Giá niêm yết gốc ban đầu tính bằng **cents USD** khi chưa giảm giá. |
| 13 | `discount` | Integer | 0 (0.0%) | `0`, `25`, `50`, `75` | Tỷ lệ phần trăm giảm giá đang được áp dụng. |
| 14 | `positive` | Integer | 0 (0.0%) | `7642084` | Số lượt đánh giá tích cực (Upvote/Thumb-up) từ game thủ. |
| 15 | `negative` | Integer | 0 (0.0%) | `1173003` | Số lượt đánh giá tiêu cực (Downvote/Thumb-down) từ game thủ. |
| 16 | `userscore` | Integer | 0 (0.0%) | `0` | Điểm đánh giá người dùng (phần lớn = 0 do hạn chế SteamSpy v2 API). |
| 17 | `metacritic_score` | String / Object | 236 nulls (5.9%) | `88`, `NaN` | Điểm số phê bình Metacritic chính thức trên Steam (thang 100). |
| 18 | `ccu` | Integer | 0 (0.0%) | `1013936`, `450` | Lượng người chơi cùng lúc cao nhất (Peak Concurrent Users) gần nhất. |
| 19 | `average_forever` | Integer | 0 (0.0%) | `32560` (phút) | Thời gian chơi trung bình trọn đời của mỗi tài khoản (phút). |
| 20 | `average_2weeks` | Integer | 0 (0.0%) | `850` (phút) | Thời gian chơi trung bình trong 2 tuần gần nhất (phút). |
| 21 | `median_forever` | Integer | 0 (0.0%) | `6450` (phút) | Giá trị trung vị thời gian chơi trọn đời (phút). |
| 22 | `median_2weeks` | Integer | 0 (0.0%) | `0` (phút) | Giá trị trung vị thời gian chơi 2 tuần gần nhất (phút). |
| 23 | `score_rank` | Float | 3.998 nulls (100.0%) | `NaN` | Thứ hạng điểm số (khuyết 100%, không sử dụng). |

---

### 3.3. File `mobile_playstore_games_2000+.csv` (Mobile Platform - Google Play)
*Tập dữ liệu vi mô đại diện cho hệ sinh thái Game di động trên Android, phản ánh mô hình Free-to-Play, lượt tải và thanh toán trong ứng dụng (IAP).*

| STT | Tên Cột (`Field Name`) | Kiểu Dữ Liệu | Tỷ lệ Null thực tế | Ví dụ / Mẫu | Mô tả chi tiết & Ý nghĩa phân tích |
|:---:|:---|:---|:---:|:---|:---|
| 1 | `app_id` | String (Categorical) | 0 (0.0%) | `com.alexanderwinn.landfall` | Định danh gói ứng dụng (Package Name) duy nhất trên Google Play (Primary Key). |
| 2 | `title` | String (Text) | 0 (0.0%) | `TerraGenesis: Landfall` | Tên chính thức của tựa game di động. |
| 3 | `genre` | String (Categorical) | 0 (0.0%) | `Simulation`, `Strategy`, `Action` | Tên thể loại trò chơi theo Google Play Store. |
| 4 | `genre_id` | String (Categorical) | 0 (0.0%) | `GAME_SIMULATION` | Mã định danh thể loại chuẩn hóa theo hệ thống Android. |
| 5 | `realInstalls` | Integer | **0 (0.0%)** | `1733498`, `50000000` | **Chỉ số Lượng cốt lõi**: Ước tính số lượt cài đặt thực tế chính xác của trò chơi. |
| 6 | `min_installs` | Integer | 0 (0.0%) | `1000000` | Mốc phân nhóm lượt cài đặt tối thiểu hiển thị công khai. |
| 7 | `installs_range` | String (Categorical) | 0 (0.0%) | `"1,000,000+"` | Khoảng phân cấp lượt tải hiển thị cho người dùng. |
| 8 | `score` | Float | 0 (0.0%) | `4.39`, `4.57` | Điểm đánh giá trung bình từ người dùng (thang điểm 5 sao). |
| 9 | `ratings` | Integer | 0 (0.0%) | `42012`, `1500000` | Tổng số lượng người dùng đã chấm điểm sao. |
| 10 | `reviews` | Integer | 0 (0.0%) | `2006`, `85400` | Tổng số lượt nhận xét/bình luận dạng văn bản. |
| 11 | `price_usd` | Float | 0 (0.0%) | `0.0`, `1.99` | Giá tải xuống ban đầu tính bằng USD (đa phần = 0 do là game Free-to-Play). |
| 12 | `is_free` | Boolean | 0 (0.0%) | `True`, `False` | Cờ phân phối: `True` (Tải miễn phí), `False` (Phải trả phí tải ban đầu). |
| 13 | `currency` | String (Categorical) | 0 (0.0%) | `USD` | Đơn vị tiền tệ của giá tải (chuẩn hóa USD). |
| 14 | `offersIAP` | Boolean | 0 (0.0%) | `True`, `False` | Trò chơi có tích hợp tính năng Mua vật phẩm trong ứng dụng (IAP) hay không. |
| 15 | `inAppProductPrice` | String (Text) | 270 nulls (9.9%) | `$0.49 - $99.99 per item` | Dải giá của các gói nạp vật phẩm/tiền ảo trong game. |
| 16 | `developer` | String (Text) | 0 (0.0%) | `Tilting Point`, `Supercell` | Tên nhà phát triển hoặc đơn vị phát hành trò chơi. |
| 17 | `developer_id` | String (Categorical) | 0 (0.0%) | `5479878731323183535` | ID định danh tài khoản nhà phát triển trên hệ thống Google Play. |
| 18 | `released` | String (Date Text) | 12 nulls (0.4%) | `Aug 9, 2022` | Ngày phát hành chính thức ban đầu của trò chơi. |
| 19 | `release_year` | Float | 12 nulls (0.4%) | `2022.0` | Năm phát hành trích xuất (2010 – 2025). |
| 20 | `version` | String (Text) | 0 (0.0%) | `2.92`, `1.72.65` | Phiên bản ứng dụng cập nhật tại thời điểm thu thập dữ liệu. |
| 21 | `content_rating` | String (Categorical) | 0 (0.0%) | `Everyone`, `Teen`, `Mature 17+` | Phân loại độ tuổi và kiểm duyệt nội dung của Google Play. |
| 22 | `description` | String (Text) | 0 (0.0%) | `"From the makers of..."` | Đoạn tóm tắt mô tả nội dung gameplay của trò chơi. |
| 23 | `playstore_url` | String (URL) | 0 (0.0%) | `https://play.google.com/...` | Đường link truy cập trang chi tiết sản phẩm trên Google Play Store. |

---

### 3.4. File `genre_revenue_2024_2025.csv` (Macro Industry Benchmark)
*Tập dữ liệu chuẩn vĩ mô cung cấp tổng doanh thu thực tế cấp ngành của 12 thể loại game lớn trong 2 năm 2024 và 2025 (Nguồn: Sensor Tower & Steam Market Reports).*

| STT | Tên Cột (`Field Name`) | Kiểu Dữ Liệu | Tỷ lệ Null | Ví dụ / Mẫu | Mô tả chi tiết & Ý nghĩa phân tích |
|:---:|:---|:---|:---:|:---|:---|
| 1 | `Genre` | String (Categorical) | 0 (0.0%) | `Strategy`, `RPG`, `Action` | Tên của 12 thể loại game cốt lõi trên thị trường toàn cầu. |
| 2 | `Mobile_Revenue_2024_USD_Billion` | Float | 0 (0.0%) | `19.0`, `17.5`, `14.5` | Tổng doanh thu thị trường Mobile toàn cầu năm 2024 theo thể loại (đơn vị: Tỷ USD). |
| 3 | `Mobile_Revenue_2025_USD_Billion` | Float | 0 (0.0%) | `22.0`, `16.0`, `16.5` | Tổng doanh thu thị trường Mobile toàn cầu năm 2025 theo thể loại (đơn vị: Tỷ USD). |
| 4 | `Steam_Revenue_2024_USD_Billion` | Float | 0 (0.0%) | `1.1`, `3.0`, `3.2` | Tổng doanh thu nền tảng PC Steam năm 2024 theo thể loại (đơn vị: Tỷ USD). |
| 5 | `Steam_Revenue_2025_USD_Billion` | Float | 0 (0.0%) | `1.2`, `2.7`, `4.2` | Tổng doanh thu nền tảng PC Steam năm 2025 theo thể loại (đơn vị: Tỷ USD). |

---

### 3.5. File `revenue_by_region(2021 - 2025).csv` (Geographic Market Share Benchmark)
*Tập dữ liệu chuẩn vĩ mô từ Newzoo bóc tách tỷ trọng thị phần (%) và tốc độ tăng trưởng (% YoY) của 5 khu vực địa lý lớn trong 5 năm liên tiếp (2021–2025), dùng để trực quan hóa bản đồ **Choropleth Map**.*

| STT | Tên Cột (`Field Name`) | Kiểu Dữ Liệu | Tỷ lệ Null | Ví dụ / Mẫu | Mô tả chi tiết & Ý nghĩa phân tích |
|:---:|:---|:---|:---:|:---|:---|
| 1 | `Region` | String (Categorical) | 0 (0.0%) | `Asia-Pacific`, `North America` | Tên khu vực địa lý toàn cầu (5 khu vực: APAC, NA, EU, LATAM, MENA). |
| 2 | `Region_Code` | String (Categorical) | 0 (0.0%)* | `APAC`, `NA`, `EU`, `LATAM`, `MENA` | Mã viết tắt chuẩn của khu vực. *(Lưu ý: Mã `"NA"` là North America, cần tránh bị thư viện đọc nhầm thành `NaN`)*. |
| 3 | `Year` | Integer | 0 (0.0%) | `2021`, `2022`, `2023`, `2024`, `2025` | Năm ghi nhận dữ liệu chuỗi thời gian 5 năm liên tiếp (từ đỉnh COVID-19 đến nay). |
| 4 | `Share_Pct` | Float | 0 (0.0%) | `48.3`, `26.5`, `17.7`, `4.2`, `3.3` | **Tỷ trọng thị phần đóng góp vào doanh thu toàn cầu (%)** của khu vực trong năm đó. |
| 5 | `YoY_Growth_Pct` | Float | 5 nulls (20.0%) | `-5.6`, `1.7`, `3.4`, `6.6` | Tốc độ tăng trưởng doanh thu so với năm trước (% YoY). Trống ở năm gốc 2021. |

---

## 🧮 4. NGUYÊN TẮC CHUẨN HÓA & 5 CALCULATED FIELDS BẮT BUỘC

Do 3 nền tảng đo lường bằng các đơn vị khác nhau (Console = Bản xuất xưởng, Steam = Khoảng tài khoản sở hữu, Mobile = Lượt tải), Pipeline ETL Python sẽ tạo ra **5 trường dữ liệu tính toán chuẩn hóa**:

### 4.1. Chỉ số Quy mô về LƯỢNG (`Volume_Units`)
*   **Console:** `Volume_Units` = `Total_Shipped` quy đổi sang số nguyên (bỏ chữ `m`, nhân với $1.000.000$).
*   **PC (Steam):** `Volume_Units` = `Midpoint(owners)`  
    $$\text{Midpoint} = \frac{\text{Min\_Owners} + \text{Max\_Owners}}{2} \quad (\text{VD: } \text{'10M .. 20M'} \longrightarrow 15.000.000)$$
*   **Mobile:** `Volume_Units` = `realInstalls` (Lượt tải thực tế).

### 4.2. Chỉ số Doanh số về GIÁ TRỊ (`Harmonized_Revenue_USD`)
*   **Console:** Áp dụng mô hình **Generational Baseline MSRP** (Dựa trên nghiên cứu giá bán của IGN/Circana):
    $$\text{Harmonized\_Revenue}_{\text{Console}} = \text{Volume\_Units} \times \text{MSRP}_{\text{Era}}$$
    *(Trong đó: $\text{MSRP} = \$50$ nếu Năm $\le 2005$; $\text{MSRP} = \$60$ nếu $2006 \le \text{Năm} \le 2020$; $\text{MSRP} = \$70$ nếu $\ge 2021$).*
*   **PC (Steam):** Áp dụng giá sau chiết khấu:
    $$\text{Harmonized\_Revenue}_{\text{PC}} = \text{Volume\_Units} \times \left(\frac{\text{price}}{100} \times (1 - \frac{\text{discount}}{100})\right)$$
*   **Mobile:** Áp dụng tỷ trọng doanh thu thể loại Sensor Tower:
    $$\text{Harmonized\_Revenue}_{\text{Mobile}} = \text{realInstalls} \times \text{ARPU}_{\text{Genre}} + (\text{price\_usd} \times \text{realInstalls})$$
    *(Trong đó $\text{ARPU}_{\text{Genre}} = \frac{\text{SensorTower\_Revenue}(\text{Genre})}{\sum \text{realInstalls}(\text{Genre})}$).*

### 4.3. Thang Điểm Đánh Giá Chuẩn Hóa (`Standardized_Rating` 0 – 100)
Toàn bộ hệ thống đánh giá được đưa về thang chuẩn **0 – 100**:
$$\text{Standardized\_Rating} = 
\begin{cases} 
\text{Critic Score} \times 10 & \text{(Console: thang 0--10)} \\
\text{Metacritic Score} & \text{(Console/PC: thang 0--100)} \\
\dfrac{\text{positive}}{\text{positive} + \text{negative}} \times 100 & \text{(PC Steam: Tỷ lệ \% đánh giá tích cực)} \\
\text{score} \times 20 & \text{(Mobile: thang 0--5 sao)}
\end{cases}$$

### 4.4. Phân Nhóm Chất Lượng (`Rating_Tier` / `Rating_Class`)
*   `Masterpiece`: $\ge 85$ điểm
*   `Great`: $75 - 84$ điểm
*   `Mixed / Average`: $50 - 74$ điểm
*   `Poor / Flop`: $< 50$ điểm

### 4.5. Nhãn Nhận Diện Đa Nền Tảng (`Is_CrossPlatform`)
*   Thuật toán so khớp chuỗi tiêu đề (`Game_Title`) chuẩn hóa chữ thường và loại bỏ ký tự đặc biệt.
*   Nếu tựa game xuất hiện trên $\ge 2$ nền tảng khác nhau $\longrightarrow \text{Is\_CrossPlatform} = \text{True}$.
*   Ngược lại $\longrightarrow \text{Is\_CrossPlatform} = \text{False}$ (Game độc quyền / Exclusive).

---

## ⚠️ 5. LƯU Ý KỸ THUẬT QUAN TRỌNG KHI XỬ LÝ (DATA GOTCHAS)

1. **Vấn đề Mã Vùng `NA` trong `revenue_by_region(2021 - 2025).csv`:**  
   Thư viện Pandas khi dùng lệnh `pd.read_csv()` mặc định sẽ hiểu chuỗi ký tự `"NA"` (North America) là giá trị rỗng (`NaN`).  
   *Giải pháp bắt buộc:* Thêm tham số `keep_default_na=False` hoặc cấu hình `na_values=['']` khi đọc file để giữ nguyên mã vùng `NA`.

2. **Cột Doanh số rỗng trong `vgchartz_games.csv`:**  
   Các cột `Total Sales`, `NA Sales`, `PAL Sales`, `Japan Sales`, `Other Sales` bị rỗng 100% trong bản cào all-time của VGChartz vì hệ thống hiển thị `Total Shipped`.  
   *Giải pháp:* Dùng cột `Total Shipped` (đầy đủ 100%) làm chỉ số lượng cho Console, và sử dụng file `revenue_by_region(2021 - 2025).csv` làm căn cứ phân rã địa lý cho bản đồ Choropleth Map.

3. **Đơn vị Cents của Steam:**  
   Các cột `price` và `initialprice` trong `steamspy_games_4000.csv` đang lưu ở đơn vị **cents**. Khi tính toán bắt buộc phải chia cho `100` để quy đổi về đơn vị **USD**.
