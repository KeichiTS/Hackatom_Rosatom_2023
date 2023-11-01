# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 04:45:14 2023

@author: KeichiTS
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

df = pd.read_csv('C:/Users/KeichiTS/Desktop/PETCT.csv', sep=';')
regioes = ["Norte", "Nordeste", "Sudeste", "Sul", "CentroOeste", "Total"]
df = df.drop(len(df) - 1)

# Loop para plotar uma regressão linear para cada região
for regiao in regioes:
    # Crie o gráfico de regressão linear
    g = sns.lmplot(x="Ano", y=regiao, data=df)
    
    # Realize a regressão linear
    x = df["Ano"]
    y = df[regiao]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    # Calcule o coeficiente angular (a) e o coeficiente linear (b)
    a = slope
    b = intercept
    r_squared = r_value**2
    
    # Adicione o texto com os valores no gráfico
    text = f"a: {a:.4f}\nb: {b:.4f}\nR²: {r_squared:.4f}"
    plt.gcf().text(0.20, 0.8, text, fontsize=12)
    
    # Personalize o título e os rótulos do eixo
    plt.title(f'PETCT em {regiao}')
    plt.xlabel('Ano')
    plt.ylabel('Procedimentos')
    
    # Mostre o gráfico
    plt.show()