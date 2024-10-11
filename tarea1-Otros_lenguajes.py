import requests
import plotly.express as px

def obtener_repositorios_populares(lenguaje):
    # Llamada a la API de GitHub para obtener repositorios populares en un lenguaje específico
    url = f"https://api.github.com/search/repositories?q=language:{lenguaje}+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    
    # Verifica el código de estado de la solicitud
    print(f"Código de estado para {lenguaje}: {r.status_code}")

    # Si la llamada no fue exitosa, muestra un mensaje de error
    if r.status_code != 200:
        print(f"Error al obtener repositorios para {lenguaje}")
        return

    # Obtiene los resultados en formato JSON
    response_dict = r.json()
    print(f"Resultados completos para {lenguaje}: {not response_dict['incomplete_results']}")

    # Extrae la información de los repositorios
    repo_dicts = response_dict['items']
    repo_links, stars, hover_texts = [], [], []

    for repo_dict in repo_dicts:
        # Crea enlaces activos con el nombre del repositorio
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])
        hover_texts.append(repo_dict['description'] or "Sin descripción")

    # Configura el título y las etiquetas del gráfico
    title = f"Top {lenguaje} Projects on GitHub by Stars"
    labels = {'x': 'Repository', 'y': 'Stars'}

    # Crea el gráfico de barras
    fig = px.bar(
        x=repo_links, 
        y=stars, 
        title=title, 
        labels=labels, 
        hover_name=hover_texts
    )

    # Personaliza el diseño del gráfico
    fig.update_layout(
        title_font_size=28,
        title_font_family="Arial",
        xaxis_title_font_size=20,
        yaxis_title_font_size=20,
        xaxis_tickfont=dict(size=14, color="black"),
        yaxis_tickfont=dict(size=14, color="black"),
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
        paper_bgcolor='rgba(245, 245, 245, 1)',  # Fondo del lienzo
        hoverlabel=dict(font_size=12, font_family="Arial")
    )

    # Ajusta las barras
    fig.update_traces(
        marker_color='SteelBlue', 
        marker_opacity=0.7
    )

    # Muestra el gráfico
    fig.show()

# Lista de lenguajes a probar
lenguajes = ["JavaScript", "Ruby", "C", "Java", "Perl", "Haskell", "Go"]

# Llama a la función para cada lenguaje
for lenguaje in lenguajes:
    obtener_repositorios_populares(lenguaje)
