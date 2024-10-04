import matplotlib.pyplot as plt

#datos a graficar
valores_x=range(1,5001)
valores_y=[x**3 for x in valores_x]

#agregar estilo
plt.style.use('seaborn-v0_8')

#Crear figura y ejes
fig, ax=plt.subplots()

#agregar un punto a la grafica
ax.scatter(valores_x, valores_y, c=valores_y,cmap=plt.cm.PuBuGn, s=5) #(1,1)(2,4)(3,9)(4,6)(5,25)

#establecer el titulo del grafico y etiquetas de los ejes
ax.set_title("Numeros al cubo",fontsize=24)
ax.set_xlabel("Valor",fontsize=14)
ax.set_ylabel("cubo del valor",fontsize=14)

#ajustar el tamaño de las etiquetas de los ejes
ax.tick_params(axis="both",labelsize=14)

#establecer el rango para cada eje
ax.axis([0, 1100, 0, 1100000])

#crear grafica
plt.savefig('scatter_con_ciclo.png', bbox_inches='tight')
plt.scatter(valores_x, valores_y, color='blue')
plt.show()