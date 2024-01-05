from gtts import gTTS
from playsound import playsound
import os

# global variable to hold all the vocabulary
vocabulary = []
LANG = "fr"

def limpiaPantalla():
    os.system('clear')

def loadVocabulary():
    FILE_VOCABULARY = "vocabulary.txt"
    i = 0
    with open(FILE_VOCABULARY) as archivo:
        for linea in archivo:
            vocabulary[i] = linea 
            i=i+1 


limpiaPantalla()
loadVocabulary()

for word in vocabulary:
    tts = gTTS(text=word, lang=LANG, slow=False)
    tts.save("pronunciations/"+word+".mp3")

print("End---")
#playsound("pronunciations/test.mp3")
#os.remove("./pronunciations/test.mp3")