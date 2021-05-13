divisivel_5 = {
    True: 'É divisível por 5.',
    False: 'Não é divisível por 5.'
}

numero = int(input('Entre com um número: '))
resto = numero % 5

print(divisivel_5[resto == 0])
