import matplotlib.pyplot as plt
import random

# Generar datos de lanzamiento de dados
dados = [random.randint(1, 6) for _ in range(1000)]

# Crear la visualización
plt.hist(dados, bins=6, edgecolor='black')
plt.title("Distribución de Lanzamiento de Dados")
plt.xlabel("Valor del Dado")
plt.ylabel("Frecuencia")
plt.show()

import plotly.graph_objs as go
import random

# Generar una caminata aleatoria
x_values = [0]
y_values = [0]
[x_values.append(x_values[-1] + random.choice([-1, 1])) for _ in range(100)]
[y_values.append(y_values[-1] + random.choice([-1, 1])) for _ in range(100)]

# Crear la visualización
fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines+markers'))
fig.update_layout(title="Caminata Aleatoria con Plotly",
                  xaxis_title="Paso",
                  yaxis_title="Posición")
fig.show()