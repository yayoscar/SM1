#mpl_cuadrados.py
import matplotlib.pyplot as plt

#Lista de datos a graficar valores de entrada y cubos de los valores
valores_x=range(1,5001)
valores_y=[x**3 for x in valores_x]

#usar un estilo predefinido de grafica
plt.style.use('seaborn-v0_8')

#crear figura y eje
fig, ax=plt.subplots()


#Grafica los datos y ajustar el ancho de la linea
ax.plot(valores_x, valores_y, linewidth=5)

#restablecer titulo
ax.set_title("Numeros del cubo",fontsize=24)
ax.set_xlabel("Valor",fontsize=14)
ax.set_ylabel("cubo del valor",fontsize=14)

#ajustar el tamaño de las etiquetas de los ejes
ax.tick_params(axis="both",labelsize=17)

#crear grafio
plt.show()

#jaris y alexa

