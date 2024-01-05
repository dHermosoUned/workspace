import os
import random

tablasARepasar = []
numPreguntas=""
aciertos=0
errores=0
tablasConErrores=[]

def limpiarPantalla():
    os.system('clear')

def pideTablas():
    continuar=True
    while continuar:
        opcion = input("Que tabla quieres repasar? (Pulsa 'S' para salir): ")
        opcion = opcion.upper()
        if opcion == "S":
            continuar=False
        else:
            tablasARepasar.append(opcion)

def pideNumPreguntas():
    limpiarPantalla()
    return input("Cuantas preguntas quieres que te haga?: ")

def muestraReport():
    limpiarPantalla()
    print("**********************************")
    print("* ACIERTOS: " + str(aciertos))
    print("* ERRORES: "+ str(errores))
    print("**********************************")
    print("\n\n tienes que repasar estas tablas...")

    for i in range(len(tablasConErrores)):
        tablaConError = tablasConErrores[i]
        print("\nTabla del "+str(tablaConError))
        print("--------------")
        for j in range(13):
            print(str(tablaConError)+" x " + str(j) +" = " + str(tablaConError*j))

limpiarPantalla()
pideTablas()
numPreguntas = pideNumPreguntas()

for i in range(int(numPreguntas)):
    limpiarPantalla()
    multiplicando = random.randint(0,10)
    multiplicador = int(tablasARepasar[random.randint(0, len(tablasARepasar)-1)])
    respuesta = input(str(multiplicador) + " x " + str(multiplicando) + " = ")
    respuestaCorrecta = multiplicando*multiplicador
    if int(respuesta) == respuestaCorrecta:
        print("Ohhh yeah baby! sigue asi...")
        aciertos +=1
    else:
        print("Oooppss! la respuesta era: " + str(respuestaCorrecta))
        tablasConErrores.append(multiplicador)
        errores +=1
    input("\n\nPulsa la tecla gorda (ENTER) para la siguiente pregunta...")

muestraReport()



    