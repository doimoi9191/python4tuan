"""
for expression:
    for-block
else:
    else-block
nếu vòng for kết thúc bình thường (ko dùng lệnh break) thì sẽ chạy else-block
"""
a=int(input("nhập a:"))
s=0
for n in range(5,10):
    if 4%a is 1:
        print("Ngừng for")
        break
    s=s+n
else:
    print("Sum ",s)