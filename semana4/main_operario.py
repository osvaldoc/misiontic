# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 20:08:32 2021

@author: Osvaldo
"""
from operario import Operario
ope1=Operario("Felipe", "Galvez", 25, "M")
print(ope1.mostrar_nombre_completo() + " - " + ope1.talla_uniforme)

ope2=Operario("Luisa", "Gomez", 17, "S")
print(ope2.nombre)
print(ope2.es_mayor_edad())

