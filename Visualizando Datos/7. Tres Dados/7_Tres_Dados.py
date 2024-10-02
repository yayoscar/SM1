"""Cuando lanzas tres dados D6, el número más pequeño que puedes obtener es 3 y el número más grande es 18.
Crea una visualización que muestre lo que sucede cuando lanzas tres dados D6."""
from dado import Dado
from plotly.graph_objs import Bar,Layout
from plotly import offline

#crear dos dados de 6 lados
dado_1=Dado()
dado_2=Dado()
dado_3=Dado()

#lanza el dado 100 veces y guardalo en una lista e imprime el resultado
resultados=[]

for lanzamiento in range(1000):
    resultado=dado_1.lanzar()+dado_2.lanzar()+dado_3.lanzar()
    resultados.append(resultado)

#analizar resultados
frecuencias=[]
maximo_resultados=dado_1.lados+dado_2.lados+dado_3.lados
for valor in range (3,maximo_resultados+1):
    frecuencia=resultados.count(valor)
    frecuencias.append(frecuencia)

#visualizar los resultados
valores_x=list(range(2,maximo_resultados+1))
datos=[Bar(x=valores_x,y=frecuencias)]
configuracion_eje_x={'title':'Resultado','dtick':1}
configuracion_eje_y={'title':'Frecuencia del resultado'}
configuracion=Layout(title='Resultados del lanzamiento de 3 dados de 6 caras',
                     xaxis=configuracion_eje_x,
                     yaxis=configuracion_eje_y)
offline.plot({'data':datos,'layout':configuracion},filename='dado_visual.html')
 