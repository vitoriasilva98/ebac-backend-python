import os
import json
import time
from random import random
from datetime import datetime
import requests
import csv
from sys import argv
import pandas as pd
import seaborn as sns

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'


def extrair_taxa():
    # Captando a taxa CDI do site da B3
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.HTTPError as exc:
        print("Dado não encontrado, continuando.")
        return None
    except Exception as exc:
        print("Erro, parando a execução.")
        raise exc
    else:
        return json.loads(response.text)
        # return json.loads(response.text)[-1]['valor']

def gerar_csv():
    # Extraindo a taxa CDI
    dado = extrair_taxa()

    for i in range(0, 10):
        # Criando a variável data e hora
        data_e_hora = datetime.now()
        data = datetime.strftime(data_e_hora, '%Y/%m/%d')
        hora = datetime.strftime(data_e_hora, '%H:%M:%S')

        cdi = float(dado[i]['valor']) + (random() - 0.5)

        # Verificando se o arquivo "taxa-cdi.csv" existe
        if os.path.exists('./taxa-cdi.csv') == False:
            with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
                fp.write('data,hora,taxa\n')

        # Salvando dados no arquivo "taxa-cdi.csv"
        with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
            fp.write(f'{data},{hora},{cdi}\n')
        time.sleep(1)

    print("CSV gerado com sucesso")

def gerar_grafico(nome_grafico):
    # Extraindo as colunas hora e taxa
    df = pd.read_csv('./taxa-cdi.csv')

    # criando o gráfico
    grafico = sns.lineplot(x=df['hora'], y=df['taxa'])

    # Definindo os ticks antes de definir os rótulos
    grafico.set_xticks(range(len(df['hora'])))  # Define os ticks

    # definição dos rótulos dos ticks com rotação
    _ = grafico.set_xticklabels(labels=df['hora'], rotation=90)

    # Salvando o gráfico como arquivo PNG
    grafico.get_figure().savefig(f"{nome_grafico}.png")


def main():
    nome_grafico = argv[1]
    gerar_csv()
    gerar_grafico(nome_grafico)

if __name__ == "__main__":
    main()
