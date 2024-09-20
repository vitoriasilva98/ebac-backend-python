from modulo_7.extracao.arquivo_csv import ArquivoCSV

arquivo_banco = ArquivoCSV(arquivo='./arquivos/banco.csv')

# education = arquivo_banco._extrair_conteudo()
education = arquivo_banco.extrair_coluna(indice_coluna=3)
print(education)