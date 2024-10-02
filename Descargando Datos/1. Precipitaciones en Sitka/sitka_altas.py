import csv
from datetime import datetime
import matplotlib.pyplot as plt

nombre_archivo = 'Descargando Datos/data/sitka_weather_07-2021_simple.csv'

# Abrir archivo
with open(nombre_archivo) as archivo:
    # Crear un objeto lector para leer el archivo CSV
    lector = csv.reader(archivo)

    # Leer los encabezados de la primera línea
    Fila_encabezado = next(lector)

    # Obtener las temperaturas máximas y mínimas y las fechas
    Altas, Fechas, Bajas = [], [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            alta = int(fila[4])
            baja = int(fila[5])
        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")
        else:
            Fechas.append(fecha_actual)
            Altas.append(alta)
            Bajas.append(baja)

# Crear un gráfico de las temperaturas máximas y mínimas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(Fechas, Altas, c='red', linewidth=0.4, label="Max")
ax.plot(Fechas, Bajas, c='blue', linewidth=0.4, label="Min")
plt.fill_between(Fechas, Altas, Bajas, facecolor='Purple', alpha=0.4)
ax.legend(loc='upper right', fontsize=10)

# Formato del gráfico
ax.title.set_text('Temperaturas máximas y mínimas diarias, Año 2018 - Sitka, AK')
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatura (F)')
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=14)

# Mostrar el gráfico
plt.show()
