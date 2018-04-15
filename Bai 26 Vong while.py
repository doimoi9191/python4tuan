"""
while condition:
    block
nếu condition = True thì block sẽ được lặp lại

value = -1
while value < 1 or value > 10:
    value=int(input("Nhập giá trị [1...10]"))
"""
# print("nhập một số trong [1...10]")
# x = -1
# while x < 1 or x > 10:
#     x = int(input("Nhập [1..10]"))
# print(x**2)

#s = 1+2+3+...+n
print("Nhập N:")
n = int(input())
s = 0
i=1
while i <= n:
    s = s + i
    i += 1
print("Tổng =",s)
