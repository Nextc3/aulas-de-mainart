nome = input('Entre com um nome: ')
idade = int(input('Entre com a idade: '))
sexo = input('Entre com o sexo (F/M): ')

aceitacao = {
    True: 'ACEITA.',
    False: 'NÃO ACEITA.'
}

print(aceitacao[(idade < 25) and (sexo == 'F')])
