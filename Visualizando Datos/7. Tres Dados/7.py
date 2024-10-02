import numpy as np
import matplotlib.pyplot as plt

def simular_lanzamientos_tres_dados(num_lanzamientos):
    dado1 = np.random.randint(1, 7, num_lanzamientos)
    dado2 = np.random.randint(1, 7, num_lanzamientos)
    dado3 = np.random.randint(1, 7, num_lanzamientos)
    
    resultados = dado1 + dado2 + dado3

    return resultados

def visualizar_simulacion_tres_dados(num_lanzamientos):
    resultados = simular_lanzamientos_tres_dados(num_lanzamientos)
    
    plt.figure(figsize=(10, 6))
    plt.hist(resultados, bins=np.arange(3, 19) - 0.5, edgecolor='black', density=True)
    plt.title(f"Distribución de sumas en {num_lanzamientos} lanzamientos de tres dados D6")
    plt.xlabel("Suma de los tres dados")
    plt.ylabel("Frecuencia relativa")
    plt.xticks(range(3, 19))
    plt.show()

visualizar_simulacion_tres_dados(1000)
