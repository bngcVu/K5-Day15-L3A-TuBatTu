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
| 2 | Chuyến gần nhất đó đi đâu? | Đà Lạt · Nơi khác trong nước · Nước ngoài | Mô tả mẫu |
| 3 | Bạn bắt đầu lên lịch trước ngày đi khoảng bao lâu? | Dưới 1 tuần · 1–4 tuần · Trên 1 tháng | Mô tả mẫu |
| 4 | Bạn kiểm giờ mở cửa của các điểm bằng cách nào? | Chọn nhiều: Google Maps · Trang / fanpage của điểm · Bài review / blog · Hỏi bạn bè · Gọi điện · Không kiểm · Khác | Cách xoay xở hiện tại |
| 5 | Việc kiểm giờ mở cửa cho cả lịch trình mất khoảng bao lâu? | Không kiểm · Dưới 15' · 15–30' · 30–60' · Trên 60' | Chi phí hiện tại |
| 6 | Trong 12 tháng qua, bạn có lần nào tới một điểm mà nó đóng cửa hoặc khác giờ bạn dự định không? | Có, **đóng cửa / ngày nghỉ** · Có, **giờ khác dự định** · Có, cả hai · Không | **Số chính của giả thuyết** |
| 7 | *(Nếu câu 6 ≠ Không)* Lần gần nhất đó bạn xử lý thế nào? | Chọn một: Đổi sang điểm khác ngay · Chờ tới giờ mở · Bỏ điểm đó · Xếp lại cả buổi / ngày · Khác | Hậu quả |
| 8 | *(Nếu câu 6 ≠ Không)* Lần đó bạn mất thêm khoảng bao lâu? | Dưới 15' · 15–30' · 30–60' · Trên 60' | Hậu quả |
| 9 | Bước nào khi lên lịch khiến bạn mất công hoặc khó chịu nhất? Kể về lần gần nhất. | Đoạn văn | Kiểm cách giải thích khác (pain là việc khác?) và lấy trích dẫn |
| 10 | *(Tuỳ chọn)* Bạn có sẵn lòng cho nhóm hỏi thêm 10 phút không? | Có — để cách liên hệ (không bắt buộc) · Không | Nguồn phỏng vấn thêm |

Câu 9 không gợi ý "giờ mở cửa" để xem có ai tự nhắc tới không.

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

- `results.csv` — bản xuất **đã xoá** mọi cột nhận ra người trả lời (nên xoá cả cột câu 10 nếu có thông tin liên hệ). Bản gốc còn thông tin cá nhân thì **không** commit.
- Số chính + ≥3 câu trả lời nguyên văn (từ câu 9) → chép vào `evidence/summary.md`.
