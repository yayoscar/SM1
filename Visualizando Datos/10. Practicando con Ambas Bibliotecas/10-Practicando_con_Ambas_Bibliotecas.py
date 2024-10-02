"""Intenta utilizar Matplotlib para crear una visualización de lanzamiento de dados y 
utiliza Plotly para hacer la visualización de una caminata aleatoria. 
(Necesitarás consultar la documentación de cada biblioteca para completar este ejercicio).
"""

""""USANDO MATPLOTLIB"""

# Tengo el archivo que pide para que corra (dado), sin embargo no corre.

import matplotlib.pyplot as plt
from dado import Dado

# Crear dos dados de 6 lados
dado_1 = Dado()
dado_2 = Dado()

# Lanzar el dado 1000 veces y guardarlo en una lista
resultados = []

for lanzamiento in range(1000):
    resultado = dado_1.lanzar() + dado_2.lanzar()
    resultados.append(resultado)

# Analizar resultados
frecuencias = []
maximo_resultados = dado_1.lados + dado_2.lados
for valor in range(2, maximo_resultados + 1):
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)

# Visualizar los resultados con Matplotlib
valores_x = list(range(2, maximo_resultados + 1))

plt.bar(valores_x, frecuencias, color='skyblue')
plt.title('Resultados del lanzamiento de dos dados de 6 caras')
plt.xlabel('Resultado')
plt.ylabel('Frecuencia del resultado')
plt.xticks(valores_x)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
