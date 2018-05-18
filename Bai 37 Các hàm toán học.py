from math import *
x=5
y=7
print(pow(x,y))
print(x**y)
print(sqrt(25))
do = 30
print("30=>",radians(do))
rad=radians(do)
print("chuyen tu radian ve do",degrees(rad))
print("log10(100)=",log10(100))

print("moi thym nhap vao mot goc:")
goc=float(input())
sinx = sin(radians(goc))
cosx = cos(radians(goc))
tanx = tan(radians(goc))
cotanx = 1/tanx

print("sin({0})={1}".format(goc,sinx))
print("cos({0})={1}".format(goc,cosx))
print("tan({0})={1}".format(goc,tanx))
print("cotan({0})={1}".format(goc,cotanx))