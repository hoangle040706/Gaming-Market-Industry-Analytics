# DATA DICTIONARY (TỪ ĐIỂN DỮ LIỆU)

---

## 1. BẢNG `vgchartz_games.csv` (Console & History)
* **Nguồn:** [VGChartz Global Database](https://www.vgchartz.com/)

| Tên Cột | Ví Dụ Dữ Liệu | Ý Nghĩa / Mô Tả | Nguồn Dữ Liệu |
| :--- | :--- | :--- | :--- |
| `Pos` | `1` | Thứ hạng của tựa game trên bảng xếp hạng VGChartz | VGChartz |
| `Game` | `Grand Theft Auto V` | Tên tựa game / thương hiệu trò chơi | VGChartz |
| `Platform` | `PS4`, `X360`, `NS` | Hệ máy / nền tảng phát hành game | VGChartz |
| `Genre` | `Action`, `Shooter` | Thể loại trò chơi | VGChartz |
| `Publisher` | `Nintendo`, `Electronic Arts` | Công ty phát hành game ra thị trường | VGChartz |
| `Developer` | `Rockstar North` | Studio trực tiếp lập trình và phát triển game | VGChartz |
| `Critic Score` | `9.7` | Điểm đánh giá từ các nhà phê bình chuyên môn (thang 10) | VGChartz |
| `User Score` | `8.5` | Điểm đánh giá bình quân từ cộng đồng người chơi (thang 10) | VGChartz |
| `Metacritic (RAWG)` | `97.0` | Điểm Metascore tổng hợp từ RAWG (thang 100) | RAWG / Metacritic |
| `VGChartz Score` | `9.0` | Điểm số do ban biên tập VGChartz đánh giá | VGChartz |
| `Total Shipped` | `520.00m` | Tổng số lượng bản game đã xuất xưởng toàn cầu (triệu bản) | VGChartz |
| `Total Sales` | `NaN` | Tổng doanh số bán lẻ toàn cầu | VGChartz |
| `NA Sales` | `NaN` | Doanh số tại thị trường Bắc Mỹ | VGChartz |
| `PAL Sales` | `NaN` | Doanh số tại thị trường Châu Âu | VGChartz |
| `Japan Sales` | `NaN` | Doanh số tại thị trường Nhật Bản | VGChartz |
| `Other Sales` | `NaN` | Doanh số tại các khu vực còn lại | VGChartz |
| `Release Date` | `17th Sep 13` | Ngày phát hành chính thức của trò chơi | VGChartz |
| `Release Year` | `2013` | Năm phát hành trò chơi | VGChartz |
| `Last Update` | `27th Feb 20` | Ngày hệ thống VGChartz cập nhật số liệu gần nhất | VGChartz |

---

## 2. BẢNG `steamspy_games_4000.csv` (PC Gaming - Steam)
* **Nguồn:** [SteamSpy API](https://steamspy.com/api.php) & [Steam Store](https://store.steampowered.com/)

| Tên Cột | Ví Dụ Dữ Liệu | Ý Nghĩa / Mô Tả | Nguồn Dữ Liệu |
| :--- | :--- | :--- | :--- |
| `appid` | `730` | Mã định danh duy nhất của game trên Steam (Steam AppID) | Steam / SteamSpy |
| `name` | `Counter-Strike: Global Offensive` | Tên chính thức của tựa game trên Steam | Steam |
| `genre` | `Action` | Thể loại chính của trò chơi | Steam |
| `tags` | `{'FPS': 92348, 'Action': 89201}` | Thẻ phân loại và số lượt bình chọn từ cộng đồng Steam | Steam |
| `game_mode` | `Multi-player`, `Single-player` | Chế độ chơi (Chơi đơn, Nhiều người, Co-op) | Steam |
| `developer` | `Valve` | Studio trực tiếp phát triển trò chơi | Steam |
| `publisher` | `Valve` | Nhà phát hành thương mại của trò chơi | Steam |
| `release_date` | `Aug 21, 2012` | Ngày phát hành trên nền tảng Steam | Steam |
| `release_year` | `2012` | Năm phát hành trên Steam | Steam |
| `owners` | `100,000,000 .. 200,000,000` | Khoảng ước tính số tài khoản sở hữu game | SteamSpy API |
| `price` | `2999` (tương đương $29.99) | Giá bán hiện tại của game (đơn vị: Cents USD) | Steam Store |
| `initialprice` | `3999` (tương đương $39.99) | Giá niêm yết gốc ban đầu chưa giảm giá (đơn vị: Cents USD) | Steam Store |
| `discount` | `25` (giảm 25%) | Tỷ lệ phần trăm giảm giá đang áp dụng | Steam Store |
| `positive` | `7642084` | Tổng số lượt đánh giá tích cực (Thích / Upvote) | Steam Store |
| `negative` | `1173003` | Tổng số lượt đánh giá tiêu cực (Không thích / Downvote) | Steam Store |
| `userscore` | `0` | Điểm đánh giá người dùng nội bộ | SteamSpy API |
| `metacritic_score` | `88` | Điểm số phê bình Metacritic chính thức trên Steam | Metacritic / Steam |
| `ccu` | `1013936` | Lượng người chơi cùng lúc cao nhất (Peak Concurrent Users) | SteamSpy API |
| `average_forever` | `32560` (phút) | Thời gian chơi trung bình trọn đời của người dùng (phút) | SteamSpy API |
| `average_2weeks` | `850` (phút) | Thời gian chơi trung bình trong 2 tuần gần nhất (phút) | SteamSpy API |
| `median_forever` | `6450` (phút) | Trung vị thời gian chơi trọn đời của người dùng (phút) | SteamSpy API |
| `median_2weeks` | `0` (phút) | Trung vị thời gian chơi trong 2 tuần gần nhất (phút) | SteamSpy API |
| `score_rank` | `NaN` | Thứ hạng điểm số do SteamSpy tính | SteamSpy API |

---

## 3. BẢNG `mobile_playstore_games_2000+.csv` (Mobile Gaming - Google Play)
* **Nguồn:** [Google Play Store qua google-play-scraper](https://github.com/JoMingyu/google-play-scraper)

| Tên Cột | Ví Dụ Dữ Liệu | Ý Nghĩa / Mô Tả | Nguồn Dữ Liệu |
| :--- | :--- | :--- | :--- |
| `app_id` | `com.alexanderwinn.landfall` | Mã định danh gói ứng dụng (Package Name) duy nhất trên Google Play | Google Play Store |
| `title` | `TerraGenesis: Landfall` | Tên chính thức của tựa game trên Play Store | Google Play Store |
| `genre` | `Simulation` | Tên thể loại trò chơi | Google Play Store |
| `genre_id` | `GAME_SIMULATION` | Mã định danh thể loại chuẩn hóa theo Google Play | Google Play Store |
| `realInstalls` | `1733498` | Số lượt cài đặt thực tế ước tính của trò chơi | Google Play Store |
| `min_installs` | `1000000` | Mốc số lượt cài đặt tối thiểu hiển thị công khai | Google Play Store |
| `installs_range` | `1,000,000+` | Khoảng phân cấp lượt tải hiển thị cho người dùng | Google Play Store |
| `score` | `4.39` | Điểm đánh giá trung bình từ người dùng (thang điểm 5 sao) | Google Play Store |
| `ratings` | `42012` | Tổng số lượng người dùng đã chấm điểm sao | Google Play Store |
| `reviews` | `2006` | Tổng số lượt nhận xét / bình luận dạng văn bản | Google Play Store |
| `price_usd` | `0.0` | Giá tải xuống ban đầu tính bằng USD | Google Play Store |
| `is_free` | `True` | Game tải miễn phí (`True`) hay trả phí (`False`) | Google Play Store |
| `currency` | `USD` | Đơn vị tiền tệ của giá tải game | Google Play Store |
| `offersIAP` | `True` | Game có tính năng mua vật phẩm trong ứng dụng (In-App Purchases) không | Google Play Store |
| `inAppProductPrice` | `$0.49 - $99.99 per item` | Dải giá của các gói vật phẩm / tiền ảo trong game | Google Play Store |
| `developer` | `Tilting Point` | Tên nhà phát triển hoặc đơn vị phát hành trò chơi | Google Play Store |
| `developer_id` | `5479878731323183535` | ID định danh tài khoản nhà phát triển trên Google Play | Google Play Store |
| `released` | `Aug 9, 2022` | Ngày phát hành đầu tiên trên Play Store | Google Play Store |
| `release_year` | `2022` | Năm phát hành của trò chơi | Google Play Store |
| `version` | `2.92` | Phiên bản cập nhật hiện tại của ứng dụng | Google Play Store |
| `content_rating` | `Everyone` | Phân loại độ tuổi và kiểm duyệt nội dung | Google Play Store |
| `description` | `"From the makers of..."` | Đoạn tóm tắt giới thiệu nội dung trò chơi | Google Play Store |
| `playstore_url` | `https://play.google.com/store/apps/details?id=...` | Đường dẫn link trực tiếp đến trang game trên Google Play | Google Play Store |

---

## 4. BẢNG `genre_revenue_2024_2025.csv` (Tham Chiếu Thể Loại Vĩ Mô)
* **Nguồn:** [Sensor Tower State of Gaming Report](https://sensortower.com/report/state-of-gaming-2026/download) & Steam Market Reports

| Tên Cột | Ví Dụ Dữ Liệu | Ý Nghĩa / Mô Tả | Nguồn Dữ Liệu |
| :--- | :--- | :--- | :--- |
| `Genre` | `Strategy`, `RPG`, `Action` | Tên 12 thể loại trò chơi cốt lõi toàn cầu | Sensor Tower & Steam |
| `Mobile_Revenue_2024_USD_Billion` | `19.0` | Doanh thu toàn cầu của thể loại trên Mobile năm 2024 (Tỷ USD) | Sensor Tower |
| `Mobile_Revenue_2025_USD_Billion` | `22.0` | Doanh thu toàn cầu của thể loại trên Mobile năm 2025 (Tỷ USD) | Sensor Tower |
| `Steam_Revenue_2024_USD_Billion` | `1.1` | Doanh thu toàn cầu của thể loại trên PC Steam năm 2024 (Tỷ USD) | Steam Market Reports |
| `Steam_Revenue_2025_USD_Billion` | `1.2` | Doanh thu toàn cầu của thể loại trên PC Steam năm 2025 (Tỷ USD) | Steam Market Reports |

---

## 5. BẢNG `revenue_by_region(2021 - 2025).csv` (Thị Phần Địa Lý Vĩ Mô)
* **Nguồn:** [Newzoo Global Games Market Reports (2021 – 2025/2026)](https://www.scribd.com/document/759739689/2024-Newzoo-Free-Global-Games-Market-Report)

| Tên Cột | Ví Dụ Dữ Liệu | Ý Nghĩa / Mô Tả | Nguồn Dữ Liệu |
| :--- | :--- | :--- | :--- |
| `Region` | `Asia-Pacific`, `North America` | Tên khu vực địa lý toàn cầu (APAC, NA, EU, LATAM, MENA) | Newzoo |
| `Region_Code` | `APAC`, `NA`, `EU` | Mã ký hiệu viết tắt chuẩn của khu vực địa lý | Newzoo |
| `Year` | `2021`, `2022`, `2023`, `2024`, `2025` | Năm ghi nhận dữ liệu thống kê | Newzoo |
| `Share_Pct` | `48.3`, `26.5` | Tỷ trọng thị phần đóng góp vào tổng doanh thu toàn cầu (%) | Newzoo |
| `YoY_Growth_Pct` | `3.4`, `-5.6` | Tốc độ tăng trưởng doanh thu so với năm trước (% YoY) | Newzoo |
