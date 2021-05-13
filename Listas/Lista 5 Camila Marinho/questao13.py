multiplo_3 = {
    True: 'É múltiplo de 3.',
    False: 'Não é múltiplo de 3.'
}

numero = int(input('Entre com um número: '))
resto = numero % 3

print(multiplo_3[resto == 0])
