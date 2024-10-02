import csv
from datetime import datetime
import  matplotlib.pyplot as plt

nombre_archivo= 'Descargando Datos\\data\\sitka_weather_2021_full.csv'

#Abrir archivo

with open(nombre_archivo) as archivo:
    #Creamos Un objeto lector para leer el objeto csv
    lector = csv.reader(archivo)

    #Leer los encabezaados de la primera linea
    Fila_encabezado = next(lector)

    #Obtener las temperaturas de la columna con indice 5 TMAX
    Altas,Fechas,Bajas,Lluvias = [],[],[],[]
    for fila in lector:
        fecha_actual= datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            alta = int(fila[7])
            Baja = int(fila[8])
            lluvias=float(fila[5])
        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")
        else:
            Fechas.append(fecha_actual)
            Altas.append(alta)
            Bajas.append(Baja)
            Lluvias.append(lluvias)


#Crear un grafico de las temperaturas máximas
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(Fechas, Altas, c='red', linewidth=0.4, label="Max")
ax.plot(Fechas, Bajas, c='blue', linewidth=0.4, label="Min")
ax.plot(Fechas,Lluvias, c= 'Green',linewidth=0., label ="Lluvias")
ax.legend(loc='upper right', fontsize=10)
plt.fill_between(Fechas, Altas, Bajas, facecolor='Purple', alpha=0.4)

#Formato del grafico
ax.title.set_text('Temperaturas maximas diarias, Año 2018 - Sitka, Ak ')
ax.set_xlabel('',fontsize= 16)
ax.set_ylabel('Temperatura (F)')
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
