import requests

def obtener_repositorios_populares():
    """
    Llama a la API de GitHub para obtener los repositorios de Python más populares
    y muestra información básica de los primeros 5 repositorios.
    """
    try:
        # URL de la API de GitHub para obtener repositorios populares en Python
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        headers = {"Accept": "application/vnd.github.v3+json"}
        
        # Realizar la solicitud a la API
        r = requests.get(url, headers=headers)

        # Verificar el código de estado de la respuesta
        print(f"Código de estado: {r.status_code}")
        if r.status_code == 200:
            # Procesar la respuesta si es exitosa
            response_dict = r.json()
            num_repos = len(response_dict['items'])
            print(f"Número de repositorios encontrados: {num_repos}")
            
            # Mostrar la información de los primeros 5 repositorios
            print("\nTop 5 repositorios de Python por estrellas:")
            for repo in response_dict['items'][:5]:
                print(f"\nNombre del repositorio: {repo['name']}")
                print(f"Estrellas: {repo['stargazers_count']}")
                print(f"URL: {repo['html_url']}")
        else:
            print("Error en la llamada a la API.")
    
    except Exception as e:
        # Capturar cualquier error que ocurra durante la ejecución
        print(f"Ocurrió un error: {e}")

# Llamar a la función para obtener repositorios populares
obtener_repositorios_populares()
