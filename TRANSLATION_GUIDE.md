# QUY CHUẨN DỊCH THUẬT & BẢNG THUẬT NGỮ RIMWORLD (VIỆT HÓA)

## 1. Văn phong & Định hướng giọng điệu (Tone & Voice)

Bản dịch chia làm **2 lớp văn bản** rõ ràng tùy theo vị trí xuất hiện trong game:

- **Lớp 1 - Giao diện, Chỉ số, Nút bấm & Cơ chế (UI / Stats / Gizmos):**
  - **Yêu cầu:** Ngắn gọn, súc tích, chuẩn xác, ưu tiên danh từ và động từ trực diện để không bị tràn khung giao diện. Tuyệt đối không tự ý thêm từ thừa (ví dụ: chỉ dùng `tổ` cho *hive*, không kéo dài thành *tổ côn trùng*).
  - **Ví dụ:** `Giường y tế`, `Cấm chặt cây`, `San lấp`, `Độ lệch hồng tâm`, `Nhiệt thần kinh`, `Chọn tổ`.

- **Lớp 2 - Cảnh báo, Hội thoại, Mô tả sự kiện & Thông báo (Alerts / Dialogs / Descriptions):**
  - **Yêu cầu:** Bụi bặm, đời thường, mang chất sinh tồn khắc nghiệt pha chút hài hước đen (dark humor) đặc trưng của RimWorld. Cho phép dùng khẩu ngữ, từ lóng tự nhiên nhưng không lạm dụng gây phản cảm.
  - **Ví dụ:** _"tuôn một tràng chửi thề vào bộ đàm rồi dập máy cái rụp"_, _"đứng mọc rêu chờ bạn chỉ hướng đi"_, _"quỵt luôn tiền thưởng"_, _"Cư dân rảnh háng"_, _"Thu hoạch toang"_.

- **Quy tắc xưng hô:**
  - Gọi người chơi là **bạn**.
  - Gọi cư dân hoặc đồng minh là **họ / người này**.
  - Gọi kẻ địch hoặc phe thù địch là **chúng / bọn chúng / đám...** (áp dụng cả trong mô tả quan hệ ngoại giao của phe thù địch).
  - Gọi động vật là **nó / chúng** (không gọi là _họ_).

- **Quy tắc giữ nguyên tên riêng & vật phẩm đặc thù:**
  - Giữ nguyên tên riêng của các bệnh, thuốc lắc, thực phẩm đặc trưng, sinh vật hư cấu (`scaria`, `yayo`, `flake`, `luciferium`, `psychoid`, `thrumbo`...) và các thuật ngữ công nghệ/khoa học viễn tưởng đã Việt hóa thông dụng (`hack`, `EMP`, `laser`, `plasma`...). Không giữ hậu tố số nhiều `-s` của tiếng Anh.

## 2. Quy tắc kỹ thuật XML & Ngữ pháp tiếng Việt

1. **Bảo toàn thẻ và biến hệ thống:**
   - Tuyệt đối không dịch, không xóa hoặc đổi tên các biến trong ngoặc nhọn (`{0}`, `{PAWN_labelShort}`, `{FACTION_name}`, `{GERUND}`, `{LAYER}`...), biến ngoặc vuông (`[PAWN_pronoun]`), các thẻ định dạng (`(*SectionTitle)...(/SectionTitle)`, `(*Name)...(/Name)`) và ký tự xuống dòng (`\n`, `\n\n`). Tuyệt đối không tự ý thêm biến lạ không có trong câu gốc tiếng Anh.

2. **Xử lý biến sở hữu (`{0_possessive}`, `{PAWN_possessive}`):**
   - Đặt biến sở hữu **ngay sau danh từ**, **KHÔNG** thêm chữ _"của"_ phía trước vì bộ ngữ pháp của game sẽ tự động chèn _"của \[Tên\]"_.
   - **Đúng:** `khu định cư {0_possessive}`, `tước hiệu {TITLE} {PAWN_possessive}`
   - **Sai:** `khu định cư của {0_possessive}` (sẽ bị lặp thành _"của của..."_).

3. **Xử lý biến danh xưng & chủ ngữ sự kiện:**
   - Không thêm chữ _"một"_ trước `{PAWN_titleIndef}` vì biến này đã mang sẵn danh xưng hoàn chỉnh.
   - Trong các tiêu đề `Caravan meeting by {0}` hoặc `Caravan demand by {0}`, biến `{0}` là **tên đoàn lữ hành của người chơi** (không phải kẻ địch).

