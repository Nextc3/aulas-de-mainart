'''
13. Entrar com um número e escrever uma das mensagens: “é múltiplo de 3", ou "não é múltiplo de 3"

'''

numero = int(input("Entre com o numero:"))

resto = numero % 3
valor = resto == 0
decisao = {True:"é múltiplo de 3", False:"não é múltiplo de 3"}
ehMultiplo = decisao[valor]
print(ehMultiplo)