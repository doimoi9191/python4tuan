"""
continue là từ khóa đặc biệt để nhảy sớm đến lần lặp kế tiếp
các lệnh dưới continue sẽ ko dc thực thi
- gặp break thì vòng lặp ngừng luôn
- gặp continue thì chỉ dừng lần lặp hiện tại đang dở để chuyển qua lần lặp tiếp theo
vd tính tổng số lẻ từ 1->15, ngoại trừ 3 và 11
sum = 0
for n in range(1,16,2):
    if n is 3 or n is 11:
        continue
    sum +=n
print(sum)
"""
n=15
s=0
for x in range(1,n+1,2):
    if x is 3 or x is 11:
        continue
    s=s+x
print("s = ",s)
# 1+5+7+9+13+15