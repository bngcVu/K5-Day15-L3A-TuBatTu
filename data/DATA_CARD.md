# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp. Track C không được BTC cấp data.

## Dataset 1 · Danh sách địa điểm (`data/diem_dalat.json`)

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ `tra_diem`, `kiem_gio`; căn cứ để chấm bộ câu thử |
| Từ đâu | Nhóm tự dựng: bản nháp do coding agent (Claude Code) viết tay, **không sinh bằng seed** |
| Xử lý những bước gì | Không lọc, không làm sạch, không lấy từ web. Không có dữ liệu cá nhân |
| Số dòng / số đoạn | 12 địa điểm (mã DL01–DL12) |
| Phiên bản / ngày lấy | Bản đầu, 27/11/2026 |
| Nhãn | `synthetic`: tên, giờ mở cửa, ngày nghỉ đều là dựng, **không phải thông tin du lịch thật** |
| Giới hạn | Chỉ có giờ mở và ngày nghỉ theo thứ; không có ngày lễ, giờ nhận khách cuối, giá vé, thời gian di chuyển. Dữ liệu sạch hơn thực tế: chưa có thông tin mâu thuẫn giữa các nguồn hoặc đã cũ |

**Chỗ khó cài sẵn:** hai điểm trùng tên gọi "vườn hoa" (DL02, DL03) · một điểm chưa có giờ mở (DL09) · một điểm chưa có ngày nghỉ (DL10) · một điểm nghỉ trưa (DL04) · một điểm chỉ mở cuối tuần (DL12).

**Quy ước:** `nghi: []` là mở cả tuần; `null` là chưa rõ. Đến đúng giờ đóng cửa tính là vướng.

**Cách sinh:** coding agent viết trực tiếp theo yêu cầu "địa điểm tên dựng, có đủ các chỗ khó ở trên". **Người kiểm:** Nguyễn Thế Trường (cùng rà soát tự động qua script) · **số dòng đã kiểm tay:** 12/12 (khớp schema `ma/ten/ten_khac/gio/nghi`, 5 chỗ khó và các câu `eval/benchmark.csv`).

## Dataset 2 · Bộ câu thử (`eval/benchmark.csv`)

| | |
|---|---|
| Dùng để làm gì | Bộ câu thử để đo theo `eval/metric_spec.yaml` |
| Từ đâu | 16 câu nháp (`tu_viet`) + 8 câu trích xuất từ phỏng vấn P1–P3 và khảo sát người dùng (`nguoi_dung`) |
| Số dòng | 24: thuong 11 · kho 9 · tu_choi 4 (trong đó 2 câu tấn công) |
| Nhãn | `synthetic` kết hợp `nguoi_dung` |
| Giới hạn | **8/24 câu (33.3%) từ người dùng thật** (`nguoi_dung`), đạt chuẩn CP3 (≥1/3). Phản ánh chính xác các tình huống người dùng thực tế gặp phải (quán nghỉ, đến sớm, bảo tàng bảo trì, đòi hủy/hoàn tiền). **Người kiểm:** Tô Minh Thành & Nguyễn Thế Trường đã rà soát 24/24 câu (27/11/2026) |

Data tự dựng **không phải bằng chứng pain**.
