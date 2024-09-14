linha = None
idades = [45, 20, 80, 69, 24, 53]
frutas = ['banana', 'morango', 'melancia', 'limão', 'melão']

with open('./arquivos/novo_arquivo_idades_w.text', 'w') as txt:
    linha = 'idades' + '\n'
    txt.write(linha)

    for idade in idades:
        linha = str(idade) + '\t'
        txt.write(linha)

    txt.write("\n")

    linha = 'frutas' + '\n'
    txt.write(linha)

    for fruta in frutas:
        linha = str(fruta) + '\t'
        txt.write(linha)

    txt.write("\n")