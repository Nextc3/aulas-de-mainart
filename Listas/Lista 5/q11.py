'''
11. Entrar com um número se ele for igual ou maior que 20, escrever "o número é igual ou maior que 20,
se for menor "o número é menor que 20"

'''
numero = int(input("Entre com um numero: "))
dict_numero = {True:"o número é igual ou maior que 20", False: "o número é menor que 20"}
print(dict_numero[numero >= 20])