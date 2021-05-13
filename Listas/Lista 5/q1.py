numero = int(input("entre com o número"))
valor = (numero > 20) and (numero < 90) 
dict_numero = {True:"Sim. O valor compreende entre 20 e 90", False:"Não. O número não compreende entre 20 e 90"}
print(dict_numero[valor])