import matplotlib.pyplot as plt
import pandas as pd

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] 
vendas = [120, 150, 130, 170, 200, 240, 260, 250, 230, 210, 190, 220]

#Gráfico de linhas sobre isso
plt.plot(meses, vendas, marker='o', color='purple', linestyle='-', linewidth=4)
plt.title("Vendas Mensais")
plt.xlabel("Meses")
plt.ylabel("Vendas")
plt.legend(["Vendas"])
plt.grid(True)
plt.show()

# Gráfico de barras
plt.bar(meses, vendas, color='blue')
plt.title("Vendas Mensais")
plt.xlabel("Meses")
plt.ylabel("Vendas")
plt.show()

#1: Qual desses gráficos é o mais adequado para este conjunto de dados?
#Por quê? Justifique sua resposta e cite ao menos três motivos pela sua escolha.
#Na minha visão, o gráfico de linhas é bem mais adequado para este conjunto de dados. Primeiramente que 
#pra mim, fica mais fácil de visualizar a tedência de vendas ao longo do ano. Também é mais bonito.
#E por fim, da pra saber mais facilmente qual foi o mês com maior e menor venda só de bater o olho.

#2: No gráfico, é possível notar alguma tendência ou padrão ou extrair alguma informação relevante? Justifique sua resposta.
#Sim, da pra perceber que ao longo do ano, desde o começo até o meio, as vendas foram aumentando, depois decairam e por fim, 
#aumentaram um poquinho.