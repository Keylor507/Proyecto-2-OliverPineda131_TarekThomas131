# Integrantes: Oliver Pineda y Tarek Thomas
# Cédulas: 8-978-694 y 8-970-510
# Grupo: 1SF131

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

MAX_ITER = 20

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
    i = 0
    while True:
        h = func(eq,x)/derivFunc(derivada,x)
         
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

        # Se imprime el resultado de cada iteración acorde a si se puede calcular error relativo o no
        if i >= 1:
            error = abs((x-xAnt)/x)*100
            print("Iteración {:d}: Raíz = {:.4f}; Error = {:.4f}%".format(i, x, error))
            if error < 1 or i == MAX_ITER:  #Se establecen las condiciones para detener la ejecución
                break
        else:
            print("Iteración {:d}: Raíz = {:.4f}".format(i, x))
        
        # Se imprime un mensaje en caso de llegar a la máxima iteración permitida
        if i == MAX_ITER:
            print("Se alcanzó la máxima cantidad de iteraciones permitidas ({:d})".format(MAX_ITER))

        xAnt = x
        i = i + 1
     
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