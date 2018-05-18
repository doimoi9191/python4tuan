# hàm format sử dụng {} để dành chỗ xuất dữ liệu

a=5
b=9
c=a/b
s="{0}/{1}={2}".format(a,b,c)
print(s)

# hàm substring để trích lọc chuỗi
x="Hello Xuan"
# cắt từ trái sang phải, từ ký tự số 2
print(x[2:])
# cắt từ trái sang phải đến ký tự số 2
print(x[:2])
# cắt từ trái sang phải, đến ký tự -2
print(x[:-2])
# cắt từ phải sang trái, đến ký tự số -2 (ngoài cùng bên phải là -1)
print(x[-2:])

print(x[2:-2])

print(x[6:11])