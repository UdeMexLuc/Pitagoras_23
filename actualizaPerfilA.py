import re

# Función para leer el archivo de perfil y obtener la habilidad de "hab_num_variables"
def leer_perfil_habilidad(file_path, num_variables):
    habilidad_actual = None
    with open(file_path, 'r') as file:
        for line in file:
            if f"hab_num_variables({num_variables}" in line:
                habilidad_actual = int(re.search(r'\((\d+), (\d+)\)', line).group(2))
                break
    print("abilidad actual=", habilidad_actual) 
    return habilidad_actual

# Función para leer el archivo de características y obtener los problemas que tienen el número de variables solicitado
def obtener_actividades_por_num_variables(file_path, num_variables):
    actividades = []
    with open(file_path, 'r') as file:
        for line in file:
            if f"num_variables({num_variables}" in line:
                actividad_num = int(re.search(r'\((\d+),', line).group(1))
                actividades.append(actividad_num)
    return actividades


########
# Función para obtener la fórmula y la interpretación
def obtener_formula_interpretacion(history_file, actividad):
    formula = None
    interpretacion = None
    inside_block = False
    with open(history_file, 'r') as history:
        for line in history:
            # Detectar el inicio del bloque correspondiente a la actividad
            if f"Actividad [Evaluacion de Formula].{actividad}" in line:
                inside_block = True
            elif inside_block:
                # Encontrar la línea que contiene la fórmula
                if line.startswith("F ="):
                    formula = line.strip()
                # Encontrar la línea que contiene la interpretación
                elif "I(" in line:
                    interpretacion = line.strip().replace("I(", "").replace(")", "").replace(" = ", "")
                    interpretacion_abreviada = ', '.join([f'{var}{val}' for var, val in re.findall(r'([a-z])(\d)', interpretacion)])
                    return formula, interpretacion_abreviada
                # Si se encuentra una línea vacía, terminar el bloque
                elif line.strip() == "":
                    break
    return formula, interpretacion


###
# Función para contar las respuestas correctas e incorrectas del alumno y generar la tabla
def contar_respuestas_y_generar_tabla(history_file, correct_answers_file, actividades):
    tabla_resultados = []
    for actividad in actividades:
        # Obtener la fórmula y la interpretación abreviada
        formula, interpretacion = obtener_formula_interpretacion(history_file, actividad)
        print("actividad")
        print(actividad)
        print("F, I=", )

        # Buscar la respuesta del alumno
        respuesta_alumno = None
        with open(history_file, 'r') as history:
            for line in history:
                if f"Actividad [Evaluacion de Formula].{actividad}" in line:
                    respuesta_alumno = 0 if "I(F) = 0" in line else 1

        # Buscar la respuesta correcta
        respuesta_correcta = None
        with open(correct_answers_file, 'r') as correct_answers:
            for correct_line in correct_answers:
                if f"Actividad [Evaluacion de Formula].{actividad}" in correct_line:
                    respuesta_correcta = 0 if "I(F) = 0" in correct_line else 1

        if formula and interpretacion and respuesta_alumno is not None and respuesta_correcta is not None:
            # Añadir los resultados a la tabla
            tabla_resultados.append([formula, interpretacion, respuesta_alumno, respuesta_correcta])

    return tabla_resultados

# Función para calcular la nueva habilidad del alumno
def calcular_nueva_habilidad(habilidad_actual, correctas, incorrectas):
    total = correctas + incorrectas
    if total > 0:
        porcentaje_aciertos = correctas / total
        nueva_habilidad = (habilidad_actual + porcentaje_aciertos * 10) / 2
        return round(nueva_habilidad, 2)
    return habilidad_actual

# Función principal para procesar la actualización de la habilidad del alumno y generar la tabla de resultados
def actualizar_habilidad_por_num_variables(perfil_file, history_file, correct_answers_file, caractePr1_file):
    for num_variables in range(1, 5):
        # Obtener la habilidad actual del alumno para problemas con 'num_variables'
        habilidad_actual = leer_perfil_habilidad(perfil_file, num_variables)
        
        if habilidad_actual is None:
            print(f"No se encontró la habilidad para {num_variables} variables en el perfil del alumno.")
            continue

        # Obtener las actividades con problemas que tienen 'num_variables'
        actividades_variables = obtener_actividades_por_num_variables(caractePr1_file, num_variables)

        if not actividades_variables:
            print(f"No se encontraron actividades con {num_variables} variables.")
            continue

        # Contar las respuestas correctas e incorrectas y generar la tabla
        tabla_resultados = contar_respuestas_y_generar_tabla(history_file, correct_answers_file, actividades_variables)
        
        # Calcular las respuestas correctas e incorrectas
        correctas = sum(1 for fila in tabla_resultados if fila[2] == fila[3])
        incorrectas = len(tabla_resultados) - correctas

        # Calcular la nueva habilidad del alumno
        nueva_habilidad = calcular_nueva_habilidad(habilidad_actual, correctas, incorrectas)

        # Mostrar los resultados en formato de tabla
        print(f"\nNúmero de variables: {num_variables}")
        print(f"Habilidad actual: {habilidad_actual}")
        print(f"Respuestas correctas: {correctas}")
        print(f"Respuestas incorrectas: {incorrectas}")
        print(f"Nueva habilidad: {nueva_habilidad}")
        print("\nTabla de resultados:")
        if tabla_resultados:
            print(f"{'Fórmula':<60} {'Interpretación':<30} {'Respuesta Alumno':<20} {'Respuesta Correcta'}")
            for fila in tabla_resultados:
                print(f"{fila[0]:<60} {fila[1]:<30} {fila[2]:<20} {fila[3]}")
        else:
            print("No se encontraron ejercicios.")

# Llamada a la función principal con los archivos correctos
actualizar_habilidad_por_num_variables('KB/perfilAlum.dl', 'his/history.txt', 'Probls/1CleanE.txt', 'KB/caractePr1.dl')


    
