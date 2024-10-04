import matplotlib.pyplot as plt
from random import choice

class Random_walk:
    def __init__(self,num_puntos=5000):
        self.num_puntos=num_puntos

        self.valores_x = [0]
        self.valores_y = [0]
    
    def obtener_paso(self,list):
        direccion=choice([1,-1])
        distancia=choice([0,1,2,3,4])
        paso=direccion*distancia

        a = list[-1] + paso

        list.append(a)


        
    def rellenar_caminata(self):
        while len(self.valores_x) < self.num_puntos:
            x = self.obtener_paso(self.valores_x)
            y = self.obtener_paso(self.valores_y)



rw=Random_walk()
rw.rellenar_caminata()

plt.style.use('seaborn-v0_8')

fig,ax =plt.subplots()
ax.scatter(rw.valores_x,rw.valores_y,s=10,c="Red")


ax.set_title("Pasos aleatorios", fontsize=24, color='Red')

ax.tick_params()

plt.show()

#victor mono