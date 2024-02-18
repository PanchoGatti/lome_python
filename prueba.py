def matriz_iterada(n, m):
    """
    Genera todas las combinaciones posibles de 0 y 1 para una matriz de dimensiones n x m,
    con la restricción de que solo puede haber un 1 por fila.
    """
    import itertools

    # Generar todas las combinaciones posibles de 0 y 1 para una fila de tamaño m
    combinaciones_fila = list(itertools.product([0, 1], repeat=m))

    # Generar matrices que cumplan con la restricción de un único "1" por fila
    matrices_iteradas = []
    for combinacion in itertools.product(combinaciones_fila, repeat=n):
        if all(sum(fila) <= 1 for fila in combinacion):  # Verificar la restricción
            matrices_iteradas.append(list(combinacion))

    return matrices_iteradas