'''
3) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será
classificado como "Inocente".
'''
perguntas = []

print("Responda Sim ou Não ")

reposta = input("Telefonou para a vítima? ")
if (reposta == "Sim") :
    perguntas.append(reposta)

reposta = input("Esteve no local do crime? ")
if (reposta == "Sim") :
    perguntas.append(reposta)

reposta = input("Mora perto da vítima? ")
if (reposta == "Sim") :
    perguntas.append(reposta)


reposta = input("Devia para a vítima? ")
if (reposta == "Sim") :    
    perguntas.append(reposta)

reposta = input("Já trabalhou com a vítima? ")
if (reposta  == "Sim") :
    perguntas.append(reposta)

positivas = len(perguntas)
respostasL = ["Inocente", "Inocente", "Suspeita", "Cúmplice", "Cúmplice","Assassino"]


print("Veredito: {}".format(respostasL[positivas]))