4. **Quy tắc viết hoa / viết thường:**
   - Các thẻ có hậu tố `Lower` (như `<DyingLower>`, `<AnimalsLower>`, `<StunLower>`) hoặc cụm từ nối tiếp giữa câu bắt buộc **viết thường chữ cái đầu** (trừ danh từ riêng).
   - Không để dấu cách thừa trước dấu chấm câu, dấu chấm lửng (`...`) hoặc trước thẻ đóng XML.
5. **Chính tả & Hậu tố biến tên gọi:**
   - Giữ nguyên tuyệt đối hậu tố độ dài tên biến (`{1_labelShort}`, `{0_label}`, `{0_definite}`), không tự ý đổi sang hậu tố khác.
   - Thống nhất chính tả tiếng Việt: viết **`kỹ năng`** (không dùng *kĩ năng*); phân biệt **`dành cho`** (để riêng cho ai/cái gì) với **`giành`** (tranh giành).
## 3. Bảng thuật ngữ chuẩn (Standard Glossary)

### A. Con người, Phe phái & Ngoại giao

| Tiếng Anh (EN)       | Tiếng Việt chuẩn (VI)     | Ghi chú ngữ cảnh                                |
| -------------------- | ------------------------- | ----------------------------------------------- |
| **Colonist**         | cư dân                    | Thành viên thuộc địa của người chơi (không dịch _thực dân_) |
| **Prisoner**         | tù nhân                   |                                                 |
| **Slave**            | nô lệ                     |                                                 |
| **Refugee**          | dân tị nạn                |                                                 |
| **Wanderer / Traveler** | lữ khách               | Người qua đường / người xin gia nhập            |
| **Visitor**          | khách ghé thăm            |                                                 |
| **Warden**           | quản ngục                 | Công việc cai quản / chiêu mộ tù nhân           |
| **Handler**          | dân chăn nuôi             | Công việc thuần hóa / lùa gia súc               |
| **Trait**            | tính cách                 | Đặc tính nhân vật (không dịch _đặc điểm_)        |
| **Bio**              | tiểu sử                   | Thẻ thông tin tiểu sử nhân vật                  |
| **Opinion**          | thiện cảm                 | Điểm quan hệ giữa hai cá nhân (không dịch _ý kiến_) |
| **Resistance**       | độ phản kháng             | Chỉ số kháng cự chiêu mộ của tù nhân            |
| **Unwavering loyalty** | trung thành tuyệt đối      | Tù nhân không thể chiêu mộ                      |
| **Faction**          | phe / phe phái            | Dùng _phe_ trong hội thoại, _phe phái_ trên UI (không dịch _bè phái_) |
| **Faction leader**   | thủ lĩnh                  |                                                 |
| **Bestower**         | sứ giả ban tước           | Sứ giả Đế chế tổ chức lễ phong tước             |
| **Settlement**       | khu định cư               | Căn cứ cố định của các phe trên bản đồ thế giới |
| **Colony**           | thuộc địa / căn cứ        | _Thuộc địa_ (chính thức), _căn cứ_ (văn nói)    |
| **Outpost**          | tiền đồn                  |                                                 |
| **Site**             | địa điểm                  | Địa điểm sự kiện/nhiệm vụ trên bản đồ thế giới  |
| **Goodwill**         | thiện chí                 | Điểm quan hệ ngoại giao giữa các phe            |
| **Natural goodwill** | thiện chí tự nhiên        |                                                 |
| **Raid**             | đột kích                  |                                                 |
| **Hostile / Hostiles** | thù địch / thế lực thù địch / kẻ thù | Dùng _chúng / bọn chúng_ khi nói về phe thù địch |
| **Permanently hostile** | thù địch không đội trời chung | Phe thù địch vĩnh viễn, không thể giảng hòa  |
| **Enemy of**         | kẻ thù của                | Thống nhất cho cả `Enemy of {0}` và `Enemy of:` |

### B. Phương tiện, Lữ hành & Bản đồ thế giới

| Tiếng Anh (EN)               | Tiếng Việt chuẩn (VI) | Ghi chú ngữ cảnh                                            |
| ---------------------------- | --------------------- | ----------------------------------------------------------- |
| **Transport pod / Drop pod** | khoang vận chuyển     | Thống nhất dùng chung cho cả bệ phóng và rơi tự do          |
| **Cargo pod**                | khoang hàng           | Không dịch là _thùng hàng_                                  |
| **Shuttle**                  | tàu con thoi          |                                                             |
| **Cryptosleep casket**       | kén ngủ đông          | Chỉ dùng chữ _kén_ cho loại này                             |
| **Orbital trader / Trade ship** | tàu buôn vũ trụ    | Không dịch là _thương nhân quỹ đạo_                         |
| **Caravan / Trade caravan**  | đoàn lữ hành          | Dùng thống nhất cho cả đoàn của người chơi và đoàn buôn NPC |
| **Planet layer**             | lớp hành tinh         | Dùng cho bản đồ quỹ đạo / bề mặt                            |
| **Biome**                    | quần xã sinh vật      |                                                             |
| **Waypoint**                 | điểm dừng chân        |                                                             |

