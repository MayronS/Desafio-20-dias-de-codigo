saldoInicial = int(input())
saldo = saldoInicial
cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
cont1 = 0

while saldo > 0:
    
    if saldo >= 100:
        saldo = saldo - 100
        cont100+=1
    elif saldo < 100 and saldo >= 50:
        saldo = saldo - 50
        cont50+=1
    elif saldo < 50 and saldo >= 20:
        saldo = saldo - 20
        cont20+=1
    elif saldo < 20 and saldo >= 10:
        saldo = saldo - 10
        cont10+=1
    elif saldo < 10 and saldo >= 5:
        saldo = saldo - 5
        cont5+=1
    elif saldo < 5 and saldo >= 2:
        saldo = saldo - 2
        cont2+=1
    elif saldo < 2:
        saldo = saldo - 1
        cont1+=1

print(saldoInicial)
print("{} nota(s) de R$ 100,00".format(cont100))
print("{} nota(s) de R$ 50,00".format(cont50))
print("{} nota(s) de R$ 20,00".format(cont20))
print("{} nota(s) de R$ 10,00".format(cont10))
print("{} nota(s) de R$ 5,00".format(cont5))
print("{} nota(s) de R$ 2,00".format(cont2))
print("{} nota(s) de R$ 1,00".format(cont1))
    