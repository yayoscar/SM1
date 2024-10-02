import csv
from datetime import datetime
import  matplotlib.pyplot as plt

nombre_archivo= '/Users/pattu/Desktop/5to SEMESTRE/Descargando_datos/data/death_valley_2021_full.csv'
nombre_archivo_2='/Users/pattu/Desktop/5to SEMESTRE/Descargando_datos/data/sitka_weather_2021_full.csv'

#Abrir archivo

with open(nombre_archivo) as archivo:
    #Creamos Un objeto lector para leer el objeto csv
    lector = csv.reader(archivo)

    #Leer los encabezaados de la primera linea
    Fila_encabezado = next(lector)

    #Obtener las temperaturas de la columna con indice 5 TMAX
    Altas,Fechas,Bajas = [],[],[]
    for fila in lector:
        fecha_actual= datetime.strptime(fila[2], '%Y-%m-%d')
        try:
            alta = int(fila[6])
            Baja = int(fila[7])
        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")
        else:
            Fechas.append(fecha_actual)
            Altas.append(alta)
            Bajas.append(Baja)

with open(nombre_archivo_2) as archivo:
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



#Crear un grafico de las temperaturas máximas
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(Fechas,Altas, c= 'Red',linewidth=0.8)
ax.plot(Fechas,Bajas, c= 'Blue',linewidth=0.8)
plt.fill_between(Fechas, Altas, Bajas, facecolor='Purple', alpha=0.4)

ax.plot(fechas,altas, c= 'Yellow',linewidth=0.8)
ax.plot(fechas,bajas, c= 'Green',linewidth=0.8)
plt.fill_between(fechas, altas, bajas, facecolor='Grey', alpha=0.4)

#Formato del grafico
ax.title.set_text('"Temperaturas máximas y mínimas diarias - entre sitka. y Death Valley, CA')
ax.set_xlabel('',fontsize= 16)
ax.set_ylabel('Temperatura (F)')
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
