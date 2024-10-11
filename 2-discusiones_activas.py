""" Usando los datos de hn_submissions.py , crea un gráfico de barras que muestre las 
discusiones más activas que están ocurriendo actualmente en Hacker News. La altura de 
cada barra debe corresponder al número de comentarios que tiene cada publicación. La 
etiqueta de cada barra debe incluir el título de la publicación y actuar como un enlace a la 
página de discusión de esa publicación. Si obtienes un KeyError al crear un gráfico, utiliza 
un bloque try-except para omitir las publicaciones promocionales. """

from operator import itemgetter
import requests
import matplotlib.pyplot as plt

# Realizar una llamada a la API y verificar la respuesta.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Código de estado: {r.status_code}")
 
# Procesar información sobre cada publicación.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:5]:
    # Realizar una nueva llamada a la API para cada publicación.
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
        print(f"Se omitió la publicacion con el id {submission_id} por un KeyError")
 
# Ordenamos los artículos por el número de comentarios.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Crear el grafico para su visualizacion
titles = [submission['title'] for submission in submission_dicts]
comments = [submission['comments'] for submission in submission_dicts]

plt.figure(figsize=(10, 6))
bars = plt.barh(titles, comments, color='pink')

# Agregamos etiquetas para las barras y saber de que trata
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{int(bar.get_width())}', va='center')

plt.title('Lo más activas en hacker news')
plt.xlabel('Total de comentarios')
plt.ylabel('Título de la publicación')
plt.tight_layout()

# Mostrar el gráfico
plt.show()
