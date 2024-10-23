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
# print("len ", len)
 for i in Lcad:
 #   print(i)

    if operando(i) :
      x= val_var(i,inC)
      pushC(x)
    else:
      if i=="-":
        A=popC()
        pushC(resultadoCu(i,A))
      else:
  #    print("operador ", Lcad[i])
        B = popC()
        A = popC()
 #       print("trace i", i)
 #       print("trace A", A)
 #       print("trace B", B)
        pushC(resultadoC(i,A,B))

 return popC()


def Eval_Clase(pout, Lcad, inC):
 global  pilaA, pp, pilaC, pc 
 pp=0
 pc=0
 Ic = -1 
# print("len ", len)
 for i in Lcad:
 #   print(i)

    if operando(i):
      pushA(i)
      x= val_var(i,inC)
      pushC(x)
      pout.write("I("+i+") = "+ str(x) +"\n")
    else:
      if i=="-":
        Ac=popC()
        Ic = resultadoCu(i,Ac)
        pushC(Ic)

        A=popA()
        pushA(resultadoAu(i,A))
        pout.write("I("+resultadoAu(i,A)+") = "+ str(Ic) +"\n")
      else:
        Bc = popC()
        Ac = popC()
        Ic = resultadoC(i,Ac,Bc)
        pushC(Ic)

  #    print("operador ", Lcad[i])
        B = popA()
        A = popA()
 #       print("trace i", i)
 #       print("trace A", A)
 #       print("trace B", B)
        pushA(resultadoA(i,A,B))
        pout.write("I("+resultadoA(i,A,B)+") = "+ str(Ic) +"\n")
 ou1= popA()
 Ic = popC()
 if ou1[0]=="(":
  return "I(F) = I("+ou1[1: len(ou1)-1]+") = " + str(Ic)
 return "I(F) = I("+ ou1 +") = " + str(Ic)




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
# print("len ", len)
 for i in Lcad:
 #   print(i)

    if operando(i):
      pushA(i)
    else:
      if i=="-":
        A=popA()
        pushA(resultadoAu(i,A))
      else:
  #    print("operador ", Lcad[i])
        B = popA()
        A = popA()
 #       print("trace i", i)
 #       print("trace A", A)
 #       print("trace B", B)
        pushA(resultadoA(i,A,B))
 ou1= popA()
 if ou1[0]=="(":
  return ou1[1: len(ou1)-1]
 return ou1
################

def degeneraEval_abstr(Lcad,defectos):
 global  pilaA, pp
 pp=0
 opsL = ["-","+","&",">"]
# print("len ", len)
 for i in Lcad:
 #   print(i)
    d = random.randint(0,10)
    if operando(i):
      if(d<=2):
        di = random.randint(0,len(opsL)-1)
        pushA(opsL[di])
        defectos.append("Operador "+ opsL[di] +" funcionando como operando (atomo).")
      else :
        pushA(i)
    else:
      if i=="-":
        A=popA()
        if(d<=2):
          di = random.randint(1,len(opsL)-1)
          pushA(resultadoAu(opsL[di],A))
          defectos.append("Operador binario "+ opsL[di] +" funcionando como operador unario.")
        else:          
          pushA(resultadoAu(i,A))
      else:
        B = popA()
        A = popA()
        if(d<=2):
          pushA(resultadoA(opsL[0],A,B))
          defectos.append("Operador unario "+ opsL[0] +" funcionando como operador binario.")
        else: 
          pushA(resultadoA(i,A,B))
 ou1= popA()
 if ou1[0]=="(":
  return ou1[1: len(ou1)-1]
 return ou1



################

def casoF(m):
 if m == 0: return 0
 return (m%2)+1


def gen_fA(n):
  f=[None]*10
  if n==0: 
     f= [0]
     return f
  n=n-1
  m= random.randint(0, 10)
  op=casoF(m)
  if op==0: 
     f= [0]
     return f
  elif op==2:
    f=gen_fA(n) + gen_fA(n) + [2]
    return f
  else:
    f=gen_fA(n) + [1]
    return f

###########

def gen_fA_NL(n):
  f=[None]*10
  if n==0: 
     f= [0]
     return f
  n=n-1
  m= random.randint(0, 9)
  if (0<=m<=1):
    op = 1
  elif (2<=m<=9):
    op = 2
  else:
    op = 0
  if op==0: 
     f= [0]
     return f
  elif op==2:
    f=gen_fA(n) + gen_fA(n) + [2]
    return f
  else:
    f=gen_fA(n) + [1]
    return f

#######

def gen_tA(n):
  ll=random.randint(2, 4)
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

def gen_tC(t1,m):
 teoria=[]
 for i in t1:
     t2= gen_fC(i,m)
     teoria=teoria + [t2]
 return teoria


def gen_fC(F,m):
 global vari,conta
 conta=0
 bin="&+>"
 c=""
 conta=0
 for i in F:
   if i== 0:
      n= random.randint(0, m-1)
##      n=gen_num_var(m)
      c=c+ vari[n]
   elif i==1:
       c=c+ "-"
   else:
       n=random.randint(0, 2)
       c=c+ bin[n]
 return c


#############
def gen_fC_LN(F,m):
 global vari,conta
 conta=0
 bin="&+>"
 c=""
 conta=0
 cimp = 0 
 for i in F:
   if i== 0:
      mrr= random.randint(0, m-1)
      n = 0
      for rr in range(mrr):
         n= random.randint(0, m-1)
##      n=gen_num_var(m)
      c=c+ vari[n]
   elif i==1:
       c=c+ "-"
   else:
       n=random.randint(0, 10)
       if(0<=n<=9 and cimp<2):
         c=c+ bin[2]
         cimp = cimp+1
       else:
         n = random.randint(0,1)
         c=c+ bin[n]
 return c


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

def escribeIC(inC,y):
 global vari
 str = ""
 m=len(inC)
 print("interpretacion dada")
 for i in range(m):
   c=vari[i]
   x=val_var(c,inC)
   if c in y: 
     print(c, "evalua a ", x)
     str1 = "1"
     if (x==0):
      str1 = "0"
     str+= "I(" + c +") = " + str1 + ", "
 return str[0:len(str)-2]

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

