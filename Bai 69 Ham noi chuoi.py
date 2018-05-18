"hàm join dùng để nối chuỗi"

s='sv007;lý văn tèo; 1/1/2009'
ar = s.split(';')
for x in ar:
    print(x)
s2=","
s2=s2.join(ar)
print(s2)