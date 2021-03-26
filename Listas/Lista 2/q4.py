#Calcular o salario liquido de um professor. Os dados fornecidos serão: a) valor hora aula; b) numero de
#aulas dadas; c) percentual de desconto INSS.

valorHoraAula = float(input("Entre com o valor da hora aula "))
aulasDadaNoMes = int(input("Entre com a quantidade de aulas dadas no mês "))
inss = float(input("Entre com o percentual do inss em percentual "))

aux = valorHoraAula * aulasDadaNoMes
percentual = (inss / 100)
aux2 = aux * percentual
salario = aux  - aux2

print("Salário liquido será: {}".format(salario))