### C. Công trình, Chăn nuôi & Vật phẩm

| Tiếng Anh (EN)               | Tiếng Việt chuẩn (VI)          | Ghi chú ngữ cảnh                          |
| ---------------------------- | ------------------------------ | ----------------------------------------- |
| **Bill**                     | công việc / việc               | Danh sách lệnh làm việc trên bếp, bàn chế tạo, lò... |
| **Nutrient paste dispenser** | máy đùn cám heo                | Giữ đúng chất hài hước đặc trưng của game |
| **Hopper**                   | phễu nạp                       |                                           |
| **Battery**                  | ắc quy                         | Thiết bị trữ điện căn cứ (không dịch _pin_) |
| **Turret**                   | trụ súng / ụ súng              | Dùng _trụ súng_ trên UI                   |
| **Throneroom**               | phòng ngai vàng                |                                           |
| **Hive**                     | tổ                             | Tổ bọ (không kéo dài thành _tổ côn trùng_) |
| **Animal pen**               | chuồng / chuồng gia súc        |                                           |
| **Pen marker**               | cọc đánh dấu chuồng            |                                           |
| **Hitching spot**            | cọc buộc gia súc / cọc gia súc |                                           |
| **Stockpile zone**           | vùng kho chứa                  |                                           |
| **Dumping stockpile**        | vùng bãi thải                  |                                           |
| **Growing zone**             | vùng trồng trọt                |                                           |
| **Plan**                     | quy hoạch                      |                                           |
| **Extract tree**             | bứng cây                       |                                           |
| **Drug / Drug policy**       | thuốc / chính sách thuốc       | Không dịch là _dược phẩm_                 |
| **Tainted (apparel)**        | ô uế                           | Quần áo lột từ xác chết                   |
| **Tattered apparel**         | trang phục rách rưới           |                                           |
| **Blight**                   | bệnh cháy lá                   |                                           |
| **Wort**                     | hèm bia                        | Nguyên liệu ủ bia                         |
| **Food** | lương thực / thức ăn | Dùng _lương thực_ cho kho dự trữ tổng, đoàn lữ hành, thu hoạch; dùng _thức ăn_ cho bữa ăn cá nhân, vật nuôi, nguyên liệu nấu nướng |
| **Food restriction / policy** | chế độ ăn / chính sách ăn uống | Thiết lập khẩu phần trong tab Phân công (không dịch là _giới hạn thức ăn_) |
| **Medicine restriction** | mức thuốc cho phép / chế độ dùng thuốc | Thiết lập loại thuốc được phép dùng trong tab Sức khỏe (không dịch là _giới hạn thuốc_) |
### D. Trạng thái, Tâm linh, Nghiên cứu & Công nghệ cao

| Tiếng Anh (EN)              | Tiếng Việt chuẩn (VI)                     | Ghi chú ngữ cảnh                              |
| --------------------------- | ----------------------------------------- | --------------------------------------------- |
| **Sharp (armor / damage)**  | xuyên cắt / chống xuyên cắt               | Đạn bắn, mũi tên, dao kiếm, móng vuốt (không dịch _nhọn_) |
| **Blunt (armor / damage)**  | va đập / chống va đập                     | Chùy, búa, nắm đấm, chấn động (không dịch _cùn_) |
| **Heat (armor / damage)**   | nhiệt / chống nhiệt                       | Lửa, laser, plasma                            |
| **Draft / Drafted**         | triệu tập / được triệu tập                | Trạng thái điều khiển trực tiếp chiến đấu     |
| **Mental break**            | suy sụp tinh thần                         |                                               |
| **Incapacitated**           | mất khả năng hành động                    |                                               |
| **Downed**                  | gục ngã                                   |                                               |
| **Pain shock**              | sốc vì đau                                |                                               |
| **Sterile / Sterilize**     | vô sinh / thiến                       | Không dịch *sterile* là *vô tính*             |
| **Psylink**                 | liên kết tâm linh                         |                                               |
| **Psycast / Psychic power** | năng lực tâm linh                         |                                               |
| **Psyfocus**                | tinh thần lực                             |                                               |
| **Neural heat**             | nhiệt thần kinh                           |                                               |
| **Psychic drone**           | âm vang tâm linh                          |                                               |
| **Persona weapon**          | vũ khí tri giác                           |                                               |
| **Bladelink (Bonded)**      | liên kết                                  |                                               |
| **Biocoded**                | khóa sinh trắc                            |                                               |
| **Skill neurotrainer**      | ống cấy kỹ năng                           |                                               |
| **Mechanoid**               | robot sát thủ Mechanoid / robot Mechanoid | Giữ lại tên riêng _Mechanoid_ để dễ nhận diện |
| **Techprint**               | bản thiết kế công nghệ                    |                                               |
| **Research project**        | đề tài nghiên cứu                         | Dùng _đề tài_ thay cho _dự án_               |
| **Study**                   | khảo sát                                  | Nghiên cứu thực thể/cổ vật (không dịch _học tập_) |
| **Hack / Hacking**          | hack                                      | Giữ nguyên từ mượn _hack_ (tránh dùng _xâm nhập_ dễ nhầm với kẻ địch đột nhập căn cứ) |

