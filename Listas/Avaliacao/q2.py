'''
2) Dada a frase “Python é muito legal”, use fatiamento para dar nome às variáveis contendo
cada palavra. O programa deverá:
a. imprima a quantidade de elementos da frase, das variáveis com os respectivos conteúdos
e tamanho.
b. imprima a frase invertida;

'''

frase = "Python é muito legal"
fraseFatiada = frase.split()
print(fraseFatiada)
quantidadeDeElementos = len(fraseFatiada)
fraseDic = {
    fraseFatiada[0] : len(fraseFatiada[0]),
    fraseFatiada[1] : len(fraseFatiada[1]),
    fraseFatiada[2] : len(fraseFatiada[2]),
    fraseFatiada[3] : len(fraseFatiada[3])
}
print("Frase, suas palavras e tamanho de cada uma: {}".format(fraseDic))
print("Quantidade de elementos da frase toda: {}".format(quantidadeDeElementos))

print("Imprimindo a frase invertida: ")
print(frase[::-1])