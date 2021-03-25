#Entrar com dois números inteiros e imprimir a seguinte saída: a)dividendo; b) divisor; c) quociente; d) resto.

numero1 = int(input("Entre com o primeiro número "))
numero2 = int(input("Entre com o segundo número "))

print("Como {} sendo dividendo e {} sendo divisor".format(numero1, numero2))

print("Dividendo {} \n divisor {} \n quociente {} \n resto {} ".format(numero1, numero2, numero1/numero2, numero1%numero2))

print("Como {} sendo dividendo e {} sendo divisor".format(numero2, numero1))

print("Dividendo {} \n divisor {} \n quociente {} \n resto {} ".format(numero2, numero1, numero2/numero1, numero2%numero1))