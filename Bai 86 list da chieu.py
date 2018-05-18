from random import randrange


def TaoMaTran(m,n):
    D=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(randrange(0,100))
        D.append(row)
    return D
def XuatMatTran(D):
    for row in D:
        for element in row:
            print(element,end='\t')
        print()

def LayDong(r):
    R=D[r]
    return R
def XuatList1Chieu(R):
    for element in R:
        print(element,end='\t')
def LayCot(C):
    C=[]
    for i in range(len(D)):
        C.append(D[i][c])
    return C
def MAX(D):
    max=D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if (max<D[i][j]):
                max=D[i][j]
    return max


print("Nhap so dong: ")
m=int(input())
print("Nhap so cot: ")
n=int(input())
D=TaoMaTran(m,n)
XuatMatTran(D)
print("moi ban nhap dong muon xuat: ")
r=int(input())
XuatList1Chieu(LayDong(r))
print()
print("moi ban nhap cot muon xuat")
c=int(input())
XuatList1Chieu(LayCot(c))
print()
max=MAX(D)
print("So lon nhat trong ma tran=",max)