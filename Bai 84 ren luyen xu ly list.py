from random import randrange

print("Chuong trinh xu ly list")
n=int(input("Nhap so phan tu: "))
lst=[0]*n
for i in range(n):
    lst[i]=randrange(-100,100)
print("List ngau nhien la:")
print(lst)
print("Moi ban them so moi: ")
value=int(input())
lst.append(value)
print(lst)
print("Ban muon dem so nao: ")
k=int(input())
dem=lst.count(k)
print(k,"xuat hien ",dem,"lan trong list")
def CheckPrime(n):
    d=0
    for i in range(1,n):
        if n%i==0:
            d+=1
        return dem==2
demnt=0
tongnt=0
for x in lst:
    if CheckPrime(x):
        demnt+=1
        tongnt+=x
print("Co ",demnt," so nguyen to trong list")
print("Tong= ",tongnt)
lst.sort()
print("list sau khi sort: ")
print(lst)
del lst
print("list sau khi xoa")
print(lst)