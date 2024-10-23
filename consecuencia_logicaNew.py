

# Función que encuentra la letra mayor en orden lexicográfico en una cadena de entrada
def letra_mayor(cadena):
    # Filtramos solo las letras en la cadena, en caso de que haya otros caracteres
    letras = [char for char in cadena if char.isalpha()]
    # Devolvemos la letra máxima en orden lexicográfico
    return max(letras) if letras else None  # Si no hay letras, devolvemos None



def resultadoCu(op,A):
 salida = 1- A
 return salida

def resultadoC(op,A,B):
 if op=="+":
   return A or B
 if op=="&":
   return A and B
 else:
   return (1-A) or B


def popC():
  global  pilaC, pc
  pc= pc-1
  x= pilaC[pc]
  return x

def pushC(x):
  global  pilaC, pc
  pilaC[pc]= x
  pc= pc +1

def Eval_concr(Lcad, inC):
 global  pilaC, pc
 pc=0
 for i in Lcad:


    if operando(i) :
      x= val_var(i,inC)
      pushC(x)
    else:
      if i=="-":
        A=popC()
        pushC(resultadoCu(i,A))
      else:
        B = popC()
        A = popC()
        pushC(resultadoC(i,A,B))

 return popC()

############

def resultadoAu(op,A):
 salida ="(" + op + A + ")"
 return salida

def resultadoA(op,A,B):
 salida ="(" + A + op + B + ")"
 return salida

def operando(op):
 if op in "abcdefghij": return 1
 else: return

def popA():
  global banco_sets, expr, pilaA, pp
  pp= pp-1
  x= pilaA[pp]
  return x

def pushA(x):
  global banco_sets, expr, pilaA, pp
  pilaA[pp]= x
  pp= pp +1

def  Eval_abstrt(t):
 global  pilaA, pp
 teoria=[]
 for i in t:
   t1= Eval_abstr(i)
   teoria=teoria + [t1]
 return teoria
    

def Eval_abstr(Lcad):
 global  pilaA, pp
 pp=0

 for i in Lcad:
    if operando(i):
      pushA(i)
    else:
      if i=="-":
        A=popA()
        pushA(resultadoAu(i,A))
      else:

        B = popA()
        A = popA()

        pushA(resultadoA(i,A,B))

 return popA()

################

def casoF(m):
 if m == 0: return 0
 return (m%2)+1



def gen_tA(n,ll):
  teoria=[]
  for i in range(ll):
     t1= gen_fA(n)
     teoria=[t1] + teoria
  return teoria
   
 

def gen_num_var(m):
 global conta
 if conta==0:
   conta=conta+1
   return 0
 if conta > m : 
   n=random.randint(0, conta-1)
   return n
 fl= random.randint(0, 1)
 if fl==0:
  n=random.randint(1, conta)
  return n-1
 else:
   temp=conta
   conta=conta+1
   return temp

def gen_tC(ll,prf,nVar):
 teoria=[]

 ## for i in  range(0, ll-1):
 for i in  range(0, ll):
     t2= gen_fC(prf, nVar)
     teoria=teoria + [t2]
 return teoria

def algunElem(v):
  n=random.randint(0, len(v)-1)
  return v[n]

def genParVal(prM,mM):
     incorrect=1
     while incorrect:
        pr=random.randint(0, prM)
        m=random.randint(1, mM)
        cade=str(pr)+ str(m)
       
        if cade in formula_dict:
          return formula_dict[cade]
       

# Generacion concreta de la formula
# F es la formula abstracta
# m es el numero de variables (maximo)
# ejemplo 
# Input:  [0, 0, 2, 1] 2
# Output:  ab>-
def gen_fC(prM,mM):
        v= genParVal(prM,mM)
        k= algunElem(v)
        l=dictM.get(k)
        return l

def num_bin(inte):
 if inte<2: return str(inte)
 r= inte %2
 y= inte // 2
 return str(r) + num_bin(y) 

def inte_concre(num_var, inte):
 k= num_bin(inte)
 s= k+"000000000000"
 return s[0:num_var]
 
def val_var(v,inC):
 a= ord(v)-ord("a")
 return int(inC[a])

def escribe_contraE(inC,y):
 global vari
 m=len(inC)
 print("Contraejemplo")
 for i in range(m):
   c=vari[i]
   x=val_var(c,inC)
   if c in y: print(c, "evalua a ", x)

def conjAll(t):
 f=""
 for i in t:
  f=f+i
 for i1 in range(1,len(t)):
  f=f+ "&"
 return f

def transCLunsat(Te,fo):
 t1= conjAll(Te)
 fo1= fo + "-"
 tf= t1 + fo1 + "&"
 return tf

