
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 05:40:27 2023

@author: KeichiTS
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

df = pd.read_csv('C:/Users/KeichiTS/Desktop/Consumo_Energia_Brasil_Região.csv', sep=';')
df["total"] = df["total"].str.replace(',', '.', regex=True)
df["total"] = df["total"].astype(float)

novo_df = pd.DataFrame(columns=["Ano", "Região", "Total"])
regioes = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]

for ano in df["ano"].unique():
    for regiao in df["macro_grupo"].unique():
        filtro = (df["ano"] == ano) & (df["macro_grupo"] == regiao)
        total_regiao = df[filtro]["total"].sum()
        novo_df = novo_df.append({"Ano": ano, "Região": regiao, "Total": total_regiao}, ignore_index=True)

# Adicionar linhas "Total" para cada ano
for ano in df["ano"].unique():
    total_ano = novo_df[novo_df["Ano"] == ano]["Total"].sum()
    novo_df = novo_df.append({"Ano": ano, "Região": "Total", "Total": total_ano}, ignore_index=True)

novo_df["Ano"] = novo_df["Ano"].astype(int)
novo_df["Total"] = novo_df["Total"].astype(float)

for regiao in regioes + ["Total"]:
    regiao_data = novo_df[novo_df["Região"] == regiao]

    if not regiao_data.empty:
        g = sns.lmplot(x="Ano", y="Total", data=regiao_data)

        x = regiao_data["Ano"]
        y = regiao_data["Total"]
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

        a = slope
        b = intercept
        r_squared = r_value**2

        text = f"a: {a:.4f}\nb: {b:.4f}\nR²: {r_squared:.4f}\nTotal: {y.values[0]:.2f}"
        plt.gcf().text(0.20, 0.8, text, fontsize=12)

        plt.title(f'Consumo de energia (GWh) - {regiao}')
        plt.xlabel('Ano')
        plt.ylabel('Energia (GWh)')

        plt.show()
        
novo_df.to_csv('Consumo_Energia_Brasil_Região_com_total.csv', index=False)
