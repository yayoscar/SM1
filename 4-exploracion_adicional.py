"""Visita la documentación de Plotly y de la API de GitHub o de la API de Hacker News. Usa algo 
de la información que encuentres allí para personalizar el estilo de los gráficos que ya hemos 
hecho o para obtener información diferente y crear tus propias visualizaciones. Si tienes 
curiosidad por explorar otras APIs, echa un vistazo a las APIs mencionadas en el repositorio 
de GitHub en 
https://github.com/public-apis"""

import pandas as pd
import requests
import json
from operator import itemgetter
import plotly.express as px

def fetch_article(article_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{article_id}.json"
    r = requests.get(url)
    print(f"Código de estado para artículo {article_id}: {r.status_code}")
    if r.status_code == 200:
        response_dict = r.json()
        response_string = json.dumps(response_dict, indent=4)
        print(response_string)
    else:
        print(f"No se pudo obtener el artículo {article_id}.")

def fetch_top_stories(limit=5):
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url)
    print(f"Código de estado para historias principales: {r.status_code}")
    
    if r.status_code == 200:
        submission_ids = r.json()
        submission_dicts = []
        
        for submission_id in submission_ids[:limit]:
            url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
            r = requests.get(url)
            print(f"id: {submission_id}\tstatus: {r.status_code}")
            
            if r.status_code == 200:
                response_dict = r.json()
                try:
                    submission_dict = {
                        'title': response_dict['title'],
                        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
                        'comments': response_dict.get('descendants', 0),
                    }
                    submission_dicts.append(submission_dict)
                except KeyError:
                    continue  # Omite la iteración si falta alguna clave

        # Ordenar los artículos por número de comentarios.
        submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

        # Imprimir información sobre los artículos principales.
        for submission_dict in submission_dicts:
            print(f"\nTítulo: {submission_dict['title']}")
            print(f"Enlace a la discusión: {submission_dict['hn_link']}")
            print(f"Comentarios: {submission_dict['comments']}")

        # Creamos un Data Frame usando pandas para que podamos hacer la visualizacion con plotly
        df=pd.DataFrame(submission_dicts)

        # Visualización usando Plotly
        fig=px.bar(df, x='title', y='comments', 
                     title='Tops de Hacker News',
                     labels={'title': 'Título', 'comments': 'Numero de comentarios total'},
                     color='comments', color_continuous_scale=px.colors.sequential.Viridis)

        fig.update_layout(xaxis_title='Título', yaxis_title='Número de Comentarios')
        fig.show()
        
    else:
        print("No se pudieron obtener las historias principales")

if __name__=="__main__":
    fetch_article(31353677)  
    fetch_top_stories()
