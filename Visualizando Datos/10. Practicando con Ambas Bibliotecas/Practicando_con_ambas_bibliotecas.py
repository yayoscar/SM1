# Código para Matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

num_lanzamientos = 1000
resultados = np.random.randint(1, 7, num_lanzamientos)
frecuencias = np.bincount(resultados)[1:]

fig, ax = plt.subplots()
ax.bar(range(1, 7), frecuencias, color='blue', alpha=0.7)
ax.set_xlabel('Resultado del Dado')
ax.set_ylabel('Frecuencia')
ax.set_title('Simulación de Lanzamientos de Dados')





num_pasos = 1000
pasos = np.random.choice([-1, 1], size=num_pasos)
posiciones = np.cumsum(pasos)

fig = go.Figure()
fig.add_trace(go.Scatter(x=list(range(num_pasos)), y=posiciones, mode='lines', name='Caminata Aleatoria'))
fig.update_layout(title='Visualización de Caminata Aleatoria', xaxis_title='Paso', yaxis_title='Posición')
fig.show()
plt.show()