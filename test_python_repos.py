"""En python_repos.py , imprimimos el valor de status_code para asegurarnos de que la
llamada a la API fue exitosa. Escribe un programa llamado test_python_repos.py que use 
pytest para afirmar que el valor de status_code es 200. Piensa en algunas otras
afirmaciones que puedas hacer, por ejemplo, que la cantidad de elementos devueltos es la
esperada y que el número total de repositorios es mayor que una cierta cantidad.
"""

import requests
import pytest 

# Realizar una llamada a la API y verificar la respuesta.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
assert r.status_code==200
print(f"Código de estado: {r.status_code}")

# Convertir el objeto de respuesta a un diccionario.
response_dict = r.json()

# Explorar información sobre los repositorios.
repo_dicts = response_dict['items']
assert len(repo_dicts)>0
print("Han sido devueltos más de 0") 

# Imprimir el total de repositorios y si los resultados están completos.
total_count=response_dict['total_count']
assert total_count>0
print("Repositorios mayores a la cantidad esperada")
print(f"Resultados completos: {not response_dict['incomplete_results']}")


print("\nInformación seleccionada sobre cada repositorio:")
for repo_dict in repo_dicts:
    print(f"\nNombre: {repo_dict['name']}")
    print(f"Propietario: {repo_dict['owner']['login']}")
    print(f"Estrellas: {repo_dict['stargazers_count']}")
    print(f"Repositorio: {repo_dict['html_url']}")
    print(f"Descripción: {repo_dict['description']}")


