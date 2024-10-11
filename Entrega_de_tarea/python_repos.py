import requests

url_api = "https://api.github.com/search/repositories"
url_api += "?q=language:python+sort:stars+stars:>10000"
cabeceras = {"Accept": "application/vnd.github.v3+json"}
respuesta = requests.get(url_api, headers=cabeceras)
print(f"Código de estado: {respuesta.status_code}")

resultado_json = respuesta.json()

print(f"Total de repositorios: {resultado_json['total_count']}")
print(f"Resultados completos: {not resultado_json['incomplete_results']}")

repositorios = resultado_json['items']
print(f"Repositorios devueltos: {len(repositorios)}")

print("\nInformación seleccionada sobre cada repositorio:")
for repo in repositorios:
    print(f"\nNombre: {repo['name']}")
    print(f"Propietario: {repo['owner']['login']}")
    print(f"Estrellas: {repo['stargazers_count']}")
    print(f"Repositorio: {repo['html_url']}")
    print(f"Descripción: {repo['description']}")
