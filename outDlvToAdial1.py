# outDlvToAdial.py
# Se ejecuta:
# python outDlVToAdial.py



import random

# Funcion residuo o modulo
# Supongo que int trunca, x confirmar
def modulo(extrae,no_models):
 return extrae- ( no_models * (int(extrae/no_models)))


# Convierte lista a cadena y la escribe
# Seguro se puede escribir mejor
# print se puede activar

def extrae_alnum(cadena):
 cad1= ""
 for k6 in range(0, len(cadena)):
  if cadena[k6].isalnum():
    cad1 += cadena[k6]
 return cad1

# Similar a la anterior funcion
def extrae_num(cadena):
 cad1= ""
 for k6 in range(0, len(cadena)):
  if cadena[k6].isdigit():
    cad1 += cadena[k6]
 return cad1




############# FIN de FUNCIONES

# Programa principal

#import sys

extrae= random.randint(1, 5)

file_name1= 'Adial1.int'

# Abre archivos e inicializa 
iden1 =open(file_name1,'r')

file_name2= "Adial1a.py"
iden2 =open(file_name2,"w")

# Leemos archivo y contamos modelos en no_models
no_models=0
apunt=[]
for renglon in iden1:
 if "{" !=  renglon[0]: continue
 no_models=no_models+1
 iden1.close
# Cerramos archivo
# no_models tiene el # de modelos

if no_models > 0:

# Usamos funcion residuo para seleccionar que modelo seleccionaremos
# obtenemos residuo y evitamos el 0
 counter= modulo(extrae,no_models) +1

# re open
 iden1 =open(file_name1,'r')

# Leemos archivo para seleccionar el modelo
# el modelo queda en la lista Adial1
# Esta lista contiene los atomos en posicion par e ubicacion en el sript
# En la posicion non contiene el token
 for renglon in iden1:
   if "{" !=  renglon[0]: continue
   counter=counter-1
   if counter !=0:continue
   Adial1 = renglon.split(',')
   break

# Ahora procesamos la lista para obtener en Adial2 la lista de tokens y
# en Apun la lista de apuntadores al sitio del token en el script

 Adial2=[]
 Apun=[]


 for jj in range(0, len(Adial1)):
    if jj%2 !=0:
      Adial2 += [extrae_alnum(Adial1[jj])]
    else:
      Apun += [int(extrae_num(Adial1[jj]))]


# print("Adial inicial= ", Adial2)
# print("Apun = ", Apun)
 iden1.close



# Ahora vamos a la ultima fase para obter Adial ordenada
 Adial= [None]*len(Apun)

 for JJ in range(0, len(Apun)):
  Adial[Apun[JJ]-1]= Adial2[JJ]
 
  Adial3 = ["1"] + Adial[ :2]  + Adial[2:3] + ["400"] + Adial[3:5 ] +  ["401"]


else:
 print(" Ya no hay actividades t1")
 Adial3=["1", "2", "3", "4"]


# Escribimos la salida
print("A1= ", Adial3)
iden2.writelines("def acti1():")
iden2.writelines("\n")
iden2.writelines("    return [")

for i in range(0, len(Adial3)-1):
  iden2.writelines(Adial3[i])
  iden2.writelines(",")
iden2.writelines(Adial3[len(Adial3)-1])
iden2.writelines("]")
iden2.writelines("\n")


#### fin

iden2.close







