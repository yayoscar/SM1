"""Modifica `rw_visual.py` reemplazando `plt.scatter()` con `plt.plot()`. 
 Para simular el camino de un grano de polen en la superficie de una gota de agua,
 pasa los valores `rw.valores_x` y `rw.valores_y`, e incluye un argumento `linewidth`. 
 Usa 5,000 en lugar de 50,000 puntos."""

import matplotlib.pyplot as plt
from random_walks import RandomWalks

#hacer multiples caminatas
while True:

  #crear una instancia de RandomWalks
  rw=RandomWalks(5_000)
  rw.llenar_caminata()

  #inicializamos nuestra ventana de grafica
  plt.style.use('classic')
  fig,ax=plt.subplots(figsize=(10, 6), dpi=90)
  numeros_puntos=range(rw.numero_puntos)
  ax.scatter(rw.valores_x,rw.valores_y,c=numeros_puntos,cmap=plt.cm.Blues,edgecolors='none',s=15)
  #Enfatizar los primeros y ultimos puntos 
  ax.scatter(0,0,c='green',edgecolors='none',s=100)
  plt.plot(rw.valores_x[-1],rw.valores_y[-1],linewidth=0.5)

  #Eliminar los ejes
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)

  plt.title("Caminata Aleatoria de un Grano de Polen")

  #mostrar la grafica
  plt.show()

  continuar=input("¿hacer otra caminata? (s/n):")
  if continuar=='n':
     break
  
  