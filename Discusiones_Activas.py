import requests
from operator import itemgetter
import plotly.express as px

# Realizar una llamada a la API y verificar la respuesta.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

# Verificar el código de estado
if r.status_code != 200:
    print("Error al obtener las historias principales.")
    exit()

# Procesar información sobre cada publicación.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:10]:  # Limitar a las 10 historias
    #Crear Una llamada a la API para cada publicación.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)

    if r.status_code != 200:
        print(f"Publicación omitida: {submission_id}, código de estado: {r.status_code}")
        continue

    try:
        response_dict = r.json()

        # Crear un diccionario para obtener cada artículo.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict.get('descendants', 0),
        }
        submission_dicts.append(submission_dict)

    except KeyError:
        print(f"Publicación omitida por KeyError: {submission_id}")

# Ordenar los artículos por número de comentarios.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

#Obtener las listas para el gráfico.
titles = [f"<a href='{item['hn_link']}'>{item['title']}</a>" for item in submission_dicts]
comments = [item['comments'] for item in submission_dicts]

# Crear el gráfico de barras.
fig = px.bar(x=titles, y=comments, title="Discusiones más activas en Hacker News",
             labels={'x': 'Publicación', 'y': 'Número de comentarios'}, hover_name=titles)

# Personalizacion del gráfico barras.
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

# Obtener El Resultado :D profe.
fig.show()

# Limberth :D