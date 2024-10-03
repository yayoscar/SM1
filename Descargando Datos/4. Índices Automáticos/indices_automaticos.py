import csv
from datetime import datetime
import matplotlib.pyplot as plt

def leer_datos(nombre_archivo):
    """Lee los datos de temperatura desde un archivo CSV."""
    with open(nombre_archivo) as archivo:
        lector = csv.reader(archivo)
        Fila_encabezado = next(lector)
        
        # Determinar los índices de las columnas TMAX y TMIN
        indice_fecha = Fila_encabezado.index('DATE')
        indice_max = Fila_encabezado.index('TMAX')
        indice_min = Fila_encabezado.index('TMIN')
        indice_nombre_estacion = Fila_encabezado.index('NAME')

        # Extraer las temperaturas y fechas
        altas, bajas, fechas, nombre_estacion = [], [], [], None
        for fila in lector:
            fecha_actual = datetime.strptime(fila[indice_fecha], '%Y-%m-%d')
            try:
                alta = int(fila[indice_max])
                baja = int(fila[indice_min])
                nombre_estacion = fila[indice_nombre_estacion]  # Obtener el nombre de la estación
            except ValueError:
                print(f"Datos faltantes para {fecha_actual}")
            else:
                fechas.append(fecha_actual)
                altas.append(alta)
                bajas.append(baja)

    return fechas, altas, bajas, nombre_estacion

# Leer los datos de ambos archivos
nombre_archivo_1= 'Descargando Datos/data/death_valley_2021_full.csv'
nombre_archivo_2='Descargando Datos/data/sitka_weather_2021_full.csv'


fechas_1, altas_1, bajas_1, nombre_estacion_1 = leer_datos(nombre_archivo_1)
fechas_2, altas_2, bajas_2, nombre_estacion_2 = leer_datos(nombre_archivo_2)

# Crear el gráfico de las temperaturas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Graficar los datos de la primera estación
ax.plot(fechas_1, altas_1, c='Red', linewidth=0.8, label=f"Máximas {nombre_estacion_1}")
ax.plot(fechas_1, bajas_1, c='Blue', linewidth=0.8, label=f"Mínimas {nombre_estacion_1}")
plt.fill_between(fechas_1, altas_1, bajas_1, facecolor='Purple', alpha=0.4)

# Graficar los datos de la segunda estación
ax.plot(fechas_2, altas_2, c='Yellow', linewidth=0.8, label=f"Máximas {nombre_estacion_2}")
ax.plot(fechas_2, bajas_2, c='Green', linewidth=0.8, label=f"Mínimas {nombre_estacion_2}")
plt.fill_between(fechas_2, altas_2, bajas_2, facecolor='Grey', alpha=0.4)

# Formato del gráfico
ax.set_title(f"Temperaturas máximas y mínimas diarias - {nombre_estacion_1} y {nombre_estacion_2}")
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatura (F)', fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=14)

# Añadir leyenda
ax.legend()

# Mostrar el gráfico
plt.show()
