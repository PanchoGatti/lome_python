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

# Itera a través de las hojas del diccionario y muestra todos los registros de cada hoja
def datos_loc_ets ():
    for nombre_hoja, datos in datos_excel.items():
        
        if nombre_hoja == 'Datos_Loc_ETs':
            rows = datos['Distancia Loc - ETs'].tolist()
            cols = datos.columns[1:].tolist()
            result_matrix = np.zeros((len(rows), len(cols)), dtype=int)

            for i, row_label in enumerate(rows):
                for j, col_label in enumerate(cols):
                    result_matrix[i, j] = datos.at[i, col_label]
            return(result_matrix)