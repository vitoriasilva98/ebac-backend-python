## Exercício 1 - Pandas

import pandas as pd

df = pd.read_csv('./dados/dow_jones_index.csv')

df.head(n=10)
df.columns.to_list()

linhas, colunas = df.shape
print(f'Número de linhas: {linhas}')
print(f'Número de colunas: {colunas}')

df_mcd = df[df['stock'] == 'MCD']
df_mcd = df_mcd[['date', 'open', 'high', 'low', 'close']]

# print(df_mcd)

df_mcd.head(n=10)
df_mcd.dtypes

## c. Vamos limpar as colunas com o método apply, que permite a aplicação de uma função anônima (lambda) qualquer. A função lambda remove o caracter $ e faz a conversão do tipo de str para float.
for col in ['open', 'high', 'low', 'close']:
  df_mcd[col] = df_mcd[col].apply(lambda value: float(value.split(sep='$')[-1]))

df_mcd.head(n=10)
df_mcd.dtypes

# print(df_mcd)

### Incío do exercício

# Crie um Dataframe filtrado, selecionando as linha do dataframe original df em que a coluna stock é igual a KO.
df_coke = df[df['stock'] == 'KO']

# Selecione apenas as colunas de data e valores de ações: ['date', 'open', 'high', 'low', 'close'].
df_coke = df_coke[['date','open', 'close', 'high', 'low']]

# Limpe as colunas com o método `apply`, que permite a aplicação de uma função anônima (`lambda`) qualquer. A função `lambda` deve remover o caracter `$` e fazer a conversão do tipo de `str` para `float`.
for colunm in ['open', 'high', 'low', 'close']:
    df_coke[colunm] = df_coke[colunm].apply(lambda value: float(value.split(sep='$')[-1]))

print(df_coke)
# print the types
print(df_coke.dtypes)