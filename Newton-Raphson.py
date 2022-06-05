# Integrantes: Oliver Pineda y Tarek Thomas
# Cédulas: 8-978-694 y 8-970-510
# Grupo: 1SF131

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

'''
def f(x,a,b,c):
    return a*x**2+b*x+c

xlist = np.linspace(-10, 10,num=20)
ylist = f(xlist,3,1,4)

'''

def f(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d

xlist = np.linspace(-10, 10,num=20)
ylist = f(xlist,1,0,-2,-5)

plt.figure(dpi=120)
plt.plot(xlist,ylist)
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')
plt.ylim(-10,10)
plt.show()