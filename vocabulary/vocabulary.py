from gtts import gTTS
from playsound import playsound
import os
import random

# global variable to hold all the vocabulary
vocabulary = {}
#Para el report del final
aciertos=0
errores=0
numPreguntas=0
LANG = "fr"
GLOBAL_PATH = "/Users/user1/workspace/vocabulary"

def limpiaPantalla():
    os.system('clear')

def loadVocabulary():
    FILE_VOCABULARY = GLOBAL_PATH + "/vocabulary.txt"
    i = 0
    with open(FILE_VOCABULARY) as archivo:
        for linea in archivo:
            vocabulary[i] = str.strip(linea)
            i=i+1 

def createAudios():
    for index in vocabulary:
        text = vocabulary[index]
        tts = gTTS(text=text, lang=LANG, slow=False)
        tts.save(GLOBAL_PATH + "/pronunciations/"+str(index)+".mp3")

def askQuestions():
    global aciertos
    global errores
    numPreguntas = input("Combien de questions veux-tu?: ")
    limpiaPantalla
    input("\n\nVoy a comenzar a dictarte palabras. Pulsa la tecla gorda (ENTER) para la siguiente pregunta...")
    for i in range(int(numPreguntas)):
        randIndexAudio = random.randint(0,len(vocabulary)-1)
        playsound(GLOBAL_PATH + "/pronunciations/"+str(randIndexAudio)+".mp3")
        respuesta = input("Escribe lo que has oido: ")
        respuestaCorrecta = vocabulary[randIndexAudio]
        if respuesta == respuestaCorrecta:
            print("Correcto! sigues asi")
            aciertos=aciertos+1
        else:
            print("Meeeeeec... error, el resultado correcto era ("+respuestaCorrecta+") intenta mejorar...")
            errores=errores+1

def printReport():
    print("********************* RESULTADOS *****************")
    print("***** ACIERTOS: " + str(aciertos) + " ********************************")
    print("***** ERRORES: " + str(errores) + " ********************************")
    print("***** Has sacado un: " + str(6-(errores/aciertos)*int(numPreguntas)) )
    print("*************************************************")


def main():
    limpiaPantalla()
    loadVocabulary()
    createAudios()
    limpiaPantalla()
    askQuestions()
    limpiaPantalla
    printReport()

if __name__ == "__main__":
    main()

#playsound("pronunciations/test.mp3")
#os.remove("./pronunciations/test.mp3")