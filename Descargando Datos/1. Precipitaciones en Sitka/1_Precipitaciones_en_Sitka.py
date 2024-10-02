"""Sitka está en un bosque lluvioso templado, por lo que recibe una cantidad considerable de lluvia. 
En el archivo de datos `sitka_weather_2021_simple.csv` hay un encabezado llamado `PRCP`, 
que representa las cantidades diarias de lluvia. Haz una visualización enfocada en los datos de esta columna. 
Puedes repetir el ejercicio para Death Valley si te interesa ver cuánta poca lluvia cae en un desierto."""

import csv
from datetime import datetime
import matplotlib.pyplot as plt


nombre_archivo='Descargando Datos/data/sitka_weather_2021_full.csv'

with open(nombre_archivo) as archivo:
    
    lector=csv.reader(archivo)
     
    fila_encabezado=next(lector)

    fechas,precipitaciones,=[],[]
    for fila in lector:
        fecha_actual=datetime.strptime(fila[2],'%Y-%m-%d')
        precipitacion=float(fila[5])
        fechas.append(fecha_actual)
        precipitaciones.append(precipitacion)

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(fechas,precipitaciones,c='orange',alpha=0.5)

plt.title('Cantidades diarias de lluvia -2021-Sitka, AK',fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Precipitaciones',fontsize=20)
fig.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
