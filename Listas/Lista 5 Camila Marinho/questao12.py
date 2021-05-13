maior_20 = {
    True: 8, #maior que 20
    False: -5 #menor ou igual a 20
}

numero1 = int(input('Entre com o primeiro número: '))
numero2 = int(input('Entre com o segundo número: '))
soma = numero1 + numero2

print(soma + maior_20[soma > 20])
