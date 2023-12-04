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

def misma_cantidad_filas(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    filas_matriz2 = len(matriz2)
    
    return filas_matriz1 == filas_matriz2

def evaluarPrimeraRestriccion(Xij,Zik):
    num_filas = Xij.shape[0]
    # Variable para verificar si se encontró alguna suma distinta de 1
    correcto = True
    # Realizar la suma de cada fila de A con la respectiva fila de B
    for i in range(num_filas):
        suma_fila = np.sum(Xij[i]) + np.sum(Zik[i])
        if suma_fila != 1:
            correcto = False
            break
    return correcto

def evaluarSegundaRestriccion(A, B):
    num_filas_A, num_columnas_A = A.shape
    # Variable para verificar si se cumple la condición
    condicion_cumplida = True
    # Verificar si la suma de las columnas de A es igual a 0 y las filas correspondientes de B también son 0
    for i in range(num_columnas_A):
        suma_columna_A = np.sum(A[:, i])
        suma_fila_B = np.sum(B[i])
        if suma_columna_A == 0:
           if suma_fila_B != 0:
             condicion_cumplida = False
        if suma_columna_A !=0:
           if suma_fila_B == 1:
             condicion_cumplida = True
            
    return condicion_cumplida