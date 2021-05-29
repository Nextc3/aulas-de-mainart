#2.Entrar com números enquanto forem positivos, e imprimir quantos números foram digitados;

numero = float(input("Entre com o numero: "))
quantidade = 0
while numero > 0:
    quantidade += 1
    print("Quantidade de números digitados: {}".format(quantidade))
    numero = float(input("Entre com o numero: "))
print("Programa encerrado")

