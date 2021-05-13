'''
Escreva um programa para armazenar uma agenda de 10 telefones em um dicionário. Cada pessoa
pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve
ter as seguintes funções:
-incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou
mais telefones. Ela deve receber como argumentos o nome e os telefones.
-incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda.
Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja
incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo
nome.
-excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a
pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
-excluirNome – essa função exclui uma pessoa da agenda.
-consultarTelefone – essa função retorna os telefones de uma pessoa na agenda
'''
nome = input("Digite nome: ")
numero = 0
agenda = {
    input("Digite nome {}: ".format(1)) : input("Digite telefone: {}".format(1)),
    input("Digite nome {}: ".format(numero + 2)) : input("Digite telefone: {}".format(2)),
    input("Digite nome {}: ".format(numero = numero + 1)) : input("Digite telefone: {}".format(3)),
    input("Digite nome {}: ".format(4)) : input("Digite telefone: {}".format(4)),
    input("Digite nome {}: ".format(5)) : input("Digite telefone: {}".format(5)),
    input("Digite nome {}: ".format(6)) : input("Digite telefone: {}".format(6)),
    input("Digite nome {}: ".format(7)) : input("Digite telefone: {}".format(7)),
    input("Digite nome {}: ".format(8)) : input("Digite telefone: {}".format(8)),
    input("Digite nome {}: ".format(9)) : input("Digite telefone: {}".format(9)),
    input("Digite nome {}: ".format(10)) : input("Digite telefone: {}".format(10)),
}
excluir = input("Deseja excluir um telefone pelo nome? Sim ou Não")
if(excluir == "Sim"):
    nomeExcluir = input("Qual o nome? ")
    del (agenda[nomeExcluir])
excluir = input("Deseja excluir um telefone pelo telefone? Sim ou Não")
if(excluir == "Sim"):
    telefoneExcluir = input("Qual o telefone? ")
    del (agenda[telefoneExcluir])
print(agenda)