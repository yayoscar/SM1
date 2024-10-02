from random import choice

class RandomWalks:
    """clase para crear una caminata aleatoria"""

    def __init__(self,numero_puntos=5000):
        #inicializamos atributos
        self.numero_puntos=numero_puntos
        #todas las caminatas inician en 0,0
        self.valores_x=[0]
        self.valores_y=[0]

    def llenar_caminata(self):
        while len(self.valores_x)<self.numero_puntos:
            #direccion y distancias para x
            direccion_x=choice([1,-1])
            pasos_x=choice([0,1,2,3,4,5,6,7,8])
            distancia_x=direccion_x*pasos_x

            #direccion y distancia para y
            direccion_y=choice([1,-1])
            pasos_y=choice([0,1,2,3,4])
            distancia_y=direccion_y*pasos_y


            #validar que se va a mover de la posicion actual
            if pasos_x==0 and pasos_y==0:
                continue
            
            #incrementamos los valores en x y y
            x=self.valores_x[-1]+distancia_x
            y=self.valores_y[-1]+distancia_y
            #agregamos los nuevos valores a la lista
            self.valores_x.append(x)
            self.valores_y.append(y)