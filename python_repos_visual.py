# Primero importamos el módulo requests
import requests

import plotly.express as px
# Realizar una llamada a la API y verificar la respuesta.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
#definimos encabezados para la llamada a la API que piden explícitamente utilizar;
# esta versión de la API y devolver los resultados en formato JSON.
headers = {"Accept": "application/vnd.github.v3+json"}

#Luego usamos requests para hacer la llamada a la API. Llamamos a 
#get() y le pasamos la URL y el encabezado que definimos, y asignamos el 
# objeto de respuesta a la variable r

r = requests.get(url, headers=headers)

#Imprimimos el valor de status_code para asegurarnos de que la llamada 
# se realizó correctamente.
print(f"Código de estado: {r.status_code}")

# Convertir el objeto de respuesta a un diccionario.
response_dict = r.json()

# Imprimir el total de repositorios y si los resultados están completos.
print(f"Resultados completos: {not response_dict['incomplete_results']}")

# Procesar información de los repositorios.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Convertir nombres de repositorios en enlaces activos.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # Construir textos de tooltip.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Crear visualización.
title = "Proyectos de Python con Más Estrellas en GitHub"
labels = {'x': 'Repositorio', 'y': 'Estrellas'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, 
hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show() 