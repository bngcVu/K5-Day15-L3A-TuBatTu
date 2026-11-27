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

**Cách sinh:** coding agent viết trực tiếp theo yêu cầu "địa điểm tên dựng, có đủ các chỗ khó ở trên". **Người kiểm:** chưa có · **số dòng đã kiểm tay:** 0/12.

## Dataset 2 · Bộ câu thử (`eval/benchmark.csv`)

| | |
|---|---|
| Dùng để làm gì | Bộ câu thử để đo theo `eval/metric_spec.yaml` |
| Từ đâu | Bản nháp do coding agent viết (`tu_viet`) |
| Số dòng | 16: thuong 7 · kho 6 · tu_choi 3 (2 câu tấn công) |
| Nhãn | `synthetic` |
| Giới hạn | **0/16 câu từ người dùng hoặc data thật.** CP3 cần 20–30 câu và ≥1/3 từ `nguoi_dung` / `data_that` (thêm ≥8 câu thật vào 16 câu này sẽ được 24 câu). Người viết code và người viết câu thử là cùng một agent, nên bộ này dễ nương theo code. **Người kiểm:** chưa có |

Data tự dựng **không phải bằng chứng pain**.
