# python cung cấp cách thức khai báo một hàm như sau
#
# def name (parameter list):
#     block

def ptb1(a,b):
    if a is 0 and b is 0:
        return "Vô số nghiệm"
    elif a==0 and b!= 0:
        return "Vô nghiệm"
    else:
        return "x={0}".format(-b/a)
def xuatdulieu(data):
    print(data)

kq=ptb1(0,0)
kq2=ptb1(0,1)
kq3=ptb1(6,7)

xuatdulieu(kq)
xuatdulieu(kq2)
xuatdulieu(kq3)