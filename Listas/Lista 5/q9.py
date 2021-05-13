'''
9.Um comerciante comprou um produto e quer vende-lo com um lucro de 45% se o valor da compra for
menor que 20,00, caso contrário o lucro será de 30%. entrar com o valor do produto e imprimir o valor da
venda.
'''
valorProduto = int(input("Entre com o valor do produto: "))

dict_lucro = {True:0.45, False:0.30}
lucro = dict_lucro[valorProduto < 20]
valorDeVenda = valorProduto + (valorProduto * lucro)
print("Valor de venda: {}".format(valorDeVenda))