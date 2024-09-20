class ArquivoTexto(object):
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self.extrair_conteudo()

    def extrair_conteudo(self):
        # Para acessar o arquivo você deve utilizar o caminho: "/data/"
        with open(file='./arquivos/' + self.arquivo, mode='r', encoding='utf8') as arquivo:
            return arquivo.readlines()

    def extrair_linha(self, numero_linha: int):
        return self.conteudo[numero_linha - 1].strip()


# musica = ArquivoTexto('musica.txt')
# print(musica.conteudo)
# print(musica.extrair_linha(1))
# Para acessar o arquivo você deve utilizar o caminho: "/data/"
