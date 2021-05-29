
#1. Entrar como n's números e imprimir o triplo de cada. o programa encerra quando entrar com o numero 999;




numero = float(input("Entre com o numero: "))
while numero != 999:
    triplo = numero * 3
    print("Triplo do números: {}".format(triplo))
    numero = int(input("Entre com o numero: "))
print("Programa encerrado")