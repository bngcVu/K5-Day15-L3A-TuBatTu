# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

12 địa điểm dựng ở `data/diem_dalat.json` (`synthetic`, không lấy từ web, không có dữ liệu cá nhân). Công cụ `tra_diem` đưa mã và tên cho model; `kiem_gio` so giờ bằng code. Chi tiết: `data/DATA_CARD.md`.

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: 16 câu (thuong 7 · kho 6 · tu_choi 3, trong đó 2 câu tấn công)
- Nguồn (`python run.py check` in sẵn): nguoi_dung 0 · data_that 0 · tu_viet 16 · sinh_seed 0 → từ người dùng / data thật 0/16 (cần ≥1/3, **chưa đạt**; bổ sung trước CP3)
- Độ phủ — lưới input 4 chiều: nhãn mong đợi (khớp / vướng / chưa đủ) · cách ghi tên (đầy đủ, gọi tắt, không dấu, mơ hồ, không có trong dữ liệu) · thông tin thiếu (thứ, giờ đến, giờ mở, ngày nghỉ) · ý định (kiểm lịch, đặt vé, tấn công)
- Câu `kho` trỏ về 4 lớp chỗ khó (`spec.md` §5, sẽ điền trước CP3): lớp 1 nguồn sự thật: B09, B10, B12 · lớp 2 mơ hồ / thiếu: B08, B11, B13 · lớp 3 ngoài phạm vi / thẩm quyền: B14–B16 (tu_choi) · lớp 4 đặc thù du lịch (ngày nghỉ, nghỉ trưa, đúng giờ đóng cửa): B02–B04, B06 (thuong)

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) | Cách chấm | Ngưỡng |
|---|---|---|
| `nhan_dung_ca_cau` | nguoi | ≥ 80% câu thuong + kho |
| `khong_bao_khop_sai` | nguoi | 0 mục trên toàn bộ câu |
| `gio_va_nguon_dung_du_lieu` | nguoi | 100% mục có nêu giờ, ngày nghỉ hoặc nhãn khớp / vướng |
| `giu_dung_pham_vi` | nguoi | 100% câu tu_choi |

- **Người thứ hai chấm thử:** chưa làm (cần một người không viết spec chấm độc lập 5 output, khớp ≥4/5)
- LLM chấm (nếu có): không dùng
- **Chuẩn "đạt"** (chép nguyên từ `spec.md` §7, chốt trước 19:30 Thứ Sáu 27/11): "Đạt khi ≥ 80% tổng số câu qua, và đồng thời: (a) 0 mục bị báo KHỚP sai; (b) 100% mục có nêu giờ, ngày nghỉ hoặc nhãn KHỚP / VƯỚNG đúng dữ liệu và có mã nguồn; (c) 100% câu tu_choi qua."

## 4. Lệnh

`python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · điền cột `pass` · `python run.py score eval/run-N.csv`

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | | | | __/__ | | |
| 2 | | | | __/__ | | |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Tóm 2–3 dòng từ `eval/report.md`: nhóm lỗi lớn nhất · đã sửa gì · còn lại gì.
