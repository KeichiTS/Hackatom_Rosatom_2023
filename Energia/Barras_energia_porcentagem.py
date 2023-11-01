# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 06:20:46 2023

@author: KeichiTS
"""

import pandas as pd
import matplotlib.pyplot as plt

# Se você não tiver lido os dados do CSV, faça isso primeiro
df = pd.read_csv('C:/Users/KeichiTS/Desktop/Energia/Consumo_Energia_Brasil_Região_com_total.csv')

# Filtre o DataFrame para excluir o total por ano
df = df[df['Região'] != 'Total']

# Pivot the DataFrame para ter anos como colunas
df_pivot = df.pivot(index='Ano', columns='Região', values='Total')

# Normalize os dados para que cada barra represente 100%
df_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0) * 100

# Crie um gráfico de barras agrupadas
df_normalized.plot(kind='bar', figsize=(12, 6))
plt.title('Consumo de energia por Região (%) e Ano')
plt.xlabel('Ano')
plt.ylabel('Porcentagem do Consumo de energia')
plt.legend(title='Região', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()