def escribe_l(l):
 strl = "{"
 print("{")
 for i in l[0:len(l)-1]:
   print(" ",i, ",")
   strl+=" "+str(i)+ ","
 print(" ", l[len(l)-1])
 strl+= " " + str(l[len(l)-1])
 print("}")
 strl+= " }"
 return strl


def makeNota(pout, textoP, opciones, opcionCorrecta):
  #pout.write("MC\t")
  pout.write("---\n")
  pout.write(textoP)
  #pout.write("\t")

  op = 0
  while op<len(opciones) :
    opRan = random.randint(0,len(opciones)-1)
    opTmp = opciones[opRan]
    opciones.remove(opTmp)
    opciones.append(opTmp)
    op = op +1   

  pout.write("Posibles respuestas:\n\n")
  k = 1
  for o in opciones:
    pout.write(str(k)+". ")
    pout.write(o)
    pout.write("\n")
    #if(o==opcionCorrecta):
    #  pout.write("correct\t")
    #else:
    #  pout.write("incorrect\t")
    k = k +1
  pout.write("\n\n")
  pout.write("La respuesta correcta es: "+ opcionCorrecta+".\n\n") 


def init_text_atoms():
 global text_atoms
 text_atoms = []
 file_name= "text_atoms_bd.in"
 pin =open(file_name,"r")
 for atom in pin:
   if(atom[0]!="#"):
    text_atoms.append(atom.strip())
   else:
     break
 pin.close

def asignaHashTableChAtoms(strF):
  global text_atoms,htChToAtom
  htChToAtom.clear()
  cp_ta = text_atoms.copy()
  htChToAtom["+"] = "o"
  htChToAtom["&"] = "y"
  htChToAtom[">"] = "implica que"
  htChToAtom["-"] = "no es cierto que"

  for c in strF:
    if operando(c):
      vht = htChToAtom.get(c)
      if (vht == None):
        ri = random.randint(0,len(cp_ta)-1)
        htChToAtom[c] = cp_ta[ri]
        cp_ta.remove(cp_ta[ri])
  cp_ta.clear()

def toNaturalLang(strF):
  global text_atoms, htChToAtom
  htChToAtom.clear()
  asignaHashTableChAtoms(strF)
  strNL = ""
  for c in strF:
    txt = htChToAtom.get(c)
    if txt!=None:
      strNL+=txt+" "
    elif c=="<<":
      strNL+="( "
    elif c==">>":
      strNL+=")"
  return strNL.strip()


############ BATERIAS DE EJERCICIOS ##############

def write_bateria_evaluaInterpretacion(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):
  x= gen_fA(prfM)
  if len(x)<3:
   continue
  print(" ")
  print(" --------- Caso # " , num_casos)
  print("genera formula abstracta (polaca)")
  print(x)
  y= gen_fC(x,num_var)
##  num_var=conta
  num_inte= pow(2,num_var)
  print("genera formula concreta (polaca)")
  print(y)

  print(" ")
  z= Eval_abstr(y)
  print("genera formula concreta (standard)")
  print(z)

#genera interpretacion
  inA= random.randint(0, num_inte-1)
  inC= inte_concre(num_var, inA)

  Istr = escribeIC(inC,y)

  e= Eval_concr(y, inC)

  print(" Formula evalua (interpretacion)=", e)
  ### EJERCICIO EVLAUACION
  textoP = "Ejemplo [Evaluacion de Formula]."+str(num_casos+1)+".\n\n" 
  textoP+= "Dada la siguiente formula logica: \n\n"
  textoP+= "F = "+ z +". \n\n"
  textoP+= "Y la siguiente interpretacion: \n\n" + Istr +". \n\n"
  textoP+= "Evalue la interpretacion I de la formula dada F si es 1 o 0.\n\n "
  opciones = []
  opciones.append("I(F) = 1")
  opciones.append("I(F) = 0")
  if e==0 :
    opcionCorrecta = "I(F) = 0"
  else: 
    opcionCorrecta = "I(F) = 1"

  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion: \n\n")
  Eval_Clase(pout, y, inC)
  ### FIN EJERCICIO EVALUACION

  num_casos=num_casos +1  

def write_bateria_tautologia(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):
  x= gen_fA(prfM)
  if len(x)<3:
   continue
  print(" ")
  print(" --------- Caso # " , num_casos)
  print("genera formula abstracta (polaca)")
  print(x)
  y= gen_fC(x,num_var)
##  num_var=conta
  num_inte= pow(2,num_var)
  print("genera formula concreta (polaca)")
  print(y)

  print(" ")
  z= Eval_abstr(y)
  print("genera formula concreta (standard)")
  print(z)

#genera interpretacion
  inA= random.randint(0, num_inte-1)
  inC= inte_concre(num_var, inA)

  Istr = escribeIC(inC,y)

  e= Eval_concr(y, inC)

  print(" Formula evalua (interpretacion)=", e)

  es_taut=1
  es_inc= 1
  for k in range(num_inte):
    inC= inte_concre(num_var, k)
    e= Eval_concr(y, inC)
    if e==0:
      es_taut=0
    else: 
      es_inc=0

  if es_taut:
    print("La formula es tautologia")
  elif es_inc:
    print("La formula es inconsistente")
  else:
    print("La formula es incontingente ( es sat sin ser tautologia)")

  ### EJERCICIO TAUTOLOGIA 
  textoP = "Ejemplo [Vefificar Tautologia de Formula]."+str(num_casos+1)+".\n\n" 
  textoP+= "Dada la siguiente formula logica: \n\n"
  textoP+= "F = "+ z +". \n\n"
  textoP+= "Evalue si la formula F dada es una tautología: es decir para cada  interpretacion I de la formula F,  I(F)=1. \n\n"

  textoP+= "La Formula F dada: \n\n"
  opciones = []
  opciones.append("SI es una tautologia")
  opciones.append("NO es una tautologia")
  if es_taut==0 :
    opcionCorrecta = "NO es una tautologia"
  else: 
    opcionCorrecta = "SI es una tautologia"

  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion:\n\n")
  
  pout.write("A. Verifiquemos todas las interpretaciones:\n\n")
  es_taut=1
  es_inc= 1
  hayI = dict()
  hayI.clear
  ki = 0
  for k in range(num_inte):
	  
    inC= inte_concre(num_var, k)
    Istr = escribeIC(inC,y)
    hayIf = hayI.get(Istr)
    if hayIf == None : 
      pout.write("A"+str(ki)+ ". Evaluemos la interpretacion: "+Istr+ ".\n\n")
    
      e= Eval_concr(y, inC)
    
      u = Eval_Clase(pout, y, inC)
      pout.write(u+ "\n\n")
      if e==0:
        pout.write("Ya que I(F) = 0. La Formula F no es tautologia ya que existe al menos una interpretacion I que evalua a 0\n\n")
        es_taut=0
      else: 
        es_inc=0
      hayI[Istr] = Istr 
      ki = ki+1

  pout.write("Conclusion: "+ opcionCorrecta)
  ### FIN EJERCICIO TAUTOLOGIA
  num_casos=num_casos +1



