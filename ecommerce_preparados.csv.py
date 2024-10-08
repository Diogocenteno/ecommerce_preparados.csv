import pandas as pd

# Carregar o DataFrame e remover NaNs
df = pd.read_csv('/data/ecommerce_preparados.csv')
df = df.dropna()

# Cálculo das estatísticas
media = df['Desconto'].mean()  # Média dos descontos
mediana = df['Desconto'].median()  # Mediana dos descontos
variancia = df['Desconto'].var()  # Variância dos descontos
desvio_padrao = df['Desconto'].std()  # Desvio padrão dos descontos

# A função mode() retorna uma Série, então pegamos o primeiro elemento
moda = df['Desconto'].mode()[0]  # Moda dos descontos

minimo = df['Desconto'].min()  # Valor mínimo do desconto
quartis = df['Desconto'].quantile([0.25, 0.5, 0.75])  # Quartis dos descontos
maximo = df['Desconto'].max()  # Valor máximo do desconto

# Exibe as primeiras linhas do DataFrame
print(df.head())

# Exibindo as estatísticas calculadas
print("Média dos descontos:", media)
print("Mediana dos descontos:", mediana)
print("Variância dos descontos:", variancia)
print("Desvio padrão dos descontos:", desvio_padrao)
print("Moda dos descontos:", moda)
print("Valor mínimo do desconto:", minimo)
print("Quartis dos descontos:\n", quartis)
print("Valor máximo do desconto:", maximo)
