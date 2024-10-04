import csv
from datetime import datetime
import matplotlib.pyplot as plt

def leer_datos(nombre_archivo):
    """Lee los datos de temperatura desde un archivo CSV."""
    with open(nombre_archivo) as archivo:
        lector = csv.reader(archivo)
        Fila_encabezado = next(lector)
        
        # Determinar los índices de las columnas TMAX y TMIN
        indice_fecha = Fila_encabezado.index('DATE' )
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

nombre_archivo='SM1/Descargando Datos/data/sitka_weather_2021_full.csv'
with open(nombre_archivo) as archivo:
    # Creamos un objeto lector para leer el objeto csv
    lector = csv.reader(archivo)

    # Leer los encabezados de la primera línea
    Fila_encabezado = next(lector)

    altas, fechas, bajas = [], [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            # Asegurarse de que ambas temperaturas estén presentes
            alta = int(fila[7])
            baja = int(fila[8])
        except ValueError:
            print(f"Datos faltantes para {fecha_actual} sitka")
        else:
            fechas.append(fecha_actual)
            altas.append(alta)
            bajas.append(baja)

# Verificar la longitud de las listas antes de graficar
print(f"Número de fechas: {len(fechas)}")
print(f"Número de altas: {len(altas)}")
print(f"Número de bajas: {len(bajas)}")

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(fechas, altas, c='Red', linewidth=0.8, label=f"Máximas")
ax.plot(fechas, bajas, c='Blue', linewidth=0.8, label=f"Mínimas")
ax.legend(loc='upper right', fontsize=10)
plt.fill_between(fechas, altas, bajas, facecolor='Purple', alpha=0.4)

# Formato del gráfico
ax.title.set_text('"Temperaturas máximas y mínimas diarias - entre Sitka y Death Valley, CA')
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatura (F)')
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=14)

# Mostrar el gráfico
plt.show()
