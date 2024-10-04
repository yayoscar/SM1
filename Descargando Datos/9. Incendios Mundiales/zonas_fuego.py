
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
archivo_incendios =('Descargando Datos/data/world_fires_1_day.csv')
datos_incendios = pd.read_csv(archivo_incendios)

# Asegurarnos de que la columna 'brightness' sea de tipo numérico y eliminar NaN
datos_incendios["brightness"] = pd.to_numeric(datos_incendios["brightness"], errors='coerce')
datos_incendios = datos_incendios.dropna(subset=["brightness"])  # Eliminar filas con valores NaN en 'brightness'

# Extraer latitud, longitud y brillo de los incendios
latitudes = datos_incendios["latitude"]
longitudes = datos_incendios["longitude"]
brillo = datos_incendios["brightness"]

# Crear el gráfico de dispersión geográfico usando Plotly
titulo = "Mapa de incendios en el mundo (1 día)"
fig = px.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    size=brillo,
    title=titulo,
    color=brillo,
    color_continuous_scale='YlOrRd',  # Escala de colores adecuada para el brillo
    labels={"color": "Brillo"},
    hover_name=brillo,
    projection="natural earth"
)

# Mostrar el gráfico
fig.show()
