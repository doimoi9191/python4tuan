from random import randrange

lst=[]
print("Nhap so phan tu: ")
n=int(input())
for i in range(n):
    lst.append(randrange(0,100))
print("list sau khi tao ngau nhien la: ")
print(lst)
x=int(input("moi ban chen them so moi: "))
lst.append(x)
print(lst)

k=int(input("moi nhap so de xoa: "))
while lst.count(k) >0:
    lst.remove(k)
print("list sau khi xoa: ")
print(lst)

def CheckDoiXung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst)-i-1]:
            return False
    return True
kt=CheckDoiXung(lst)
if kt==True:
    print("list doi xung")
else:
    print("list ko doi xung")
