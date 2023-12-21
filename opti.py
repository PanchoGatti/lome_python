import pandas as pd
import os
import sys
import numpy as np
from Datos_ETs_CAs import datos_ets_cas
from Datos_Loc_CAs import datos_loc_cas

from Datos_Loc_ETs import datos_loc_ets
from Utiles import calcular_termino_producto_escalar2, calcular_termino_producto_escalar3, evaluarCuartaRestriccion, evaluarPrimeraRestriccion, evaluarSegundaRestriccion, evaluarTerceraRestriccion, generar_matriz, generar_matriz_nueva, generarNuevoBjK, productoEscalar2Matrices, productoEscalar3Matrices, productoEscalar4Matrices
from prueba import matriz_iterada
from datetime import datetime

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
hoja_INPUTS_Generales = datos_excel.get('INPUTS_Generales')
hoja_Datos_Loc_ETs = datos_excel.get('Datos_Loc_ETs')
hoja_Datos_Loc_CAs = datos_excel.get('Datos_Loc_CAs')
hoja_Datos_ETs_CAs = datos_excel.get('Datos_ETs_CAs')
hoja_Gen_Cap = datos_excel.get('Gen-Cap')

if hoja_INPUTS_Generales is not None:
    INVTSj = hoja_INPUTS_Generales.iloc[20, 6]
    OPTSj = hoja_INPUTS_Generales.iloc[21, 6]
    RECj = hoja_INPUTS_Generales.iloc[22, 6]
    SPj = hoja_INPUTS_Generales.iloc[23, 6]
    INVLk = hoja_INPUTS_Generales.iloc[24, 6]
    OPLk = hoja_INPUTS_Generales.iloc[25, 6]
    cantidad_de_ks = hoja_INPUTS_Generales.iloc[29,6]
    CC = hoja_INPUTS_Generales.iloc[14,5]
    TC = hoja_INPUTS_Generales.iloc[14,6]
    Vc = hoja_INPUTS_Generales.iloc[8,5]
    Ec = hoja_INPUTS_Generales.iloc[9,5]
    Dc = hoja_INPUTS_Generales.iloc[12,5]
    Rc = hoja_INPUTS_Generales.iloc[13,5]
    T1c = hoja_INPUTS_Generales.iloc[2,5]
    T2c = (hoja_INPUTS_Generales.iloc[3,5])/60
    T3c = (hoja_INPUTS_Generales.iloc[4,5])/60
    T4c = hoja_INPUTS_Generales.iloc[5,5]
    T5c = (hoja_INPUTS_Generales.iloc[6,5])/60
    SPDc = hoja_INPUTS_Generales.iloc[7,5]
    Vt = hoja_INPUTS_Generales.iloc[8,6]
    Et = hoja_INPUTS_Generales.iloc[9,6]
    Dt = hoja_INPUTS_Generales.iloc[12,6]
    Rt = hoja_INPUTS_Generales.iloc[13,6]
    T1t = hoja_INPUTS_Generales.iloc[2,6]
    T2t = (hoja_INPUTS_Generales.iloc[3,6])/60
    T3t = (hoja_INPUTS_Generales.iloc[4,6])/60
    T4t = hoja_INPUTS_Generales.iloc[5,6]
    T5t = (hoja_INPUTS_Generales.iloc[6,6])/60
    SPDt = hoja_INPUTS_Generales.iloc[7,6]
    Uc = hoja_INPUTS_Generales.iloc[17,5]
    KPLc = hoja_INPUTS_Generales.iloc[15,5]
    Ut = hoja_INPUTS_Generales.iloc[17,6]
    KPLt = hoja_INPUTS_Generales.iloc[15,6]

if hoja_Datos_Loc_ETs is not None:
    Dij = datos_loc_ets(hoja_Datos_Loc_ETs)

if hoja_Datos_Loc_CAs is not None:
    Dik = datos_loc_cas(hoja_Datos_Loc_CAs)

if hoja_Datos_ETs_CAs is not None:
    Djk = datos_ets_cas(hoja_Datos_ETs_CAs)

