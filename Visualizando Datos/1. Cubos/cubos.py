import matplotlib.pyplot as plt
import numpy as np
#Datos para los primeros 5 números cúbicos
x_small=np.arange(1, 6)
y_small=x_small ** 3
#Crear una figura y ejes para el gráfico
plt.figure(figsize=(7, 6))
#Graficar los primeros 5 números cúbicos
scatter1 = plt.scatter(x_small, y_small,c=y_small,cmap='viridis')
plt.title('Primeros 5 números cúbicos')
plt.xlabel('Número')
plt.ylabel('Cubo del número')
plt.colorbar(scatter1,label='Valor del Cubo')
#Mostrar la gráfica
plt.show()
