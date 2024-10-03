import matplotlib.pyplot as plt

# Generar los primeros 5000 números cúbicos
x_5000 = list(range(1, 5001))
y_5000 = [n**3 for n in x_5000]

# Crear la figura
plt.figure(figsize=(10,6))

# Aplicar el mapa de colores (colormap) usando scatter
plt.scatter(x_5000, y_5000, c=y_5000, cmap='viridis', s=10, edgecolor='none')

# Títulos y etiquetas
plt.title('Primeros 5000 números cúbicos con mapa de colores')
plt.xlabel('Número')
plt.ylabel('Cubo del número')

# Mostrar la barra de colores
plt.colorbar(label='Cubo del número')

# Mostrar gráfico
plt.tight_layout()
plt.show()
