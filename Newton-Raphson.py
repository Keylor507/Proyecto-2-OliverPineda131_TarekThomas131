# Integrantes: Oliver Pineda y Tarek Thomas
# Cédulas: 8-978-694 y 8-970-510
# Grupo: 1SF131

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2
def func(eq,x):
    resp = eval(eq, {"x": x})
    return resp

# Derivative of the above function
# which is 3*x^x - 2*x
def derivFunc(derivada,x):
    resp = eval(derivada, {"x": x})
    return resp

# Function to find the root
def newtonRaphson( x ):
    h = func(eq,x) / derivFunc(derivada,x)
    print(h)
    while abs(h) >= 0.0001:
        h = func(eq,x)/derivFunc(derivada,x)
         
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
     
    print("The value of the root is : ",
                             "%.4f"% x)

potencia = int(input("Ingresa el mayor exponente en la ecuación: "))
eq = ""
for i in reversed(range (potencia + 1)):
    num = float(input("Ingresa el coeficiente de x^" + str(i) + ": "))
    if i == 0:
        eq = eq + "(" + str(num) + "*x**" + str(i) + ")"
    else:
        eq = eq + "(" + str(num) + "*x**" + str(i) + ") + "

derivada=str(sp.diff(eq))

xlist = np.linspace(-10, 10,num=1000)
ylist = func(eq, xlist)
plt.figure(dpi=120)
plt.plot(xlist,ylist)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
plt.ylim(-10,10)
plt.show()

# Driver program to test above
x = float(input("Ingresa un punto cercano a la unión de la gráfica con el eje x: "))

newtonRaphson(x)