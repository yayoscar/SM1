"""Aplica un mapa de colores a tu gráfico de cubos."""

import matplotlib.pyplot as plt

valores_x = range(1, 5001)
valores_y = [x**3 for x in valores_x]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

sc = ax.scatter(valores_x, valores_y, c=valores_y, cmap=plt.cm.Blues, s=10)

ax.set_title("Números Cúbicos Coloreados", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Cubo del Valor", fontsize=14)
ax.axis([0, 5100, 0, 5100**3])

ax.tick_params(axis='both', which='major', labelsize=14)

fig.colorbar(sc, label='Valor del Cubo')

ax.grid(True, linestyle='--', alpha=0.7)

plt.show()



