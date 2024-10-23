def procesar_archivos(archivo_ra, archivo_rc):
    # Inicializar contadores
    C = 0  # Coincidencias
    N = 0  # Número de veces que encontramos "dificil" en Z
    I = 0  # Calculado como 7 - (C + N)
    
    # Abrir ambos archivos
    with open(archivo_ra, 'r', encoding='utf-8') as ra, open(archivo_rc, 'r', encoding='utf-8') as rc:
        lineas_ra = ra.readlines()
        lineas_rc = rc.readlines()

    # Asegurarse de que ambos archivos tengan el mismo número de líneas no vacías
    lineas_ra = [linea.strip() for linea in lineas_ra if linea.strip()]
    lineas_rc = [linea.strip() for linea in lineas_rc if linea.strip()]

    if len(lineas_ra) != len(lineas_rc):
        raise ValueError("Los archivos no tienen el mismo número de líneas no vacías.")

    # Procesar cada línea de ambos archivos
    for linea_ra, linea_rc in zip(lineas_ra, lineas_rc):
        # Extraer el valor Z de cada línea (es el valor después de ':')
        z_ra = linea_ra.split(':')[-1].strip()
        z_rc = linea_rc.split(':')[-1].strip()
        
        # Contar coincidencias C
        if z_ra == z_rc:
            C += 1
        
        # Contar ocurrencias de "dificil" en Z
        if "dificil" in z_ra:
            N += 1

    return C, N

# Llamar a la función con los archivos de entrada
archivo_ra = 'Ra11.txt'
archivo_rc = 'RC11.txt'
carpeta="RespExamenes/"
C, N = procesar_archivos(carpeta+archivo_ra, carpeta+archivo_rc)

# Mostrar los resultados
print(f"Coincidencias (C)= {C}" f" Num de  veces que aparece 'dificil' (N)= {N}")


