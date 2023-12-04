    
from itertools import product
import numpy as np


def generar_combinaciones(matriz, i, j, m, n, combinaciones):
    if i == m:
        combinaciones.append([fila[:] for fila in matriz])
        return

    for k in range(2):
        matriz[i][j] = k
        if j + 1 < n:
            generar_combinaciones(matriz, i, j + 1, m, n, combinaciones)
        else:
            generar_combinaciones(matriz, i + 1, 0, m, n, combinaciones)


def matriz_iterada(Xij):
    matriz_dimensiones = Xij
    filas = len(matriz_dimensiones)
    columnas = len(matriz_dimensiones[0])

    # Inicializar una matriz de dimensiones mxn con ceros
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Lista para almacenar las matrices con combinaciones binarias
    matrices_combinadas = []

    # Generar todas las combinaciones binarias posibles
    generar_combinaciones(matriz, 0, 0, filas, columnas, matrices_combinadas)

    return  matrices_combinadas

def generarMatrizYjk():
    A = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
    ]
    all_B_variants = []
    for i in range(A.shape[1]):  # Iterar sobre todas las columnas de A
        suma_columna = np.sum(A[:, i])  # Calcular la suma de la columna i de A
        possible_B_variants = []

    for combination in product([0, 1], repeat=A.shape[0]):  # Generar todas las combinaciones de 0 y 1 para la fila i de B
        if np.sum(combination) == suma_columna:
            possible_B_variants.append(list(combination))
    all_B_variants.append(possible_B_variants)
    print("la wea fome", all_B_variants)


    