import os


def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
    palavras_linha = []

    with open(file='./arquivos/' + nome_arquivo, mode='r', encoding='utf8') as arquivo:
        for lineText in range(0, numero_linha):
            linha = arquivo.readline()

        quebra_linha = linha.split(sep=' ')
        palavras_linha = quebra_linha

    return palavras_linha


linha10 = extrai_linha_txt(nome_arquivo='musica.txt', numero_linha=5)
print(linha10)

# leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'. O caminho para o arquivo deve começar com "../../data/".
# extraia a linha do arquivo utilizando o parametro 'numero_linha'
# quebre a linha em palavras com o comando split, note que o separador é um espaço ' '
