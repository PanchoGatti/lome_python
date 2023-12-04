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

#Tercer término de camiones
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



###################################### Comienza la tercera expresión ################










print("Comienzo de la tercer expresión  - Cálculo de gases de EI en kg de CO2 eq")



A = np.array(Xij)
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
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        columna_matriz_3 = C[:, i]
        columna_matriz_4 = D[:, i]
        producto_escalar = np.sum(columna_matriz_1 * columna_matriz_2 * columna_matriz_3 * columna_matriz_4)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    #print("\nResultado final del producto escalar entre las columnas:", resultado_final)

    primer_termino_tercerexp = resultado_final*(Uc/KPLc)*2
    
    print("Resultado del primer término de la tercer expresión:", primer_termino_tercerexp)
    ###################################### Hasta acá primer termino de la tercer expresión ################
    

A = np.array(Yjk)
B = np.array(NTjk)
C = np.array(Djk)
D = np.array(TRtjk)

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
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        columna_matriz_3 = C[:, i]
        columna_matriz_4 = D[:, i]
        producto_escalar = np.sum(columna_matriz_1 * columna_matriz_2 * columna_matriz_3 * columna_matriz_4)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    #print("\nResultado final del producto escalar entre las columnas:", resultado_final)

    segundo_termino_tercerexp = resultado_final*(Ut/KPLt)*2
    
    print("Resultado del segundo término de la tercer expresión:", segundo_termino_tercerexp)
    
###################################### Hasta acá segundo termino de la tercer expresión ################  

A = np.array(Zik)
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
    n_columnas = A.shape[1]
    productos = []
    
     # Calcular el producto escalar entre las columnas correspondientes
    for i in range(n_columnas):
        columna_matriz_1 = A[:, i]
        columna_matriz_2 = B[:, i]
        columna_matriz_3 = C[:, i]
        columna_matriz_4 = D[:, i]
        producto_escalar = np.sum(columna_matriz_1 * columna_matriz_2 * columna_matriz_3 * columna_matriz_4)
        productos.append(producto_escalar)
        print(f"Producto escalar columna {i + 1}: {producto_escalar}")

    # Sumar los productos escalares individuales para obtener el resultado final
    resultado_final = sum(productos)
    #print("\nResultado final del producto escalar entre las columnas:", resultado_final)

    tercer_termino_tercerexp = resultado_final*(Ut/KPLt)*2
    

    
    
    print("El costo total es de: ", primer_termino + segundo_termino + tercer_termino + cuarto_termino + quinto_termino + sexto_termino + septimo_termino + octavo_termino + noveno_termino - decimo_termino)
    print(" La flota total es de " , primer_termino_segundaexp + segundo_termino_segundaexp + tercer_termino_segundaexp, "camiones")
    print("Los gases invernadero total son: ", primer_termino_tercerexp + segundo_termino_tercerexp + tercer_termino_tercerexp)
    
 ###############################################################################################################################################   