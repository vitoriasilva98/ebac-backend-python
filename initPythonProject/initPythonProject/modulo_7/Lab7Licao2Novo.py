import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_coke = pd.read_csv('./data/df_coke.csv', index_col=0)

fig, axs = plt.subplots(1, figsize=(8, 8))

plot = sns.lineplot(x="date", y="open", data=df_coke)
plot.tick_params(axis='x', labelrotation=45)

plot.figure.savefig("./ko.png")

plt.show()