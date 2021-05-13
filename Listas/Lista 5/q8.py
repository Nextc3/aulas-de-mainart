'''
entrar com o nome, nota 1 e nota 2 de um aluno, imprimir nome, Nota1, nota2, média e a mensagem
aprovado, reprovado ou em prova final. (a média é 7 para aprovado, 3 para reprovado, e as demais para
prova final.
'''

aluno = {
    "nome":input("Entre com nome"),
    "nota1":int(input("Entre com nota 1: ")),
    "nota2":int(input("Entre com nota 2: ")),
    "media": 0.0,
    "mensagem":{True:""}

}
aluno["media"] = (aluno["nota1"] + aluno["nota2"])/2

aluno["mensagem"][(aluno["media"] >= 7)] = "Aprovado"
aluno["mensagem"][(aluno["media"] <= 3)] = "Reprovado"
aluno["mensagem"][(aluno["media"] < 7) and (aluno["media"] > 3)] = "Prova Final"

print("Nome: {}".format(aluno["nome"]))
print("Nota1: {}".format(aluno["nota1"]))
print("Nota2: {}".format(aluno["nota2"]))
print("Média: {}".format(aluno["media"]))
print("Mensagem: {}".format(aluno["mensagem"][True]))


