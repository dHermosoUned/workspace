from gtts import gTTS
from playsound import playsound
import os

textToTranslate = input("Dit moi une phrase s'il te plait: ")
lang = "fr"

tts = gTTS(text=textToTranslate, lang=lang, slow=False)

tts.save("pronunciations/test.mp3")
playsound("pronunciations/test.mp3")

os.remove("./pronunciations/test.mp3")