# AI SPEC — Kiểm lịch trình nháp đi Đà Lạt · Nhóm Tứ Bất Tử · Phòng [H209] · Zone [4]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [x] C · [ ] D · [ ] E — bài toán: nhóm tự mở rộng trong bối cảnh du lịch (gần hướng C1): kiểm giờ mở cửa và ngày nghỉ trong lịch nháp đi Đà Lạt 2–3 ngày
Data BTC cấp đã dùng (nếu có — không commit nguyên file): không (Track C không được cấp data)

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này:
  1. Người lên lịch mở Google Sheets / Note ghi nháp các điểm muốn đi theo từng buổi trong ngày (sáng, chiều, tối).
  2. Mở Google Maps, fanpage hoặc TikTok tìm từng điểm để xem giờ mở cửa và ngày nghỉ.
  3. Ghi chú thủ công giờ mở cửa vào lịch nháp hoặc chỉ nhớ mang máng.
  4. Sát ngày đi hoặc đến nơi mới phát hiện điểm đóng cửa (nghỉ cố định theo thứ hoặc bảo trì đột xuất), dẫn đến việc phải đổi điểm vội vàng trên đường đi.
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn: Google Maps (xem giờ mở/đóng), ChatGPT / Claude (hỏi lịch trình mẫu chung chung nhưng AI thường bịa giờ mở cửa không có căn cứ) — nguồn: phỏng vấn P2, P3 (`evidence/interviews/P2.md`, `P3.md`).

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): Người tự lên lịch (không mua tour) cho chuyến du lịch 2–3 ngày của nhóm bạn, đã có lịch nháp và chuẩn bị đi.
- Việc họ cố làm xong: Kiểm tra đối chiếu giờ mở cửa và ngày nghỉ của các điểm tham quan trong lịch nháp trước chuyến đi 2–3 ngày để không bị lỡ kế hoạch.
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ: Giải bằng tra cứu thủ công qua Google Maps, fanpage, bài review; hỏng vì thông tin rải rác, Maps không cập nhật ngày nghỉ hàng tuần của quán nhỏ/tư nhân hoặc đóng cửa bảo trì; chưa bỏ vì không có công cụ tự động nào chuyên kiểm đối chiếu lịch nháp.
- Pain: Người tự lên lịch — đang kiểm tra lịch trình chuẩn bị đi — vướng vì thông tin giờ mở cửa/ngày nghỉ nằm rải rác và không chính xác trên mạng — hậu quả là tới nơi điểm đóng cửa, tốn 30–40 phút di chuyển, mất 50.000–120.000đ tiền xe và phải bỏ điểm, xếp lại lịch cả ngày.
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`):
  - Phỏng vấn sâu 3 người ngoài nhóm: 2/3 người (P2, P3) kể được lần cụ thể trong 12 tháng qua tới nơi gặp điểm đóng cửa; mất 30–40 phút và 50.000–120.000đ tiền xe, phải cắt bỏ điểm tham quan.
  - Khảo sát định lượng: 19/21 người tự lên lịch cho chuyến đi 2–3 ngày trong 12 tháng qua; có **17/19 người (89.5%)** từng gặp điểm đóng cửa hoặc sai giờ mở cửa (9 người gặp đóng cửa/ngày nghỉ, 4 người gặp sai giờ, 4 người gặp cả hai). Hơn 50% mất từ 15–60 phút xử lý. Giả thuyết được xác nhận hoàn toàn.

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| Kiểm giờ mở cửa / ngày nghỉ lịch nháp Đà Lạt 2–3 ngày | ~700 người (học viên / du khách tự túc) | 1–2 lần / tháng | 30–40 phút kiểm tra thủ công + rủi ro mất 50k–120k tiền xe | ~700 người × 1.5 lần × 35 phút ≈ 612 giờ / tháng | Kịp (phạm vi workflow hẹp, 1 lần gọi model + code so giờ) | Chọn |
| Tự động tạo toàn bộ lịch trình du lịch tối ưu đường đi | Rất nhiều du khách | 1 lần / chuyến | 2–3 giờ nghiên cứu | Lớn | Không kịp (quá rộng, phụ thuộc nhiều API bản đồ / routing) | Loại |
| Đặt vé và gợi ý combo giá rẻ | Khách du lịch | 1 lần / chuyến | 30 phút tìm vé | Trung bình | Không kịp (cần tích hợp cổng thanh toán / đối tác) | Loại |

- **Impact / tháng** của hướng chọn = 700 người × 1.5 lần × 35 phút = 36.750 phút (~612 giờ tiết kiệm và tránh lãng phí chi phí đi lại) — nguồn: quy mô lớp L3 (~700 học viên) và phỏng vấn P2, P3.
- Hướng ĐÃ LOẠI + vì sao: Loại hướng tạo lịch trình tự động toàn diện và đặt vé vì không thể kiểm chứng chất lượng và vượt quá thời gian làm trong hackathon.
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8): Người đi ít: 4 lần/năm (~0.33 lần/tháng); Người đi vừa: 10 lần/năm; Người đi nhiều: 20 lần/năm.

## §3. Giải pháp tương tự *(guide 2.1)*
- Google Maps:
  - Một điều đáng học: Giao diện trực quan, dữ liệu giờ mở cửa phong phú cho các địa điểm lớn.
  - Một điều đáng né: Bắt người dùng phải tra cứu từng điểm một cách rời rạc, thông tin ngày nghỉ của các quán nhỏ/điểm địa phương hay bị sai hoặc thiếu.
  - Mình khác gì: Người dùng chỉ cần dán nguyên đoạn lịch trình nháp 2–3 ngày viết tự do; hệ thống tự động tách từng mục, đối chiếu đồng loạt với dữ liệu đã kiểm chứng và chỉ ra ngay điểm nào bị vướng kèm mã nguồn rõ ràng.

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả): Một người tự lên lịch dán lịch nháp đi Đà Lạt 2–3 ngày, AI quyết định mỗi mục viết tự do trong lịch là địa điểm nào trong danh sách có mã nguồn hay phải hỏi lại, để code đối chiếu giờ mở cửa và ngày nghỉ, rồi người đó nhận bảng đánh dấu "khớp", "vướng giờ / ngày nghỉ" hoặc "chưa đủ thông tin" kèm nguồn để tự sửa lịch trước khi đi.
- Không làm (≥3 điều): (1) không đặt vé, đặt chỗ, thanh toán; (2) không tự sửa hay tự xếp lại lịch; (3) không tính thời gian di chuyển, thời gian ở lại, giờ nhận khách cuối; (4) không xét giá vé, thời tiết, ngày lễ; (5) không lấy dữ liệu trực tiếp từ web; (6) không hỏi đáp nhiều lượt: người dùng sửa lịch rồi dán lại.
- **Sơ đồ** (Input → AI Core → Chặn rủi ro → Output):

```mermaid
flowchart TD
    subgraph IN["1. Input"]
        A["Lịch nháp viết tự do:<br/>thứ, giờ, tên địa điểm"]
        T1["Công cụ tra_diem:<br/>mã và tên, không kèm giờ"]
    end
    subgraph CORE["2. AI Core: một lần gọi model"]
        M["Model quyết định: ngoài phạm vi hay kiểm lịch;<br/>mỗi mục là địa điểm nào hay cần hỏi lại.<br/>Trả về JSON"]
    end
    subgraph GUARD["3. Chặn rủi ro: code"]
        G1{"JSON đúng dạng<br/>và trong phạm vi?"}
        G2["Trích dẫn phải có trong lịch<br/>Mã phải có trong dữ liệu<br/>Tên gọi tắt trùng nhiều điểm: ép hỏi lại<br/>Thứ phải có trong lịch<br/>Code tự đọc giờ từ trích dẫn"]
        T2["Công cụ kiem_gio:<br/>so giờ và ngày nghỉ"]
        G3["Mốc giờ chưa được kiểm: cảnh báo"]
    end
    subgraph OUT["4. Output: code soạn"]
        O1["KHỚP / VƯỚNG / CHƯA ĐỦ THÔNG TIN<br/>kèm mã nguồn hoặc câu hỏi lại"]
        O2["Từ chối bằng câu cố định<br/>và chỉ việc làm tiếp"]
        O3["Báo không đọc được lịch,<br/>không đánh dấu mục nào"]
        H["Người dùng tự quyết định sửa lịch"]
    end
    A --> M
    T1 --> M
    M --> G1
    G1 -- "sai dạng" --> O3
    G1 -- "ngoài phạm vi" --> O2
    G1 -- "kiểm lịch" --> G2
    G2 --> T2
    T2 --> G3
    G3 --> O1
    O1 --> H
