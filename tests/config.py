import os
import sys
from typing_extensions import Self
from gtts import gTTS, tts
import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia



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
    
    def centry(self, ask=''):
        with sr.Microphone() as mic:
            if ask:
                self.init_alice(ask)
            voz = self.driver.listen(mic, 2, 5)
                
        self.init_alice('fazendo reconhecimento de voz')
        try:
            commands = self.driver.recognize_google(voz, language='pt-BR')
          

        except sr.UnknownValueError:
          self.init_alice('Sinto muito senhor, nao foi possivel entender oque voçê disse, poderia repetir?')
        except sr.RequestError:
            self.init_alice('Sinto muito senhor, meu servidor está com problemas')

        return commands.lower()
    
   


    def exec(self, voz_data):

        if 'toque' in voz_data:
            cmd = voz_data.replace('toque', '')
            result = pywhatkit.playonyt(cmd)
            print('tocando...')
            

        elif 'procurar por' in voz_data:
            cmd = voz_data.replace('procurar por', '')
            wikipedia.set_lang('pt')
            result = wikipedia.summary(cmd, 2)
            print(result)
            self.init_alice(result)

   
            
        

    

alice  = Teste('Alice', 'Julio')


voz = alice.centry('em que posso ajudar, senhor?')
alice.exec(voz)