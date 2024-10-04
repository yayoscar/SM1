"""El bucle que extrae datos de `all_eq_dicts` utiliza variables para la magnitud, longitud, latitud y
 el título de cada terremoto antes de agregar estos valores a sus listas correspondientes. 
 Este enfoque fue elegido para mayor claridad sobre cómo extraer datos de un archivo GeoJSON, 
 pero no es necesario en tu código. En lugar de usar estas variables temporales, extrae cada valor de `eq_dict` 
 y agrégalo a la lista correspondiente en una sola línea.
 Hacer esto debería reducir el cuerpo de este bucle a solo cuatro líneas."""
from pathlib import Path
import json 
import plotly.express as px

#Explorar la estructura de los datos-Esto da la ruta del archivo
path=Path('SM1/Descargando Datos/data1/eq_data_1_day_m1.geojson')

#Abrimos este archivo gracias a la ruta
contenido=path.read_text()
todos_los_datos_eq=json.loads(contenido)

#Examinar todos los terremotos en el conjunto de datos
dicc_terremotos=todos_los_datos_eq["features"]
magnitudes,longitudes,latitudes,titulos_terremotos=[],[],[],[]
magnitudes = [dicc_terremoto["properties"]["mag"] for dicc_terremoto in dicc_terremotos]
longitudes = [dicc_terremoto["geometry"]["coordinates"][0] for dicc_terremoto in dicc_terremotos]
latitudes = [dicc_terremoto["geometry"]["coordinates"][1] for dicc_terremoto in dicc_terremotos]
titulos_terremotos = [dicc_terremoto["properties"]["title"] [3]for dicc_terremoto in dicc_terremotos]

titulo="Mapa de Terremotos"
fig=px.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    size=magnitudes,
    title=titulo,
    color=magnitudes,
    color_continuous_scale='Viridis',
    labels={"color":"Magnitud"},
    projection="natural earth",
    hover_name=titulos_terremotos
)
fig.show()
