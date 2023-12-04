import pandas as pd
import os
import sys
import numpy as np

from Utiles import generar_matriz_nueva


Zik = [
    [1, 1],
    [1, 1],
    [1, 1],
    [1, 1]
]

Yjk = [
    [1, 0],
    [1, 1],
    [1, 0],
    [1, 0]
]
Cik = [
        [120,  85, 160, 170],
        [120,  85, 160, 170]
    ]

BJK =[
        [0, 0],
        [0, 0],
        [160, 160],
        [170, 170]
    ]
Ejepmlo= [1800,1800]


def evaluarCuartaRestriccion(A, B):
    n = len(B)  # Número de filas de B
    m = len(B[0])  # Número de columnas de B

    for i in range(n):
        suma_columna_A = sum(A[i])  # Suma de la fila i de A
        suma_fila_B = sum(B[i])  # Suma de la fila i de B

        if suma_columna_A <= suma_fila_B:
            continue
        else:
            return False
    return True


matriz_transpuesta_cik = list(map(list, zip(*Cik)))
A = ((np.array(Yjk) * np.array(BJK)) +  (np.array(Zik)  * np.array(matriz_transpuesta_cik)))
print(A)
B = generar_matriz_nueva(Ejepmlo)
print(B)
print(evaluarCuartaRestriccion(A,B))