def write_bateria_inconsistencia(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):
  x= gen_fA(prfM)
  if len(x)<3:
   continue
  print(" ")
  print(" --------- Caso # " , num_casos)
  print("genera formula abstracta (polaca)")
  print(x)
  y= gen_fC(x,num_var)
##  num_var=conta
  num_inte= pow(2,num_var)
  print("genera formula concreta (polaca)")
  print(y)

  print(" ")
  z= Eval_abstr(y)
  print("genera formula concreta (standard)")
  print(z)

#genera interpretacion
  inA= random.randint(0, num_inte-1)
  inC= inte_concre(num_var, inA)

  Istr = escribeIC(inC,y)

  e= Eval_concr(y, inC)

  print(" Formula evalua (interpretacion)=", e)

  es_taut=1
  es_inc= 1
  for k in range(num_inte):
    inC= inte_concre(num_var, k)
    e= Eval_concr(y, inC)
    if e==0:
      es_taut=0
    else: 
      es_inc=0

  if es_taut:
    print("La formula es tautologia")
  elif es_inc:
    print("La formula es inconsistente")
  else:
    print("La formula es incontingente ( es sat sin ser tautologia)")

  ### EJERCICIO INCONSISTENCIA
  textoP = "Ejemplo [Vefificar Inconsistencia de Formula]."+str(num_casos+1)+".\n\n" 
  textoP+= "Dada la siguiente formula logica:\n\n"
  textoP+= " F = "+ z +". \n\n"
  textoP+= "Evalue si la formula F es inconsistente: es decir para cada  interpretacion I de la formula F,  I(F)=0.\n "
  textoP+= "La Formula F dada: \n\n"
  opciones = []
  opciones.append("SI es inconsistente")
  opciones.append("NO es inconsistente")
  if es_inc==0 :
    opcionCorrecta = "NO es inconsistente"
  else: 
    opcionCorrecta = "SI es inconsistente"

  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion:\n\n")
  
  pout.write("A. Verifiquemos todas las interpretaciones:\n\n")
  es_taut=1
  es_inc= 1
  hayI = dict()
  hayI.clear
  ki = 0
  for k in range(num_inte):
	  
    inC= inte_concre(num_var, k)
    Istr = escribeIC(inC,y)
    hayIf = hayI.get(Istr)
    if hayIf == None : 
      pout.write("A"+str(ki)+ ". Evaluemos la interpretacion: "+Istr+ ".\n\n")
    
      e= Eval_concr(y, inC)
    
      u = Eval_Clase(pout, y, inC)
      pout.write(u+ "\n\n")
      if e==0:
        es_taut=0
      else: 
        pout.write("Ya que I(F) = 1. La Formula F no es Inconsistente ya que existe al menos una interpretacion I que evalua a 1\n\n")
        es_inc=0
      hayI[Istr] = Istr 
      ki = ki+1

  pout.write("Conclusion: "+ opcionCorrecta)

  
  ### FIN EJERCICIO INCONSISTENCIA
  num_casos=num_casos +1

def write_bateria_tau_incons_contin(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):
  x= gen_fA(prfM)
  if len(x)<3:
   continue
  print(" ")
  print(" --------- Caso # " , num_casos)
  print("genera formula abstracta (polaca)")
  print(x)
  y= gen_fC(x,num_var)
##  num_var=conta
  num_inte= pow(2,num_var)
  print("genera formula concreta (polaca)")
  print(y)

  print(" ")
  z= Eval_abstr(y)
  print("genera formula concreta (standard)")
  print(z)

#genera interpretacion
  inA= random.randint(0, num_inte-1)
  inC= inte_concre(num_var, inA)

  Istr = escribeIC(inC,y)

  e= Eval_concr(y, inC)

  print(" Formula evalua (interpretacion)=", e)

  es_taut=1
  es_inc= 1
  for k in range(num_inte):
    inC= inte_concre(num_var, k)
    e= Eval_concr(y, inC)
    if e==0:
      es_taut=0
    else: 
      es_inc=0

  if es_taut:
    print("La formula es tautologia")
  elif es_inc:
    print("La formula es inconsistente")
  else:
    print("La formula es incontingente ( es sat sin ser tautologia)")


  ### EJERCICIO TAUT, INCONS O CONTIN
  textoP = "Ejemplo [Vefificar Tipo de Evaluacion de Formula]."+str(num_casos+1)+". \n\n"
  textoP+= "Dada la siguiente formula logica:\n\n"
  textoP+= "F = "+ z +".\n\n"
  textoP+= "Evalue si la formula F dada es Tautologia, Inconsistente o Contingente (no es tautologia, ni es inconsistente). \n\n"
  textoP+= "La Formula F dada es: \n\n"
  opciones = []
  opciones.append("TAUTOLOGIA")
  opciones.append("INCONSISTENTE")
  opciones.append("CONTINGENTE")
  if es_taut:
    opcionCorrecta = "La Formula F es una tautologia"
  elif es_inc:
    opcionCorrecta = "La Formula F es inconsistente"
  else:
    opcionCorrecta = "La Formula F es contingente"

  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion:\n\n")
  
  pout.write("A. Verifiquemos todas las interpretaciones:\n\n")
  es_taut=1
  es_inc= 1
  hayI = dict()
  hayI.clear
  ki = 0
  for k in range(num_inte):
	  
    inC= inte_concre(num_var, k)
    Istr = escribeIC(inC,y)
    hayIf = hayI.get(Istr)
    if hayIf == None : 
      pout.write("A"+str(ki)+ ". Evaluemos la interpretacion: "+Istr+ ".\n\n")
    
      e= Eval_concr(y, inC)
    
      u = Eval_Clase(pout, y, inC)
      pout.write(u+ "\n\n")
      if e==0:
        pout.write("Ya que I(F) = 0. La Formula F no es tautologia ya que existe al menos una interpretacion I que evalua a 0\n\n")		  
        es_taut=0
      else: 
        pout.write("Ya que I(F) = 1. La Formula F no es Inconsistente ya que existe al menos una interpretacion I que evalua a 1\n\n")
        es_inc=0
      hayI[Istr] = Istr 
      ki = ki+1

  pout.write("Conclusion: "+ opcionCorrecta)

  
  ### FIN EJERCICIO TAUT, INCONS O CONTIN
  num_casos=num_casos +1


