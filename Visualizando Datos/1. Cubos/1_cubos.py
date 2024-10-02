""" Un número elevado a la tercera potencia es un cubo. 
Grafica los primeros cinco números cúbicos y luego grafica los primeros 5000 números cúbicos."""
import matplotlib.pyplot as plt

#datos para graficar
#valores de entrada y cubos de los valores
valores_entrada=[1,2,3,4,5]
cubos=[1,8,27,64,125]

#utiliza un estilo de gráfica
plt.style.use('seaborn-v0_8')

#crear figura y ejes
fig,ax=plt.subplots()

#grafica de datos
ax.plot(valores_entrada,cubos,linewidth=5)

#establecer titulos
ax.set_title("Números cubos",fontsize=14)
ax.set_xlabel("Valor",fontsize=14)
ax.set_ylabel("Cubo del Valor",fontsize=14)

#ajustar el tamaño de etiquetas de los ejes
ax.tick_params(axis="both",labelsize=14)

#mostrar la gráfica
plt.show()