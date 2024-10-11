import time
import requests
import plotly.express as px
from operator import itemgetter
import plotly.io as pio

# Configurar el renderer para Visual Studio.
pio.renderers.default = 'browser'

def fetch_with_retries(url, retries=3, delay=5, timeout=30):
    """
    Realiza una solicitud HTTP a la URL con un número definido de reintentos
    en caso de fallos de conexión.
    """
    for i in range(retries):
        try:
            r = requests.get(url, timeout=timeout)
            r.raise_for_status()  # Verifica si la respuesta es exitosa
            return r
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Reintentando ({i + 1}/{retries}) en {delay} segundos...")
            time.sleep(delay)
    print(f"Error permanente al conectar con la URL: {url}")
    return None

# Llamada a la API de Hacker News para obtener las historias principales
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = fetch_with_retries(url)

# Verificación de la respuesta de la API
if not response:
    print("No se pudo obtener la lista de historias principales.")
    exit()

# Procesar información de cada historia (top 10)
submission_ids = response.json()
submission_dicts = []

for submission_id in submission_ids[:10]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = fetch_with_retries(url)

    if not r:
        print(f"Publicación omitida: {submission_id}")
        continue

    print(f"id: {submission_id}\tstatus: {r.status_code}")

    try:
        response_dict = r.json()

        # Diccionario con la información de cada historia
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict.get('descendants', 0),  # Comentarios
            'score': response_dict.get('score', 0),           # Puntuación
            'author': response_dict.get('by', 'N/A')          # Autor
        }
        submission_dicts.append(submission_dict)

    except KeyError:
        print(f"Error al procesar la publicación: {submission_id}")

# Ordenar las historias por número de comentarios de mayor a menor
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Preparar los datos para el gráfico
titles = [f"<a href='{item['hn_link']}'>{item['title']}</a>" for item in submission_dicts]
comments = [item['comments'] for item in submission_dicts]
scores = [item['score'] for item in submission_dicts]

# Crear la visualización en un gráfico de barras
title = "Top 10 Discusiones Más Activas en Hacker News"
labels = {'x': 'Publicación', 'y': 'Número de comentarios'}

fig = px.bar(
    x=titles, 
    y=comments, 
    title=title, 
    labels=labels, 
    hover_name=titles
)

# Personalizar el estilo del gráfico
fig.update_traces(
    marker_color='royalblue', 
    marker_line_color='black', 
    marker_line_width=1.5
)

# Ajustes de layout (presentación visual)
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    xaxis_tickangle=-45,  # Inclinar las etiquetas del eje X
    yaxis=dict(
        title=dict(font=dict(size=18)),
        tickfont=dict(size=16)
    ),
    template='plotly_white',  # Estilo de gráfico claro
    annotations=[
        dict(
            x=titles[i],
            y=comments[i],
            text=f"Score: {scores[i]}<br>Autor: {submission_dicts[i]['author']}",
            showarrow=True,
            arrowhead=1
        ) for i in range(len(titles))
    ]
)

# Mostrar el gráfico
fig.show()
