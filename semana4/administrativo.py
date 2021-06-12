# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 20:31:55 2021

@author: Osvaldo
"""
from empleado import Empleado

#Heredamos de empleado
class Administrativo(Empleado):
    #Definir horas_extras no son obligarias para introduccir
    def __init__(self, 
                 nombre = None, 
                 apellido = None, 
                 edad = 0, 
                 horas_extras = 0, 
                 cargo = None):
        Empleado.__init__(self,nombre, apellido, edad)
        self.horas_extras=horas_extras
        self.cargo = cargo
        
    def calcular_pago_nomina():
        '''Muchas lineas, multiplan,suma, incapacidades'''
        pass
        