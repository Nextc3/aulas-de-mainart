'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que
custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
• Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
em 3 situações:
• comprar apenas latas de 18 litros;
• comprar apenas galões de 3,6 litros;
• misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

areaPintada = int(input("Escreva a área pintada"))
tintasAComprar = {"latas":0, "galoes":0}
# 1 litro pra 6 metros
#lata 18 litros . 80 reais a lata
#galoes 3,6. 25
litros = areaPintada / 6
litros = litros + (litros * 0.1) #folga 

tintasAComprar["latas"] = litros // 18
resto = litros % 18
if (litros % 18) != 0:
    tintasAComprar["latas"] = tintasAComprar["latas"] + 1
    aviso = True
print("Só em latas {}. Total {}".format(tintasAComprar["latas"], tintasAComprar["latas"] * 80))

tintasAComprar["galoes"] = litros // 3.6
resto =  litros % 3.6
if (litros % 3.6) != 0:
    tintasAComprar["galoes"] = tintasAComprar["galoes"] + 1
print("Só galões {}. Total {}".format(tintasAComprar["galoes"], tintasAComprar["galoes"] * 25))

if aviso:
    tintasAComprar["latas"] = tintasAComprar["latas"] - 1
    resto = litros % 18
    if (resto % 3.6) != 0: 
        tintasAComprar["galoes"] = (resto // 3.6) + 1
        
else:
    tintasAComprar["galoes"] = 0

print("Misto {}".format(tintasAComprar))



