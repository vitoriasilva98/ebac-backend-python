# import sys
# sys.path.insert(0, './arquivos/')
# import ArquivoTexto
from modulo_6.ArquivoTexto import ArquivoTexto


class ArquivoCSV(ArquivoTexto):

    def __init__(self, arquivo: str):
        super().__init__(arquivo=arquivo)
        self.colunas = self.extrair_coluna(1)

    def extrair_nome_colunas(self):
        return self.conteudo[0].strip().split(sep=',')

    def extrair_coluna(self, indice_coluna: int):
        coluna = list()
        for linha in self.conteudo:
            conteudo_linha = linha.strip().split(sep=',')
            coluna.append(conteudo_linha[indice_coluna - 1])
        coluna.pop(0)
        return coluna

arquivo_csv = ArquivoCSV('arquivo.csv')
print(arquivo_csv.conteudo)
print(arquivo_csv.extrair_coluna(2))
