from extracao.arquivo_csv import ArquivoCSV
from extracao.arquivo_txt import ArquivoTXT

arquivo_noticia = ArquivoTXT(arquivo='./arquivos/noticia.txt')
titulo = arquivo_noticia.extrair_linha(numero_linha=1)
print(titulo)

arquivo_banco = ArquivoCSV(arquivo='./arquivos/banco.csv')
education = arquivo_banco.extrair_coluna(indice_coluna=3)
print(education)