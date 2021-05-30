'''
7.Dado um pais A, com 5.000.0000 de habitantes e uma taxa de natalidade de 3%
ao ano, e um pais B com 7.000.000 de habitantes e uma taxa de natalidade
de 2% ao ano. calcular e imprimir o tempo necessário para que a
população do pais A ultrapasse a população do pais B;
'''
paisA = 5000000
paisB = 7000000
ano = 0

while paisA < paisB:
    paisB += (paisB * 0.02)
    paisA += (paisA * 0.03)
    print("Pais A")
    print(paisA)
    print("Pais B")
    print(paisB)
    ano += 1
print("O ano que o pais A alcançou o B foi: {}".format(ano))