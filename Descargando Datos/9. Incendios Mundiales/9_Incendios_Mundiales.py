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

archivo_incendios = 'Descargando Datos/data1/world_fires_1_day.csv'
datos_incendios = pd.read_csv(archivo_incendios)

print(datos_incendios.head())

fig = px.scatter_geo(
    datos_incendios,
    lat='latitude',
    lon='longitude',
    size='brightness',  
    title='Incendios Mundiales Recientes',
    color='brightness',  
    color_continuous_scale='Reds',
    labels={'brightness': 'Brillo'},
    projection='natural earth',
)

fig.show()