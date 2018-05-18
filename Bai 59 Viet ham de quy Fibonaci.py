"""
1-1-2-3-5-8-...

Nếu n = 1,n=2 -> fn = 1
Nếu n > 2 -> fn = fn-1 + fn-2
"""

def FIBO(n):
    if n <= 2:
        return 1
    return FIBO(n-1)+FIBO(n-2)


def listFibo(n):
    for i in range(1,n+1):
        print(FIBO(i),end='\t')

print(FIBO(6))
listFibo(6)