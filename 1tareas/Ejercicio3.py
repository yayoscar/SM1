import requests
import plotly.express as px

# Realizar una llamada a la API y verificar la respuesta.
url = "https://api.github.com/search/repositories"
url += "?q=language: python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Código de estado: {r.status_code}")

# Procesar los resultados generales.
response_dict = r.json()
print(f"Resultados completos: {not response_dict['incomplete_results']}")

# Procesar información de los repositorios.
repo_dicts = response_dict['items']
repo_names, stars = [],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Crear visualización.
fig = px.bar (x=repo_names, y=stars)
fig.show()