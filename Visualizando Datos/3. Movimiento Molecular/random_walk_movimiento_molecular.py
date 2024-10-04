from random import choice
class RandomWalk:
    def __init__(self,num_puntos=5000):
        self.num_puntos = num_puntos
        self.valores_x = [0]
        self.valores_y = [0]
    def llenar_caminata(self):
        
        while len(self.valores_x) < self.num_puntos:
            direccion_x = choice([1, -1])
            distancia_x = choice([0,1,2,3,4])
            paso_x = direccion_x * distancia_x
            
            direccion_y = choice([1, -1])
            distancia_y = choice([0,1,2,3,4])
            paso_y = direccion_y * distancia_y
            
            if paso_x == 0 and paso_y == 0:
                continue
            
            x = self.valores_x[-1] + paso_x
            y = self.valores_y[-1] + paso_y
            
            self.valores_x.append(x)
            self.valores_y.append(y)