"""
trong python có 1 chút rắc rối khi so sánh số thức
đó là có sai số
người dùng phải quyết định theo ngưỡng sai số cho phép là bao nhiêu

ta phải tạo 1 ngưỡng sai số
"""
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print('d1 =',d1,'d2 =',d2)
diff = d1 - d2
if diff < 0:
    diff = -diff
if diff < 0.0000001:
    print("SAME")
else:
    print("DIFFERENT")