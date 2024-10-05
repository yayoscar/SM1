import matplotlib.pyplot as plt
from random import choice  # Asegúrate de importar la función choice

# Modificar las listas en la clase RandomWalk para direcciones y distancias
class RandomWalkModificado:
    def __init__(self, num_puntos=5000 ):
        self.num_puntos = num_puntos
        self.valores_x = [0]
        self.valores_y = [0]

    def llenar_caminata(self):
        while len(self.valores_x) < self.num_puntos:
            x_direccion = choice([1, -1])  # Modificar lista de direcciones
            x_distancia = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])  # Modificar lista de distancias
            x_paso = x_direccion * x_distancia

            y_direccion = choice([1, -1])  # Modificar lista de direcciones
            y_distancia = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])  # Modificar lista de distancias
            y_paso = y_direccion * y_distancia

            if x_paso == 0 and y_paso == 0:
                continue

            siguiente_x = self.valores_x[-1] + x_paso
            siguiente_y = self.valores_y[-1] + y_paso

            self.valores_x.append(siguiente_x)
            self.valores_y.append(siguiente_y)

# Crear una caminata aleatoria modificada
rw_modificado = RandomWalkModificado(5000)
rw_modificado.llenar_caminata()

# Graficar la caminata modificada
plt.figure(figsize=(10, 6))
plt.plot(rw_modificado.valores_x, rw_modificado.valores_y, linewidth=1)
plt.title('Caminata aleatoria modificada')
plt.show()
