print("Testando")

import speech_recognition as sr

import os

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #chama um algoritmo de reducao de ruidos
        microfone.adjust_for_ambient_noise(source)
        
        #frase para o usuario dizer algo
        print("Fale alguma coisa: ")
        
        #armazena o que foi dito em uma variavel
        audio = microfone.listen(source)
        
    try:
        
        #passa a variavel para o algoritmo reconhecedor de padroes
       frase = microfone.recognize_google(audio,language='pt-BR')
       
       if "navegador" in frase:
           os.system("start Opera.exe")
           
       elif "jogo" in frase:
           os.system("start Valorant.exe")
         
         #retorna a frase pronunciada
         print("Você disse: " + frase)
         
    #se nao reconheceu o padrao de fala, exibe a mensagem
   except sr.UnkownValueError:
       print("Não entendi")
       
    return frase

ouvir_microfone()