def write_bateria_cadena_es_formula(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):

  ### EJERCICIO DETERMINAR SI CADENA ES FORMULA 
  print("***********DEGENERANDO")
  x = []
  while len(x)<3:
    x= gen_fA(prfM)


  print("genera formula abstracta (polaca)")
  print(x)
  y= gen_fC(x,num_var)
##  num_var=conta
  num_inte= pow(2,num_var)
  print("genera formula concreta (polaca)")
  print(y)

  print(" ")
  zgood = Eval_abstr(y)
  print("formula correcta")
  print(zgood)

  opciones = []
  opciones.append(zgood)
  oi = 0 
  defectos = []
  hdef = dict()
  while(oi<3):
   defectos = []	  
   zbad= degeneraEval_abstr(y,defectos)
   if zbad!=zgood:
      print("DEgenera formula concreta (standard)")
      print(zbad)
      opciones.append(zbad)
      hdef[zbad] = defectos
      oi = oi + 1

  textoP = "Ejemplo [Determinar si es una formula bien escrita]."+str(num_casos+1)+". \n\n"
  textoP+= "Determine cual de las siguientes expresiones es una formula: \n\n"
  opcionCorrecta = zgood
  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion:\n\n")
  
  for opt in opciones:
    if (opt!=zgood):
       pout.write("La expresion "+opt +" tiene los siguientes errores:\n")
       defectos = hdef.get(opt)
       for dft in defectos:
          pout.write("Error: " + dft +  "\n")
       pout.write("Por lo tanto no es formula\n\n")
  
  pout.write("La formula "+ opcionCorrecta + " tiene todos sus operadores y operandos correctos.\n\n")
  pout.write("Conclusion:  La expresion "+ opcionCorrecta + " es una formula.\n\n" )
  
  ### FIN EJERCICIO DETERMINAR SI CADENA ES FORMULA 

  

  num_casos=num_casos +1


def write_bateria_lengNat(pout,NO_CASOS, num_var, prfM):
 global pilaA, vari, pilaC, conta, text_atoms, htChToAtom

 num_casos=0
 while(num_casos < NO_CASOS):

  ### EJERCICIO Formalizar un enunciado (de leng natural a lenguaje simbólico)
  print("***********LENGUAJE NATURAL")
  x = []
  while len(x)<3:
    x= gen_fA_NL(3)

  print("genera formula abstracta (polaca)")
  print(x)
  y= gen_fC_LN(x,num_var)
  
  print("genera formula concreta (polaca)")
  print(y)

  print(" ")
  zgood = Eval_abstr(y)
  print("formula correcta")
  print(zgood)

  zNL = toNaturalLang(zgood)
  print(zNL)

  textoP = "Ejemplo [Formalizar un enunciado de lenguaje natural a lenguaje simbolico)]."+str(num_casos+1)+". \n\n"
  textoP+= "Dado el siguiente enunciado: \n\n"
  textoP+= "'"+ zNL +"'. \n\n"
  textoP+= "Determine cual es la formula que formaliza en lenguaje simbolico el enunciado dado: \n\n"
  opciones = []
  opciones.append(zgood)
  for bf in range(3) :
   x = [] 
   while len(x)<3:
     x= gen_fA_NL(3)
   y= gen_fC_LN(x,num_var)
   zbad = Eval_abstr(y)
   opciones.append(zbad)
  opcionCorrecta = zgood
  makeNota(pout, textoP, opciones, opcionCorrecta)
  
  pout.write("Demostracion: \n\n")
  pout.write("Considere la formula "+ opcionCorrecta +".\n\n")
  pout.write("Del enunciado determinamos los posibles operadores (conectivos), asi como los operandos (atomos) que aparecen en la oracion: \n\n")
  hks = htChToAtom.keys()
  for hk in hks:
    pout.write("- "+ htChToAtom[hk]+ ".\n")
   
   
  pout.write("\nPara cada conectivo lo abstraemos a un operador y para cada atomo lo abstraemos a una variable: \n\n")
  for hk in hks:
    pout.write("Sustituimos '"+ htChToAtom[hk] + "' por " + hk +".\n")
  pout.write("Sustituimos cuñas << en el enunciado por parentesis ( en la formula abstracta.\n")
  pout.write("Sustituimos cuñas >> en el enunciado por parentesis ) en la formula abstracta.\n")
  
  pout.write("\nConclusion: La formula "+ opcionCorrecta +" formaliza en lenguaje simbolico el enunciado dado.\n\n")
  
  
  ### FIN EJERCICIO Formalizar un enunciado (de leng natural a lenguaje simbólico)

  num_casos=num_casos +1

#### baterias de teoria 

def write_bateria_modelaInterpretacionTeoria(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):
  t1= gen_tA(prfM)
  print(" ")
  print(" --------- Caso # " , num_casos)
  print("genera teoria abstracta (polaca)")
  escribe_l(t1)
  t2= gen_tC(t1,num_var)
