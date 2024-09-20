import seaborn as sns
import pandas as pd


df = pd.read_csv('./dados/dow_jones_index.csv')

df.head(n=10)
df.columns.to_list()

linhas, colunas = df.shape
print(f'Número de linhas: {linhas}')
print(f'Número de colunas: {colunas}')

df_mcd = df[df['stock'] == 'MCD']
df_mcd = df_mcd[['date', 'open', 'high', 'low', 'close']]

plot = sns.lineplot(x="date", y="open", data=df_mcd)
plot.tick_params(axis='x', labelrotation = 45)

plot = sns.lineplot(x="date", y="value", hue='variable', data=pd.melt(df_mcd, ['date']))
plot.tick_params(axis='x', labelrotation = 45)

# Comando a abaixo gera a imagem
# plot.figure.savefig("./mcd.png")

df_coke = df[df['stock'] == 'KO']
df_coke = df_coke[['date', 'open', 'high', 'low', 'close']]

plot = sns.lineplot(x="date", y="open", data=df_coke)
plot.tick_params(axis='x', labelrotation=45)

plot.figure.savefig("./ko.png")

