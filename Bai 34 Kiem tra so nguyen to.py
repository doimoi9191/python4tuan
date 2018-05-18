"""
số nguyên tố là số chỉ có 2 ước số là 1 và chính nó. số 0 ko phải là số nguyên tố
"""

# n=int(input("Nhập 1 số nguyên dương "))
# dem=0
# for i in range (1,n+1):
#     if n % i == 0:
#         dem+=1
# if dem==2:
#     print("Số ",n," là số nguyên tố")
# else:
#     print("Số ",n," không là số nguyên tố")


while True:
    n = int(input("Nhập 1 số nguyên dương "))
    dem = 0
    for i in range(1,n+1):
        if n % i ==0:
            dem += 1
        if dem == 2:
            print(n," là số nguyên tố")
        else:
            print(n," không là số nguyên tố")

        hoi = input("Tiếp không thím?(c/k):")
        if hoi is "k":
            break
print("BYE")