#6.Entrar com vários números ate entrar com o numero 999. para cada numero imprimir seus divisores;

numero = int(input("Entre com um número: "))

while numero < 999:
    resto = 1
    for i in range(1,numero):
        resto = numero % i
        if resto == 0:
            print("Divisor: {}".format(i))
    print("Divisor: {}".format(numero))
    numero = int(input("Entre com um número: "))