nome = input('Entre com o nome: ')
nota1 = int(input('Entre com a primeira nota: '))
nota2 = int(input('Entre com a segunda número: '))

media = (nota1 + nota2) / 2

aprovado = {
    True: 'aprovado', #media > 7
    False: 'em prova final' #antes de testar se foi reprovado
}
aprovacao = aprovado[media > 7]

reprovado = {
    True: 'reprovado', #media <= 3
    False: aprovacao #mantem o resultado anterior
}
aprovacao = reprovado[media <= 3]

print('Aluno(a) {}, com nota {}, e nota {}, e média {}, {}.'.format(nome, nota1, nota2, media, aprovacao))
