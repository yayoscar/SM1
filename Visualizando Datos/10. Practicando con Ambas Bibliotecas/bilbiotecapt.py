import random
import plotly.graph_objs as go
from plotly import offline

#Generar una caminata aleatoria
x_values=[0]
y_values=[0]

for _ in range(1000):
    x_step=random.choice([1,-1])
    y_step=random.choice([1,-1])
    x_values.append(x_values[-1]+x_step)
    y_values.append(y_values[-1]+y_step)

#Crear la gráfica de la caminata aleatoria
datos=go.Scatter(x=x_values, y=y_values, mode='markers', marker=dict(size=8,color='red'))

#Configurar el layout del gráfico
layout=go.Layout(title="Caminata Aleatoria", xaxis={'title': 'Paso X'},yaxis={'title': 'Paso Y'})

#Mostrar la gráfica
offline.plot({'data': [datos], 'layout': layout}, filename='caminata_aleatoria.html')
