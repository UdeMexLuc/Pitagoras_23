# Pitagoras_23

---


## Sistema de Generación y Evaluación de Ejercicios de Lógica Proposicional. 
Desarrollado en el contexto del "HACK4EDU 2024" y tiene como objetivo generar y evaluar automáticamente ejercicios de lógica proposicional, adaptados al perfil de los estudiantes.

Este prototipo fue desarrollado en el contexto del **HACK4EDU 2024** y tiene como objetivo generar y evaluar automáticamente ejercicios de lógica proposicional, adaptados al perfil de los estudiantes.

### Descripción General

El sistema consta de múltiples programas escritos en **DLV** y **Python**, que trabajan en conjunto para generar problemas, evaluarlos y calificar las respuestas de los estudiantes.

### Ejecución del Sistema

Para ejecutar el sistema, se debe utilizar el archivo `ejecutaSistema.cmd` desde la línea de comandos. Este archivo ejecuta una secuencia de actividades que incluyen la generación de problemas y su posterior evaluación.

---

### Flujo de Actividades

1. **Generación de Problemas: **
   - Se proponen 5 conjuntos de 5 problemas para el estudiante, seleccionados con base en su perfil y las características de los problemas.
   - La base de conocimiento para este proceso se encuentra en la carpeta 'KB', y la salida se almacena en el archivo `Adial1.int`.

2. **Categorías de Actividades:**
   - El sistema maneja dos categorías de actividades: identificadas por el número "1" y "11" en los archivos correspondientes.
   - Cada categoría ejecuta el mismo proceso de manera independiente.

3. **Archivos de Salida:**
   - `Adial1.int` y `Adial11.int` contienen los problemas propuestos para el estudiante.
   - `outDlvToAdial1.py` y `outDlvToAdial11.py` selecciona un problema del conjunto previamente seleccionado de manera aleatoria y agregan tres problemas fijos para crear un archivo de Python con un diccionario de los problemas seleccionados.

*Nota:* Los ejercicios fijos se agregan pensando en la posibilidad de que el docente decida agregar ciertos ejercicios que en su experiencia los estudiantes deben tener siempre presente. Sin embargo, es posible seleccionar estos ejercicios usando otros criterios. 

4. **Funciones Generadas:**
   - Los archivos `Adial1a.py` y `Adial11a.py` contienen funciones que devuelven los problemas seleccionados por el sistema en formato de lista.

5. **Extracción de Ejercicios:**
   - `genActB1.py` y `genActB11.py` extraen los problemas seleccionados del banco (`1BancoT.txt`), generando como salida el archivo `1Tarea.txt` con los enunciados de los ejercicios.

6. **Simulación de Respuestas y Calificación:**
   - Los archivos `simulaAlumnoExp1.py`, `simulaAlumnoExp11.py`, `califica1.py` y `califica11.py` simulan tanto las respuestas de los estudiantes como la calificación asignada. 
   - En una futura integración con una plataforma educativa, estos archivos serán reemplazados por la interacción real con el estudiante.
   
*Nota:* El sistema actualmente puede generar los ejercicios en formato compatible con **Blackboard** y se está trabajando para que también sea compatible en **Moodle**

7. **Extracción de Respuestas Correctas:**
   - `extraRcorrectas1.py` y `extraRcorrectas11.py` extraen las respuestas correctas de los ejercicios seleccionados.

8. **DLV Ejecutable:**
   - El archivo `dlv.exe` es el ejecutable del software **DLV**, que es de acceso abierto. Se espera que el usuario tenga instalado en su computadora el software.

9. Trabajo en Proceso:
   - El archivo `consecuencia_logicaNew.py` contiene información preliminar para implementar ejercicios de lenguaje natural simple.

10. Reinicio del Sistema:
   - `reinicia.cmd` reinicia todo el sistema, eliminando cualquier historial previo. Debe usarse con precaución. 
   - Este archivo está incluido sólo como auxiliar en las pruebas preliminares de los desarrolladores y no se espera que el usuario lo utilice.

---


### Estado Actual
Este prototipo se encuentra en fase de pruebas. 

---


### Instalación y Requerimientos

1. Python 3.x
2. DLV  (incluido en el proyecto) [Página principal](https://dlv.demacs.unical.it/home)
3. Sistema operativo compatible con los comandos `.cmd` (Windows)

---
