"""
câu 1:
cho x,y,z = 3,5,7
hãy cho biết kết quả boolead expression

x==3
x<y
x>=y
x<=y
x!=y-2
x<10
x>=0 and x<10
x<0 and x<10
x>=0 and x<2
x<0 or x<10
x>0 or x<10
x<0 or x>10

Câu 2: cho i,j,k là các con số và lệnh dưới đây:
if i < j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print("i = ",i,"j = ",j,"k = ",k)

Hãy cho biết kết quả xuất ra màn hình nếu tuần tự 3 biên trên có các giá trị sau:
a. i,j,k = 3,5,7
a. i,j,k = 3,7,5
a. i,j,k = 5,3,7
a. i,j,k = 5,7,3
a. i,j,k = 7,3,5
a. i,j,k = 7,5,3

Câu 3: nhập một số có tối đa 2 chữ số, hãy cho biết cách độc ra dạng chữ
vd: n=35 -> ba mươi lăm, n=5 -> năm
Câu 4: nhập vào một ngày (ngày, tháng,năm). tìm ngày kế sau ngày vừa nhập(ngày/tháng/năm)
Câu 5: nhập vào 2 giá trị a,b và phép toán +,-,*,/ hãy xuất kết quả theo đúng phép toán đã nhập
Câu 6: nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm
"""

from math import math
print('-'*20)
print("CÂU 1")
x=3
y=5
z=7

x==3
x<y
x>=y
x<=y
x!=y-2
x<10
x>=0 and x<10
x<0 and x<10
x>=0 and x<2
x<0 or x<10
x>0 or x<10
x<0 or x>10