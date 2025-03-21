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

tempo = "Tempo {}h: {}m :{}s".format(horas, minutos, segundos)

if (segundos > 60):
        print("digite um valor válido!")
elif (minutos > 60):
        print("digite um valor válido!")
elif (horas > 24):
        print("digite um valor válido!")
        
def ir(): 
    global segundos, minutos, horas
    while segundos > 0:
        segundos = segundos - 1 
        print(tempo)
        break

iniciar = input("Para começar, digite 1\nPara refazer, digite 2 ")
def comecar():
    global segundos, minutos, horas
    if iniciar == 1:
        ir()
    
    elif iniciar == 2:
        return tempo
    else:
        print ("inválido!")
        return tempo