##  num_var=conta
  num_inte= pow(2,num_var)
  print("genera teoria concreta (polaca)")
  escribe_l(t2)
  y= conjAll(t2)

#  print("conjAll")
#  print(y)

  print(" ")
  t3= Eval_abstrt(t2)
  print("genera teoria concreta (standard)")
  strT3 = escribe_l(t3)

#genera interpretacion
  inA= random.randint(0, num_inte-1)
  inC= inte_concre(num_var, inA)

  Istr= escribeIC(inC,y)

  e= Eval_concr(y, inC)

  print(" Teoria evalua (interpretacion)=", e)
  ### EJERCICIO EVLAUACION
  textoP = "Ejemplo [Verificar si una Interpretacion Modela una Teoria]."+str(num_casos+1)+".\n\n"
  textoP+= "Dada la siguiente Teoria : \n\n"
  textoP+= "T = "+ strT3 +". \n\n"
  textoP+= "Y la siguiente interpretacion: \n\n"
  textoP+= Istr +". \n\n"
  textoP+= "Evalue si la interpretacion I es modelo de la teoria T. \n\n"
  opciones = []
  opciones.append("La interpretacion I SI es modelo de la teoria T")
  opciones.append("La interpretacion I NO es modelo de la teoria T")
  if e==0 :
    opcionCorrecta = "La interpretacion I NO es modelo de la teoria T"
  else: 
    opcionCorrecta = "La interpretacion I SI es modelo de la teoria T"

  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion: \n\n")
  pout.write("Dada la interpretacion: "+ Istr +".\n")
  pout.write("Y la Teoria T = " +strT3+".\n\n")
  pout.write("I modela a T si y solo si I(F) = 1 para toda F en la teoria T. \n")
  pout.write("Verifiquemos la interpretacion I para cada formula F en la teoria T: \n")
  for fy in t2:
    z= Eval_abstr(fy)
    pout.write("Sea F en la teoria T con F = " +z +".\n")
    pout.write("Calculemos I(F):\n")
    u = Eval_Clase(pout, fy, inC)
    pout.write(u + "\n\n")

  if e==0 :
    pout.write("Observe que existe al menos una formula F en la teoria T donde I(F) = 0\n\n")
  else: 
    pout.write("Observe que para todas las formulas F en la teoria T I(F) = 1\n\n") 
  
  pout.write("Conclusion: "+opcionCorrecta+".\n\n")
  
  pout.write("Demostracion alternativa: \n\n")
  pout.write("Dada la interpretacion: "+ Istr +".\n")
  pout.write("Y la Teoria T = " +strT3+".\n\n")

  pout.write("Es posible unir todas las formulas en la teoria T con el conectivo and.\n")
  pout.write("Esto nos da una unica formula G = "+ Eval_abstr(y)+ ".\n")
  pout.write("La interpretacion I modela la teoria T si y solo si I(G) = 1.\n")
  pout.write("Calculamos I(G): \n")
  u = Eval_Clase(pout, y, inC)
  u = u[0:2] + 'G' +u[3:]
  pout.write(u + "\n\n")
  
  pout.write("Conclusion: "+opcionCorrecta+".\n\n")
  ### FIN EJERCICIO EVALUACION

  num_casos=num_casos +1



def write_bateria_esTeoriaInconsistente(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):
  t1= gen_tA(prfM)
  print(" ")
  print(" --------- Caso # " , num_casos)
  print("genera teoria abstracta (polaca)")
  escribe_l(t1)
  t2= gen_tC(t1,num_var)
##  num_var=conta
  num_inte= pow(2,num_var)
  print("genera teoria concreta (polaca)")
  escribe_l(t2)
  y= conjAll(t2)

#  print("conjAll")
#  print(y)

  print(" ")
  t3= Eval_abstrt(t2)
  print("genera teoria concreta (standard)")
  strT3 = escribe_l(t3)

#genera interpretacion
  inA= random.randint(0, num_inte-1)
  inC= inte_concre(num_var, inA)

  escribeIC(inC,y)

  e= Eval_concr(y, inC)

  if e:
    print("La interpretacion modela a la teoria")
  else:
    print("La interpretacion NO modela a la teoria")

  es_taut=1
  es_inc= 1
  for k in range(num_inte):
    inC= inte_concre(num_var, k)
    e= Eval_concr(y, inC)
    if e==0:
      es_taut=0
    else: 
      es_inc=0

  if es_taut:
    print("Todas las interpretaciones modelan a la teoria")
  elif es_inc:
    print("La teoria es inconsistente")
  else:
    print("La teoria es incontingente ( es consistente pero existen interpretaciones que no modelan a la teoria")


  ### EJERCICIO INCONSISTENCIA
  textoP = "Ejemplo [Vefificar Inconsistencia de una Teoria]."+str(num_casos+1)+".\n\n"
  textoP+= "Dada la siguiente Teoria : \n\n"
  textoP+= "T = "+ strT3 +". \n\n"
  textoP+= "Determine si la teoria T es inconsistente. \n\n"
  textoP+= "La Teoria T dada: \n\n"
  opciones = []
  opciones.append("SI es inconsistente")
  opciones.append("NO es inconsistente")
  if es_inc==0 :
    opcionCorrecta = "La Teoria T NO es inconsistente"
  else: 
    opcionCorrecta = "La Teoria T SI es inconsistente"

  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion: \n\n")
  pout.write("Dada la Teoria T = " +strT3+".\n\n")
  pout.write("La Teoria T es inconsistente si solo si para toda Interpretacion I, I(T) = 0.\n")
  pout.write("Es posible unir todas las formulas en la teoria T con el conectivo and.\n")
  pout.write("Esto nos da una unica formula G = "+ Eval_abstr(y)+ ".\n")
  pout.write("Una interpretacion I modela la teoria T si y solo si I(G) = 1.\n")
  pout.write("La Teoria T es inconsistente si solo si para toda Interpretacion I, I(G) = 0.\n")
  pout.write("A. Por lo tanto para cada interpretacion I debemos calcular I(G): \n")
  
  hayI = dict()
  hayI.clear
  ki = 0
  for k in range(num_inte):
	  
    inC= inte_concre(num_var, k)
    Istr = escribeIC(inC,y)
    hayIf = hayI.get(Istr)
    if hayIf == None : 
      pout.write("A"+str(ki)+ ". Evaluemos la interpretacion: "+Istr+ ".\n\n")
    
      e= Eval_concr(y, inC)
    
      u = Eval_Clase(pout, y, inC)
      u = u[0:2] + 'G' +u[3:]
      pout.write(u+ "\n\n")
      if e==0:
        es_taut=0
      else: 
        pout.write("Ya que I(G) = 1. La Teoria T no es inconsistente ya que existe al menos una interpretacion I que evalua a 1\n\n")
        es_inc=0
      hayI[Istr] = Istr 
      ki = ki+1

  pout.write("Conclusion: "+opcionCorrecta+".\n\n")
  ### FIN EJERCICIO INCONSISTENCIA

  num_casos=num_casos +1

