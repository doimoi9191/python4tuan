# cau 1: có bao nhiêu dấu * được in ra màn hình
a=0
while a<100:
    print('*',end='')
print()

# câu 2 có bao nhiêu dấu * được in trên màn hình
a=0
while a<100:
    b=0
    while b<40:
        if (a+b)%2==0:
            print('*',end='')
        b+=1
    print()
    a+=1

# câu 3 giải thích cách chạy các dòng lệnh range
range(5)
range(5,10)
range(5,20,3)
range(20,5,-1)
# cau 4 boa nhiêu dấu # đc in ra màn hình
for a in range(20,100,5):
    print('*',end='')
print()
# bai 5 viet lai coding duoi day bnag cach su dung tu khoa break thay the cho bien done
done = False
n,m = 0,100
while not done and n!= m:
    n=int(input())
    if n<0:
        done = True
    print("n= ",n)

# bai 6 vẽ các hình dưới đây

# ****
# *  *
# *  *
# ****
#
#
#     *
#    **
#   ***
#  ****
#
#
# *
# **
# *  *
# *******
#     * *
#      **
#       *

# bài 7 nhập x,n tính S(x,n)
# S(x,n) = x + x^3/3! + x^5/5! + ...+ x^(2n+1)/(2n+1)!