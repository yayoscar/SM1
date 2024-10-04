import matplotlib.pyplot as plt
from caminatas_aleatorias_modificadas_random_walk import RandomWalk

rw = RandomWalk()
rw.llenar_caminata()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.valores_x, rw.valores_y, s=15)

plt.show() 