'''
2. Criar programa que leia dois conjuntos de números inteiros,
 tendo cada um 10 e 20 elementos e apresente os elementos 
 comuns aos conjuntos. lembre-se de que os elementos podem 
 se repetir mas não podem aparecer repetidos na saída.
 '''
import random

resultado = []

conjunto1 = [random.randint(0,30) for _ in range(10)]
conjunto2 = [random.randint(0,30) for _ in range(20)]
conjunto1.sort()
conjunto2.sort()
print(conjunto1)
print (conjunto2)
for i in conjunto1:
    for j in conjunto2:
        if i == j and j not in resultado:
            resultado.append(j)

for i in resultado:
    print(f'Elemento em comum: {i}')           
