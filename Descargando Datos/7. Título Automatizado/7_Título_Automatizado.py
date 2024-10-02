"""En esta sección, usamos el título genérico *Terremotos Globales*. En su lugar, 
puedes usar el título del conjunto de datos en la parte de metadatos del archivo GeoJSON.
Extrae este valor y asígnalo a la variable `title`."""
from pathlib import Path
import json
import plotly.express as px

# Leer los datos como una cadena y convertirlos en un objeto de Python
path = Path('Descargando Datos/data1/eq_data_1_day_m1.geojson')
contenido = path.read_text()
todos_los_datos_terremotos = json.loads(contenido)

# Obtener los diccionarios de todos los terremotos
todos_los_dicc_terremotos = todos_los_datos_terremotos['features']

# Inicializar listas para almacenar magnitudes, longitudes y latitudes
magnitudes, longitudes, latitudes = [], [], []

# Extraer datos
for dicc_terremoto in todos_los_dicc_terremotos:
    magnitudes.append(dicc_terremoto['properties']['mag'])
    longitudes.append(dicc_terremoto['geometry']['coordinates'][0])
    latitudes.append(dicc_terremoto['geometry']['coordinates'][1])

# Extraer el título de los metadatos
titulo = todos_los_datos_terremotos['metadata']['title']

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