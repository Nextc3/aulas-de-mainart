emprestimo = {
    True: 'O empréstimo pode ser concedido.', #menor ou igual que 30%
    False: 'O empréstimo não pode ser concedido.' #maior que 30%
}

salario_bruto = float(input('Entre com o salário bruto: '))
prestacao = float(input('Entre com o valor da prestação: '))

porcentagem = prestacao / salario_bruto * 100

print(emprestimo[porcentagem <= 30])
