
# rw_visual.py
import matplotlib.pyplot as plt
from random_walk import Randomwalk

while True:
 # Crear una caminata aleatoria.
   rw = Randomwalk(50000)
   rw.llenar_caminata()

   # Graficar los puntos de la caminata.
   plt.style.use('classic')
   fig, ax = plt.subplots(figsize=(10, 6),  dpi=128)

   numeros_puntos = range(rw.numero_puntos)
   ax.plot(rw.valores_x, rw.valores_y, linewidth=1)  

 # Enfatizar los primeros y últimos puntos.
   ax.scatter(0, 0, c='green', edgecolors='none', s=100)
   ax.scatter(rw.valores_x[-1], rw.valores_y[-1], c='red', edgecolors='none', s=100)

   # Eliminar los ejes.
   ax.get_xaxis().set_visible(False)
   ax.get_yaxis().set_visible(False)

   plt.show()
   continuar = input("¿Hacer otra caminata? (s/n): ")
   if continuar == 'n':
         break