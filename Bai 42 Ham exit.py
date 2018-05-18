"""
hàm để thoát hẳn phần mềm # hẳn lệnh break

"""
while True:
    print("nhập 1 số:")
    n=int(input())
    dem=0
    for i in range(1,n+1):
        if n%i==0:
            dem+=1
    if(dem is 2):
        print(n,"là số nguyên tố")
    else:
        print(n,"không là số nguyên tố")
    print("Tiếp không?(c/k):")
    if(input()=="k"):
        exit()
print("Biến")