
from operator import itemgetter
import requests
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Código de estado: {r.status_code}")
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTítulo: {submission_dict['title']}")
    print(f"Enlace a la discusión: {submission_dict['hn_link']}")
    print(f"Comentarios: {submission_dict['comments']}")