import numpy as np
import matplotlib.pyplot as plt

def simular_lanzamientos(num_lanzamientos):
    # Dos dados de 8 caras
    dado1 = np.random.randint(1, 9, num_lanzamientos)
    dado2 = np.random.randint(1, 9, num_lanzamientos)
    
    resultados = dado1 + dado2

    return resultados

def visualizar_simulacion(num_lanzamientos):
    resultados = simular_lanzamientos(num_lanzamientos)
    
    plt.figure(figsize=(10, 6))
    plt.hist(resultados, bins=np.arange(2, 18) - 0.5, edgecolor='black', density=True)
    plt.title(f"Distribución de sumas en {num_lanzamientos} lanzamientos de dos dados de 8 caras")
    plt.xlabel("Suma de los dos dados")
    plt.ylabel("Frecuencia relativa")
    plt.xticks(range(2, 17))
    plt.show()

visualizar_simulacion(1000)
