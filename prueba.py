    
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
    