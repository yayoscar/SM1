#Crea una simulación que muestre lo que sucede cuando lanzas dos dados de ocho caras
# 1000 veces. Intenta imaginar cómo crees que se verá la visualización antes de
# ejecutar la simulación; luego verifica si tu intuición era correcta.
# Aumenta gradualmente el número de lanzamientos hasta que comiences a ver los
# límites de las capacidades de tu sistema.

from dado8 import Dado
from plotly.graph_objs import Bar,Layout
from plotly import offline

dado1 = Dado(8)
dado2 = Dado(8)

resultados=[]
for lanzamiento in range(1000):
    resultado = dado1.lanzar()+dado2.lanzar()
    resultados.append(resultado)
    
frecuencias = []
maximo_resultado=dado1.lados+dado2.lados
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
offline.plot({'data':datos, 'layout':configuracion},filename='dosD8.html')