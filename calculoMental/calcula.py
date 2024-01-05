import os
import random
import threading
import time
from gtts import gTTS
from playsound import playsound

multiplicandos = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
multiplicadores = [100,20,35,40,56,78,200,1000,500,250,75,10,30,40,80]
numPreguntas=""
respuesta=""
aciertos=0
errores=0
multiplicandosARepasar=[]

def limpiarPantalla():
    os.system('clear')

def counter(numSeconds):
    for i in range(int(numSeconds)):
        time.sleep(1)
    if respuesta == "":
        playsound("/Users/user1/workspace/calculoMental/endRing.mp3")
        
def pideNumPreguntas():
    limpiarPantalla()
    return input("Cuantas preguntas quieres que te haga?: ")

def createAudioFin():
    text = "Ops! se ha acabado el tiempo!"
    tts = gTTS(text=text, lang="es", slow=False)
    tts.save("/Users/user1/workspace/calculoMental/endRing.mp3")

def pideTimer():
    limpiarPantalla()
    return input("Cuantas segundos para contestar?: ")

def muestraReport():
    limpiarPantalla()
    print("**********************************")
    print("* ACIERTOS: " + str(aciertos))
    print("* ERRORES: "+ str(errores))
    print("**********************************")
    print("\n\n tienes que repasar las multiplicaciones con estos numeros...")

    for i in range(len(multiplicandosARepasar)):
        tablaConError = multiplicandosARepasar[i]
        print("\n Numero "+str(tablaConError))
        print("--------------")
        for j in range(13):
            print(str(tablaConError)+" x " + str(j) +" = " + str(tablaConError*j))

limpiarPantalla()
numPreguntas = pideNumPreguntas()
timer = pideTimer()
createAudioFin()

for i in range(int(numPreguntas)):
    limpiarPantalla()
    respuesta = ""
    multiplicando = multiplicandos[random.randint(0, len(multiplicandos)-1)]
    multiplicador = multiplicadores[random.randint(0, len(multiplicadores)-1)]
    t1 = threading.Thread(target=counter, args=(timer,))
    t1.start()
    respuesta = input(str(multiplicador) + " x " + str(multiplicando) + " = ")
    respuestaCorrecta = multiplicando*multiplicador
    if int(respuesta) == respuestaCorrecta:
        print("Ohhh yeah baby! sigue asi...")
        aciertos +=1
    else:
        print("Oooppss! la respuesta era: " + str(respuestaCorrecta))
        multiplicandosARepasar.append(multiplicador)
        errores +=1
    input("\n\nPulsa la tecla gorda (ENTER) para la siguiente pregunta...")

muestraReport()



    