import numpy as np
from io import StringIO  

def Floyd(matrix):
    mat=[ row[:] for row in matrix]
    col=len(mat[0])
    row=len(mat)
    for k in range(max(col,row)):
        for c in range(col):
            for r in range(row):
                mat[c][r]=min(mat[c][r], mat[c][k]+mat[k][r])
    return mat

matran1=[]
matran2=[]

def nhap():
    r=int(input("Nhập số hàng của ma trận: "))
    c=int(input("Nhập số cột của ma trận: "))
    for i in range(r):
        hang=list(map(float,input(f"Hàng {i+1}: ").split()))
        if len(hang)!=c:
            print("Dữ liệu đã bị sai")
            hang=list(map(float,input(f"Hàng {i+1}: ").split()))
        matran1.append(hang)
    print("Ma trận vừa nhập:")
    for row in matran1:
        print(row)

def read_csv():
    print("Dán dữ liệu CSV vào đây (xong thì Enter 2 lần):")
    global matran1  # (SỬA 2) gán vào biến global

    lines = []
    while True:
        line = input()
        if line == "":  # Enter 2 lần để kết thúc
            break
        lines.append(line)

    data = "\n".join(lines)  
    matran1 = np.loadtxt(StringIO(data), delimiter=',')
    for row in matran1:
        print(row)

o=int(input("Bạn muốn nhập tay(1) hay nhập CSV(2)?   "))
if o==1:
    nhap()
elif o==2:
    read_csv()

matran2=Floyd(matran1)

print("Mat trận khoảng cách tối ưu là:")
for row in matran2: 
    print(row)
