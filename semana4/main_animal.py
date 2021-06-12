# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:59:35 2021

@author: Osvaldo
"""
from animal import Animal

animal1 = Animal("Cerdo", "Mamifero",4, False)
animal2 = Animal("Gallina", "Hervivoro",2, False)
animal3 = Animal("Tigre", "Carnivoro",4, True)

print(animal3.nombre_comun, animal3.peligrosidad)