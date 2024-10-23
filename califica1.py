
def contar_subcadenas_y_renglones_comunes(archivo1, archivo2):
    # Contadores para N y M
    N = 0  # Subcadenas "= d" en archivo1
    M = 0  # Renglones comunes con "= d" en ambos archivos, en la misma posición (línea)

    # Leer ambos archivos
    with open(archivo1, 'r', encoding='utf-8') as f1:
        lineas1 = f1.readlines()
    
    with open(archivo2, 'r', encoding='utf-8') as f2:
################parche abajo FEO
        lineas2 = f2.readlines()[1:]

    # Asegurarse de que ambos archivos tengan el mismo número de líneas
    min_lineas = min(len(lineas1), len(lineas2))
#    print(len(lineas1),",", len(lineas2))
#    print(lineas1[0])
#    print(lineas2[0])
    if len(lineas1) != len(lineas2) :
      print("ERROR")

    # Iterar sobre las líneas correspondientes de ambos archivos
    for i in range(min_lineas):
        linea1 = lineas1[i].strip()
        linea2 = lineas2[i].strip()

        # Verificar si la línea tiene más de un símbolo "=" y descartarla
        if linea1.count('=') > 1 or linea2.count('=') > 1:
            continue  # Ignorar la línea si tiene más de un "="

        # Contar las ocurrencias de subcadena "= d" en el primer archivo (Ra11.txt)
        if "= 0" in linea1 or "= 1" in linea1:
            N += 1
        
        # Verificar si las líneas son iguales en ambas posiciones y tienen la subcadena "= d"
        if (linea1 == linea2) and ("= 0" in linea1 or "= 1" in linea1):
            M += 1

    # Desplegar los valores de N y M
    print(f"N = {N}", f" M = {M}")
#    print(f"M = {M}")

# Llamar a la función con los archivos de entrada
contar_subcadenas_y_renglones_comunes('RespExamenes/Ra1.txt', 'RespExamenes/RC1.txt')
