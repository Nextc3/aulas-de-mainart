#Entrar com quatro números e imprimir a media ponderada, sabendo-se que os pesos são respectivamente
#1,2,3,4.

numero1 = int(input("Entre com o numero1 "))
numero2 = int(input("Entre com o numero2 "))
numero3 = int(input("Entre com o numero3 "))
numero4 = int(input("Entre com o numero4 "))

resultado = (numero1 * 1 + numero2 * 2 + numero3 * 3 + numero4 * 4)/4

print("Resultado é {}".format(resultado))