import requests
import plotly.express as px

def obtener_repositorios_destacados(idioma):
    url = f"https://api.github.com/search/repositories?q=language:{idioma}+sort:stars+stars:>10000"
    encabezados = {"Accept": "application/vnd.github.v3+json"}
    respuesta = requests.get(url, headers=encabezados)
    print(f"Código de estado para {idioma}: {respuesta.status_code}")

    if respuesta.status_code != 200:
        print(f"Error al obtener repositorios para {idioma}")
        return

    datos_json = respuesta.json()
    print(f"Resultados completos para {idioma}: {not datos_json['incomplete_results']}")

    repositorios_info = datos_json['items']
    enlaces_repositorios, estrellas, descripciones_hover = [], [], []
    
    for repo in repositorios_info:
        nombre_repo = repo['name']
        url_repo = repo['html_url']
        enlace_repo = f"<a href='{url_repo}'>{nombre_repo}</a>"
        enlaces_repositorios.append(enlace_repo)
        estrellas.append(repo['stargazers_count'])
        descripciones_hover.append(repo['description'] or "Sin descripción")

    titulo = f"Proyectos de {idioma} con Más Estrellas en GitHub"
    etiquetas = {'x': 'Repositorio', 'y': 'Estrellas'}
    grafico = px.bar(x=enlaces_repositorios, y=estrellas, title=titulo, labels=etiquetas, hover_name=descripciones_hover)
    grafico.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
    grafico.show()

lista_idiomas = ["JavaScript", "Ruby", "C", "Java", "Perl", "Haskell", "Go"]

for idioma in lista_idiomas:
    obtener_repositorios_destacados(idioma)