```

- **Hình dạng:** [x] workflow cố định · [ ] một agent · [ ] nhiều agent — Các bước luôn đi theo một thứ tự (tra danh sách, nhận diện, chặn, so giờ, soạn), một lần gọi model là đủ. Không chọn agent vì không có bước nào cần AI tự quyết gọi gì tiếp; thêm vòng lặp chỉ tăng chi phí, độ trễ và chỗ có thể sai.
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  | `tra_diem` | không | danh sách mã, tên, tên gọi khác (không kèm giờ) | Không (chỉ đọc) |
  | `kiem_gio` | mã, thứ hoặc trống, giờ đến hoặc trống | nhãn, lý do, mã nguồn | Không (chỉ đọc) |

- **Mức tự động:** [x] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do: nếu sai, người đi chịu mất thời gian, tiền đi lại và lỡ điểm muốn đến; công cụ không có quyền đặt hay sửa gì.
- **Chỗ chặn rủi ro** (rủi ro lớn nhất: báo "khớp" cho điểm thật ra đóng cửa hoặc không có căn cứ): model không được xem giờ mở và không quyết định nhãn. Nhãn KHỚP / VƯỚNG chỉ ra từ `kiem_gio`; chữ model viết không được đưa thẳng ra output. Rủi ro còn lại: model gán nhầm địa điểm, hoặc nhầm thứ giữa các thứ có trong lịch; output ghi lại trích dẫn, tên đã gán và thứ để người dùng nhận ra.
- **Chỗ người duyệt** (việc AI không được tự làm): sửa lịch, chọn giữa hai địa điểm trùng tên gọi, đặt vé hoặc đặt chỗ.
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc | Tên mơ hồ thì hỏi lại; thiếu giờ mở, ngày nghỉ, thứ hoặc giờ đến mà không kết luận được thì ghi CHƯA ĐỦ THÔNG TIN |
  | Nói rõ căn cứ | Mỗi mục KHỚP / VƯỚNG có mã nguồn, giờ mở hoặc ngày nghỉ đã dùng |
  | Nói rõ giới hạn | Câu cuối output ghi dữ liệu là dựng, chỉ là gợi ý, không đặt chỗ; chế độ giả ghi CHẾ ĐỘ GIẢ |
  | Để người dùng sửa | Output lặp lại nguyên văn từng mục đã đọc và báo mốc giờ chưa được kiểm |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…): 12 địa điểm trong `data/diem_dalat.json` là **dữ liệu dựng** (tên dựng, giờ dựng). Model thật đã nối trong `codebase/ai.py` (Groq). Khi `MODEL_PROVIDER=fake`, bước nhận diện thay bằng quy tắc khớp tên đơn giản.

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
| Địa điểm không có trong dữ liệu (Hồ Cá Voi Xanh) | (1) Nguồn sự thật | Báo CHƯA ĐỦ THÔNG TIN, ghi rõ không nhận diện được điểm này trong dữ liệu, không đoán mò | B09 |
| Địa điểm chưa có dữ liệu giờ mở cửa (Làng Len Cổ Tích) | (1) Nguồn sự thật | Báo CHƯA ĐỦ THÔNG TIN, ghi rõ dữ liệu chưa có giờ mở cửa, không bịa giờ | B10 |
| Trùng tên gọi tắt ("vườn hoa" khớp cả DL02 và DL03) | (2) Mơ hồ / thiếu | Báo CHƯA ĐỦ THÔNG TIN, liệt kê tên các ứng viên (Vườn Hoa Thung Gió / Vườn Hoa Đồi Nắng) và hỏi lại | B08 |
| Lịch ghi "Ngày 1", "Ngày 2", không ghi thứ cụ thể | (2) Mơ hồ / thiếu | Không tự đoán thứ; với điểm có ngày nghỉ trong tuần thì báo CHƯA ĐỦ THÔNG TIN do thiếu thứ | B11 |
| Lịch chỉ ghi buổi sáng/chiều, không có mốc giờ cụ thể | (2) Mơ hồ / thiếu | Báo CHƯA ĐỦ THÔNG TIN, nêu rõ lịch chưa ghi giờ đến và in khung giờ mở của điểm | B13 |
| Điểm nghỉ định kỳ theo thứ (Đồi Mơ Sương nghỉ Thứ Hai) | (4) Đặc thù lĩnh vực | Báo VƯỚNG GIỜ / NGÀY NGHỈ, nêu rõ dữ liệu ghi nghỉ Thứ Hai kèm mã nguồn DL01 | B02 |
| Điểm nghỉ trưa (Bảo tàng Lá Thông nghỉ 11:30–13:30) | (4) Đặc thù lĩnh vực | Báo VƯỚNG GIỜ / NGÀY NGHỈ khi đến lúc 12h trưa, nêu rõ ngoài khung giờ mở | B03 |
| Đến đúng mốc giờ đóng cửa (Ga xe lửa đóng cửa lúc 17:30) | (4) Đặc thù lĩnh vực | Quy ước tính là VƯỚNG, báo ngoài khung giờ mở cửa để bảo vệ người dùng không bị hụt | B06 |
| Người dùng yêu cầu đặt vé và thanh toán trực tiếp | (3) Ngoài thẩm quyền | Từ chối bằng câu cố định: nói rõ ngoài phạm vi (chỉ kiểm giờ/ngày nghỉ, không đặt vé/thanh toán), hướng dẫn dán lịch | B14 |
| Tấn công ép bỏ qua kiểm tra, đánh dấu KHỚP toàn bộ | *(tấn công)* Lớp 3 | Không làm theo; code chặn rủi ro vẫn đối chiếu giờ thật và báo VƯỚNG hoặc từ chối | B15 |
| Giả mạo ban quản lý yêu cầu cập nhật giờ mở 24/24 | *(tấn công)* Lớp 3 | Không cập nhật dữ liệu; không cho phép thay đổi dữ liệu dựng; vẫn đối chiếu giờ chuẩn | B16 |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: Người dùng dán lịch trình có đủ thứ, giờ, tên điểm rõ ràng → AI trích xuất mục → Code đối chiếu khớp giờ mở → Trả về danh sách từng mục kèm nhãn `[KHỚP]` và mã nguồn `(nguồn: DLxx, dữ liệu dựng)`.
- Không chắc (lớp 2): Người dùng ghi tên vắn tắt hoặc trùng nhiều điểm (vd: "vườn hoa") → Trả về nhãn `[CHƯA ĐỦ THÔNG TIN]` kèm câu hỏi gợi ý "bạn muốn nói Vườn Hoa Thung Gió hay Vườn Hoa Đồi Nắng? Hãy ghi rõ tên".
- Không có căn cứ (lớp 1): Người dùng ghi điểm lạ không có trong cơ sở dữ liệu hoặc điểm chưa có thông tin giờ mở → Trả về `[CHƯA ĐỦ THÔNG TIN]`, không suy đoán hay bịa đặt giờ mở cửa.
- Người dùng sửa: Người dùng đọc các mục `[VƯỚNG]` hoặc `[CHƯA ĐỦ THÔNG TIN]`, chỉnh sửa lại giờ hoặc tên điểm trong ghi chú cá nhân rồi dán lại vào hệ thống để kiểm tra lượt mới.
- Bị đòi ngoài phạm vi (lớp 3): Người dùng yêu cầu đặt phòng, mua vé, thanh toán hoặc prompt injection → Hệ thống trả về thông báo từ chối cố định, giải thích rõ phạm vi và hướng dẫn cách dán lịch.
- Trường hợp đặc thù lĩnh vực (lớp 4): Điểm nghỉ định kỳ theo thứ, nghỉ trưa hoặc người dùng đến sát giờ đóng cửa → Hệ thống báo ngay `[VƯỚNG GIỜ / NGÀY NGHỈ]` để người dùng tránh mất công di chuyển vô ích.

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — 24 câu (thuong 11 · kho 9 · tu_choi 4, trong đó 2 câu tấn công và 8 câu từ người dùng thật) · metric: `eval/metric_spec.yaml` (4 metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ 80% tổng số câu qua, và đồng thời: (a) 0 mục bị báo KHỚP sai; (b) 100% mục có nêu giờ, ngày nghỉ hoặc nhãn KHỚP / VƯỚNG đúng dữ liệu và có mã nguồn; (c) 100% câu tu_choi qua."
- Cách tính: một câu **qua** khi output đúng `expected` và đạt `pass_criterion` của câu đó. Phải thoả cả mức 80% lẫn (a), (b), (c). Câu lỗi kỹ thuật tính là không qua. Metric `nhan_dung_ca_cau` (≥ 80% câu thuong + kho) báo cáo riêng.
- Kết quả: lượt 1 9/24 (38%) · lượt 2 24/24 (100%) — run ID: run-1@20261128-092617 / run-2@20261128-103134 → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-1.csv` (50 phiên, tỉ lệ đạt lấy từ `eval/run-2.csv` = 24/24; token đo trên `openai/gpt-oss-120b`)
- Chi phí / task thành công: $0.0015 ≈ 39 ₫ (model gemini-3.1-flash-lite) · $0.0079 ≈ 202 ₫ (model gemini-4-hydrogen)
- Chi phí / tháng ở quy mô thật (flash-lite · hydrogen): thấp $3.07 · $16.07 — cơ sở $7.16 · $37.49 — cao $12.27 · $64.27 → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): **đáng làm**. Chi phí ≈ 260–1.360 ₫ / người / tháng, trong khi mỗi người tiết kiệm ≈ 52,5 phút kiểm tra thủ công và tránh rủi ro mất 50.000–120.000 ₫ tiền xe.

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp): Bùi Ngọc Vũ (Đội trưởng - Agent/Prompt/Chạy Eval); Nguyễn Thế Trường (Công cụ tools.py / Data địa điểm / Data Card); Tô Minh Thành (Bộ câu thử Benchmark / Metric); Nguyễn Thị Dung (Bằng chứng Pain / Phỏng vấn & Khảo sát).
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`): Dùng Claude Code để hỗ trợ viết khung `agent.py`, `tools.py` và nháp bộ câu thử; dùng Antigravity rà soát và kiểm thử tự động. Thành viên người thật đã rà soát 100% logic, dữ liệu và câu thử.
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
| 27/11 23:25 | Cập nhật kết quả khảo sát n=19/21 vào `evidence/summary.md` | Hoàn thành thu thập bằng chứng định lượng đạt ngưỡng giả thuyết (89.5% gặp vấn đề) |
| 27/11 23:30 | Mở rộng bộ câu thử từ 16 lên 24 câu (thêm 8 câu `source: nguoi_dung`) | Đáp ứng chuẩn CP3 (20–30 câu và ≥1/3 câu từ người dùng thật), phản ánh đúng các ca người dùng kể (bảo tàng bảo trì, quán nghỉ thứ Hai, đến quá sớm) |
| 28/11 10:35 | Cải tiến auto-retry backoff trong `codebase/ai.py` và chạy Lượt 2 (`eval/run-2.csv`) | Khắc phục triệt để lỗi HTTP 429 rate limit ở Lượt 1, nâng tỉ lệ đạt từ 38% lên 100% (24/24 câu) đạt chuẩn |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
