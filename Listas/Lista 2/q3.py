#Entrar com um nome e imprimir: a) todo o nome; b) primeiro carcater; c) ultimo carcater; d) do primeiro
#ate o terceiro caracter; e)quarto caracter; f) os dois últimos.

nome = input("Entre com o nome por favor ")
todoNome = nome[:]
primeiro = nome[0]
ultimo = nome[-1]
primeiroTerceiro = nome[0:3]
quarto = nome[3]
doisUltimos = nome[-2:]
print("todo nome {} \nprimeiro caracter {}\n ultimo caracter {}\n do primeiro até o terceiro caracter {}\n quarto caracter {}\n os dois últimos {}".format(todoNome, primeiro, ultimo, primeiroTerceiro, quarto, doisUltimos))
