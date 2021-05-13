maior_20 = {
    True: 'O número é igual ou maior que 20.',
    False: 'O número é menor que 20.'
}

numero = int(input('Entre com um número: '))
print(maior_20[numero >= 20])
