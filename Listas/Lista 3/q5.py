#Dado uma lista de números, faça com que os números sejam ordenados e, em seguida, inverta a
#ordem da lista
#usando slicing.

numeros = [2, 1, 8, 3, 10, 3, 7, 4]
print("Lista de números")
print(numeros)
numeros.sort()
print("Lista ordenada")
print(numeros)
print("Imprimindo uma lista invertida")
print(numeros[::-1])
