# Integrantes: Oliver Pineda y Tarek Thomas
# Cédulas: 8-978-694 y 8-970-510
# Grupo: 1SF131

import matplotlib.pyplot as plt
import numpy as np

def func(eq,x):
    resp = eval(eq, {"x": x})
    #ecuacion = float(eq)
    return resp

# Prints root of func(x)
# with error of EPSILON
def bisection(a,b):
 
    if (func(eq, a) * func(eq, b) >= 0):
        print("You have not assumed right a and b\n")
        return
  
    c = a
    #for i in range (MAX_ITER):
    while ((b-a) >= 0.01):
 
        # Find middle point
        c = (a+b)/2
  
        # Check if middle point is root
        if (func(eq, c) == 0.0):
            break
  
        # Decide the side to repeat the steps
        if (func(eq, c)*func(eq, a) < 0):
            b = c
        else:
            a = c
             
    print("The value of root is : ","%.4f"%c)

potencia = int(input("Ingresa el mayor exponente en la ecuación: "))
eq = ""
for i in reversed(range (potencia + 1)):
    num = float(input("Ingresa el coeficiente de x^" + str(i) + ": "))
    if i == 0:
        eq = eq + "(" + str(num) + "*x**" + str(i) + ")"
    else:
        eq = eq + "(" + str(num) + "*x**" + str(i) + ") + "

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

a = float(input("Ingresa un punto por la izquierda de la gráfica: "))
b = float(input("Ingresa un punto por la derecha de la gráfica: "))

bisection(a, b)