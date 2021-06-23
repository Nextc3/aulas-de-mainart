# sourcery skip
'''
1. Criar um programa que leia o preço de compra e o preço de venda de 100 produtos. 
o programa devera imprimir quantas mercadoria proporcionam 
a) lucro < 10%, b) 10% <= lucro <= 20%, c) lucro > 20%.
'''
menorDez = 0
entreDezVinte = 0
maiorVinte = 0
for _ in range(100) :
    precoCompra = float(input("Digite o preço de compra: "))
    precoVenda = float(input("Entre com preço de venda: "))
    lucro = precoVenda - precoCompra
    percentualLucro = (lucro * 100) / precoCompra
    if (percentualLucro < 10):
        menorDez += 1
    elif (percentualLucro >= 10 ) and (percentualLucro <= 20):
        entreDezVinte += 1
    else:
        maiorVinte += 1
print(f'Vendidas com menos de 10%: {menorDez}')
print(f'Vendidas com mais de 10% e menos do que 20%: {entreDezVinte}')
print(f'Vendidas com mais de 20%: {maiorVinte}')


    




