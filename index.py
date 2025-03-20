import time 

print("cronometro")
horas = input("digite as horas ")
minutos = input("digite os minutos ")
segundos = input("digite os segundos ")

tempo = input("Tempo {}h: {}m :{}s".format(horas, minutos, segundos))
dinal = time.ctime()

for t in range (1, horas - 1):
