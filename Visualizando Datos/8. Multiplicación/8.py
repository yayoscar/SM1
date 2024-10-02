import numpy as np
import matplotlib.pyplot as plt

def simular_multiplicacion_dados(num_lanzamientos):
    dado1 = np.random.randint(1, 7, num_lanzamientos)
    dado2 = np.random.randint(1, 7, num_lanzamientos)
    
    resultados = dado1 * dado2

    return resultados

def visualizar_simulacion_multiplicacion(num_lanzamientos):
    resultados = simular_multiplicacion_dados(num_lanzamientos)
    
    plt.figure(figsize=(10, 6))
    plt.hist(resultados, bins=np.arange(1, 37) - 0.5, edgecolor='black', density=True)
    plt.title(f"Distribución de productos en {num_lanzamientos} lanzamientos de dos dados D6")
    plt.xlabel("Producto de los dos dados")
    plt.ylabel("Frecuencia relativa")
    plt.xticks(range(1, 37))
    plt.show()

visualizar_simulacion_multiplicacion(1000)
