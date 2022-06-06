# Integrantes: Oliver Pineda y Tarek Thomas
# Cédulas: 8-978-694 y 8-970-510
# Grupo: 1SF131

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#Función que resuelve la ecuación usando el valor brindado para x 
def func(eq,x):
    resp = eval(eq, {"x": x})
    return resp

#Función que resuelve la derivada usando el valor brindado para x 
def derivFunc(derivada,x):
    resp = eval(derivada, {"x": x})
    return resp

#Función para obtener la raíz con el método númerico elegido
def newtonRaphson( x ):
    h = func(eq,x) / derivFunc(derivada,x)
    print(h)
    while abs(h) >= 0.0001:
        h = func(eq,x)/derivFunc(derivada,x)
         
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
     
    print("El valor de la raíz es: : ",
                             "%.4f"% x)

#Programa principal
#Se ingresa la ecuación a utilizar y se muestra al usuario
potencia = int(input("Ingresa el mayor exponente en la ecuación: "))
while potencia <= 0:
    print("La cantidad debe ser positiva")
    potencia = int(input("Ingresa el mayor exponente en la ecuación: "))
eq = ""
for i in reversed(range (potencia + 1)):
    num = float(input("Ingresa el coeficiente de x^" + str(i) + ": "))
    if i == 0:
        eq = eq + "(" + str(num) + "*x**" + str(i) + ")"
    else:
        eq = eq + "(" + str(num) + "*x**" + str(i) + ") + "
print("La ecuación a utilizar es: " + eq)
print("Observe la gráfica y elija 1 punto cercano a la unión de la gráfica con el eje x")

#Se calcula la derivada de la ecuación
derivada=str(sp.diff(eq))

#Se diseña la gráfica para la ecuación ingresada
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

#Se solicita el punto inicial para hacer los cálculos
x = float(input("Ingresa un punto cercano a la unión de la gráfica con el eje x: "))

#Se ejecuta el método
newtonRaphson(x)