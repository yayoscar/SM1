import csv
import matplotlib.pyplot as plt

filename = 'Descargando Datos\data\sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    tmin_index = header_row.index('TMIN')
    tmax_index = header_row.index('TMAX')

    tmins, tmaxs = [], []
    for row in reader:
        tmins.append(float(row[tmin_index]))
        tmaxs.append(float(row[tmax_index]))

plt.figure(figsize=(10, 6))
plt.plot(tmins, label='Temperatura Mínima')
plt.plot(tmaxs, label='Temperatura Máxima')
plt.title('Temperaturas Mínimas y Máximas en Sitka (2021)')
plt.xlabel('Días del Año')
plt.ylabel('Temperatura (°F)')
plt.legend()
plt.show()
