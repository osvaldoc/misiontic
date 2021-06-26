import numpy as np
from math import sqrt
from math import modf
#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 



"""Fin espacio para programar funciones propias"""

def solucion(A):
    """
    En esta función deberás programar tu solución.
    Explicación del parámetro que recibe:
    - A: Es una matriz cuadrada de números enteros aleatoria (NO TE DEBES PREOCUPAR POR LLENARLA, YA LO ESTÁ), 
        para indexar un elemento en la fila i, columna j se hace así:
        A[i,j] o A[i][j], como te sientas más cómod@.
        El orden de la matriz lo puedes calcular así: n = A.shape[0]
        
    Explicación de lo que debe retornar:
    -n_cuadrados_perfectos: Número de cuadrados perfectos que aparece en la matriz A, es de tipo float o entero (Elige el tipo que quieras).
    -cuadrados_perfectos: Lista de números cuadrados perfectos que hay en la matriz A, es de tipo float o entero (Elige el tipo que quieras).
    
    """
    
    n_cuadrados_perfectos = 0
    cuadrados_perfectos = []
    n = A.shape[0]
    
    for i in range (0, n-1):
        for j in range (0, n-1):
            r = sqrt(A[i,j])
            P_decimal, P_entera = modf(r)
            
            if P_decimal == 0:
                n_cuadrados_perfectos += 1
                cuadrados_perfectos.append(A[i,j])
    
    return n_cuadrados_perfectos, cuadrados_perfectos



"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
"""
#NO MODIFICAR
matriz_entrada = np.array([[ 758, 1379, 5033, 1044, 6453, 1355,  835, 3974,  267],
       [2280, 4049, 3880, 4424, 2826, 8965, 2902, 8168, 5085],
       [6994, 7538, 8387, 8246, 9272, 2918,  326, 2866, 8901],
       [6365, 2559, 5586, 6925, 5588, 4530, 1237, 7636,  410],
       [7604, 3548, 4280,  906, 7948, 5854, 4709, 6591, 4029],
       [7415, 1921, 6378, 3876, 5696, 2827, 2776, 9835, 5677],
       [9691,  708, 6742, 7338, 8281, 1006, 2921, 6517,  931],
       [2663, 2807, 6840, 3125, 4676, 2507, 5831, 2381, 1438],
       [3803, 6343, 1428, 7690, 1583, 1350, 7930, 1268, 8064]])

n_cuadrados_perfectos_correcto = 1
cuadrados_perfectos_correcto = [8281]

n_cuadrados_perfectos_estudiante = solucion(matriz_entrada)[0]
cuadrados_perfectos_estudiante = solucion(matriz_entrada)[1]


print("MATRIZ ENTREGADA:\n", matriz_entrada,"\n")
print(f"""===SALIDA ESPERADA===
        El número de cuadrados perfectos que hay en la matriz dada es = {n_cuadrados_perfectos_correcto}
        Los cuadrados perfectos que hay en la matriz son = {cuadrados_perfectos_correcto}""")

print(f"""===TU SALIDA===
        El número de cuadrados perfectos que hay en la matriz dada es = {n_cuadrados_perfectos_estudiante}
        Los cuadrados perfectos que hay en la matriz son = {cuadrados_perfectos_estudiante}\n""")

if n_cuadrados_perfectos_correcto == n_cuadrados_perfectos_estudiante and set(cuadrados_perfectos_correcto) == set(cuadrados_perfectos_estudiante):
    print("Todo se ve correcto, ¡Procede a calificar tu código!")
else:
    print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")