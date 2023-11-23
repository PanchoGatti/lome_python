import pandas as pd
import os
import sys
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

# Obtiene la ruta del directorio actual
ruta_actual = os.path.dirname(os.path.abspath(sys.argv[0]))

# Nombre del archivo Excel que quieres leer
nombre_archivo = 'modelo.xlsm'  # Reemplaza con el nombre de tu archivo Excel

# Une la ruta del directorio actual con el nombre del archivo Excel
ruta_archivo = os.path.join(ruta_actual, nombre_archivo)

# Lee todas las hojas del archivo Excel en un diccionario
datos_excel = pd.read_excel(ruta_archivo, sheet_name=None)
nuevo_arreglo = []
INVTSj = 0  # Costo de Inversión ET
OPTSj = 0  # Costo Operativo ET
RECj = 0  # Tasa de material recuperado
SPj = 0  # Costo de venta de material recuperado
INVLk = 0  # Costo de inversión de Centro Ambiental
OPLk = 0  # Costo operativo de Centro Ambiental	
cantidad_de_ks = 0 # Cantidad de Centros ambientales definidos en la celda G31
CC = 0 # Costo de transporte de camiones recolectores
TC = 0 # Costo de transporte de camiones de transferencia

# Itera a través de las hojas del diccionario y muestra todos los registros de cada hoja
for nombre_hoja, datos in datos_excel.items():
    if nombre_hoja == 'INPUTS_Generales':
       INVTSj = datos.iloc[20, 6]
       OPTSj = datos.iloc[21, 6]
       RECj = datos.iloc[22, 6]
       SPj = datos.iloc[23, 6]
       INVLk = datos.iloc[24, 6]
       OPLk = datos.iloc[25, 6]
       cantidad_de_ks = datos.iloc[29,6]
       CC = datos.iloc[14,5]
       TC = datos.iloc[14,6]
    
    if nombre_hoja == 'Gen-Cap':
        data = pd.DataFrame(datos)
        values_list = data.values.flatten().tolist()
        numeric_arrays = []
        current_numeric_array = []
        for val in values_list:
            if val == '[t/d]':
                if current_numeric_array:
                    numeric_arrays.append([x for x in current_numeric_array if not np.isnan(x)])
                    current_numeric_array = []
            elif isinstance(val, (int, float)):
                current_numeric_array.append(val)

        # Añadir el último array numérico si existe después de la última aparición de '[t/d]'
        if current_numeric_array:
            numeric_arrays.append([x for x in current_numeric_array if not np.isnan(x)])

        # Imprimir los arrays numéricos
        # for i, arr in enumerate(numeric_arrays):
        #      print(f"Array {i + 1}: {arr}")
            # Obtén la longitud del array numeric_values
        n = len(numeric_arrays[0])
        # Genera una matriz cuadrada de tamaño nxn inicializada con ceros
        Aij = np.zeros((n, n))
        Aij = np.tile(numeric_arrays[0], (n, 1))
        # print(Aij)
        
        TSj = generar_matriz(numeric_arrays[1])
        Ik = generar_matriz(numeric_arrays[2])
        
        m = len(numeric_arrays[2])
        Cik = np.zeros((n,m))
        Cik = np.tile(numeric_arrays[0], (m,1))
        
       
        
        # while values_list and (pd.isnull(values_list[0]) or isinstance(values_list[0], str)):
        #         values_list.pop(0)
        # numeric_values = []
        # for x in values_list:
        #     if isinstance(x, (int, float)):
        #         numeric_values.append(x)
        #     elif isinstance(x, str) or pd.isnull(x):
        #         break
        # while numeric_values and (pd.isnull(numeric_values[-1]) or isinstance(numeric_values[-1], str)):
        #         numeric_values.pop()
##########################################################################################Hasta acá hizo tino#########################
Xij = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
# # Ejemplo de uso:
matriz_transpuesta = list(map(list, zip(*Aij)))
# print(Xij[0][0])
# print(matriz_transpuesta[0][0])
# resultado = sumaproducto(Xij, matriz_transpuesta)
# print(resultado)


A = np.array(Xij)

B = np.array(matriz_transpuesta)

C = np.array(TSj)

# Calcular el producto escalar
producto_escalar = np.sum(A * B* C)

print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)
print("\nMatriz C:")
print(C)
print("\nEl producto escalar de las matrices A y B es:", producto_escalar)

###################################################### HASTA ACA HIZO TINO 22/11 17HS###################3
# Obtener el número de columnas de la matriz
num_filasA, num_columnasA = A.shape

# Iterar sobre cada columna
for i in range(num_columnasA):
    columna_actualA = A[:, i]
    #print(f"Columna {i + 1}: {columna_actualA}")
    
    # Obtener el número de columnas de la matriz
num_filasB, num_columnasB = B.shape

# Iterar sobre cada columna
for i in range(num_columnasB):
    columna_actualB = B[:, i]
    #print(f"Columna {i + 1}: {columna_actualB}")
    
    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")
else:
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    print("\nResultado final del producto escalar entre las columnas:", resultado_final)
    
    # Convertir la lista de productos a un arreglo NumPy
vector_resultante = np.array(productos)

# Mostrar el vector resultante
print("Vector resultante:", vector_resultante)

# Multiplicación escalar entre los dos vectores
resultado_multiplicacion = np.dot(vector_resultante, C)

primer_termino = resultado_multiplicacion*INVTSj
print("Resultado del primer término:", primer_termino)


