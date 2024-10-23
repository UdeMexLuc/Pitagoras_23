import re

def extraer_respuestas_correctas(archivo_entrada):
    with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    # Expresión regular para encontrar el número del ejercicio y las respuestas
    ejercicio_pattern = re.compile(r'Ejercicio.*?\.(\d+)\.')
    respuesta_correcta_pattern = re.compile(r'((SI|NO).+?)correct')

    for linea in lineas:
        # Buscar el número del ejercicio
        ejercicio_match = ejercicio_pattern.search(linea)
        # Buscar la respuesta correcta (SI o NO) antes de "correct"
        respuesta_correcta_match = respuesta_correcta_pattern.search(linea)

        if ejercicio_match and respuesta_correcta_match:
            # Obtener el número de ejercicio y la respuesta correcta
            numero_ejercicio = ejercicio_match.group(1)
            respuesta_correcta = respuesta_correcta_match.group(2)

            # Imprimir el número de ejercicio y la respuesta correcta
            print(f"Ejercicio {numero_ejercicio}: {respuesta_correcta}")

# Llamar a la función con el archivo del examen
extraer_respuestas_correctas("Probls/"+'11BB.txt')
