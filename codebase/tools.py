"""Công cụ của bài toán: kiểm lịch trình nháp đi Đà Lạt (Track C — Du lịch). Sơ đồ ở spec.md §4.

Mỗi công cụ là một hàm Python có @tool. Docstring ghi đúng 4 ý: tên · input · output · có tác động ra ngoài không.
Cả hai công cụ chỉ đọc. Dữ liệu ở data/diem_dalat.json là DỰNG (synthetic), mô tả ở data/DATA_CARD.md.
So giờ làm bằng code ở đây, không để model tự tính.
"""
import json
import os

from tracing import tool, TOOLS  # noqa: F401  (TOOLS: danh sách công cụ đã đăng ký, dùng khi viết vòng lặp agent)

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "diem_dalat.json")
TEN_THU = {"t2": "Thứ Hai", "t3": "Thứ Ba", "t4": "Thứ Tư", "t5": "Thứ Năm",
           "t6": "Thứ Sáu", "t7": "Thứ Bảy", "cn": "Chủ Nhật"}


def doc_diem() -> dict:
    """Đọc file dữ liệu → {mã: địa điểm}."""
    with open(DATA, encoding="utf-8") as f:
        return {d["ma"]: d for d in json.load(f)["diem"]}


@tool
def tra_diem() -> list:
    """Tên: tra_diem. Input: không. Output: danh sách {"ma", "ten", "ten_khac"} (không kèm giờ).
    Không tác động ra ngoài."""
    return [{"ma": d["ma"], "ten": d["ten"], "ten_khac": d["ten_khac"]} for d in doc_diem().values()]


@tool
def kiem_gio(ma: str, thu, gio) -> dict:
    """Tên: kiem_gio. Input: mã địa điểm, thứ ("t2"…"t7", "cn" hoặc None), giờ đến ("HH:MM" hoặc None).
    Output: {"nhan": "khop" | "vuong" | "chua_du", "ly_do", "nguon"}. Không tác động ra ngoài."""
    d = doc_diem().get(ma)
    if d is None:
        return {"nhan": "chua_du", "ly_do": "không có địa điểm này trong dữ liệu", "nguon": ""}

    def ket(nhan, ly_do):
        return {"nhan": nhan, "ly_do": ly_do, "nguon": ma}

    if thu and d["nghi"] and thu in d["nghi"]:
        return ket("vuong", "dữ liệu ghi nghỉ %s" % TEN_THU[thu])
    if d["gio"] is None:
        return ket("chua_du", "dữ liệu chưa có giờ mở cửa")
    khung = ", ".join("%s–%s" % (a, b) for a, b in d["gio"])
    if gio is None:
        return ket("chua_du", "lịch chưa ghi giờ đến (giờ mở: %s)" % khung)
    if not any(a <= gio < b for a, b in d["gio"]):  # chuỗi "HH:MM" so được theo thứ tự chữ
        return ket("vuong", "đến lúc %s, ngoài giờ mở %s" % (gio, khung))
    if d["nghi"] is None:
        return ket("chua_du", "trong giờ mở %s nhưng dữ liệu chưa có ngày nghỉ" % khung)
    if d["nghi"] and thu is None:
        nghi = ", ".join(TEN_THU[t] for t in d["nghi"])
        return ket("chua_du", "trong giờ mở %s nhưng lịch chưa ghi thứ (điểm này nghỉ %s)" % (khung, nghi))
    return ket("khop", "trong giờ mở %s" % khung)
