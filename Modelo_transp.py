import pandas as pd
import os
import sys
import numpy as np

def generar_matriz(arr):
    matriz = [[1 if num == 0 else 0] for num in arr]
    return matriz

# Obtiene la ruta del directorio actual
ruta_actual = os.path.dirname(os.path.abspath(sys.argv[0]))

# Nombre del archivo Excel que quieres leer
nombre_archivo = 'modelo.xlsm'  # Reemplaza con el nombre de tu archivo Excel

# Une la ruta del directorio actual con el nombre del archivo Excel
ruta_archivo = os.path.join(ruta_actual, nombre_archivo)

# Lee todas las hojas del archivo Excel en un diccionario
datos_excel = pd.read_excel(ruta_archivo, sheet_name=None)
nuevo_arreglo = []
costo_de_inversion_et = 0  # Costo de Inversión ET
costo_operativo_et = 0  # Costo Operativo ET
tasa_de_material_recuperado = 0  # Tasa de material recuperado
costo_de_venta_de_material_recuperado = 0  # Costo de venta de material recuperado
costo_de_inversion_de_centro_ambiental = 0  # Costo de inversión de Centro Ambiental
costo_operativo_de_centro_ambiental = 0  # Costo operativo de Centro Ambiental	

# Itera a través de las hojas del diccionario y muestra todos los registros de cada hoja
for nombre_hoja, datos in datos_excel.items():
    if nombre_hoja == 'INPUTS_Generales':
       costo_de_inversion_et = datos.iloc[20, 6]
       costo_operativo_et = datos.iloc[21, 6]
       tasa_de_material_recuperado = datos.iloc[22, 6]
       costo_de_venta_de_material_recuperado = datos.iloc[23, 6]
       costo_de_inversion_de_centro_ambiental = datos.iloc[24, 6]
       costo_operativo_de_centro_ambiental = datos.iloc[25, 6]
    
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
        for i, arr in enumerate(numeric_arrays):
             print(f"Array {i + 1}: {arr}")
            # Obtén la longitud del array numeric_values
        n = len(numeric_arrays[0])
        # Genera una matriz cuadrada de tamaño nxn inicializada con ceros
        matrix = np.zeros((n, n))
        matrix = np.tile(numeric_arrays[0], (n, 1))
        print(matrix)
        
        mi_matriz = generar_matriz(numeric_arrays[1])
        print(mi_matriz)
        
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

# Imprimir la matriz
for fila in Xij:
    print(' '.join(map(str, fila)))
    
####### HOLA SOY FELAPIO



    