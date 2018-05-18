"""
ROI = return on investment - đo lường hiệu quả đồng vốn đầu tư
ROI = (doanh thu - chi phí)/ chi phí
"""
def ROI(dt,cp):
    return (dt-cp)/cp
def GoiYDauTu(roi):
    if roi >= 0.57:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"

print("Chương trình tính ROI")
dt = int(input("Nhập doanh thu"))
cp = int(input("Nhập chi phí"))

roi = ROI(dt,cp)
print("Tỉ lệ ROI:",roi)
print("Gọi ý đầu tư",GoiYDauTu(roi))