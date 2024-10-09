import requests
import plotly.express as px
import numpy as np

# Realizar una llamada a la API y verificar la respuesta.
url = "https://api.github.com/search/repositories"
url += "?q=language:haskell+sort:stars+stars:>1000"

headers = {"Accept": "application/vnd.github.v3+json"}  # Encabezado: solo acepto la versión 3 de la API en formato JSON
r = requests.get(url, headers=headers)

print(f"Código de estado: {r.status_code}")

# Convertir el objeto de respuesta a un diccionario.
response_dict = r.json()

# Imprimir el total de repositorios y si los resultados están completos.
print(f"Total de repositorios: {response_dict['total_count']}")
print(f"Resultados completos: {not response_dict['incomplete_results']}")

# Explorar información sobre los repositorios.
repo_dicts = response_dict['items']
print(f"Repositorios devueltos: {len(repo_dicts)}")

repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    # Convertir nombres de repositorios en enlaces activos.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # Construir textos de tooltip
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Crear el gráfico de barras con gradiente
title = 'Proyectos de Haskell con más de 1,000 estrellas en GitHub'
labels = {'x': 'Repositorio', 'y': 'Estrellas'}

# Crear una lista de colores basados en los valores de estrellas usando una escala de colores
colors = np.array(stars)

haskell_gradient = [
    [0.0, "#5e5086"],  # Color inicial del logo de Haskell
    [0.33, "#66CDAA"], # Verde intermedio 1
    [0.66, "#77DD77"], # Verde intermedio 2
    [1.0, "#98FB98"]   # Verde pálido
]


fig = px.bar(
    x=repo_links, 
    y=stars, 
    title=title, 
    labels=labels,
    hover_name=hover_texts,
    color=colors,  # Asigna los colores basados en la lista de estrellas
    color_continuous_scale=haskell_gradient)

# Personalizar la apariencia del gráfico
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()
