""" En python_repos.py , imprimimos el valor de status_code para asegurarnos de que la llamada a 
la API fue exitosa. Escribe un programa llamado pytest para afirmar que el valor de 
test_python_repos.py que use status_code es 200. Piensa en algunas otras afirmaciones que puedas 
hacer, por ejemplo, que la cantidad de elementos devueltos es la esperada y que el número total 
de repositorios es mayor que una cierta cantidad. """

import requests

def test_python_repos():
    # Realizar una llamada a la API y verificar la respuesta.
    url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r=requests.get(url, headers=headers)

    # Verificamos que nos marque el codigo 200
    assert r.status_code==200
    print(f"Código de estado: {r.status_code}")

    # Convertir el objeto de respuesta a un diccionario.
    response_dict = r.json()

    # Verificar el total de repositorios
    total_count=response_dict['total_count']
    assert total_count>0
    print=("El total de repos debe ser mayor a 0")

    # Verificar que los elementos se devuelven
    repo_dicts=response_dict['items']
    assert len(repo_dicts)>0
    print("Deben haber repositorios que han sido devueltos")

    # Verificamos que la cantidad de repos sea mayor que 10,000
    assert total_count>10000 
    print("El numero total de repos debe ser mayor a los 10,000")