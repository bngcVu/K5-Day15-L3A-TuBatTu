# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Claude Code | Viết `agent.py`, `tools.py`, nhánh Groq trong `ai.py` | Nguyễn Thế Trường | Bùi Ngọc Vũ |
| Prompt / thiết kế lời gọi mô hình | Claude Code | Viết prompt hệ thống, sơ đồ `spec.md` §4; đề xuất metric và chuẩn "đạt" | Nguyễn Thế Trường | Bùi Ngọc Vũ |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | Claude Code | Viết nháp 16 câu B01–B16 | Mỗi câu thử có `source`; cả 16 câu là AI viết; Tô Minh Thành rà lại 16/16 câu | Tô Minh Thành |
| Sinh data `synthetic` (nếu có) | Claude Code | Viết tay 12 địa điểm dựng | Không dùng seed · kiểm tay 0/12 dòng | Nguyễn Thế Trường |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
