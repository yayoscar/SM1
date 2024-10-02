"""Las escalas de temperatura en los gráficos de Sitka y Death Valley reflejan los 
 diferentes rangos de datos. Para comparar con precisión el rango de temperaturas en
 Sitka y Death Valley, necesitas escalas idénticas en el eje y. Cambia la configuración del eje 
 y en uno o ambos gráficos de las **5** y **6**. Luego haz una comparación directa entre los rangos 
 de temperatura en Sitka y Death Valley (o cualquier otro par de lugares que quieras comparar).
"""
import csv
from datetime import datetime
import matplotlib.pyplot as plt

#donde se encuentra el archivo(direccion del archivo)
nombre_archivo_0='Descargando Datos/data0/sitka_weather_2021_simple.csv'
nombre_archivo_1='Descargando Datos/data0/death_valley_2021_simple.csv'

#Abrimos el archivo csv
with open(nombre_archivo_0) as archivo:
    #creamos un objeto csv reader
    lector=csv.reader(archivo)
     
    #leer los encabezados de la primera fila
    fila_encabezado=next(lector)

    #obtener temperaturas 
    tem_alta_sitka,temp_baja_sitka,fechas=[],[],[]
    for fila in lector:
        fecha_actual=datetime.strptime(fila[2],'%Y-%m-%d')
        fechas.append(fecha_actual)
        sitka_alta=int(fila[4])
        tem_alta_sitka.append( sitka_alta)
        sitka_baja=int(fila[5])
        temp_baja_sitka.append(sitka_baja)

with open(nombre_archivo_1) as archiv:
    #creamos un objeto csv reader
    lector=csv.reader(archiv)
     
    #leer los encabezados de la primera fila
    fila_encabezado=next(lector)

    #obtener temperaturas 
    fechas_d,tem_alta_death,tem_baja_death=[],[],[]
    for fila in lector:
        fecha_actual_d=datetime.strptime(fila[2],'%Y-%m-%d')
        fechas_d.append(fecha_actual_d)
        death_alta=int(fila[4])
        tem_alta_death.append(death_alta)
        death_baja=int(fila[4])
        tem_baja_death.append(death_baja)
   
#crea un grafico de las temperaturas maximas y mínimas
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(fechas,tem_alta_sitka,c='green',alpha=0.5)
ax.plot(fechas,temp_baja_sitka,c='green',alpha=0.5)
ax.plot(fechas_d,tem_alta_death,c='purple',alpha=0.5)
ax.plot(fechas_d,tem_baja_death,c='purple',alpha=0.5)
plt.fill_between(fechas,tem_alta_sitka,temp_baja_sitka,facecolor='blue',alpha=0.1)

#formatear el grafico
plt.title('Temperaturas Rango Sitka y Death Valley',fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperatura (F),fontsize=16')
fig.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()


