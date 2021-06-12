# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:25:29 2021

@author: Osvaldo
"""
from empleado import Empleado

empl1=Empleado("juan","perez", 48)
empl2=Empleado("maria","lopez", 24)

print("Nombre :",empl1.nombre)
print("Nombre completo :",empl1.mostrar_nombre_completo())
print("Es mayor edad: ",empl1.es_mayor_edad())
print("Pension :",empl1.se_aproxima_pension())