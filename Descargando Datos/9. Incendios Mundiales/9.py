import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


archivo_incendios = 'Descargando Datos\data\world_fires_1_day.csv' 
datos_incendios = pd.read_csv(archivo_incendios)


gdf_incendios = gpd.GeoDataFrame(
    datos_incendios, 
    geometry=gpd.points_from_xy(datos_incendios.longitude, datos_incendios.latitude))


mapa_mundial = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

fig, ax = plt.subplots(figsize=(15, 10))
mapa_mundial.plot(ax=ax, color='lightgray')


gdf_incendios.plot(ax=ax, markersize=1, color='red', alpha=0.5)

plt.title('Mapa de Incendios Mundiales')
plt.show()
