"""Genera algunas visualizaciones adicionales que examinen otros aspectos meteorológicos que te interesen,
 en cualquier ubicación que tengas curiosidad por explorar."""
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Cargar el archivo de datos
nombre_archivo = 'SM1/Descargando Datos/data/death_valley_2021_simple.csv'

fechas, altas, bajas, precipitaciones = [], [], [], []

# Leer el archivo y manejar datos faltantes
with open(nombre_archivo) as archivo:
    lector = csv.reader(archivo)
    fila_encabezado = next(lector)
    
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            alta = int(fila[4])
            baja = int(fila[5])
            precipitacion = float(fila[3]) if fila[3] else 0.0  # manejar datos de precipitación
        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")
        else:
            fechas.append(fecha_actual)
            altas.append(alta)
            bajas.append(baja)
            precipitaciones.append(precipitacion)



# Gráfico de dispersión entre temperaturas máximas y mínimas
plt.figure(figsize=(10, 5))
plt.scatter(altas, bajas, color='purple', alpha=0.5)
plt.title("Relación entre Temperaturas Máximas y Mínimas - 2021\nDeath Valley, CA")
plt.xlabel("Temperatura Máxima (°F)")
plt.ylabel("Temperatura Mínima (°F)")
plt.tight_layout()
plt.show()

