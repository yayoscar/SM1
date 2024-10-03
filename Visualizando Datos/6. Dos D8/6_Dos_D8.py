import matplotlib.pyplot as plt
import random

# Clase Dado, para lanzar un dado con un número dado de caras
class Dado:
    def __init__(self, lados=8):
        self.lados = lados

    def lanzar(self):
        return random.randint(1, self.lados )

# Crear dos dados de 8 caras
dado1 = Dado()
dado2 = Dado()

# Lanzar los dados 1000 veces y guardar los resultados
resultados = []
for lanzamiento in range(1000):
    resultado = dado1.lanzar() + dado2.lanzar()
    resultados.append(resultado)

# Analizar los resultados
frecuencias = []
maximo_resultado = dado1.lados + dado2.lados
valores_x = list(range(2, maximo_resultado + 1))

for valor in valores_x:
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)

# Visualizar los resultados usando matplotlib
plt.figure(figsize=(10, 6))
plt.bar(valores_x, frecuencias, color='green', edgecolor='black')

plt.title('Resultados del lanzamiento de 2 dados de 8 caras (1000 lanzamientos)', fontsize=14)
plt.xlabel('Resultado', fontsize=12)
plt.ylabel('Frecuencia del resultado', fontsize=12)
plt.xticks(valores_x)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
