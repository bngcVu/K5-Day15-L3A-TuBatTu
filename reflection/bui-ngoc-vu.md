# Reflection — Bùi Ngọc Vũ

1. Vai trò + phần mình làm (trỏ tới file / commit):
Mình là đội trưởng, phụ trách luồng `codebase/agent.py`, nối model và TEAMS / nộp bài.
Mình đưa khung repo lên (`448db11`), nộp CP1 với `TEAMS.md` và `canvas.md` (`948c0ac`, giữ ở nhánh `CP1`).
Ở CP2 mình đưa lên bản chạy thử (`490be14`): `agent.py`, nhánh Groq trong `ai.py`, `tools.py`, 12 địa điểm dựng, 16 câu thử, metric và `spec.md`; phần code và bản nháp này làm cùng Claude Code.
Luồng: model chỉ nhận diện địa điểm hoặc hỏi lại, còn code đọc giờ, so giờ / ngày nghỉ và soạn câu trả lời.

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
Mình dùng Claude Code để soạn canvas, viết `agent.py`, `tools.py`, nối Groq, nháp câu thử, metric và sơ đồ.
Bản canvas đầu để AI tự phán đoán khớp giờ; đối chiếu với tài liệu Track C (bẫy "để model tự nhẩm giờ") thì phải sửa: so giờ chuyển sang code.
Khi chạy thử model thật có 2 câu sai: B03 model trả JSON thừa dấu `}` nên code không đọc được; B05 model hiểu "Thứ Sáu" thành `t5`.
Cách sửa là đọc đối tượng JSON đầu tiên và ghi rõ bảng mã thứ trong prompt; câu thử và `expected` giữ nguyên.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
B14 (nhờ đặt 2 vé và thanh toán) trượt ở lượt 1 (`eval/run-1.csv`): không có output vì Groq trả HTTP 429, nên chưa đo được câu từ chối này.
Cả 15 câu trượt của lượt 1 đều là lỗi 429; sau khi Trường thêm chờ rồi thử lại trong `ai.py` (`5743f3f`), lượt 2 đạt 24/24 và B14 từ chối đúng.
Mình học được: phải tách lỗi hạ tầng khỏi lỗi quyết định của model; mức tăng từ 9/24 lên 24/24 không chứng minh model phán đoán tốt hơn.
24/24 cũng chỉ đúng trên bộ câu thử này với dữ liệu địa điểm dựng, chưa nói được gì về lịch trình và giờ mở cửa thật ở Đà Lạt.
