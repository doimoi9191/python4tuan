"""
python tương tự c++, có hỗ trợ parameter mặc định khi khao báo hàm
hàm print ta sd cũng có các parameter mặc định
def print(self, *args, sep=' ', end='\n', file=None):
"""
def SumRange(n,m=0):
    sum = 0
    for i in range(1,m+n,1):
        sum=i
    return sum

x1=SumRange(5)
print("x1=",x1)
x2=SumRange(5,1)
print("x2=",x2)