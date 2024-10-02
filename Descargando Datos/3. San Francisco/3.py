import pandas as pd
import matplotlib.pyplot as plt

sitka_data = pd.read_csv('Descargando Datos/data/sitka_weather_2021_full.csv')
sitka_data['date'] = pd.to_datetime(sitka_data['DATE'])
sitka_max = sitka_data.groupby('date')['TMAX'].max()
sitka_min = sitka_data.groupby('date')['TMIN'].min()

death_valley_data = pd.read_csv('Descargando Datos/data/death_valley_2021_simple.csv')
death_valley_data['date'] = pd.to_datetime(death_valley_data['DATE'])
death_valley_max = death_valley_data.groupby('date')['TMAX'].max()
death_valley_min = death_valley_data.groupby('date')['TMIN'].min()

sf_data = pd.read_csv('Descargando Datos/data/sanfrancisco.csv')
print(sf_data.columns)
sf_data['date'] = pd.to_datetime(sf_data['Date'])
sf_max = sf_data.groupby('date')['Max.TemperatureF'].max()
sf_min = sf_data.groupby('date')['Min.TemperatureF'].min()

plt.figure(figsize=(12, 6))
plt.plot(sitka_max.index, sitka_max, label='Max Temp Sitka', color='blue', linewidth=2)
plt.plot(sitka_min.index, sitka_min, label='Min Temp Sitka', color='lightblue', linestyle='--')

plt.plot(death_valley_max.index, death_valley_max, label='Max Temp Death Valley', color='red', linewidth=2)
plt.plot(death_valley_min.index, death_valley_min, label='Min Temp Death Valley', color='lightcoral', linestyle='--')

plt.plot(sf_max.index, sf_max, label='Max Temp San Francisco', color='green', linewidth=2)
plt.plot(sf_min.index, sf_min, label='Min Temp San Francisco', color='lightgreen', linestyle='--')

plt.title('Comparación de Temperaturas Máximas y Mínimas')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°F)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
