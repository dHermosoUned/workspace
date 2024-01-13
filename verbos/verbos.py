import os
import random

# variables globales
pronombres = {}
tiempos  = {"P":"Presente", "I":"Imperfait", "F":"Future", "C":"Passé Composé"}
opciones = {"P" : "Presente", "I" : "Imperfecto", "F": "Futuro", "C" : "PasseComposse" , "E" : "ModeTest", "X" : "Salir"}
opcion=""
tiemposConVerbsConjugados = {}
verbsConjugados = {}
#Contiene todos los posibles verbos a preguntar para un tiempo verbal dado.
verbs = []
#Para el report del final
aciertos=0
errores=0

def limpiaPantalla():
    os.system('clear')

def getPronombre(randPronombreIndex):
    pronombresList = pronombres[randPronombreIndex]
    randPronombre = pronombresList[random.randint(0,len(pronombresList)-1)]
    return randPronombre

def cargaPronombres():
    FILE_PRONOMBRES = "/Users/user1/workspace/verbos/pronombres.txt"
    i = 0
    with open(FILE_PRONOMBRES) as archivo:
        for linea in archivo:
            pronombres[i] = linea.rstrip().split(',') 
            i=i+1 
        
def cargaTodosVerbos():
    #load all verbs from all tenses
    for opcion in opciones:
        if opcion != "E" and opcion != "X":
            tiemposConVerbsConjugados[opcion] = cargaVerbos(opcion)

def cargaVerbos(opt):
    #load all verbs
    vc = {}
    VERBS_FOLDER = "/Users/user1/workspace/verbos/verbos/"+opciones[opt]
    with os.scandir(VERBS_FOLDER) as ficheros:
        for fichero in ficheros:
            fileName = fichero.name.split('.')[0]
            verbs.append(fileName)

            #load conjugations
            with open(fichero) as archivo:
                for linea in archivo:
                    vc[fileName] = linea.split(',')  
    return vc                        

limpiaPantalla()
cargaPronombres()

#Pregunta por el tiempo verbal
while opcion not in opciones:
    opcion = input("Que tiempo verbal quieres estudiar? \n [P] Presente \n [I] Imperfecto \n [F] Futuro \n [C] Passé Composé \n [E] Mode Test \n\n [X] para salir: " ).upper()
    
opcion=opcion.upper()
if opcion == "X": 
    exit()
    
#limpiaPantalla()
if opcion == "E":
    cargaTodosVerbos()
else:
    verbsConjugados = cargaVerbos(opcion)

numVerbs = len(verbs)
numPreguntas = input("Cuantas preguntas quieres responder? : ")

    
limpiaPantalla()
for i in range(int(numPreguntas)):
    randPronombreIndex = random.randint(0,5)
    randPronombre = getPronombre(randPronombreIndex)
    respuesta=""
    respuestaCorrecta=""
    if opcion == "E":
        randTenseIndex = random.randint(0,len(tiempos)-1)
        tiempo = list(tiempos)[randTenseIndex]
        randVerboIndex = random.randint(0,len(tiemposConVerbsConjugados[tiempo])-1)
        verboSeleccionado = list(tiemposConVerbsConjugados[tiempo])[randVerboIndex]
        respuesta = input("Pregunta #"+str(i)+" "+randPronombre+" ["+ verboSeleccionado +"] en ["+tiempos[tiempo]+"]: ")
        respuestaCorrecta = tiemposConVerbsConjugados[tiempo][verboSeleccionado][randPronombreIndex]
    else:
        randVerboIndex = random.randint(0,len(verbs)-1)
        respuesta = input("Pregunta #"+str(i)+" "+randPronombre+" ["+ verbs[randVerboIndex] +"]: ")
        verboSeleccionado = verbs[randVerboIndex]
        respuestaCorrecta = verbsConjugados[verboSeleccionado][randPronombreIndex]

    if respuesta == respuestaCorrecta:
        print("Correcto! sigues asi")
        aciertos=aciertos+1
    else:
        print("Meeeeeec... error, el resultado correcto era ("+respuestaCorrecta+") intenta mejorar...")
        errores=errores+1

limpiaPantalla()
print("********************* RESULTADOS *****************")
print("***** ACIERTOS: " + str(aciertos) + " ********************************")
print("***** ERRORES: " + str(errores) + " ********************************")
print("***** Has sacado un: " + str(6-(errores/aciertos)*int(numPreguntas)) )
print("*************************************************")


