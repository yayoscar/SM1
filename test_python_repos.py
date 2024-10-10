import requests
import pytest

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

def test_api_response():
   
    r = requests.get(url, headers=headers)

    # Afirmar que el código de estado es 200
    assert r.status_code == 200, f"Se esperaba 200, pero se obtuvo {r.status_code}"

    # Convertir la respuesta a un diccionario
    response_dict = r.json()

    # Afirmar que el total de repositorios devueltos es mayor que 0
    assert response_dict['total_count'] > 0, "Se esperaba al menos un repositorio."

    # Afirmar que la respuesta no es incompleta
    assert not response_dict['incomplete_results'], "Los resultados son incompletos."

    # Afirmar que la cantidad de elementos devueltos es mayor que un valor esperado
    expected_min_repos = 10  
    assert len(response_dict['items']) >= expected_min_repos, f"Se esperaban al menos {expected_min_repos} repositorios, pero se obtuvieron {len(response_dict['items'])}."

    # Afirmar que el número total de repositorios es mayor que un umbral ajustado
    min_total_repos = 500 
    assert response_dict['total_count'] > min_total_repos, f"Se esperaban más de {min_total_repos} repositorios en total."

if __name__ == "__main__":
    pytest.main()
