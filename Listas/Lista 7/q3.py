#3.Entrar com vários números positivos e imprimir a media dos números digitados. o
#programa acaba quando se informar que não deseja mais continuar.


numero = float(input("Entre com o numero: "))
mensagem = "sim"
quantidade = 0
numeroAnterior = 0 
while numero > 0 and mensagem == "sim":
    quantidade += 1
    media = (numero + numeroAnterior)/quantidade
    print("A média agora eh: {}".format(media))
    mensagem = input("Deseja continuar?(sim) ou qualquer coisa pra não ")
    if (mensagem != "sim"):
        break
    numeroAnterior += numero
    numero = float(input("Entre com o numero: "))

