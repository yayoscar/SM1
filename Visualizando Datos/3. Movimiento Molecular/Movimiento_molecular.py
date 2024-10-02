import matplotlib.pyplot as plt
from random_walks import Randomwalks  # Asegúrate de que el nombre sea correcto

def plot_random_walk():
    # Crear una caminata aleatoria con 5,000 puntos.
    rw = RandomWalks(5_000)
    rw.fill_walk()  # Asegúrate de que el método se llame correctamente

    # Graficar los puntos de la caminata usando plt.plot
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    
    # Trazar la caminata aleatoria como una línea continua
    ax.plot(rw.valores_x, rw.valores_y, linewidth=1, color='blue')  # Usa linewidth para el grosor de la línea

    # Enfatizar los primeros y últimos puntos
    ax.plot(0, 0, 'go', markersize=10)  # Primer punto en verde
    ax.plot(rw.valores_x[-1], rw.valores_y[-1], 'ro', markersize=10)  # Último punto en rojo

    # Eliminar los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Mostrar la gráfica
    plt.show()

# Bucle para realizar múltiples caminatas
while True:
    plot_random_walk()
    
    continuar = input("¿Hacer otra caminata? (s/n): ").strip().lower()
    if continuar != 's':
        break