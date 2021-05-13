maior = 0
menor = 0
intermediario = 0
numero1 = int(input("Entre com o numero1: "))
numero2 = int(input("Entre com o numero2: "))
numero3 = int(input("Entre com o numero3: "))
lista_numero = [numero1,numero2,numero3]
lista_numero.sort()
menor = lista_numero[0]
intermediario = lista_numero[1]
maior = lista_numero[2]

print("Numeros - maior {} intermediário {} menor {}".format(maior, intermediario, menor))