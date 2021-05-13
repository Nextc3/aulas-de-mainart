numero1 = int(input("Entre com o numero1: "))
numero2 = int(input("Entre com o numero2: "))
numero3 = int(input("Entre com o numero3: "))

lista_numero = [numero1, numero2, numero3]
lista_numero.sort()
print("Maior numero: {}".format(lista_numero[-1]))