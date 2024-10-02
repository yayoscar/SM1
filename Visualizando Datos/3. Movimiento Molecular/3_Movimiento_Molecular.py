"""Modifica `rw_visual.py` reemplazando `plt.scatter()` con `plt.plot()`. 
 Para simular el camino de un grano de polen en la superficie de una gota de agua,
 pasa los valores `rw.valores_x` y `rw.valores_y`, e incluye un argumento `linewidth`. 
 Usa 5,000 en lugar de 50,000 puntos."""

import matplotlib.pyplot as plt
from random_walks import RandomWalks

while True:

  rw=RandomWalks(5_000)
  rw.llenar_caminata()

  plt.style.use('classic')
  fig,ax=plt.subplots(figsize=(10, 6), dpi=90)
  numeros_puntos=range(rw.numero_puntos)
  ax.scatter(rw.valores_x,rw.valores_y,c=numeros_puntos,cmap=plt.cm.Reds,edgecolors='none',s=15) 
  ax.scatter(0,0,c='blue',edgecolors='none',s=100)
  plt.plot(rw.valores_x[-1],rw.valores_y[-1],linewidth=0.5)

  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)

  plt.title("Caminata Aleatoria de un Grano de Polen")

  plt.show()

  continuar=input("¿hacer otra caminata? (s/n):")
  if continuar=='n':
     break
  
  