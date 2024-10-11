import requests

# Prueba para verificar que el código de estado de la API es 200.
def test_status_code():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    response = requests.get(url)
    assert response.status_code == 200

# Prueba para verificar que la API devuelve más de 1000 repositorios de Python.
def test_total_repositories():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    response = requests.get(url)
    response_dict = response.json()
    assert response_dict['total_count'] > 1000
