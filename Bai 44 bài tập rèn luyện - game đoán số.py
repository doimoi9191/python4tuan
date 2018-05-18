"""
ôn tập về số ngẫu nhiên và các vòng lặp
máy ra 1 số trong đoạn [1...100]
người chơi đoán số, chỉ dc phép sai 7 lần
mỗi lần đoán sẽ thông báo số người chơi đoán nhỏ hơn hay lớn hơn số của máy và hiển thị số lần đoán
game kết thúc khi: đoán sai quá 7 lần hoặc đoán đúng trước 7 lần
sau khi kết thúc game sẽ hỏi người chơi có muốn chơi tiếp hay ko
"""
from random import *
while True:
    solandoan=0
    somay=randrange(1,101)
    win=False

    while solandoan < 7:
        solandoan +=1
        songuoi=int(input("Máy đoán [1..100], mời bạn đoán:"))
        print("Bạn đoán lần thứ: ",solandoan)
        if somay == songuoi:
            print("Chúc mừng bạn đoán đúng, số máy là=",somay)
            win=True
            break
        if somay > songuoi:
            print("Bạn đóa sai, số máy > số bạn")
        elif somay < songuoi:
            print("bạn đoán sai, số máy < số bạn")
    if win == False:
        print("GAME ÂU VỜ",somay)
    hoi=input("Tiếp chứ?")
    if hoi == "k":
        break
print("Cám ơn bạn đã chơi gêm")