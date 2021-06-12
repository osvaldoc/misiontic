# -*- coding: utf-8 -*-
"""
Created on Fri May 28 19:25:04 2021

@author: Osvaldo
"""

a = 16
b = True
c = 4
d = 8
e = 5
# (1) a > c = True
# (2) e <= d = True
# (1) -> True and (2) -> True
resultado= a > c and e <= d
#print(resultado)

# (d - e) == 3
# (a / c) == 4
# 3 > 4 = False 
# True or False
resultado2= b or (d - e) > a / c
#print(resultado2)

resultado3 = not b
#print(resultado3)

#pensar o analizar bien esta expresion
resultado4= not b and c < d or a / d <= e
print(resultado4)

#Python sensible a los espacios o tabuladores
#a = 5
#      a = 5

