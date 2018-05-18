s='sv007;nguyễn duy xuân;19/07/1991'
arr=s.split(';')
for x in arr:
    print(x)

s1="""
    cuộc đời là
        bể khổ
            còn lâu!
"""
a=s1.splitlines()
for line in a:
    print(line,"a->",line.count('a'))

s2="""
    sv01;nguyễn thị hạnh;1/2/2991
    sv02;trần trùng trục;1/1/1990
    sv03;hồ văn an;2/3/1998
    sv04;lý tòng tòe;5/6/2008    
"""
arrSv=s2.splitlines()
for line in arrSv:
    arrInfo = line.strip().split(';')
    print(len(arrInfo))
    if len(arrInfo) ==3:
        print(arrInfo)