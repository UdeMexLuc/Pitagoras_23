
import random

def extraer_digitos(cadena):
    # Usamos join para concatenar los dígitos en una sola cadena
    digitos = ''.join([char for char in cadena if char.isdigit()])
    return digitos

def ordenar_por_tamano(lista_cadenas):
    # Usamos sorted() con la función clave len para ordenar por tamaño de cadena
    return sorted(lista_cadenas, key=len)


def extraer_ejercicios_aleatorios(archivo_entrada, archivo_salida, num_ejercicios=23):
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
        lineas = entrada.readlines()

    # Dividir el archivo en bloques de ejercicios
    ejercicios = []
    ejercicio_actual = []

    for linea in lineas:
        # Detectar el inicio de un nuevo ejercicio por el encabezado "Actividad"
        if linea.startswith("Actividad"):
            # Si ya hay un ejercicio actual en progreso, agregarlo a la lista de ejercicios
            if ejercicio_actual:
                ejercicios.append(ejercicio_actual)
            # Iniciar un nuevo ejercicio
            ejercicio_actual = [linea]
        else:
            # Agregar las líneas al ejercicio actual
            ejercicio_actual.append(linea)

    # Agregar el último ejercicio
    if ejercicio_actual:
        ejercicios.append(ejercicio_actual)

    # Seleccionar aleatoriamente 7 ejercicios
    ejS = ordenar_por_tamano(random.sample(ejercicios, num_ejercicios))[0:7]
    
    

    # Escribir los ejercicios seleccionados en el archivo de salida
    with open(archivo_salida, 'w', encoding='utf-8') as salida:
        for ejercicio in ejS:
            print(extraer_digitos(ejercicio[0]))
            salida.writelines(ejercicio)
            salida.write("\n")  # Asegurar una línea en blanco entre ejercicios

# Llamar a la función para extraer 7 ejercicios aleatorios
extraer_ejercicios_aleatorios('1BancoT.txt', '1Tarea.txt')
