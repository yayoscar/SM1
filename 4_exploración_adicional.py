import requests
import plotly.express as px
import pandas as pd

# Hacer una solicitud a la API de Hacker News para obtener los IDs de las historias más populares
response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
top_story_ids = response.json()[:10]  # Obtener las 10 historias más populares

# Lista para almacenar los detalles de las historias
stories = []

# Obtener los detalles de cada historia utilizando su ID
for story_id in top_story_ids:
    story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
    story_data = story_response.json()
    stories.append({
        'title': story_data.get('title'),
        'score': story_data.get('score', 0),  # Obtener la puntuación o 0 si no está disponible
        'url': story_data.get('url')  # Obtener la URL del artículo
    })

# Crear un DataFrame con la información de las historias
df = pd.DataFrame(stories)

# Crear un gráfico de barras con Plotly Express
fig = px.bar(df, x='title', y='score', title='Top 10 Historias en Hacker News', text='score')

# Personalizar la apariencia del gráfico
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(
    title='Puntuación de las Historias Más Populares en Hacker News',
    xaxis_title='Historia',
    yaxis_title='Puntuación',
    xaxis_tickangle=-45  # Girar los títulos de las historias para mejor visibilidad
)

# Mostrar el gráfico
fig.show()
