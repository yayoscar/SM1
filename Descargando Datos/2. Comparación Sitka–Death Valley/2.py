import csv
import matplotlib.pyplot as plt
from datetime import datetime

sitka_filename = 'Descargando Datos\data\sitka_weather_2021_simple.csv'
death_valley_filename = 'Descargando Datos\data\death_valley_2021_simple.csv'

sitka_dates, sitka_tmaxs = [], []
death_valley_dates, death_valley_tmaxs = [], []

with open(sitka_filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    tmax_index = header_row.index('TMAX')
    date_index = header_row.index('DATE')

    for row in reader:
        try:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            tmax = float(row[tmax_index])
        except ValueError:
            continue
        else:
            sitka_dates.append(current_date)
            sitka_tmaxs.append(tmax)

with open(death_valley_filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    tmax_index = header_row.index('TMAX')
    date_index = header_row.index('DATE')

    for row in reader:
        try:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            tmax = float(row[tmax_index])
        except ValueError:
            continue
        else:
            death_valley_dates.append(current_date)
            death_valley_tmaxs.append(tmax)

plt.figure(figsize=(10, 8))
plt.plot(sitka_dates, sitka_tmaxs, c='blue', label='Sitka')
plt.plot(death_valley_dates, death_valley_tmaxs, c='red', label='Death Valley')

plt.title("Comparación de Temperaturas Máximas entre Sitka y Death Valley - 2021", fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Temperatura Máxima (°F)', fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 130) 
plt.xlim(min(sitka_dates + death_valley_dates), max(sitka_dates + death_valley_dates))
plt.legend()
plt.tight_layout(pad=2.0)

plt.show()
