"""
vẽ chữ N dùng vòng for lồng nhau
"""
n = int(input("Nhập chiều cao: "))
# print("Vẽ chữ N")
# for i in range(n):
#     for j in range(n):
#         if i==j or j==0 or j==n-1:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()
# """
# Vẽ tam giác dùng vòng for lồng nhau
# """
# print("Vẽ tam giác")
# for i in range(n):
#     for j in range(n):
#         if i==j or j==0 or i==n-1:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()
"""
Vẽ chữ N dùng vòng while lồng nhau
"""
print("#"*30)
i=0
while i<n:
    j=0
    while j<n:
        if j == 0 or i == j or j == n-1:
            print("#",end='')
        else:
            print(" ",end='')
        j+=1
    i+=1
    print()