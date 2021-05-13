lucro = {
    True: 45, #menor que 20
    False: 30 #maior que 20
}
valor_compra = float(input('Entre com o valor do produto: '))
porcentagem_lucro = lucro[valor_compra < 20] / 100
valor_venda = valor_compra + valor_compra * porcentagem_lucro

print('Valor da venda: {}.'.format(valor_venda))

