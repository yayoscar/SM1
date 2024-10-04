import matplotlib.pyplot as plt
from dado6 import Dado

dado1 = Dado(6)
dado2 = Dado(6)
dado3 = Dado(6)

resultados = [dado1.lanzar() + dado2.lanzar() + dado3.lanzar() for _ in range(1000)]

maximo_resultado = dado1.lados + dado2.lados + dado3.lados
frecuencias = [resultados.count(valor) for valor in range(3, maximo_resultado + 1)]

valores_x = list(range(3, maximo_resultado + 1))

plt.bar(valores_x, frecuencias, color='blue')
plt.title('Resultados del lanzamiento de los dados', fontsize=14)
plt.xlabel('Suma de los dados', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)

plt.show()
