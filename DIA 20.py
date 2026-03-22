tempoDuracao = int(input())

horas  = 0
minutos = 0
segundos = 0

while tempoDuracao > 0:
    if tempoDuracao >= 3600:
        tempoDuracao -= 3600
        horas += 1
    elif tempoDuracao >= 60:
        tempoDuracao -= 60
        minutos += 1
    else:
        segundos = tempoDuracao
        break

print("{}:{}:{}".format(horas,minutos,segundos))