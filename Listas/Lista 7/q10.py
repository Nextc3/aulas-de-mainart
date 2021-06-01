'''
10.Criar um
programa que deixe entrar com 10 números positivos e imprima a raiz
quadrada de cada numero. para cada entrada de dados devera haver um
trecho de "proteção" para que um numero negativo não seja aceito.
'''


#import math


for _ in range(10):
    numero = int(input("Entre com o número: "))
    if(numero < 0):
        print("Número digitado deve ser positivo")
        continue
    print("Raiz quadrada do número digitado: {}".format(numero ** (1/2)))
