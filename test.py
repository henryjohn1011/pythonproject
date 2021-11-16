

import os
from typing import Text
import playsound
import speech_recognition as sr
import wikipedia
import pyttsx3
from gtts import gTTS
from typing import Text



def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")
speak("hello")