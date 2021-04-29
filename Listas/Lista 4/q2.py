#2. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana,
#tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo
#recebem listas vazias, ou você tem aula?).

semana = {}
semana["domingo"] = ["chaincode"]
semana["segunda"] = ["arquitetura de software"]
semana["terça"] = ["golang","infra hyperledger"]
semana["quarta"] = ["chaincode","infra hyperledger"]
semana["quinta"] = ["python", "arquitetura de software", "sistemas distribuídos"]
semana["sexta"] = ["chaincode","golang"]
semana["sábado"] = ["chaincode","golang"]

print (semana)