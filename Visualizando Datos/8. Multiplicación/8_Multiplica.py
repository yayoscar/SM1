import random
import matplotlib.pyplot as plt

# Lanzar dos dados D6 y multiplicar los resultados
lanzamientos = 1000  # Puedes cambiar el número de lanzamientos
resultados = [random.randint(1, 6) * random.randint(1, 6) for _ in range(lanzamientos)]

# Contar la frecuencia de cada resultado (de 1 a 36)
frecuencias = [resultados.count(valor) for valor in range(1, 37)]

# Graficar los resultados
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
valores_x = list(range(1, 37))  # Posibles productos de los dos dados
ax.bar(valores_x, frecuencias, width=0.8, color='blue')

# Configuración del gráfico
ax.set_title("Resultados de la Multiplicación de Dos Dados D6", fontsize=20)
ax.set_xlabel("Producto de los dos dados", fontsize=15)
ax.set_ylabel("Frecuencia", fontsize=15)
plt.show()
