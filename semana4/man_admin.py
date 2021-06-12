# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 20:38:58 2021

@author: Osvaldo
"""
from administrativo import Administrativo

#Si definimos algunos parametros no obligatorio 
#en el constructor, debemos indicar el nombre de parametro que corresponde  
#en asignacion, ya funcionaria en desorden
adm1 = Administrativo(edad=55,
                      apellido="Lopez",
                      cargo="Gerente",
                      nombre="Sebastian")
print(adm1.mostrar_nombre_completo())