"""
tính S(x,n) = x + x^2/2! + x^3/3! + ... + x^n/n!
"""
x=int(input("nhập x:"))
n=int(input("nhập n:"))
s=0
for i in range(1,n+1):
    tu=x**i
    mau=1
    for j in range(1,i+1):
        mau=mau*j
    s=s+tu/mau
print("kết quả:",s)