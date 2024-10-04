import csv
import matplotlib.pyplot as plt
from datetime import datetime

nombre_archivo = 'Descargando Datos/data/sanfrancisco.csv'

with open(nombre_archivo) as archivo:
    lector = csv.reader(archivo)
    fila_encabezado = next(lector)

    for indice, encabezado_columna in enumerate(fila_encabezado):
        print(indice, encabezado_columna)

    altas, fechas, bajas = [], [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[1],'%Y-%m-%d')
        try:
            alta = int(fila[3])
            baja = int(fila[4])
        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")
        else:
            fechas.append(fecha_actual)
            altas.append(alta)
            bajas.append(baja)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(fechas, altas, c='red', alpha=0.5, label='Máxima')
ax.plot(fechas, bajas, c='blue', alpha=0.5, label='Mínima')
plt.fill_between(fechas, altas, bajas, facecolor='blue', alpha=0.1)


plt.title("Temperaturas máximas y mínimas diarias, año 2021 - San Francisco, CA", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend()
plt.show()


#EL ARCHIVO NO CARGA DEBIDO A QUE NO SE PUEDE DESCARGAR EN EL LINK QUE NOS COMPARTIO PROFE