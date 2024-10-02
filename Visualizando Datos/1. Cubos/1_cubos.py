""" Un número elevado a la tercera potencia es un cubo. 
Grafica los primeros cinco números cúbicos y luego grafica los primeros 5000 números cúbicos."""
import matplotlib.pyplot as plt

valores_entrada=[1,2,3,4,5] 
cubos=[1,8,27,64,125]

plt.style.use('bmh')

fig, ax = plt.subplots()

ax.plot(valores_entrada,cubos, linewidth=3)

ax.set_title("Números al cubo", fontsize=20)
ax.set_xlabel("Valor", fontsize=10)
ax.set_ylabel("El cubo del Valor", fontsize=10)

ax.tick_params(axis='both', labelsize=10)

plt.show()