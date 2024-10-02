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

nombre_archivo='Descargando Datos\data\sitka_weather_2021_full.csv'

with open(nombre_archivo) as archivo:
    #Creamos Un objeto lector para leer el objeto csv
    lector = csv.reader(archivo)

    #Leer los encabezaados de la primera linea
    Fila_encabezado = next(lector)

    altas,fechas,bajas= [],[],[]
    for fila in lector:
        fecha_actual= datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            alta_ = int(fila[7])
            Baja_ = int(fila[8])
        except ValueError:
            print(f"Datos faltantes para {fecha_actual} sitka")
        else:
            fechas.append(fecha_actual)
            altas.append(alta_)
            bajas.append(Baja_)

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(fechas, altas, c='Red', linewidth=0.8, label=f"Máximas")
ax.plot(fechas, bajas, c='Blue', linewidth=0.8, label=f"Mínimas")
ax.legend(loc='upper right', fontsize=10)
plt.fill_between(fechas, altas, bajas, facecolor='Purple', alpha=0.4)


#Formato del grafico
ax.title.set_text('"Temperaturas máximas y mínimas diarias - entre sitka. y Death Valley, CA')
ax.set_xlabel('',fontsize= 16)
ax.set_ylabel('Temperatura (F)')
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=14)


# Mostrar el gráfico
plt.show()
