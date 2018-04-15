"""
python hỗ trợ else block trong th while kết thúc một cách bình thường
- tức là ko dùng beak để kết thúc

while condition:
    while block
else:
    else block
nếu while kết thúc 1 cách bt thì else-block sẽ tự động dc thực hiện ngay sau đó.
"""
count = sum = 0
print("Nhập danh sách các số dương để tính trung bình")
while count < 5:
    val = float(input('Nhập số: '))
    if val < 0:
        print("Số 0 sai quy tắc, thoát phần mềm")
        break
    count += 1
    sum += val
else:
    print('Trung bình = ',sum/count)