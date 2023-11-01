# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 05:17:58 2023

@author: KeichiTS
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv('C:/Users/KeichiTS/Desktop/PETCT.csv', sep =';')

# Substituir vírgulas por pontos e converter para float
#for col in df.columns[1:]:
#    df[col] = df[col].str.replace(',', '.').astype(float)

#df[df.columns[1:5]] = df[df.columns[1:5]] *100


# Preparação dos dados
anos = df['Ano']
regioes = df.columns[1:]
valores = df.iloc[:, 1:].values.T  # Transpor os valores para que as regiões fiquem no eixo x

# Configuração da figura e dos eixos
fig, ax = plt.subplots(figsize=(12, 6))
largura_barra = 0.15
posicoes = np.arange(len(anos))

# Loop para criar barras agrupadas para cada ano
for i, regiao in enumerate(regioes):
    ax.bar(posicoes + i * largura_barra, valores[i], largura_barra, label=regiao)

# Configuração dos eixos
ax.set_xlabel('Ano')
ax.set_ylabel('Procedimentos')
ax.set_title('Procedimentos de PETCT por Ano e Região')
ax.set_xticks(posicoes + (largura_barra * len(regioes)) / 2)
ax.set_xticklabels(anos)
ax.legend()

plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

