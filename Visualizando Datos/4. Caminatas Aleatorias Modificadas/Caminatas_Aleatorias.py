import random
import matplotlib.pyplot as plt

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # Inicializa las listas para los valores de las coordenadas x e y.
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # Elige la dirección y la distancia para el eje x.
            x_direction = random.choice([1, -1])  # Puedes eliminar el -1 si quieres solo una dirección.
            x_distance = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8] )
            x_step = x_direction * x_distance

            # Elige la dirección y la distancia para el eje y.
            y_direction = random.choice([1, -1])  # También puedes modificar esta lista.
            y_distance = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            # Rechaza movimientos que no cambien de posición.
            if x_step == 0 and y_step == 0:
                continue

            # Calcula las nuevas posiciones de x e y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

# Crear una instancia de RandomWalk y generar la caminata.
rw = RandomWalk(5000)
rw.fill_walk()

# Visualizar la caminata.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

# Enfatizar el primer y último punto.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # Inicio de la caminata.
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # Final de la caminata.

plt.show()
