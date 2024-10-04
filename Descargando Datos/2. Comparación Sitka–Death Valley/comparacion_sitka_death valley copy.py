import csv
import matplotlib.pyplot as plt
from datetime import datetime

nombre_archivo_sitka = 'Descargando Datos/data/sitka_weather_2021_full.csv'
nombre_archivo_death_valley = 'Descargando Datos/data/death_valley_2021_full.csv'


with open(nombre_archivo_sitka) as archivo_sitka:
    lector_sitka = csv.reader(archivo_sitka)
    fila_encabezado = next(lector_sitka)


    fechas_sitka, temperaturas_sitka = [], []
    for fila in lector_sitka:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            temperatura_max = int(fila[7])  
            fechas_sitka.append(fecha_actual)
            temperaturas_sitka.append(temperatura_max)
        except ValueError:
            print(f"Faltan datos de temperatura para {fecha_actual}")


with open(nombre_archivo_death_valley) as archivo_death_valley:
    lector_death_valley = csv.reader(archivo_death_valley)
    fila_encabezado = next(lector_death_valley)

    fechas_death_valley, temperaturas_death_valley = [], []
    for fila in lector_death_valley:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            temperatura_max = int(fila[6])  # Convertir a entero
            fechas_death_valley.append(fecha_actual)
            temperaturas_death_valley.append(temperatura_max)
        except ValueError:
            print(f"Faltan datos de temperatura para {fecha_actual}")


min_temp = min(min(temperaturas_sitka), min(temperaturas_death_valley))
max_temp = max(max(temperaturas_sitka), max(temperaturas_death_valley))


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(12, 6))


ax.plot(fechas_sitka, temperaturas_sitka, c='blue', label='Sitka')


ax.plot(fechas_death_valley, temperaturas_death_valley, c='red', label='Death Valley')


ax.set_title("Comparación de Temperaturas Máximas: Sitka vs Death Valley", fontsize=20)
ax.set_xlabel('Fecha', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura Máxima (°C)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

ax.set_ylim([min_temp, max_temp])

ax.legend()

plt.show()

#jaris y alexa
