"""
BMI = chỉ số cân dối cơ thể
"""

def BMI(cc,cn):
    return cn/cc/cc

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi <= 24.9:
        return "Bình thường"
    elif bmi <= 29.9:
        return "Hơi béo"
    elif bmi <= 34.9:
        return "Béo phì cấp độ 1"
    elif bmi <= 39.9:
        return "Béo phì cấp độ 2"
    else:
        return "Béo phì cấp độ 3"
def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <= 24.9:
        return "trung bình"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất cao"
    else:
        return "Nguy hiểm"




print("nhập vào chiều cao: ")
cc=float(input())
print("nhập vào cân nặng: ")
cn=float(input())

bmi=BMI(cc,cn)

print("BMI của bạn =", bmi)
print("Phân loại cân nặng của bạn là",PhanLoai(bmi))
print("Nguy cơ bệnh của chú là",NguyCoBenh(bmi))