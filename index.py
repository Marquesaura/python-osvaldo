import time 

print("cronometro")
horas = input("digite as horas ")
horas  = int(horas)
minutos = input("digite os minutos ")
minutos = int(minutos)
segundos = input("digite os segundos ")
segundos = int(segundos)


iniciar = 0
iniciar = int(iniciar)
iniciar = input("Para começar, digite 1\nPara refazer, digite 2 ")
tempo = "Tempo {}h: {}m :{}s".format(horas, minutos, segundos)

def conferir():
    if (segundos > 60):
        print("digite um valor válido!")
    elif (minutos > 60):
        print("digite um valor válido!")
    elif (horas > 24):
        print("digite um valor válido!")


def comecar():
    segundos, minutos, horas
    if iniciar == 1:
        comecar()
        
    if iniciar == 2 :
        print(tempo)
    else:
        print ("inválido!")
        
    while segundos > 0:
        segundos = segundos - 1 
        print(tempo)
