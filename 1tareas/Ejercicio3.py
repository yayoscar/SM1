import pytest
import requests

# URL de la API de GitHub para obtener repositorios de Python.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# Función para obtener los datos de la API
def get_api_data(url):
    response = requests.get(url)
    return response

# Prueba para asegurar que el código de estado sea 200.
def test_status_code():
    response = get_api_data(url)
    assert response.status_code == 200, "La API no respondió con el código de estado 200."

# Prueba para asegurar que se devuelvan al menos 1000 repositorios.
def test_total_repositories():
    response = get_api_data(url)
    response_dict = response.json()
    assert response_dict['total_count'] > 1000, "El número total de repositorios de Python debería ser mayor que 1000."

# Prueba para asegurar que se devuelvan al menos 30 repositorios (por defecto devuelve 30).
def test_items_length():
    response = get_api_data(url)
    response_dict = response.json()
    assert len(response_dict['items']) == 30, "El número de repositorios devueltos no es 30."
