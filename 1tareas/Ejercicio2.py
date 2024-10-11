import requests
import plotly.express as px
from operator import itemgetter

# Realizar una llamada a la API para obtener los IDs de las publicaciones principales
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

if r.status_code == 200:
    submission_ids = r.json()
    submission_dicts = []

    # Obtener detalles de las 10 publicaciones más comentadas
    for submission_id in submission_ids[:10]:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
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
                continue

    # Ordenar las publicaciones por el número de comentarios
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    # Preparar datos para el gráfico
    titles = [f"<a href='{item['hn_link']}'>{item['title']}</a>" for item in submission_dicts]
    comments = [item['comments'] for item in submission_dicts]

    # Crear la visualización
    fig = px.bar(x=titles, y=comments, labels={'x': 'Publicación', 'y': 'Comentarios'},
                title='Discusiones Más Activas en Hacker News')
    fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
    fig.show()
else:
    print("Error al recuperar los datos de Hacker News")