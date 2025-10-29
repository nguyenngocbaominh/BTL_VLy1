import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t= sp.symbols('t', real="True")
m= sp.symbols('m', positive="True")

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

t0=float(input("Nhập thời điểm t="))

#Gọi biến
speed=sp.N(v_t.subs(t, t0))
L_value=sp.N(L.subs(t, t0))

#Chạy thử
print("Vận tốc của vật tại thời điểm t là :", speed)
print("Momen động lượng của vật tại thời điểm t là :", L_value)
