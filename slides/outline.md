# Dàn slide → lấy số từ file nào

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11. Nộp PDF, không nộp link.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 0 | Bìa *(thêm)* | Tên đề tài · nhóm · thành viên · 1 con số (17/19) · hình minh họa vẽ bằng hình khối | `evidence/summary.md` | ☑ bản nháp |
| 1 | Người dùng & pain | Ai · việc gì · chỗ đau + số và trích dẫn | `evidence/summary.md` | ☑ bản nháp (còn 4 điểm kiểm ở dưới) |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn + hướng bị loại | `spec.md` §2 | ☑ bản nháp |
| 3 | Giải pháp | Lát cắt một câu · sơ đồ · AI tự làm đến đâu, vì sao | `spec.md` §4 | ☑ bản nháp |
| 4 | Demo live | 1 trường hợp thường + 1 trường hợp khó (lấy từ bộ câu thử); mạng hỏng → video dự phòng | `eval/benchmark.csv` | ☑ bản nháp (còn thiếu video dự phòng) |
| 5 | **Đánh giá thế nào** | Dataset · bộ câu thử · metric · lượt 1 → lượt 2 so với chuẩn "đạt" (kèm run ID) · lỗi chính | `eval/README.md`, `eval/report.md` | ☑ bản nháp |
| 6 | **Chi phí khi dùng thật** | Chi phí / task thành công · 3 kịch bản · so với impact | `cost/cost-estimate.md` | ☑ bản nháp (số từ simulate-1) |
| 7 | Kết luận | Go / iterate / stop — dẫn số ở trang 1, 5, 6 | — | ☑ kết luận ITERATE |
| 8 | Nếu có thêm 1 tuần | 2–3 việc, trỏ về lỗi còn lại / phản hồi người dùng | `eval/report.md` mục 4 · `validation/log.md` | ☐ hai việc đầu đã điền từ report.md; việc 3 chờ người dùng thử |

**File deck:** `demo-slides.pptx` (9 trang = bìa + 8 trang trong bảng; số trang in trên slide lệch +1 so với cột `#`). PDF `demo-slides.pdf` chưa xuất: xuất sau khi nhóm chốt trang 7–8.

**Trước khi lên:** tải repo về một máy khác (hoặc thư mục mới), chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · biết bản chạy thử sẽ làm gì với **1 câu thử lạ** của giám khảo.

Ai nói trang nào (mỗi người ≥1 phần):

| Trang | Người nói |
|---|---|
| Bìa | *(chưa phân công, nhóm chốt)* |
| Trang 1–2: Người dùng & Pain, Vì sao chọn | Nguyễn Thị Dung |
| Trang 3: Giải pháp (Sơ đồ, AI gợi ý & Code kiểm giờ, giới hạn) | Nguyễn Thế Trường |
| Trang 4: Demo live & Kiến trúc chạy thử | Bùi Ngọc Vũ |
| Trang 5: Đánh giá & Dataset (Benchmark, Metric, Kết quả) | Tô Minh Thành |
| Trang 6–8: Chi phí, Kết luận & Hướng phát triển | Bùi Ngọc Vũ / Nguyễn Thế Trường |

## Trang 1 — Người dùng & pain *(bản nháp khung, số lấy từ `evidence/summary.md`)*

**Tiêu đề trang (nói được kết luận):** Tự lên lịch du lịch, tới nơi mới biết điểm đóng cửa

**Bố cục:** trái = người dùng + pain (3 dòng) · giữa = 3 con số lớn · phải = 2 trích dẫn · chân trang = nguồn và giới hạn.

**Người dùng (1 dòng):** Người tự lên lịch (không mua tour) cho chuyến đi 2–3 ngày của nhóm bạn, đã có lịch nháp và sắp đi.

**Pain (1 câu):** Khi chốt lịch, giờ mở cửa và ngày nghỉ nằm rải rác, có thể đã cũ → tới nơi mới biết điểm đóng cửa, mất công đi và phải xếp lại lịch trong ngày.

**3 con số** *(mỗi số kèm nguồn nhỏ dưới chân)*

| Số | Nguồn |
|---|---|
| **17/19** người từng gặp điểm đóng cửa hoặc sai giờ trong 12 tháng qua | Khảo sát, n = 19 người qua sàng lọc |
| **2/3** người phỏng vấn kể được một lần cụ thể | Phỏng vấn P2, P3 *(n nhỏ, không ghi %)* |
| **30–40 phút** và **50.000–120.000đ** tiền xe mỗi lần | Phỏng vấn P2, P3 |

**2 trích dẫn** (nguyên văn, bỏ tên)
- "Tới nơi thì cổng đóng, có tờ giấy dán 'nghỉ thứ Hai hàng tuần'. Trên Maps không hiển thị ngày nghỉ này." — P3
- "Hôm đó mình định đi một bảo tàng ở Đà Nẵng nhưng đến nơi mới biết bảo tàng đóng cửa để bảo trì, trong khi Google Maps vẫn hiển thị giờ mở cửa bình thường." — P2

**Chân trang (nói thật giới hạn):** n nhỏ (19 khảo sát + 3 phỏng vấn); chưa có người đi Đà Lạt trong 3 buổi phỏng vấn; câu 6 khảo sát đổi cách hỏi lúc 18:20 27/11 (xem `evidence/survey/questions.md`).

**Lời nói (≈40 giây, Nguyễn Thị Dung):**
"Người dùng của nhóm mình là người tự lên lịch cho chuyến đi vài ngày. Họ kiểm giờ mở cửa ở nhiều nơi nhưng thông tin vẫn có thể sai. Trong 19 người khảo sát có 17 người từng tới nơi mới biết điểm đóng cửa hoặc khác giờ. Hai trong ba người phỏng vấn kể lại một lần cụ thể, mỗi lần mất khoảng 30–40 phút và vài chục nghìn tiền xe. Nên nhóm chọn đúng khâu này làm lát cắt."

**Còn phải kiểm trước khi chốt slide:**
- [ ] `summary.md`: hậu quả câu 7 cộng ra 19 thay vì 17 (xem lại dữ liệu gốc) — nếu số này lên slide thì phải đúng.
- [ ] Tách đáp án "Kiểm tra giờ mở cửa" ở câu 9 ra khỏi nhóm gộp, để slide không nói quá pain chính.
- [ ] Xác nhận 19 người đều ngoài nhóm.
- [ ] Số 17/19 chỉ lên slide sau khi hai điểm trên được xác nhận.
