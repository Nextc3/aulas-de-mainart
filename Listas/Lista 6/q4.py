'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
b. até 20 litros, desconto de 3% por litro
c. acima de 20 litros, desconto de 5% por litro
d. Gasolina:
e. até 20 litros, desconto de 4% por litro
f. acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool
é R$ 1,90.

'''
dict_valorCombustivel = {"A":1.9, "G":2.5}
combustivel = input("Escreva qual tipo de combustivel. Álcool(A) Gasolina(G): ")
litrosVendidos = int(input("Escreva número litros vendidos: "))
desconto = 0

if (combustivel == "A") and (litrosVendidos <= 20):
    desconto = 0.03
elif (combustivel == "A") and not(litrosVendidos <= 20):
    desconto = 0.05
elif (combustivel == "G") and (litrosVendidos <= 20):
    desconto = 0.04
elif (combustivel == "G") and not(litrosVendidos <=20):
    desconto = 0.06
dict_valorCombustivel[combustivel] = dict_valorCombustivel[combustivel] - (dict_valorCombustivel[combustivel] * desconto)
total = litrosVendidos * (dict_valorCombustivel[combustivel])

print("Desconto de: {}".format(desconto * 100))
print("Preço do combustivel liquido: {}".format(dict_valorCombustivel[combustivel]))
print("Valor a ser pago: {}".format(total))