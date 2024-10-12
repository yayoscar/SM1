import requests

def obtener_repositorios_populares():
    try:
        # Llamar a la API de GitHub para obtener los repositorios populares en Python.
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        headers = {"Accept": "application/vnd.github.v3+json"}
        r = requests.get(url, headers=headers)

        # Verificar Si La llamada Fue Correcta.
        print(f"Código de estado: {r.status_code}")
        if r.status_code == 200:
            # Obtener la respuesta Si Es Correcta.
            response_dict = r.json()
            print(f"Número de repositorios: {len(response_dict['items'])}")
            
            # Obtener La Info básica De Cada Repositorio.
            for repo in response_dict['items'][:5]:  # Solo los primeros 5
                print(f"\nNombre: {repo['name']}")
                print(f"Estrellas: {repo['stargazers_count']}")
                print(f"URL: {repo['html_url']}")
        else:
            print("Error en la llamada a la API")
    except Exception as e:
        # Crear Una Capturar Cualquier Error Que Ocurra Durante La Ejecucion.
        print(f"Ocurrió un error: {e}")

# Crear Una Llamar a la función para Obtener repositorios populares.
obtener_repositorios_populares()