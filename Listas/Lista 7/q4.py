#4.Entrar com vários números e informar quantos números entre 100 e 200 foram
#digitados. quando o valor 0 for digitado o programa deve encerrar;

numero = float(input("Entre com o número: "))
quantidade = 0
while numero != 0:
    if numero > 100 and numero < 200:
        quantidade += 1
    print ("Quantidade de números entr 100 e 200: {}".format(quantidade))
    numero = float(input("Entre com o número: "))