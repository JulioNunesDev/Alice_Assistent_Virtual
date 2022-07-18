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
            comando = r.recognize_google(voz, language='pt-br')
            comando = comando.lower()
            print(comando)
            if 'alice' in comando:
                comando = comando.replace('alice', '')
                alice.say(comando)
                alice.runAndWait()

    except sr.UnknownValueError:
        alice.say('voce falou alguma coisa?, poderia repetir')
        alice.runAndWait()
        comando_voz_usuario()
    except sr.RequestError:
        alice.say('Desculpe nao conseguir completar a tarefa')
        alice.runAndWait()
        comando_voz_usuario()
    
    except:
        alice.say('seu microfone está desligado?')

    return comando

def comando_voz_usuario(valor):

    if 'horas' in valor:
        hora = datetime.now().strftime('%H:%M')
        alice.say('Agora são' + hora)
        alice.runAndWait()
    elif 'procure por' in valor:
        procurar = valor.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        alice.say(resultado)
        alice.runAndWait()
    elif 'toque' in valor:
        musica = valor.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        alice.say('Tocando música')
        alice.runAndWait()

value = True
while value:
    comando = executa_comando()
    comando_voz_usuario(comando)