def escribe_lc(l,fo):
 print("{")
 strl = "{"
 for i in l[0:len(l)-1]:
   print(" ",i, ",")
   strl+= " "+str(i)+ ","
 print(" ", l[len(l)-1])
 strl+= " " + str(l[len(l)-1])
 print("} |= ", fo)
 strl+=" } |= "+ str(fo)
 return strl

# Checar
def escribe_l(l):
 strl = "{"
# print("{")
 for i in l[0:len(l)-1]:
#   print(" ",i, ",")
   strl+=" "+str(i)+ ","
# print(" ", l[len(l)-1])
 strl+= " " + str(l[len(l)-1])
# print("}")
 strl+= " }"
 return strl


def makePreguntaMC(pout, textoP, opciones, opcionCorrecta):
  pout.write("MC\t")
  pout.write(textoP)
  pout.write("\t")

  op = 0
  while op<len(opciones) :
    opRan = random.randint(0,len(opciones)-1)
    opTmp = opciones[opRan]
    opciones.remove(opTmp)
    opciones.append(opTmp)
    op = op +1   

  for o in opciones:
    pout.write(o)
    pout.write("\t")
    if(o==opcionCorrecta):
      pout.write("correct\t")
    else:
      pout.write("incorrect\t")
  pout.write("\n")


def write_bateria_consecuenciaLogica(pout,NO_CASOS, num_var,ll, prfM):
# print("num_var (maximo)=",num_var)
# print("numeros de formulas en la teoria=",ll)
# print("profundidad maxima=", prfM)
 contSi=0
 contNo=0
 num_casos=0
 while(num_casos < NO_CASOS):
  print(" ")
  print(" --------- Caso # " , num_casos)

  gg= gen_fC(prfM,num_var-1)
  hh= Eval_abstr(gg)
#  print ("hh= ", hh)
  t2= gen_tC(ll,prfM,num_var-1)
#  print("teoria ", t2)
  y= transCLunsat(t2,gg)

  letraMay=letra_mayor(y)
  print(" ")
  t3= Eval_abstrt(t2)
 # print("genera problema de consecuencia logica (standard)")
  strT3 = escribe_l(t3)
  strCL = escribe_lc(t3,hh)

  es_sat= 0
  num_varM=ord(letraMay.lower()) - ord('a')+1
  num_inte= pow(2,num_varM)

  for k in range(num_inte):
    inC= inte_concre(num_varM, k)
    e= Eval_concr(y, inC)
    if e==1:
      es_sat=1
      testigo= inC

  if es_sat==0:
    print("Si es consecuencia logica")
    contSi=contSi+1
  else:
    print("No es consecuencia logica")
    escribe_contraE(testigo,y)
    contNo=contNo+1
    
  ### EJERCICIO CONSECUENCIA LOGICA
  textoP = "Ejercicio [Verificar si una formula es consecuencia logica de una Teoria]."+str(num_casos+1)+". "
  textoP+="Dada la siguiente Teoria : T = "+ strT3 +". Y la formula F="+str(hh) +". "
  textoP+= "Determine si la formula F es consecuencia logica de T, es decir: " + strCL+ " . " 
  opciones = []
  opciones.append("La formula F SI es consecuencia logica de la teoria T.")
  opciones.append("La formula F NO es consecuencia logica de la teoria T.")
  if es_sat ==0 :
    opcionCorrecta = "La formula F SI es consecuencia logica de la teoria T."
  else: 
    opcionCorrecta = "La formula F NO es consecuencia logica de la teoria T."

  makePreguntaMC(pout, textoP, opciones, opcionCorrecta)
  ### FIN EJERCICIO CONSECUENCIA LOGICA
    
  num_casos=num_casos +1

 print()
 print("Resumen de casos")
 print(" Si, No =(",contSi, ",", contNo, ")" )


####### main
global pilaA, vari, pilaC, conta
import random
from universal import dictMain,dict4

formula_dict = dict4.get_info2Fnum()
dictM = dictMain.get_formula_dictionary()

pilaA=[None]*100
pilaC=[None]*100

numero_ejemplos=1000

vari="abcdefghij"
# numero de variables a lo mas 6
num_var=3
#num_inte= pow(2,num_var)
ll=random.randint(1, 3)

# profundidad maxima formulas
prfM=2

file_name= "11_logica_conseq_log_bb.txt"
#file_name= "black_board/11_logica_conseq_log_bb.txt"
pout =open(file_name,"w")
print("Problemas de consecuencia logica.")
write_bateria_consecuenciaLogica(pout, numero_ejemplos, num_var,ll, prfM)
pout.close





