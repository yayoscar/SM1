import matplotlib.pyplot as plt

# Lista de datos a graficar valores de entrada y cubos de los valores
valores_entrada = [1, 2, 3, 4, 5]
cubos = [1, 4, 9, 16, 25]

# Crear la figura y los ejes
fig,ax=plt.subplots()

# Graficar los datos y ajustar el ancho de la linea
ax.plot(valores_entrada, cubos,linewidth=5)

# Establecer título del gráfico y etiquetas de los ejes
ax.set_title("Números Cubos", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Cubos del Valor", fontsize=14)

# Ajustar el tamaño de las etiquetas de las marcas de los ejes
ax.tick_params(axis='both', labelsize=14)

# Mostrar la gráfica
plt.show()