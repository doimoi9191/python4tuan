"""
Câu 6: nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm
"""
# print("CÂU 1")
# x=3
# y=5
# z=7
# print("x==3:",x==3)
# print("x<y:",x<y)
# print("x>=y:",x>=y)
# print("x<=y:",x<=y)
# print("x!=y-2:",x!=y-2)
# print("x<10:",x<10)
# print("x>=0 and x<10:",x>=0 and x<10)
# print("x<0 and x<10:",x<0 and x<10)
# print("x>=0 and x<2:",x>=0 and x<2)
# print("x<0 or x<10:",x<0 or x<10)
# print("x>0 or x<10:",x>0 or x<10)
# print("x<0 or x>10:",x<0 or x>10)
# print("HẾT CÂU 1")

# print("CÂU 2")
# print("""
#     Mời bạn nhập vào các số i,j,k.
#     Bắt buộc phải nằm trong các cặp số sau:
#     a) i,j,k = 3,5,7
#     b) i,j,k = 3,7,5
#     c) i,j,k = 5,3,7
#     d) i,j,k = 5,7,3
#     e) i,j,k = 7,3,5
#     f) i,j,k = 7,5,3
# """)
# i = int(input("i = :"))
# j = int(input("j = :"))
# k = int(input("k = :"))
#
# if((i==3 and j==5 and k==7)or(i==3 and j==7 and k==5)or(i==5 and j==3 and k==7)or(i==5 and j==7 and k==3)or(i==7 and j==3 and k==5)or(i==7 and j==5 and k==3)):
#     if i < j:
#         if j < k:
#             i = j
#         else:
#             j = k
#     else:
#         if j > k:
#             j = i
#         else:
#             i = k
#     print("i = ", i, "j = ", j, "k = ", k)
# else:
#     print("NHẬP SAI BỘ SỐ")
# print("\nHẾT CÂU 2")
# print("CÂU 3")
# a= int(input("Nhập vào số có 2 tối đa 2 chữ số: "))
# i = a//10
# j = a%10
#
# if a>=10 and a<=99:
#     if i == 1:
#         dli = "Mười"
#     elif i == 2:
#         dli = "Hai mươi"
#     elif i == 3:
#         dli = "Ba mươi"
#     elif i == 4:
#         dli = "Bốn mươi"
#     elif i == 5:
#         dli = "Năm mươi"
#     elif i == 6:
#         dli = "Sáu mươi"
#     elif i == 7:
#         dli = "Bảy mươi"
#     elif i == 8:
#         dli = "Tám mươi"
#     elif i == 9:
#         dli = "Chín mươi"
#     else:
#         dli=""
#     if j == 1:
#         dlj = "một"
#     elif j == 2:
#         dlj = "hai"
#     elif j == 3:
#         dlj = "ba"
#     elif j == 4:
#         dlj = "bốn"
#     elif j == 5:
#         dlj = "năm"
#     elif j == 6:
#         dlj = "sáu"
#     elif j == 7:
#         dlj = "bảy"
#     elif j == 8:
#         dlj = "tám"
#     elif j == 9:
#         dlj = "chín"
#     else:
#         dlj=""
#     print("Số ",a,"được đọc là: ",dli,'', dlj)
# else:
#     print("ngoài vùng phủ sóng")
# print("HẾT CÂU 3")
# print("CÂU 4")
# d = int(input("Ngày: "))
# m = int(input("Tháng: "))
# y = int(input("Năm: "))
#
# d2 = 0
# m2 = 0
# y2= 0
#
# if ((d <= 0) or (m <= 0) or (y <= 0)):
#     print("Exception 1")
#     exit()
# else:
#     # nếu năm nhuận
#     if ((y%4==0)and(y%100!=0)) or (y%400==0):
#         # tháng 2 có 29 ngày
#         print("Năm nhuận - tháng 2 có 29 ngày")
#         # nếu tháng nhập vào = 1,3,5,7,8,10,12
#         if m in (1,3,5,7,8,10,12):
#             # nếu tháng = 12
#             if m == 12:
#                 # nếu ngày nhập vào thêm một ngày > 31
#                 if (d + 1 > 31):
#                     # thì ngày mới = 1
#                     d2 = 1
#                     # tháng mới = 1
#                     m2 = 1
#                     # năm mới = năm cũ + 1
#                     y2 = y + 1
#                 # ngược lại nếu d + 1 <= 31
#                 else:
#                     # thì d2 = d + 1
#                     d2 = d + 1
#                     #  tháng giữ nguyên
#                     m2 = m
#                     # năm giữ nguyên
#                     y2 = y
#             # nếu tháng khác 12 - tức là tháng = 1,3,5,7,8,10
#             else:
#                 if (d + 1 > 31):
#                     d2 = 1
#                     m2 = m +1
#                     y2 = y
#                 else:
#                     d2 = d + 1
#                     m2 = m
#                     y2 = y
#         elif m in (4,6,9,11):
#             if (d + 1 > 30):
#                 d2 = 1
#                 m2 = m + 1
#                 y2 = y
#             else:
#                 d2 = d + 1
#                 m2 = m
#                 y2 = y
#         else:
#             if d > 29:
#                 print("Tháng 2 năm nhuận có 29 ngày chứ méo có ",d,'ngày')
#                 exit()
#             elif (d + 1 > 29):
#                 d2 = 1
#                 m2 = m + 1
#                 y2 = y
#             else:
#                 d2 = d + 1
#                 m2 = m
#                 y2 = y
#         # print("Sau ngày ", d, "/", m, "/", y, "là ngày: ", d2, '/', m2, '/', y2)
#     else:
#         print("Năm không nhuận - tháng 2 có 28 ngày")
#         if m in (1,3,5,7,8,10,12):
#             if m == 12:
#                 if (d + 1 > 31):
#                     d2 = 1
#                     m2 = 1
#                     y2 = y + 1
#                 else:
#                     d2 = d + 1
#                     m2 = m
#                     y2 = y
#             else:
#                 if (d + 1 > 31):
#                     d2 = 1
#                     m2 = m +1
#                     y2 = y
#                 else:
#                     d2 = d + 1
#                     m2 = m
#                     y2 = y
#         elif m in (4,6,9,11):
#             if (d + 1 > 30):
#                 d2 = 1
#                 m2 = m + 1
#                 y2 = y
#             else:
#                 d2 = d + 1
#                 m2 = m
#                 y2 = y
#         else:
#             if d > 28:
#                 print("Tháng 2 năm không nhuận có 28 ngày chứ méo có ",d,'ngày')
#                 exit()
#             elif (d + 1 > 28):
#                 d2 = 1
#                 m2 = m + 1
#                 y2 = y
#             else:
#                 d2 = d + 1
#                 m2 = m
#                 y2 = y
# print("Sau ngày ",d,"/",m,"/",y,"là ngày: ",d2,'/',m2,'/',y2)
# print("CÂU 5")
# def pheptoan(x,y,pt):
#     if pt == '+':
#         return x + y
#     elif pt == '-':
#         return x - y
#     elif pt == '*':
#         return x * y
#     else:
#         return x/y
#
# a = int(input("Nhập vào số a: "))
# b = int(input("Nhập vào số b: "))
# c = input("""
#     Nhập vào tên phép toán.
#     Ví dụ:
#     phép cộng nhập vào là +
#     phép trừ nhập vào là -
#     phép nhân nhập vào là *
#     phép chia nhập vào là /
# """)
# print("Kết quả của phép toán: ",a,c,b,"=",pheptoan(a,b,c))
# print("HẾT CÂU 5")
print("CÂU 6")
t = int(input("Nhập vào tháng trong năm: "))
if t in (1,2,3):
    print("Quý 1")
elif t in (4,5,6):
    print("Quý 2")
elif t in (7,8,9):
    print("Quý 3")
elif t in (10,11,12):
    print("Quý 4")
else:
    print("Ngoài vùng phủ sóng")