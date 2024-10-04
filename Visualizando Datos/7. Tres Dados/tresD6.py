# Cuando lanzas tres dados D6, el número más pequeño que puedes obtener es 3
# y el número más grande es 18. Crea una visualización que muestre lo que sucede
# cuando lanzas tres dados D6.

from dado6 import Dado
from plotly.graph_objs import Bar,Layout
from plotly import offline

dado1 = Dado(6)
dado2 = Dado(6)
dado3 = Dado(6)

resultados=[]
for lanzamiento in range(1000):
    resultado = dado1.lanzar()+dado2.lanzar()+dado3.lanzar()
    resultados.append(resultado)
    
frecuencias = []
maximo_resultado=dado1.lados+dado2.lados+dado3.lados
for valor in range(3, maximo_resultado+1):
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)
    
valores_x=list(range(3,maximo_resultado+1))
datos=[Bar(x=valores_x, y=frecuencias)]
configuracion_eje_x= {'title':'Resultado','dtick':1}
configuracion_eje_y= {'title':'Frecuencia del Resultado'}
configuracion= Layout(title='Resultados del lanzamiento de tres dados de 6 lados',
                      xaxis=configuracion_eje_x,
                      yaxis=configuracion_eje_y)
offline.plot({'data':datos, 'layout':configuracion},filename='tresD6.html')