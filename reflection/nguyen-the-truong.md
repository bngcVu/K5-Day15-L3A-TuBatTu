# Reflection — Nguyễn Thế Trường

> Mã học viên: 2A202603393 · Nhóm: Tứ Bất Tử · Track C (Du lịch)

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   - Trong dự án, mình đảm nhận vai trò phụ trách công cụ (`codebase/tools.py`), cơ sở dữ liệu địa điểm (`data/diem_dalat.json`), tài liệu dữ liệu (`data/DATA_CARD.md`), và phụ trách cải tiến đánh giá Lượt 1 → Lượt 2 trong `eval/report.md`.
   - Các đóng góp chính qua các commit: commit `6d7404a` chuẩn hoá hàm `tra_diem()` và `kiem_gio()`, rà soát 12/12 dòng địa điểm dựng có cài 5 ca khó (trùng tên gọi tắt, nghỉ trưa, thiếu ngày nghỉ, chỉ mở cuối tuần); commit `61c8698` hỗ trợ hoàn thiện spec §0–§3, §5–§6 và `cost/personas.yaml`; commit `5743f3f` bổ sung cơ chế auto-retry backoff khi gặp lỗi rate limit `HTTP 429` trong `codebase/ai.py` giúp lượt 2 đạt kết quả 24/24 câu (100%).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   - Mình sử dụng Claude Code và Antigravity để sinh khung nháp ban đầu cho các hàm trong `tools.py`, gợi ý cấu trúc JSON địa điểm và viết script kiểm thử tự động.
   - Điểm AI làm chưa tốt mà mình phải trực tiếp kiểm tra và sửa lại: AI ban đầu viết hàm `kiem_gio` chưa xử lý chặt chẽ các ca biên đầu vào (chuỗi viết hoa, thiếu số 0 ở đầu giờ, hoặc giờ sai định dạng). Mình đã tự viết thêm hai hàm `_chuan_thu` và `_chuan_gio` bằng regex để chuẩn hoá dữ liệu trước khi so khớp. Đồng thời, ở Lượt 1 khi gọi mô hình qua Groq API, AI ban đầu không tính đến giới hạn tốc độ (Rate Limit TPM), dẫn đến lỗi hàng loạt `HTTP 429`; mình đã phải cấu hình lại cơ chế tự động chờ luỹ tiến (backoff retry) để hệ thống hoạt động ổn định.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   - Câu thử trượt đáng nhớ nhất là câu B09 (`Thứ Năm: 9h Hồ Cá Voi Xanh, 11h Thác Nai Ngủ`) ở Lượt 1. Câu này mong đợi hệ thống nhận diện Hồ Cá Voi Xanh là địa điểm lạ và gắn nhãn `CHƯA ĐỦ THÔNG TIN` chứ không được đoán mò. Tuy nhiên ở lượt chạy đầu tiên, câu này bị trượt do lỗi mạng `HTTP 429` vì gọi model quá dồn dập.
   - Bài học rút ra: Xây dựng một ứng dụng AI đáng tin cậy không chỉ nằm ở prompt hay thuật toán mô hình mà còn phụ thuộc rất lớn vào tính bền bỉ của hạ tầng mạng, quản lý hạn ngạch API và thiết kế các tầng bảo vệ (guardrails) bằng code truyền thống. Việc kết hợp AI để nhận diện ngữ nghĩa và dùng code tường minh để kiểm tra giờ mở cửa là hướng đi an toàn, giúp tránh hoàn toàn hiện tượng AI bịa đặt dữ liệu (hallucination).
