
import re

def eliminar_lineas_duplicadas(lista_lineas):
    return list(dict.fromkeys(lista_lineas))

def procesar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
   
        lineas = entrada.readlines()

    nueva_salida = []
    reemplazar = True  # Control para reemplazar "= 0" y "= 1"
    dentroDemo = False
    
    
    for linea in lineas:
        # Cambiar "Ejemplo" por "Actividad"
        if "Ejemplo" in linea:
            linea = linea.replace("Ejemplo", "\n"+ "Actividad")
            dentroDemo=False
            demoActual=[]
        
        # Encontrar la línea posterior a "Y la siguiente interpretacion:"
        if "Y la siguiente interpretacion:" in linea:
            reemplazar = False
                    
        # Reemplazar "= 0" o "= 1" por "= *" en todo lo demás

        if "= 0" in linea or "= 1" in linea:
          if reemplazar:
            linea = re.sub(r'= [01]', '= *', linea)
          else:
            reemplazar=True
          if dentroDemo:
            if linea in demoActual: linea=""
        if "Posibles respuestas" in linea:
            reemplazar=False
            linea= "Cambia * por tu respuesta.\n"+linea

        if "Demostracion:" in linea:
           dentroDemo = True
           demoActual=[]
        
        if dentroDemo:  
           demoActual=demoActual+[linea]
        nueva_salida.append(linea)

 

    # Escribir el resultado al archivo de salida
    with open(archivo_salida, 'w', encoding='utf-8') as salida:
        salida.writelines(nueva_salida)

# Llamar a la función con el archivo de entrada y salida
procesar_archivo('1._Eval.txt', '1BancoT.txt')
