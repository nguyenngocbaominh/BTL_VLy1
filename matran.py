def pivot_index(row, eps=1e-12):#đếm số số không trước tham số cơ sở
    for j, x in enumerate(row):
        if abs(x) > eps:
            return j
    return len(row) 
def sort_rows(mat, eps=1e-12):#sắp xếp lại ma trận
    mat.sort(key=lambda r: pivot_index(r, eps))
    return mat
def det(matrix):
    n=len(matrix)
    det=1
    for i in range(n):
        det=det*matrix[i][i]
    return det

def biendoi(matrix):
    """ Biến đổi ma trận về dạng bậc thang """
    n = len(matrix)
    m = len(matrix[0])
    mat = [row[:] for row in matrix]  #tạo acc clone cho ma trận gốc
    row = 0
    for col in range(m):
        if row >= n:
            break
        mat=sort_rows(mat)

        # Nếu vẫn 0 thì bỏ qua cột này
        if mat[row][col] == 0:
            continue
        # Xử lí các hàng dưới
        for r in range(row + 1, n):
            if mat[r][col] != 0:
                factor = mat[r][col] / mat[row][col]
                mat[r] = [a - factor * b for a, b in zip(mat[r], mat[row])]
        row += 1
    return mat
matran1=[]
r=int(input("Nhập số hàng của ma trận: "))
c=int(input("Nhập số cột của ma trận: "))
for i in range(r):
    hang=list(map(float,input(f"Hàng {i+1}: ").split()))
    if len(hang)!=c:
        print("Nhập sai rồi kìa má")
        hang=list(map(float,input(f"Hàng {i+1}: ").split()))
    matran1.append(hang)
print("Ma trận vừa nhập:")
for row in matran1:
    print(row)
matran2=biendoi(matran1)
print("Ma trận dạng bậc thang:")
for row in matran2:
    print(row)
if len(matran1)!=len(matran1[0]):
    print("Không có định thức!!!")
else:
    det1=det(biendoi(matran1))
    print(f"Định thức của ma trận vừa nhập là {det1}")
