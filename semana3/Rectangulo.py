# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:46:42 2021

@author: Osvaldo
"""
#Ejemplo: class:Persona 
#Atributos(cedula, nombre, genero, edad)
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
    def base(self):
        return self.base

    def altura(self):
        return self.altura
    
rec=Rectangulo(5, 6)    
print(rec.area())
print(rec.base)
    