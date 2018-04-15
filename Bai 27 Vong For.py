"""
Lập tuần tự các công việc
dùng range để định nghĩa vùng dữ liệu lặp và bước lặp
cú pháp hàm range: range(begin,end,step)
begin: giá trị bắt đầu
end: giá trị cuối
step: bước nhảy

range(10) -> 0,1,2,3,4,5,6,7,8,9
range(1,10) -> 1,2,3,4,5,6,7,8,9
range(1,11,2) -> 1,3,5,7,9

for n in range():
    pass
"""
n = int(input("mời nhập số: "))
s = 0
if n%2 == 0:
    for x in range(2,n+1,2):
        s = s+x
elif n%2 != 0:
    for x in range(1,n+1,2):
        s=s+x
print("Tổng s=",s)