import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

Valores_x = range(1,5001)
Valores_y = [x**3 for x in Valores_x]

fig,ax =plt.subplots()
ax.scatter(Valores_x,Valores_y,c='Green',s=35)
ax.plot(Valores_x,Valores_y)

ax.set_title("Cuadrados", fontsize=24, color='Red')
ax.set_xlabel("Valor", fontsize=14, color='Red')
ax.set_ylabel("Cuadrado de valor", fontsize=14,color='Red')

ax.tick_params(axis="both", labelsize=14)

plt.show()

