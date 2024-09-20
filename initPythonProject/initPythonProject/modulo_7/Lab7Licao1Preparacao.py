# 1ª Parte - Instalando o pacote wget na versão 3.2. - pip install wget==3.2

# 2ª Parte - Fazendo o download dos dados no arquivo compactado dados.zip.
import wget
wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')

# 3ª Parte - Descompactando os dados na pasta dados com o pacote nativo zipfile.
import zipfile
with zipfile.ZipFile('./dados.zip', 'r') as fp:
  fp.extractall('./dados')

# 5ª Parte - Renomeando o arquivo com o pacote nativo os.

import os
os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')
