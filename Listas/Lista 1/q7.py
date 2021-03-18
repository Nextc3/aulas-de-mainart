#7. uma figura cujo ângulo e 80 graus. Imprima o seno, co-seno, tangente, secante, cp-secante, e co-tangente.

import math

graus = 80
radianos = math.radians(80)

seno = math.sin(radianos)
print("Seno")
print(seno)

cosseno = math.cos(radianos)
print("CosSeno")
print(cosseno)

tangente = math.tan(radianos)
print("Tangente")
print(tangente)

secante = 1 / cosseno
print("Secante")
print(secante)

cosecante = 1 / seno
print("CoSecante")
print(cosecante)

cotangente = 1 / tangente
print("Cotangente")
print(cotangente)
