import matplotlib.pyplot as plt  # Importa matplotlib para las gráficas
from random import choice  # Importa la función choice desde el módulo random

# Clase refactorizada para la caminata aleatoria
class RandomWalkRefactorizado:
    def __init__(self, num_puntos=5000 ):
        self.num_puntos = num_puntos
        self.valores_x = [0]
        self.valores_y = [0]

    def obtener_paso(self):
        direccion = choice([1, -1])
        distancia = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        return direccion * distancia

    def llenar_caminata(self):
        while len(self.valores_x) < self.num_puntos:
            paso_x = self.obtener_paso()
            paso_y = self.obtener_paso()

            if paso_x == 0 and paso_y == 0:
                continue

            siguiente_x = self.valores_x[-1] + paso_x
            siguiente_y = self.valores_y[-1] + paso_y

            self.valores_x.append(siguiente_x)
            self.valores_y.append(siguiente_y)

# Crear una caminata aleatoria refactorizada
rw_refactorizado = RandomWalkRefactorizado(5000)
rw_refactorizado.llenar_caminata()

# Graficar la caminata refactorizada
plt.figure(figsize=(10, 6))
plt.plot(rw_refactorizado.valores_x, rw_refactorizado.valores_y, linewidth=1)
plt.title('Caminata aleatoria refactorizada')
plt.show()