## 4. Các lỗi dịch thô cần tránh (Do's & Don'ts)

- **Sharp / Blunt -> `xuyên cắt / va đập`** (Trong chỉ số giáp dùng _chống xuyên cắt / chống va đập_, không dịch thô là _nhọn / cùn_).
- **Trait -> `tính cách`** (Không dịch là _đặc điểm_).
- **Drug policy -> `chính sách thuốc`** (Không dịch là _chính sách dược phẩm_).
- **Hive -> `tổ`** (Không dịch dài dòng thành _tổ côn trùng_).
- **Bill -> `công việc / việc`** (Bao quát cả bếp nấu, bàn rèn, lò hỏa táng; không dịch là _hóa đơn_ hay _đơn chế tạo_).
- **Chance -> `tỉ lệ`** (Không dịch là _cơ hội_ hay _xác suất_ trong các thông số UI: _tỉ lệ bắn trúng_, _tỉ lệ suy sụp_).
- **Incident -> `sự kiện`** (Không dịch là _sự cố_ trong phần thiết lập kịch bản).
- **Hit points -> `độ bền`** (Không dịch là _điểm máu_ đối với vật thể/công trình).
- **Work type -> `công việc`** (Không dịch là _loại hình lao động_).
- **Colony wealth -> `tài sản thuộc địa`** (Không dịch là _độ giàu_ hay _của cải_).
- **Offer -> `lời đề nghị`** (Trong nhiệm vụ/giao thương, không dịch là _ưu đãi_).
- **Click / Jump to -> `nhấp / chuyển tới`** (Thống nhất trên mọi hướng dẫn UI, không dùng _click_ hay _nhảy tới_).
- **Recruit -> `chiêu mộ`** (Không dịch là _tuyển dụng_ hay _chiêu hàng_).
- **Capture -> `bắt giữ`** (Không dịch máy móc là _nắm bắt_ hay _bắt buộc_).
- **A child of {AGE} -> `một đứa trẻ {AGE} tuổi`** (Không dịch nhầm thành _con của {AGE}_).
- **Brawler -> `Đấu sĩ`** (Tính cách cận chiến).
- **Teetotaler -> `Bài chất kích thích`** (Tính cách).
- **Body purist -> `Tôn thờ nguyên bản`** (Tính cách).
- **Reserved / Reserved by -> `đã bị chiếm dụng` / `đã bị {1} chiếm dụng`** (Không dịch là *dự trữ* hay *dành cho* trong trạng thái tương tác vật thể).
- **No power -> `không có điện`** (Không dịch máy móc là *không có năng lượng*).
- **No path -> `không có lối đi`** (Thống nhất trên toàn bộ thông báo, không dùng *con đường*).
- **Deconstruct / Mining -> `tháo dỡ / khai khoáng`** (Không dịch là *phá hủy / đào mỏ*).
- **Incapable of violence / shooting -> `không có khả năng bạo lực / bắn súng`** (Không dịch là *sợ bạo lực* hay *chụp*).
- **Implant (install) -> `cấy ghép`** (Không dịch là *cài đặt* như phần mềm).
- **Food / Medicine restriction -> `chế độ ăn / mức thuốc cho phép`** (Không dịch thô *restriction* là *giới hạn*).
- **Pack animal -> `thú thồ`** (Không dịch là *đàn thú*).
- **Tend -> `chữa trị`** (Thống nhất với *tự chữa trị*, không dịch là *chăm nom*).
- **Hack -> `xâm nhập`** (Thống nhất cả tiêu đề lẫn mô tả, không dùng *truy cập trái phép* gây dài dòng trên nút).
- **Designation -> `chỉ định`** (Không nhầm lẫn với *destination / đích đến*).
- **Contents (khoang vận chuyển / hòm đồ) -> `vật phẩm bên trong`** (Không dịch máy móc là *nội dung*).