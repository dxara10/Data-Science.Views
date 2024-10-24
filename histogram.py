import matplotlib.pyplot as plt
import numpy as np

# Dados
dados = np.random.randn(1000)

# Criar histograma
plt.hist(dados, bins=30)
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.show()
