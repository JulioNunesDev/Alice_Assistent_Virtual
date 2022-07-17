from datetime import datetime
from email.mime import audio
import webbrowser

import pywhatkit
import speech_recognition as sr
import playsound
from gtts import gTTS, tts
import random
import pyttsx3
import os
import wikipedia


class AssistentAlice:
    def __init__(self, name_assistent, name_own):
        self.name_assistent = name_assistent
        self.name_own = name_own

        self.alice = pyttsx3.init()
        self.google = sr.Recognizer()
        self.data_voice = ''

    def alice_voz_dela(self, text):
        """
        Fala da alice virtual
        """
        text = str(text)
        self.alice.say(text)
        self.alice.runAndWait()
    
    def gravando_voz(self, pergunte=''):


        with sr.Microphone() as source:
            if pergunte:
                print('Gravando...')
                self.alice_voz(pergunte)

            audio = self.google.listen(source, 3, 3)
            print('Procurando no banco de dados')

            try:
                self.data_voice = self.google.recognize_google(audio, language='pt-BR')
            except sr.UnknownValueError:
                self.alice_voz('Sinto muito senhor, nao foi possivel entender oque voçê disse, poderia repetir?')

            except sr.RequestError:
                self.alice_voz('Sinto muito senhor, meu servidor está com problemas')
            
            print('>>', self.data_voice.lower())
            self.data_voice = self.data_voice.lower()

            return self.data_voice.lower()

    def alice_voz(self, audio_str):
        audio_strs = str(audio_str)
        tts = gTTS(text=audio_strs, lang='pt')
        r = random.randint(1, 20000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.name_assistent + ':' + audio_str)
        os.remove(audio_file)


    def com_termos(self, termos):
        for term in termos:
            if term in self.data_voice:
                return True


    def resposta(self, voice_data):
        if self.com_termos(['ei', 'ola', 'oi', 'hello', 'hi']):
            boasVindas = [f'Olá {self.name_own}, O que voce deseja hoje?',
            'olá meu senhor, em que posso ajudar ?',
            'bem vindo de volta senhor, posso ajudar em algo?']

            boas = boasVindas[random.randint(0, len(boasVindas)-1)]

            self.alice_voz(boas)

            #google comandos

            

            if self.com_termos(['toque']):
                result = voice_data.split('toque')[-1]
                url = pywhatkit.playonyt(result)
               

    

assitent = AssistentAlice('Alice', 'Julio')

while True:
    voz_comando = assitent.gravando_voz('Escutando...')
    assitent.resposta(voz_comando)

    if assitent.com_termos(['bye', 'tchau', 'adeus', 'ate mais']):
        assitent.alice_voz_dela('Tenha um bom dia senhor!')
        break