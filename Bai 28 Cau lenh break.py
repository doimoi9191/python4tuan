"""
Thoát vòng lặp chứa nó trực tiếp
while True:
    block
    break
print("heheh")
"""
# while True:
#     x = int(input("Nhập vào một số: "))
#     print(x," là số chẵn" if x % 2 == 0 else "là số lẻ")
#     hoi=input("Tiếp không thím?(c/k):")
#     if hoi=="k":
#         break;
# print("BYE! Cảm ơn thím đã dùng soft này")

n = int(input("Nhập n: "))
s=0
for x in range(1,n):
    s=s+x
    if s>15:
        break
print("S = ",s)