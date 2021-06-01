'''
9.Uma empresa de
fornecimento de energia elétrica faz a leitura mensal dos medidores de
consumo. para cada consumidor, são digitados os seguintes dados:
a)Numero do consumidor; b)Quantidade de kWh consumidos durante o mês; c)
tipo do consumidor -> 1-residencial, preço em reias de kWh = 0,3 /
2-comercial, preço em reias de kWh = 0,5 / 3-industrial, preço em reias
de kWh = 0,7. Os dados devem ser lidos ate que seja encontrado um
consumidor com numero 0(zero). calcular e imprimir: a) o custo total
para cada consumidor; b)o total de consumo para os 3(três) tipos de
consumidor; c)a media de consumo dos tipos 1 e 2.

'''


listaConsumidores = []
consumidor = {
    "consumo": 0,
    "tipo": 0,
    "numero": -1,
}

consumoBruto = 0

quantidadeResidencial = 0
quantidadeComercial = 0
mediaResidencial = 0
mediaComercial = 0

totalAcumuladoComercial = 0
totalAcumuladoResidencia = 0
totalAcumuladoIndustrial = 0
numero = -1
while numero != 0:
    
    numero = int(input("Entre com o número do consumidor: "))
    if (numero == 0):
        break
    consumidor["numero"] = numero
    consumoBruto = int(input("Entre com o consumo: "))
    consumidor["tipo"] = int(input("Entre com o tipo: "))
    if (consumidor["tipo"] == 1):
        consumidor["consumo"] = consumoBruto * 0.3
        totalAcumuladoResidencia += consumidor["consumo"]
        quantidadeResidencial += 1
    elif (consumidor["tipo"] == 2):
        consumidor["consumo"] = consumoBruto * 0.5
        totalAcumuladoComercial += consumidor["consumo"]
        quantidadeComercial += 1
    elif (consumidor["tipo"] == 3):
        consumidor["consumo"] = consumoBruto * 0.7 
        totalAcumuladoIndustrial += consumidor["consumo"]

    print("Total de consumo: {}".format(consumidor["consumo"]))
    listaConsumidores.append(consumidor)
    
    
    
print("Tamanho da lista de consumidores: {}".format(len(listaConsumidores)))    
mediaResidencial = totalAcumuladoResidencia / quantidadeResidencial
mediaComercial = totalAcumuladoComercial / quantidadeComercial
print("Total de consumo: Residencial = {}\nComercial = {}\nIndustrial = {}".format(totalAcumuladoResidencia,totalAcumuladoComercial,totalAcumuladoIndustrial))

print("Media de consumo: Residencial = {}\nCcomercial = {}".format(mediaResidencial,mediaComercial))
print(listaConsumidores)