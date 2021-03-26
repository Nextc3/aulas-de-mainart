#Dado um numero de conta corrente com três dígitos, retorne o seu digito verificador, o qual é calculado da
#seguinte maneira. Exemplo: numero conta 235, somar o numero da conta com seu inverso : 235+532=767.
#Multiplicar cada digito pela sua ordem posicional e somar estes resultados: 7 6 7 (7x1+6x2+7x3) = 40. O
#ultimo digito desse resultado é o digito verificador da conta (40-> 0 )

numero = int(input("Digite a conta corrente: "))
aux0 = numero
aux1 = numero % 10
numero = numero // 10
aux2 = numero % 10
numero = numero // 10
aux3 = numero % 10


numero = aux1 * 10
numero = (numero + aux2) * 10
numero = numero + aux3

numero3 = aux0 + numero
numero3 = str(numero3)

aux3 = (int(numero3[0]) * 1) + (int(numero3[1]) * 2) + (int(numero3[2]) * 3)
aux3 = str(aux3)

print("Digito verificador eh: {}".format(aux3[-1]))
