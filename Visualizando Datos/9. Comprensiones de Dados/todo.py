import random
import matplotlib.pyplot as plt

# 1. Cubos: Graficar los primeros cinco números cúbicos y luego los primeros 5000
def graficar_cubos():
    # Primeros cinco números cúbicos
    x_values = [1, 2, 3, 4, 5]
    y_values = [x**3 for x in x_values]
    
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, linewidth=3)
    ax.set_title("Primeros cinco números cúbicos", fontsize=24)
    ax.set_xlabel("Valor", fontsize=14)
    ax.set_ylabel("Cubo del valor", fontsize=14)
    plt.show()

    # Primeros 5000 números cúbicos
    x_values = list(range(1, 5001))
    y_values = [x**3 for x in x_values]

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, linewidth=3)
    ax.set_title("Primeros 5000 números cúbicos", fontsize=24)
    ax.set_xlabel("Valor", fontsize=14)
    ax.set_ylabel("Cubo del valor", fontsize=14)
    plt.show()

# 2. Cubos Coloreados
def graficar_cubos_coloreados():
    x_values = list(range(1, 5001))
    y_values = [x**3 for x in x_values]
    
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    sc = ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
    ax.set_title("Cubos Coloreados", fontsize=24)
    ax.set_xlabel("Valor", fontsize=14)
    ax.set_ylabel("Cubo del valor", fontsize=14)
    plt.colorbar(sc)
    plt.show()

# 3. Movimiento Molecular (caminata aleatoria con plot)
class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.valores_x = [0]
        self.valores_y = [0]

    def llenar_caminata(self):
        while len(self.valores_x) < self.num_points:
            paso_x = self.obtener_paso()
            paso_y = self.obtener_paso()

            x = self.valores_x[-1] + paso_x
            y = self.valores_y[-1] + paso_y

            self.valores_x.append(x)
            self.valores_y.append(y)

    def obtener_paso(self):
        direccion = random.choice([1, -1])
        distancia = random.choice([0, 1, 2, 3, 4])
        return direccion * distancia

def graficar_caminata():
    rw = RandomWalk(5000)
    rw.llenar_caminata()
    
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(rw.valores_x, rw.valores_y, linewidth=1)
    ax.set_title("Simulación de Movimiento Molecular", fontsize=24)
    plt.show()

# 6. Dos D8
def lanzar_dados_d8():
    lanzamientos = 1000
    resultados = [random.randint(1, 8) + random.randint(1, 8) for _ in range(lanzamientos)]
    
    frecuencias = [resultados.count(valor) for valor in range(2, 17)]
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    valores_x = list(range(2, 17))
    ax.bar(valores_x, frecuencias, width=0.8, color='blue')
    ax.set_title("Simulación de Dos Dados D8", fontsize=20)
    ax.set_xlabel("Suma de los dos dados", fontsize=15)
    ax.set_ylabel("Frecuencia", fontsize=15)
    plt.show()

# 7. Tres Dados D6
def lanzar_tres_dados_d6():
    lanzamientos = 1000
    resultados = [sum(random.randint(1, 6) for _ in range(3)) for _ in range(lanzamientos)]
    
    frecuencias = [resultados.count(valor) for valor in range(3, 19)]
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    valores_x = list(range(3, 19))
    ax.bar(valores_x, frecuencias, width=0.8, color='green')
    ax.set_title("Simulación de Tres Dados D6", fontsize=20)
    ax.set_xlabel("Suma de los tres dados", fontsize=15)
    ax.set_ylabel("Frecuencia", fontsize=15)
    plt.show()

# 8. Multiplicación de dos dados
def multiplicacion_dos_dados():
    lanzamientos = 1000
    resultados = [random.randint(1, 6) * random.randint(1, 6) for _ in range(lanzamientos)]
    
    frecuencias = [resultados.count(valor) for valor in range(1, 37)]
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    valores_x = list(range(1, 37))
    ax.bar(valores_x, frecuencias, width=0.8, color='red')
    ax.set_title("Multiplicación de Dos Dados D6", fontsize=20)
    ax.set_xlabel("Producto de los dos dados", fontsize=15)
    ax.set_ylabel("Frecuencia", fontsize=15)
    plt.show()

# Menú para seleccionar la simulación o visualización que deseas ejecutar
def menu():
    while True:
        print("\n--- Menú de Visualizaciones y Simulaciones ---")
        print("1. Graficar Cubos")
        print("2. Graficar Cubos Coloreados")
        print("3. Simular Movimiento Molecular (Caminata Aleatoria)")
        print("4. Simular Lanzamiento de Dos Dados D8")
        print("5. Simular Lanzamiento de Tres Dados D6")
        print("6. Simular Multiplicación de Dos Dados D6")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            graficar_cubos()
        elif opcion == "2":
            graficar_cubos_coloreados()
        elif opcion == "3":
            graficar_caminata()
        elif opcion == "4":
            lanzar_dados_d8()
        elif opcion == "5":
            lanzar_tres_dados_d6()
        elif opcion == "6":
            multiplicacion_dos_dados()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú
menu()
