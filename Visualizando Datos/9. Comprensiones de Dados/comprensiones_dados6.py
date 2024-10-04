# Para mayor claridad, los listados en esta sección utilizan la forma larga de los 
# bucles for. Si te sientes cómodo utilizando comprensiones de listas, intenta
# escribir una comprensión para uno o ambos bucles en cada uno de estos programas

from dado6 import Dado
from plotly.graph_objs import Bar, Layout
from plotly import offline

dado1 = Dado(6)
dado2 = Dado(6)
dado3 = Dado(6)

resultados = [dado1.lanzar() + dado2.lanzar() + dado3.lanzar() for _ in range(1000)]

maximo_resultado = dado1.lados + dado2.lados + dado3.lados
frecuencias = [resultados.count(valor) for valor in range(3, maximo_resultado + 1)]

valores_x = list(range(3, maximo_resultado + 1))
datos = [Bar(x=valores_x, y=frecuencias)]
configuracion_eje_x = {'title': 'Resultado', 'dtick': 1}
configuracion_eje_y = {'title': 'Frecuencia del Resultado'}
configuracion = Layout(title='Resultados del lanzamiento de tres dados de 6 lados',
                      xaxis=configuracion_eje_x,
                      yaxis=configuracion_eje_y)
offline.plot({'data': datos, 'layout': configuracion}, filename='tresD6.html')
