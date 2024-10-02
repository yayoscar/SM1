""" En los recursos para este capítulo, encontrarás un archivo llamado `world_fires_1_day.csv`. 
Este archivo contiene información sobre incendios que arden en diferentes ubicaciones alrededor del mundo,
incluyendo la latitud, longitud y el brillo de cada incendio. Usando el procesamiento de datos de la primera
parte de este capítulo y el trabajo de mapeo de esta sección, crea un mapa que muestre qué partes del mundo 
están afectadas por incendios.Puedes descargar versiones más recientes de estos datos en 
[https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data]
(https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data). 
Puedes encontrar enlaces a los datos en formato CSV en la sección *SHP, KML, and TXT Files*."""
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
archivo_incendios = 'SM1/Descargando Datos/data1/world_fires_1_day.csv'
datos_incendios = pd.read_csv(archivo_incendios)

# Inspeccionar las primeras filas del DataFrame
print(datos_incendios.head())

# Crear el mapa
fig = px.scatter_geo(
    datos_incendios,
    lat='latitude',
    lon='longitude',
    size='brightness',  # Puedes ajustar el tamaño basado en la intensidad del incendio
    title='Incendios Mundiales Recientes',
    color='brightness',  # Colorear según la intensidad del incendio
    color_continuous_scale='Reds',
    labels={'brightness': 'Brillo'},
    projection='natural earth',
)

fig.show()