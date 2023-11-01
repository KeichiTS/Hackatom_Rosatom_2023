# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 06:11:23 2023

@author: KeichiTS
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv('C:/Users/KeichiTS/Desktop/Energia/Consumo_Energia_Brasil_Região_com_total.csv')



# Filtre o DataFrame para excluir o total por ano
#df = df[df['Região'] != 'Total']

# Pivot the DataFrame para ter anos como colunas
df_pivot = df.pivot(index='Ano', columns='Região', values='Total')

# Crie um gráfico de barras agrupadas
df_pivot.plot(kind='bar', figsize=(12, 6))
plt.title('Consumo de energia (GWh) por Região e Ano')
plt.xlabel('Ano')
plt.ylabel('Consumo de energia (GWh)')
plt.legend(title='Região', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()