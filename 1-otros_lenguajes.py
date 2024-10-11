"""Modifica la llamada a la API en python_repos.py para que genere un gráfico que muestre 
los proyectos más populares en otros lenguajes. Prueba lenguajes como JavaScript, Ruby, C, 
Java, Perl, Haskell y Go."""

import requests
import matplotlib.pyplot as plt

# Hacemos una lista de los lenguajes 
lenguajes=["JavaScript", "Ruby", "C", "Java", "Perl", "Haskell", "Go"]

# Almacenamos los datos en un repo
repos_count={}

# Realizar una llamada a la API y verificar la respuesta.
for lenguaje in lenguajes:
    url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r=requests.get(url, headers=headers)

    print(f"Código de estado para {lenguaje}: {r.status_code}")

    if r.status_code==200:
        # Convertir el objeto de respuesta a un diccionario.
        response_dict = r.json()
        repos_count[lenguaje]=response_dict['total_count']
        print(f"Total de los repositorios para {lenguaje}: {repos_count[lenguaje]}")
    else:
        print(f"No se obtuvieron los datos para el lenguaje {lenguaje}.")

# Creamos una grafica para poder mostrar los proyectos
plt.figure(figsize=(10, 10))
plt.bar(repos_count.keys(), repos_count.values(), color='pink')
plt.title("Los proyectos más populares de otros lenguajes de programación")
plt.xlabel("Lenguajes de programación")
plt.ylabel("Total de repositorios")

# Mostramos la grafica
plt.show()