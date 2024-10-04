import csv 
import matplotlib.pyplot as plt
from datetime import datetime 

nombre_archivo = 'data/sitka_weather_2021_simple.csv'

# Abrimos el archivo CSV
with open(nombre_archivo) as archivo:
        # Creamos un objeto lector para leer el archivo CSV
        lector = csv.reader(archivo)

        # Obtenemos la primera línea del archivo (los encabezados)
        fila_encabezado = next(lector)

       
        # Obtener las temperaturas máximas de este archivo
        altas, fechas, bajas = [], [], []
        for fila in lector:
            fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
            fechas.append(fecha_actual)
            alta = int(fila[4])
            altas.append(alta)
            baja=int(fila[5])
            bajas.append(baja)

#crear un grafico de las temperaturas maximas y minimas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(fechas, altas,c='red', alpha=0.5)
ax.plot(fechas, bajas,c='blue', alpha=0.5)
plt.fill_between(fechas, altas, bajas, facecolor='blue', alpha=0.1)

# Formato del gráfico
plt.title("Temperaturas máximas y minimas diarias, año 2021", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show() 





