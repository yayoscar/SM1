import requests
import plotly.express as px

lenguajes=["JavaScript"]

def obtener_repositorios_populares(lenguaje):
    url=f"https://api.github.com/search/repositories?q=language:{lenguaje}+sort:stars+stars:>10000"
    headers={"Accept": "application/vnd.github.v3+json"}
    r=requests.get(url, headers=headers)
    print(f"Código de estado para {lenguaje}: {r.status_code}")

    
    if r.status_code!=200:
        print(f"Error al obtener repositorios para {lenguaje}")
        return

   
    response_dict=r.json()
    print(f"Resultados completos para {lenguaje}: {not response_dict['incomplete_results']}")

   
    repo_dicts=response_dict['items']
    repo_links,stars,hover_texts = [],[],[]
    
    for repo_dict in repo_dicts:
        repo_name=repo_dict['name']
        repo_url=repo_dict['html_url']
        repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])
        hover_texts.append(repo_dict['description'] or "Sin descripción")

    title=f"Proyectos de {lenguaje} con Más Estrellas en GitHub"
    labels={'x': 'Repositorio', 'y': 'Estrellas'}
    fig=px.bar(x=repo_links,y=stars,title=title,labels=labels,hover_name=hover_texts)
    fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)
    fig.show()
    
for lenguaje in lenguajes:
    obtener_repositorios_populares(lenguaje)