def write_bateria_esTeoriaTautologia(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):
  t1= gen_tA(prfM)
  print(" ")
  print(" --------- Caso # " , num_casos)
  print("genera teoria abstracta (polaca)")
  escribe_l(t1)
  t2= gen_tC(t1,num_var)
##  num_var=conta
  num_inte= pow(2,num_var)
  print("genera teoria concreta (polaca)")
  escribe_l(t2)
  y= conjAll(t2)

#  print("conjAll")
#  print(y)

  print(" ")
  t3= Eval_abstrt(t2)
  print("genera teoria concreta (standard)")
  strT3 = escribe_l(t3)

#genera interpretacion
  inA= random.randint(0, num_inte-1)
  inC= inte_concre(num_var, inA)

  escribeIC(inC,y)

  e= Eval_concr(y, inC)

  if e:
    print("La interpretacion modela a la teoria")
  else:
    print("La interpretacion NO modela a la teoria")

  es_taut=1
  es_inc= 1
  for k in range(num_inte):
    inC= inte_concre(num_var, k)
    e= Eval_concr(y, inC)
    if e==0:
      es_taut=0
    else: 
      es_inc=0

  if es_taut:
    print("Todas las interpretaciones modelan a la teoria")
  elif es_inc:
    print("La teoria es inconsistente")
  else:
    print("La teoria es incontingente ( es consistente pero existen interpretaciones que no modelan a la teoria")


  ### EJERCICIO TATUTOLOGIA
  textoP = "Ejemplo [Vefificar Tautologia en una Teoria]."+str(num_casos+1)+". \n\n"
  textoP+= "Dada la siguiente Teoria :\n\n"
  textoP+= "T = "+ strT3 +". \n\n"
  textoP+= "Determine si la teoria T es modelada por todas sus interpretaciones. \n\n"
  textoP+= "La Teoria T: \n\n"
  opciones = []
  opciones.append("SI es modelada por todas sus interpretaciones")
  opciones.append("NO es modelada por todas sus interpretaciones")
  if es_taut==0 :
    opcionCorrecta = "La Teoria T NO es modelada por todas sus interpretaciones"
  else: 
    opcionCorrecta = "La Teoria T SI es modelada por todas sus interpretaciones"

  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion: \n\n")
  pout.write("Dada la Teoria T = " +strT3+".\n\n")
  pout.write("La Teoria T es modelada por toda interpretacion si solo si para toda Interpretacion I, I(T) = 1.\n")
  pout.write("Es posible unir todas las formulas en la teoria T con el conectivo and.\n")
  pout.write("Esto nos da una unica formula G = "+ Eval_abstr(y)+ ".\n")
  pout.write("Una interpretacion I modela la teoria T si y solo si I(G) = 1.\n")
  pout.write("La Teoria T es modelada por toda interpretacion si solo si para toda Interpretacion I, I(G) = 1.\n")
  pout.write("A. Por lo tanto para cada interpretacion I debemos calcular I(G): \n")
  
  hayI = dict()
  hayI.clear
  ki = 0
  for k in range(num_inte):
	  
    inC= inte_concre(num_var, k)
    Istr = escribeIC(inC,y)
    hayIf = hayI.get(Istr)
    if hayIf == None : 
      pout.write("A"+str(ki)+ ". Evaluemos la interpretacion: "+Istr+ ".\n\n")
    
      e= Eval_concr(y, inC)
    
      u = Eval_Clase(pout, y, inC)
      u = u[0:2] + 'G' +u[3:]
      pout.write(u+ "\n\n")
      if e==0:
        es_taut=0
        pout.write("Ya que I(G) = 0. La Teoria T no es modelada por toda interpretacion ya que existe al menos una interpretacion I que evalua a 0\n\n")
      else: 
        #pout.write("Ya que I(G) = 1. La Teoria T no es inconsistente ya que existe al menos una interpretacion I que evalua a 1\n\n")
        es_inc=0
      hayI[Istr] = Istr 
      ki = ki+1

  pout.write("Conclusion: "+opcionCorrecta+".\n\n")
  
  
  ### FIN EJERCICIO TAUTOLOGIA


  num_casos=num_casos +1

def write_bateria_esTeoria_Inc_Tau_Cont(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):
  t1= gen_tA(prfM)
  print(" ")
  print(" --------- Caso # " , num_casos)
  print("genera teoria abstracta (polaca)")
  escribe_l(t1)
  t2= gen_tC(t1,num_var)
##  num_var=conta
  num_inte= pow(2,num_var)
  print("genera teoria concreta (polaca)")
  escribe_l(t2)
  y= conjAll(t2)

#  print("conjAll")
#  print(y)

  print(" ")
  t3= Eval_abstrt(t2)
  print("genera teoria concreta (standard)")
  strT3 = escribe_l(t3)

