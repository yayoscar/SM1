import time
import requests
import plotly.express as px
from operator import itemgetter
import plotly.io as pio

#here we need configurar renderer para Visual Studio.
pio.renderers.default='browser'

def fetch_with_retries(url, retries=3, delay=5, timeout=30):
    """Realiza una solicitud a la URL con reintentos."""
    for i in range(retries):
        try:
            r=requests.get(url, timeout=timeout)
            r.raise_for_status()
            return r
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Reintentando ({i + 1}/{retries}) en {delay} segundos...")
            time.sleep(delay)
    print(f"Error permanente al conectar con la URL: {url}")
    return None

#then we relizamos una llamada a la API para obtener las historias principales.
url="https://hacker-news.firebaseio.com/v0/topstories.json"
response = fetch_with_retries(url)

if not response:
    print("No se pudo obtener la lista de historias principales.")
    exit()

#after  información sobre cada publicación.
submission_ids = response.json()
submission_dicts=[]
for submission_id in submission_ids[:10]:  # Limitar a las 10 discusiones más activas
    url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=fetch_with_retries(url)

    if not r:
        print(f"Publicación omitida: {submission_id}")
        continue

    print(f"id: {submission_id}\tstatus: {r.status_code}")

    try:
        response_dict=r.json()
        submission_dict={
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict.get('descendants', 0),
            'score': response_dict.get('score', 0),  # Añadir puntuación
            'author': response_dict.get('by', 'N/A')  # Añadir autor
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        print(f"Error al procesar la publicación: {submission_id}")

#then ordenamos los artículos por número de comentarios.
submission_dicts=sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

#creamo listas para el gráfico.
titles=[f"<a href='{item['hn_link']}'>{item['title']}</a>" for item in submission_dicts]
comments=[item['comments'] for item in submission_dicts]
scores=[item['score'] for item in submission_dicts]  # Puntuaciones

#visualización.
title="Discusiones más activas en Hacker News"
labels={'x': 'Publicación', 'y': 'Número de comentarios'}
fig=px.bar(x=titles, y=comments, title=title, labels=labels, hover_name=titles)

#if you want we can personalozar el estilo del gráfico
fig.update_traces(marker_color='royalblue', marker_line_color='black', marker_line_width=1.5)
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    xaxis_tickangle=-45,
    yaxis=dict(
        title=dict(font=dict(size=18)),
        tickfont=dict(size=16)
    ),
    template='plotly_white',
    annotations=[
        dict(
            x=titles[i],
            y=comments[i],
            text=f"Score: {scores[i]}<br>Author: {submission_dicts[i]['author']}",
            showarrow=True,
            arrowhead=1
        ) for i in range(len(titles))
    ]
)

#finally we show the gráfico
fig.show()
