"""
chuỗi tối ưu = ko thừa space bên trái, bên phải; ở giữa cách nhau 1 space
"""
def ToiUuChuoi(s):
    s2=s
    s2=s2.strip()
    arr=s2.split(' ')
    s2=""
    for x in arr:
        word = x
        if len(word.strip()) !=0:
            s2=s2+word+" "
    return s2.strip()



s="      Trần Lý                Lê           "
print(s,"=>",len(s))
s=ToiUuChuoi(s)
print(s,"=>",len(s))