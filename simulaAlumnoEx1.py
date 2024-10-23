
import random

def reemplazar_estrellas_por_binario(archivo_entrada):
    with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    # Procesar cada línea
    for linea in lineas:
        # Reemplazar cada "= *" por "= 0" o "= 1" aleatoriamente
        linea_modificada = linea.replace('= *', f'= {random.choice([0, 1])}')
        print(linea_modificada, end='')

# Llamar a la función para procesar el archivo y mostrar el resultado en pantalla
reemplazar_estrellas_por_binario('Probls/1Tarea.txt')


