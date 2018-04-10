# Cau 1 Python hỗ trợ những kiểu dữ liệu cơ bản nào?
# Câu 2 trình bày các loại ghi chú trong python
# Câu 3 trình bày ý nghĩa toán tử /,//,%,**,and,or,is
# câu 4 trình bày một số cách nhập dữ liệu từ bàn phím
# Câu 5 trình bày các loại lỗi khi lập trình và cách bắt lỗi trong python

# Câu 1: kiểu dữ liệu cơ bản là: in, float, boolean
# Câu 2: các loại ghi chú trong python là
# #This would be a comment in Python
"""This would be a multiline comment
in Python that spans several lines and
describes your code, your day, or anything you want it to
…
"""
# Câu 3 ý nghĩa toán tử /,//,%,**,and,or,is
# / có nghĩa là phép chia
# // chia lấy phần nguyên
# % chia lấy phần dư
# ** lũy thừa mũ
# phép toán and

# def and_(a, b):
#     "Same as a & b."
#     return a & b
#
# def is_(a, b):
#     "Same as a is b."
#     return a is b
# def or_(a, b):
#     "Same as a | b."
#     return a | b
#
# # Câu 4 một số cách nhập liệu dữ liệu từ bàn phím
# input()
# input("Mời bạn nhập: ")
# # Câu 5 các loại lỗi khi lập trình và cách bắt lỗi
# - cú pháp
# - logic
# - sai yêu cầu đề bài
# bắt lỗi sd
# try:
#     ...
# except:

# Câu 6
# print('-'*15)
# i1 = 2
# i2 =5
# i3=-3
# d1=2.0
# d2=5.0
# d3=-0.5
#
# print("i1=",i1)
# print("i2=",i2)
# print("i3=",i3)
# print("d1=",d1)
# print("d2=",d2)
# print("d3=",d3)
# print('-'*15)
# print("i1+(i2*i3)=",i1+(i2*i3))
# print("i1*(i2+i3)=",i1*(i2+i3))
# print("i1/(i2+i3)=",i1/(i2+i3))
# print("i1//(i2+i3)=",i1//(i2+i3))
# print("i1/i2+i3=",i1/i2+i3)
# print("i1//i2+i3=",i1//i2+i3)
# print("3+4+5/3=",3+4+5/3)
# print("3+4+5//3=",3+4+5//3)
# print("(3+4+5)/3=",(3+4+5)/3)
# print("(3+4+5)//3=",(3+4+5)//3)
# print("d1+(d2*d3)=",d1+(d2*d3))
# print("d1+d2*d3=",d1+d2*d3)
# print("d1/d2-d3=",d1/d2-d3)
# print("d1/(d2-d3)=",d1/(d2-d3))
# print("d1+d2+d3/3=",d1+d2+d3/3)
# print("(d1+d2+d3)/3=",(d1+d2+d3)/3)
# print("d1+d2+(d3/3)=",d1+d2+(d3/3))
# print("3*(d1+d2)*(d1-d3)=",3*(d1+d2)*(d1-d3))

# Cau 7 viet ngan gon lai cac lenh sau
# x = x + 1 -> x+=1
# x = x/2 -> x/=2
# x = x-1 -> x-=1
# x=x+y  -> x +=y
# x=x-(y+7)
# x=2*x  -> x *= 2
# n=n+2*n

# -=, subtracts a value from variable, setting the variable to the result
# *=, multiplies the variable and a value, making the outcome the variable
# /=, divides the variable by the value, making the outcome the variable
# %=, performs modulus on the variable, with the variable then being set to the result of it
x =3
a = x * 2
x *= 2
print(a)
print(x)
