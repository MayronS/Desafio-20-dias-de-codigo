nomeVendedor = input()
salarioF = float(input())
totalV = float(input())

comissao = totalV * 0.15

salTotal = comissao + salarioF

print("TOTAL = R$ {:.2f}".format(salTotal))