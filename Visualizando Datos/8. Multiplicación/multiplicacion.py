# Cuando lanzas dos dados, generalmente sumas los dos números para obtener
# el resultado. Crea una visualización que muestre lo que sucede si multiplicas
# estos números en su lugar.

from multiplicacion_dado import Dado
from plotly.graph_objs import Bar,Layout
from plotly import offline

dado1 = Dado()
dado2 = Dado()

resultados=[]
for lanzamiento in range(1000):
    resultado = dado1.lanzar()*dado2.lanzar()
    resultados.append(resultado)
    
frecuencias = []
maximo_resultado=dado1.lados*dado2.lados
for valor in range(3, maximo_resultado+1):
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)
    
valores_x=list(range(3,maximo_resultado+1))
datos=[Bar(x=valores_x, y=frecuencias)]
configuracion_eje_x= {'title':'Resultado','dtick':1}
configuracion_eje_y= {'title':'Frecuencia del Resultado'}
configuracion= Layout(title='Resultados del lanzamiento de dos dados de 8 lados',
                      xaxis=configuracion_eje_x,
                      yaxis=configuracion_eje_y)
offline.plot({'data':datos, 'layout':configuracion},filename='multiplicacion.html')