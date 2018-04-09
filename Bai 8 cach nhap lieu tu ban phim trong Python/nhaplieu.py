# print("mời bạn nhập giá trị:")
s = float(input("Mời bạn nhập giá trị: "))
print("bạn nhập= ",s)
print(type(s))

def StrToBool(s):
    return s.lower() in("true", "t","1","yes")
x = input("Moi ban nhap True/False:")
x = StrToBool(x)
print(x)