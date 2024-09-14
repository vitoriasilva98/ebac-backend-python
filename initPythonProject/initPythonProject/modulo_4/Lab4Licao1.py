valor_venda = []

with open(file='./arquivos/carros.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # lê o cabeçalho
    linha = arquivo.readline()  # lê a primeira linha
    while linha:
        linha_separada = linha.split(sep=",")  # quebra a string nas virgulas e salva os resultados em uma lista

        valor = str(linha_separada[1])  # seleciona o segundo elemento da lista
        valor_venda.append(valor)  # salva o valor na lista de valor_venda
        linha = arquivo.readline()  # lê uma nova linha, se a linha não existir, salva o valor None

print(valor_venda)
