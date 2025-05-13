import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Dados dos restaurantes
restaurante_X = np.random.normal(30, 5, 500)
restaurante_Y = np.random.normal(35, 7, 500)

data = {'Restaurante X': restaurante_X, 'Restaurante Y': restaurante_Y}
df = pd.DataFrame(data)

df_long = df.melt(var_name='Restaurante', value_name='Minutos')

# Cire um Boxplot comparativo entre os restaurantes
plt.subplot(2,2,1)
sns.boxplot(x='Restaurante', y='Minutos', data=df_long, palette='pastel', showmeans=True,
            meanprops={"marker":"o","markerfacecolor":"red", "markeredgecolor":"black"})
plt.title('Boxplot de Distribuições de Tempo Entrega')
plt.tight_layout()
plt.show()


# Histograma superposto
plt.figure(figsize=(10, 6))
sns.histplot(restaurante_X, kde=True, color='blue', label='Restaurante X', alpha=0.5)
sns.histplot(restaurante_Y, kde=True, color='red', label='Restaurante Y', alpha=0.5)
plt.title('Distribuição de Tempos de Entrega')
plt.xlabel('Minutos')
plt.legend()
plt.show()

# 1- Qual restaurante tem o tempo médio de entrega menor? E qual tem maior variabilidade?
media_restaurante_x = restaurante_X.mean()
media_restaurante_y = restaurante_Y.mean()

print("\nResposta questão 1")

if media_restaurante_x < media_restaurante_y:
    print(f"O restaurante X tem um tempo médio de entrega menor: {media_restaurante_x:.2f} minutos")
else:
    print(f"O restaurante Y tem um tempo médio de entrega menor: {media_restaurante_y:.2f} minutos")


dp_x = restaurante_X.std()
dp_y = restaurante_Y.std()

cv_x = (dp_x / media_restaurante_x) * 100
cv_y = (dp_y / media_restaurante_y) * 100

if cv_x > cv_y:
    print(f"O restaurante X tem maior variablidade com um coeficiente de variância de: {cv_x:.2f}%")
else:
    print(f"O restaurante Y tem maior variablidade com um coeficiente de variância de: {cv_y:.2f}%")

# 2- Calcule a probabilidade de cada restaurante entregar em menos de 25 minutos.
z_25_x = (25 - media_restaurante_x) / dp_x
z_25_y = (25 - media_restaurante_y) / dp_y

prob_x = stats.norm.cdf(z_25_x)
prob_y = stats.norm.cdf(z_25_y)

print("\nResposta questão 2")
print(f"A probabilidade do restaurante X entregar em menos de 25 minutos é de {prob_x*100:.2f}%")
print(f"A probabilidade do restaurante Y entregar em menos de 25 minutos é de {prob_y*100:.2f}%")

# 3- Se um cliente quer ter 95% de chance de receber seu pedido em até X minutos, qual seria X para cada restaurante?
print("\nResposta questão 3")

tempo_x = stats.norm.ppf(0.95, loc=media_restaurante_x, scale=dp_x)
tempo_y = stats.norm.ppf(0.95, loc=media_restaurante_y, scale=dp_y)

print(f"Para o restaurante X ele precisaria esperar até {tempo_x:.2f} minutos")
print(f"Para o restaurante Y ele precisaria esperar até {tempo_y:.2f} minutos")

# 4- Um tempo de 40 minutos seria considerado atípico para algum dos restaurantes? Justifique usando z-scores.
print("\nResposta questão 4")

z_40_x = (40 - media_restaurante_x) / dp_x
z_40_y = (40 - media_restaurante_y) / dp_y

if z_40_x >= 2:
    print(f"40 minutos é atípico para o restaurante X já que possui um z-score de {z_40_x:.2f}")
else: 
    print(f"40 minutos não é atípico para o restaurante X já que possui um z-score de {z_40_x:.2f}")

if z_40_y >= 2:
    print(f"40 minutos é atípico para o restaurante Y já que possui um z-score de {z_40_y:.2f}")
else:
    print(f"40 minutos não é atípico para o restaurante Y já que possui um z-score de {z_40_y:.2f}")