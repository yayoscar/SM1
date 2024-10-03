"""Para mayor claridad, los listados en esta sección utilizan la forma larga de los bucles `for`. 
Si te sientes cómodo utilizando comprensiones de listas, intenta escribir una comprensión para uno
o ambos bucles en cada uno de estos programas."""

from dado import Dado
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Crear dos dados de 6 lados
dado_1 = Dado()
dado_2 = Dado()

#Lanza el dado 1000 veces y guardar el resultado en una lista
resultados = [dado_1.lanzar() * dado_2.lanzar() for lanzamiento in range(1000)]

#Analizamos los resultados
resultados_max = dado_1.lados * dado_2.lados
frecuencias = [resultados.count(valor) for valor in range(2, resultados_max + 1)]

#Visualizamos los resultados
valores_x = list(range(2, resultados_max + 1))
datos = [Bar(x=valores_x, y=frecuencias)]
configuracion_eje_x = {'title': 'Resultado', 'dtick': 1}
configuracion_eje_y = {'title': 'Frecuencia del resultado'}
configuracion = Layout(title='Resultados del lanzamiento de la multiplicación de la suma de dos dados de 6 caras',
                       xaxis=configuracion_eje_x,
                       yaxis=configuracion_eje_y)

offline.plot({'data': datos, 'layout': configuracion}, filename='dado_visual.html')
