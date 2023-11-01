# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 07:03:15 2023

@author: KeichiTS
"""

import pandas as pd
import matplotlib.pyplot as plt

# Se você não tiver lido os dados do CSV, faça isso primeiro
brasil = pd.read_csv('C:/Users/KeichiTS/Desktop/Crescimento_Populacional/Censo 2022 - Crescimento Populacional - Brasil.csv')
norte = pd.read_csv('C:/Users/KeichiTS/Desktop/Crescimento_Populacional/Censo 2022 - Crescimento Populacional - Norte.csv')
nordeste = pd.read_csv('C:/Users/KeichiTS/Desktop/Crescimento_Populacional/Censo 2022 - Crescimento Populacional - Nordeste.csv')
centrooeste = pd.read_csv('C:/Users/KeichiTS/Desktop/Crescimento_Populacional/Censo 2022 - Crescimento Populacional - Centro-Oeste.csv')
sudeste = pd.read_csv('C:/Users/KeichiTS/Desktop/Crescimento_Populacional/Censo 2022 - Crescimento Populacional - Sudeste.csv')
sul = pd.read_csv('C:/Users/KeichiTS/Desktop/Crescimento_Populacional/Censo 2022 - Crescimento Populacional - Sul.csv')

df = pd.concat([norte, nordeste, centrooeste, sudeste, sul])

# Pivot the DataFrame para ter anos como colunas
df_pivot = df.pivot(index='Ano da pesquisa', columns='Grande Região', values='População(pessoas)')


# Normalize os dados para que cada barra represente 100%
df_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0) * 100

## Crie um gráfico de barras agrupadas
#df_pivot.plot(kind='bar', figsize=(12, 6))
#plt.title('Percentual de Habitantes por Região e Ano')
#plt.xlabel('Ano')
#plt.ylabel('Habitantes')
#plt.legend(title='Região', bbox_to_anchor=(1.05, 1), loc='upper left')
#plt.tight_layout()
#plt.show()

# Crie um gráfico de barras agrupadas
df_normalized.plot(kind='bar', figsize=(12, 6))
plt.title('Percentual de Habitantes (%) por Região e Ano')
plt.xlabel('Ano')
plt.ylabel('Percentual de Habitantes (%)')
plt.legend(title='Região', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()