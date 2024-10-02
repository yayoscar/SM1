
import numpy as np

# Datos de tiempo (en segundos) y velocidades (en cm/s)
# Ingresa aquí tus valores de tiempo y velocidad
tiempo = np.array([5,10,15,20,25,30,35,40,45,50])  # ejemplo de tiempos en segundos
velocidades = np.array([340,320,310,300,304,300,302,307,306,304])  # velocidades en cm/s

# Calcular aceleración (a) como la derivada de la velocidad
# a = (v_f - v_i) / (t_f - t_i) usando diferencias finitas
aceleraciones = np.diff(velocidades) / np.diff(tiempo)

# Mostrar resultados
for i in range(len(aceleraciones)):
    print(f"Aceleración entre t={tiempo[i]}s y t={tiempo[i+1]}s: {aceleraciones[i]:.2f} cm/s²")

