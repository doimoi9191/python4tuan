"""
    lambda - hàm nặc danh
"""

def handle(f,x):
    return f(x)
kq1=handle(lambda x:x**2,9)
print(kq1)

kq2 = handle(lambda x:x%2==0,4)
print(kq2)

"""
    Cùng là một hàm có tên handle nhưng thông qua lambda expression chúng ta có thể gán cho nớ nhiều hàm
    khác nhau.
"""


"""
    Đối với những hàm phức tạp - complex thì phải bóc tách các hàm đó ra thành các hàm thành phần
"""

def LaSoChan(x):
    return x%2==0

# Cách 1 Viết tắt
kq3 = handle(LaSoChan,4)
print("kq3 =",kq3)
# Cách 2 Viết đầy đủ dễ hiểu
kq4 = handle(lambda x:LaSoChan(x),4)
print("kq4 =",kq4)