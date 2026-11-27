# Khảo sát — bộ câu hỏi và nhật ký gửi

> Ngưỡng: **≥20 người ngoài nhóm, đúng người dùng** (tính theo người qua câu 1 = "Có"), giữ log đủ câu hỏi và từng câu trả lời.
> Hỏi **hành vi đã xảy ra**, không hỏi "có thích không". Không thu tên, email, mã học viên.
> Giả thuyết đang kiểm: `evidence/hypothesis.md` — đúng nếu ≥50% người qua sàng lọc đã gặp đóng cửa / sai giờ trong 12 tháng qua.

## Mô tả đầu form (chép nguyên)

"Nhóm mình đang tìm hiểu cách mọi người tự lên lịch cho chuyến đi vài ngày. Form khoảng 3 phút, ẩn danh, chỉ hỏi chuyện đã xảy ra. Không bán hay giới thiệu sản phẩm."

## Bộ câu hỏi (Google Form)

| # | Câu hỏi | Kiểu trả lời | Dùng để |
|---|---|---|---|
| 1 | Trong 12 tháng qua, bạn có tự lên lịch (không mua tour) cho một chuyến đi 2–3 ngày không? | Có · Không → *kết thúc form, không tính vào n* | Sàng lọc đúng vai |
| 2 | Chuyến gần nhất đó đi đâu? |Chọn một: Trong nước · Nước ngoài | Mô tả mẫu |
| 3 | Bạn bắt đầu lên lịch trước ngày đi khoảng bao lâu? | Chọn một: Dưới 1 tuần · Từ 1 tuần đến 1 tháng · Trên 1 tháng | Mô tả mẫu |
| 4 | Bạn kiểm giờ mở cửa của các điểm bằng cách nào? | Chọn nhiều: Google Maps · Trang / fanpage của điểm đến · Bài review / blog · Hỏi bạn bè · Gọi điện tới điểm đến · Không kiểm giờ mở cửa · Khác | Cách xoay xở hiện tại |
| 5 | Việc kiểm giờ mở cửa cho cả lịch trình mất khoảng bao lâu? | Chọn một: Không kiểm · Dưới 15 phút · 15–30 phút · 30–60 phút · Trên 60 phút | Chi phí hiện tại |
| 6 | Trong 12 tháng qua, bạn có lần nào tới một điểm mà nó đóng cửa hoặc khác giờ bạn dự định không ? | Chọn một: Có, **đóng cửa / ngày nghỉ** · Có, **giờ khác dự định** · Có, cả hai · Không | **Số chính của giả thuyết** |
| 7 | Lần gần nhất không theo kế hoạch đã chốt bạn xử lý như thế nào ? | Chọn một: Đổi sang điểm khác tương tự ngay  · Chờ tới giờ mở · Bỏ qua hoạt động đó · Khác | Hậu quả |
| 8 | Lần đó bạn mất thêm khoảng bao lâu? | Chọn một: Dưới 15 phút · 15–30 phút · 30–60 phút · Trên 60 phút | Hậu quả |
| 9 | Bước nào khi lên lịch khiến bạn mất công hoặc khó chịu nhất ?| Chọn một : Tìm kiếm địa điểm phù hợp với sở thích · Xem đánh giá các địa điểm trên mạng xã hội / google map · Kiểm tra giờ mở cửa và đóng cửa · Sắp xếp kế hoạch đi qua các địa điểm · Thay đổi địa điểm bất ngờ do địa điểm không mở cửa · Khác | Kiểm cách giải thích khác (pain là việc khác ?)|
| 10 | Kể lại lần gần nhất bạn gặp điểm đóng cửa hoặc khác giờ | Đoạn văn (tuỳ chọn) | Lấy trích dẫn |

## Nhật ký thay đổi form (ghi trung thực, không xoá)

| Phiên bản | Thời gian | Khác gì | Phiếu thuộc bản này |
|---|---|---|---|
| A | mở 17:5x 27/11 | 9 câu. Câu 6 hỏi "Trong chuyến du lịch đó…" (chuyến gần nhất, không nêu mốc 12 tháng). Không có câu 10 | 7 phiếu đầu, Timestamp 17:54–17:58 |
| B | sửa lúc 18:20 27/11 | Câu 6 đổi thành "Trong 12 tháng qua…". Thêm câu 10 (mở, tuỳ chọn). Các câu còn lại giữ nguyên *(câu 7 có "Khác" từ trước khi public, file chỉ ghi chưa kịp)* | Phiếu từ Timestamp ≥ 18:20 27/11 |

**Khi đếm câu 6:**
- Chuyến gần nhất nằm trong 12 tháng (câu 1 đã lọc), nên một đáp án "Có" ở bản A cũng là "Có" cho 12 tháng. Vì vậy với **tỷ lệ đã gặp**, được gộp bản A và B.
- Một đáp án "Không" ở bản A **không** suy ra "Không" cho 12 tháng. Phiếu như vậy phải tách riêng, không tính vào mẫu số của giả thuyết.
- Phần phân loại (đóng cửa / giờ khác / cả hai) của bản A có thể hụt vì chỉ nghĩ tới một chuyến. Nêu rõ khi báo cáo.
- Ghi vào `summary.md` rằng câu 6 đổi cách hỏi, kèm giờ đổi.

## Cách đếm (viết trước khi xem kết quả)

- **n** = số người trả lời câu 1 = "Có" (người trả "Không" ghi riêng, không tính).
- **Số chính** = số người chọn "Có, …" ở câu 6 / n. Đếm riêng đóng cửa, giờ khác, cả hai.
- Dưới ~10 người thì chỉ ghi x/n, không ghi %.
- Loại phiếu trùng nhìn ra được (cùng nội dung, cùng giờ) và ghi lại số lượng đã loại.
- Phiếu của thành viên nhóm và người nhà thân không tính vào n.

## Nhật ký gửi (điền khi chạy)

| Kênh | Đối tượng | Giờ mở | Giờ chốt | Số phiếu thu được | Số qua sàng lọc |
|---|---|---|---|---|---|
| | | | | | |

## Lưu vào thư mục này

- `results.csv` — bản xuất từ Google Form (bản B có 10 câu, không thu email), **đã xoá** mọi cột nhận ra người trả lời nếu có. Giữ cột `Timestamp` để loại phiếu trùng. Bản gốc còn thông tin cá nhân thì **không** commit.
- Số chính (câu 6, bản B) → chép vào `evidence/summary.md`. Câu 10 là câu mở tuỳ chọn: lấy trích dẫn nguyên văn từ đó (chỉ từ bản B, ẩn danh), bổ sung từ phỏng vấn (`P1.md`…). Câu 9 là trắc nghiệm, dùng để đếm bước nào gây khó chịu nhất.
