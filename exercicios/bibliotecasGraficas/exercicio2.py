import numpy as np
# import pandas as pd (removido porque não é utilizado)
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Dados de altura
alturas = np.random.normal(170, 8, 1000)

# Plot o histograma
plt.figure(figsize=(12, 5))

plt.subplot(1,2,1)
sns.histplot(alturas, bins=15, kde=True, color='salmon')  # Corrigido para usar o array diretamente
plt.title('Histograma de Alturas')
plt.xlabel('Altura')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# Estatísticas descritivas
media = np.mean(alturas)
desvio_padrao = np.std(alturas)

print(f"Média: {media:.2f} cm")
print(f"Desvio padrão: {desvio_padrao:.2f} cm")

#Respostas

# 1
altura_alvo = 185
z_185 = (altura_alvo - media) / desvio_padrao
print(f"Z-score para 185 cm: {z_185:.2f}")

# 2
z_160 = (160 - media) / desvio_padrao
prob_160 = stats.norm.cdf(z_160)
print(f"Probabilidade de altura < 160 cm: {prob_160*100:.2f}%")

# 3 
z_165 = (165 - media) / desvio_padrao
z_175 = (175 - media) / desvio_padrao
prob_165_175 = stats.norm.cdf(z_175) - stats.norm.cdf(z_165)
print(f"Probabilidade de altura entre 165 cm e 175 cm: {prob_165_175*100:.2f}%")

# 4
altura_p90 = stats.norm.ppf(0.90, loc=media, scale=desvio_padrao)
print(f"Altura no percentual 90: {altura_p90:.2f} cm")