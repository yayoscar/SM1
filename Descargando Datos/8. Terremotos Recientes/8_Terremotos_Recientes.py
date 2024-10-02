"""Puedes encontrar archivos de datos en línea que contienen información sobre los terremotos más recientes 
en periodos de 1 hora, 1 día, 7 días y 30 días. Ve a 
[https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) 
y verás una lista de enlaces a conjuntos de datos para varios periodos de tiempo, 
enfocados en terremotos de diferentes magnitudes.Descarga uno de estos conjuntos de datos 
y crea una visualización de la actividad sísmica más reciente."""
from pathlib import Path
import json
import plotly.express as px
import requests

# Descargar el conjunto de datos de terremotos recientes
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
respuesta = requests.get(url)

# Verificar que la respuesta fue exitosa
if respuesta.status_code == 200:
    datos_terremotos_recientes = respuesta.json()
else:
    raise Exception("No se pudieron obtener los datos.")

# Obtener los diccionarios de todos los terremotos
todos_los_dicc_terremotos = datos_terremotos_recientes['features']

# Inicializar listas para almacenar magnitudes, longitudes y latitudes
magnitudes, longitudes, latitudes = [], [], []

# Extraer datos
for dicc_terremoto in todos_los_dicc_terremotos:
    magnitudes.append(dicc_terremoto['properties']['mag'])
    longitudes.append(dicc_terremoto['geometry']['coordinates'][0])
    latitudes.append(dicc_terremoto['geometry']['coordinates'][1])

# Título automatizado
titulo = datos_terremotos_recientes['metadata']['title']

# Crear el mapa
fig = px.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    size=magnitudes,
    title=titulo,
    color=magnitudes,
    color_continuous_scale='Viridis',
    labels={'color': 'Magnitud'},
    projection='natural earth',
)

fig.show()