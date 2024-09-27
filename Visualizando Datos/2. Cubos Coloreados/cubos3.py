import matplotlib.pyplot as plt
import numpy as np
#Datos para los primeros 50 números cúbicos
x=np.arange(1,51)
y=x**3
#Crear una figura y ejes para el gráfico
plt.figure(figsize=(10,6))
#Graficar los números cúbicos aplicando un mapa de colores
scatter=plt.scatter(x, y, c=y, cmap='inferno')
plt.title('Números cúbicos coloreados')
plt.xlabel('Número')
plt.ylabel('Cubo del número')
plt.colorbar(scatter, label='Valor del Cubo')
#Mostrar la gráfica
plt.show()
