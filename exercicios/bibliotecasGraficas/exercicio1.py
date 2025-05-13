import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração inicial
np.random.seed(42)

sns.set_style("whitegrid")  
plt.style.use('ggplot') 
# %matplotlib inline is specific to Jupyter notebooks and is not needed in standard Python scripts.

# Dados das turmas
turma_A = np.random.normal(7.5, 1.2, 50)
turma_B = np.random.normal(6.8, 1.5, 50)
turma_C = np.random.normal(8.0, 0.8, 50)

# Crie um dataframe com as turmas
data = {'turma A': turma_A, 'turma B': turma_B, 'turma C': turma_C}
df = pd.DataFrame(data)
df.index = range(1, len(df) + 1)
print(df)

# Transforme o dataframe para o formato longo
df_long = df.melt(var_name='Turma', value_name='Nota')

# Plot um boxplot
plt.subplot(2, 2, 1)
sns.boxplot(x='Turma', y='Nota', data=df_long, palette='pastel', showmeans=True,
            meanprops={"marker": "o", "markerfacecolor": "red", "markeredgecolor": "black"})
plt.title('Boxplot das Turmas')
plt.tight_layout()
plt.show()

# Respostas
# 1- Maior mediana: Turma C; Menor mediana: Turma B
# 2- Maior dispersão de notas: Turma B
# 3- Há presença de outliers em alguma turma? Se sim, em qual(is)?  Sim, na Turma B
# 4- Desempenho mais homogeneo: Turma C