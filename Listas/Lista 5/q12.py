'''
12. Entrar com dois números inteiros e efetuar a adição. Caso o valor somado seja maior que 20, este
deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este
deverá ser apresentado subtraindo-se 5.
'''
numero1 = int(input("Entre com o numero1: "))
numero2 = int(input("Entre com o numero2: "))

adicao = numero1 + numero2
dict_somatorio = {True:adicao + 8, False: adicao - 5}
print("Resultado: {}".format(dict_somatorio[adicao > 20]))