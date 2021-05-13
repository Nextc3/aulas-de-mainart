'''
10. sabendo-se que somente os municípios que possuem mais de 20 mil eleitores
aptos tem segundo turno nas eleições para prefeito caso o primeiro colocado
não tenha mais do que 50% DOS VOTOS. FAZER UM PROGRAMA QUE LEIA O NOME do município, a
quantidade de eleitores aptos, o número de votos do candidato mais votado e informar se ele terá ou não
segundo turno.
'''
nome = input("Entre com o nome do municipio: ")
eleitores = int(input("Entre com quantidade de eleitores aptos: "))
votosDoCandi = int(input("Entre com os votos dos candidato mais votado: "))

decisao = {True:"Sim", False:"Não"}

eleitores50 = eleitores * 0.5



segundoTurno = decisao[((eleitores > 20000) and (eleitores50 > votosDoCandi))]





print("Terá segundo turno: {}".format(segundoTurno))
