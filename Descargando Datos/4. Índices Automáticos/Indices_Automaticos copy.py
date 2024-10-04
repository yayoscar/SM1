import csv
import matplotlib.pyplot as plt
from datetime import datetime

def plot_temperatures(nombre_archivo):
    with open(nombre_archivo) as archivo:
        lector = csv.reader(archivo)
        fila_encabezado = next(lector)

        # Encuentra los índices de las columnas TMIN y TMAX
        indice_tmin = fila_encabezado.index('TMIN')
        indice_tmax = fila_encabezado.index('TMAX')
        nombre_estacion = fila_encabezado.index('NAME')  # Ajusta esto si el nombre está en otra columna

        altas, fechas, bajas = [], [], []
        for fila in lector:
            fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
            try:
                alta = int(fila[indice_tmax])
                baja = int(fila[indice_tmin])
            except ValueError:
                print(f"Datos faltantes para {fecha_actual}")
            else:
                fechas.append(fecha_actual)
                altas.append(alta)
                bajas.append(baja)

        # Título automático basado en el nombre de la estación
        titulo = f"Temperaturas máximas y mínimas diarias, año 2021 - {fila[nombre_estacion]}"

        # Crear un gráfico de las temperaturas máximas y mínimas
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()
        ax.plot(fechas, altas, c='red', alpha=0.5)
        ax.plot(fechas, bajas, c='blue', alpha=0.5)
        plt.fill_between(fechas, altas, bajas, facecolor='blue', alpha=0.1)

        # Formato del gráfico
        plt.title(titulo, fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperatura (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

# Usa la función para tus archivos CSV
plot_temperatures('data/san_francisco_2021_simple.csv')
plot_temperatures('data/death_valley_2021_simple.csv')

#EL ARCHIVO NO CARGA DEBIDO A QUE NO SE PUEDE DESCARGAR EN EL LINK QUE NOS COMPARTIO PROFE