#Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. 
# Ele quer saber aulas 
# quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!

percentual = 0.75
meses = 4
aulasPorSemana = 2
semanasPorMeses = 4

totalAulas = meses * aulasPorSemana * semanasPorMeses

aulasQuePodeFaltar = totalAulas * percentual

print("Davinir pode faltar")
print(aulasQuePodeFaltar)