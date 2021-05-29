#5.Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro caracter de cada nome;
nome = input("Entre com um nome: ")
while nome != "FIM":
    print("Primeira letra do nome: {}".format(nome[0]))
    nome = input("Entre com um nome: ")
