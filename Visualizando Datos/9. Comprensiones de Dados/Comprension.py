from dado import Dado
from plotly.graph_objs import Bar,Layout
from plotly import offline

dado_1=Dado()
dado_2=Dado()
dado_3=Dado()

resultados=[]

for _ in range(1000):
    resultado=dado_1.lanzar() + dado_2.lanzar() + dado_3.lanzar() 
    resultados.append(resultado)

maximoResultados=dado_1.lados + dado_2.lados + dado_3.lados
frecuencias=[resultados.count(valor) for valor in range(3,maximoResultados+1)]

valores_x=list(range(3,maximoResultados + 1))
datos= [Bar(x=valores_x,y=frecuencias)]

configuracion_eje_x={'title':'resultado','dtick':1}
configuracion_eje_y= {'title':'frecuencia de resultados'}
configuracion=Layout(title='Resultado del lanzamiento de 3 dados de 6 lados',
                     xaxis=configuracion_eje_x,
                     yaxis=configuracion_eje_y)
offline.plot({'data':datos,'layout':configuracion},filename='comprensiones_de_Dados.html')