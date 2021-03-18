#8. supondo um numero 123, imprimi-lo invertido. 
# Exemplo (123, 321). O numero deverá ser armazenado em outra
#variável.

numero = 123

aux1 = numero % 10
numero = numero // 10
aux2 = numero % 10
numero = numero // 10
aux3 = numero % 10


numero = aux1 * 10
numero = (numero + aux2) * 10
numero = numero + aux3
print(numero)