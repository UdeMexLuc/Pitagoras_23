
def procesar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    # Inicializamos el contador
    n = 0
    
    # Procesamos las líneas
    for linea in lineas:
        if linea.startswith("F = "):
            # Eliminamos la subcadena "F = " y agregamos una coma al final
            cadena = linea.replace("F = ", "").strip()
            print(f'{n}:"{cadena}",')
            n += 1

# Llamamos a la función con el archivo de entrada
procesar_archivo("1._Eval.txt")
