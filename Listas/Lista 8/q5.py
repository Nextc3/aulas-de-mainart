'''
5. Criar programa que leia dados de 20 elementos inteiros. imprimir 
o maior e o menor, sem ordenar, o percentual de números pares e a
 media dos elementos do vetor.

'''
import random

vetor = [random.randint(0,100) for i in range(20)]

print (vetor)
maior = 0
menor = vetor[0]

par = 0
somatorio = 0
percentual = 0
for i in vetor:
    if i > maior :
        maior = i
    if i < menor :
        menor = i
    if (i % 2) == 0:
        par += 1
    somatorio += i

media = somatorio / 20
percentual = (par * 100) / 20
print(f'O maior número: {maior}')
print(f'O menor número: {menor}')
print(f'O número de pares: {par}')
print(f'O número de média: {media}')

    