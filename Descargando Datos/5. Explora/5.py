import csv
import matplotlib.pyplot as plt

filename = 'Descargando Datos\data\sitka_weather_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    awnd_index = header_row.index('AWND')

    wind_speeds = []
    for row in reader:
        if row[awnd_index]:  
            wind_speeds.append(float(row[awnd_index]))

plt.figure(figsize=(10, 6))
plt.plot(wind_speeds, label='Velocidad Promedio del Viento (m/s)', color='orange')
plt.title('Velocidad Promedio del Viento en Sitka (2021)')
plt.xlabel('Días del Año')
plt.ylabel('Velocidad del Viento (m/s)')
plt.legend()
plt.show()
