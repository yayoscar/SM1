import time
import requests
import plotly.express as px
from operator import itemgetter
import plotly.io as pio

# Configurar renderer para Visual Studio.
pio.renderers.default = 'browser'

# Definir una función para manejar los reintentos.
def fetch_with_retries(url, retries=3, delay=5, timeout=30):
    """Realiza una solicitud a la URL con reintentos."""
    for i in range(retries):
        try:
            r = requests.get(url, timeout=timeout)
            r.raise_for_status()
            return r
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Reintentando ({i + 1}/{retries}) en {delay} segundos...")
            time.sleep(delay)
    print(f"Error permanente al conectar con la URL: {url}")
    return None

# Realizar una llamada a la API para obtener las historias principales.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = fetch_with_retries(url)

if not response:
    print("No se pudo obtener la lista de historias principales.")
    exit()

# Procesar información sobre cada publicación.
submission_ids = response.json()
submission_dicts = []
for submission_id in submission_ids[:10]:  # Limitar a las 10 discusiones más activas
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = fetch_with_retries(url)

    if not r:
        print(f"Publicación omitida: {submission_id}")
        continue

    print(f"id: {submission_id}\tstatus: {r.status_code}")

    try:
        response_dict = r.json()
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict.get('descendants', 0),
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        print(f"Error al procesar la publicación: {submission_id}")

# Ordenar los artículos por número de comentarios.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Crear listas para el gráfico.
titles = [f"<a href='{item['hn_link']}'>{item['title']}</a>" for item in submission_dicts]
comments = [item['comments'] for item in submission_dicts]

# Crear visualización.
title = "Discusiones más activas en Hacker News"
labels = {'x': 'Publicación', 'y': 'Número de comentarios'}
fig = px.bar(x=titles, y=comments, title=title, labels=labels, hover_name=titles)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

# Mostrar gráfico
fig.show()
