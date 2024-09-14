
conteudo = None

print("Primeira leitura com método read()")

with open(file='./arquivos/banco.csv', mode='r', encoding='utf8') as planilha :
    conteudo = planilha.read()

print(conteudo + "\n")

print("Primeira leitura com método readline()")

linha = None
conteudo = []

with open('./arquivos/banco.csv', 'r') as planilha:
    linha = planilha.readline()

    while linha:
        conteudo.append(linha)
        linha = planilha.readline()

print(conteudo)