if hoja_Gen_Cap is not None:
    data = pd.DataFrame(hoja_Gen_Cap)
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

    # Obtén la longitud del array numeric_values
    n = len(numeric_arrays[0])
    # Genera una matriz cuadrada de tamaño nxn inicializada con ceros
    Aij = np.zeros((n, n))
    Aij = np.tile(numeric_arrays[0], (n, 1))
    TSj = generar_matriz(numeric_arrays[1])
    Ik = generar_matriz(numeric_arrays[2])
    m = len(numeric_arrays[2])
    Cik = np.zeros((n,m))
    Cik = np.tile(numeric_arrays[0], (m,1))
        


matrices_iteradas_Xij = matriz_iterada(Dij)
matrices_iteradas_Zik = matriz_iterada(Dik)
matrices_iteradas_Yjk = matriz_iterada(Djk)
matriz_optimaXij = Dij
matriz_optimaZik = Dik
matriz_optimaYjk = Djk
vector_termino_primero=[]
valor_suma_minimo=999999999999999999999999999
hora_actual = datetime.now()
print("La hora actual es:", hora_actual)
for Xij in matrices_iteradas_Xij:
    for Zik in matrices_iteradas_Zik:
        for Yjk in matrices_iteradas_Yjk:
            if(evaluarPrimeraRestriccion(np.array(Xij),np.array(Zik))):
                if(evaluarSegundaRestriccion (Xij,Yjk)):
                    matriz_transpuesta = list(map(list, zip(*Aij)))
                    A = np.array(Xij)
                    B = np.array(matriz_transpuesta)
                    C = np.array(TSj)
                    D = np.array(Xij) * np.array(matriz_transpuesta)
                    E = generar_matriz_nueva(numeric_arrays[1])
                    if(evaluarTerceraRestriccion(D,E)):
                            # Verificar si las matrices tienen la misma forma
                        if A.shape != B.shape:
                            print("Las matrices no tienen la misma forma.")
                        # else:
                        #     productos = productoEscalar2Matrices(A,B)
                        #     resultado_final = sum(productos)
                        productos = productoEscalar2Matrices(A,B)
                        vector_resultante = np.array(productos)
                        vector_termino_primero = vector_resultante
                        resultado_multiplicacion = np.dot(vector_resultante, C)
                        primer_termino = resultado_multiplicacion*INVTSj
                        #####HASTA ACÁ LLEGA EL PRIMER TÉRMINO, ARRANCA EL SEGUNDO. SE TOMAN VARIAS VARIABLES YA DEFINIDAS###

                        segundo_termino = sum(productos) * OPTSj
                        #HASTA ACÁ LLEGA EL SEGUNDO TÉRMINO, ARRANCA EL TERCERO. SE TOMAN VARIAS VARIABLES YA DEFINIDAS###
                        Bjk = (np.tile(vector_resultante, (cantidad_de_ks, 1)).T) * (1- RECj)
                        matriz_transpuesta_cik = list(map(list, zip(*Cik)))
                        D = ((np.array(Yjk) * np.array(Bjk)) +  (np.array(Zik)  * np.array(matriz_transpuesta_cik)))
                        E = generar_matriz_nueva(numeric_arrays[2])
                        if(evaluarCuartaRestriccion(D,E)):
                            A = np.array(Yjk)
                            B = np.array(Bjk)
                            C = np.array(Ik)
                            # Verificar si las matrices tienen la misma forma
                            if A.shape != B.shape:
                                print("Las matrices no tienen la misma forma.")
                            # else:
                            #     productos = productoEscalar2Matrices(A,B)
                            #     resultado_final = sum(productos)
                                # Convertir la lista de productos a un arreglo NumPy
                            productos = productoEscalar2Matrices(A,B)
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
                            # else:
                            #     productos = productoEscalar2Matrices(A,B)
                            #     resultado_final = sum(productos)
                                # Convertir la lista de productos a un arreglo NumPy
                            productos = productoEscalar2Matrices(A,B)
                            vector_resultante = np.array(productos)
                            resultado_multiplicacion = np.dot(vector_resultante, C)
                            cuarto_termino = resultado_multiplicacion*INVLk

                            #################################HASTA ACÁ CUARTO TÉRMINO#############################

                            A = np.array(Yjk)
                            B = np.array(Bjk)

                            # Verificar si las matrices tienen la misma forma
                            if A.shape != B.shape:
                                print("Las matrices no tienen la misma forma.")
                            
                            quinto_termino = calcular_termino_producto_escalar2(A,B,OPLk)

                            ######################HASTA ACÁ QUINTO TÉRMINO###############################
                            matriz_transpuesta = list(map(list, zip(*Cik)))
                            A = np.array(Zik)
                            B = np.array(matriz_transpuesta)
                            # Verificar si las matrices tienen la misma forma
                            if A.shape != B.shape:
                                print("Las matrices no tienen la misma forma.")
                            
                            sexto_termino = calcular_termino_producto_escalar2(A,B,OPLk)

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
                                
                            septimo_termino = calcular_termino_producto_escalar3(A,B,C,CC)

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
                                
                            # else:
                            #     productos = productos = productoEscalar3Matrices(A,B,C)
                            #     resultado_final = sum(productos)
                            octavo_termino = calcular_termino_producto_escalar3(A,B,C,CC)

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
                         
                            noveno_termino = calcular_termino_producto_escalar3(A,B,C,TC)

                            ###############################HASTA ACÁ noveno TÉRMINO######################

                            # Mostrar el vector resultante calculado anteriormente, de hacer Xij(A) * Aij(B)
                            A = np.array(Xij)
                            B = np.array(list(map(list, zip(*Aij))))

                            decimo_termino = calcular_termino_producto_escalar2(A,B,(RECj * SPj))
                            ###############################HASTA ACÁ decimo TÉRMINO######################
                            sumatotal = (primer_termino + segundo_termino + tercer_termino + cuarto_termino + quinto_termino  + sexto_termino + septimo_termino + octavo_termino + noveno_termino - decimo_termino)
                            if(sumatotal < valor_suma_minimo):
                                valor_suma_minimo = sumatotal
                                matriz_optimaXij = Xij
                                matriz_optimaZik = Zik
                                matriz_optimaYjk = Yjk
                    
