
import random

def extraer_digitos(cadena):
    # Usamos join para concatenar los dígitos en una sola cadena
    digitos = ''.join([char for char in cadena if char.isdigit()])
    return digitos

def ordenar_por_tamano(lista_cadenas):
    # Usamos sorted() con la función clave len para ordenar por tamaño de cadena
    return sorted(lista_cadenas, key=len)


def extraer_ejercicios_aleatorios(archivo_entrada):
    ejercs_sel = Adial1a.acti1()
 #   print(ejercs_sel)
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

    # Escribir los ejercicios seleccionados en el archivo de salida
 ##   with open(archivo_salida, 'w', encoding='utf-8') as salida:
        print()
        for ejercicio in ejercicios[1: ]:
            Ei=extraer_digitos(ejercicio[0])
            if int(Ei) in  ejercs_sel:
              # print(Ei)
                print(''.join(ejercicio))

          #     salida.writelines(ejercicio)
          #    salida.write("\n")  # Asegurar una línea en blanco entre ejercicios

import Adial1a
# Llamar a la función para extraer 7 ejercicios aleatorios
extraer_ejercicios_aleatorios('Probls/1CleanE.txt')
