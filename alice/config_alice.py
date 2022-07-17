from datetime import datetime
import os
import wikipedia
from random import Random, random
from unittest import result
from click import command
import gtts
import pyttsx3
import pywhatkit
import speech_recognition as sr


r = sr.Recognizer()
alice = pyttsx3.init()
own_name = 'Julio'


def voz_alice(text):
    texto = str(text)
    alice.say(texto)
    alice.runAndWait()


def executa_comando():
    try:
        with sr.Microphone() as source:
            alice.say('Ouvindo..')
            alice.runAndWait()
            print('Ouvindo...')
            voz = r.listen(source)
            comando = r.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            print(comando)
            if 'alice' in comando:
                comando = comando.replace('alice', '')
                alice.say(comando)
                alice.runAndWait()

    except:
        print('Microfone não está ok')
    

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.now().strftime('%H:%M')
        alice.say('Agora são' + hora)
        alice.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        alice.say(resultado)
        alice.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        alice.say('Tocando música')
        alice.runAndWait()



comando_voz_usuario()