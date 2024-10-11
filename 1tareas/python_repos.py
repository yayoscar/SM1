import requests
import plotly.express as px

# Realizar una llamada a la API y verificar la respuesta.
url = "https://api.github.com/search/repositories"
params = {
    'q': 'language:python stars:>10000',  # Parametros de búsqueda
    'sort': 'stars',
    'order': 'desc'
}
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers, params=params)
print(f"Código de estado: {r.status_code}")

# Asegurarse de que la solicitud se haya realizado correctamente
if r.status_code == 200:
    response_dict = r.json()
    print(f"Resultados completos: {not response_dict['incomplete_results']}")

    # Procesar información de los repositorios.
    repo_dicts = response_dict['items']
    repo_names, stars = [], []
    for repo_dict in repo_dicts:
        repo_names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])

    # Crear visualización.
    fig = px.bar(x=repo_names, y=stars, labels={'x': 'Repositorio', 'y': 'Estrellas'},
                title='Proyectos de Python con Más Estrellas en GitHub')
    fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
    fig.show()
else:
    print("Error al hacer la solicitud a la API.")