print("Optima Xij", matriz_optimaXij)
print("Optima Zik", matriz_optimaZik)
print("Optima Yjk", matriz_optimaYjk)
print("suma valor minimo" ,valor_suma_minimo)

############################################################################################################






###################################### Comienza la segunda expresión ################

print("Comienzo de la segunda expresión  - Cálculo de camiones")

#Primer término de camiones

Qwc = Vc*Ec*Dc / (1+Rc)
TRcij= (T1c-(T2c+T3c))/((2*Dij/SPDc)+T4c+T5c)

matriz_transpuesta = list(map(list, zip(*Aij)))

A = np.array(matriz_transpuesta)
TRcij = np.array(TRcij)
B = np.floor(TRcij)
TRcij = B
NCij = A / (Qwc*B)


A = np.array(matriz_optimaXij)
NCij = np.array(NCij)
B = np.ceil(NCij)
NCij=B

# n_columnas = A.shape[1]
# productos = []
# productos = np.sum(A * B, axis=0)
productos = productoEscalar2Matrices(A,B)
primer_termino_segundaexp = np.sum(productos)


print("Resultado del primer termino segunda expresión:", primer_termino_segundaexp)

###################################### Hasta acá primer termino segunda exp ################


#Segundo término de camiones

Qwt = Vt*Et*Dt / (1+Rt)
TRtjk= (T1t-(T2t+T3t))/((2*Djk/SPDt)+T4t+T5t)

Bjk = generarNuevoBjK((np.array(matriz_optimaXij) * np.array(matriz_transpuesta)) * (1 - RECj),matriz_optimaYjk)
A = np.array(Bjk)
TRtjk = np.array(TRtjk)
# Redondear los valores de la matriz A hacia arriba al número entero más cercano
B = np.floor(TRtjk)
TRtjk=B

NTjk = A / (Qwt*B)


