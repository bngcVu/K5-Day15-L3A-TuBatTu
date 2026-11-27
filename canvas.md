# Canvas — Tứ Bất Tử · Track C

> Điền ở guide bước 1.4. CP1 17:00 Thứ Sáu 27/11: nộp bản đầu, đủ 7 dòng (dòng 4 được ghi giả thuyết + nguồn sẽ kiểm).
> CP2 19:30 Thứ Sáu 27/11: cập nhật (số bằng chứng đầu, lát cắt đã chốt) và điền dòng "Đã đổi gì so với CP1".
> Track F: chép thêm thẻ đề của nhóm (khung trong file track F) xuống dưới bảng này.

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | **Track C — Du lịch** · Kiểm lịch trình nháp đi Đà Lạt 2–3 ngày: điểm nào vướng giờ mở cửa / ngày nghỉ |
| 2 | Người dùng chính (một vai cụ thể — không phải "học viên nói chung") | Người tự lên lịch (không mua tour) cho chuyến đi Đà Lạt 2–3 ngày của nhóm bạn, đã có lịch nháp và sắp đi |
| 3 | Pain một câu: ai — đang làm gì — vướng đâu — hậu quả | Người tự lên lịch đi Đà Lạt, khi chốt lịch trình 2–3 ngày, khó kiểm giờ mở cửa và ngày nghỉ của từng điểm vì thông tin nằm rải rác, có thể đã cũ, nên dễ tới nơi mới biết điểm đóng cửa, mất công đi và phải xếp lại lịch trong ngày. |
| 4 | Bằng chứng đầu — CP1: giả thuyết + nguồn sẽ kiểm · CP2: số đầu tiên + 1 trích dẫn | **Giả thuyết:** đúng nếu ≥2/3 người phỏng vấn hoặc ≥50% khảo sát gặp điểm đóng cửa / sai giờ. **Kết quả:** Phỏng vấn đạt 2/3 người (P2, P3); Khảo sát đạt **17/19 người (89.5%)** tự lên lịch trong 12 tháng qua từng gặp đóng cửa hoặc sai giờ (9 đóng cửa/nghỉ, 4 sai giờ, 4 cả hai). **Trích dẫn:** "Đi du lịch Tết quán đóng cửa nhưng trên gg map vẫn hiện thông tin mở cửa" (Khảo sát) & "Tới nơi thì cổng đóng, có tờ giấy dán 'nghỉ thứ Hai hàng tuần'" (P3). |
| 5 | **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả) | Một người tự lên lịch dán lịch nháp đi Đà Lạt 2–3 ngày, AI quyết định mỗi mục viết tự do trong lịch là địa điểm nào trong danh sách có mã nguồn hay phải hỏi lại, để code đối chiếu giờ mở cửa và ngày nghỉ, rồi người đó nhận bảng đánh dấu "khớp", "vướng giờ / ngày nghỉ" hoặc "chưa đủ thông tin" kèm nguồn để tự sửa lịch trước khi đi. |
| 6 | AI tự làm đến đâu + 1 dòng lý do: sai thì ai chịu gì | AI chỉ nhận diện địa điểm, hỏi lại và gợi ý, người dùng quyết; so giờ bằng code, giờ mở cửa chỉ lấy từ công cụ, không có dữ liệu thì báo "chưa đủ thông tin"; không tự sửa lịch, không đặt vé / đặt chỗ — vì nếu sai, người đi chịu mất thời gian, tiền đi lại và lỡ điểm muốn đến |
| 7 | Phân công có tên | Bùi Ngọc Vũ: luồng `agent.py`, nối model, TEAMS / nộp bài · Nguyễn Thế Trường: `tools.py` + dữ liệu địa điểm + data card · Tô Minh Thành: bộ câu thử + metric + chạy eval · Nguyễn Thị Dung: giả thuyết, phỏng vấn / khảo sát, tổng hợp bằng chứng |
| — | *(CP2)* Đã đổi gì so với CP1 | Bản chạy thử dùng 12 địa điểm **dựng** (tên và giờ dựng, `data/diem_dalat.json`) nên lát cắt đổi "link nguồn" thành "mã nguồn"; chốt phân vai: model nhận diện địa điểm hoặc hỏi lại, code đọc giờ và gắn nhãn. Dòng 4: thêm số đầu tiên (2/3) và trích dẫn từ 3 phỏng vấn; giữ nguyên giả thuyết. Phỏng vấn cho thấy nguồn công khai (Google Maps) hay sai ở **quán nhỏ / điểm tư nhân** và **đóng cửa đột xuất** (bảo trì) — loại đóng cửa đột xuất nằm ngoài lát cắt hiện tại (chỉ kiểm giờ mở và ngày nghỉ theo thứ) |
