# Modifica rw_visual.py reemplazando plt.scatter() con plt.plot(). Para simular
# el camino de un grano de polen en la superficie de una gota de agua, pasa los valores
# rw.valores_x y rw.valores_y, e incluye un argumento linewidth. Usa 5,000 en lugar
# de 50,000 puntos

import matplotlib.pyplot as plt
from random_walk_movimiento_molecular import RandomWalk

rw = RandomWalk(num_puntos = 5000)
rw.llenar_caminata()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(rw.valores_x, rw.valores_y, linewidth=2)

plt.show() 