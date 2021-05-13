'''
14.Entrar com um número e escrever se ele é ou não divisível por 5.
'''
numero = float(input("Entre com o numero: "))

resto = numero % 5
valor = resto == 0
decisao = {True:"é divisível de 5", False:"não é divisível de 5"}
ehDivisivel = decisao[valor]
print(ehDivisivel)