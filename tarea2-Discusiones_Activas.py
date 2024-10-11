import requests
from operator import itemgetter
import plotly.express as px

# Llamada a la API de Hacker News para obtener las historias principales
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

# Verificar el código de estado de la respuesta
if r.status_code != 200:
    print("Error al obtener las historias principales.")
    exit()

# Procesar información sobre cada historia
submission_ids = r.json()
submission_dicts = []

# Limitar a las 10 principales historias
for submission_id in submission_ids[:10]:
    # Llamada a la API para cada historia individual
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)

    if r.status_code != 200:
        print(f"Historia omitida: {submission_id}, código de estado: {r.status_code}")
        continue

    try:
        response_dict = r.json()

        # Crear un diccionario para almacenar información de cada historia
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict.get('descendants', 0),  # Número de comentarios
        }
        submission_dicts.append(submission_dict)

    except KeyError:
        print(f"Historia omitida por KeyError: {submission_id}")

# Ordenar las historias por el número de comentarios de forma descendente
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Preparar los datos para el gráfico
titles = [f"<a href='{item['hn_link']}'>{item['title']}</a>" for item in submission_dicts]
comments = [item['comments'] for item in submission_dicts]

# Crear el gráfico de barras
fig = px.bar(
    x=titles, 
    y=comments, 
    title="Top 10 Most Active Discussions on Hacker News",
    labels={'x': 'Post', 'y': 'Number of Comments'},
    hover_name=titles
)

# Personalización del gráfico de barras
fig.update_layout(
    title_font_size=28,
    title_font_family="Arial",
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    xaxis_tickfont=dict(size=14, color="black"),
    yaxis_tickfont=dict(size=14, color="black"),
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
    paper_bgcolor='rgba(245, 245, 245, 1)',  # Lienzo claro
    hoverlabel=dict(font_size=12, font_family="Arial")
)

# Ajustar el color y opacidad de las barras
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.7)

# Mostrar el gráfico
fig.show()
