#Crie três listas, uma lista de cada coisa a seguir:
##• frutas
#• docinhos de festa (não se esqueça de brigadeiros!!)
#• ingredientes de feijoada
#Lembre-se de salvá-las em alguma variável!
#a. Agora crie uma lista que contém essas três listas.
#Nessa lista de listas (vou chamar de listona):
#b. você consegue acessar o elemento brigadeiro?
#c. Adicione mais brigadeiros à segunda lista de listona. O que aconteceu com a lista de docinhos
#de festa?
#d. Adicione bebidas ao final da listona, mas sem criar uma lista!

frutas = ["maçã", "uva", "jaca"]
docinhos_de_festa = ["brigadeiro", "beijinho", "cajuzinho"]
ingredientes = ["fejão", "calabresa", "coentro"]

listona = [frutas, docinhos_de_festa, ingredientes]

print("Listona: ")
print(listona)

print("Imprimindo o elemento brigadeiro listona[2][0]")
print(listona[2][0])

listona[1].append("brigadeiro1")
listona[1].append("brigadeiro2")

print("Imprimindo depois de adicionar brigadeiros")
print(listona)

print(docinhos_de_festa)

listona.append("cerveja")
listona.append("refrigerante")
listona.append("água")

print("Imprimindo depois de adicionar bebidas:")
print(listona)


