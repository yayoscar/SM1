from random import choice

class Randomwalk:
    """Una clase para crear un caminata areatoria"""

    def __init__(self, numero_puntos=50000):
        """Inicializamos atributos"""
        self.numero_puntos=numero_puntos

        #Todas las caminatas inician en caminat 0,0
        self.valores_x=[0]
        self.valores_y=[0]

    def obtener_paso(self):
        direccion = choice([1, -1])  
        pasos = choice([0, 1, 2, 3, 4])  
        return direccion * pasos  

    def llenar_caminata(self):
        while len(self.valores_x)<self.numero_puntos:
           distancia_x = self.obtener_paso()
           distancia_y = self.obtener_paso()
            #Validar que se va a mover de la posicion actual 
           if distancia_x==0 and distancia_y==0:
                continue

           x=self.valores_x[-1]+distancia_x
           y=self.valores_y[-1]+distancia_y

           self.valores_x.append(x)
           self.valores_y.append(y)