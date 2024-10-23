import random
import re

def resolver_examen(archivo_entrada):
    # Abrir el archivo de entrada y leer todas las líneas
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
        lineas = entrada.readlines()
    # Expresión regular para encontrar el número del ejercicio y las respuestas
    ejercicio_pattern = re.compile(r'Ejercicio.*?\.(\d+)\.')
    
    # Generar una respuesta aleatoria ("correct" o "incorrect") para cada línea
    for linea in lineas:
        ejercicio_match = ejercicio_pattern.search(linea)
        numero_ejercicio = ejercicio_match.group(1)
        # Generar aleatoriamente "SI" o "NO" o "dificil"
        respuesta = random.choice(["SI", "NO", "dificil"])
        print("ejercicio", str(numero_ejercicio)+ ":", respuesta)
        # Almacenar el número de línea y la respuesta
    
  

# Llamar a la función con el archivo del examen
resolver_examen("Probls/"+'11BB.txt')

