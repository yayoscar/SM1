"""Genera algunas visualizaciones adicionales que examinen otros aspectos meteorológicos que te interesen,
 en cualquier ubicación que tengas curiosidad por explorar."""
import csv
from datetime import datetime
import matplotlib.pyplot as plt


nombre_archivo = 'Descargando Datos/data/death_valley_2021_simple.csv'

fechas, altas, bajas, precipitaciones = [], [], [], []

with open(nombre_archivo) as archivo:
    lector = csv.reader(archivo)
    fila_encabezado = next(lector)
    
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            alta = int(fila[4])
            baja = int(fila[5])
            precipitacion = float(fila[3]) if fila[3] else 0.0  
        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")
        else:
            fechas.append(fecha_actual)
            altas.append(alta)
            bajas.append(baja)
            precipitaciones.append(precipitacion)

plt.figure(figsize=(10, 5))
plt.hist(altas, bins=20, color='pink', alpha=0.7)
plt.title("Distribución de Temperaturas Máximas - 2020\nDeath Valley, CA")
plt.xlabel("Temperatura Máxima (°F)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()