from dado import Dado
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Crea una instancia de un dado de 6 lados
dado_1 = Dado()
dado_2 = Dado()
dado_3 = Dado()

# Lanza el dado 1000 veces y guarda los resultados en una lista
resultados = []

for _ in range(1000):
    resultado = dado_1.lanzar()+dado_2.lanzar()+dado_3.lanzar()
    resultados.append(resultado)  # Aquí guardamos el resultado en la lista 'resultados'

# Analizar los resultados 
frecuencias = []
maximo_resultado=dado_1.lados+dado_2.lados+dado_3.lados
for valor in range(3,19):
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)

# Visualizar los resultados
valores_x = list(range(3,19))
datos = [Bar(x=valores_x, y=frecuencias)]
configuracion_eje_x = {'title': 'Resultado', 'dtick': 1}
configuracion_eje_y = {'title': 'Frecuencia del resultado'}
configuracion = Layout(title='Resultados de los lanzamientos de 2 dados de 8 lados',
                       xaxis=configuracion_eje_x,
                       yaxis=configuracion_eje_y)
offline.plot({'data': datos, 'layout': configuracion}, filename='dado_visual.html')
