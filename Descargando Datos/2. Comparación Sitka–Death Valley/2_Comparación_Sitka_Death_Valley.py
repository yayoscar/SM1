"""Las escalas de temperatura en los gráficos de Sitka y Death Valley reflejan los 
 diferentes rangos de datos. Para comparar con precisión el rango de temperaturas en
 Sitka y Death Valley, necesitas escalas idénticas en el eje y. Cambia la configuración del eje 
 y en uno o ambos gráficos de las **5** y **6**. Luego haz una comparación directa entre los rangos 
 de temperatura en Sitka y Death Valley (o cualquier otro par de lugares que quieras comparar).
"""
import csv
from datetime import datetime
import matplotlib.pyplot as plt

nombre_archivo_0='Descargando Datos/data/sitka_weather_2021_simple.csv'
nombre_archivo_1='Descargando Datos/data/death_valley_2021_simple.csv'

with open(nombre_archivo_0) as archivo:

    lector=csv.reader(archivo)     
    fila_encabezado=next(lector)

    tem_alta_sitka,temp_baja_sitka,fechas=[],[],[]
    for fila in lector:
        fecha_actual=datetime.strptime(fila[2],'%Y-%m-%d')
        fechas.append(fecha_actual)
        sitka_alta=int(fila[4])
        tem_alta_sitka.append( sitka_alta)
        sitka_baja=int(fila[5])
        temp_baja_sitka.append(sitka_baja)

with open(nombre_archivo_1) as archiv:
    
    lector=csv.reader(archiv) 
    fila_encabezado=next(lector)

    fechas_d,tem_alta_death,tem_baja_death=[],[],[]
    for fila in lector:
        fecha_actual_d=datetime.strptime(fila[2],'%Y-%m-%d')
        fechas_d.append(fecha_actual_d)
        death_alta=int(fila[4])
        tem_alta_death.append(death_alta)
        death_baja=int(fila[4])
        tem_baja_death.append(death_baja)
   
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(fechas,tem_alta_sitka,c='pink',alpha=0.5)
ax.plot(fechas,temp_baja_sitka,c='pink',alpha=0.5)
ax.plot(fechas_d,tem_alta_death,c='purple',alpha=0.5)
ax.plot(fechas_d,tem_baja_death,c='purple',alpha=0.5)
plt.fill_between(fechas,tem_alta_sitka,temp_baja_sitka,facecolor='blue',alpha=0.1)

plt.title('Temperaturas Rango Sitka y Death Valley',fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperatura (F),fontsize=16')
fig.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()


