# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:12:27 2021

@author: Osvaldo
"""
from empleado import Empleado

#Herencia??
#Motivo: evitar tener que volver a escribir dichos métodos, no duplicar info
#Lo que esta entre parentesis es lo que voy a heredar, todo lo que esta en la 
#clase (en este caso Empleado), tambien lo va a tener Operario
class Operario(Empleado):
    def __init__(self, nombre, apellido, edad, talla_uniforme):
        Empleado.__init__(self,nombre,apellido,edad)
        self.talla_uniforme = talla_uniforme
  