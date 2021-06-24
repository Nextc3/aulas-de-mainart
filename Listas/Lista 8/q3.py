'''
3. Cria um programa que leia vários números inteiros e positivos.
 A leitura se encerra quando encontrar um numero negativo ou quando o
  vetor ficar completo. sabe-se que o vetor possui no maximo 10 elementos.
   gerar e imprimir um vetor onde cada elemento é o inverso do correspondente 
   do vetor principal.
'''

vetor = []
for _ in range(10):
    numero = int(input("Digite o número para inserir no vetor: "))
    if numero < 0:
        break
    vetor.append(numero)
novoVetor = [1/i for i in vetor]
print(novoVetor)


