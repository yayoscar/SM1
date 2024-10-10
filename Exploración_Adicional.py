import requests
import plotly.express as px
import pandas as pd


response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
top_story_ids = response.json()[:10] 

stories = []
for story_id in top_story_ids:
    story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
    story_data = story_response.json()
    stories.append({
        'title': story_data.get('title'),
        'score': story_data.get('score', 0),
        'url': story_data.get('url')
    })


df = pd.DataFrame(stories)


fig = px.bar(df, x='title', y='score', title='Top 10 Historias en Hacker News', text='score')


fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(
    title='Puntuación de las Historias Más Populares en Hacker News',
)

fig.update_xaxes(title='Historia', title_font=dict(size=18))
fig.update_yaxes(title='Puntuación', title_font=dict(size=18))

fig.update_layout(xaxis_tickangle=-45)


fig.show()
