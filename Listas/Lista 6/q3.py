'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
Até 5 Kg Acima de 5 Kg
File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
Picanha R$ 6,90 por Kg R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da
promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no
cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva
um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom
fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''


tipoCarne = int(input("Insira o tipo de Carmne: File Duplo (1) Alcatra (2) Picanha(3): ")) 
quantidadeCarne = int(input("Entre com a quantidade(kg): "))
valorPorKilo = 0
if (quantidadeCarne > 5.0):
    valorPorKilo = valorPorKilo + 0.9
total = 1
if tipoCarne == 1:
    valorPorKilo = valorPorKilo + 4.9
elif tipoCarne == 2:
    valorPorKilo = valorPorKilo + 5.9
elif tipoCarne == 3:
    valorPorKilo = valorPorKilo + 6.9
else:
    print("Tipo informado incorretamente")
    quit()

total = valorPorKilo * quantidadeCarne
pagamento = int(input("Insira o tipo de pagamento. Dinheiro(1) Cartão Tabajara(2): "))
desconto = 0
aPagar = total
if pagamento == 2:
    desconto = total * 0.05
    aPagar = total - desconto

carne = {1:"Filé duplo", 2:"Alcatra", 3:"Picanha"}
dict_pagamento = {1:"Dinheiro", 2:"Cartão Tabajara"}
print("Cupom Fiscal:")
print("Tipo de pagamento: {}".format(dict_pagamento[pagamento]))
print("Tipo de carne: {}".format(carne[tipoCarne]))
print("Quantidade: {}".format(quantidadeCarne))
print("Valor total: {}".format(total))
print("Desconto: {}".format(desconto))
print("Valor a pagar: {}".format(aPagar))
