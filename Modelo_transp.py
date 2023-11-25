import pandas as pd
import os
import sys
import numpy as np
from Datos_ETs_CAs import datos_ets_cas
from Datos_Loc_CAs import datos_loc_cas

from Datos_Loc_ETs import datos_loc_ets

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
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
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
print("verctor resultante primer termino: ", vector_resultante)
resultado_multiplicacion = np.dot(vector_resultante, C)
print("DOOOT resultante primer termino: ", resultado_multiplicacion)

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
    [1, 1],
    [1, 1],
    [1, 1],
    [1, 1]
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
    [1, 1],
    [1, 1],
    [1, 1],
    [1, 1]
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



matriz_transpuesta = list(map(list, zip(*Aij)))

Dij = datos_loc_ets()
A = np.array(Xij)
B = np.array(matriz_transpuesta)
C = np.array(Dij)

    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")

elif A.shape != C.shape:
    print("Las matrices no tienen la misma forma")
    
else:
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        columna_matriz_3 = C[:, i]
        producto_escalar = np.sum(columna_matriz_1 * columna_matriz_2 * columna_matriz_3)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    print("\nResultado final del producto escalar entre las columnas:", resultado_final)

septimo_termino = resultado_final*CC
print("Resultado del septimo término:", septimo_termino)

###############################HASTA ACÁ SÉPTIMO TÉRMINO######################


print("EMPIEZXA EL OCTAVOOOOOOOO")

matriz_transpuesta = list(map(list, zip(*Cik)))

Dik = datos_loc_cas()
A = np.array(Zik)
B = np.array(matriz_transpuesta)
C = np.array(Dik)

    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")

elif A.shape != C.shape:
    print("Las matrices no tienen la misma forma")
    
else:
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        columna_matriz_3 = C[:, i]
        producto_escalar = np.sum(columna_matriz_1 * columna_matriz_2 * columna_matriz_3)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    print("\nResultado final del producto escalar entre las columnas:", resultado_final)

octavo_termino = resultado_final*CC
print("Resultado del octavo término:", octavo_termino)

###############################HASTA ACÁ Octqavo TÉRMINO######################

print("EMPIEZXA EL NOVENOOOO")

matriz_transpuesta = list(map(list, zip(*Bjk)))

Djk = datos_ets_cas()
A = np.array(Yjk)
B = np.array(Bjk)
C = np.array(Djk)

print("A ", A ,"B ", B ,"C ", C)

    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")

elif A.shape != C.shape:
    print("Las matrices no tienen la misma forma")
    
else:
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        columna_matriz_3 = C[:, i]
        producto_escalar = np.sum(columna_matriz_1 * columna_matriz_2 * columna_matriz_3)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    print("\nResultado final del producto escalar entre las columnas:", resultado_final)

noveno_termino = resultado_final*TC
print("Resultado del noveno término:", noveno_termino)


###############################HASTA ACÁ noveno TÉRMINO######################

# Mostrar el vector resultante calculado anteriormente, de hacer Xij(A) * Aij(B)
A = np.array(Xij)
B = np.array(list(map(list, zip(*Aij))))
n_columnas = A.shape[1]
productos = []
for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")
resultado_final = sum(productos)
decimo_termino = (resultado_final*(RECj * SPj))

print("Resultado del decimo término:", decimo_termino)

###############################HASTA ACÁ decimo TÉRMINO######################

#print("LA SUMAMAM: ", primer_termino + segundo_termino + tercer_termino + cuarto_termino + quinto_termino + sexto_termino + septimo_termino + octavo_termino + noveno_termino - decimo_termino)



###################################### Comienza la segunda expresión ################

print("Comienzo de la segunda expresión  - Cálculo de camiones")

#Primer término de camiones

Qwc = Vc*Ec*Dc / (1+Rc)
TRcij= (T1c-(T2c+T3c))/((2*Dij/SPDc)+T4c+T5c)

matriz_transpuesta = list(map(list, zip(*Aij)))

A = np.array(matriz_transpuesta)
B = np.array(TRcij)
NCij = A / (Qwc*B)


A = np.array(Xij)
B = np.array(NCij)
n_columnas = A.shape[1]
productos = []
for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")
resultado_final = sum(productos)
primer_termino_segundaexp = (resultado_final)

print("Resultado del primer termino segunda expresión:", primer_termino_segundaexp)

###################################### Hasta acá primer termino segunda exp ################


#Segundo término de camiones

Qwt = Vt*Et*Dt / (1+Rt)
TRtjk= (T1t-(T2t+T3t))/((2*Djk/SPDt)+T4t+T5t)


A = np.array(Bjk)
B = np.array(TRtjk)
NTjk = A / (Qwt*B)


A = np.array(Yjk)
B = np.array(NTjk)
n_columnas = A.shape[1]
productos = []
for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")
resultado_final = sum(productos)
segundo_termino_segundaexp = (resultado_final)

print("Resultado del segundo termino segunda expresión:", segundo_termino_segundaexp)


########################HASTA ACÁ SEGUNDO TÉRMINO DE LA SEGUNDA EXPRESIÓN #################

print("Tercer término de camiones!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


TRcik= (T1c-(T2c+T3c))/((2*Dik/SPDc)+T4c+T5c)
matriz_transpuesta = list(map(list, zip(*Cik)))

A = np.array(matriz_transpuesta)
B = np.array(TRcik)
NCik = A / (Qwc*B)

print(NCik)

A = np.array(Zik)
B = np.array(NCik)
n_columnas = A.shape[1]
productos = []
for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        producto_escalar = np.dot(columna_matriz_1, columna_matriz_2)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")
resultado_final = sum(productos)
tercer_termino_segundaexp = (resultado_final)



#########################SUMA TOTAL DE CAMIONES

print(" La flota total de camiones se constituye por ", primer_termino_segundaexp + tercer_termino_segundaexp , "de camiones recolectores y ", segundo_termino_segundaexp, "de camiones transportadores, dando un total de " , primer_termino_segundaexp + segundo_termino_segundaexp + tercer_termino_segundaexp, "camiones")

print(primer_termino_segundaexp)
print(segundo_termino_segundaexp)
print(tercer_termino_segundaexp)

###################################### Comienza la tercera expresión ################

