nome = input("Entre com o nome: ")
idade = int(input("Entre com a idade: "))
sexo = input("Entre com o sexo. (M)asculino. (F)eminino: ")
sexo = (sexo == "F") #Convertendo a variável pra bool devido a só dois valores possíveis
aceitando = {True:"ACEITA", False:"NÃO ACEITA"}
print("Nome: {}".format(nome))
print("Idade: {}".format(idade))
print(aceitando[(idade < 25) and sexo])
