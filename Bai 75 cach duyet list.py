"""
co 2 cách duyệt list
1. duyệt theo collection
2. duyệt theo chỉ số index
"""
print("*"*35)
ls=[1,5,657,8,89,9,6,7,98]
for x in ls:
    print(x,end='\t')
print()
print("*"*35)

for i in range(len(ls)):
    x=ls[i]
    print(x,end='\t')
print()
print("*"*35)
for i in range(len(ls)-1,-1,-1):
    x=ls[i]
    print(x,end='\t')