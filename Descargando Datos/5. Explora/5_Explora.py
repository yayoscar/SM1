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

# Gráfico de temperaturas máximas y mínimas
plt.figure(figsize=(10, 5))
plt.plot(fechas, altas, label='Temperatura Máxima', color='red')
plt.plot(fechas, bajas, label='Temperatura Mínima', color='blue')
plt.fill_between(fechas, altas, bajas, color='lightgray', alpha=0.5)
plt.title("Temperaturas máximas y mínimas diarias - 2018\nDeath Valley, CA")
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°F)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de precipitación
plt.figure(figsize=(10, 5))
plt.bar(fechas, precipitaciones, color='blue', alpha=0.7)
plt.title("Precipitación diaria - 2021\nDeath Valley, CA")
plt.xlabel("Fecha")
plt.ylabel("Precipitación (pulgadas)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de dispersión entre temperaturas máximas y mínimas
plt.figure(figsize=(10, 5))
plt.scatter(altas, bajas, color='purple', alpha=0.5)
plt.title("Relación entre Temperaturas Máximas y Mínimas - 2021\nDeath Valley, CA")
plt.xlabel("Temperatura Máxima (°F)")
plt.ylabel("Temperatura Mínima (°F)")
plt.tight_layout()
plt.show()

# Histograma de temperaturas máximas
plt.figure(figsize=(10, 5))
plt.hist(altas, bins=20, color='orange', alpha=0.7)
plt.title("Distribución de Temperaturas Máximas - 2021\nDeath Valley, CA")
plt.xlabel("Temperatura Máxima (°F)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()