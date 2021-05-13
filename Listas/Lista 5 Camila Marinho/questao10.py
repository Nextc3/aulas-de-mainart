segundo_turno = {
    True: 'Terá segundo turno.', #menor que 50%
    False: 'Não terá segundo turno.' #maior que 50%
}

municipio = input('Entre com o nome do município: ')
qtd_eleitores = int(input('Entre com o número de eleitores aptos: '))
qtd_votos = int(input('Entre com o número de votos do candidato mais votado: '))

porcentagem_votos = qtd_votos / qtd_eleitores * 100

print(segundo_turno[porcentagem_votos < 50])
