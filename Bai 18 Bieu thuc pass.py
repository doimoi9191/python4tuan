"""
Biểu thức pass dùng để dành chỗ lập trình.
Ví dụ bạn biết chỗ đó phải viết nhiều mã nhưng tại thời điểm này chưa làm kịp
ta sẽ dung pass để đánh dấu vị trí đó


"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a==0:
    pass#ta sẽ làm sau, đang mót ị gần chết
else:
    x = -b/a
    print("Nghiệm x=",-b/a)