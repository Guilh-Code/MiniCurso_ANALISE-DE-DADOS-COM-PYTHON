import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Lê o CSV com encoding latin1
tabela = pd.read_csv("Projeto/ClientesBanco.csv", encoding="latin1")

# Remove colunas e valores ausentes
tabela = tabela.drop("CLIENTNUM", axis=1) # Drop -> deleta colunas ou linhas (axis = 0 - para linha / axis = 1 - para coluna)
tabela = tabela.dropna()

# Informações básicas da tabela
print("\nInformações da tabela")
print(tabela.info())

print("\nDescrição dos itens")
print(tabela.describe().round(1))

print("-="*25)

# Quantidade absoluta e percentual por Categoria
qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True).round(2)
print(qtde_categoria_perc)

print("-="*25)

'''
  Temos varias formas de descobrir o motivo de cancelamento
    - Podemos olhar a comparação entre Clientes e Cancelados em cada uma das colunas da nossa base de dados, para ver se essa informação traz algum insight novo para a gente
'''



# Criar pasta "graficos" se não existir
pasta = "graficos"
os.makedirs(pasta, exist_ok=True)

# Loop pelas colunas numéricas da tabela
for coluna in tabela.select_dtypes(include='number').columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=tabela, x=coluna, hue="Categoria", bins=20, palette="Set2")
    
    # Título e rótulos dinâmicos
    plt.title(f"Distribuição de {coluna} por Categoria de Cliente")
    plt.xlabel(coluna)
    plt.ylabel("Quantidade")
    
    plt.tight_layout()
    
    # Caminho e nome do arquivo
    caminho_arquivo = os.path.join(pasta, f"{coluna}_distribuicao.jpg")
    plt.savefig(caminho_arquivo, format='jpg', dpi=300)  # Salva com alta resolução
    
