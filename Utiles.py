import numpy as np

def generar_matriz(arr):
    matriz = [[1 if num == 0 else 0] for num in arr]
    return matriz


def sumaproducto(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")

    # Realizar la multiplicación de matrices usando numpy.dot()
    resultado = np.dot(matriz1, matriz2)

    # Sumar todos los elementos de la matriz resultante para obtener un solo número entero
    resultado_entero = int(np.sum(resultado))

    return resultado_entero


def productoEscalar2Matrices(A , B):
    n_columnas = A.shape[1]
    productos = []
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
    return productos

def productoEscalar3Matrices(A , B, C):
    n_columnas = A.shape[1]
    productos = []
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        columna_matriz_3 = C[:, i]
        producto_escalar = np.sum(columna_matriz_1 * columna_matriz_2 * columna_matriz_3)
        productos.append(producto_escalar)
    return productos