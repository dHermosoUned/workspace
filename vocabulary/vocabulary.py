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
languages = {"F":"fr", "D": "de", "I":"en"}

DEFAULT_LANG = "fr"
GLOBAL_PATH = script_dir = os.path.dirname(__file__)

def limpiaPantalla():
    os.system('cls')

def loadVocabulary(file="vocabulary.txt"):
    FILE_VOCABULARY = GLOBAL_PATH +"\\"+ file
    print(FILE_VOCABULARY)
    i = 0
    with open(FILE_VOCABULARY, encoding='utf-8') as reader:
        for line in reader.readlines():
            vocabulary[i] = str(line).strip()
            i = i+1

def createAudios(language=DEFAULT_LANG):
    for index in vocabulary:
        linea = vocabulary[index]
        print(linea)
        text = str(linea).split(" = ")[0]
        print(text)
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(GLOBAL_PATH + "/pronunciations/"+language+"/"+str(index)+".mp3")
        print("grabado en index", index)

def askQuestions(language=DEFAULT_LANG):
    global aciertos
    global errores
    global numPreguntas
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
        respuestaCorrectaLinea = vocabulary[randIndexAudio]
        respuestaCorrecta = str(respuestaCorrectaLinea).split(" = ")[1]
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
    coef = errores / int(numPreguntas)
    reduccion = 1-coef
    nota = reduccion * 6
    print("********************* RESULTADOS *****************")
    print("***** ACIERTOS: " + str(aciertos) + " ********************************")
    print("***** ERRORES: " + str(errores) + " ********************************")
    print("***** Has sacado un: " + str(float(nota) ))
    print("*************************************************")

def cleanUp():
    lista_ficheros = os.listdir(GLOBAL_PATH + "/pronunciations")
    for fichero in lista_ficheros:
        if fichero.endswith(".mp3"):
            os.remove(GLOBAL_PATH + "/pronunciations/" + fichero)
        
def main():
    cleanUp()
    lang = input("En que idioma quieres practicar?: \n\n [F] Francais \n [D] Deutsch \n [I] Ingles \n\n [X] Salir \n\n Elige una opcion: ").upper()
    if lang == "X":
        exit()

    vocabularyFile = input("Dime como se llama el vocabulario a repasar: ").lower()

    limpiaPantalla()
    loadVocabulary(vocabularyFile)
    print("creando audios...")
    createAudios(languages[lang])
    print("audios creados...")
    #limpiaPantalla()
    askQuestions(languages[lang])
    #limpiaPantalla
    printReport()

if __name__ == "__main__":
    main()