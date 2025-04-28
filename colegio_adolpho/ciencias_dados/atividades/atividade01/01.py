import pandas as pd
dados = [10, 20, 30, 40, 50]
matriz = [
    ['Arthur', 25, 'Brasilia'],
    ['Bruno', 30, 'São Paulo'],
    ['Danilo', 22, 'Belo Horizonte']
]
series = pd.Series (dados)
print(series)
df = pd.DataFrame(matriz, columns=['Nome', 'Idade', 'Cidade'])
print(df['Nome'])
df['Profissão']=['Cantor', 'Médico', 'Pintor']
print(df)
filtro = df['Idade']>25
print(df[filtro])