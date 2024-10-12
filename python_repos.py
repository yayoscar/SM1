import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Código de estado: {r.status_code}")


response_dict = r.json()
 

print(f"Total de repositorios: {response_dict['total_count']}")
print(f"Resultados completos: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repositorios devueltos: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print("\nInformación seleccionada sobre cada repositorio:")
for repo_dict in repo_dicts:
    print(f"\nNombre: {repo_dict['name']}")
    print(f"Propietario: {repo_dict['owner']['login']}")
    print(f"Estrellas: {repo_dict['stargazers_count']}")
    print(f"Repositorio: {repo_dict['html_url']}")
    print(f"Descripción: {repo_dict['description']}")