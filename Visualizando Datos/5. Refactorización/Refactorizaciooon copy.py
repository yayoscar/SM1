# rw_visual.py
import matplotlib.pyplot as plt
from rw_visual import Randomwalk

while True:
 # Crear una caminata aleatoria.
   rw = Randomwalk()
   rw.llenar_caminata()

   # Graficar los puntos de la caminata.
   plt.style.use('classic')
   fig, ax = plt.subplots()

   numeros_puntos = range(rw.numero_puntos)
   ax.scatter(rw.valores_x, rw.valores_y, c=numeros_puntos, cmap=plt.cm.Blues, edgecolors='none', s=15)

   plt.show()
   continuar = input("¿Hacer otra caminata? (s/n): ")
   if continuar == 'n':
         break