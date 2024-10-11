import requests
import plotly.express as px

# Llamada a la API de GitHub para obtener repositorios de Python con más de 10,000 estrellas
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

# Verifica el estado de la respuesta
print(f"Código de estado de la solicitud: {r.status_code}")

# Obtiene los resultados de la respuesta en formato JSON
response_dict = r.json()
print(f"Resultados completos: {not response_dict['incomplete_results']}")

# Procesa la información de los repositorios
repo_dicts = response_dict['items']
repo_links, stars = [], []
for repo_dict in repo_dicts:
    # Genera enlaces activos con el nombre del repositorio
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

# Título y etiquetas del gráfico
title = "Top Python Repositories on GitHub by Stars"
labels = {'x': 'Repository', 'y': 'Stars'}

# Crea la visualización del gráfico de barras
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels)

# Actualiza el estilo del gráfico
fig.update_layout(
    title_font_size=28, 
    title_font_family="Arial",
    xaxis_title_font_size=20, 
    yaxis_title_font_size=20,
    xaxis_tickfont=dict(size=14, color="black"),
    yaxis_tickfont=dict(size=14, color="black"),
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
    paper_bgcolor='rgba(245, 245, 245, 1)',  # Fondo del lienzo
)

# Personaliza las barras
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.7)

# Muestra el gráfico
fig.show()

