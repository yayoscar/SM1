import csv 
import matplotlib.pyplot as plt
from datetime import datetime 

nombre_archivo = 'data/sitka_weather_2021_full.csv'

# Abrimos el archivo CSV
with open(nombre_archivo) as archivo:
        # Creamos un objeto lector para leer el archivo CSV
        lector = csv.reader(archivo)

        # Obtenemos la primera línea del archivo (los encabezados)
        fila_encabezado = next(lector)

        
        precipitaciones, fechas = [], []
        
        for fila in lector:
            fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
            fechas.append(fecha_actual)
            precipitacion = float(fila[5])
            precipitaciones.append(precipitacion)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(fechas, precipitaciones,c='red')

# Formato del gráfico
plt.title("Fechas", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitacion", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show() 





