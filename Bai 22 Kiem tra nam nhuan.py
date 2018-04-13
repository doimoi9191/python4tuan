"""
Năm nhuận là năm:
1.chia hết cho 4 nhưng không chia hết cho 100
2. hoặc chia hết cho 400
"""
print("chương trình kiểm tra năm nhuận")
year = int(input("mời thím nhập vào 1 năm: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Năm ",year,"là năm nhuận.")
else:
    print("Năm ",year,"không nhuận.")