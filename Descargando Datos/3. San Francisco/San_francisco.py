import csv
from datetime import datetime
import  matplotlib.pyplot as plt

nombre_archivo= 'Descargando Datos\data\sanfrancisco.csv'

#Abrir archivo

with open(nombre_archivo) as archivo:
    #Creamos Un objeto lector para leer el objeto csv
    lector = csv.reader(archivo)

    #Leer los encabezaados de la primera linea
    Fila_encabezado = next(lector)

    #Obtener las temperaturas de la columna con indice 5 TMAX
    Altas,Fechas,Bajas = [],[],[]
    for fila in lector:
        try:
            # Convertir el texto de la fecha a un objeto datetime
            fecha = datetime.strptime(fila[1], '%Y-%m-%d')
            
            # Verificar que la fecha pertenece al año 2021
            if fecha.year == 2015:
                # Leer temperaturas altas y bajas
                alta = int(fila[2])
                baja = int(fila[4])
                
                # Almacenar la fecha y las temperaturas en las listas
                Fechas.append(fecha)
                Altas.append(alta)
                Bajas.append(baja)
        except ValueError as e:
            # Imprimir cualquier error encontrado, como datos faltantes o formatos incorrectos
            print(f"Error procesando la fila {fila}: {e}")


#Crear un grafico de las temperaturas máximas
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(Fechas,Altas, c= 'red',linewidth=0.4, label="Altas")
ax.plot(Fechas,Bajas, c= 'blue',linewidth=0.4 ,label="Bajas")
ax.legend(loc='upper right', fontsize=10)
plt.fill_between(Fechas, Altas, Bajas, facecolor='Purple', alpha=0.4)

#Formato del grafico
ax.title.set_text('Temperaturas maximas y minimas diarias, san francisco, Ak ')
ax.set_xlabel('',fontsize= 16)
ax.set_ylabel('Temperatura (F)')
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
