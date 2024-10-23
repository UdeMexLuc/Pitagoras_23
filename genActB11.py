#def acti():
#    return [1, 10, 15, 17, 400, 23, 401]

def seleccionar_renglones(carpeta,archivo_entrada, archivo_salida):
    # Obtener los números de línea de la función acti()
    lineas_seleccionadas = Adial11a.acti11()
    
    # Abrir el archivo de entrada y procesar las líneas
  
    a1=carpeta+archivo_entrada
    a2=carpeta+archivo_salida
    with open(a1, 'r', encoding='utf-8') as entrada:
        lineas = entrada.readlines()
    
    # Abrir el archivo de salida para escribir las líneas seleccionadas
    with open(a2, 'w', encoding='utf-8') as salida:
        for i, linea in enumerate(lineas, start=1):
            if i in lineas_seleccionadas:
                salida.write(linea)

# Llamar a la función con el archivo de entrada y el archivo de salida
import Adial11a

carpeta= "Probls/"
seleccionar_renglones(carpeta, '11_logica_conseq_log_bb.txt', '11BB.txt')