#genera interpretacion
  inA= random.randint(0, num_inte-1)
  inC= inte_concre(num_var, inA)

  escribeIC(inC,y)

  e= Eval_concr(y, inC)

  if e:
    print("La interpretacion modela a la teoria")
  else:
    print("La interpretacion NO modela a la teoria")

  es_taut=1
  es_inc= 1
  for k in range(num_inte):
    inC= inte_concre(num_var, k)
    e= Eval_concr(y, inC)
    if e==0:
      es_taut=0
    else: 
      es_inc=0

  if es_taut:
    print("Todas las interpretaciones modelan a la teoria")
  elif es_inc:
    print("La teoria es inconsistente")
  else:
    print("La teoria es incontingente ( es consistente pero existen interpretaciones que no modelan a la teoria")


  ### EJERCICIO TATUTOLOGIA_inconsistencia_contingencia
  textoP = "Ejemplo [Vefificar Tautologia en una Teoria]."+str(num_casos+1)+". \n\n"
  textoP+= "Dada la siguiente Teoria : \n\n"
  textoP+= "T = "+ strT3 +". \n\n"
  textoP+= "Determine si la teoria T es modelada por todas sus interpretaciones o bien es inconsistente o bien es contingente. \n\n"
  textoP+= "La Teoria T es:\n\n "
  opciones = []
  opciones.append("Es modelada por todas sus interpretaciones")
  opciones.append("INCONSISTENTE")
  opciones.append("CONTINGENTE")
  if es_taut:
    opcionCorrecta = "La teoria T es modelada por todas las interpretaciones"
  elif es_inc:
    opcionCorrecta = "La teoria T es Inconsistente"
  else:
    opcionCorrecta = "La Teoria T es contingente"

  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion: \n\n")
  pout.write("Dada la Teoria T = " +strT3+".\n\n")
  pout.write("La Teoria T es modelada por una interpretacion I si solo si I(T) = 1.\n")
  pout.write("Es posible unir todas las formulas en la teoria T con el conectivo and.\n")
  pout.write("Esto nos da una unica formula G = "+ Eval_abstr(y)+ ".\n")
  pout.write("Una interpretacion I modela la teoria T si y solo si I(G) = 1.\n")
  pout.write("A. para toda Interpretacion I debemos calcular I(G): \n")
  
  hayI = dict()
  hayI.clear
  ki = 0
  for k in range(num_inte):
	  
    inC= inte_concre(num_var, k)
    Istr = escribeIC(inC,y)
    hayIf = hayI.get(Istr)
    if hayIf == None : 
      pout.write("A"+str(ki)+ ". Evaluemos la interpretacion: "+Istr+ ".\n\n")
    
      e= Eval_concr(y, inC)
    
      u = Eval_Clase(pout, y, inC)
      u = u[0:2] + 'G' +u[3:]
      pout.write(u+ "\n\n")
      if e==0:
        es_taut=0
        pout.write("Ya que I(G) = 0. La Teoria T no es modelada por toda interpretacion ya que existe al menos una interpretacion I que evalua a 0\n\n")
      else: 
        pout.write("Ya que I(G) = 1. La Teoria T no es inconsistente ya que existe al menos una interpretacion I que evalua a 1\n\n")
        es_inc=0
      hayI[Istr] = Istr 
      ki = ki+1

  pout.write("Conclusion: "+opcionCorrecta+".\n\n")

   
  ### FIN EJERCICIO TAUTOLOGIA_inconsistente_contingencia


  num_casos=num_casos +1

def write_bateria_consecuenciaLogica(pout,NO_CASOS, num_var, prfM):
 num_casos=0
 while(num_casos < NO_CASOS):

  ff=gen_fA(prfM)
  gg= gen_fC(ff,num_var-1)
  hh= Eval_abstr(gg)
  t1= gen_tA(prfM)
  print(" ")
  print(" --------- Caso # " , num_casos)
#  print("genera teoria abstracta (polaca)")
##  escribe_l(t1)
  t2= gen_tC(t1,num_var-1)
##  num_var=conta
  num_inte= pow(2,num_var)
#  print("genera teoria concreta (polaca)")
##  escribe_l(t2)
  y= transCLunsat(t2,gg)
#  print(y)

#  print("conjAll")
#  print(y)

  print(" ")
  t3= Eval_abstrt(t2)
  print("genera problema de consecuencia logica (standard)")
  strT3 = escribe_l(t3)
  strCL = escribe_lc(t3,hh)

