#1. Cubos: Un número elevado a la tercera potencia es un cubo. Grafica los primeros cinco
#números cúbicos y luego grafica los primeros 5000 números cúbicos.

#2. Cubos Coloreados: Aplica un mapa de colores a tu gráfico de cubos.

import matplotlib.pyplot as plt

#datos a graficas
valores_x_5=range(1, 6) #de los primeros 5 numeros
valores_y=[x**3 for x in valores_x_5] 

#para los primeros 5000 numeros
valores_x_5mil=range(1, 5001)
valores_y_5mil=[x**3 for x in valores_x_5mil] 

#agregar estilos
plt.style.use('seaborn-v0_8-dark-palette')

#crear figura y ejes
fig,ax=plt.subplots()

#agregar un punto a la grafica de los primeros 5 numeros
ax.scatter(valores_x_5,valores_y, c=valores_y, cmap=plt.cm.PuBuGn, s=10) #(1,1)(2,4)(3,9)(4,16)(5,25)

#establecer el titulo del grafico y etiqueta de los ejes
ax.set_title("Primeros 5 números",fontsize=24)
ax.set_xlabel("Valor",fontsize=14)
ax.set_ylabel("Cubo del valor",fontsize=14)

#ajustar el tamaño de las etiquetas de los ejes de los primeros 5 numeros
ax.tick_params(axis='both',labelsize=14)

#establecer el rango para cada eje de los primeros 5 numeros
ax.axis([0,6, 0,150])

########## PRIMEROS 5000 NUMEROS ##########

#agregar un punto a la grafica de los primeros 5000 numeros
ax.scatter(valores_x_5mil,valores_y_5mil, c=valores_y_5mil, cmap=plt.cm.PuBuGn, s=10) #(1,1)(2,4)(3,9)(4,16)(5,25)

#establecer el titulo del grafico y etiqueta de los ejes
ax.set_title("Primeros 5000 números",fontsize=24)
ax.set_xlabel("Valor",fontsize=14)
ax.set_ylabel("Cubo del valor",fontsize=14)

#ajustar el tamaño de las etiquetas de los ejes de los primeros 5 numeros
ax.tick_params(axis='both',labelsize=14)

#establecer el rango para cada eje de los primeros 5 numeros
ax.axis([0,5000, 0,150000000000])

#mostrar la grafica
plt.show() 