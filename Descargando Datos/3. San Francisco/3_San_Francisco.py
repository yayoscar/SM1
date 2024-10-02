""" ¿Las temperaturas en San Francisco son más parecidas a las de Sitka o
 a las de Death Valley? Descarga algunos datos para San Francisco y genera 
 un gráfico de temperaturas máximas y mínimas para comparar."""
import csv
from datetime import datetime
import matplotlib.pyplot as plt

nombre_archivo='Descargando Datos/data/san_francisco.csv'

with open(nombre_archivo) as archivo:
    
    lector=csv.reader(archivo)
    fila_encabezado=next(lector)

    altas,fechas,bajas=[],[],[]
    for fila in lector:
        fecha_actual=datetime.strptime(fila[0],'%Y-%m-%d')
        try:
            alta=int(fila[0])
            baja=int(fila[0])

        except ValueError:
            print(f"Datos faltantes para {fecha_actual}")

        else:
           fechas.append(fecha_actual)
           altas.append(alta)
           bajas.append(baja)

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(fechas,altas,c='blue',alpha=0.5)
ax.plot(fechas,bajas,c='yelow',alpha=0.5)
plt.fill_between(fechas,altas,bajas,facecolor='blue',alpha=0.1)

plt.title('Temperaturas máximas y mínimas San Francisco',fontsize=16)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperatura (F),fontsize=16')
fig.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()