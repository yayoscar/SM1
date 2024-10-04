import csv
from datetime import datetime
import matplotlib.pyplot as plt

def leer_datos(nombre_archivo):
    """Lee los datos de temperatura desde un archivo CSV."""
    with open(nombre_archivo) as archivo:
        lector = csv.reader(archivo)
        fila_encabezado = next(lector)
        
        # Determinar los índices de las columnas TMAX y TMIN
        indice_fecha = fila_encabezado.index('DATE')
        indice_max = fila_encabezado.index('TMAX')
        indice_min = fila_encabezado.index('TMIN')

        # Extraer las temperaturas y fechas
        altas, bajas, fechas = [], [], []
        for fila in lector:
            try:
                fecha_actual = datetime.strptime(fila[indice_fecha], '%Y-%m-%d')
                alta = int(fila[indice_max])
                baja = int(fila[indice_min])
            except ValueError:
                print(f"Datos faltantes para {fecha_actual}")
            else:
                fechas.append(fecha_actual)
                altas.append(alta)
                bajas.append(baja)

    return fechas, altas, bajas

# Nombre del archivo
nombre_archivo = 'Descargando Datos/data/sitka_weather_2021_full.csv'

# Leer los datos
fechas, altas, bajas = leer_datos(nombre_archivo)

# Crear el gráfico de temperaturas
plt.style.use('ggplot')  # Cambiar a un estilo válido

fig, ax = plt.subplots()
ax.plot(fechas, altas, c='red', linewidth=0.8, label="Máximas")
ax.plot(fechas, bajas, c='blue', linewidth=0.8, label="Mínimas")
ax.fill_between(fechas, altas, bajas, facecolor='purple', alpha=0.4)
ax.legend(loc='upper right', fontsize=10)

# Formato del gráfico
ax.set_title('Temperaturas máximas y mínimas diarias en Sitka, AK')
ax.set_xlabel('Fecha', fontsize=16)
ax.set_ylabel('Temperatura (°F)', fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=14)

# Mostrar el gráfico
plt.show()