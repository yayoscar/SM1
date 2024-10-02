from dado import Dado 
from plotly.graph_objs import Bar,Layout
from plotly import offline


dado_1= Dado()
dado_2= Dado()

resultados=[]

for lanzamiento in range(1000):
    resultado=dado_1.lanzar()*dado_2.lanzar()
    resultados.append(resultado)
 
frecuencias=[]

maximo_resultado= dado_1.lados * dado_2.lados
for valor in range(2, maximo_resultado+1):
    frecuancia= resultados.count(valor)
    frecuencias.append(frecuancia)

valores_x=list(range(2, maximo_resultado+1))
datos=[Bar(x=valores_x, y=frecuencias)]
configuracion_eje_x={'title':'Resultado','dtick':1}
configuracion_eje_y={'title':'Frecuencia del resultado'}
configuracion=Layout(title='Resultado del lanzamiento de dos dados de 6 lados',
                     xaxis=configuracion_eje_x,
                     yaxis=configuracion_eje_y)
offline.plot({'data':datos, 'layout':configuracion}, filename='dado_visual.html')