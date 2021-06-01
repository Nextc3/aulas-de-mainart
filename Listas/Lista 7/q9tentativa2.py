'''
9.Uma empresa de
fornecimento de energia elétrica faz a leitura mensal dos medidores de
consumo. para cada consumidor, são digitados os seguintes dados:
a)Numero do consumidor; 
b)Quantidade de kWh consumidos durante o mês; 
c)tipo do consumidor -> 
    1-residencial, preço em reias de kWh = 0,3 /
    2-comercial, preço em reias de kWh = 0,5 / 
    3-industrial, preço em reias de kWh = 0,7.
 Os dados devem ser lidos ate que seja encontrado um
consumidor com numero 0(zero). calcular e imprimir: 
a) o custo total para cada consumidor; 
b)o total de consumo para os 3(três) tipos de
consumidor; 
c)a media de consumo dos tipos 1 e 2.

'''

consumidores = {}


tipos = {
    1:"Residencial",
    2:"Comercial",
    3:"Industrial"

}
cobrancas = {
    1 : 0.3,
    2 : 0.5,
    3 : 0.7
}



medias = {
    1:0,
    2:0
    }
numero = -1
while numero != 0:
    numero = int(input("Entre com o numero do consumidor: "))
    consumidores [numero] = {
        "tipo": int(input("Entre com o tipo: ")),
        "consumo":int(input("Enre com o consumo: "))

    }
del consumidores[0]
consumoAcumulado = {
    1: 0,
    2: 0,
    3: 0

}
quantidade = {
    1:0,
    2:0
}

for chave,consumidor in consumidores.items():
    
    consumoAcumulado[consumidor["tipo"]] += consumidor["consumo"]
    if (consumidor["tipo"] != 3):
        quantidade[consumidor["tipo"]] += 1
    consumidor["custo"] = consumidor["consumo"] * cobrancas[consumidor["tipo"]]
    print("Consumidor {} consumo {}kw/h tipo {} custo {}".format(chave,consumidor["consumo"],consumidor["tipo"],consumidor["custo"]))


medias[1] = consumoAcumulado[1] / quantidade[1]
medias[2] = consumoAcumulado[2] / quantidade[2]



print("Total de Consumo: Residencial {} Comercial {} Industrial {}".format(consumoAcumulado[1],consumoAcumulado[2], consumoAcumulado[3]))
print("Média de consumo: Residencial {} Comercial {}".format(medias[1],medias[2]))

