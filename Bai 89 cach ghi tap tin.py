"""
dung hàm
open('myfile.txt','w') - mở tập tin để ghi mới

open('myfile.txt','a' - mở tập tin ghi nối đuôi
"""

def luuFile():
    file=open('sinhvien.txt','w',encoding='utf-8')
    file.writelines("sv01;Chuc;9.5\n")
    file.writelines("sv02;Mung;9.9\n")
    file.writelines("sv03;Nam;10\n")
    file.writelines("sv04;Moi;5.9\n")
    file.close()
luuFile()