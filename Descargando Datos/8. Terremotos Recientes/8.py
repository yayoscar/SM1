import json
import matplotlib.pyplot as plt
import requests

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
response = requests.get(url)

if response.status_code == 200:
    all_eq_data = response.json()
    magnitudes, longitudes, latitudes = [], [], []

    for eq_dict in all_eq_data['features']:
        magnitudes.append(eq_dict['properties']['mag'])
        longitudes.append(eq_dict['geometry']['coordinates'][0])
        latitudes.append(eq_dict['geometry']['coordinates'][1])

    plt.figure(figsize=(10, 6))
    plt.scatter(longitudes, latitudes, c=magnitudes, cmap='viridis', s=10)
    plt.colorbar(label='Magnitude')
    plt.title('Recent Earthquakes')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()
else:
    print("Error al obtener los datos:", response.status_code)
