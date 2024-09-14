norte_europa = {'reino unido', 'suecia', 'russia', 'noruega', 'dinamarca'}
escandinavia = {'noruega', 'dinamarca', 'suecia'}

norte_europa_nao_escandivano = norte_europa - escandinavia
print(norte_europa_nao_escandivano)

escandivano_nao_norte_europa = escandinavia - norte_europa
print(escandivano_nao_norte_europa)

print('\n')

times_paulistas = {'São Paulo', 'Palmeiras', 'Corinthians', 'Santos'}
print(times_paulistas)
print(type(times_paulistas))
print('\n')

# Conversão
meu_conjunto = {1, 2, 3, 4}
minha_lista = list(meu_conjunto)
print(minha_lista)  # [1, 2, 3, 4]

minha_lista = [1, 2, 3, 4, 4]
meu_conjunto = set(minha_lista)
print(meu_conjunto)  # {1, 2, 3, 4}