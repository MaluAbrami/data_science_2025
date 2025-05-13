import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Dados das disciplinas
matematica = np.random.normal(6.5, 1.8, 200)
portugues = np.random.normal(7.2, 1.2, 200)

# Crie um dataframe
data = {'Matemática': matematica, 'Português': portugues}
df = pd.DataFrame(data)
df.index = ['Aluno' + ' ' + str(i) for i in range(1, len(df) + 1)]
print(df)

# Mostre os valores de média e desvio padrão para as duas disciplinas
media_mat = matematica.mean()
dp_mat = matematica.std()

print("Matemática:")
print(f"Média: {media_mat:.2f}")
print(f"Desvio padrão: {dp_mat:.2f}\n")


media_port = portugues.mean()
dp_port = portugues.std()

print("Português:")
print(f"Média: {media_port:.2f}")
print(f"Desvio padrão: {dp_port:.2f}")

# 1- Um aluno tirou 8.5 em Matemática e 7.8 em Português. Em qual disciplina ele se saiu melhor em relação à turma?

# Calcula o z-score para Matemática e Português
z_score_mat = (8.5 - media_mat) / dp_mat
z_score_port = (7.8 - media_port) / dp_port

print("\nResposta questão 1:")
# Compara os z-scores
if z_score_mat > z_score_port:
    print("O aluno se saiu melhor em Matemática em relação à turma.")
elif z_score_mat < z_score_port:
    print("O aluno se saiu melhor em Português em relação à turma.")
else:
    print("O aluno teve desempenho equivalente nas duas disciplinas em relação à turma.")

# 2- Qual nota em Português seria equivalente a uma nota de 5.0 em Matemática (em termos de posição relativa)?
nota_matematica = 5
z_matematica = (5 - media_mat) / dp_mat

print("\nResposta questão 2:")
nota_portugues = z_matematica * dp_port + media_port
print(f"A nota em portguês equivalente a nota 5 em matemática é: {nota_portugues:.2f}")

# 3- Se um aluno está no percentil 75 em Matemática, qual seria a nota equivalente em Português?
print("\nResposta questão 3")

percentil_mat_75 = stats.norm.ppf(0.75, media_mat, dp_mat)
print(f"Nota do aluno no percentil 75 em matemática: {percentil_mat_75:.2f}")

percentil_port_75 = stats.norm.ppf(0.75, media_port, dp_port)
print(f"Nota do aluno no percentil 75 em portguês: {percentil_port_75:.2f}")


# 4-Em qual disciplina há maior variabilidade relativa no desempenho dos alunos?
print("\nResposta questão 4")
cv_mat = (dp_mat / media_mat) * 100
cv_port = (dp_port / media_port) * 100

print(f"Coeficiente de Variação - Matemática: {cv_mat:.2f}%")
print(f"Coeficiente de Variação - Português: {cv_port:.2f}%")

if cv_mat > cv_port:
    print("Há maior variabilidade relativa em Matemática")
else:
    print("Há maior variabilidade relativa em Português")