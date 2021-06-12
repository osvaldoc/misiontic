# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:12:27 2021

@author: Osvaldo
"""
#Esto es un objeto, es una clase, tiene atributos, tiene miles, 
#solo tenemos nombre, apellido, edad
class Empleado:
    #contructor, el que inicializa una clase
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def mostrar_nombre_completo(self):
        ''' metodo para mostrar nombre completo'''
        return self.nombre + " " + self.apellido
    
    def es_mayor_edad(self):
        ''' Este metodo devuelve un verdadero si es mayor de edad'''
        if self.edad >=18:
            return True
        else:
            return False
        
    def se_aproxima_pension(self):
        if self.edad >= 60:
            return True
        else:
            return False