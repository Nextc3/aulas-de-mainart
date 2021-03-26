#Criar um programa que leia a quantidade de fotas de uma locadora de vídeo possui e o valor que ela cobra
#por cada aluguel, mostrando as informações pedidas a seguir: a) sabendo que um terço das fitas são
#alugadas por mês, exiba o faturamento anual da locadora; b)Quando o cliente atrasa a entrega, é cobrada
#uma multa de 10% sobre o valor do aluguel. Sabendo que um decimo das fitas alugadas no mês são
#devolvidas com atraso, calcule o valor ganho com multas por mês; c) sabendo ainda que 2% de fitas se
#estragam ao longo do ano, e um decimo do total é comprado para reposição, exiba a quantidade de fitas
#que a locadora terá no final do ano.

fitas = int(input("Entre com a quantidade de fitas: "))
valorAluguel = float(input("Entre com o valor do alguel: "))
alugadasPorMes = fitas // 3
faturamentoMes = valorAluguel * alugadasPorMes
faturamentoAnual = faturamentoMes * 12
multa = 0.1
valorAluguelComMulta = valorAluguel + (multa * valorAluguel)
fitasEmAtraso = 0.1
fitasAtrasadas = alugadasPorMes * fitasEmAtraso
faturamentoPorMesComMultas =  (fitasAtrasadas * valorAluguelComMulta) + ((alugadasPorMes - (fitasEmAtraso * alugadasPorMes)) * valorAluguel)
faturamentoPorMesEmMultas = faturamentoPorMesComMultas - faturamentoMes 
faturamentoPorAnoComMultas = faturamentoPorMesComMultas * 12
fitasEstragadasEmUmAno = 0.2 * fitas 
compradasPraReposicao = fitas  * 0.1 
totalFinalDeAno = compradasPraReposicao + fitas - fitasEstragadasEmUmAno

print("Faturamento anual da locadora: {}".format(faturamentoAnual))
print("Faturamento anual da locadora com multas: {}".format(faturamentoPorAnoComMultas))
print("Faturamento mensal da locadora: {}".format(faturamentoMes))
print("Faturamento mensal em multas: {}".format(faturamentoPorMesEmMultas))
print("Faturamento mensal com multas: {}".format(faturamentoPorMesComMultas))
print("Total de fitas no final do ano: {}".format(totalFinalDeAno))
