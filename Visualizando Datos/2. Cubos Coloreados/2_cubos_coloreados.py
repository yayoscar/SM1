"""Aplica un mapa de colores a tu gráfico de cubos."""

import matplotlib.pyplot as plt

# Listas de valores x e y para los primeros 5000 números cúbicos
valores_x = range(1, 5001)
valores_y = [x**3 for x in valores_x]

# Estilo de gráfica
plt.style.use('seaborn-v0_8')

# Crear figura y ejes
fig, ax = plt.subplots()

# Usamos el mapa de colores 'Blues' y pasamos los valores_y para determinar el color
sc = ax.scatter(valores_x, valores_y, c=valores_y, cmap=plt.cm.Blues, s=10)

# Establecer título del gráfico y etiquetas de los ejes
ax.set_title("Números Cúbicos de Color", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Cubo del Valor", fontsize=14)

# Establecer el rango de los ejes
ax.axis([0, 5100, 0, 5100**3])

# Ajustar el tamaño de las etiquetas de los ejes
ax.tick_params(axis='both', which='major', labelsize=14)

# Agregar barra de colores
fig.colorbar(sc, label='Escala de Valor')

# Agregar grilla
ax.grid(True, linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()



