"""Para mayor claridad, los listados en esta sección utilizan la forma larga de los bucles `for`. 
Si te sientes cómodo utilizando comprensiones de listas, intenta escribir una comprensión para uno
o ambos bucles en cada uno de estos programas."""

from dado import Dado
from plotly.graph_objs import Bar, Layout
from plotly import offline


dado_1 = Dado()
dado_2 = Dado()
dado_3 = Dado()

resultados = [dado_1.lanzar() + dado_2.lanzar() + dado_3.lanzar() for _ in range(1000)]

maximo_resultados = dado_1.lados + dado_2.lados + dado_3.lados
frecuencias = [resultados.count(valor) for valor in range(3, maximo_resultados + 1)]

valores_x = list(range(3, maximo_resultados + 1))  
datos = [Bar(x=valores_x, y=frecuencias)]

configuracion_eje_x = {'title': 'Resultado', 'dtick': 1}
configuracion_eje_y = {'title': 'Frecuencia del resultado'}
configuracion = Layout(title='Resultados del lanzamiento de 3 dados de 6 caras',
                       xaxis=configuracion_eje_x,
                       yaxis=configuracion_eje_y)
offline.plot({'data':datos, 'layout':configuracion}, filename='dado_visual.html')
