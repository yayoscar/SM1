import json
from pathlib import Path
import plotly.express as px

nombre_archivo = Path('SM1/Descargando Datos/data/teremotos_7dias_atras.geojson')
contenido = nombre_archivo.read_text()
todos_datos = json.loads(contenido)

# Examinar todos los terremotos a partir de la clave 'features'
Terremotos_dic = todos_datos["features"]

# Extraer los datos en un bucle reducido a cuatro líneas
magnitudes = [dicc_terremoto["properties"]["mag"] for dicc_terremoto in Terremotos_dic]
longitudes = [dicc_terremoto["geometry"]["coordinates"][0] for dicc_terremoto in Terremotos_dic]
latitudes = [dicc_terremoto["geometry"]["coordinates"][1] for dicc_terremoto in Terremotos_dic]
titulos_terremotos = [dicc_terremoto["properties"]["title"] for dicc_terremoto in Terremotos_dic]

# Crear y mostrar el mapa
titulo = "Mapa de terremotos"
fig = px.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    size=magnitudes,
    title=titulo,
    color=magnitudes,
    color_continuous_scale='Viridis',
    labels={"color": "Magnitud"},
    hover_name=titulos_terremotos,
    projection="natural earth"
)
fig.show()
