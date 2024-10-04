import random
import plotly.graph_objs as go
from plotly import offline

num_pasos = 1000
posiciones_x = [0]
posiciones_y = [0]

for i in range(num_pasos):
    paso_x = random.choice([1, -1])
    paso_y = random.choice([1, -1])
    
    nueva_posicion_x = posiciones_x[-1] + paso_x
    nueva_posicion_y = posiciones_y[-1] + paso_y
    
    posiciones_x.append(nueva_posicion_x)
    posiciones_y.append(nueva_posicion_y)

datos = go.Scatter(
    x=posiciones_x,
    y=posiciones_y,
    mode='markers+lines',
    marker=dict(size=5, color=list(range(num_pasos)), colorscale='Viridis', showscale=True),
    line=dict(color='blue', width=2)
)

configuracion = go.Layout(
    title='Caminata Aleatoria (1000 pasos)',
    xaxis=dict(title='Posición X'),
    yaxis=dict(title='Posición Y'),
    showlegend=False
)

offline.plot({'data': [datos], 'layout': configuracion}, filename='caminata_aleatoria.html')
