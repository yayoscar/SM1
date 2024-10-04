from random import choice

class Randomwalk:
    """Una clase para crear un caminata areatoria"""

    def __init__(self, numero_puntos=50000):
        """Inicializamos atributos"""
        self.numero_puntos=numero_puntos

        #Todas las caminatas inician en caminat 0,0
        self.valores_x=[0]
        self.valores_y=[0]

    def llenar_caminata(self):
        while len(self.valores_x)<self.numero_puntos:
            #Direccion y distancia para x 
            direccion_x=choice([1,-1])
            pasos_x=choice([0,1,2,3,4])
            distancia_x=direccion_x * pasos_x

            #Direccion y distancia para y

            direccion_y=choice([1])
            pasos_y=choice([0,1,2,3,4])
            distancia_y=direccion_y * pasos_y

            #Validar que se va a mover de la posicion actual 
            if pasos_x==0 and pasos_y==0:
                continue

            x=self.valores_x[-1]+distancia_x
            y=self.valores_y[-1]+distancia_y

            self.valores_x.append(x)
            self.valores_y.append(y)