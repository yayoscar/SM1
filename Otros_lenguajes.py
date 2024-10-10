# Primero importamos el módulo requests
import requests

import plotly.express as px

# Realizar una llamada a la API y verificar la respuesta.
url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>10000" #JAVASCRIPT

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
print(f"Total de repositorios: {response_dict['total_count']}")
print(f"Resultados completos: {not response_dict['incomplete_results']}")

# Explorar información sobre los repositorios.
repo_dicts = response_dict['items']
print(f"Repositorios devueltos: {len(repo_dicts)}")

print("\nInformación seleccionada sobre cada repositorio:")
for repo_dict in repo_dicts:
    print(f"\nNombre: {repo_dict['name']}")
    print(f"Propietario: {repo_dict['owner']['login']}")
    print(f"Estrellas: {repo_dict['stargazers_count']}")
    print(f"Repositorio: {repo_dict['html_url']}")
    print(f"Descripción: {repo_dict['description']}")   


repo_names = [repo_dict['name'] for repo_dict in repo_dicts]
repo_stars = [repo_dict['stargazers_count'] for repo_dict in repo_dicts]

fig = px.bar(
    x=repo_names,
    y=repo_stars,
    labels={"x": "Repositorio", "y": "Estrellas"},
    title="Proyectos más populares en GitHub en JavaScript"
)

fig.show()