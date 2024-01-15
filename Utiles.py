import numpy as np

def generar_matriz(arr):
    matriz = [[1 if num == 0 else 0] for num in arr]
    return matriz

def generar_matriz_nueva(arr):
    matriz = [[9999 if num == 0 else num] for num in arr]
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
    productos = np.sum(A * B, axis=0)
    return productos

def productoEscalar3Matrices(A , B, C):
    productos = np.sum(A * B * C, axis=0)
    return productos

def productoEscalar4Matrices(A , B, C,D):
    productos = np.sum(A * B * C * D, axis=0)
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
    n = len(A)  # Número de filas de A
    m = len(B[0])  # Número de columnas de B

    for i in range(n):
        suma_columna_A = sum([fila[i] for fila in A])  # Suma de la columna i de A
        suma_fila_B = sum(B[i])  # Suma de la fila i de B
        
        if suma_columna_A != 0:
            if suma_fila_B == 1:
                continue
            else:
                return False
        else:
            if suma_fila_B == 0:
                continue
            else:
                return False

    return True

def evaluarTerceraRestriccion(A, B):
    n = len(A)  # Número de filas de A
    m = len(B[0])  # Número de columnas de B

    for i in range(n):
        suma_columna_A = sum([fila[i] for fila in A])  # Suma de la columna i de A
        suma_fila_B = sum(B[i])  # Suma de la fila i de B
        
        if suma_columna_A <= suma_fila_B :
            continue
        else:
                return False
    return True

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

def generarNuevoBjK(A, C):

    nueva_fila = len(C)
    nueva_columna = len(C[0])

    # Sumar cada columna de la matriz A
    sumas_columnas = np.sum(A, axis=0)

    # Crear la matriz B con las dimensiones de la matriz C
    filas, columnas = nueva_fila, nueva_columna
    B = np.zeros((filas, columnas))  # Crear una matriz B con las dimensiones obtenidas de C

    for i in range(filas):
        B[i, :] = sumas_columnas[i % len(sumas_columnas)]  # Repetir el valor de la suma de la columna i en la fila i de la matriz B
    return B * C

def calcular_termino_producto_escalar2(A, B, CC):
    productos = productoEscalar2Matrices(A, B)
    resultado_final = sum(productos)
    return resultado_final * CC

def calcular_termino_producto_escalar3(A, B, C, coeficiente):
    productos = productoEscalar3Matrices(A, B, C)
    resultado_final = sum(productos)
    return resultado_final * coeficiente

def funcion_ci_ca(x):
    return 34545*x+9*(10**6)
    
def funcion_co_ca(x):
    return 2012.4*(x**(-0.865))

def funcion_ci_et(x,quiebre_et1y2):
    if x < quiebre_et1y2:
        return (0.034*x + 5*(10**(-8)))*1000000
    else:
        return (0.0101*x + 2.5749)*1000000
    
def funcion_co_et(x):
    return 691.43*(x**(-0.83))