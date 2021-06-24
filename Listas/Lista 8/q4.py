'''
4. Ler um vetor vet de 10 elementos e obter um vetor w cujos componentes
 são os fatoriais dos respectivos componentes de v;
 '''


import random

#vetor = [int(input("Digite um número: ")) for _ in range(10)]

vetor = [random.randint(1,10) for _ in range(10)]
vetorw = []
aux = 1
for i in vetor:
    for j in range(1,i + 1):
        aux *= j
    vetorw.append(aux)
    aux = 1
print(vetor)
print(vetorw)