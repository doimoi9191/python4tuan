"""
hàm hữu dụng trong viết game,giả lập dữ liệu, thống kê
randrange(x,5) -> lấy số ngẫu nhiên >= x và < y
"""
from random import *
count=0
while True:
    x=randrange(-100,100)
    count+=1
    print(x,end=',')
    if x is 50:
        break
print()
print("BYE")
print(count)