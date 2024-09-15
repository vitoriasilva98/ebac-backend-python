# Função filter
numeros = [1, 2, 3, 4, 5]
numeros_par = filter(lambda num: num % 2 == 0, numeros)

print(list(numeros_par))