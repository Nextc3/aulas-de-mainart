#Calcular a quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12km
#com 1 litro. Deverão. Ser fornecidos a) tempo gasto na viagem; b) e a velocidade media. Apresentar os
#valores da velocidade media, tempo gasto, distancia percorrida e quatidade de litros gastos.

tempoGasto = float(input("Entre com o tempo gasto em horas "))
velocidadeMedia = float(input("Entre com a velocidade media em km por horas "))
distancia = tempoGasto * velocidadeMedia

print("Velocidade média: {}".format(velocidadeMedia))
print("Tempo gasto: {}".format(tempoGasto))
print("Distância(km): {}".format(distancia))
print("Combustível gasto: {}".format(distancia / 12))

