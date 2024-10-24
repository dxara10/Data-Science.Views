import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

# Criar gráfico de barras
plt.bar(categorias, valores)
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')
plt.show()
