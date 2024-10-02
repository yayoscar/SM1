import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Rutas de los archivos
nombre_archivo = 'Descargando Datos/data/death_valley_2021_full.csv'
nombre_archivo_2 = 'Descargando Datos/data/sitka_weather_2021_simple.csv'

# Abrir archivo de Death Valley
with open(nombre_archivo) as archivo:
    lector = csv.reader(archivo)
    fila_encabezado = next(lector)

    # Obtener las temperaturas de la columna con índice 6 TMAX y 7 TMIN
    altas_dv, fechas_dv, bajas_dv = [], [], []
    for fila in lector:
        if len(fila) >= 8:  # Asegúrate de que hay al menos 8 columnas
            fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
            try:
                alta = int(fila[6])  # TMAX
                baja = int(fila[7])   # TMIN
            except ValueError:
                print(f"Datos faltantes para {fecha_actual}")
            else:
                fechas_dv.append(fecha_actual)
                altas_dv.append(alta)
                bajas_dv.append(baja)

# Abrir archivo de Sitka
with open(nombre_archivo_2) as archivo:
    lector = csv.reader(archivo)
    fila_encabezado = next(lector)

    altas_sitka, fechas_sitka, bajas_sitka = [], [], []
    for fila in lector:
        if len(fila) >= 9:  # Asegúrate de que hay al menos 9 columnas
            fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
            try:
                alta_ = int(fila[7])  # TMAX
                baja_ = int(fila[8])   # TMIN
            except ValueError:
                print(f"Datos faltantes para {fecha_actual} en Sitka")
            else:
                fechas_sitka.append(fecha_actual)
                altas_sitka.append(alta_)
                bajas_sitka.append(baja_)
        else:
            print(f"Fila incompleta en Sitka: {fila}")

# Crear un gráfico de las temperaturas máximas y mínimas
plt.style.use('seaborn-v0_8')  # Asegúrate de que 'seaborn-v0_8' esté instalado

fig, ax = plt.subplots()
ax.plot(fechas_dv, altas_dv, c='red', linewidth=0.8, label='Death Valley - Altas')
ax.plot(fechas_dv, bajas_dv, c='blue', linewidth=0.8, label='Death Valley - Bajas')
plt.fill_between(fechas_dv, altas_dv, bajas_dv, facecolor='purple', alpha=0.4)

ax.plot(fechas_sitka, altas_sitka, c='yellow', linewidth=0.8, label='Sitka - Altas')
ax.plot(fechas_sitka, bajas_sitka, c='green', linewidth=0.8, label='Sitka - Bajas')
plt.fill_between(fechas_sitka, altas_sitka, bajas_sitka, facecolor='grey', alpha=0.4)

# Formato del gráfico
ax.set_title("Temperaturas máximas y mínimas diarias - Death Valley y Sitka, CA", fontsize=20)
ax.set_xlabel('Fecha', fontsize=16)
ax.set_ylabel('Temperatura (°F)', fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=14)

# Añadir leyenda
ax.legend()

plt.show()
