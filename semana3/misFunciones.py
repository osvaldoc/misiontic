# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:17:03 2021

@author: Osvaldo
"""
import math
import random


def esPrimo (n):
  if n % 2 == 0: #Si un numero es par, no es primo
      return False
  i = 3
  while i <= math.sqrt(n):
     if n % i == 0:
       return False
     i = i + 2
  return True


def comienzaCon(x):
    pd = x
    while pd > 9:
        pd = pd // 10
    return pd

def mcd (x,y):
    res = x % y
    while res != 0:
       x = y
       y = res
       res = x % y
    return y

#Funcion puede llamar a otra funcion o a ella misma
#funciona llama a si misma se llama RECURSIVIDAD
def mcm (x, y):
    return x * y // mcd (x,y)

