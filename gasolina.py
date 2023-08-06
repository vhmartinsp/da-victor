import csv
from sys import argv
import matplotlib.pyplot as plt


import seaborn as sns

# Extraindo as colunas hora e taxa

dias = []
preços = []

with open(file='./gasolina.csv', mode='r', encoding='utf8') as fp:
  linha = fp.readline()
  linha = fp.readline()
  while linha:
    linha_separada = linha.split(sep=',')
    dia = linha_separada[1]
    dias.append(dia)
    taxa = float(linha_separada[2])
    dias.append(taxa)
    linha = fp.readline()

# Salvando no grafico
grafico = sns.lineplot(x=dias, y=preços)
grafico = plt.gca()

largura =  80 / 2.54
altura =  20 / 2.54
grafico.figure.set_size_inches(w=largura, h=altura)

grafico.set_title("Preço da gasolina por dia", fontsize=12, fontweight="bold");
grafico.set_xlabel("Dia", fontsize=10);
grafico.set_ylabel("Preço", fontsize=10);


grafico.figure.savefig(fname="gasolina.png", bbox_inches="tight")

