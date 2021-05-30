'''

8.Chico tem
1.50m e cresce 2 centímetros por ano, enquanto Juca tem 1.10m e cresce 3
cm por ano. construir um programa que calcule e imprima quantos anos
serão necessários para Juca seja maior que Chico;

'''

chico = 1.5
juca = 1.1 
anos = 0 
while chico > juca:
    chico += 0.02
    juca += 0.03
    print("Idade de Chico: {}".format(chico))
    print("Idade de Juca: {}".format(juca))
    anos += 1

print(anos)