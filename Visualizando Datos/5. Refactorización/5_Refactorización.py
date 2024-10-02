"""El método `llenar_caminata()` es extenso. Crea un nuevo método llamado `obtener_paso()` 
para determinar la dirección y la distancia de cada paso, y luego calcular el paso. 
Deberías terminar con dos llamadas a `obtener_paso()` en `llenar_caminata()`:

```python
paso_x = self.obtener_paso()
paso_y = self.obtener_paso()
```

Esta refactorización debería reducir el tamaño de `llenar_caminata()` y hacer que el método sea
más fácil de leer y entender.
"""
# random_walk.py
from random import choice

class RandomWalk:
    """Una clase para generar caminatas aleatorias."""
    
    def _init_(self, num_puntos=5000):
        """Inicializar los atributos de una caminata."""
        self.num_puntos = num_puntos
        self.valores_x = [0]
        self.valores_y = [0]

    def obtener_paso(self):
        """Determina la dirección y la distancia de cada paso."""
        direccion = choice([1, -1])  
        distancia = choice([0, 1, 2, 3, 4])  
        return direccion * distancia  

    def llenar_caminata(self):
        """Calcular todos los puntos en la caminata."""
 
        while len(self.valores_x) < self.num_puntos:
            
            paso_x = self.obtener_paso()
            paso_y = self.obtener_paso()

            if paso_x == 0 and paso_y == 0:
                continue

            x = self.valores_x[-1] + paso_x
            y = self.valores_y[-1] + paso_y
            self.valores_x.append(x)
            self.valores_y.append(y)
