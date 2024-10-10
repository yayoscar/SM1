import requests
from operator import itemgetter
import plotly.graph_objs as go

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Código de estado: {r.status_code}")

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:  
    
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
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

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles = [sub['title'] for sub in submission_dicts]
comments = [sub['comments'] for sub in submission_dicts]
links = [sub['hn_link'] for sub in submission_dicts]

fig = go.Figure(go.Bar(x=titles, y=comments))
fig.update_layout(
    title='Discusiones más activas en Hacker News',
    xaxis_title='Título de la Publicación',
    yaxis_title='Número de Comentarios'
)
fig.show()
