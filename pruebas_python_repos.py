import requests

def obtener_repositorios_populares():
    try:
        #aca llamamos a la API de GitHub para obtener los repositorios populares en Python.
        url="https://api.github.com/search/repositories?q=language:python&sort=stars"
        headers={"Accept": "application/vnd.github.v3+json"}
        r=requests.get(url, headers=headers)

        #Verificar si la llamada fue exitosa.
        print(f"Código de estado:{r.status_code}")
        if r.status_code==200:
            #Procesar la respuesta si es exitosa.
            response_dict = r.json()
            print(f"Número de repositorios: {len(response_dict['items'])}")
            
            #here nene mostramos información básica de cada repositorio.
            for repo in response_dict['items'][:5]: #pero solo los primeros 5
                print(f"\nNombre: {repo['name']}")
                print(f"Estrellas: {repo['stargazers_count']}")
                print(f"URL: {repo['html_url']}")
        else:
            print("Error en la llamada a la API")
    except Exception as e:
        #aqui ocupamos capturar cualquier error que ocurra durante la ejecución.
        print(f"Ocurrió un error: {e}")

#para llamar a la función para obtener repositorios populares.
obtener_repositorios_populares()
