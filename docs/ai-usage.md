# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử (`agent.py`, `ai.py`) | Claude Code | Viết `agent.py`, nhánh Groq trong `ai.py` | Chưa có người kiểm | Bùi Ngọc Vũ |
| Code công cụ (`tools.py`) | Claude Code + Antigravity | Viết và chuẩn hoá kiểm tra đầu vào `tra_diem`, `kiem_gio` | Đã kiểm logic, docstring, và chạy test các ca biên (khớp biên đóng cửa, `thu`/`gio` thiếu hoặc sai dạng) | Nguyễn Thế Trường |
| Prompt / thiết kế lời gọi mô hình | Claude Code | Viết prompt hệ thống, sơ đồ `spec.md` §4; đề xuất metric và chuẩn "đạt" | Chưa có người kiểm | Bùi Ngọc Vũ |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | Claude Code | Viết nháp 16 câu B01–B16 | Mỗi câu thử có `source`; cả 16 câu là AI viết, chưa có người kiểm | Tô Minh Thành |
| Sinh data `synthetic` (nếu có) | Claude Code | Viết tay 12 địa điểm dựng | Không dùng seed · đã kiểm 12/12 dòng khớp schema, quy ước và 5 chỗ khó | Nguyễn Thế Trường |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
