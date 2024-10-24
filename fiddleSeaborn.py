import seaborn as sns
import numpy as np

# Dados
dados = np.random.normal(loc=0, scale=1, size=100)

# Criar gráfico de violino com Seaborn
sns.violinplot(data=dados)
plt.xlabel('Valores')
plt.title('Gráfico de Violino')
plt.show()
