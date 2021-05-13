'''
15.A prefeitura do Rio de Janeiro abriu uma linha de crédito para seus funcionários. O valor máximo da
prestação não poderá ultrapassar 30% do salário bruto. Fazer um programa que permita entrar com o
salário bruto e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
'''

salarioBruto = int(input("Entre com o salario Bruto: "))
prestacao = int(input("Entre com o valor da prestação: "))
limite = salarioBruto * 0.3



dict_emprestimo = {True:"Pode ser concedido", False:"Não pode ser concedido"}
podeEmprestimo = dict_emprestimo[limite > prestacao]
print(podeEmprestimo)