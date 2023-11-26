import pandas as pd
import os
import sys
import numpy as np
from Datos_ETs_CAs import datos_ets_cas
from Datos_Loc_CAs import datos_loc_cas

from Datos_Loc_ETs import datos_loc_ets
from Utiles import generar_matriz, productoEscalar2Matrices, productoEscalar3Matrices
from prueba import matriz_iterada

# def generar_matriz(arr):
#     matriz = [[1 if num == 0 else 0] for num in arr]
#     return matriz
# def sumaproducto(matriz1, matriz2):
#     if len(matriz1[0]) != len(matriz2):
#         raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")

#     # Realizar la multiplicación de matrices usando numpy.dot()
#     resultado = np.dot(matriz1, matriz2)

#     # Sumar todos los elementos de la matriz resultante para obtener un solo número entero
#     resultado_entero = int(np.sum(resultado))

#     return resultado_entero

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
Djk = [[]]
Dik = [[]]
Dij = [[]]
Vc = 0 #Capacidad en m3 de camion recolector
Ec = 0 #Eficiencia de carga en % recolector
Dc = 0 #Densidad en tn/m3 de RSU en camion recolector
Rc = 0 #Tasa de reserva de camiones recolectores
T1c = 0 # Horas de trabajo de camion recolector
T2c = 0 # Horas de preparación de camion recolector
T3c = 0 # Horas de limpieza de camion recolector
T4c = 0 # Horas de carga de camion recolector
T5c = 0 # Horas de descarga de camion recolector
SPDc = 0 # Velocidad de camion recolector
Vt = 0 #Capacidad en m3 de camion transportador
Et = 0 #Eficiencia de carga en % transportador
Dt = 0 #Densidad en tn/m3 de RSU en camion transportador
Rt = 0 #Tasa de reserva de camiones transportadores
T1t = 0 # Horas de trabajo de camion transportador
T2t = 0 # Horas de preparación de camion transportador
T3t = 0 # Horas de limpieza de camion transportador
T4t = 0 # Horas de carga de camion transportador
T5t = 0 # Horas de descarga de camion transportador
SPDt = 0 # Velocidad de camion transportador
Uc = 0 # Factor U para recolectores
KPLc = 0 # distancia recorrida en un litro de camiones recolectores km/l
Ut = 0 # Factor U para transportadores
KPLt = 0 # distancia recorrida en un litro de camiones transportadores km/l

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
       Vc = datos.iloc[8,5]
       Ec = datos.iloc[9,5]
       Dc = datos.iloc[12,5]
       Rc = datos.iloc[13,5]
       T1c = datos.iloc[2,5]
       T2c = (datos.iloc[3,5])/60
       T3c = (datos.iloc[4,5])/60
       T4c = datos.iloc[5,5]
       T5c = (datos.iloc[6,5])/60
       SPDc = datos.iloc[7,5]
       Vt = datos.iloc[8,6]
       Et = datos.iloc[9,6]
       Dt = datos.iloc[12,6]
       Rt = datos.iloc[13,6]
       T1t = datos.iloc[2,6]
       T2t = (datos.iloc[3,6])/60
       T3t = (datos.iloc[4,6])/60
       T4t = datos.iloc[5,6]
       T5t = (datos.iloc[6,6])/60
       SPDt = datos.iloc[7,6]
       Uc = datos.iloc[17,5]
       KPLc = datos.iloc[15,5]
       Ut = datos.iloc[17,6]
       KPLt = datos.iloc[15,6]
    
    if nombre_hoja == 'Datos_Loc_ETs':
        Dij = datos_loc_ets(datos)
    
    if nombre_hoja == 'Datos_Loc_CAs':
        Dik = datos_loc_cas(datos)

    if nombre_hoja == 'Datos_ETs_CAs':
        Djk = datos_ets_cas(datos)
        
         
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


Xij_inicial = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
Yjk_inicial = [
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0]
]

