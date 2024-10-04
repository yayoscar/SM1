import random
import matplotlib.pyplot as plt

#Lanza dos dados y guarda las sumas en una lista usando comprensión de listas
resultados = [random.randint(1, 6) + random.randint(1, 6) for _ in range(1000)]

#Cuenta la frecuencia de cada resultado
max_resultado=6+6  # Máximo valor que se puede obtener al lanzar dos dados
frecuencias=[resultados.count(valor) for valor in range(2, max_resultado + 1)]

# Graficar los resultados
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
valores_x = list(range(2, max_resultado + 1))
ax.bar(valores_x, frecuencias, width=0.8, color='blue')

# Configuración del gráfico
ax.set_title("Resultados del Lanzamiento de Dos Dados", fontsize=20)
ax.set_xlabel("Suma de los dos dados", fontsize=15)
ax.set_ylabel("Frecuencia", fontsize=15)
plt.show()