#  print(y)
  es_sat= 0
  for k in range(num_inte):
    inC= inte_concre(num_var, k)
    e= Eval_concr(y, inC)
    if e==1:
      es_sat=1
      testigo= inC

  if es_sat==0:
    print("Si es consecuencia logica")
  else:
    print("No es consecuencia logica")
    escribe_contraE(testigo,y)
    
  ### EJERCICIO CONSECUENCIA LOGICA
  textoP = "Ejemplo [Verificar si una formula es consecuencia logica de una Teoria]."+str(num_casos+1)+". \n\n"
  textoP+="Dada la siguiente Teoria: \n\n" 
  textoP+="T = "+ strT3 +". \n\n"
  textoP+= "Y la formula:\n\n"
  textoP+= "F = "+str(hh) +". \n\n"
  textoP+= "Determine si la formula F es consecuencia logica de T, es decir: \n\n" 
  textoP+= strCL+ " . \n\n" 
  opciones = []
  opciones.append("La formula F SI es consecuencia logica de la teoria T.")
  opciones.append("La formula F NO es consecuencia logica de la teoria T.")
  if es_sat ==0 :
    opcionCorrecta = "La formula F SI es consecuencia logica de la teoria T"
  else: 
    opcionCorrecta = "La formula F NO es consecuencia logica de la teoria T"

  makeNota(pout, textoP, opciones, opcionCorrecta)
  pout.write("Demostracion:\n\n")
  pout.write("Una formula F es consecuencia Logica de una teoria T si y solo si para toda interpretacion I si I(T) = 1 entonces I(F) = 1\n") 
  pout.write("Dada una interpretacion I la sentencia 'Si I(T)=1 entonces I(F) = 1' es equivalente a I(T) = 0 o I(F) = 1\n")
  pout.write("Luego Una formula F es consecuencia logica de una teoria T si y solo si para toda interpretacion I es cierto se cumple que I(T) = 0 o I(F) = 1.\n")
  pout.write("Luego Una formula F NO es consecuencia logica de una teoria T si y solo si Existe una interpretacion I donde se cumple que I(T) = 1 y I(F) = 0.\n")
  pout.write("Luego podemos suponer que F es consecuencia logica de la Teoria T a menos que se demuestre lo contrario: \n")
  pout.write("Es decir que  existe una interpretacion I donde I(T) = 1 y I(F) = 0.\n") 
  pout.write("Por tanto es necesario evaluar toda interpretacion para verificar si I(T) = 1 y I(F) = 0.\n") 
  pout.write("Podemos en una nueva formula H unir las formulas en la teoria T con el y la formula -F todas con el conectivo and.\n")
  pout.write("Dada una interpretacion I, I(T)=1 y I(F) = 0 si y solo si I(H) = 1.\n")
  pout.write("Por tanto si existe una interpretacion I donde I(H) = 1 entonces la formula F no es una consecuencia logica de la teoria T\n")
  pout.write("Verifiquemos cada Interpretacion evaluando I(H): \n\n") 

  pout.write("Dada la  Teoria: \n" )
  pout.write("T = "+ strT3 +". \n")
  pout.write("Y la formula:\n")
  pout.write("F = "+str(hh) +". \n")
  pout.write("Formamos la formula H = "+ Eval_abstr(y) +".\n\n")
  
  hayI = dict()
  hayI.clear
  ki = 0
  es_sat= 0
  for k in range(num_inte):
    inC= inte_concre(num_var, k)
    Istr = escribeIC(inC,y)
    hayIf = hayI.get(Istr)
    if hayIf == None : 
      pout.write("A"+str(ki)+ ". Evaluemos la interpretacion: "+Istr+ ".\n\n")
      e= Eval_concr(y, inC)
    
      u = Eval_Clase(pout, y, inC)
      u = u[0:2] + 'H' +u[3:]
      pout.write(u+ "\n\n")

      if e==1:
        pout.write("Observe que existe una interpretacion donde I(H) = 1 por tanto la formula F no es consecuencia logica de la teoria T.\n")  
        es_sat=1
        testigo= inC

      hayI[Istr] = Istr 
      ki = ki+1

  if es_sat==0:
    pout.write("Ya que para toda interpretacion I, I(H) = 0 entonces:\n")
    #print("Si es consecuencia logica")
  #else:
    #print("No es consecuencia logica")
    #escribe_contraE(testigo,y)



  pout.write("Conclusion: "+opcionCorrecta+".\n\n")


  ### FIN EJERCICIO CONSECUENCIA LOGICA
    
  num_casos=num_casos +1


####### MAIN

global pilaA, vari, pilaC, conta, text_atoms, htChToAtom
import random

init_text_atoms()
#print(text_atoms)

#hash table en python
htChToAtom = dict()
#asignaHashTableChAtoms("-a+b>i&a+c&b")
#print(htChToAtom)
#txt = toNaturalLang("-a+b>i&a+c&b")
#print(txt)

pilaA=[None]*100
pilaC=[None]*100


vari="abcdefghij"
# numero de variables a lo mas 6
num_var=6
#num_inte= pow(2,num_var)

# profundidad maxima formulas
prfM=4

## write down baterias
NO_EJERCICIOS = 1000

##file_name= "black_board/notas_logica_out.txt"
file_name= "notas_logica_out.txt"
pout = open(file_name,"w")

pout.write("NOTAS DE CLASE PARA TEMA DE LOGICA.\n") 
pout.write("PROFESOR: DR. MAURICIO OSORIO GALINDO.\n\n")
pout.write("IMPORTANTE. Te sugerimos  leer antes la teoría en  el libro de texto y tener a la mano el glosario proporcionado en clase.")

TEXTO_N = "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "1. Evaluacion de una formula dada una Interpretacion.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_evaluaInterpretacion(pout,NO_EJERCICIOS, num_var, prfM)

TEXTO_N = "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "2. Determinar si una formula es una tautologia.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_tautologia(pout,NO_EJERCICIOS, 3, prfM)

TEXTO_N = "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "3. Determinar si una formula es Inconsistente.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_inconsistencia(pout,NO_EJERCICIOS, 3, prfM)

TEXTO_N= "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "4. Determinar si una formula es una Tautologia, Inconsistente o Contingente.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_tau_incons_contin(pout,NO_EJERCICIOS, 3, prfM)

TEXTO_N= "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "5. Determinar si una expresion es una Formula.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_cadena_es_formula(pout,NO_EJERCICIOS, num_var, prfM)

TEXTO_N= "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "6. Abstraer una expresion en lenguaje natural a una formula en lenguaje simbolico.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_lengNat(pout,NO_EJERCICIOS, num_var, prfM)

TEXTO_N= "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "NOTAS SOBRE TEORIAS EN LOGICA.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)

TEXTO_N= "**************************************************\n"
TEXTO_N+= "7. Dada una teoria determinar si una interpretacion dada modela a la teoria dada.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_modelaInterpretacionTeoria(pout,NO_EJERCICIOS, 6, 2)


TEXTO_N= "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "8. Dada una teoria determinar si toda interpretacion modela la teoria dada.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_esTeoriaTautologia(pout,NO_EJERCICIOS, 3, 2)

TEXTO_N= "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "9. Dada una teoria determinar si es una teoria inconsistente.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_esTeoriaInconsistente(pout,NO_EJERCICIOS, 3, 2)


TEXTO_N= "\n\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "10. Dada una teoria determinar si toda interpretacion modela la teoria dada, o es Inconsistente o bien Contingente.\n"
TEXTO_N+= "**************************************************\n"
TEXTO_N+= "\n\n"
pout.write(TEXTO_N)
write_bateria_esTeoria_Inc_Tau_Cont(pout,NO_EJERCICIOS, 3, 2)

#TEXTO_N= "\n\n"
#TEXTO_N+= "**************************************************\n"
#TEXTO_N+= "11. Dada una teoria y una formula determinar si la formula es #consecuencia logica de la teoria dada.\n"
#TEXTO_N+= "**************************************************\n"
#TEXTO_N+= "\n\n"
#pout.write(TEXTO_N)
#write_bateria_consecuenciaLogica(pout,NO_EJERCICIOS, 3, 2)

pout.close
