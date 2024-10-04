"""Intenta utilizar Matplotlib para crear una visualización de lanzamiento de dados y 
utiliza Plotly para hacer la visualización de una caminata aleatoria. 
(Necesitarás consultar la documentación de cada biblioteca para completar este ejercicio).
"""

import plotly.graph_objects as go
import numpy as np

# Crear la clase RandomWalk
class RandomWalk:
    """Una clase para generar caminatas aleatorias."""
    
    def __init__(self, num_puntos=5000):
        """Inicializar los atributos de una caminata."""
        self.num_puntos = num_puntos
        self.valores_x = [0]
        self.valores_y = [0]

    def llenar_caminata(self):
        """Calcular todos los puntos en la caminata."""
        while len(self.valores_x) < self.num_puntos:
            # Generar aleatoriamente dirección y distancia para x
            direccion_x = np.random.randint(2) * 2 - 1 
            distancia_x = np.random.randint(0, 5)  
            paso_x = direccion_x * distancia_x
            
            # Generar aleatoriamente dirección y distancia para y
            direccion_y = np.random.randint(2) * 2 - 1  
            distancia_y = np.random.randint(0, 5)  
            paso_y = direccion_y * distancia_y

            if paso_x == 0 and paso_y == 0:
                continue

            x = self.valores_x[-1] + paso_x
            y = self.valores_y[-1] + paso_y

            self.valores_x.append(x)
            self.valores_y.append(y)

# Crear una instancia de RandomWalk y generar los puntos
rw = RandomWalk(5000)
rw.llenar_caminata()

# Convertir el rango a una lista
colors = list(range(rw.num_puntos))

# Crear la figura usando Plotly
fig = go.Figure(data=go.Scatter(
    x=rw.valores_x,
    y=rw.valores_y,
    mode='markers',
    marker=dict(
        color=colors,  # Cambiado a lista
        colorscale='Viridis',
        size=5,
        colorbar=dict(title='Número de pasos')
    )
))

# Configuración del layout
fig.update_layout(
    title='Caminata Aleatoria con Plotly',
    xaxis_title='Coordenada X',
    yaxis_title='Coordenada Y',
    showlegend=False
)

# Mostrar la figura
fig.show()
