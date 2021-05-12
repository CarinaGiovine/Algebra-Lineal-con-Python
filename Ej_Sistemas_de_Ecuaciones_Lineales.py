# -*- coding: utf-8 -*-
"""
Created on Tue May 11 22:20:57 2021

@author: Carina Giovine
"""

#Sistemas de ecuaciones lineales

import sympy as sm

x=sm.Symbol("x")
y=sm.Symbol("y")
z=sm.Symbol("z")
a=sm.solve([3*x - 2*y - 4, 5*x + 2* y - 12],[x,y])   #las rectas se intersectan en un punto
print(a)

b=sm.solve([x - y - 7 , 2*x - 2*y -14],[x,y])
print(b)  #esta ecuacion tiene un nro infinito de soluciones. 

c= sm.solve([x + y - 3, x + 2*y + 8], [x,y])  #ejercicio 1 del libro de Algebre pag 6
print(c)

d=sm.solve([2*x + 3*y - 3, -2*x -3*y + 3],[x,y])  #ejercicio 2
print(d)

e=sm.solve([3*x - 7*y + 5 , 4*x - 3*y + 2],[x,y])  #ejercicio 6
print(e)

f=sm.solve([x - y - 7, 2*x - 2*y - 13],[x,y])    #sistema que no tiene solucion, porque no se verifica.Las rectas son paralelas y distintas
print(f)

g=sm.solve ([2*x + 4*y + 6*z - 18, 4*x + 5*y + 6*z - 24, 3*x + y - 2*z - 4],[x,y,z])  #sistema con 3 incógnitas, unica solución
print(g)

h=sm.solve([2*x + 4*y + 6*z -18, 4*x + 5*y + 6*z -24, 2*x + 7*y + 12*z - 30],[x,y,z])  #nro infinito de soluciones
print(h)

i=sm.solve([2*y + 3*z - 4, 2*x - 6*y + 7*z -15, x - 2*y + 5*z -10],[x,y,z])
print(i)  # este sistema no tiene solución. En este caso se dice que el sistema es inconsistente
'''
Se dice que un sistema de ecuaciones lineales es inconsistente si no tiene solución. 
Se dice que un sistema que tiene al menos una solución es consistente.
'''


#from sympy import *

#Se define las variables simbolicas x,y,z

x = sm.Symbol('x')
y = sm.Symbol('y')
z= sm.Symbol('z')

#Resolver el sistema de ecuaciones
#3x+9y-10z  =   24
#x-6y+4z      =   -4
#10x-2y+8z  =  20

resultado =sm.solve([3*x+9*y-10*z-24,x-6*y+4*z+4,10*x-2*y+8*z-20],[x,y,z])

print (resultado)

