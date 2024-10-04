#El método llenar_caminata() es extenso. Crea un nuevo método
#llamado obtener_paso() para determinar la dirección y la distancia de cada paso,
# y luego calcular el paso. Deberías terminar con dos llamadas
# a obtener_paso() en llenar_caminata() :

from random import choice
class RandomWalk:
    
    def __init__(self,num_puntos=5000):
        self.num_puntos = num_puntos
        self.valores_x = [0]
        self.valores_y = [0]
        
    def obtener_paso(self):
        direccion = choice([1,-1])
        distancia = choice([0,1,2,3,4])
        paso = direccion * distancia
        return paso
        
    def llenar_caminata(self):
        
        while len(self.valores_x) < self.num_puntos:
            paso_x = self.obtener_paso()
            paso_y = self.obtener_paso()
            
            if paso_x == 0 and paso_y == 0:
                continue
            
            x = self.valores_x[-1] + paso_x
            y = self.valores_y[-1] + paso_y
            
            self.valores_x.append(x)
            self.valores_y.append(y)