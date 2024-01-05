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
    if numPreguntas == 0:
        exit()

    limpiaPantalla
    input("\n\nVoy a comenzar a dictarte palabras. Pulsa la tecla gorda (ENTER) para comenzar...")
    for i in range(int(numPreguntas)):
        randIndexAudio = random.randint(0,len(vocabulary)-1)
        playsound(GLOBAL_PATH + "/pronunciations/"+str(randIndexAudio)+".mp3")
        respuesta = input("Escribe lo que has oido: ")
        respuestaCorrecta = vocabulary[randIndexAudio]
        if respuesta.casefold() == str(respuestaCorrecta).casefold():
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

def cleanUp():
    lista_ficheros = os.listdir(GLOBAL_PATH + "/pronunciations")
    for fichero in lista_ficheros:
        print(str(fichero))
        if fichero.endswith(".mp3"):
            print("borrando")
            os.remove(GLOBAL_PATH + "/pronunciations/" + fichero)
        
def main():
    cleanUp()
    limpiaPantalla()
    loadVocabulary()
    createAudios()
    limpiaPantalla()
    askQuestions()
    limpiaPantalla
    printReport()

if __name__ == "__main__":
    main()