# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:54:14 2021

@author: Osvaldo
"""

#Factorial de un numero
#5! = 5x4x3x2x1


#9! = 1*2*3*4*5*6*7*8*9
num = 5
mult = 1
for i in range (1, num + 1 ):
    mult = mult * i
print(mult)


#9! = 9x8x7x6x5x4x3x2x1
#decremento -1
num = 5
mult = 1
for i in range (num , 0, -1  ):
    mult = mult * i
print(mult)

