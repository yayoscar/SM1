#Cuando lanzas 3 dados d6, el numero mas pequeño que piuedes obtener es 3 y el numero mas grande es 18. 
# Crea una visualizacion que muestre lo que sucede cuando lanzas 3 dados d6
#lanzar dos dados de 8 caras mil veces. Ver la visualicion antes de ejecutar la simulacion; 
# aumenta gradualmente el numero de lanzamientos hasta que comiences a ver los limites de las capacidades de tu sistema

from plotly.graph_objs import Bar,Layout
from dado import Dado
from plotly import offline
#crear 2 dadoos
dado1=Dado()
dado2=Dado()
dado3=Dado()

#lanza el dado 1000 veces y guradalo en una linea
resultados=[]

for lanzamiento in range(1000):
    resultado=dado1.lanzar()+dado2.lanzar()+dado3.lanzar()
    resultados.append(resultado)
    
#analiza los resultados
frecuencias=[]
maximo_resultado= dado1.lados+ dado2.lados +dado3.lados
for valor in range(3, maximo_resultado+1):
    frecuencia=resultados.count(valor)
    frecuencias.append(frecuencia)
    
#visualizar los resultados

valores_x=list(range(3,maximo_resultado+1))
datos=[Bar(x=valores_x, y=frecuencias)]
configuracion_eje_x={'title':'Resultado','dtick':1}
configuracion_eje_y={'title':'Frecuencia del resultado'}
configuracion=Layout(title='Resultados del lanzamiento de 3 dados', xaxis=configuracion_eje_x, yaxis=configuracion_eje_y)
offline.plot({'data':datos, 'layout':configuracion}, filename='dado_visual.html')
xaxis=configuracion_eje_x,yaxis=configuracion_eje_y
offline.plot({'data':datos, 'layout':configuracion}, filename='dado_visual.html' )