Zik_inicial = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
]
matrices_iteradas_Xij = matriz_iterada(Xij_inicial)
matrices_iteradas_Zik = matriz_iterada(Zik_inicial)
matrices_iteradas_Yjk = matriz_iterada(Yjk_inicial)
matriz_optimaXij = Xij_inicial
matriz_optimaZik = Zik_inicial
matriz_optimaYjk = Yjk_inicial
valor_suma_minimo=999999999999999999999999999
for Xij in matrices_iteradas_Xij:
    for Zik in matrices_iteradas_Zik:
        for Yjk in matrices_iteradas_Yjk:
            matriz_transpuesta = list(map(list, zip(*Aij)))
            A = np.array(Xij)
            B = np.array(matriz_transpuesta)
            C = np.array(TSj)
                
                # Verificar si las matrices tienen la misma forma
            if A.shape != B.shape:
                print("Las matrices no tienen la misma forma.")
            else:
                productos = productoEscalar2Matrices(A,B)
                resultado_final = sum(productos)
            vector_resultante = np.array(productos)
            resultado_multiplicacion = np.dot(vector_resultante, C)
            primer_termino = resultado_multiplicacion*INVTSj
            #####HASTA ACÁ LLEGA EL PRIMER TÉRMINO, ARRANCA EL SEGUNDO. SE TOMAN VARIAS VARIABLES YA DEFINIDAS###

            segundo_termino = resultado_final*OPTSj
            #HASTA ACÁ LLEGA EL SEGUNDO TÉRMINO, ARRANCA EL TERCERO. SE TOMAN VARIAS VARIABLES YA DEFINIDAS###
            Bjk = np.tile(vector_resultante, (cantidad_de_ks, 1)).T
            A = np.array(Yjk)
            B = np.array(Bjk)
            C = np.array(Ik)
            # Verificar si las matrices tienen la misma forma
            if A.shape != B.shape:
                print("Las matrices no tienen la misma forma.")
            else:
                productos = productoEscalar2Matrices(A,B)
                resultado_final = sum(productos)
                # Convertir la lista de productos a un arreglo NumPy
            vector_resultante = np.array(productos)
            resultado_multiplicacion = np.dot(vector_resultante, C)
            tercer_termino = resultado_multiplicacion*INVLk
            ######HASTA ACA TERCER TERMINO############

            matriz_transpuesta = list(map(list, zip(*Cik)))
            A = np.array(Zik)
            B = np.array(matriz_transpuesta)
            C = np.array(Ik)

            # Verificar si las matrices tienen la misma forma
            if A.shape != B.shape:
                print("Las matrices no tienen la misma forma.")
            else:
                productos = productoEscalar2Matrices(A,B)
                resultado_final = sum(productos)
                # Convertir la lista de productos a un arreglo NumPy
            vector_resultante = np.array(productos)
            resultado_multiplicacion = np.dot(vector_resultante, C)
            cuarto_termino = resultado_multiplicacion*INVLk

            #################################HASTA ACÁ CUARTO TÉRMINO#############################

            A = np.array(Yjk)
            B = np.array(Bjk)

            # Verificar si las matrices tienen la misma forma
            if A.shape != B.shape:
                print("Las matrices no tienen la misma forma.")
            else:
                productos = productoEscalar2Matrices(A,B)
                resultado_final = sum(productos)
            quinto_termino = resultado_final*OPLk

            ######################HASTA ACÁ QUINTO TÉRMINO###############################
            matriz_transpuesta = list(map(list, zip(*Cik)))
            A = np.array(Zik)
            B = np.array(matriz_transpuesta)
            # Verificar si las matrices tienen la misma forma
            if A.shape != B.shape:
                print("Las matrices no tienen la misma forma.")
            else:
                productos = productoEscalar2Matrices(A,B)
                resultado_final = sum(productos)
            sexto_termino = resultado_final*OPLk

            ###############################HASTA ACÁ SEXTO TÉRMINO######################

            matriz_transpuesta = list(map(list, zip(*Aij)))
            A = np.array(Xij)
            B = np.array(matriz_transpuesta)
            C = np.array(Dij)

            # Verificar si las matrices tienen la misma forma
            if A.shape != B.shape:
                print("Las matrices no tienen la misma forma.")

            elif A.shape != C.shape:
                print("Las matrices no tienen la misma forma")
                
            else:
                productos = productoEscalar3Matrices(A,B,C)
                # Sumar los productos escalares individuales para obtener el resultado final
                resultado_final = sum(productos)
            septimo_termino = resultado_final*CC

            ###############################HASTA ACÁ SÉPTIMO TÉRMINO######################
            matriz_transpuesta = list(map(list, zip(*Cik)))
            A = np.array(Zik)
            B = np.array(matriz_transpuesta)
            C = np.array(Dik)
                # Verificar si las matrices tienen la misma forma
            if A.shape != B.shape:
                print("Las matrices no tienen la misma forma.")

            elif A.shape != C.shape:
                print("Las matrices no tienen la misma forma")
                
            else:
                productos = productos = productoEscalar3Matrices(A,B,C)
                resultado_final = sum(productos)
            octavo_termino = resultado_final*CC

            ###############################HASTA ACÁ Octqavo TÉRMINO######################
            matriz_transpuesta = list(map(list, zip(*Bjk)))

            A = np.array(Yjk)
            B = np.array(Bjk)
            C = np.array(Djk)
                # Verificar si las matrices tienen la misma forma
            if A.shape != B.shape:
                print("Las matrices no tienen la misma forma.")

            elif A.shape != C.shape:
                print("Las matrices no tienen la misma forma")
                
            else:
                productos = productoEscalar3Matrices(A,B,C)
                resultado_final = sum(productos)
            noveno_termino = resultado_final*TC

            ###############################HASTA ACÁ noveno TÉRMINO######################

            # Mostrar el vector resultante calculado anteriormente, de hacer Xij(A) * Aij(B)
            A = np.array(Xij)
            B = np.array(list(map(list, zip(*Aij))))

            productos = productoEscalar2Matrices(A,B)
            resultado_final = sum(productos)
            decimo_termino = (resultado_final*(RECj * SPj))
            ###############################HASTA ACÁ decimo TÉRMINO######################
            sumatotal = (primer_termino + segundo_termino + tercer_termino + cuarto_termino + quinto_termino + sexto_termino + septimo_termino + octavo_termino + noveno_termino - decimo_termino)
            if(sumatotal < valor_suma_minimo):
                valor_suma_minimo = sumatotal
                matriz_optimaXij = Xij
                matriz_optimaZik = Zik
                matriz_optimaYjk = Yjk


print("suma valor minimo" ,valor_suma_minimo)
print("Optima Xij", Xij)
print("Optima Zik", Zik)
print("Optima Yjk", Yjk)


    
  

 ############# EMPIEzA ULTIMA WEA########################
 #    