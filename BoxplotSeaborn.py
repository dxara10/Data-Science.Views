import seaborn as sns
import numpy as np

# Dados
dados = np.random.normal(loc=0, scale=1, size=100)

# Criar boxplot com Seaborn
sns.boxplot(data=dados)
plt.xlabel('Valores')
plt.title('Boxplot')
plt.show()
