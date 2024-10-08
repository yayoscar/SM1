import requests
import plotly.express as px

#una llamada a la API y verificar la respuesta.
url="https://api.github.com/search/repositories"
url+="?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Código de estado: {r.status_code}")

#los resultados generales.
response_dict = r.json()
print(f"Resultados completos: {not response_dict['incomplete_results']}")

#Procesa información de los repositorios.
repo_dicts=response_dict['items']
repo_links, stars=[], []
for repo_dict in repo_dicts:
    #nombres de repositorios en enlaces activos.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

#creamos visualización.
title="Proyectos de Python con Más Estrellas en GitHub"
labels={'x': 'Repositorio', 'y': 'Estrellas'}
fig=px.bar(x=repo_links, y=stars, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()