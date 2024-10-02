"""Intenta utilizar Matplotlib para crear una visualización de lanzamiento de dados y 
utiliza Plotly para hacer la visualización de una caminata aleatoria. 
(Necesitarás consultar la documentación de cada biblioteca para completar este ejercicio).
"""

""""USANDO PLOTLY"""

# No marca error, pero tarda en ejecutar el codigo, no siempre carga a la primera.

from random import choice
import plotly.graph_objs as go

class RandomWalks:
    """Clase para crear una caminata aleatoria"""

    def __init__(self, numero_puntos=5000):
        # Inicializamos atributos
        self.numero_puntos = numero_puntos
        # Todas las caminatas inician en 0,0
        self.valores_x = [0]
        self.valores_y = [0]

    def llenar_caminata(self):
        while len(self.valores_x) < self.numero_puntos:
            # Dirección y distancias para x
            direccion_x = choice([1, -1])  # Cambiado para permitir movimiento en ambas direcciones
            pasos_x = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            distancia_x = direccion_x * pasos_x

            # Dirección y distancia para y
            direccion_y = choice([1, -1])  # Cambiado para permitir movimiento en ambas direcciones
            pasos_y = choice([0, 1, 2])
            distancia_y = direccion_y * pasos_y

            # Validar que se va a mover de la posición actual
            if pasos_x == 0 and pasos_y == 0:
                continue
            
            # Incrementamos los valores en x y y
            x = self.valores_x[-1] + distancia_x
            y = self.valores_y[-1] + distancia_y
            # Agregamos los nuevos valores a la lista
            self.valores_x.append(x)
            self.valores_y.append(y)

    def graficar_caminata(self):
        # Crear la figura usando Plotly
        fig = go.Figure()
        
        # Añadir la caminata aleatoria al gráfico
        fig.add_trace(go.Scatter(x=self.valores_x, y=self.valores_y, mode='lines+markers', name='Caminata Aleatoria'))

        # Actualizar el diseño del gráfico
        fig.update_layout(title='Visualización de una Caminata Aleatoria',
                          xaxis_title='Posición X',
                          yaxis_title='Posición Y',
                          showlegend=True)

        # Mostrar el gráfico
        fig.show()

# Crear una instancia de RandomWalks
caminata = RandomWalks()
caminata.llenar_caminata()
caminata.graficar_caminata()