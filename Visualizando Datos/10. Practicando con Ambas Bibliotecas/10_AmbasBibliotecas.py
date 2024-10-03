import numpy as np
import matplotlib.pyplot as plt

# Simulación de lanzamientos de dados
num_rolls = 1000
dice1 = np.random.randint(1, 7, num_rolls)
dice2 = np.random.randint(1, 7, num_rolls)
sums = dice1 + dice2

# Crear histograma
plt.figure(figsize=(10, 6))
plt.hist(sums, bins=np.arange(2, 14) - 0.5, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.xticks(range(2, 13))
plt.title("Distribución de Sumas de Dos Dados")
plt.xlabel("Suma")
plt.ylabel("Frecuencia Relativa")
plt.grid(axis='y', alpha=0.75 )
plt.show()
