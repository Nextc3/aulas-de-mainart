numero1 = int(input("Entre com o numero1: "))
numero2 = int(input("Entre com o numero2: "))
dict_decisao = {True:numero1, False:numero2}
print("Maior numero: {}".format(dict_decisao[numero1 > numero2]))