#####HASTA ACÁ LLEGA EL PRIMER TÉRMINO, ARRANCA EL SEGUNDO. SE TOMAN VARIAS VARIABLES YA DEFINIDAS###

# Mostrar el vector resultante calculado anteriormente, de hacer Xij(A) * Aij(B)
print("Resultado final (Escalar entre Xij y Aij):", resultado_final)

segundo_termino = resultado_final*OPTSj

print("Resultado del segundo término:", segundo_termino)

#HASTA ACÁ LLEGA EL SEGUNDO TÉRMINO, ARRANCA EL TERCERO. SE TOMAN VARIAS VARIABLES YA DEFINIDAS###


matriz_resultante = np.tile(vector_resultante, (cantidad_de_ks, 1)).T

Bjk = matriz_resultante

# Mostrar la matriz resultante
print("Matriz resultante BJK:")
print(Bjk)

Yjk = [
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0]
]

A = np.array(Yjk)

B = np.array(Bjk)

C = np.array(Ik)

# Obtener el número de columnas de la matriz
num_filasA, num_columnasA = A.shape

# Iterar sobre cada columna
for i in range(num_columnasA):
    columna_actualA = A[:, i]
    #print(f"Columna {i + 1}: {columna_actualA}")
    
    # Obtener el número de columnas de la matriz
num_filasB, num_columnasB = B.shape

# Iterar sobre cada columna
for i in range(num_columnasB):
    columna_actualB = B[:, i]
    #print(f"Columna {i + 1}: {columna_actualB}")
    
    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")
else:
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    print("\nResultado final del producto escalar entre las columnas:", resultado_final)
    
    # Convertir la lista de productos a un arreglo NumPy
vector_resultante = np.array(productos)

# Mostrar el vector resultante
print("Vector resultante:", vector_resultante)

# Multiplicación escalar entre los dos vectores
resultado_multiplicacion = np.dot(vector_resultante, C)

# Mostrar el resultado de la multiplicación escalar
print("Resultado de la multiplicación escalar:", resultado_multiplicacion)

tercer_termino = resultado_multiplicacion*INVLk
print("Resultado del tercer término:", tercer_termino)

######HASTA ACA TERCER TERMINO############

matriz_transpuesta = list(map(list, zip(*Cik)))

Zik = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
]

A = np.array(Zik)
B = np.array(matriz_transpuesta)
C = np.array(Ik)

# Obtener el número de columnas de la matriz
num_filasA, num_columnasA = A.shape

# Iterar sobre cada columna
for i in range(num_columnasA):
    columna_actualA = A[:, i]
    #print(f"Columna {i + 1}: {columna_actualA}")
    
    # Obtener el número de columnas de la matriz
num_filasB, num_columnasB = B.shape

# Iterar sobre cada columna
for i in range(num_columnasB):
    columna_actualB = B[:, i]
    #print(f"Columna {i + 1}: {columna_actualB}")
    
    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")
else:
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    print("\nResultado final del producto escalar entre las columnas:", resultado_final)
    
    # Convertir la lista de productos a un arreglo NumPy
vector_resultante = np.array(productos)

# Mostrar el vector resultante
print("Vector resultante:", vector_resultante)

# Multiplicación escalar entre los dos vectores
resultado_multiplicacion = np.dot(vector_resultante, C)

# Mostrar el resultado de la multiplicación escalar
print("Resultado de la multiplicación escalar:", resultado_multiplicacion)

cuarto_termino = resultado_multiplicacion*INVLk
print("Resultado del cuarto término:", cuarto_termino)


#################################HASTA ACÁ CUARTO TÉRMINO#############################

A = np.array(Yjk)

B = np.array(Bjk)

# Obtener el número de columnas de la matriz
num_filasA, num_columnasA = A.shape

# Iterar sobre cada columna
for i in range(num_columnasA):
    columna_actualA = A[:, i]
    #print(f"Columna {i + 1}: {columna_actualA}")
    
    # Obtener el número de columnas de la matriz
num_filasB, num_columnasB = B.shape

# Iterar sobre cada columna
for i in range(num_columnasB):
    columna_actualB = B[:, i]
    #print(f"Columna {i + 1}: {columna_actualB}")
    
    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")
else:
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    print("\nResultado final del producto escalar entre las columnas:", resultado_final)
    
  
quinto_termino = resultado_final*OPLk
print("Resultado del quinto término:", quinto_termino)

######################HASTA ACÁ QUINTO TÉRMINO###############################
matriz_transpuesta = list(map(list, zip(*Cik)))

A = np.array(Zik)
B = np.array(matriz_transpuesta)

# Obtener el número de columnas de la matriz
num_filasA, num_columnasA = A.shape

# Iterar sobre cada columna
for i in range(num_columnasA):
    columna_actualA = A[:, i]
    #print(f"Columna {i + 1}: {columna_actualA}")
    
    # Obtener el número de columnas de la matriz
num_filasB, num_columnasB = B.shape

# Iterar sobre cada columna
for i in range(num_columnasB):
    columna_actualB = B[:, i]
    #print(f"Columna {i + 1}: {columna_actualB}")
    
    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")
else:
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    print("\nResultado final del producto escalar entre las columnas:", resultado_final)
    
  
sexto_termino = resultado_final*OPLk
print("Resultado del sexto término:", sexto_termino)


###############################HASTA ACÁ SEXTO TÉRMINO######################


