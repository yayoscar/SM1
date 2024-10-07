import requests
import plotly.express as px

def obtener_repositorios_populares(lenguaje):
    #Aca tenemos que eealizar una llamada a la API para obtener los repositorios populares en el lenguaje especificado
    url=f"https://api.github.com/search/repositories?q=language:{lenguaje}+sort:stars+stars:>10000"
    headers={"Accept": "application/vnd.github.v3+json"}
    r=requests.get(url, headers=headers)
    print(f"Código de estado para {lenguaje}:{r.status_code}")

    #Here we need procesar los resultados generales.
    response_dict=r.json()
    print(f"Resultados completos: {not response_dict['incomplete_results']}")

    #Procesamos la información de los repositorios.
    repo_dicts=response_dict['items']
    repo_links,star=[], []
    for repo_dict in repo_dicts:
        #aqui ocupamos convertir nombres de repositorios en enlaces activos.
        repo_name=repo_dict['name']
        repo_url=repo_dict['html_url']
        repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])

    #Creamos visualización ne.
    title=f"Proyectos de {lenguaje} con Más Estrellas en GitHub"
    labels={'x': 'Repositorio', 'y': 'Estrellas'}
    fig=px.bar(x=repo_links, y=stars, title=title, labels=labels)
    fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
    fig.show()

#aqui ne ponemos para diferentes lenguajes
for lenguaje in ['JavaScript', 'Ruby', 'C', 'Java', 'Perl', 'Haskell', 'Go']:
    obtener_repositorios_populares(lenguaje)

#by andy sulub and jaime diaz