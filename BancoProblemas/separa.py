
import re

def limpiar_nombre_archivo(nombre):
    # Remover caracteres que no son válidos en los nombres de archivo
    return re.sub(r'[<>:"/\\|?*]', '_', nombre)

def procesar_bloques(archivo_entrada):
    with open(archivo_entrada, 'r', encoding='latin-1') as entrada:
        lineas = entrada.readlines()

    bloque_actual = []
    nombre_archivo = None
    dentro_bloque = False

    for i, linea in enumerate(lineas):
        linea = linea.strip()

        # Detectar el patrón de inicio de bloque: asteriscos, alfanumérica, asteriscos
        if i < len(lineas) - 2 and lineas[i].strip() == "**************************************************" \
           and lineas[i+2].strip() == "**************************************************" \
           and lineas[i+1].strip() and lineas[i+1].strip()[0].isdigit() and '.' in lineas[i+1]:

            # Si ya estamos dentro de un bloque, guardamos el bloque actual
            if bloque_actual and nombre_archivo:
                with open(nombre_archivo, 'w', encoding='utf-8') as archivo_salida:
                    archivo_salida.write("\n".join(bloque_actual))
                bloque_actual = []  # Reiniciar el bloque para el siguiente

            # Generar el nombre del archivo usando los primeros 7 caracteres de la línea alfanumérica
            nombre_archivo_original = lineas[i+1][:7].replace(" ", "_") + '.txt'
            nombre_archivo = limpiar_nombre_archivo(nombre_archivo_original)

            # Saltamos las siguientes dos líneas de asteriscos y alfanumérica
            dentro_bloque = True
            continue

        # Si estamos dentro de un bloque, añadimos las líneas a bloque_actual
        if dentro_bloque:
            bloque_actual.append(linea)

    # Guardar el último bloque al terminar de leer el archivo
    if bloque_actual and nombre_archivo:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write("\n".join(bloque_actual))

# Llamar a la función con el archivo de entrada
procesar_bloques('notas_logica_out.txt')
