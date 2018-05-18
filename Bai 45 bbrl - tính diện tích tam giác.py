"""ôn tập các hàm toán học
if else
theo công thức hê rông
cv= a+b+c
p=cv/2
dt=căn bậc hai(p*(p-a)*(p-b)*(p-c))


"""

from math import *
a,b,c = eval(input("lần lượt nhập 3 cạnh của một tam giác"))

cv = a+b+c
p = cv/2
dt = sqrt(p*(p-a)*(p-b)*(p-c))
print(dt)
