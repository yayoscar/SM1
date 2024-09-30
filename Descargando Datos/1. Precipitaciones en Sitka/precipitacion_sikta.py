import csv
from datetime import datetime
import matplotlib.pyplot as plt

nombre_archivo = 'DescargandoDatos/data/sitka_weather_2021_full.csv'
with open(nombre_archivo) as archivo:
    lector = csv.reader(archivo)
    fila_encabezado = next(lector)
    # Obtener las fechas y las temperaturas máximas de este archivo.
    fechas,precipitaciones = [],[]
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            precipitacion = int(fila[4])
        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")
        else:
            fechas.append(fecha_actual)
            precipitaciones.append(precipitacion)
 # Graficar las temperaturas máximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(fechas,precipitaciones, c='blue')


 # Formato del gráfico.
plt.title("Precipitaciones registradas, Año 2021", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitacion (PRCP)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()