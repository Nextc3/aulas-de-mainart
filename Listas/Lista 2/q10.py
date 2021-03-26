#Dada a frase “Python é muito legal". use fatiamento para dar nome às variáveis contendo cada palavra.
#Qual o tamanho dessa frase? E qual o tamanho de cada palavra?

frase = "Python é muito legal"
aux = frase.split()
tamanhoDaFrase = len(aux)

print("Tamanho da frase eh: {}".format(tamanhoDaFrase))

print("Tamanho de cada palavra {} {} {} {}".format(len(aux[0]), len(aux[1]), len(aux[2]), len(aux[3])))