#Entrar com valor de um empréstimo, a taxa de juros e a quantidade de meses. Fazer um programa que
#calcule o valor da prestação.

emprestimo = float(input("Entre com o valor do empréstimo: "))
taxa = float(input("Entre com a taxa de juros: "))
meses = int(input("Entre com a quantidade de meses: "))

prestacaoSemJuros = emprestimo / meses
aux = prestacaoSemJuros * (taxa / 100)
prestacao = prestacaoSemJuros + aux
total = prestacao * meses 

print("Valor da prestação a pagar: {}".format(prestacao))
print("Valor do total: {}".format(total))
