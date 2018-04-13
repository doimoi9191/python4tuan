"""
1,3,5,7,8,10,12 - 31 ngày
4,6,9,11 -> 30 ngày
tháng 2 thì kt năm nhuận
"""

print("CHƯƠNG TRÌNH ĐẾM SỐ NGÀY TRONG THÁNG")
m = int(input("Nhập vào một tháng: "))
if m in (1,3,5,7,8,10,12):
    print("Tháng ",m,"có 31 ngày")
elif m in (4,6,9,11):
    print("Tháng ",m,"có 30 ngày")
elif m == 2:
    y = int(input("Mời bạn nhập vào năm: "))
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("Tháng ",m,"có 29 ngày")
    else:
        print("Tháng ",m,"có 28 ngày")
else:
    print("Tháng ",m,"không hợp lệ")