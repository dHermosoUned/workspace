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
languages = {"F":"fr", "D": "de"}

DEFAULT_LANG = "fr"
GLOBAL_PATH = "/Users/user1/workspace/vocabulary"

def limpiaPantalla():
    os.system('clear')

def loadVocabulary(file="vocabulary.txt"):
    FILE_VOCABULARY = GLOBAL_PATH +"/"+ file
    i = 0
    with open(FILE_VOCABULARY) as archivo:
        for linea in archivo:
            vocabulary[i] = str.strip(linea)
            i=i+1 

def createAudios(language=DEFAULT_LANG):
    for index in vocabulary:
        text = vocabulary[index]
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(GLOBAL_PATH + "/pronunciations/"+language+"/"+str(index)+".mp3")

def askQuestions(language=DEFAULT_LANG):
    global aciertos
    global errores
    numPreguntas = input("Combien de questions veux-tu?: ")
    checkCaseSensitive=False
    if numPreguntas == 0:
        exit()

    limpiaPantalla
    input("\n\nVoy a comenzar a dictarte palabras. Pulsa la tecla gorda (ENTER) para comenzar...")
    for i in range(int(numPreguntas)):
        randIndexAudio = random.randint(0,len(vocabulary)-1)
        playsound(GLOBAL_PATH + "/pronunciations/"+language+"/"+str(randIndexAudio)+".mp3")
        respuesta = input("Escribe lo que has oido: ")
        respuestaCorrecta = vocabulary[randIndexAudio]
        if(language == "de"):
            checkCaseSensitive = True

        if(checkCaseSensitive == False):
            if respuesta.strip().casefold() == str(respuestaCorrecta).casefold():
                print("Correcto! sigues asi")
                aciertos=aciertos+1
            else:
                print("Meeeeeec... error, el resultado correcto era ("+respuestaCorrecta+") intenta mejorar...")
                errores=errores+1
        else:
            if respuesta.strip() == str(respuestaCorrecta):
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
        if fichero.endswith(".mp3"):
            os.remove(GLOBAL_PATH + "/pronunciations/" + fichero)
        
def main():
    cleanUp()
    lang = input("En que idioma quieres practicar?: \n\n [F] Francais \n [D] Deutsch \n\n [X] Salir \n\n Elige una opcion: ").upper()
    if lang == "X":
        exit()

    vocabularyFile = input("Dime como se llama el vocabulario a repasar: ").lower()

    limpiaPantalla()
    loadVocabulary(vocabularyFile)
    createAudios(languages[lang])
    limpiaPantalla()
    askQuestions(languages[lang])
    limpiaPantalla
    printReport()

if __name__ == "__main__":
    main()