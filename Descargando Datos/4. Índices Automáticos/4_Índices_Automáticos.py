"""En esta sección, escribimos de manera fija los índices correspondientes a las columnas `TMIN` y `TMAX`.
 Usa la fila de encabezado para determinar los índices de estos valores, de modo que tu programa pueda 
 funcionar tanto para Sitka como para Death Valley.Usa el nombre de la estación para generar automáticamente
 un título apropiado para tu gráfico."""


import csv
from datetime import datetime
import matplotlib.pyplot as plt

nombre_archivo = 'SM1/Descargando Datos/data/death_valley_2021_simple.csv'
nombre_archivo_1='SM1/Descargando Datos/data/sitka_weather_2021_simple.csv'

with open(nombre_archivo) as archivo:
    lector = csv.reader(archivo)
    fila_encabezado = next(lector)

    # Obtener índices de TMIN y TMAX
    indice_tmin = fila_encabezado.index('TMIN')
    indice_tmax = fila_encabezado.index('TMAX')
    indice_fecha = fila_encabezado.index('DATE')

    # Obtener las fechas, y las temperaturas máximas y mínimas
    altas, fechas, bajas = [], [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            alta = int(fila[3])
            baja = int(fila[4])
        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")
        else:
            fechas.append(fecha_actual)
            altas.append(alta)
            bajas.append(baja)

with open(nombre_archivo_1) as archivo:
    lector = csv.reader(archivo)
    fila_encabezado = next(lector)

    # Obtener índices de TMIN y TMAX
    indice_tmin = fila_encabezado.index('TMIN')
    indice_tmax = fila_encabezado.index('TMAX')
    indice_fecha = fila_encabezado.index('DATE')

    # Obtener las fechas, y las temperaturas máximas y mínimas
    altas, fechas, bajas = [], [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            alta = int(fila[4])
            baja = int(fila[5])
        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")
        else:
            fechas.append(fecha_actual)
            altas.append(alta)
            bajas.append(baja)

# Crear gráfico
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(fechas, altas, c='red', alpha=0.5)
ax.plot(fechas, bajas, c='blue', alpha=0.5)
plt.fill_between(fechas, altas, bajas, facecolor='blue', alpha=0.1)

# Formatear gráfico
if nombre_archivo.endswith('death_valley_2021_simple.csv'):
    titulo = f'Temperaturas máximas y mínimas diarias - 2021\nDeath Valley, CA'
elif nombre_archivo.endswith('sitka_weather_2021_simple.csv'):
    titulo = f'Temperaturas máximas y mínimas diarias - 2021\nSitka, AK'
else:
    nombre_lugar = nombre_archivo.split('/')[-1].split('_')[0].title()
    titulo = f'Temperaturas máximas y mínimas diarias - 2021\n{nombre_lugar}'

if nombre_archivo_1.endswith('sitka_weather_2021_simple.csv'):
    titulo_1 = f'Temperaturas máximas y mínimas diarias - 2021\nSitka, AK,'
elif nombre_archivo_1.endswith('death_valley_2021_simple.csv'):
    titulo_1 = f'Temperaturas máximas y mínimas diarias - 2021\nDeath Valley, CA'
else:
    nombre_lugar_2 = nombre_archivo_1.split('/')[-1].split('_')[0].title()
    titulo_1 = f'Temperaturas máximas y mínimas diarias - 2021\n{nombre_lugar_2}'

plt.title(titulo, fontsize=16)
plt.title(titulo_1, fontsize=16)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperatura (F)', fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