A = np.array(matriz_optimaYjk)
NTjk = np.array(NTjk)
B = np.ceil(NTjk)
NTjk=B
productos = productoEscalar2Matrices(A,B)
resultado_final = sum(productos)
segundo_termino_segundaexp = (resultado_final)

print("Resultado del segundo termino segunda expresión:", segundo_termino_segundaexp)


########################HASTA ACÁ SEGUNDO TÉRMINO DE LA SEGUNDA EXPRESIÓN #################

#Tercer término de camiones
TRcik= (T1c-(T2c+T3c))/((2*Dik/SPDc)+T4c+T5c)
matriz_transpuesta = list(map(list, zip(*Cik)))

A = np.array(matriz_transpuesta)
TRcik = np.array(TRcik)
# Redondear los valores de la matriz A hacia arriba al número entero más cercano
B = np.floor(TRcik)
TRcik=B

NCik = A / (Qwc*B)



A = np.array(matriz_optimaZik)
NCik = np.array(NCik)
B = np.ceil(NCik)
NCik=B
productos = productoEscalar2Matrices(A,B)
resultado_final = sum(productos)
tercer_termino_segundaexp = (resultado_final)


#########################SUMA TOTAL DE CAMIONES

print(" La flota total de camiones se constituye por ", primer_termino_segundaexp + tercer_termino_segundaexp , "de camiones recolectores y ", segundo_termino_segundaexp, "de camiones transportadores, dando un total de " , primer_termino_segundaexp + segundo_termino_segundaexp + tercer_termino_segundaexp, "camiones")


print("Comienzo de la tercer expresión  - Cálculo de gases de EI en kg de CO2 eq")



A = np.array(matriz_optimaXij)
B = np.array(NCij)
C = np.array(Dij)
D = np.array(TRcij)

    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")

elif A.shape != C.shape:
    print("Las matrices no tienen la misma forma")
    
elif A.shape != D.shape:
    print("Las matrices no tienen la misma forma")
    
else: 
    productos = productoEscalar4Matrices(A,B,C,D)
    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    primer_termino_tercerexp = resultado_final*(Uc/KPLc)*2
    
    print("Resultado del primer término de la tercer expresión:", primer_termino_tercerexp)
    ###################################### Hasta acá primer termino de la tercer expresión ################
    

A = np.array(matriz_optimaYjk)
B = np.array(NTjk)
C = np.array(Djk)
D = np.array(TRtjk)


# print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
# print(matriz_optimaYjk)
# print(NTjk)
# print(Djk)
# print(TRtjk)

    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")

elif A.shape != C.shape:
    print("Las matrices no tienen la misma forma")
    
elif A.shape != D.shape:
    print("Las matrices no tienen la misma forma")
    
else: 
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    productos = productoEscalar4Matrices(A,B,C,D)
    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    #print("\nResultado final del producto escalar entre las columnas:", resultado_final)

    segundo_termino_tercerexp = resultado_final*(Ut/KPLt)*2
    
    print("Resultado del segundo término de la tercer expresión:", segundo_termino_tercerexp)
    
###################################### Hasta acá segundo termino de la tercer expresión ################  

A = np.array(matriz_optimaZik)
B = np.array(NCik)
C = np.array(Dik)
D = np.array(TRcik)

    # Verificar si las matrices tienen la misma forma
if A.shape != B.shape:
    print("Las matrices no tienen la misma forma.")

elif A.shape != C.shape:
    print("Las matrices no tienen la misma forma")
    
elif A.shape != D.shape:
    print("Las matrices no tienen la misma forma")
    
else: 
    
    
    # Calcular el producto escalar entre las columnas correspondientes
    productos = productoEscalar4Matrices(A,B,C,D)
    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    #print("\nResultado final del producto escalar entre las columnas:", resultado_final)

    tercer_termino_tercerexp = resultado_final*(Ut/KPLt)*2
    
    print(tercer_termino_tercerexp)
    print(np.ceil(tercer_termino_tercerexp + segundo_termino_tercerexp + primer_termino_tercerexp))

    final =  datetime.now() - hora_actual
    print("tiempo total de ejecución en minutos: ", final.total_seconds()/60)
    







