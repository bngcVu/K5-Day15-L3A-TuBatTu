# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu
  - `dung_it`: 50% người dùng · 2 phiên / người / tháng · 1 lượt hỏi / phiên
  - `dung_vua`: 30% · 6 phiên / tháng · 2 lượt / phiên
  - `dung_nhieu`: 20% · 12 phiên / tháng · 3 lượt / phiên

  Nguồn: phỏng vấn P1, P2, P3 (`spec.md` §1).
- **Số người dùng thật**, 3 kịch bản: thấp **300** · cơ sở **700** · cao **1.200**. Nguồn: quy mô lớp L3 (~700 học viên, README hackathon) và du khách tự lên lịch đi Đà Lạt. Mức thấp và mức cao là *(tự ước tính)*.
- **Giá**, 2 mức model (USD / 1 triệu token):
  - `gemini-3.1-flash-lite`: vào 0.25 · ra 1.50
  - `gemini-4-hydrogen`: vào 1.50 · ra 7.50

  Nguồn: https://ai.google.dev/gemini-api/docs/pricing, xem ngày 27/11/2026.
- **Tỉ lệ đạt** dùng để tính: **24/24 (100%)**, lượt `run-2` (run ID `run-2@20261128-103134`, lượt 2).
- Token đo trên model **`openai/gpt-oss-120b`** (qua Groq). Giá tính theo model **`gemini-3.1-flash-lite`** và **`gemini-4-hydrogen`**. Mỗi model tách token khác nhau, nên số token thật trên Gemini có thể lệch so với số đo.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-110358` · **50 phiên** (0 phiên lỗi) · seed 42.
Lệnh: `python run.py simulate --rate-from eval/run-2.csv`

Token đo được theo persona (chép từ `cost/simulate-1-summary.md`):

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 22 | 1 | 821 | 443 | 1.0 | 2.8 |
| dung_vua | 18 | 2 | 1657 | 850 | 2.0 | 5.9 |
| dung_nhieu | 10 | 3 | 2457 | 1346 | 3.0 | 8.1 |

Chi phí (tỷ giá 1 USD = 25.400 ₫, Vietcombank ngày 27/11/2026):

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (300) | / tháng — cơ sở (700) | / tháng — cao (1.200) | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0015 (≈ 39 ₫) | $0.0015 (≈ 39 ₫) | $3.07 (≈ 77.930 ₫) | $7.16 (≈ 181.838 ₫) | $12.27 (≈ 311.722 ₫) | $0.0102 (≈ 260 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0079 (≈ 202 ₫) | $0.0079 (≈ 202 ₫) | $16.07 (≈ 408.129 ₫) | $37.49 (≈ 952.300 ₫) | $64.27 (≈ 1.632.515 ₫) | $0.0536 (≈ 1.360 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**. Ở đây chi phí / task thành công trùng với chi phí / phiên vì lượt 2 đạt thật 24/24 trên bộ câu thử. Bộ câu thử chỉ có 24 câu, nên khi dùng thật tỉ lệ đạt có thể thấp hơn. Khi đó chi phí / task thành công sẽ tăng tương ứng: ví dụ đạt 80% thì flash-lite là ≈ $0.0019 / task *(tự ước tính, chưa đo)*.

## 3. So với impact

- **Impact / người / tháng** (`spec.md` §2): 1,5 lần × 35 phút ≈ **52,5 phút** kiểm tra thủ công được tiết kiệm. Ngoài ra còn tránh rủi ro mất 50.000–120.000 ₫ tiền xe khi tới nơi gặp điểm đóng cửa (phỏng vấn P2, P3).
- **Chi phí / người / tháng** (cơ sở): **≈ 260 ₫** với model `gemini-3.1-flash-lite`, **≈ 1.360 ₫** với model `gemini-4-hydrogen`.
- **Kết luận một dòng — đáng làm không:** **Đáng làm.** Kể cả với model đắt (≈ 1.360 ₫ / người / tháng), chi phí vẫn chưa bằng 3% của một lần mất tiền xe 50.000 ₫, trong khi mỗi người tiết kiệm được khoảng 52 phút / tháng. Ở mức cơ sở (700 người), tổng chi phí chỉ khoảng 182.000–952.000 ₫ / tháng.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
