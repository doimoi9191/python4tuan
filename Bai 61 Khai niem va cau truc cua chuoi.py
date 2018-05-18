"""
    Chuỗi là tập các ký tự nằm trong nháy đơn hoặc nháy đôi, hoặc 3 nháy đơn hoặc 3 nháy đôi.
    Chuỗi rất quan trọng trong mọi ngôn ngữ, hầu hết ta đều gặp xử lý chuỗi
"""

s1 = 'Hê lô ABC'
s2 = "Bê nhô"
s3 = """
    Quanh năm buôn bán ở mom sông
    Nuôi đủ năm con với một chồng
    Lặn lội thân cò khi quãng vắng
    Eo sèo mặt nước buổi đò đông
"""
s4 = '''
    Cha mẹ thói đời ăn ở bạc
    có chồng hờ hững cũng như không
'''

print(s1)
print(s2)
print(s3)
print(s4)

"""
upper, lower
rjust - can le phai
ljust - can le trai
center - can le giua
"""
# w = "ABCD"
# print(w.rjust(10, "*"))
# print(w.rjust(3, "*"))
# print(w.rjust(15, ">"))
# print(w.rjust(10))
# print(w.ljust(1))
# print(w.ljust(2))
# print(w.ljust(3))
# print(w.ljust(4))
# print(w.ljust(5))
# print(w.ljust(10))
# print(w.ljust(10,'*'))
# print(w.center(10))
# print(w.center(10))
# print(w.center(10,'*'))
# print(w.center(21,'*'))

"""
Xoa khoang cach du thua: trip
"""
s1 = "  hello con cho obama"
print(s1,len(s1))
s2=s1.strip()
print(s2,len(s2))

s = "## ##JOHN###"
s=s.strip('#')
print(s)