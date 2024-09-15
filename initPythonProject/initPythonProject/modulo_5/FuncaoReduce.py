# Função reduce

from functools import reduce # Precisa do import

numeros = [1, 2, 3]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)