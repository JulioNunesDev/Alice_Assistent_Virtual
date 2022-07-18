import os
import sys
from typing_extensions import Self
from gtts import gTTS, tts
import pyttsx3
import speech_recognition as sr



class Teste:
    def __init__(self, name, own):
        self.name = name
        self.own = own
        self.engine_alice = pyttsx3.init() 
        self.driver = sr.Recognizer()

    def init_alice(self, texto_string):
        text = str(texto_string)
        self.engine_alice.say(text)
        self.engine_alice.runAndWait()
    
    def centry(self):
        with sr.Microphone() as mic:
            voz = self.driver.listen(mic)

        try:
            commands = self.driver.recognize_google(voz, language='pt-br')

            if 'alice' in commands:
                self.init_alice('Olá meu senhor') 

        except sr.UnknownValueError:
          self.init_alice('Sinto muito senhor, nao foi possivel entender oque voçê disse, poderia repetir?')
        except sr.RequestError:
            self.init_alice('Sinto muito senhor, meu servidor está com problemas')

        return commands.lower()

alice  = Teste('Alice', 'Julio')

alice.centry()