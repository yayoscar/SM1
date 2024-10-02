import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Descargando Datos\data\death_valley_2021_simple.csv'

dates, tmaxs = [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    print(header_row)

    tmax_index = header_row.index('TMAX')
    date_index = header_row.index('DATE')

    for row in reader:
        try:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            tmax = float(row[tmax_index])
        except ValueError:
            print(f"Datos faltantes para {row[date_index]}")
            continue
        else:
            dates.append(current_date)
            tmaxs.append(tmax)

plt.figure(figsize=(10, 6))
plt.plot(dates, tmaxs, c='red')

plt.title("Temperatura Máxima Diaria en Death Valley - 2021", fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Temperatura Máxima (°F)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
