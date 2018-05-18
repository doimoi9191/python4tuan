"""
time có nhiều hàm
clock tùy thuộc vào hdh mà cách thức xử lý khác nhau.
với window thì clock trả về số giây khi ta gọi làm clock
start=Clock()
end=Clock()
thời gian thwucj thi = end - start



sleep giúp ta tạm dừng quá trình chạy trong 1 đơn vị thời gian nào đó
thay vì ct chạy 1 mạch, khi gặp sleep nó sẽ tạm dừng lại
"""
from time import *
# print("Mời đồng chí nhập tên: ", end="")
# start_time = clock()
# name=input()
# elapsed = clock() - start_time
# print(name,"it took you",elapsed,"seconds to respond")
for count in range(10,1,-1): # range 10,9,8, ...,0
    print(count) # hiển thị biến count
    sleep(1) # tạm dừng chương trình 1 giây