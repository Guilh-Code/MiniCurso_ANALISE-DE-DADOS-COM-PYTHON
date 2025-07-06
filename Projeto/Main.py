import pandas as pd

tabela = pd.read_csv("Projeto/ClientesBanco.csv", encoding="latin1") # Formatar a tabela para LATIN

tabela = tabela.drop("CLIENTNUM", axis= 1) # Drop -> deleta colunas ou linhas (axis = 0 - para linha / axis = 1 - para coluna)

tabela = tabela.dropna() # Dropna excluí todas as linhas se tiver UM valor VAZIO

print()
print("Informações da tabela")
print(tabela.info())

print()
print("Descrição dos itens")
print(tabela.describe().round(1)) # Arredonda para 1 casa decimal os valores da tabela

print("-="*25)

# Vamos avaliar como está a divisão entre Clientes vs Cancelados

qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True).round(2)
print(qtde_categoria_perc)

print("-="*25)

'''
  Temos varias formas de descobrir o motivo de cancelamento
    - Podemos olhar a comparação entre Clientes e Cancelados em cada uma das colunas da nossa base de dados, para ver se essa informação traz algum insight novo para a gente
'''

import plotly.express as px
import plotly.io as pio
import plotly
print(plotly.__version__)

# Força o gráfico a abrir no navegador padrão do seu sistema
pio.renderers.default = 'browser'

grafico = px.histogram(tabela, x = "Idade", color="Categoria")
print(grafico.show())