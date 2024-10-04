# Aplica un mapa de colores a tu gráfico de cubos
import matplotlib. pyplot as plt
valores_x=range(1,6) 
valores_y=[x**3 for x in valores_x]
plt.style.use('seaborn-v0_8') 
fig,ax = plt.subplots()
ax.scatter(valores_x,valores_y, c=valores_y,cmap=plt.cm.Purples, s=10) 
ax.set_title("Los primeros 5 números",fontsize=24) 
ax.set_xlabel("Valor",fontsize=14)
ax.set_ylabel("Cubo del valor",fontsize=14)
ax.tick_params(axis='both', labelsize=14) 
ax.tick_params(axis='both',labelsize=14)
ax.axis([0,6,0,130])
plt.show()

import matplotlib. pyplot as plt
valores_x=range(1,5001) 
valores_y=[x**3 for x in valores_x]
plt.style.use('seaborn-v0_8') 
fig,ax = plt.subplots()
ax.scatter(valores_x,valores_y, c=valores_y,cmap=plt.cm.Purples, s=10) 
ax.set_title("Los primeros 5000 números",fontsize=24) 
ax.set_xlabel("Valor",fontsize=14)
ax.set_ylabel("Cubo del valor",fontsize=14)
ax.tick_params(axis='both', labelsize=14) 
ax.tick_params(axis='both',labelsize=14)
ax.axis([0,5000,0,125000000000])
plt.show()
