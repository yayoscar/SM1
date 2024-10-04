from dado import Dado
from plotly.graph_objs import Bar, Layout
from plotly import offline

dado_1=Dado(6)
dado_2=Dado(6)
dado_3=Dado(6)


resultados=[]

for numero_lanzamiento in range(100):
    resultado=dado_1.lanzar()+dado_2.lanzar()+dado_3.lanzar()
    resultados.append(resultado)


frecuencias=[]
maximo_resultado=dado_1.lados+dado_2.lados+dado_3.lados
for valor in range(3,maximo_resultado+1):
    frecuencia=resultados.count(valor)
    frecuencias.append(frecuencia)


valores_x=list(range(3, maximo_resultado+1))
datos=[Bar(x=valores_x, y=frecuencias)]
configuracion_eje_x={'title':'Resultado', 'dtick':1}
configuracion_eje_y={'title':'Frecuencia del Resultado'}
configuracion=Layout(title='Resultados del lanzamiento',
                        xaxis=configuracion_eje_x,
                        yaxis=configuracion_eje_y)
offline.plot({'data':datos, 'layout':configuracion},filename='dado_visual.html')

#jaris y alexa