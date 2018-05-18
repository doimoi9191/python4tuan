lst = [
    [4,2,10],
    [7,10,5],
    [-7,9,2]
]
print(lst)
for row in lst:
    for colum in row:
        print(colum,end='\t')
    print()
print("*"*20)
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j],end='\t')
    print()