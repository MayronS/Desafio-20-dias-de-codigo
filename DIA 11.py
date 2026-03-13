produto1 = input()
produto2 = input()

dividido1 = produto1.split()
dividido2 = produto2.split()

total = int(dividido1[1]) * float(dividido1[2]) + int(dividido2[1]) * float(dividido2[2])

print("VALOR A PAGAR: R$ {:.2f}".format(total))