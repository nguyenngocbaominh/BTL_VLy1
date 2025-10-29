import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t= sp.symbols('t', real=True)
m= sp.symbols('m', positive=True)

print("Nhập biểu thức x(t), y(t):")
x_inp=input(" \tx(t)=")
y_inp=input(" \ty(t)=")
print("Nhập khối lượng(kg) của vật :")
m=float(input(" \tm="))

x_t=sp.sympify(x_inp , locals={'t':t})
y_t=sp.sympify(y_inp , locals={'t':t})

vx_t=sp.diff(x_t , t)
vy_t=sp.diff(y_t , t)
#Khai hàm
L=sp.simplify(m*(x_t*vy_t-y_t*vx_t))
v_t=sp.simplify(sp.sqrt(vx_t*vx_t+vy_t*vy_t))


x_num = sp.lambdify(t, x_t, 'numpy')
y_num = sp.lambdify(t, y_t, 'numpy')
L_num = sp.lambdify(t, L , 'numpy')

print("Nhập khoảng thời gian khảo sát chuyển động của vật:")
t0=float(input("\tt0="))
t1=float(input("\tt1="))
print("Nhập thời gian cần tính vận tốc, momen động lượng:")
T0=float(input("\tT="))

T = np.linspace(t0, t1, 400)
X = x_num(T)
Y = y_num(T)
L1 = L_num(T)


#Gọi biến
speed=sp.N(v_t.subs(t, T0))
L_value=sp.N(L.subs(t, T0))

#Chạy thử
print("Vận tốc của vật tại thời điểm t là :", speed)
print("Momen động lượng của vật tại thời điểm t là :", L_value)

plt.figure()
plt.plot(X, Y)
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.title("Quỹ đạo chuyển động")
plt.axis('equal')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(T, L1)
plt.xlabel("t(s)")
plt.ylabel("Momen động lượng")
plt.title("Biến thiên Momen đlượng theo thời gian")
plt.grid(True)
plt.show()

