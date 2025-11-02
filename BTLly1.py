import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

# === HÀM CHUẨN HÓA BIỂU THỨC NGƯỜI DÙNG NHẬP ===
def chuan_hoa_bieu_thuc(expr: str) -> str:
    expr = expr.lower().strip()
    expr = expr.replace("^", "**")       # t^2 → t**2
    expr = expr.replace("e**", "exp(")   # e^t → exp(t)
    expr = expr.replace("ln(", "log(")   # ln(t) → log(t)
    expr = expr.replace("lnt", "log(t)") # lnt → log(t)
    return expr

# === KHAI BÁO BIẾN ===
t = sp.Symbol('t', real=True)

# === HƯỚNG DẪN NHẬP ===
print("""
📘 HƯỚNG DẪN NHẬP HÀM:
---------------------------------
e^t        → exp(t)
ln(t)      → log(t)
t^2        → t**2
sqrt(t)    → sqrt(t)
sin(t)     → sin(t)
cos(t)     → cos(t)
π          → pi
---------------------------------
""")

# === NHẬP BIỂU THỨC ===
print("Nhập biểu thức x(t), y(t):")
x_inp = chuan_hoa_bieu_thuc(input(" \tx(t) = "))
y_inp = chuan_hoa_bieu_thuc(input(" \ty(t) = "))

print("Nhập khối lượng (kg) của vật:")
m = float(input(" \tm = "))

# === PHÂN TÍCH BIỂU THỨC ===
local_dict = {'t': t, 'exp': sp.exp, 'log': sp.log,
               'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
               'sqrt': sp.sqrt, 'pi': sp.pi}

x_t = parse_expr(x_inp, local_dict=local_dict)
y_t = parse_expr(y_inp, local_dict=local_dict)

# === TÍNH ĐẠO HÀM ===
vx_t = sp.diff(x_t, t)
vy_t = sp.diff(y_t, t)

# === CÔNG THỨC MOMEN ĐỘNG LƯỢNG VÀ VẬN TỐC ===
L = sp.simplify(m * (x_t * vy_t - y_t * vx_t))
v_t = sp.simplify(sp.sqrt(vx_t**2 + vy_t**2))

# === CHUYỂN THÀNH HÀM SỐ (NUMPY) ===
x_num = sp.lambdify(t, x_t, 'numpy')
y_num = sp.lambdify(t, y_t, 'numpy')
L_num = sp.lambdify(t, L, 'numpy')

# === NHẬP THỜI GIAN ===
print("Nhập khoảng thời gian khảo sát chuyển động của vật:")
t0 = float(input("\tt0 = "))
t1 = float(input("\tt1 = "))

print("Nhập thời điểm cần tính vận tốc và momen động lượng:")
T0 = float(input("\tT = "))

# === TÍNH TOÁN GIÁ TRỊ ===
T = np.linspace(t0, t1, 400)
X = x_num(T)
Y = y_num(T)
L1 = np.ravel(L_num(T))   # làm phẳng mảng để khớp kích thước

# === TÍNH GIÁ TRỊ TẠI THỜI ĐIỂM T0 ===
speed = float(v_t.subs(t, T0))
L_value = float(L.subs(t, T0))

# === IN KẾT QUẢ RA MÀN HÌNH ===
print(f"\n Vận tốc của vật tại t = {T0:.2f} s là: {speed:.4f} m/s")
print(f" Momen động lượng tại t = {T0:.2f} s là: {L_value:.4f} kg·m²/s\n")

# === VẼ QUỸ ĐẠO CHUYỂN ĐỘNG ===

# --- Đồ thị gốc ---
plt.figure(figsize=(6,5))
plt.plot(X, Y, label='Quỹ đạo chuyển động', color='blue')
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.title("Quỹ đạo chuyển động của vật")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()

# --- Đồ thị chuẩn hóa & loại bỏ phần t < 0 ---
mask = T >= 0
T_pos = T[mask]
X_pos = X[mask]
Y_pos = Y[mask]

# --- CHUẨN HÓA DƯƠNG (min–max) ---
X_scaled = (X_pos - np.min(X_pos)) / (np.max(X_pos) - np.min(X_pos))
Y_scaled = (Y_pos - np.min(Y_pos)) / (np.max(Y_pos) - np.min(Y_pos))

# --- Vẽ đồ thị chuẩn hóa ---
plt.figure(figsize=(6, 5))
plt.plot(X_scaled, Y_scaled, color='orange', label='Quỹ đạo chuẩn hóa (t ≥ 0, dương)')
plt.xlabel("x(t) (đã chuẩn hóa)")
plt.ylabel("y(t) (đã chuẩn hóa)")
plt.title("Quỹ đạo chuyển động (đã chuẩn hóa dương, t ≥ 0)")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

# === VẼ ĐỒ THỊ MOMEN ĐỘNG LƯỢNG THEO THỜI GIAN ===
plt.figure()
plt.plot(T, L1)
plt.xlabel("t (s)")
plt.ylabel("Momen động lượng (kg·m²/s)")
plt.title("Biến thiên Momen động lượng theo thời gian")
plt.grid(True)
plt.show()

