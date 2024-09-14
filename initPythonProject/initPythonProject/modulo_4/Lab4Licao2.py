import os


def extrai_coluna_csv(nome_arquivo: str,
                      indice_coluna: int):  # leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
    coluna = []

    with open(file='./arquivos/'+nome_arquivo, mode='r', encoding='utf8') as arquivo:
        linha = arquivo.readline()
        linha = arquivo.readline()

        while linha:
            quebra_linha = linha.split(sep=",")

            valor_venda = str(
                quebra_linha[indice_coluna])  # extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
            coluna.append(valor_venda)
            linha = arquivo.readline()

    return coluna


valor_manutencao = extrai_coluna_csv(nome_arquivo='carros.csv', indice_coluna=2)
# valor_manutencao = extrai_coluna_csv(nome_arquivo='../../data/carros.csv', indice_coluna=2) # para teste naplataforma
print(valor_manutencao)

# leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
# O caminho para o arquivo deve começar com '../../data/'
# extraia a coluna do arquivo utilizando o parametro 'indice_coluna'