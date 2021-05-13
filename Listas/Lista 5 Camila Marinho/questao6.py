lista = []

numero1 = int(input('Entre com o primeiro número: '))
numero2 = int(input('Entre com o segundo número: '))
numero3 = int(input('Entre com o terceiro número: '))

lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
lista.sort()

print('Lista ordenada: {}, {}, {}'.format(lista[0],lista[1],lista[2]))
