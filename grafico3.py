import matplotlib.pyplot as plt

# Dados fornecidos
total_admissoes = 53
total_rescisoes = 55

# Calcular a média de admissões e demissões
media_total = (total_admissoes + total_rescisoes) / 2

# Dados para o gráfico
labels = ['Admissões', 'Demissões', 'Média']
values = [total_admissoes, total_rescisoes, media_total]
colors = ['lightgreen', 'lightcoral', 'lightskyblue']

# Gerando o gráfico de barras
plt.figure(figsize=(7, 5))
plt.bar(labels, values, color=colors)
plt.title('Admissões, Demissões e Média')
plt.xlabel('Categoria')
plt.ylabel('Número Total')
plt.tight_layout()

# Exibir o gráfico
plt.show()

# Exibindo a média
print(f"Média de Admissões e Demissões: {media_total}")

