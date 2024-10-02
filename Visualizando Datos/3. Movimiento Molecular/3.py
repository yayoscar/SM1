import numpy as np
import matplotlib.pyplot as plt
import random


class RandomWalk:
    def __init__(self):
        self.valores_x = [0]
        self.valores_y = [0]

    def realizar_paseo(self, num_puntos=5000):
        for _ in range(num_puntos - 1):
            x_step = random.choice([-1, 1])
            y_step = random.choice([-1, 1])
            self.valores_x.append(self.valores_x[-1] + x_step)
            self.valores_y.append(self.valores_y[-1] + y_step)

rw = RandomWalk()
rw.realizar_paseo()

plt.figure(figsize=(10, 6))
plt.plot(rw.valores_x, rw.valores_y, linewidth=2) 
plt.title('Camino de un Grano de Polen en Agua')
plt.xlabel('Posición en X')
plt.ylabel('Posición en Y')
plt.grid(True)
plt.show()
