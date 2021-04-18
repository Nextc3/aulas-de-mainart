#Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!
#Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.
#Agora «vá à sorveteria» e se empanturre de sorvete e tire o sorvete da lista.

lista_de_compras = ["kiboa","detegente", "fejão", "arroz", "vassoura", "geléia"]

print("Lista de compras")
print(lista_de_compras)
print("Indo no mercado")
print("Deletando produtos de limpeza")
del lista_de_compras[0]
del lista_de_compras[1]
print(lista_de_compras)
print("Indo na sorveteria")
lista_de_compras.append("sorvete de morango")
lista_de_compras.append("sorvete de chocolate")
lista_de_compras.append("sorvete de pistache")
print("Depois de comer na sorveteria")
print(lista_de_compras)
print("Deletando sorvetes da lista")
del lista_de_compras["sorvete de morango"]
del lista_de_compras["sorvete de chocolate"]
del lista_de_compras["sorvete de pistache"]
print(lista_de_compras)
