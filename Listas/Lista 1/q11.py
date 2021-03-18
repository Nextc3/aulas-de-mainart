#11. Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson)
#  foram no supermercado e
#compraram alguns itens:
#• 75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
#• 2 pacotes de macarrão: R$ 8,73 cada
#• 1 pacote de Molho de tomate: R$ 3,45
#• 420g Cebola: R$ 5,40/kg
#• 250g de Alho: R$ 30/kg
#• 450g de pães franceses: R$ 25/kg
#Calcule quanto ficou para cada um.

cerveja = 75
macarrao = 2 
molhoTomate = 1
cebola = 420
alho = 250
paes = 450


total = cerveja * 2.20 + macarrao * 8.73 + molhoTomate * 3.45 + (cebola / 1000) * 5.40 + (alho / 1000) * 30 + (paes / 1000) * 25 
print("Fica pra cada:")
print(total / 5)