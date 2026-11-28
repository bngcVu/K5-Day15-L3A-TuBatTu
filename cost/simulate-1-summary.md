# Tóm tắt mô phỏng simulate-1@20261128-110358

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 22 | 1 | 821 | 443 | 1.0 | 2.8 |
| dung_vua | 18 | 2 | 1657 | 850 | 2.0 | 5.9 |
| dung_nhieu | 10 | 3 | 2457 | 1346 | 3.0 | 8.1 |

Tỉ lệ đạt dùng để tính: 24/24 (100%) — lượt run-2@20261128-103134

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (300 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.200 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0015 (≈ 39 ₫) | $0.0015 (≈ 39 ₫) | $0.00086 (≈ 22 ₫) | $3.07 (≈ 77.930 ₫) | $7.16 (≈ 181.838 ₫) | $12.27 (≈ 311.722 ₫) | $0.0102 (≈ 260 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0079 (≈ 202 ₫) | $0.0079 (≈ 202 ₫) | $0.0045 (≈ 115 ₫) | $16.07 (≈ 408.129 ₫) | $37.49 (≈ 952.300 ₫) | $64.27 (≈ 1.632.515 ₫) | $0.0536 (≈ 1.360 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: openai/gpt-oss-120b. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.400 ₫ (Tỉ giá Vietcombank ngày 27/11/2026).
