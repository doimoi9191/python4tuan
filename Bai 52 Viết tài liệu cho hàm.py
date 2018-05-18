"""
python hỗ trợ cta bổ sung hdsd - tài liệu - document cho hàm
sử dụng 3 dấu nháy kép or 3 dấu nháy đơn (nên dùng 3 dấu nháy kép)
các ghi chú phải dc viết ở những odngf đầu tiên khi khai báo hàm
"""

def UCLN(a,b):
    """
    Hàm này dùng để tìm ước số chung lớn nhất.
    Ví dự a = 9, b= 6 thì UCLN là 3
    """
    min = a if a<b else b
    for i in range(min,0,-1):
        if a%i==0 and b%i==0:
            return i
    return 1
uoc = UCLN(25,15)
print(uoc)
