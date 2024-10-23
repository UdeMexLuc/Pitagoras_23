
import re

# Definimos los conectivos posibles
conectivos = ['&', '+', '-', '>']

def analizar_formula(N, F):
    # Identificar los conectivos presentes (sin duplicados)
    conectivos_presentes = set(c for c in conectivos if c in F)
    
    # El número de conectivos es simplemente el tamaño del conjunto de conectivos presentes
    num_conectivos = len(conectivos_presentes)
    
    # Contar el número de variables distintas (letras minúsculas)
    variables = set(re.findall(r'[a-z]', F))
    num_variables = len(variables)
    
    # Longitud de la fórmula como cadena
    longitud_formula = len(F)
    
    # Profundidad de anidamiento (equivalente al máximo número de paréntesis anidados)
    max_anidamiento = 0
    profundidad_actual = 0
    for char in F:
        if char == '(':
            profundidad_actual += 1
            if profundidad_actual > max_anidamiento:
                max_anidamiento = profundidad_actual
        elif char == ')':
            profundidad_actual -= 1
    
    return num_conectivos, conectivos_presentes, num_variables, longitud_formula, max_anidamiento

def generar_bde(nombre_archivo_entrada, nombre_archivo_salida):
    with open(nombre_archivo_entrada, 'r') as archivo:
        lineas = archivo.readlines()

    with open(nombre_archivo_salida, 'w') as salida:
        for linea in lineas:
            N, F = linea.strip().split(':')
            num_conectivos, conectivos_presentes, num_variables, longitud_formula, max_anidamiento = analizar_formula(N, F)
            
            # Escribimos las relaciones en el archivo
            salida.write(f"num_conectivos({N}, {num_conectivos}).\n")
            for conectivo in conectivos_presentes:
                salida.write(f'usa_conectivo({N}, "{conectivo}").\n')
            salida.write(f"num_variables({N}, {num_variables}).\n")
            salida.write(f"longitud_formula({N}, {longitud_formula}).\n")
            salida.write(f"anidamiento({N}, {max_anidamiento}).\n")

# Generar 5 archivos
for i in range(1, 6):
    generar_bde('ListaFormulas.txt', f'archivo{i}.txt')

print("Archivos generados correctamente.")
